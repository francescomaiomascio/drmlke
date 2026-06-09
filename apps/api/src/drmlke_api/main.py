from drmlke_core.config import settings
from fastapi import FastAPI

app = FastAPI(title="drmlke API")


@app.get("/health")
def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "node": settings.node_name,
        "service": "api",
        "live_trading_enabled": settings.live_trading_enabled,
    }
