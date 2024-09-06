from typing import Optional

from pydantic import BaseModel, Field


class GoodDB(BaseModel):
    """Схема модели Good для работы с БД."""

    id: int = Field()
    name: str = Field()

    class Config:
        from_attributes = True


class GoodCreate(BaseModel):
    """Схема для создания модели Good."""

    name: str = Field()

    class Config:
        extra = 'ignore'
        str_min_length = 1


class GoodList(BaseModel):
    """Схема для отображения модели Good с пагинацией."""

    count: int = Field()
    next: Optional[str] = Field()
    previous: Optional[str] = Field()
    results: list[GoodDB]
