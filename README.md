# AI Inference Service - AIAhura Tech DevOps Assessment

## Overview
This repo hosts the AI Inference Service for AIAhura Tech's DevOps interview process, showcasing containerization, CI/CD, and monitoring skills.

## Project Details

- **Docker**: Multi-stage Dockerfile (non-root, pinned deps) + `docker-compose.yml` (services, healthchecks, ports, limits).
- **Features**: `/healthz`, `/metrics` (prometheus_client), request instrumentation (`metrics.py`: Counter, Histogram), Redis-based rate limiting (`rate_limit.py` decorator) for `/predict`.
- **Monitoring**: Prometheus scraping (updated `prometheus.yml`), Grafana with datasource (debug dashboards and `datasource.yml`).
- **Traefik**: Used as a domain resolver for  `grafana`, and `prometheus` with custom domains.
- **CI/CD**: GitHub Actions (`ci.yml`) for linting, testing, building, and pushing to GHCR on `main` and deploy on server.
- **Docs**: README covers trade-offs and troubleshooting.

## Domains
- App (metrics): [http://157.245.68.163:8000/metrics](http://157.245.68.163:8000/metrics)
- App (healthz): [http://157.245.68.163:8000/healthz](http://157.245.68.163:8000/healthz)
- Grafana: [https://grafana.ramtinboreili.ir](https://grafana.ramtinboreili.ir/) (admin/ZlYHCAsr96zD0W)
- Prometheus: [https://prom.ramtinboreili.ir ](https://prom.ramtinboreili.ir/)

Contributing
Mr.mohamad sadr

License
Part of AIAhura Tech assessment process.

Acknowledgments
Thanks to AIAhura Tech for this DevOps challenge!

**Ramtin Boreili**
