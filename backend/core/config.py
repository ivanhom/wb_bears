from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройка переменных окружения для backend."""

    app_title: str
    app_description: str
    database_url: str
    db_update_timer: int = 5

    class Config:
        env_file = '../infra/.env'
        extra = 'ignore'


settings = Settings()
