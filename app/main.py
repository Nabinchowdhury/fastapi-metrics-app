from fastapi import FastAPI
from routers import api


fast_api_app = FastAPI()

fast_api_app.include_router(api.router)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World explore"}

