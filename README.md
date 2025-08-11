# AI Inference Service - AIAhura Tech DevOps Assessment

## Overview
This repo hosts the AI Inference Service for AIAhura Tech's DevOps interview process, showcasing containerization, CI/CD, and monitoring skills.

## Project Details

- **Docker**: Multi-stage Dockerfile (non-root, pinned deps) + `docker-compose.yml` (services, healthchecks, ports, limits).
- **Features**: `/healthz`, `/metrics` (prometheus_client), request instrumentation (`metrics.py`: Counter, Histogram), Redis-based rate limiting (`rate_limit.py` decorator) for `/predict`.
- **Monitoring**: Prometheus scraping (updated `prometheus.yml`), Grafana with datasource (optional dashboard).
- **CI/CD**: GitHub Actions (`ci.yml`) for linting, testing, building, and pushing to GHCR on `main`.
- **Docs**: README covers trade-offs and troubleshooting.

## Getting Started

### Prerequisites
- Docker, Docker Compose
- GitHub account with GHCR access

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/ramtinboreili/ai-inference-assessment.git
   cd ai-inference-assessment
