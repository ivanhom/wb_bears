from sqlalchemy import Column, String

from core.db import Base


class Good(Base):
    name = Column(String(100), unique=True, nullable=False)
