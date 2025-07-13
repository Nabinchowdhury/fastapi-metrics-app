from fastapi import APIRouter, Body
# from metrics.http_metrics import request_total

router = APIRouter()

@router.get("/")
async def read_root():
    # request_total.labels(method="method", endpoint="path", status_code="status_code").inc()
    return {"Hello": 'explore'}

@router.get("/data")
async def getData():
    return {"data": 'Here is some data'}

@router.post("/data")
def create_item(item: dict = Body(...)):
    return {"message": "Item created successfully", "item": item}