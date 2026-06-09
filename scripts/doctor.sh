#!/usr/bin/env sh
set -eu

required="git ssh vim curl make docker uv node corepack pnpm"

for cmd in $required; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "ok: %s -> %s\n" "$cmd" "$(command -v "$cmd")"
  else
    printf "missing: %s\n" "$cmd"
    exit_code=1
  fi
done

if docker compose version >/dev/null 2>&1; then
  printf "ok: docker compose v2\n"
else
  printf "missing: docker compose v2\n"
  exit_code=1
fi

if docker buildx version >/dev/null 2>&1; then
  printf "ok: docker buildx\n"
else
  printf "missing: docker buildx\n"
  exit_code=1
fi

node_version="$(node -v 2>/dev/null || true)"
case "$node_version" in
  v24.*)
    printf "ok: node major -> %s\n" "$node_version"
    ;;
  *)
    printf "wrong-version: node expected v24.x, got %s\n" "${node_version:-missing}"
    exit_code=1
    ;;
esac

exit "${exit_code:-0}"
