from fastapi import APIRouter

from api.api_v1.good import router as good_router

router = APIRouter(
    prefix='/v1',
)

router.include_router(good_router, prefix='/goods')
