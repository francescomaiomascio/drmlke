# drmlke

Local-first family crypto intelligence, paper-trading, treasury-ledger, and agentic runtime project.

Canonical spine: [docs/drmlke-roadmap.md](docs/drmlke-roadmap.md).

Current product model:

- one owner-managed treasury / portfolio
- Francesco is the owner/operator
- Padre and Zio are initial viewer accounts
- one shared client UI with role/capability locks
- backend-enforced permissions

This repository is in bootstrap state. It intentionally does not include:

- live trading
- real wallet custody
- exchange API keys
- real AI models
- withdrawal support

## Development

Active development checkouts:

- Linux workstation canonical path: `/home/mothx/code/drmlke`
- MacBook secondary active node: `/Users/mothx/Developer/drmlke`

Spark is a future runtime/deploy target and is not the authoring repo.

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
