from decimal import Decimal

import pytest
from drmlke_core.identity import (
    INITIAL_USER_PROFILES,
    Capability,
    Role,
    UserId,
    UserProfile,
    capabilities_for_role,
    is_capability_globally_locked,
)
from drmlke_core.safety import (
    DEFAULT_GLOBAL_SAFETY_LOCKS,
    GlobalSafetyLocks,
    assert_bootstrap_safety,
)
from drmlke_core.treasury import (
    DEFAULT_PAPER_TREASURY_BOUNDARY,
    LIVE_CAPITAL_EUR,
    PAPER_TREASURY_INITIAL_CAPITAL_EUR,
    TreasuryMode,
    validate_single_paper_treasury,
)


def test_owner_has_expected_operator_capabilities() -> None:
    capabilities = capabilities_for_role(Role.OWNER_OPERATOR)

    expected = {
        Capability.VIEW_TREASURY,
        Capability.VIEW_POSITIONS,
        Capability.VIEW_PNL,
        Capability.VIEW_RUNTIME_STATUS,
        Capability.VIEW_SIGNALS,
        Capability.VIEW_NEWS,
        Capability.VIEW_ALERTS,
        Capability.VIEW_AUDIT_SUMMARY,
        Capability.MANAGE_RUNTIME,
        Capability.PAUSE_RUNTIME,
        Capability.RESUME_RUNTIME,
        Capability.EMERGENCY_STOP,
        Capability.MANAGE_STRATEGIES,
        Capability.MANAGE_RISK_POLICY,
        Capability.APPROVE_PAPER_ACTION,
        Capability.MANAGE_DEVICES,
        Capability.MANAGE_USERS,
        Capability.VIEW_SENSITIVE_LOGS,
    }

    assert expected <= capabilities
    assert Capability.APPROVE_FUTURE_LIVE_ACTION not in capabilities
    assert Capability.MANAGE_EXCHANGE_CONNECTIONS not in capabilities


def test_viewer_family_cannot_mutate_treasury_runtime_or_risk() -> None:
    viewer = UserProfile(UserId("padre"), Role.VIEWER_FAMILY, "Padre")

    forbidden = {
        Capability.MANAGE_RUNTIME,
        Capability.PAUSE_RUNTIME,
        Capability.RESUME_RUNTIME,
        Capability.MANAGE_STRATEGIES,
        Capability.MANAGE_RISK_POLICY,
        Capability.APPROVE_PAPER_ACTION,
        Capability.APPROVE_FUTURE_LIVE_ACTION,
        Capability.MANAGE_DEVICES,
        Capability.MANAGE_USERS,
        Capability.MANAGE_EXCHANGE_CONNECTIONS,
        Capability.VIEW_SENSITIVE_LOGS,
    }

    assert viewer.capabilities.isdisjoint(forbidden)
    assert not viewer.has_capability(Capability.APPROVE_PAPER_ACTION)
    assert not viewer.has_capability(Capability.APPROVE_FUTURE_LIVE_ACTION)


def test_viewer_family_cannot_gain_mutating_authority_through_overrides() -> None:
    viewer = UserProfile(
        UserId("padre"),
        Role.VIEWER_FAMILY,
        "Padre",
        capability_overrides=frozenset(
            {
                Capability.MANAGE_RUNTIME,
                Capability.MANAGE_STRATEGIES,
                Capability.MANAGE_RISK_POLICY,
                Capability.APPROVE_PAPER_ACTION,
                Capability.MANAGE_USERS,
            }
        ),
    )

    assert Capability.MANAGE_RUNTIME not in viewer.capabilities
    assert Capability.MANAGE_STRATEGIES not in viewer.capabilities
    assert Capability.MANAGE_RISK_POLICY not in viewer.capabilities
    assert Capability.APPROVE_PAPER_ACTION not in viewer.capabilities
    assert Capability.MANAGE_USERS not in viewer.capabilities


def test_globally_locked_capabilities_cannot_be_granted_through_overrides() -> None:
    owner = UserProfile(
        UserId("francesco"),
        Role.OWNER_OPERATOR,
        "Francesco",
        capability_overrides=frozenset(
            {
                Capability.APPROVE_FUTURE_LIVE_ACTION,
                Capability.MANAGE_EXCHANGE_CONNECTIONS,
            }
        ),
    )

    assert Capability.APPROVE_FUTURE_LIVE_ACTION not in owner.capabilities
    assert Capability.MANAGE_EXCHANGE_CONNECTIONS not in owner.capabilities


def test_live_and_exchange_capabilities_remain_globally_locked() -> None:
    locked = {
        Capability.APPROVE_FUTURE_LIVE_ACTION,
        Capability.MANAGE_EXCHANGE_CONNECTIONS,
    }

    for capability in locked:
        assert is_capability_globally_locked(capability)

    for role in Role:
        capabilities = capabilities_for_role(role)
        assert capabilities.isdisjoint(locked)


def test_admin_technical_has_no_trading_authority_by_default() -> None:
    capabilities = capabilities_for_role(Role.ADMIN_TECHNICAL)

    trading_authority = {
        Capability.MANAGE_STRATEGIES,
        Capability.MANAGE_RISK_POLICY,
        Capability.APPROVE_PAPER_ACTION,
        Capability.APPROVE_FUTURE_LIVE_ACTION,
        Capability.MANAGE_EXCHANGE_CONNECTIONS,
    }

    assert capabilities.isdisjoint(trading_authority)
    assert Capability.VIEW_SENSITIVE_LOGS in capabilities


def test_initial_family_profiles_match_correct_account_model() -> None:
    profiles = {profile.display_name: profile for profile in INITIAL_USER_PROFILES}

    assert profiles["Francesco"].role is Role.OWNER_OPERATOR
    assert profiles["Padre"].role is Role.VIEWER_FAMILY
    assert profiles["Zio"].role is Role.VIEWER_FAMILY


def test_global_safety_locks_disable_forbidden_runtime_behavior() -> None:
    locks = DEFAULT_GLOBAL_SAFETY_LOCKS

    assert locks.is_bootstrap_safe()
    assert not locks.live_trading_enabled
    assert not locks.withdrawals_enabled
    assert not locks.wallet_custody_enabled
    assert not locks.exchange_credentials_enabled
    assert not locks.model_execution_can_override_risk
    assert not locks.ui_locks_are_security_boundary
    assert locks.server_side_enforcement_required
    assert_bootstrap_safety(locks)


def test_unsafe_global_safety_locks_fail_fast() -> None:
    locks = GlobalSafetyLocks(live_trading_enabled=True)

    with pytest.raises(ValueError, match="live trading enabled"):
        assert_bootstrap_safety(locks)


def test_paper_treasury_boundary_is_exactly_one_200_eur_treasury() -> None:
    treasury = validate_single_paper_treasury([DEFAULT_PAPER_TREASURY_BOUNDARY])

    assert treasury.mode is TreasuryMode.PAPER
    assert treasury.one_treasury_only
    assert not treasury.per_person_portfolios_enabled
    assert treasury.initial_capital_eur == Decimal("200.00")
    assert treasury.initial_capital_eur == PAPER_TREASURY_INITIAL_CAPITAL_EUR
    assert treasury.live_capital_eur == Decimal("0.00")
    assert treasury.live_capital_eur == LIVE_CAPITAL_EUR
    assert treasury.can_role_manage(Role.OWNER_OPERATOR)
    assert not treasury.can_role_manage(Role.VIEWER_FAMILY)
    assert treasury.can_role_view(Role.VIEWER_FAMILY)


def test_multiple_paper_treasuries_are_rejected() -> None:
    with pytest.raises(ValueError, match="exactly one paper treasury"):
        validate_single_paper_treasury(
            [
                DEFAULT_PAPER_TREASURY_BOUNDARY,
                DEFAULT_PAPER_TREASURY_BOUNDARY,
            ]
        )
