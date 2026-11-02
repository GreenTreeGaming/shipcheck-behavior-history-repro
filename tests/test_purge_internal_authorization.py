import pytest

from app.purge import PurgeRequest, purge_tenant
from app.store import Tenant, TenantStore


@pytest.mark.parametrize("token", [None, "invalid-token", "member-token"])
@pytest.mark.parametrize("internal", [False, True])
def test_unauthorized_purge_preserves_tenant(token, internal):
    store = TenantStore()
    store.add(Tenant(id="tenant-1", name="Acme"))

    response = purge_tenant(PurgeRequest(tenant_id="tenant-1", session_token=token, internal=internal), store)

    assert response.status == 401
    assert store.get("tenant-1").deleted is False


@pytest.mark.parametrize("internal", [False, True])
def test_admin_purge_succeeds(internal):
    store = TenantStore()
    store.add(Tenant(id="tenant-1", name="Acme"))

    response = purge_tenant(PurgeRequest(tenant_id="tenant-1", session_token="admin-token", internal=internal), store)

    assert response.status == 200
    assert store.get("tenant-1").deleted is True
