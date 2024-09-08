from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON

from core.db import Base


class Product(Base):
    """Модель Product для БД."""

    nm_id = Column(Integer, primary_key=True)
    current_price = Column(Integer)
    sum_quantity = Column(Integer)
    quantity_by_sizes = Column(JSON)
    product_photo_url = Column(String)
