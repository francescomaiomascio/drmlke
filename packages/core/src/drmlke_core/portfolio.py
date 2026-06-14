"""Paper portfolio snapshot boundary contracts."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from drmlke_core.position import (
    PaperPositionBook,
    closed_paper_positions,
    open_paper_positions,
    total_open_cost_basis_eur,
    total_position_fees_eur,
    validate_paper_position_book,
)
from drmlke_core.treasury import PAPER_TREASURY_ID
from drmlke_core.treasury_projection import (
    PaperTreasurySnapshot,
    is_paper_treasury_snapshot_reconciled,
    validate_paper_treasury_snapshot,
)


@dataclass(frozen=True, slots=True)
class PaperPortfolioSnapshot:
    treasury_snapshot: PaperTreasurySnapshot
    position_book: PaperPositionBook
    treasury_id: str
    paper_only: bool
    live_capital_locked: bool
    open_position_count: int
    closed_position_count: int
    position_count: int
    available_cash_eur: Decimal
    reserved_cash_eur: Decimal
    total_cash_eur: Decimal
    open_cost_basis_eur: Decimal
    position_fees_eur: Decimal
    total_structural_exposure_eur: Decimal
    open_cost_basis_ratio: Decimal
    reconciled: bool

    def __post_init__(self) -> None:
        validate_paper_portfolio_snapshot(self)


def project_paper_portfolio_snapshot(
    treasury_snapshot: PaperTreasurySnapshot,
    position_book: PaperPositionBook,
) -> PaperPortfolioSnapshot:
    validate_paper_treasury_snapshot(treasury_snapshot)
    validate_paper_position_book(position_book)
    if treasury_snapshot.treasury_id != position_book.treasury_id:
        raise ValueError("portfolio snapshot treasury ids must match")

    open_positions = open_paper_positions(position_book)
    closed_positions = closed_paper_positions(position_book)
    open_cost_basis_eur = total_open_cost_basis_eur(position_book)
    position_fees_eur = total_position_fees_eur(position_book)
    total_structural_exposure_eur = (
        treasury_snapshot.available_cash_eur
        + treasury_snapshot.reserved_cash_eur
        + open_cost_basis_eur
    )
    snapshot = PaperPortfolioSnapshot(
        treasury_snapshot=treasury_snapshot,
        position_book=position_book,
        treasury_id=treasury_snapshot.treasury_id,
        paper_only=treasury_snapshot.paper_only
        and all(position.paper_only for position in position_book.positions),
        live_capital_locked=treasury_snapshot.live_capital_locked
        and all(not position.live_backed for position in position_book.positions),
        open_position_count=len(open_positions),
        closed_position_count=len(closed_positions),
        position_count=len(position_book.positions),
        available_cash_eur=treasury_snapshot.available_cash_eur,
        reserved_cash_eur=treasury_snapshot.reserved_cash_eur,
        total_cash_eur=treasury_snapshot.total_cash_eur,
        open_cost_basis_eur=open_cost_basis_eur,
        position_fees_eur=position_fees_eur,
        total_structural_exposure_eur=total_structural_exposure_eur,
        open_cost_basis_ratio=calculate_open_cost_basis_ratio(
            open_cost_basis_eur,
            treasury_snapshot.initial_capital_eur,
        ),
        reconciled=True,
    )
    validate_paper_portfolio_snapshot(snapshot)
    return snapshot


def validate_paper_portfolio_snapshot(snapshot: PaperPortfolioSnapshot) -> None:
    if snapshot.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("portfolio snapshot treasury id must match the paper treasury")
    if snapshot.treasury_snapshot.treasury_id != snapshot.treasury_id:
        raise ValueError("portfolio snapshot treasury id does not match treasury snapshot")
    if snapshot.position_book.treasury_id != snapshot.treasury_id:
        raise ValueError("portfolio snapshot treasury id does not match position book")
    if not snapshot.paper_only:
        raise ValueError("portfolio snapshot must remain paper-only")
    if not snapshot.live_capital_locked:
        raise ValueError("portfolio snapshot live capital must remain locked")

    validate_paper_treasury_snapshot(snapshot.treasury_snapshot)
    validate_paper_position_book(snapshot.position_book)
    _validate_nonnegative_decimal("available cash", snapshot.available_cash_eur)
    _validate_nonnegative_decimal("reserved cash", snapshot.reserved_cash_eur)
    _validate_nonnegative_decimal("total cash", snapshot.total_cash_eur)
    _validate_nonnegative_decimal("open cost basis", snapshot.open_cost_basis_eur)
    _validate_nonnegative_decimal("position fees", snapshot.position_fees_eur)
    _validate_nonnegative_decimal(
        "total structural exposure",
        snapshot.total_structural_exposure_eur,
    )
    _validate_nonnegative_decimal("open cost basis ratio", snapshot.open_cost_basis_ratio)

    if snapshot.reconciled != is_paper_portfolio_snapshot_reconciled(snapshot):
        raise ValueError("portfolio snapshot reconciliation flag is inconsistent")
    if not snapshot.reconciled:
        raise ValueError("portfolio snapshot is unreconciled")


def is_paper_portfolio_snapshot_reconciled(snapshot: PaperPortfolioSnapshot) -> bool:
    try:
        validate_paper_treasury_snapshot(snapshot.treasury_snapshot)
        validate_paper_position_book(snapshot.position_book)
        expected_open_positions = open_paper_positions(snapshot.position_book)
        expected_closed_positions = closed_paper_positions(snapshot.position_book)
        expected_open_cost_basis_eur = total_open_cost_basis_eur(snapshot.position_book)
        expected_position_fees_eur = total_position_fees_eur(snapshot.position_book)
        expected_ratio = calculate_open_cost_basis_ratio(
            expected_open_cost_basis_eur,
            snapshot.treasury_snapshot.initial_capital_eur,
        )
    except (TypeError, ValueError):
        return False

    expected_total_structural_exposure_eur = (
        snapshot.treasury_snapshot.available_cash_eur
        + snapshot.treasury_snapshot.reserved_cash_eur
        + expected_open_cost_basis_eur
    )
    return (
        snapshot.treasury_id == PAPER_TREASURY_ID
        and snapshot.treasury_id == snapshot.treasury_snapshot.treasury_id
        and snapshot.treasury_id == snapshot.position_book.treasury_id
        and is_paper_treasury_snapshot_reconciled(snapshot.treasury_snapshot)
        and snapshot.paper_only
        and snapshot.live_capital_locked
        and all(position.paper_only for position in snapshot.position_book.positions)
        and all(not position.live_backed for position in snapshot.position_book.positions)
        and snapshot.open_position_count == len(expected_open_positions)
        and snapshot.closed_position_count == len(expected_closed_positions)
        and snapshot.position_count == len(snapshot.position_book.positions)
        and snapshot.available_cash_eur == snapshot.treasury_snapshot.available_cash_eur
        and snapshot.reserved_cash_eur == snapshot.treasury_snapshot.reserved_cash_eur
        and snapshot.total_cash_eur == snapshot.treasury_snapshot.total_cash_eur
        and snapshot.open_cost_basis_eur == expected_open_cost_basis_eur
        and snapshot.position_fees_eur == expected_position_fees_eur
        and snapshot.total_structural_exposure_eur
        == expected_total_structural_exposure_eur
        and snapshot.open_cost_basis_ratio == expected_ratio
    )


def calculate_open_cost_basis_ratio(
    open_cost_basis_eur: Decimal,
    initial_capital_eur: Decimal,
) -> Decimal:
    _validate_nonnegative_decimal("open cost basis", open_cost_basis_eur)
    _validate_positive_decimal("initial capital", initial_capital_eur)
    return open_cost_basis_eur / initial_capital_eur


def _validate_positive_decimal(name: str, value: Decimal) -> None:
    _validate_decimal(name, value)
    if value <= Decimal("0"):
        raise ValueError(f"{name} must be positive")


def _validate_nonnegative_decimal(name: str, value: Decimal) -> None:
    _validate_decimal(name, value)
    if value < Decimal("0"):
        raise ValueError(f"{name} cannot be negative")


def _validate_decimal(name: str, value: Decimal) -> None:
    if not isinstance(value, Decimal):
        raise TypeError(f"{name} must be Decimal")
