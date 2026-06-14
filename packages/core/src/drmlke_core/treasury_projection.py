"""Read-side projection for the paper treasury ledger."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from drmlke_core.ledger import LedgerEntry, LedgerEntryType, PaperLedger, validate_paper_ledger
from drmlke_core.treasury import (
    LIVE_CAPITAL_EUR,
    PAPER_TREASURY_ID,
    PAPER_TREASURY_INITIAL_CAPITAL_EUR,
    TreasuryMode,
)


@dataclass(frozen=True, slots=True)
class PaperTreasurySnapshot:
    treasury_id: str
    mode: TreasuryMode
    initial_capital_eur: Decimal
    live_capital_eur: Decimal
    ledger_entry_count: int
    last_sequence: int
    available_cash_eur: Decimal
    reserved_cash_eur: Decimal
    total_cash_eur: Decimal
    total_fees_eur: Decimal
    net_adjustments_eur: Decimal
    net_corrections_eur: Decimal
    paper_only: bool
    live_capital_locked: bool
    reconciled: bool

    def __post_init__(self) -> None:
        validate_paper_treasury_snapshot(self)


def project_paper_treasury_snapshot(ledger: PaperLedger) -> PaperTreasurySnapshot:
    validate_paper_ledger(ledger)

    available_cash_eur = Decimal("0.00")
    reserved_cash_eur = Decimal("0.00")
    total_fees_eur = Decimal("0.00")
    net_adjustments_eur = Decimal("0.00")
    net_corrections_eur = Decimal("0.00")

    for entry in ledger.entries:
        available_cash_eur, reserved_cash_eur, total_fees_eur = _project_entry_cash(
            entry,
            available_cash_eur,
            reserved_cash_eur,
            total_fees_eur,
        )
        if entry.entry_type is LedgerEntryType.PAPER_CASH_ADJUSTMENT:
            net_adjustments_eur += entry.amount_eur
        elif entry.entry_type is LedgerEntryType.PAPER_CORRECTION:
            net_corrections_eur += entry.amount_eur
        _validate_cash_state(available_cash_eur, reserved_cash_eur)

    total_cash_eur = available_cash_eur + reserved_cash_eur
    last_sequence = int(ledger.entries[-1].sequence)
    snapshot = PaperTreasurySnapshot(
        treasury_id=ledger.treasury.treasury_id,
        mode=ledger.treasury.mode,
        initial_capital_eur=ledger.treasury.initial_capital_eur,
        live_capital_eur=ledger.treasury.live_capital_eur,
        ledger_entry_count=len(ledger.entries),
        last_sequence=last_sequence,
        available_cash_eur=available_cash_eur,
        reserved_cash_eur=reserved_cash_eur,
        total_cash_eur=total_cash_eur,
        total_fees_eur=total_fees_eur,
        net_adjustments_eur=net_adjustments_eur,
        net_corrections_eur=net_corrections_eur,
        paper_only=ledger.treasury.mode is TreasuryMode.PAPER,
        live_capital_locked=ledger.treasury.live_capital_eur == LIVE_CAPITAL_EUR,
        reconciled=True,
    )
    validate_paper_treasury_snapshot(snapshot)
    return snapshot


def validate_paper_treasury_snapshot(snapshot: PaperTreasurySnapshot) -> None:
    if snapshot.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("snapshot treasury id must match the paper treasury")
    if snapshot.mode is not TreasuryMode.PAPER:
        raise ValueError("snapshot mode must remain paper")
    if snapshot.initial_capital_eur != PAPER_TREASURY_INITIAL_CAPITAL_EUR:
        raise ValueError("snapshot initial capital must be 200 EUR")
    if snapshot.live_capital_eur != LIVE_CAPITAL_EUR:
        raise ValueError("snapshot live capital must be 0 EUR")
    if snapshot.available_cash_eur < Decimal("0"):
        raise ValueError("snapshot available cash cannot be negative")
    if snapshot.reserved_cash_eur < Decimal("0"):
        raise ValueError("snapshot reserved cash cannot be negative")
    if snapshot.total_fees_eur < Decimal("0"):
        raise ValueError("snapshot total fees cannot be negative")
    if snapshot.total_cash_eur != snapshot.available_cash_eur + snapshot.reserved_cash_eur:
        raise ValueError("snapshot total cash is unreconciled")
    if snapshot.ledger_entry_count < 1:
        raise ValueError("snapshot requires at least one ledger entry")
    if snapshot.last_sequence != snapshot.ledger_entry_count:
        raise ValueError("snapshot last sequence is inconsistent with ledger count")
    if not snapshot.paper_only:
        raise ValueError("snapshot must be paper-only")
    if not snapshot.live_capital_locked:
        raise ValueError("snapshot live capital must remain locked")
    if snapshot.reconciled != is_paper_treasury_snapshot_reconciled(snapshot):
        raise ValueError("snapshot reconciliation flag is inconsistent")
    if not snapshot.reconciled:
        raise ValueError("snapshot is unreconciled")


def is_paper_treasury_snapshot_reconciled(snapshot: PaperTreasurySnapshot) -> bool:
    return (
        snapshot.treasury_id == PAPER_TREASURY_ID
        and snapshot.mode is TreasuryMode.PAPER
        and snapshot.initial_capital_eur == PAPER_TREASURY_INITIAL_CAPITAL_EUR
        and snapshot.live_capital_eur == LIVE_CAPITAL_EUR
        and snapshot.available_cash_eur >= Decimal("0")
        and snapshot.reserved_cash_eur >= Decimal("0")
        and snapshot.total_cash_eur
        == snapshot.available_cash_eur + snapshot.reserved_cash_eur
        and snapshot.total_fees_eur >= Decimal("0")
        and snapshot.ledger_entry_count >= 1
        and snapshot.last_sequence == snapshot.ledger_entry_count
        and snapshot.paper_only
        and snapshot.live_capital_locked
    )


def _project_entry_cash(
    entry: LedgerEntry,
    available_cash_eur: Decimal,
    reserved_cash_eur: Decimal,
    total_fees_eur: Decimal,
) -> tuple[Decimal, Decimal, Decimal]:
    if entry.entry_type is LedgerEntryType.PAPER_INITIAL_CAPITAL:
        available_cash_eur += entry.amount_eur
    elif entry.entry_type is LedgerEntryType.PAPER_CASH_ADJUSTMENT:
        available_cash_eur += entry.amount_eur
    elif entry.entry_type is LedgerEntryType.PAPER_CORRECTION:
        available_cash_eur += entry.amount_eur
    elif entry.entry_type is LedgerEntryType.PAPER_FEE:
        if entry.amount_eur >= Decimal("0"):
            raise ValueError("paper fee entries must be negative")
        available_cash_eur += entry.amount_eur
        total_fees_eur += abs(entry.amount_eur)
    elif entry.entry_type is LedgerEntryType.PAPER_RESERVED_CASH:
        if entry.amount_eur >= Decimal("0"):
            raise ValueError("paper reserved cash entries must be negative")
        available_cash_eur += entry.amount_eur
        reserved_cash_eur += abs(entry.amount_eur)
    elif entry.entry_type is LedgerEntryType.PAPER_RELEASED_CASH:
        if entry.amount_eur <= Decimal("0"):
            raise ValueError("paper released cash entries must be positive")
        if entry.amount_eur > reserved_cash_eur:
            raise ValueError("paper release cannot exceed reserved cash")
        available_cash_eur += entry.amount_eur
        reserved_cash_eur -= entry.amount_eur
    else:
        raise ValueError(f"unsupported paper ledger entry type: {entry.entry_type}")
    return available_cash_eur, reserved_cash_eur, total_fees_eur


def _validate_cash_state(available_cash_eur: Decimal, reserved_cash_eur: Decimal) -> None:
    if available_cash_eur < Decimal("0"):
        raise ValueError("projected available cash cannot be negative")
    if reserved_cash_eur < Decimal("0"):
        raise ValueError("projected reserved cash cannot be negative")
