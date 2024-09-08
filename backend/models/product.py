from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSON

from core.db import Base


class Product(Base):
    """Модель Product для БД."""

    nm_id = Column(Integer, primary_key=True)
    data = Column(JSON)
