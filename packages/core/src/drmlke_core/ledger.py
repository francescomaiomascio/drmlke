"""Append-only paper treasury ledger contracts."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import NewType

from drmlke_core.identity import ActorMetadata
from drmlke_core.treasury import (
    DEFAULT_PAPER_TREASURY_BOUNDARY,
    PAPER_TREASURY_ID,
    PAPER_TREASURY_INITIAL_CAPITAL_EUR,
    PaperTreasuryBoundary,
    TreasuryMode,
)

LedgerEntryId = NewType("LedgerEntryId", str)
LedgerSequence = NewType("LedgerSequence", int)

INITIAL_LEDGER_SEQUENCE = LedgerSequence(1)


class LedgerEntryType(StrEnum):
    PAPER_INITIAL_CAPITAL = "paper_initial_capital"
    PAPER_CASH_ADJUSTMENT = "paper_cash_adjustment"
    PAPER_CORRECTION = "paper_correction"
    PAPER_FEE = "paper_fee"
    PAPER_RESERVED_CASH = "paper_reserved_cash"
    PAPER_RELEASED_CASH = "paper_released_cash"


NEGATIVE_ONLY_ENTRY_TYPES = frozenset(
    {
        LedgerEntryType.PAPER_FEE,
        LedgerEntryType.PAPER_RESERVED_CASH,
    }
)

POSITIVE_ONLY_ENTRY_TYPES = frozenset(
    {
        LedgerEntryType.PAPER_INITIAL_CAPITAL,
        LedgerEntryType.PAPER_RELEASED_CASH,
    }
)


@dataclass(frozen=True, slots=True)
class LedgerEntry:
    entry_id: LedgerEntryId
    treasury_id: str
    sequence: LedgerSequence
    entry_type: LedgerEntryType
    amount_eur: Decimal
    actor: ActorMetadata
    reason: str
    reference: str | None = None

    def __post_init__(self) -> None:
        if not str(self.entry_id):
            raise ValueError("ledger entry id is required")
        if self.treasury_id != PAPER_TREASURY_ID:
            raise ValueError("ledger entry treasury id must match the paper treasury")
        if int(self.sequence) < int(INITIAL_LEDGER_SEQUENCE):
            raise ValueError("ledger sequence must be positive")
        if not isinstance(self.amount_eur, Decimal):
            raise TypeError("ledger amount must be Decimal")
        if self.amount_eur == Decimal("0"):
            raise ValueError("ledger amount cannot be zero")
        if not self.reason.strip():
            raise ValueError("ledger reason is required")
        _validate_entry_amount(self.entry_type, self.amount_eur)


@dataclass(frozen=True, slots=True)
class PaperLedger:
    treasury: PaperTreasuryBoundary = DEFAULT_PAPER_TREASURY_BOUNDARY
    entries: tuple[LedgerEntry, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "entries", tuple(self.entries))
        self.treasury.validate()


def create_initial_paper_ledger(actor: ActorMetadata) -> PaperLedger:
    treasury = DEFAULT_PAPER_TREASURY_BOUNDARY
    _assert_actor_can_append(treasury, actor)
    entry = LedgerEntry(
        entry_id=LedgerEntryId("paper-initial-capital"),
        treasury_id=treasury.treasury_id,
        sequence=INITIAL_LEDGER_SEQUENCE,
        entry_type=LedgerEntryType.PAPER_INITIAL_CAPITAL,
        amount_eur=treasury.initial_capital_eur,
        actor=actor,
        reason="Initial paper treasury capital",
    )
    ledger = PaperLedger(treasury=treasury, entries=(entry,))
    validate_paper_ledger(ledger)
    return ledger


def append_paper_ledger_entry(
    ledger: PaperLedger,
    entry: LedgerEntry,
    actor: ActorMetadata,
) -> PaperLedger:
    validate_paper_ledger(ledger)
    _assert_actor_can_append(ledger.treasury, actor)
    _assert_entry_actor_matches(entry, actor)
    if entry.entry_type is LedgerEntryType.PAPER_INITIAL_CAPITAL:
        raise ValueError("initial capital cannot be appended after ledger creation")
    expected_sequence = LedgerSequence(int(ledger.entries[-1].sequence) + 1)
    if entry.sequence != expected_sequence:
        raise ValueError("ledger entry sequence must be the next append-only sequence")
    if entry.treasury_id != ledger.treasury.treasury_id:
        raise ValueError("ledger entry treasury id does not match ledger treasury")
    next_ledger = PaperLedger(treasury=ledger.treasury, entries=(*ledger.entries, entry))
    validate_paper_ledger(next_ledger)
    return next_ledger


def project_paper_cash_balance_eur(ledger: PaperLedger) -> Decimal:
    validate_paper_ledger(ledger)
    return sum((entry.amount_eur for entry in ledger.entries), Decimal("0.00"))


def validate_paper_ledger(ledger: PaperLedger) -> None:
    ledger.treasury.validate()
    if ledger.treasury.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("paper ledger must use the canonical paper treasury")
    if ledger.treasury.mode is not TreasuryMode.PAPER:
        raise ValueError("paper ledger must remain in paper mode")
    if not ledger.entries:
        raise ValueError("paper ledger requires an initial capital entry")

    initial_entries = [
        entry
        for entry in ledger.entries
        if entry.entry_type is LedgerEntryType.PAPER_INITIAL_CAPITAL
    ]
    if len(initial_entries) != 1:
        raise ValueError("paper ledger requires exactly one initial capital entry")

    for expected, entry in enumerate(ledger.entries, start=int(INITIAL_LEDGER_SEQUENCE)):
        if entry.treasury_id != ledger.treasury.treasury_id:
            raise ValueError("ledger entry treasury id does not match ledger treasury")
        if int(entry.sequence) != expected:
            raise ValueError("ledger entries must be sequential and append-only")

    initial_entry = ledger.entries[0]
    if initial_entry.entry_type is not LedgerEntryType.PAPER_INITIAL_CAPITAL:
        raise ValueError("paper ledger must start with initial capital")
    if initial_entry.amount_eur != PAPER_TREASURY_INITIAL_CAPITAL_EUR:
        raise ValueError("paper ledger initial capital must be 200 EUR")


def _assert_actor_can_append(treasury: PaperTreasuryBoundary, actor: ActorMetadata) -> None:
    if not treasury.can_role_manage(actor.role):
        raise PermissionError("actor cannot append paper ledger entries")


def _assert_entry_actor_matches(entry: LedgerEntry, actor: ActorMetadata) -> None:
    if entry.actor.user_id != actor.user_id or entry.actor.role is not actor.role:
        raise ValueError("ledger entry actor must match append actor")


def _validate_entry_amount(entry_type: LedgerEntryType, amount_eur: Decimal) -> None:
    if entry_type in NEGATIVE_ONLY_ENTRY_TYPES and amount_eur >= Decimal("0"):
        raise ValueError(f"{entry_type.value} entries must be negative")
    if entry_type in POSITIVE_ONLY_ENTRY_TYPES and amount_eur <= Decimal("0"):
        raise ValueError(f"{entry_type.value} entries must be positive")


def next_ledger_sequence(entries: Iterable[LedgerEntry]) -> LedgerSequence:
    entry_tuple = tuple(entries)
    if not entry_tuple:
        return INITIAL_LEDGER_SEQUENCE
    return LedgerSequence(int(entry_tuple[-1].sequence) + 1)
