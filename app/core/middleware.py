import logging
import time
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-Id", str(uuid4()))
        request.state.request_id = request_id
        start_time = time.time()

        response = await call_next(request)

        elapsed_ms = int((time.time() - start_time) * 1000)
        response.headers["X-Request-Id"] = request_id
        logger.info(
            # "request_id=%s status=%s method=%s path=%s duration_ms=%s",
            "status=%s path=%s duration_ms=%s",
            # request_id,
            response.status_code,
            # request.method,
            request.url.path,
            elapsed_ms,
        )
        return response
