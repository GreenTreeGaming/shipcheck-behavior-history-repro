import unittest

from app.purge import PurgeRequest, purge_tenant
from app.store import Tenant, TenantStore


class TestInternalPurgeAuthorization(unittest.TestCase):
    def test_internal_purge_rejects_missing_and_non_admin_sessions_without_deleting_tenant(self) -> None:
        for session_token in (None, "member-token"):
            with self.subTest(session_token=session_token):
                store = TenantStore()
                store.add(Tenant(id="tenant-1", name="Acme"))

                response = purge_tenant(
                    PurgeRequest(
                        tenant_id="tenant-1",
                        session_token=session_token,
                        internal=True,
                    ),
                    store,
                )

                self.assertEqual(response.status, 401)
                self.assertFalse(store.get("tenant-1").deleted)
