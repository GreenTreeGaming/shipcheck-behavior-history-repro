from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    user_id: str
    role: str


_SESSIONS = {
    "admin-token": Session(
        user_id="user-admin",
        role="admin",
    ),
    "member-token": Session(
        user_id="user-member",
        role="member",
    ),
}


def get_session(
    token: str | None,
) -> Session | None:
    if not token:
        return None

    return _SESSIONS.get(token)


def require_admin_session(
    token: str | None,
) -> Session | None:
    session = get_session(token)

    if session is None:
        return None

    if session.role != "admin":
        return None

    return session
