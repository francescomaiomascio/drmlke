"""Paper decision record boundary contracts."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import NewType

from drmlke_core.identity import ActorMetadata, Role
from drmlke_core.portfolio import (
    PaperPortfolioSnapshot,
    validate_paper_portfolio_snapshot,
)
from drmlke_core.position import (
    AssetSymbol,
    normalize_asset_symbol,
    validate_initial_paper_position_asset,
)
from drmlke_core.treasury import PAPER_TREASURY_ID

DecisionRecordId = NewType("DecisionRecordId", str)


class DecisionKind(StrEnum):
    NO_ACTION = "no_action"
    WATCH = "watch"
    ACTION_CANDIDATE = "action_candidate"
    RISK_VETOED = "risk_vetoed"
    REJECTED = "rejected"
    POSTPONED = "postponed"


class DecisionSubjectType(StrEnum):
    TREASURY = "treasury"
    ASSET = "asset"
    POSITION = "position"
    PORTFOLIO = "portfolio"
    STRATEGY = "strategy"
    RISK = "risk"


class DecisionTimeframe(StrEnum):
    ONE_DAY = "one_day"
    FOUR_HOUR_CONTEXT = "four_hour_context"
    ONE_WEEK_CONTEXT = "one_week_context"
    UNSPECIFIED = "unspecified"


class DataFreshnessState(StrEnum):
    FRESH = "fresh"
    STALE = "stale"
    MISSING = "missing"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class DecisionRiskState(StrEnum):
    NOT_EVALUATED = "not_evaluated"
    ALLOW_PAPER_REVIEW = "allow_paper_review"
    REDUCE = "reduce"
    DELAY = "delay"
    VETO = "veto"
    LOCKED = "locked"


class DecisionOutcomeState(StrEnum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    GOOD_PROCESS_WIN = "good_process_win"
    GOOD_PROCESS_LOSS = "good_process_loss"
    BAD_PROCESS_WIN = "bad_process_win"
    BAD_PROCESS_LOSS = "bad_process_loss"
    INCONCLUSIVE = "inconclusive"
    CANCELLED = "cancelled"


PENDING_OUTCOME_STATES = frozenset(
    {
        DecisionOutcomeState.PENDING,
        DecisionOutcomeState.REVIEWED,
    }
)

RISK_VETO_STATES = frozenset(
    {
        DecisionRiskState.VETO,
        DecisionRiskState.LOCKED,
        DecisionRiskState.DELAY,
        DecisionRiskState.REDUCE,
    }
)


@dataclass(frozen=True, slots=True)
class DecisionCostAssumption:
    estimated_entry_fee_eur: Decimal
    estimated_exit_fee_eur: Decimal
    estimated_spread_eur: Decimal
    estimated_slippage_eur: Decimal
    estimated_rounding_buffer_eur: Decimal
    break_even_move_pct: Decimal

    def __post_init__(self) -> None:
        validate_decision_cost_assumption(self)


@dataclass(frozen=True, slots=True)
class DecisionContext:
    treasury_id: str
    portfolio_snapshot: PaperPortfolioSnapshot | None
    asset: AssetSymbol | None
    timeframe: DecisionTimeframe
    data_freshness: DataFreshnessState
    risk_state: DecisionRiskState
    cost_assumption: DecisionCostAssumption | None
    reference: str | None = None

    def __post_init__(self) -> None:
        validate_decision_context(self)


@dataclass(frozen=True, slots=True)
class DecisionRecord:
    decision_id: DecisionRecordId
    kind: DecisionKind
    actor: ActorMetadata
    subject_type: DecisionSubjectType
    context: DecisionContext
    hypothesis: str
    reasons_to_act: tuple[str, ...]
    reasons_not_to_act: tuple[str, ...]
    final_decision: str
    outcome_state: DecisionOutcomeState = DecisionOutcomeState.PENDING
    post_mortem: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "reasons_to_act", tuple(self.reasons_to_act))
        object.__setattr__(self, "reasons_not_to_act", tuple(self.reasons_not_to_act))
        validate_decision_record(self)


def create_no_action_decision(
    *,
    decision_id: DecisionRecordId,
    actor: ActorMetadata,
    subject_type: DecisionSubjectType,
    context: DecisionContext,
    hypothesis: str,
    reasons_not_to_act: tuple[str, ...],
    final_decision: str,
    outcome_state: DecisionOutcomeState = DecisionOutcomeState.PENDING,
    post_mortem: str | None = None,
) -> DecisionRecord:
    return DecisionRecord(
        decision_id=decision_id,
        kind=DecisionKind.NO_ACTION,
        actor=actor,
        subject_type=subject_type,
        context=context,
        hypothesis=hypothesis,
        reasons_to_act=(),
        reasons_not_to_act=reasons_not_to_act,
        final_decision=final_decision,
        outcome_state=outcome_state,
        post_mortem=post_mortem,
    )


def create_watch_decision(
    *,
    decision_id: DecisionRecordId,
    actor: ActorMetadata,
    subject_type: DecisionSubjectType,
    context: DecisionContext,
    hypothesis: str,
    reasons_not_to_act: tuple[str, ...],
    final_decision: str,
    reasons_to_act: tuple[str, ...] = (),
    outcome_state: DecisionOutcomeState = DecisionOutcomeState.PENDING,
    post_mortem: str | None = None,
) -> DecisionRecord:
    return DecisionRecord(
        decision_id=decision_id,
        kind=DecisionKind.WATCH,
        actor=actor,
        subject_type=subject_type,
        context=context,
        hypothesis=hypothesis,
        reasons_to_act=reasons_to_act,
        reasons_not_to_act=reasons_not_to_act,
        final_decision=final_decision,
        outcome_state=outcome_state,
        post_mortem=post_mortem,
    )


def create_action_candidate_decision(
    *,
    decision_id: DecisionRecordId,
    actor: ActorMetadata,
    subject_type: DecisionSubjectType,
    context: DecisionContext,
    hypothesis: str,
    reasons_to_act: tuple[str, ...],
    reasons_not_to_act: tuple[str, ...],
    final_decision: str,
    outcome_state: DecisionOutcomeState = DecisionOutcomeState.PENDING,
    post_mortem: str | None = None,
) -> DecisionRecord:
    return DecisionRecord(
        decision_id=decision_id,
        kind=DecisionKind.ACTION_CANDIDATE,
        actor=actor,
        subject_type=subject_type,
        context=context,
        hypothesis=hypothesis,
        reasons_to_act=reasons_to_act,
        reasons_not_to_act=reasons_not_to_act,
        final_decision=final_decision,
        outcome_state=outcome_state,
        post_mortem=post_mortem,
    )


def validate_decision_cost_assumption(costs: DecisionCostAssumption) -> None:
    _validate_nonnegative_decimal("estimated entry fee", costs.estimated_entry_fee_eur)
    _validate_nonnegative_decimal("estimated exit fee", costs.estimated_exit_fee_eur)
    _validate_nonnegative_decimal("estimated spread", costs.estimated_spread_eur)
    _validate_nonnegative_decimal("estimated slippage", costs.estimated_slippage_eur)
    _validate_nonnegative_decimal(
        "estimated rounding buffer",
        costs.estimated_rounding_buffer_eur,
    )
    _validate_nonnegative_decimal("break-even move", costs.break_even_move_pct)


def validate_decision_context(context: DecisionContext) -> None:
    if context.treasury_id != PAPER_TREASURY_ID:
        raise ValueError("decision context treasury id must match the paper treasury")
    if context.portfolio_snapshot is not None:
        validate_paper_portfolio_snapshot(context.portfolio_snapshot)
        if context.portfolio_snapshot.treasury_id != context.treasury_id:
            raise ValueError("decision context portfolio snapshot treasury id mismatch")
    if context.asset is not None:
        normalized_asset = normalize_asset_symbol(str(context.asset))
        if normalized_asset != context.asset:
            raise ValueError("decision context asset must be normalized")
        validate_initial_paper_position_asset(context.asset)
    if context.cost_assumption is not None:
        validate_decision_cost_assumption(context.cost_assumption)


def validate_decision_record(record: DecisionRecord) -> None:
    if not str(record.decision_id):
        raise ValueError("decision record id is required")
    if record.actor.role is not Role.OWNER_OPERATOR:
        raise ValueError("decision records require owner/operator actor")

    validate_decision_context(record.context)
    _validate_nonempty_text("hypothesis", record.hypothesis)
    _validate_nonempty_text("final decision", record.final_decision)
    _validate_reason_tuple("reasons not to act", record.reasons_not_to_act)

    if record.kind is DecisionKind.ACTION_CANDIDATE:
        _validate_reason_tuple("reasons to act", record.reasons_to_act)
        if record.context.data_freshness is not DataFreshnessState.FRESH:
            raise ValueError("action candidates require fresh data")
        if record.context.risk_state is not DecisionRiskState.ALLOW_PAPER_REVIEW:
            raise ValueError("action candidates require paper review risk allowance")
        if record.context.cost_assumption is None:
            raise ValueError("action candidates require cost assumptions")

    if record.kind is DecisionKind.RISK_VETOED:
        if record.context.risk_state not in RISK_VETO_STATES:
            raise ValueError(
                "risk-vetoed decisions require a veto, lock, delay, "
                "or reduce risk state"
            )

    if record.outcome_state not in PENDING_OUTCOME_STATES and not _has_text(
        record.post_mortem
    ):
        raise ValueError("completed decision outcomes require a post-mortem")


def _validate_reason_tuple(name: str, reasons: tuple[str, ...]) -> None:
    if not reasons:
        raise ValueError(f"{name} are required")
    for reason in reasons:
        _validate_nonempty_text(name, reason)


def _validate_nonempty_text(name: str, value: str) -> None:
    if not _has_text(value):
        raise ValueError(f"{name} is required")


def _has_text(value: str | None) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_nonnegative_decimal(name: str, value: Decimal) -> None:
    _validate_decimal(name, value)
    if value < Decimal("0"):
        raise ValueError(f"{name} cannot be negative")


def _validate_decimal(name: str, value: Decimal) -> None:
    if not isinstance(value, Decimal):
        raise TypeError(f"{name} must be Decimal")
