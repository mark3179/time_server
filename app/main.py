import logging

from fastapi import FastAPI

from app.api.router import api_router
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestContextMiddleware

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title="Time Service API", version="1.0.0")
    app.add_middleware(RequestContextMiddleware)
    app.include_router(api_router)
    register_exception_handlers(app)

    @app.get("/health", tags=["health"])
    def health_check():
        logger.info("health check ok")
        return {"status": "ok"}

    return app


app = create_app()
