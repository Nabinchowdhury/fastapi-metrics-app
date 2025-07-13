from prometheus_client import Counter, Histogram

HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total number of request",
    ["method", "endpoint", "status_code"]
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "http_request_duration_seconds", 
    "HTTP request durations",
    ["method", "endpoint", "status_code"],
    buckets=[0.1, 0.3, 0.5, 1.0, 2.0, 5.0]
)