clone the github repo: 
   git clone https://github.com/Nabinchowdhury/fastapi-metrics-app.git

To run the project:
    cd fastapi-metrics-app
    docker-compose up --build

prometheus pprt : 9090
fast-api-app port: 8000

To check metrics 

### System Metrics Implementation
- **CPU Metrics**
  1. `process_cpu_seconds_total`: Total CPU time consumed by the process
  ![alt text](image-7.png)
  2. CPU usage rate calculation: `rate(process_cpu_seconds_total[5m])`
  ![alt text](image-8.png)
  3. CPU utilization percentage tracking: `avg_over_time(system_cpu_usage_percent[5m])`
  ![alt text](image-10.png)

  **Memory Metrics**
  1. `process_resident_memory_bytes`: Physical memory currently used
  ![alt text](image-11.png)
  2. `process_virtual_memory_bytes`: Virtual memory allocated
  ![alt text](image-12.png)
  3. Memory usage trends and alerting thresholds
    `system_memory_usage_percent`
    ![alt text](image-13.png)

    `avg_over_time(system_memory_usage_percent[5m])`
    ![alt text](image-14.png)

**Additional System Metrics**
  1. Process start time and uptime
    `process_start_time_seconds`
    ![alt text](image-15.png)
    `time() - process_start_time_seconds`
    ![alt text](image-16.png)

  - File descriptor usage
  - Garbage collection statistics
  - Thread count monitoring

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

    2. 95th percentile latency: `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{endpoint="/metrics",method="GET"}[5m])) by (le))`
    ![alt text](image-4.png)

    3. Request size Histogram `http_request_size_bytes_bucket`
    ![alt text](image-5.png)

    4. Response size Histogram `http_response_size_bytes_bucket`
    ![alt text](image-6.png)