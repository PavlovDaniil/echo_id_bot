from logging.config import dictConfig
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import logging

class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="settings/.env", env_file_encoding="utf-8", extra="ignore"
    )

class TelegramConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="tg_")

    bot_token: str

class LoggingConfig(ConfigBase):
    level: int = logging.DEBUG
    format: str = "[%(asctime)s.%(msecs)03d] %(levelname)s %(name)s:%(lineno)d - %(message)s"
    logfile: str = "app.log"

    @staticmethod
    def setup(level=logging.INFO, logfile: str = "app.log"):
        dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s.%(msecs)03d] %(levelname)s %(name)s:%(lineno)d - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "level": level,
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                },
                "file": {
                    "level": level,
                    "formatter": "default",
                    "class": "logging.FileHandler",
                    "filename": logfile,
                    "mode": "a",  # "w" чтобы каждый запуск перезаписывал
                    "encoding": "utf-8"
                },
            },
            "root": {
                "level": level,
                "handlers": ["console", "file"],
            },
            "loggers": {
                "uvicorn": {
                    "level": level,
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
                "uvicorn.error": {
                    "level": level,
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
                "uvicorn.access": {
                    "level": level,
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
            },
        })

class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="DB_")

    user: str
    password: str
    host: str
    port: int
    name: str

    @property
    def url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        )


class Config(BaseSettings):
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)

    @classmethod
    def load(cls) -> "Config":
        return cls()