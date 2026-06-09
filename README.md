# drmlke

Local-first family crypto intelligence, paper-trading, wallet-ledger, and agentic runtime project.

This repository is in bootstrap state. It intentionally does not include:

- live trading
- real wallet custody
- exchange API keys
- real AI models
- withdrawal support

## Development

```sh
uv sync --dev
make check
docker compose --profile provider up provider
```

Provider health:

```sh
curl http://localhost:8781/health
curl http://localhost:8781/models
```
