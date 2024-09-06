from crud.base import CRUDBase
from models import Good


class CRUDCity(CRUDBase):
    """Класс для расширения стандартных
    CRUD операций с БД для модели Good.
    """

    pass


good_crud = CRUDCity(Good)
