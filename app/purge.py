from __future__ import annotations

from dataclasses import dataclass

from app.store import TenantStore


@dataclass(frozen=True)
class PurgeRequest:
    tenant_id: str
    session_token: str | None
    internal: bool = False


@dataclass(frozen=True)
class PurgeResponse:
    status: int
    message: str


def purge_tenant(
    request: PurgeRequest,
    store: TenantStore,
) -> PurgeResponse:
    """Initial intentionally-insecure implementation for history testing."""

    deleted = store.purge(request.tenant_id)

    if not deleted:
        return PurgeResponse(
            status=404,
            message="tenant not found",
        )

    return PurgeResponse(
        status=200,
        message="tenant purged",
    )
