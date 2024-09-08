import aiohttp

from config import settings


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
