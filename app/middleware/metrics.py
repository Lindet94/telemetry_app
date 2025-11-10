import time
from fastapi import Request
from fastapi.responses import Response
from app.metrics import REQUEST_LATENCY, record_request_metrics


async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    endpoint_name = request.url.path  # Or get from request.scope.get("route").path

    # Process the request
    response = await call_next(request)

    # Calculate request duration
    request_duration = time.time() - start_time

    # Record metrics
    REQUEST_LATENCY.labels(method=request.method, endpoint=endpoint_name).observe(
        request_duration
    )

    record_request_metrics(request, response, endpoint_name)

    return response
