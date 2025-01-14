from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    """Configuration for running on local machine"""

    host: str = "localhost"
    port: int = 8000
    reload: bool = True


class CorsConfig(BaseModel):
    """Configuration for CORS policy"""

    allowed_origins: list[str]
    allow_credentials: bool = True
    allowed_methods: list[str] = ["GET", "POST", "PATCH"]
    allowed_headers: list[str] = ["*"]


class DatabaseSettings(BaseModel):
    """Database configuration"""

    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    """Application settings"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BACKEND_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
    )

    db: DatabaseSettings

    cors: CorsConfig

    run: RunConfig = RunConfig()


settings = Settings()
