import aiohttp
from aiogram import types
from aiogram.filters import BaseFilter
from redis.asyncio import Redis

from config import settings
from constants import OVERLIMIT_MSG

redis = Redis(
    host=settings.redis_host, port=settings.redis_port, decode_responses=True
)


class RateLimitFilter(BaseFilter):
    """Ограничитель для запросов пользователей."""

    def __init__(self, rate_timeout: int = settings.rate_timeout) -> None:
        self.rate_timeout = rate_timeout

    async def __call__(self, message: types.Message) -> bool:
        """Сохранение времени отправки сообщения пользователем
        и проверка на превышение лимита отправки.
        """
        user_id = message.from_user.id
        current_time = int(message.date.timestamp())
        redis_key = f'ratetimeout:{user_id}'

        last_request_time = await redis.get(redis_key)

        if last_request_time:
            elapsed_time = current_time - int(last_request_time)
            if elapsed_time < self.rate_timeout:
                await message.answer(
                    f'{chr(129396)} '
                    + OVERLIMIT_MSG.format(self.rate_timeout - elapsed_time)
                )
                return False

        await redis.set(redis_key, current_time, ex=self.rate_timeout)
        return True


async def get_response(nm_id: int) -> dict:
    """Отправка запроса к API."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{settings.backend_api_url}products/{nm_id}'
        ) as response:
            return await response.json()


def build_message(response: dict) -> str:
    """Сборка сообщения с информацией о продукте."""

    message = f'*Артикул:* `{response["nm_id"]}`\n'
    if response['current_price'] is not None:
        message += f'*Стоимость:* `{response["current_price"]} руб.`\n'
    else:
        message += '*Стоимость:* `Нет в наличии`\n'
    message += f'*Общее количество:* `{response["sum_quantity"]} шт.`\n\n'
    if response['sum_quantity']:
        message += '*Остатки на складах:*\n\n'

    for size in response['quantity_by_sizes']:
        if size['size']:
            message += f'_Размер {size["size"]}_\n'
        message += '```\n'
        message += f'{"Склад":<8} | {"Кол-во, шт.":<10}\n'
        message += f'{"-" * 8}-|-{"-" * 10}\n'

        for warehouse in size['quantity_by_wh']:
            message += f'{warehouse["wh"]:<8} | {warehouse["quantity"]:^10}\n'

        message += '```\n\n'

    return message
