"""Global bootstrap safety locks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GlobalSafetyLocks:
    live_trading_enabled: bool = False
    withdrawals_enabled: bool = False
    wallet_custody_enabled: bool = False
    exchange_credentials_enabled: bool = False
    model_execution_can_override_risk: bool = False
    ui_locks_are_security_boundary: bool = False
    server_side_enforcement_required: bool = True

    def unsafe_reasons(self) -> tuple[str, ...]:
        reasons: list[str] = []
        if self.live_trading_enabled:
            reasons.append("live trading enabled")
        if self.withdrawals_enabled:
            reasons.append("withdrawals enabled")
        if self.wallet_custody_enabled:
            reasons.append("wallet custody enabled")
        if self.exchange_credentials_enabled:
            reasons.append("exchange credentials enabled")
        if self.model_execution_can_override_risk:
            reasons.append("model execution can override risk")
        if self.ui_locks_are_security_boundary:
            reasons.append("UI locks treated as security boundary")
        if not self.server_side_enforcement_required:
            reasons.append("server-side enforcement disabled")
        return tuple(reasons)

    def is_bootstrap_safe(self) -> bool:
        return not self.unsafe_reasons()


DEFAULT_GLOBAL_SAFETY_LOCKS = GlobalSafetyLocks()


def assert_bootstrap_safety(locks: GlobalSafetyLocks = DEFAULT_GLOBAL_SAFETY_LOCKS) -> None:
    reasons = locks.unsafe_reasons()
    if reasons:
        reason_text = ", ".join(reasons)
        raise ValueError(f"unsafe bootstrap locks: {reason_text}")
