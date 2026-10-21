# ==============================================================================
# File: src/nebula_engine/main.py
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: FastAPI service for AxisOS Nebula Engine integrating Nebius Token
#              Factory, NVIDIA Nemotron models, and the AxisOS Sovereign Triad.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Created FastAPI application and endpoints.
# ==============================================================================

from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from nebula_engine.router import route_nebula_request
from nebula_engine.triad_bridge import (
    query_cloud_outpost,
    read_live_kernel_telemetry,
    worm_vault_operation,
)

app = FastAPI(
    title="Crusan & Co. — AxisOS Nebula Engine",
    description=(
        "Sovereign Multi-Agent Orchestrator uniting 112-us Freestanding C99 "
        "Triad Reflexes with NVIDIA Nemotron Nano, Super, and Ultra on Nebius Token Factory."
    ),
    version="1.0.0",
)


class NebulaInferenceRequest(BaseModel):
    prompt: str
    force_tier: Optional[str] = None


class WormEntryRequest(BaseModel):
    entry: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "company": "Crusan & Co.",
        "project": "AxisOS Nebula Engine",
        "pillars": ["HONEST", "AUDITABLE", "OWNED"],
        "nebius_token_factory": "CONNECTED",
        "nvidia_models": [
            "nvidia/Llama-3_1-Nemotron-Nano-8B-v1",
            "nvidia/Llama-3_3-Nemotron-Super-49B-v1",
            "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1",
        ],
    }


@app.get("/status")
def status():
    return {
        "telemetry": read_live_kernel_telemetry(),
        "worm_vault": worm_vault_operation("GET"),
    }


@app.post("/v1/nebula/infer")
def nebula_infer(req: NebulaInferenceRequest):
    return route_nebula_request(req.prompt, force_tier=req.force_tier)


@app.get("/v1/nebula/worm-vault")
def get_worm_vault():
    return worm_vault_operation("GET")


@app.post("/v1/nebula/worm-vault")
def append_worm_vault(req: WormEntryRequest):
    return worm_vault_operation("POST", req.entry)


@app.delete("/v1/nebula/worm-vault")
def delete_worm_vault():
    res = worm_vault_operation("DELETE")
    raise HTTPException(status_code=403, detail=res)


@app.get("/v1/nebula/cloud-outpost")
def cloud_outpost_status():
    return query_cloud_outpost()
