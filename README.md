To run the project:
    docker-compose up --build

To check metrics 
### HTTP Application Metrics: 

- **Request Volume Metrics**

    1. `http_requests_total`
    ![alt text](image-1.png)

    2. `http_requests_total{endpoint="/metrics",method="GET"}`
    ![alt text](image.png)

    3. Global request rate: `rate(http_requests_total[5m])`
    ![alt text](image-1.png)

    4. Per-endpoint request rates:  `sum(rate(http_requests_total[5m])) by (endpoint)`
    ![alt text](image-2.png)

- **Request Performance Metrics**
    1. Histogram of request durations: `http_request_duration_seconds_bucket`
    ![alt text](image-3.png)

    2. 95th percentile latency:
    ![alt text](image-4.png)