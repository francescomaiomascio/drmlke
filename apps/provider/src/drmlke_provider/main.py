from drmlke_core.config import settings
from fastapi import FastAPI

app = FastAPI(title="drmlke Provider Stub")


@app.get("/health")
def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "node": settings.node_name,
        "provider": "stub",
        "live_trading_enabled": settings.live_trading_enabled,
    }


@app.get("/models")
def models() -> dict[str, list[dict[str, str]]]:
    return {"models": []}


def main() -> None:
    import uvicorn

    uvicorn.run(
        "drmlke_provider.main:app",
        host="0.0.0.0",
        port=settings.provider_port,
        reload=False,
    )
