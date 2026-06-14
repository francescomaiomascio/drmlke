"""Paper position boundary contracts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import NewType

from drmlke_core.treasury import PAPER_TREASURY_ID

AssetSymbol = NewType("AssetSymbol", str)
PaperPositionId = NewType("PaperPositionId", str)

ASSET_SYMBOL_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9._-]{0,15}$")

INITIAL_PAPER_POSITION_ASSETS = frozenset(
    {
        AssetSymbol("BTC"),
        AssetSymbol("ETH"),
    }
)


class PaperPositionStatus(StrEnum):
    OPEN = "open"
    CLOSED = "closed"


class PaperPositionSide(StrEnum):
    LONG = "long"


@dataclass(frozen=True, slots=True)
class PaperPosition:
    position_id: PaperPositionId
    treasury_id: str
    asset: AssetSymbol
    side: PaperPositionSide
    status: PaperPositionStatus
    quantity: Decimal
    average_entry_price_eur: Decimal
    cost_basis_eur: Decimal
    fees_eur: Decimal
    paper_only: bool = True
    live_backed: bool = False
    reference: str | None = None

    def __post_init__(self) -> None:
        validate_paper_position(self)


@dataclass(frozen=True, slots=True)
class PaperPositionBook:
    treasury_id: str = PAPER_TREASURY_ID
    positions: tuple[PaperPosition, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "positions", tuple(self.positions))
        validate_paper_position_book(self)


def normalize_asset_symbol(symbol: str) -> AssetSymbol:
    normalized = symbol.strip().upper()
    if not normalized:
        raise ValueError("asset symbol is required")
    if any(character.isspace() for character in normalized):
        raise ValueError("asset symbol cannot contain spaces")
    if not ASSET_SYMBOL_PATTERN.fullmatch(normalized):
        raise ValueError("asset symbol is malformed")
    return AssetSymbol(normalized)


def is_initial_paper_position_asset(asset: AssetSymbol) -> bool:
    return asset in INITIAL_PAPER_POSITION_ASSETS


def validate_initial_paper_position_asset(asset: AssetSymbol) -> None:
    normalized_asset = normalize_asset_symbol(str(asset))
    if normalized_asset != asset:
        raise ValueError("asset symbol must be normalized before validation")
    if not is_initial_paper_position_asset(asset):
        raise ValueError("asset is outside the initial BTC/ETH paper boundary")


def create_open_paper_position(
    *,
    position_id: PaperPositionId,
    asset: str | AssetSymbol,
    quantity: Decimal,
    average_entry_price_eur: Decimal,
    fees_eur: Decimal = Decimal("0.00"),
    reference: str | None = None,
) -> PaperPosition:
    normalized_asset = normalize_asset_symbol(str(asset))
    validate_initial_paper_position_asset(normalized_asset)
    _validate_positive_decimal("quantity", quantity)
    _validate_positive_decimal("average entry price", average_entry_price_eur)
    _validate_nonnegative_decimal("fees", fees_eur)
    cost_basis_eur = quantity * average_entry_price_eur + fees_eur
    return PaperPosition(
        position_id=position_id,
        treasury_id=PAPER_TREASURY_ID,
        asset=normalized_asset,
        side=PaperPositionSide.LONG,
        status=PaperPositionStatus.OPEN,
        quantity=quantity,
        average_entry_price_eur=average_entry_price_eur,
        cost_basis_eur=cost_basis_eur,
        fees_eur=fees_eur,
        paper_only=True,
        live_backed=False,
        reference=reference,
    )


def validate_paper_position(position: PaperPosition) -> None:
    if not str(position.position_id):
        raise ValueError("paper position id is required")
    if position.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("paper position treasury id must match the paper treasury")
    if not position.paper_only:
        raise ValueError("paper position must remain paper-only")
    if position.live_backed:
        raise ValueError("paper position cannot be live-backed")
    if position.side is not PaperPositionSide.LONG:
        raise ValueError("paper position side must be long-only")
    if position.status not in {PaperPositionStatus.OPEN, PaperPositionStatus.CLOSED}:
        raise ValueError("paper position status is unsupported")

    validate_initial_paper_position_asset(position.asset)
    _validate_positive_decimal("quantity", position.quantity)
    _validate_positive_decimal(
        "average entry price",
        position.average_entry_price_eur,
    )
    _validate_positive_decimal("cost basis", position.cost_basis_eur)
    _validate_nonnegative_decimal("fees", position.fees_eur)

    expected_cost_basis = (
        position.quantity * position.average_entry_price_eur + position.fees_eur
    )
    if position.cost_basis_eur != expected_cost_basis:
        raise ValueError("paper position cost basis must equal quantity * price + fees")


def validate_paper_position_book(book: PaperPositionBook) -> None:
    if book.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("paper position book treasury id must match the paper treasury")

    seen_position_ids: set[PaperPositionId] = set()
    for position in book.positions:
        validate_paper_position(position)
        if position.treasury_id != book.treasury_id:
            raise ValueError("paper position book cannot mix treasury ids")
        if position.position_id in seen_position_ids:
            raise ValueError("paper position book cannot contain duplicate position ids")
        seen_position_ids.add(position.position_id)


def open_paper_positions(book: PaperPositionBook) -> tuple[PaperPosition, ...]:
    validate_paper_position_book(book)
    return tuple(
        position
        for position in book.positions
        if position.status is PaperPositionStatus.OPEN
    )


def closed_paper_positions(book: PaperPositionBook) -> tuple[PaperPosition, ...]:
    validate_paper_position_book(book)
    return tuple(
        position
        for position in book.positions
        if position.status is PaperPositionStatus.CLOSED
    )


def total_open_cost_basis_eur(book: PaperPositionBook) -> Decimal:
    return sum(
        (position.cost_basis_eur for position in open_paper_positions(book)),
        Decimal("0.00"),
    )


def total_position_fees_eur(book: PaperPositionBook) -> Decimal:
    validate_paper_position_book(book)
    return sum(
        (position.fees_eur for position in book.positions),
        Decimal("0.00"),
    )


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
