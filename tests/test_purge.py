from app.purge import PurgeRequest, purge_tenant
from app.store import Tenant, TenantStore


def make_store() -> TenantStore:
    store = TenantStore()
    store.add(
        Tenant(
            id="tenant-1",
            name="Acme",
        ),
    )
    return store


def test_purge_rejects_missing_session() -> None:
    store = make_store()

    response = purge_tenant(
        PurgeRequest(
            tenant_id="tenant-1",
            session_token=None,
        ),
        store,
    )

    assert response.status == 401
    assert store.get("tenant-1").deleted is False


def test_purge_rejects_non_admin_session() -> None:
    store = make_store()

    response = purge_tenant(
        PurgeRequest(
            tenant_id="tenant-1",
            session_token="member-token",
        ),
        store,
    )

    assert response.status == 401
    assert store.get("tenant-1").deleted is False


def test_purge_allows_admin_session() -> None:
    store = make_store()

    response = purge_tenant(
        PurgeRequest(
            tenant_id="tenant-1",
            session_token="admin-token",
        ),
        store,
    )

    assert response.status == 200
    assert store.get("tenant-1").deleted is True
