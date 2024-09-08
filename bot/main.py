import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import settings
from constants import (
    BEGIN_MSG,
    DONE_MSG,
    HELP_MSG,
    MAX_NM_ID,
    MIN_NM_ID,
    START_MSG,
    WRONG_ID_MSG,
)
from utils import build_message, get_response

bot = Bot(
    token=settings.telegram_bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Обработчик для команды /start."""
    await message.answer(f'{chr(128075)} ' + START_MSG)


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """Обработчик для команды /help."""
    await message.answer(f'{chr(128578)} ' + HELP_MSG)


@dp.message()
async def product_handler(message: Message) -> None:
    """Обработчик для артикула продукта с WB."""
    if message.text.isnumeric() and MIN_NM_ID <= int(message.text) < MAX_NM_ID:
        nm_id = int(message.text)
        await message.answer(f'{chr(129761)} ' + BEGIN_MSG)
        response = await get_response(nm_id)

        if type(response) is str:
            await message.answer(f'{chr(128533)} ' + response)
        else:
            await bot.send_photo(
                chat_id=message.chat.id, photo=response['product_photo_url']
            )
            await message.answer(build_message(response))
            await message.answer(f'{chr(128526)} ' + DONE_MSG)
    else:
        await message.answer(f'{chr(129300)} ' + WRONG_ID_MSG)


async def main() -> None:
    """Главная функция бота."""
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
