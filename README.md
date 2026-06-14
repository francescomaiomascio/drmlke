# drmlke

Local-first family crypto decision journal, paper treasury, strategy research,
and auditability project.

Canonical spine: [docs/drmlke-roadmap.md](docs/drmlke-roadmap.md).

Current product model:

- one owner-managed treasury / portfolio
- Francesco is the owner/operator
- Padre and Zio are initial viewer accounts
- one shared client UI with role/capability locks
- backend-enforced permissions

Current product thesis:

- not an auto-trading product
- helps Francesco make slower, better-tracked, less emotional decisions
- starts with a small private paper treasury, benchmarks, and decision records
- values learning, damage avoidance, auditability, and capital preservation

This repository is in bootstrap state. It intentionally does not include:

- live trading
- real wallet custody
- exchange API keys
- real AI models
- withdrawal support
- Spark runtime activation

## Development

Active development checkouts:

- Linux workstation canonical path: `/home/mothx/computer-science/projects/drmlke`
- MacBook secondary active node: `/Users/mothx/Developer/drmlke`

Spark is a future runtime/deploy target and is not the authoring repo.

```sh
uv sync --dev
make check
docker compose --profile provider up provider
```

Provider health:

```sh
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```
