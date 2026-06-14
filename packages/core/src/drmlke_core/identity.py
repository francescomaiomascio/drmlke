"""Identity, role, and capability contracts for the product core."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import NewType

UserId = NewType("UserId", str)


class Role(StrEnum):
    OWNER_OPERATOR = "owner_operator"
    VIEWER_FAMILY = "viewer_family"
    EMERGENCY_ONLY = "emergency_only"
    ADMIN_TECHNICAL = "admin_technical"


class Capability(StrEnum):
    VIEW_TREASURY = "view_treasury"
    VIEW_POSITIONS = "view_positions"
    VIEW_PNL = "view_pnl"
    VIEW_RUNTIME_STATUS = "view_runtime_status"
    VIEW_SIGNALS = "view_signals"
    VIEW_NEWS = "view_news"
    VIEW_ALERTS = "view_alerts"
    VIEW_AUDIT_SUMMARY = "view_audit_summary"
    MANAGE_RUNTIME = "manage_runtime"
    PAUSE_RUNTIME = "pause_runtime"
    RESUME_RUNTIME = "resume_runtime"
    EMERGENCY_STOP = "emergency_stop"
    MANAGE_STRATEGIES = "manage_strategies"
    MANAGE_RISK_POLICY = "manage_risk_policy"
    APPROVE_PAPER_ACTION = "approve_paper_action"
    APPROVE_FUTURE_LIVE_ACTION = "approve_future_live_action"
    MANAGE_DEVICES = "manage_devices"
    MANAGE_USERS = "manage_users"
    MANAGE_EXCHANGE_CONNECTIONS = "manage_exchange_connections"
    VIEW_SENSITIVE_LOGS = "view_sensitive_logs"


CapabilitySet = frozenset[Capability]

GLOBAL_LOCKED_CAPABILITIES: CapabilitySet = frozenset(
    {
        Capability.APPROVE_FUTURE_LIVE_ACTION,
        Capability.MANAGE_EXCHANGE_CONNECTIONS,
    }
)

VIEWER_CAPABILITIES: CapabilitySet = frozenset(
    {
        Capability.VIEW_TREASURY,
        Capability.VIEW_POSITIONS,
        Capability.VIEW_PNL,
        Capability.VIEW_RUNTIME_STATUS,
        Capability.VIEW_SIGNALS,
        Capability.VIEW_NEWS,
        Capability.VIEW_ALERTS,
        Capability.VIEW_AUDIT_SUMMARY,
    }
)

OVERRIDE_GRANTABLE_CAPABILITIES: CapabilitySet = VIEWER_CAPABILITIES

OWNER_DECLARED_CAPABILITIES: CapabilitySet = frozenset(
    {
        *VIEWER_CAPABILITIES,
        Capability.MANAGE_RUNTIME,
        Capability.PAUSE_RUNTIME,
        Capability.RESUME_RUNTIME,
        Capability.EMERGENCY_STOP,
        Capability.MANAGE_STRATEGIES,
        Capability.MANAGE_RISK_POLICY,
        Capability.APPROVE_PAPER_ACTION,
        Capability.APPROVE_FUTURE_LIVE_ACTION,
        Capability.MANAGE_DEVICES,
        Capability.MANAGE_USERS,
        Capability.MANAGE_EXCHANGE_CONNECTIONS,
        Capability.VIEW_SENSITIVE_LOGS,
    }
)

EMERGENCY_DECLARED_CAPABILITIES: CapabilitySet = frozenset(
    {
        Capability.VIEW_RUNTIME_STATUS,
        Capability.VIEW_ALERTS,
        Capability.EMERGENCY_STOP,
    }
)

ADMIN_TECHNICAL_DECLARED_CAPABILITIES: CapabilitySet = frozenset(
    {
        Capability.VIEW_RUNTIME_STATUS,
        Capability.VIEW_ALERTS,
        Capability.VIEW_AUDIT_SUMMARY,
        Capability.MANAGE_DEVICES,
        Capability.VIEW_SENSITIVE_LOGS,
    }
)

DECLARED_ROLE_CAPABILITY_POLICY: dict[Role, CapabilitySet] = {
    Role.OWNER_OPERATOR: OWNER_DECLARED_CAPABILITIES,
    Role.VIEWER_FAMILY: VIEWER_CAPABILITIES,
    Role.EMERGENCY_ONLY: EMERGENCY_DECLARED_CAPABILITIES,
    Role.ADMIN_TECHNICAL: ADMIN_TECHNICAL_DECLARED_CAPABILITIES,
}

ROLE_CAPABILITY_POLICY: dict[Role, CapabilitySet] = {
    role: capabilities - GLOBAL_LOCKED_CAPABILITIES
    for role, capabilities in DECLARED_ROLE_CAPABILITY_POLICY.items()
}


def capabilities_for_role(
    role: Role,
    *,
    include_globally_locked: bool = False,
) -> CapabilitySet:
    if include_globally_locked:
        return DECLARED_ROLE_CAPABILITY_POLICY[role]
    return ROLE_CAPABILITY_POLICY[role]


def is_capability_globally_locked(capability: Capability) -> bool:
    return capability in GLOBAL_LOCKED_CAPABILITIES


@dataclass(frozen=True, slots=True)
class ActorMetadata:
    user_id: UserId
    role: Role
    source: str = "local"
    reason: str | None = None


@dataclass(frozen=True, slots=True)
class UserProfile:
    user_id: UserId
    role: Role
    display_name: str
    source: str = "local"
    capability_overrides: CapabilitySet = frozenset()

    @property
    def capabilities(self) -> CapabilitySet:
        safe_overrides = self.capability_overrides & OVERRIDE_GRANTABLE_CAPABILITIES
        return capabilities_for_role(self.role) | safe_overrides

    def has_capability(self, capability: Capability) -> bool:
        return capability in self.capabilities and not is_capability_globally_locked(capability)

    def actor_metadata(self, *, reason: str | None = None) -> ActorMetadata:
        return ActorMetadata(
            user_id=self.user_id,
            role=self.role,
            source=self.source,
            reason=reason,
        )


INITIAL_USER_PROFILES: tuple[UserProfile, ...] = (
    UserProfile(UserId("francesco"), Role.OWNER_OPERATOR, "Francesco"),
    UserProfile(UserId("padre"), Role.VIEWER_FAMILY, "Padre"),
    UserProfile(UserId("zio"), Role.VIEWER_FAMILY, "Zio"),
)
