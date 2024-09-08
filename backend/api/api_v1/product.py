from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.utils import get_response, parse_response
from api.validators import check_product_exist
from core.db import get_async_session
from crud.product import product_crud
from schemas import ProductDB

router = APIRouter()


@router.get('/{nm_id}', response_model=ProductDB)
async def get_product(
    nm_id: str, session: AsyncSession = Depends(get_async_session)
) -> ProductDB:
    """Полученик информации о запрошенном с WB продукте по его nm_id."""
    product_info = await check_product_exist(int(nm_id), session)
    if not product_info:
        response = await get_response(nm_id)
        product_info = parse_response(response)
        await product_crud.create(product_info, session)
    return product_info
