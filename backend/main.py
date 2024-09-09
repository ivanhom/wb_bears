import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router
from core.config import settings
from scheduled_tasks import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер для управления жизненным
    циклом приложения.
    Этот менеджер запускает планировщик задач при старте приложения и
    завершает его выполнение при остановке приложения.
    """
    asyncio.create_task(scheduler())
    yield


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    lifespan=lifespan,
)

app.include_router(router)
