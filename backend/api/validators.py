from sqlalchemy.ext.asyncio import AsyncSession

from crud.product import product_crud
from models import Product


async def check_product_exist(
    nm_id: str, session: AsyncSession
) -> Product | None:
    """Проверяет, что продукт уже есть в БД и возвращает его."""
    if nm_id.isnumeric():
        product = await product_crud.get_by_attribute(
            attr_name='nm_id', attr_value=int(nm_id), session=session
        )
        return product if product else None
    return None
