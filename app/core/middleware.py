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
        status_code = 500
        response = None

        try:
            response = await call_next(request)
            status_code = response.status_code
            response.headers["X-Request-Id"] = request_id
            return response
        except Exception:
            # Keep bubbling the exception to global handlers/uvicorn.
            raise
        finally:
            elapsed_ms = int((time.time() - start_time) * 1000)
            logger.info(
                # "request_id=%s status=%s method=%s path=%s duration_ms=%s",
                "status=%s path=%s duration_ms=%s",
                # request_id,
                status_code,
                # request.method,
                request.url.path,
                elapsed_ms,
            )
