from fastapi import APIRouter

from app.api.v1.endpoints.qa import router as qa_router
from app.api.v1.endpoints.system import router as system_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(system_router)
api_router.include_router(qa_router)
