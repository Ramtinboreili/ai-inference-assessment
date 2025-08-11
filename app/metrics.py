
###################################################################################################
# AIAhura Tech — DevOps Technical Assessment
# Project: AI Inference Service
# This repository is part of AIAhura Tech's DevOps engineer interview process.
# All work submitted will be evaluated for technical quality, security practices, and documentation.
###################################################################################################

from prometheus_client import Counter, Histogram
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests",
    ["endpoint", "method"]
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"],
    buckets=(0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, float("inf"))
)