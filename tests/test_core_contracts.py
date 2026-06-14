from dataclasses import FrozenInstanceError, fields
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
    PaperLedger,
    append_paper_ledger_entry,
    create_initial_paper_ledger,
    project_paper_cash_balance_eur,
)
from drmlke_core.portfolio import (
    calculate_open_cost_basis_ratio,
    is_paper_portfolio_snapshot_reconciled,
    project_paper_portfolio_snapshot,
)
from drmlke_core.position import (
    INITIAL_PAPER_POSITION_ASSETS,
    AssetSymbol,
    PaperPosition,
    PaperPositionBook,
    PaperPositionId,
    PaperPositionSide,
    PaperPositionStatus,
    closed_paper_positions,
    create_open_paper_position,
    is_initial_paper_position_asset,
    normalize_asset_symbol,
    open_paper_positions,
    total_open_cost_basis_eur,
    total_position_fees_eur,
    validate_initial_paper_position_asset,
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
from drmlke_core.treasury_projection import (
    PaperTreasurySnapshot,
    is_paper_treasury_snapshot_reconciled,
    project_paper_treasury_snapshot,
)


def _actor(role: Role = Role.OWNER_OPERATOR, user_id: str = "francesco") -> ActorMetadata:
    return UserProfile(UserId(user_id), role, user_id.title()).actor_metadata()


def _ledger_entry(
    entry_id: str,
    sequence: int,
    entry_type: LedgerEntryType,
    amount_eur: Decimal,
    actor: ActorMetadata,
) -> LedgerEntry:
    return LedgerEntry(
        entry_id=LedgerEntryId(entry_id),
        treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
        sequence=LedgerSequence(sequence),
        entry_type=entry_type,
        amount_eur=amount_eur,
        actor=actor,
        reason=f"Test entry {entry_id}",
    )


def _append_entry(
    ledger: PaperLedger,
    entry_id: str,
    entry_type: LedgerEntryType,
    amount_eur: Decimal,
    actor: ActorMetadata,
) -> PaperLedger:
    entry = _ledger_entry(
        entry_id,
        len(ledger.entries) + 1,
        entry_type,
        amount_eur,
        actor,
    )
    return append_paper_ledger_entry(ledger, entry, actor)


def _unsafe_ledger_entry(
    entry_id: str,
    sequence: int,
    entry_type: LedgerEntryType,
    amount_eur: Decimal,
    actor: ActorMetadata,
) -> LedgerEntry:
    entry = object.__new__(LedgerEntry)
    object.__setattr__(entry, "entry_id", LedgerEntryId(entry_id))
    object.__setattr__(entry, "treasury_id", DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id)
    object.__setattr__(entry, "sequence", LedgerSequence(sequence))
    object.__setattr__(entry, "entry_type", entry_type)
    object.__setattr__(entry, "amount_eur", amount_eur)
    object.__setattr__(entry, "actor", actor)
    object.__setattr__(entry, "reason", f"Unsafe test entry {entry_id}")
    object.__setattr__(entry, "reference", None)
    return entry


def _valid_paper_position(
    position_id: str = "paper-position-1",
    asset: str = "BTC",
) -> PaperPosition:
    return create_open_paper_position(
        position_id=PaperPositionId(position_id),
        asset=asset,
        quantity=Decimal("0.01"),
        average_entry_price_eur=Decimal("30000.00"),
        fees_eur=Decimal("1.00"),
        reference="decision-1",
    )


def _unsafe_paper_position(
    *,
    position_id: str = "unsafe-position-1",
    treasury_id: str = DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
    asset: str = "BTC",
    side: object = PaperPositionSide.LONG,
    status: PaperPositionStatus = PaperPositionStatus.OPEN,
    quantity: Decimal = Decimal("0.01"),
    average_entry_price_eur: Decimal = Decimal("30000.00"),
    cost_basis_eur: Decimal = Decimal("301.00"),
    fees_eur: Decimal = Decimal("1.00"),
    paper_only: bool = True,
    live_backed: bool = False,
) -> PaperPosition:
    position = object.__new__(PaperPosition)
    object.__setattr__(position, "position_id", PaperPositionId(position_id))
    object.__setattr__(position, "treasury_id", treasury_id)
    object.__setattr__(position, "asset", AssetSymbol(asset))
    object.__setattr__(position, "side", side)
    object.__setattr__(position, "status", status)
    object.__setattr__(position, "quantity", quantity)
    object.__setattr__(position, "average_entry_price_eur", average_entry_price_eur)
    object.__setattr__(position, "cost_basis_eur", cost_basis_eur)
    object.__setattr__(position, "fees_eur", fees_eur)
    object.__setattr__(position, "paper_only", paper_only)
    object.__setattr__(position, "live_backed", live_backed)
    object.__setattr__(position, "reference", None)
    return position


def _initial_treasury_snapshot() -> PaperTreasurySnapshot:
    return project_paper_treasury_snapshot(create_initial_paper_ledger(_actor()))


def _unsafe_position_book(
    *,
    treasury_id: str = DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
    positions: tuple[PaperPosition, ...] = (),
) -> PaperPositionBook:
    book = object.__new__(PaperPositionBook)
    object.__setattr__(book, "treasury_id", treasury_id)
    object.__setattr__(book, "positions", positions)
    return book


def _unsafe_treasury_snapshot(
    source: PaperTreasurySnapshot,
    *,
    reconciled: bool,
) -> PaperTreasurySnapshot:
    snapshot = object.__new__(PaperTreasurySnapshot)
    for field in fields(source):
        object.__setattr__(snapshot, field.name, getattr(source, field.name))
    object.__setattr__(snapshot, "reconciled", reconciled)
    return snapshot


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


def test_initial_paper_treasury_snapshot_projects_cash_state() -> None:
    ledger = create_initial_paper_ledger(_actor())

    snapshot = project_paper_treasury_snapshot(ledger)

    assert snapshot.treasury_id == DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id
    assert snapshot.mode is TreasuryMode.PAPER
    assert snapshot.initial_capital_eur == Decimal("200.00")
    assert snapshot.live_capital_eur == Decimal("0.00")
    assert snapshot.ledger_entry_count == 1
    assert snapshot.last_sequence == 1
    assert snapshot.available_cash_eur == Decimal("200.00")
    assert snapshot.reserved_cash_eur == Decimal("0.00")
    assert snapshot.total_cash_eur == Decimal("200.00")
    assert snapshot.total_fees_eur == Decimal("0.00")
    assert snapshot.net_adjustments_eur == Decimal("0.00")
    assert snapshot.net_corrections_eur == Decimal("0.00")
    assert snapshot.paper_only
    assert snapshot.live_capital_locked
    assert snapshot.reconciled
    assert is_paper_treasury_snapshot_reconciled(snapshot)


def test_paper_fee_projection_reduces_available_cash_and_records_positive_cost() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    ledger = _append_entry(
        ledger,
        "fee-1",
        LedgerEntryType.PAPER_FEE,
        Decimal("-1.25"),
        actor,
    )

    snapshot = project_paper_treasury_snapshot(ledger)

    assert snapshot.available_cash_eur == Decimal("198.75")
    assert snapshot.reserved_cash_eur == Decimal("0.00")
    assert snapshot.total_cash_eur == Decimal("198.75")
    assert snapshot.total_fees_eur == Decimal("1.25")
    assert snapshot.reconciled


def test_paper_reserved_cash_projection_moves_available_to_reserved() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    ledger = _append_entry(
        ledger,
        "reserve-1",
        LedgerEntryType.PAPER_RESERVED_CASH,
        Decimal("-50.00"),
        actor,
    )

    snapshot = project_paper_treasury_snapshot(ledger)

    assert snapshot.available_cash_eur == Decimal("150.00")
    assert snapshot.reserved_cash_eur == Decimal("50.00")
    assert snapshot.total_cash_eur == Decimal("200.00")
    assert snapshot.reconciled


def test_paper_released_cash_projection_moves_reserved_to_available() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    ledger = _append_entry(
        ledger,
        "reserve-1",
        LedgerEntryType.PAPER_RESERVED_CASH,
        Decimal("-50.00"),
        actor,
    )
    ledger = _append_entry(
        ledger,
        "release-1",
        LedgerEntryType.PAPER_RELEASED_CASH,
        Decimal("20.00"),
        actor,
    )

    snapshot = project_paper_treasury_snapshot(ledger)

    assert snapshot.available_cash_eur == Decimal("170.00")
    assert snapshot.reserved_cash_eur == Decimal("30.00")
    assert snapshot.total_cash_eur == Decimal("200.00")
    assert snapshot.reconciled


def test_paper_projection_rejects_release_greater_than_reserved_cash() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    ledger = _append_entry(
        ledger,
        "release-1",
        LedgerEntryType.PAPER_RELEASED_CASH,
        Decimal("10.00"),
        actor,
    )

    with pytest.raises(ValueError, match="release cannot exceed reserved cash"):
        project_paper_treasury_snapshot(ledger)


@pytest.mark.parametrize(
    ("entry_type", "amount_eur"),
    [
        (LedgerEntryType.PAPER_CASH_ADJUSTMENT, Decimal("-250.00")),
        (LedgerEntryType.PAPER_CORRECTION, Decimal("-250.00")),
        (LedgerEntryType.PAPER_FEE, Decimal("-250.00")),
        (LedgerEntryType.PAPER_RESERVED_CASH, Decimal("-250.00")),
    ],
)
def test_paper_projection_rejects_entries_that_make_available_cash_negative(
    entry_type: LedgerEntryType,
    amount_eur: Decimal,
) -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    ledger = _append_entry(ledger, "negative-cash-1", entry_type, amount_eur, actor)

    with pytest.raises(ValueError, match="available cash cannot be negative"):
        project_paper_treasury_snapshot(ledger)


def test_paper_projection_rejects_positive_fee_entries() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    corrupted_entry = _unsafe_ledger_entry(
        "positive-fee-1",
        2,
        LedgerEntryType.PAPER_FEE,
        Decimal("1.00"),
        actor,
    )
    corrupted_ledger = PaperLedger(
        treasury=ledger.treasury,
        entries=(ledger.entries[0], corrupted_entry),
    )

    with pytest.raises(ValueError, match="fee entries must be negative"):
        project_paper_treasury_snapshot(corrupted_ledger)


def test_paper_projection_rejects_positive_reserved_cash_entries() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    corrupted_entry = _unsafe_ledger_entry(
        "positive-reserve-1",
        2,
        LedgerEntryType.PAPER_RESERVED_CASH,
        Decimal("10.00"),
        actor,
    )
    corrupted_ledger = PaperLedger(
        treasury=ledger.treasury,
        entries=(ledger.entries[0], corrupted_entry),
    )

    with pytest.raises(ValueError, match="reserved cash entries must be negative"):
        project_paper_treasury_snapshot(corrupted_ledger)


def test_paper_projection_rejects_negative_released_cash_entries() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    corrupted_entry = _unsafe_ledger_entry(
        "negative-release-1",
        2,
        LedgerEntryType.PAPER_RELEASED_CASH,
        Decimal("-10.00"),
        actor,
    )
    corrupted_ledger = PaperLedger(
        treasury=ledger.treasury,
        entries=(ledger.entries[0], corrupted_entry),
    )

    with pytest.raises(ValueError, match="released cash entries must be positive"):
        project_paper_treasury_snapshot(corrupted_ledger)


def test_paper_projection_correction_changes_snapshot_without_mutating_ledger() -> None:
    actor = _actor()
    ledger = create_initial_paper_ledger(actor)
    original_entries = ledger.entries
    corrected = _append_entry(
        ledger,
        "snapshot-correction-1",
        LedgerEntryType.PAPER_CORRECTION,
        Decimal("-5.00"),
        actor,
    )

    snapshot = project_paper_treasury_snapshot(corrected)

    assert ledger.entries == original_entries
    assert len(ledger.entries) == 1
    assert len(corrected.entries) == 2
    assert snapshot.available_cash_eur == Decimal("195.00")
    assert snapshot.net_corrections_eur == Decimal("-5.00")
    assert snapshot.total_cash_eur == Decimal("195.00")


def test_paper_treasury_snapshot_is_immutable() -> None:
    snapshot = project_paper_treasury_snapshot(create_initial_paper_ledger(_actor()))

    with pytest.raises(FrozenInstanceError):
        snapshot.available_cash_eur = Decimal("0.00")


def test_paper_treasury_snapshot_does_not_introduce_positions_or_market_value() -> None:
    snapshot = project_paper_treasury_snapshot(create_initial_paper_ledger(_actor()))
    snapshot_fields = {field.name for field in fields(snapshot)}

    assert "positions" not in snapshot_fields
    assert "asset_balances" not in snapshot_fields
    assert "market_value_eur" not in snapshot_fields
    assert "unrealized_pnl_eur" not in snapshot_fields


def test_paper_projection_does_not_grant_viewer_or_admin_management_path() -> None:
    snapshot = project_paper_treasury_snapshot(create_initial_paper_ledger(_actor()))

    assert not DEFAULT_PAPER_TREASURY_BOUNDARY.can_role_manage(Role.VIEWER_FAMILY)
    assert not DEFAULT_PAPER_TREASURY_BOUNDARY.can_role_manage(Role.ADMIN_TECHNICAL)
    assert not hasattr(snapshot, "capabilities")


def test_asset_symbol_normalization_for_initial_paper_positions() -> None:
    assert normalize_asset_symbol("btc") == AssetSymbol("BTC")
    assert normalize_asset_symbol(" ETH ") == AssetSymbol("ETH")

    with pytest.raises(ValueError, match="required"):
        normalize_asset_symbol("")
    with pytest.raises(ValueError, match="spaces"):
        normalize_asset_symbol("BT C")


def test_initial_paper_position_asset_boundary_is_btc_eth_only() -> None:
    assert INITIAL_PAPER_POSITION_ASSETS == frozenset(
        {AssetSymbol("BTC"), AssetSymbol("ETH")}
    )
    assert is_initial_paper_position_asset(AssetSymbol("BTC"))
    assert is_initial_paper_position_asset(AssetSymbol("ETH"))

    with pytest.raises(ValueError, match="outside the initial BTC/ETH"):
        validate_initial_paper_position_asset(AssetSymbol("DOGE"))
    with pytest.raises(ValueError, match="outside the initial BTC/ETH"):
        validate_initial_paper_position_asset(AssetSymbol("AAPL"))


def test_valid_open_btc_paper_position_uses_canonical_paper_boundary() -> None:
    position = _valid_paper_position()

    assert position.position_id == PaperPositionId("paper-position-1")
    assert position.treasury_id == DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id
    assert position.asset == AssetSymbol("BTC")
    assert position.side is PaperPositionSide.LONG
    assert position.status is PaperPositionStatus.OPEN
    assert position.quantity == Decimal("0.01")
    assert position.average_entry_price_eur == Decimal("30000.00")
    assert position.fees_eur == Decimal("1.00")
    assert position.cost_basis_eur == Decimal("301.0000")
    assert position.paper_only
    assert not position.live_backed
    assert position.reference == "decision-1"


def test_paper_position_wrong_treasury_id_is_rejected() -> None:
    with pytest.raises(ValueError, match="treasury id"):
        PaperPosition(
            position_id=PaperPositionId("wrong-treasury-position"),
            treasury_id="not-the-paper-treasury",
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=Decimal("300.00"),
            fees_eur=Decimal("0.00"),
        )


def test_live_backed_paper_position_is_rejected() -> None:
    with pytest.raises(ValueError, match="live-backed"):
        PaperPosition(
            position_id=PaperPositionId("live-backed-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=Decimal("300.00"),
            fees_eur=Decimal("0.00"),
            live_backed=True,
        )


def test_non_paper_position_is_rejected() -> None:
    with pytest.raises(ValueError, match="paper-only"):
        PaperPosition(
            position_id=PaperPositionId("non-paper-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=Decimal("300.00"),
            fees_eur=Decimal("0.00"),
            paper_only=False,
        )


@pytest.mark.parametrize("quantity", [Decimal("0"), Decimal("-0.01")])
def test_zero_or_negative_paper_position_quantity_is_rejected(quantity: Decimal) -> None:
    with pytest.raises(ValueError, match="quantity must be positive"):
        PaperPosition(
            position_id=PaperPositionId("bad-quantity-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=quantity,
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=Decimal("300.00"),
            fees_eur=Decimal("0.00"),
        )


@pytest.mark.parametrize("price", [Decimal("0"), Decimal("-1.00")])
def test_zero_or_negative_paper_position_entry_price_is_rejected(price: Decimal) -> None:
    with pytest.raises(ValueError, match="average entry price must be positive"):
        PaperPosition(
            position_id=PaperPositionId("bad-price-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=price,
            cost_basis_eur=Decimal("300.00"),
            fees_eur=Decimal("0.00"),
        )


@pytest.mark.parametrize("cost_basis", [Decimal("0"), Decimal("-1.00")])
def test_zero_or_negative_paper_position_cost_basis_is_rejected(
    cost_basis: Decimal,
) -> None:
    with pytest.raises(ValueError, match="cost basis must be positive"):
        PaperPosition(
            position_id=PaperPositionId("bad-cost-basis-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=cost_basis,
            fees_eur=Decimal("0.00"),
        )


def test_paper_position_cost_basis_must_match_quantity_price_plus_fees() -> None:
    with pytest.raises(ValueError, match="quantity \\* price \\+ fees"):
        PaperPosition(
            position_id=PaperPositionId("mismatched-cost-basis-position"),
            treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
            asset=AssetSymbol("BTC"),
            side=PaperPositionSide.LONG,
            status=PaperPositionStatus.OPEN,
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            cost_basis_eur=Decimal("300.01"),
            fees_eur=Decimal("0.00"),
        )


def test_negative_paper_position_fees_are_rejected() -> None:
    with pytest.raises(ValueError, match="fees cannot be negative"):
        create_open_paper_position(
            position_id=PaperPositionId("bad-fees-position"),
            asset="BTC",
            quantity=Decimal("0.01"),
            average_entry_price_eur=Decimal("30000.00"),
            fees_eur=Decimal("-0.01"),
        )


def test_paper_position_is_long_only_in_core3() -> None:
    position = _valid_paper_position()

    assert position.side is PaperPositionSide.LONG
    assert list(PaperPositionSide) == [PaperPositionSide.LONG]
    assert not hasattr(PaperPositionSide, "SHORT")


def test_paper_position_is_frozen() -> None:
    position = _valid_paper_position()

    with pytest.raises(FrozenInstanceError):
        position.quantity = Decimal("0.02")


def test_paper_position_book_rejects_duplicate_position_ids() -> None:
    first = _valid_paper_position(position_id="duplicate-position", asset="BTC")
    second = _valid_paper_position(position_id="duplicate-position", asset="ETH")

    with pytest.raises(ValueError, match="duplicate position ids"):
        PaperPositionBook(positions=(first, second))


def test_paper_position_book_rejects_mixed_treasury_ids() -> None:
    valid_position = _valid_paper_position(position_id="valid-position")
    wrong_treasury_position = _unsafe_paper_position(
        position_id="wrong-treasury-position",
        treasury_id="not-the-paper-treasury",
    )

    with pytest.raises(ValueError, match="treasury id"):
        PaperPositionBook(positions=(valid_position, wrong_treasury_position))


def test_paper_position_book_totals_open_cost_basis_only() -> None:
    open_position = _valid_paper_position(position_id="open-position", asset="BTC")
    closed_position = PaperPosition(
        position_id=PaperPositionId("closed-position"),
        treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
        asset=AssetSymbol("ETH"),
        side=PaperPositionSide.LONG,
        status=PaperPositionStatus.CLOSED,
        quantity=Decimal("0.10"),
        average_entry_price_eur=Decimal("2000.00"),
        cost_basis_eur=Decimal("201.00"),
        fees_eur=Decimal("1.00"),
    )
    book = PaperPositionBook(positions=(open_position, closed_position))

    assert open_paper_positions(book) == (open_position,)
    assert closed_paper_positions(book) == (closed_position,)
    assert total_open_cost_basis_eur(book) == Decimal("301.0000")
    assert total_position_fees_eur(book) == Decimal("2.00")


def test_paper_position_book_has_no_market_valuation_or_pnl_fields() -> None:
    position = _valid_paper_position()
    book = PaperPositionBook(positions=(position,))
    position_fields = {field.name for field in fields(position)}
    book_fields = {field.name for field in fields(book)}

    assert "current_price_eur" not in position_fields
    assert "market_value_eur" not in position_fields
    assert "realized_pnl_eur" not in position_fields
    assert "unrealized_pnl_eur" not in position_fields
    assert "market_value_eur" not in book_fields
    assert "unrealized_pnl_eur" not in book_fields


def test_paper_position_boundary_does_not_grant_viewer_or_admin_authority() -> None:
    position = _valid_paper_position()

    assert not DEFAULT_PAPER_TREASURY_BOUNDARY.can_role_manage(Role.VIEWER_FAMILY)
    assert not DEFAULT_PAPER_TREASURY_BOUNDARY.can_role_manage(Role.ADMIN_TECHNICAL)
    assert not hasattr(position, "capabilities")


def test_empty_paper_portfolio_snapshot_combines_cash_and_empty_position_book() -> None:
    treasury_snapshot = _initial_treasury_snapshot()
    position_book = PaperPositionBook()

    snapshot = project_paper_portfolio_snapshot(treasury_snapshot, position_book)

    assert snapshot.treasury_snapshot is treasury_snapshot
    assert snapshot.position_book is position_book
    assert snapshot.treasury_id == DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id
    assert snapshot.available_cash_eur == Decimal("200.00")
    assert snapshot.reserved_cash_eur == Decimal("0.00")
    assert snapshot.total_cash_eur == Decimal("200.00")
    assert snapshot.open_position_count == 0
    assert snapshot.closed_position_count == 0
    assert snapshot.position_count == 0
    assert snapshot.open_cost_basis_eur == Decimal("0.00")
    assert snapshot.position_fees_eur == Decimal("0.00")
    assert snapshot.total_structural_exposure_eur == Decimal("200.00")
    assert snapshot.open_cost_basis_ratio == Decimal("0")
    assert snapshot.paper_only
    assert snapshot.live_capital_locked
    assert snapshot.reconciled
    assert is_paper_portfolio_snapshot_reconciled(snapshot)


def test_paper_portfolio_snapshot_with_one_open_btc_position() -> None:
    treasury_snapshot = _initial_treasury_snapshot()
    position = create_open_paper_position(
        position_id=PaperPositionId("portfolio-btc-1"),
        asset="BTC",
        quantity=Decimal("0.01"),
        average_entry_price_eur=Decimal("4900.00"),
        fees_eur=Decimal("1.00"),
    )
    position_book = PaperPositionBook(positions=(position,))

    snapshot = project_paper_portfolio_snapshot(treasury_snapshot, position_book)
    snapshot_fields = {field.name for field in fields(snapshot)}

    assert position.cost_basis_eur == Decimal("50.0000")
    assert snapshot.open_position_count == 1
    assert snapshot.closed_position_count == 0
    assert snapshot.open_cost_basis_eur == Decimal("50.0000")
    assert snapshot.open_cost_basis_ratio == Decimal("0.2500")
    assert snapshot.available_cash_eur == Decimal("200.00")
    assert snapshot.total_structural_exposure_eur == Decimal("250.0000")
    assert "current_price_eur" not in snapshot_fields
    assert "market_value_eur" not in snapshot_fields
    assert "unrealized_pnl_eur" not in snapshot_fields


def test_paper_portfolio_snapshot_with_open_and_closed_positions() -> None:
    treasury_snapshot = _initial_treasury_snapshot()
    open_position = create_open_paper_position(
        position_id=PaperPositionId("portfolio-btc-open"),
        asset="BTC",
        quantity=Decimal("0.01"),
        average_entry_price_eur=Decimal("4900.00"),
        fees_eur=Decimal("1.00"),
    )
    closed_position = PaperPosition(
        position_id=PaperPositionId("portfolio-eth-closed"),
        treasury_id=DEFAULT_PAPER_TREASURY_BOUNDARY.treasury_id,
        asset=AssetSymbol("ETH"),
        side=PaperPositionSide.LONG,
        status=PaperPositionStatus.CLOSED,
        quantity=Decimal("0.01"),
        average_entry_price_eur=Decimal("2900.00"),
        cost_basis_eur=Decimal("30.0000"),
        fees_eur=Decimal("1.00"),
    )
    position_book = PaperPositionBook(positions=(open_position, closed_position))

    snapshot = project_paper_portfolio_snapshot(treasury_snapshot, position_book)

    assert snapshot.open_position_count == 1
    assert snapshot.closed_position_count == 1
    assert snapshot.position_count == 2
    assert snapshot.open_cost_basis_eur == Decimal("50.0000")
    assert snapshot.position_fees_eur == Decimal("2.00")
    assert snapshot.total_structural_exposure_eur == Decimal("250.0000")


def test_paper_portfolio_snapshot_rejects_treasury_id_mismatch() -> None:
    treasury_snapshot = _initial_treasury_snapshot()
    position_book = _unsafe_position_book(treasury_id="not-the-paper-treasury")

    with pytest.raises(ValueError, match="treasury id"):
        project_paper_portfolio_snapshot(treasury_snapshot, position_book)


def test_paper_portfolio_snapshot_rejects_live_backed_position_book() -> None:
    treasury_snapshot = _initial_treasury_snapshot()
    live_backed_position = _unsafe_paper_position(
        position_id="portfolio-live-backed",
        live_backed=True,
    )
    position_book = _unsafe_position_book(positions=(live_backed_position,))

    with pytest.raises(ValueError, match="live-backed"):
        project_paper_portfolio_snapshot(treasury_snapshot, position_book)


def test_paper_portfolio_snapshot_rejects_non_reconciled_treasury_snapshot() -> None:
    treasury_snapshot = _unsafe_treasury_snapshot(
        _initial_treasury_snapshot(),
        reconciled=False,
    )

    with pytest.raises(ValueError, match="reconciliation"):
        project_paper_portfolio_snapshot(treasury_snapshot, PaperPositionBook())


def test_paper_portfolio_snapshot_is_frozen() -> None:
    snapshot = project_paper_portfolio_snapshot(
        _initial_treasury_snapshot(),
        PaperPositionBook(),
    )

    with pytest.raises(FrozenInstanceError):
        snapshot.open_position_count = 99


def test_paper_portfolio_snapshot_has_no_valuation_or_pnl_fields() -> None:
    snapshot = project_paper_portfolio_snapshot(
        _initial_treasury_snapshot(),
        PaperPositionBook(),
    )
    snapshot_fields = {field.name for field in fields(snapshot)}

    assert "current_price_eur" not in snapshot_fields
    assert "market_value_eur" not in snapshot_fields
    assert "unrealized_pnl_eur" not in snapshot_fields
    assert "realized_pnl_eur" not in snapshot_fields
    assert "return_pct" not in snapshot_fields
    assert "strategy_attribution" not in snapshot_fields


def test_open_cost_basis_ratio_uses_decimal_and_rejects_invalid_capital() -> None:
    assert calculate_open_cost_basis_ratio(
        Decimal("50.00"),
        Decimal("200.00"),
    ) == Decimal("0.25")

    with pytest.raises(ValueError, match="initial capital must be positive"):
        calculate_open_cost_basis_ratio(Decimal("50.00"), Decimal("0.00"))
    with pytest.raises(ValueError, match="initial capital must be positive"):
        calculate_open_cost_basis_ratio(Decimal("50.00"), Decimal("-200.00"))
