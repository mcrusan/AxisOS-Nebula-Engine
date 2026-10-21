# ==============================================================================
# File: Dockerfile
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: Container image for deploying AxisOS Nebula Engine on Nebius
#              Serverless Endpoints or local sovereign edge hardware.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Created production Dockerfile.
# ==============================================================================
FROM python:3.11-slim

LABEL maintainer="Marc F. Crusan / Crusan & Co. w/ AGY"
LABEL org.opencontainers.image.title="AxisOS Nebula Engine"
LABEL org.opencontainers.image.description="Sovereign Multi-Agent Orchestrator Powered by Nebius Token Factory & NVIDIA Nemotron"
LABEL org.opencontainers.image.vendor="Crusan & Co."

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    APP_PORT=8090

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app/src/
COPY infra/ /app/infra/
COPY scripts/ /app/scripts/
COPY README.md LICENSE /app/

EXPOSE 8090

CMD ["uvicorn", "nebula_engine.main:app", "--host", "0.0.0.0", "--port", "8090"]
