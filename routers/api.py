from fastapi import APIRouter
# from metrics.http_metrics import request_total

router = APIRouter()

@router.get("/")
async def read_root():
    # request_total.labels(method="method", endpoint="path", status_code="status_code").inc()
    return {"Hello": 'explore'}