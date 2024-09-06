from fastapi import APIRouter

from api.api_v1 import router as router_api_v1

router = APIRouter(prefix='/api', tags=['API'])

router.include_router(router_api_v1)
