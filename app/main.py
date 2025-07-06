from fastapi import FastAPI
from routers import api, health
from prometheus_client import make_asgi_app
from middleware.metrics_middleware import MetricsMiddleware


fast_api_app = FastAPI()
# fast_api_app.middleware("http")(MetricsMiddleware())
fast_api_app.add_middleware(MetricsMiddleware)

fast_api_app.include_router(api.router)
fast_api_app.include_router(health.router)

metrics_app = make_asgi_app()
fast_api_app.mount("/metrics", metrics_app)


# @app.get("/")
# async def read_root():
#     return {"Hello": "World explore"}

