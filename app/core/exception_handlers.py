from datetime import datetime
import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas.common import ApiResponse, ResponseMeta

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=ApiResponse[dict](
                code=exc.status_code,
                message=str(exc.detail),
                data=None,
                # meta=ResponseMeta(
                #     request_id=getattr(request.state, "request_id", "unknown"),
                #     timestamp=datetime.now(),
                #     path=request.url.path,
                # ),
            ).model_dump(mode="json"),
        )

    @app.exception_handler(RequestValidationError)
    def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content=ApiResponse[dict](
                code=422,
                message="request validation error",
                data={"errors": exc.errors()},
                # meta=ResponseMeta(
                #     request_id=getattr(request.state, "request_id", "unknown"),
                #     timestamp=datetime.now(),
                #     path=request.url.path,
                # ),
            ).model_dump(mode="json"),
        )

    @app.exception_handler(Exception)
    def unhandled_exception_handler(request: Request, exc: Exception):
        # 1. 将真实的错误堆栈记录到日志，方便程序员排查
        logger.exception("unhandled exception: %s", exc)
        
        # 2. 给前端返回模糊的、友好的提示，保护系统安全
        return JSONResponse(
            status_code=500,
            content=ApiResponse[dict](
                code=500,
                message="当前系统繁忙，请稍后再试！",
                data=None,
                # meta=ResponseMeta(
                #     request_id=getattr(request.state, "request_id", "unknown"),
                #     timestamp=datetime.now(),
                #     path=request.url.path,
                # ),
            ).model_dump(mode="json"),
        )
