from datetime import timedelta, timezone

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройка переменных окружения для backend."""

    app_title: str
    app_description: str
    database_url: str
    moscow_tz: timezone = timezone(timedelta(hours=3))
    time_format: str
    telegram_bot_token: str
    backend_api: str
    base_url: str

    class Config:
        env_file = '../infra/.env'
        extra = 'ignore'

    @property
    def backend_api_url(self):
        return f'{self.base_url}{self.backend_api}'


settings = Settings()
