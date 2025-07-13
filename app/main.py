from fastapi import FastAPI
from routers import api, health
from prometheus_client import make_asgi_app, generate_latest, CONTENT_TYPE_LATEST
from middleware.metrics_middleware import MetricsMiddleware
from metrics.system_metrics import collect_system_metrics
from fastapi.responses import Response


fast_api_app = FastAPI()
# fast_api_app.middleware("http")(MetricsMiddleware())
fast_api_app.add_middleware(MetricsMiddleware)

fast_api_app.include_router(api.router)
fast_api_app.include_router(health.router)

# metrics_app = make_asgi_app()
# fast_api_app.mount("/metrics", metrics_app)
@fast_api_app.get("/metrics")
def metrics():
    collect_system_metrics()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    return {"data": 'Here is some data'}



# @app.get("/")
# async def read_root():
#     return {"Hello": "World explore"}

