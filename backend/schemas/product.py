from pydantic import BaseModel


class ProductDB(BaseModel):
    """Схема Pydantic-модели Product для работы с БД."""

    nm_id: int
    current_price: int | None
    sum_quantity: int
    quantity_by_sizes: list[dict[str, str | list[dict[str, int]]]]
    product_photo_url: str

    class Config:
        from_attributes = True
