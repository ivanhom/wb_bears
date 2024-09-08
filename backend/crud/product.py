from crud.base import CRUDBase
from models import Product


class CRUDProduct(CRUDBase):
    """Класс для расширения стандартных
    CRUD операций с БД для модели Product.
    """

    pass


product_crud = CRUDProduct(Product)
