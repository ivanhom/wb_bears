import asyncio
import logging
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from api.utils import get_response, parse_response
from core.config import settings
from core.constants import DB_UPDATED_MSG
from core.db import get_async_session
from crud.product import product_crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def update_db(session: AsyncSession) -> None:
    """Обновление всех записей в БД."""

    all_products = await product_crud.get_multi(session)
    all_products_len = len(all_products)

    if all_products_len:
        for product in all_products:
            new_product_info = await get_response(product.nm_id)
            new_product_info = parse_response(new_product_info)
            await product_crud.update(
                product, new_product_info, session, is_committed=False
            )
        logger.info(DB_UPDATED_MSG.format(all_products_len))


async def scheduler() -> None:
    """Планировщик задач для заданного временного интервала."""
    while True:
        now = datetime.now()
        next_run = now + timedelta(minutes=settings.db_update_timer)

        sleep_time = (next_run - now).total_seconds()
        await asyncio.sleep(sleep_time)

        session_gen = get_async_session()
        session = await anext(session_gen)
        async with session.begin() as transaction:
            await update_db(transaction.session)
