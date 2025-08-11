
###################################################################################################
# AIAhura Tech — DevOps Technical Assessment
# Project: AI Inference Service
# This repository is part of AIAhura Tech's DevOps engineer interview process.
# All work submitted will be evaluated for technical quality, security practices, and documentation.
###################################################################################################


FROM python:3.11-slim AS builder
WORKDIR /app
COPY app/requirements.txt .

RUN pip install --upgrade pip && pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /app

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* 
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
COPY app/ ./

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

USER appuser

EXPOSE ${PORT}

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
