FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock* ./
COPY apps ./apps
COPY packages ./packages
COPY tests ./tests

RUN uv sync --no-dev

ENV PATH="/app/.venv/bin:${PATH}"
