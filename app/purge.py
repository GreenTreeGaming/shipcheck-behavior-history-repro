from __future__ import annotations

from dataclasses import dataclass

from app.auth import require_admin_session
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


def _has_admin_session(
    request: PurgeRequest,
) -> bool:
    return require_admin_session(
        request.session_token,
    ) is not None


def purge_tenant(
    request: PurgeRequest,
    store: TenantStore,
) -> PurgeResponse:
    """Purge a tenant only for authenticated administrators."""

    if not _has_admin_session(
        request,
    ):
        return PurgeResponse(
            status=401,
            message="valid admin session required",
        )

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
