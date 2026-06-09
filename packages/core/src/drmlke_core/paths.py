from pathlib import Path

from drmlke_core.config import settings


def storage_root() -> Path:
    return Path(settings.storage_root)


def sqlite_path() -> Path:
    return Path(settings.sqlite_path)
