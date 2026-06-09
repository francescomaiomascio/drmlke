# Environment

Bootstrap target: Linux/Arch.

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
