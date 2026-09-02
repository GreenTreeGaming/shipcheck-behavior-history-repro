from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AuditEvent:
    action: str
    tenant_id: str
    actor_id: str


def record_purge(
    tenant_id: str,
    actor_id: str,
) -> AuditEvent:
    return AuditEvent(
        action="tenant.purge",
        tenant_id=tenant_id,
        actor_id=actor_id,
    )
