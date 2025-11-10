from prometheus_client import Counter, Histogram

# Request metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP Requests", ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)


def record_request_metrics(request, response, endpoint_name):
    """Record request metrics."""
    method = request.method
    status_code = response.status_code
    REQUEST_COUNT.labels(
        method=method, endpoint=endpoint_name, status_code=status_code
    ).inc()
