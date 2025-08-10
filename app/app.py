
###################################################################################################
# AIAhura Tech — DevOps Technical Assessment
# Project: AI Inference Service
# This repository is part of AIAhura Tech's DevOps engineer interview process.
# All work submitted will be evaluated for technical quality, security practices, and documentation.
###################################################################################################


import os
import time
import logging
import json
from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel

# TODO: once implemented, import metrics & limiter
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, REGISTRY
from metrics import REQUEST_COUNT, REQUEST_LATENCY
from rate_limit import rate_limiter

class JsonFormatter(logging.Formatter):
 def format(self, record):
    payload = {
       "ts": int(time.time() * 1000),
       "level": record.levelname,
       "msg": record.getMessage(),
       "logger": record.name,
    }
    if record.exc_info:
        payload["exc_info"] = self.formatException(record.exc_info)
    return json.dumps(payload)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger = logging.getLogger("app")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
logger.addHandler(handler)
logger.propagate = False

app = FastAPI()
PORT = int(os.getenv("PORT", "8000"))
RATE_LIMIT_PER_MIN = int(os.getenv("RATE_LIMIT_PER_MIN", "60"))

class PredictIn(BaseModel):
 text: str

@app.get("/healthz")
def healthz():
    REQUEST_COUNT.labels(endpoint="/healthz", method="GET").inc()
    with REQUEST_LATENCY.labels(endpoint="/healthz").time():
        return {"status": "ok"}

@app.get("/metrics")
def metrics():
        REQUEST_COUNT.labels(endpoint="/metrics", method="GET").inc()
        with REQUEST_LATENCY.labels(endpoint="/metrics").time():
 # TODO: return Prometheus metrics once metrics are implemented
          return JSONResponse({"detail": "metrics not implemented"}, status_code=501)

@app.post("/predict")
# TODO: decorate with @rate_limiter(max_per_min=RATE_LIMIT_PER_MIN) after implementing
@rate_limiter(max_per_min=RATE_LIMIT_PER_MIN)
async def predict(payload: PredictIn, request: Request):
    REQUEST_COUNT.labels(endpoint="/predict", method="POST").inc()
    with REQUEST_LATENCY.labels(endpoint="/predict").time():
    # TODO: once metrics exist, start a timer and observe latency; increment request counter
        txt = payload.text.lower()
        label = "positive" if any(k in txt for k in ["good", "great", "love", "awesome"]) else "negative"
        logger.info(json.dumps({"path": "/predict", "label": label}))
        return JSONResponse({"label": label})
