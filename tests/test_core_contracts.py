from decimal import Decimal

import pytest
from drmlke_core.identity import (
    INITIAL_USER_PROFILES,
    ActorMetadata,
    Capability,
    Role,
    UserId,
    UserProfile,
    capabilities_for_role,
    is_capability_globally_locked,
)
from drmlke_core.ledger import (
    LedgerEntry,
    LedgerEntryId,
    LedgerEntryType,
    LedgerSequence,
    append_paper_ledger_entry,
    create_initial_paper_ledger,
    project_paper_cash_balance_eur,
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


def _actor(role: Role = Role.OWNER_OPERATOR, user_id: str = "francesco") -> ActorMetadata:
    return UserProfile(UserId(user_id), role, user_id.title()).actor_metadata()


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


def test_initial_paper_ledger_creates_one_200_eur_initial_capital_entry() -> None:
    ledger = create_initial_paper_ledger(_actor())

    assert len(ledger.entries) == 1
    entry = ledger.entries[0]
    assert entry.entry_type is LedgerEntryType.PAPER_INITIAL_CAPITAL
    assert entry.amount_eur == Decimal("200.00")
    assert entry.sequence == LedgerSequence(1)
    assert ledger.treasury.initial_capital_eur == PAPER_TREASURY_INITIAL_CAPITAL_EUR
    assert ledger.treasury.live_capital_eur == LIVE_CAPITAL_EUR


def test_paper_ledger_balance_projection_starts_at_200_eur() -> None:
    ledger = create_initial_paper_ledger(_actor())

    assert project_paper_cash_balance_eur(ledger) == Decimal("200.00")


def test_owner_operator_can_append_valid_adjustment_entry() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("owner-adjustment-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(2),
        entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
        amount_eur=Decimal("10.00"),
        actor=actor,
        reason="Paper-only adjustment test",
    )

    next_ledger = append_paper_ledger_entry(ledger, entry, actor)

    assert next_ledger is not ledger
    assert len(ledger.entries) == 1
    assert len(next_ledger.entries) == 2
    assert project_paper_cash_balance_eur(next_ledger) == Decimal("210.00")


def test_viewer_family_cannot_append_ledger_entries() -> None:
    owner = _actor()
    viewer = _actor(Role.VIEWER_FAMILY, "padre")
    ledger = create_initial_paper_ledger(owner)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("viewer-adjustment-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(2),
        entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
        amount_eur=Decimal("10.00"),
        actor=viewer,
        reason="Viewer should be denied",
    )

    with pytest.raises(PermissionError, match="cannot append"):
        append_paper_ledger_entry(ledger, entry, viewer)


def test_admin_technical_cannot_append_ledger_entries() -> None:
    owner = _actor()
    admin = _actor(Role.ADMIN_TECHNICAL, "admin")
    ledger = create_initial_paper_ledger(owner)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("admin-adjustment-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(2),
        entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
        amount_eur=Decimal("10.00"),
        actor=admin,
        reason="Admin should be denied",
    )

    with pytest.raises(PermissionError, match="cannot append"):
        append_paper_ledger_entry(ledger, entry, admin)


def test_invalid_ledger_treasury_id_is_rejected() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)

    with pytest.raises(ValueError, match="treasury id"):
        LedgerEntry(
            entry_id=LedgerEntryId("wrong-treasury-1"),
            treasury_id="not-the-paper-treasury",
            sequence=LedgerSequence(2),
            entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
            amount_eur=Decimal("10.00"),
            actor=actor,
            reason="Wrong treasury",
        )

    assert project_paper_cash_balance_eur(ledger) == Decimal("200.00")


def test_wrong_ledger_sequence_is_rejected() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("wrong-sequence-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(3),
        entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
        amount_eur=Decimal("10.00"),
        actor=actor,
        reason="Wrong sequence",
    )

    with pytest.raises(ValueError, match="next append-only sequence"):
        append_paper_ledger_entry(ledger, entry, actor)


def test_duplicate_initial_capital_entry_is_rejected() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("duplicate-initial-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(2),
        entry_type=LedgerEntryType.PAPER_INITIAL_CAPITAL,
        amount_eur=Decimal("200.00"),
        actor=actor,
        reason="Duplicate initial capital",
    )

    with pytest.raises(ValueError, match="initial capital cannot be appended"):
        append_paper_ledger_entry(ledger, entry, actor)


def test_zero_amount_ledger_entry_is_rejected() -> None:
    actor = _actor()

    with pytest.raises(ValueError, match="cannot be zero"):
        LedgerEntry(
            entry_id=LedgerEntryId("zero-entry-1"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            sequence=LedgerSequence(2),
            entry_type=LedgerEntryType.PAPER_CASH_ADJUSTMENT,
            amount_eur=Decimal("0.00"),
            actor=actor,
            reason="Zero amount",
        )


def test_correction_entry_changes_balance_by_appending_without_mutating_original() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    correction = LedgerEntry(
        entry_id=LedgerEntryId("correction-1"),
        treasury_id=ledger.treasury.treasury_id,
        sequence=LedgerSequence(2),
        entry_type=LedgerEntryType.PAPER_CORRECTION,
        amount_eur=Decimal("-5.00"),
        actor=actor,
        reason="Paper correction",
    )

    corrected = append_paper_ledger_entry(ledger, correction, actor)

    assert corrected is not ledger
    assert tuple(ledger.entries) == ledger.entries
    assert len(ledger.entries) == 1
    assert len(corrected.entries) == 2
    assert project_paper_cash_balance_eur(ledger) == Decimal("200.00")
    assert project_paper_cash_balance_eur(corrected) == Decimal("195.00")
