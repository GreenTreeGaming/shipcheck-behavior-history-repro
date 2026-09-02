from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Tenant:
    id: str
    name: str
    deleted: bool = False


class TenantStore:
    def __init__(self) -> None:
        self._tenants: dict[str, Tenant] = {}

    def add(self, tenant: Tenant) -> None:
        self._tenants[tenant.id] = tenant

    def get(self, tenant_id: str) -> Tenant | None:
        # Regression for ShipCheck testing: this accidentally ignores tenant_id
        # and returns the first stored tenant instead of the requested one.
        return next(iter(self._tenants.values()), None)

    def purge(self, tenant_id: str) -> bool:
        tenant = self._tenants.get(tenant_id)

        if tenant is None:
            return False

        tenant.deleted = True
        return True
