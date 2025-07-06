from prometheus_client import Counter

request_total = Counter(
    "http_requests_total",
    "Total number of request",
    ["method", "endpoint", "status_code"]
)