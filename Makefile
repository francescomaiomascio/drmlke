.PHONY: help sync lint test check docker-base docker-provider doctor open-vscode

help:
	@printf "Targets:\n"
	@printf "  sync             Install Python workspace dependencies with uv\n"
	@printf "  lint             Run ruff checks\n"
	@printf "  test             Run pytest\n"
	@printf "  check            Run lint and tests\n"
	@printf "  docker-base      Build base image\n"
	@printf "  docker-provider  Build provider image via compose\n"
	@printf "  doctor           Run local environment checks\n"
	@printf "  open-vscode      Open this folder in VS Code\n"

sync:
	uv sync --dev

lint:
	uv run ruff check .

test:
	uv run pytest

check: lint test

docker-base:
	docker build --network=host -f infra/docker/base.Dockerfile -t drmlke/base:dev .

docker-provider:
	docker compose --profile provider build provider

doctor:
	./scripts/doctor.sh

open-vscode:
	@if command -v code >/dev/null 2>&1; then code .; else printf "Open manually: cd %s && code .\n" "$$(pwd)"; fi
