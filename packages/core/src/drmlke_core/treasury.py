"""Paper treasury boundary contracts."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from drmlke_core.identity import Role


class TreasuryMode(StrEnum):
    PAPER = "paper"


PAPER_TREASURY_ID = "drmlke-paper-treasury"
PAPER_TREASURY_INITIAL_CAPITAL_EUR = Decimal("200.00")
LIVE_CAPITAL_EUR = Decimal("0.00")


@dataclass(frozen=True, slots=True)
class PaperTreasuryBoundary:
    treasury_id: str = PAPER_TREASURY_ID
    mode: TreasuryMode = TreasuryMode.PAPER
    initial_capital_eur: Decimal = PAPER_TREASURY_INITIAL_CAPITAL_EUR
    live_capital_eur: Decimal = LIVE_CAPITAL_EUR
    one_treasury_only: bool = True
    per_person_portfolios_enabled: bool = False
    owner_role: Role = Role.OWNER_OPERATOR
    viewer_roles: frozenset[Role] = frozenset({Role.VIEWER_FAMILY})

    def validate(self) -> None:
        if self.treasury_id != PAPER_TREASURY_ID:
            raise ValueError("unexpected treasury id")
        if self.mode is not TreasuryMode.PAPER:
            raise ValueError("treasury must remain paper mode")
        if self.initial_capital_eur != PAPER_TREASURY_INITIAL_CAPITAL_EUR:
            raise ValueError("paper treasury initial capital must be 200 EUR")
        if self.live_capital_eur != LIVE_CAPITAL_EUR:
            raise ValueError("live capital must be 0 EUR")
        if not self.one_treasury_only:
            raise ValueError("exactly one treasury is required")
        if self.per_person_portfolios_enabled:
            raise ValueError("per-person portfolios are forbidden")

    def can_role_manage(self, role: Role) -> bool:
        return role is self.owner_role

    def can_role_view(self, role: Role) -> bool:
        return role is self.owner_role or role in self.viewer_roles


DEFAULT_PAPER_TREASURY_BOUNDARY = PaperTreasuryBoundary()


def validate_single_paper_treasury(
    treasuries: Iterable[PaperTreasuryBoundary],
) -> PaperTreasuryBoundary:
    treasury_list = tuple(treasuries)
    if len(treasury_list) != 1:
        raise ValueError("drmlke requires exactly one paper treasury")
    treasury = treasury_list[0]
    treasury.validate()
    return treasury
