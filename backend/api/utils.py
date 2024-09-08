import httpx

from core.constants import HEADERS, PRODUCT_URL
from schemas import ProductDB


def get_photo_url(nm_id: int) -> str:  # noqa
    """
    Определение url, на котором хранятся первая фотография продукта.

    Параметры:
    nm_id - артикул продукта

    Артикул продукта преобразовывается в величину 'vol', по которой
    проходит сверка. В зависимости от вхождения 'vol' в нужный диапазон
    назначается номер сервера.
    """
    if type(nm_id) is not int:
        raise TypeError('nm_id должен быть целым числом')

    val = nm_id // 100_000

    if 0 <= val <= 143:
        basket_number = '01'
    elif 144 <= val <= 287:
        basket_number = '02'
    elif 288 <= val <= 431:
        basket_number = '03'
    elif 432 <= val <= 719:
        basket_number = '04'
    elif 720 <= val <= 1007:
        basket_number = '05'
    elif 1008 <= val <= 1061:
        basket_number = '06'
    elif 1062 <= val <= 1115:
        basket_number = '07'
    elif 1116 <= val <= 1169:
        basket_number = '08'
    elif 1170 <= val <= 1313:
        basket_number = '09'
    elif 1314 <= val <= 1601:
        basket_number = '10'
    elif 1602 <= val <= 1655:
        basket_number = '11'
    elif 1656 <= val <= 1919:
        basket_number = '12'
    elif 1920 <= val <= 2045:
        basket_number = '13'
    elif 2046 <= val <= 2189:
        basket_number = '14'
    elif 2190 <= val <= 2405:
        basket_number = '15'
    elif 2406 <= val <= 2621:
        basket_number = '16'
    elif 2622 <= val <= 2837:
        basket_number = '17'
    else:
        basket_number = '18'

    return (
        f'https://basket-{basket_number}.wbbasket.ru/vol{nm_id // 100_000}'
        f'/part{nm_id // 1_000}/{nm_id}/images/big/1.webp'
    )


async def get_response(nm_id: str) -> dict[str, dict]:
    """Отправка запроса к WB."""

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=PRODUCT_URL.format(nm_id), headers=HEADERS
        )
    return response.json()


def parse_response(response: dict[str, dict]) -> ProductDB:
    """Парсинг полученных данных из запроса."""

    product_data = response.get('data', {}).get('products')
    product_info = dict()
    min_price = None
    sizes_info = []

    if product_data and product_data is not None:
        product_sizes = product_data[0].get('sizes')

        if product_sizes:
            for size in product_sizes:
                name = size.get('name')
                quantity = size.get('stocks')
                quantity_by_wh = []

                if quantity and quantity is not None:
                    for warehouse in quantity:
                        warehouse_id = warehouse.get('wh')
                        warehouse_quantity = warehouse.get('qty')
                        quantity_by_wh.append(
                            {'wh': warehouse_id, 'qty': warehouse_quantity}
                        )

                if quantity_by_wh:
                    sizes_info.append(
                        {'size': name, 'quantity_by_wh': quantity_by_wh}
                    )
                    size_price = size.get('price', {}).get('total')

                    if min_price is None or size_price < min_price:
                        min_price = size_price

        product_info['nm_id'] = product_data[0].get('id')
        product_info['current_price'] = (
            int(min_price / 100) if min_price is not None else None
        )
        product_info['sum_quantity'] = product_data[0].get('totalQuantity')
        product_info['quantity_by_sizes'] = sizes_info
        product_info['product_photo_url'] = get_photo_url(
            product_info.get('nm_id')
        )

    return ProductDB(**product_info)
