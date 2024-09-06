from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройка переменных окружения для bot."""

    telegram_bot_token: str
    backend_api: str = 'api/v1/'
    base_url: str

    class Config:
        env_file = '../infra/.env'
        extra = 'ignore'

    @property
    def backend_api_url(self):
        return f'{self.base_url}{self.backend_api}'


settings = Settings()
