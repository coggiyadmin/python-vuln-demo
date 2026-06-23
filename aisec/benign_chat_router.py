"""TN — benign chat router (no AI-attack surface). Routes a request to a handler by
an internal enum; no untrusted text ever reaches an instruction/system role.
"""
from enum import Enum


class Intent(Enum):
    BILLING = "billing"
    SUPPORT = "support"
    SALES = "sales"


_HANDLERS = {
    Intent.BILLING: lambda: "Routing to billing.",
    Intent.SUPPORT: lambda: "Routing to support.",
    Intent.SALES: lambda: "Routing to sales.",
}


def route(intent: Intent) -> str:
    return _HANDLERS[intent]()
