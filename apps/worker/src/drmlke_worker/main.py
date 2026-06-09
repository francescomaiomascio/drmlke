import structlog
from drmlke_core.config import settings

log = structlog.get_logger()


def heartbeat() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "node": settings.node_name,
        "service": "worker",
        "live_trading_enabled": settings.live_trading_enabled,
    }


def main() -> None:
    log.info("drmlke worker heartbeat", **heartbeat())
