from metrics.http_metrics import HTTP_REQUESTS_TOTAL, HTTP_REQUEST_DURATION_SECONDS, REQUEST_SIZE , RESPONSE_SIZE
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        path = request.url.path
        start_time = time.perf_counter()

        request_body = await request.body()
        request_size = len(request_body)

        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        async def new_body_iterator():
            yield response_body
            
        response.body_iterator = new_body_iterator()
        response_size = len(response_body)

        duration = time.perf_counter() - start_time
        status_code = response.status_code

        HTTP_REQUESTS_TOTAL.labels(method=method, endpoint=path, status_code=status_code).inc()
        HTTP_REQUEST_DURATION_SECONDS.labels(method=method, endpoint=path, status_code=status_code).observe(duration)

        REQUEST_SIZE.labels(method=method, endpoint=path, status_code=status_code).observe(request_size)
        RESPONSE_SIZE.labels(method=method, endpoint=path, status_code=status_code).observe(response_size)


        return response