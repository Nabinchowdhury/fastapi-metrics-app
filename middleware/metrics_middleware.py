from metrics.http_metrics import request_total
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        path = request.url.path
        start_time = time.perf_counter()

        response = await call_next(request)

        duration = time.perf_counter() - start_time
        status_code = response.status_code

        request_total.labels(method=method, endpoint=path, status_code=status_code).inc()
        # HTTP_REQUEST_DURATION_SECONDS.labels(method=method, endpoint=path).observe(duration)

        return response