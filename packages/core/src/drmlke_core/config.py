from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DRMLKE_", env_file=".env", extra="ignore")

    env: str = "dev"
    node_name: str = "local-dev"
    api_port: int = 8780
    provider_port: int = 8781
    storage_root: str = ".local/drmlke"
    sqlite_path: str = ".local/drmlke/state/drmlke.sqlite"
    live_trading_enabled: bool = False
    withdrawals_enabled: bool = False
    mode: str = "paper"
    family_workspace: str = "drmlke-family"


settings = Settings()
