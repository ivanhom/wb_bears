from fastapi import APIRouter

router = APIRouter()


@router.get('/{name}')
async def get_hello(name: str) -> dict[str, str]:
    """Тестовый эндпоинт."""
    return {'hello': name}
