from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройка переменных окружения для bot."""

    telegram_bot_token: str
    backend_api: str
    base_url: str
    redis_host: str
    redis_port: int
    redis_url: str
    rate_timeout: int = 60

    class Config:
        env_file = '../infra/.env'
        extra = 'ignore'

    @property
    def backend_api_url(self):
        return f'{self.base_url}{self.backend_api}'


settings = Settings()
