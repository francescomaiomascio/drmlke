# Environment

Bootstrap target: Linux/Arch.

Primary active development node: Linux workstation at
`/home/mothx/computer-science/projects/drmlke`.

Secondary active development node: MacBook at
`/Users/mothx/Developer/drmlke`.

Required tools:

- git
- openssh
- vim
- curl
- make
- docker
- docker compose v2
- docker buildx
- uv
- node
- corepack
- pnpm

Python is pinned to 3.12 through `.python-version` and `pyproject.toml`.
Node is pinned to 24 through `.node-version`.

Use nvm or an equivalent version manager to activate Node 24 before client work:

```sh
source ~/.nvm/nvm.sh
nvm install 24
nvm use 24
corepack enable
node -v
pnpm -v
```

Do not install random global npm packages.

## Linux Status

`LINUX.SETUP.1` records the Linux workstation as the canonical development node:

- Repo path: `/home/mothx/computer-science/projects/drmlke`.
- Branch: `main`.
- Git sync: `main` is aligned with `origin/main`.
- Host target: Linux/Arch local development.
- Shell: `zsh`.
- Node: `v24.16.0`.
- Project Python: Python 3.12 through `uv`.
- Docker Compose provider container: `drmlke-provider-1`.
- Provider port: `8781`.
- Provider role: local stub provider only.
- Provider health: `status=ok`, `provider=stub`,
  `live_trading_enabled=false`.
- Provider models: empty list.
- MacBook remains the secondary active development node.
- Spark remains untouched.

Linux verification commands:

```sh
cd /home/mothx/computer-science/projects/drmlke
git status --short --branch
make doctor
make check
docker compose ps
docker compose --profile provider up -d provider
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```

## MacBook Status

`MAC.SETUP.1-CLOSE` verified the MacBook as a working development node:

- macOS arm64 host.
- Shell: `/bin/zsh`.
- Repo path: `/Users/mothx/Developer/drmlke`.
- Remote: `https://github.com/francescomaiomascio/drmlke`.
- Branch: `main`.
- GitHub sync: `DOCS.SPINE.3` pushed to `origin/main`.
- Node: `v24.16.0`.
- Corepack: `0.35.0`.
- pnpm: `10.12.1`.
- uv: `0.11.17`.
- Docker-compatible runtime: OrbStack Docker context.
- VS Code `code` command is available.
- `make doctor` passes.
- `make check` passes.
- Provider stub runs locally through Docker Compose on port `8781`.

The project Python is the `uv` managed Python 3.12 environment. The MacBook
system `python3` may be newer and should not be treated as the project
interpreter.

MacBook validation commands:

```sh
cd /Users/mothx/Developer/drmlke
make doctor
make check
make docker-base
docker compose --profile provider up -d provider
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```

Spark remains intentionally untouched by MacBook setup. Tailscale and Spark
runtime work belong to later reviewed waves.
