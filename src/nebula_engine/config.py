# ==============================================================================
# File: src/nebula_engine/config.py
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: Configuration loader for Nebius Token Factory, NVIDIA Nemotron
#              model tiers, and AxisOS Sovereign Triad endpoints.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Created NebulaConfig dataclass.
# ==============================================================================

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class NebulaConfig:
    app_env: str = os.getenv("APP_ENV", "production")
    app_port: int = int(os.getenv("APP_PORT", "8090"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Nebius Token Factory & AI Cloud
    nebius_api_key: str = os.getenv("NEBIUS_API_KEY", "your_nebius_token_factory_api_key_here")
    nebius_base_url: str = os.getenv("NEBIUS_BASE_URL", "https://api.studio.nebius.com/v1")
    nebius_serverless_endpoint: str = os.getenv(
        "NEBIUS_SERVERLESS_ENDPOINT", "https://serverless.nebius.ai/v1/axisos-nebula"
    )

    # NVIDIA Open-Source Model Tiers on Nebius Token Factory
    model_nano: str = os.getenv("NVIDIA_MODEL_NANO", "nvidia/Llama-3_1-Nemotron-Nano-8B-v1")
    model_super: str = os.getenv("NVIDIA_MODEL_SUPER", "nvidia/Llama-3_3-Nemotron-Super-49B-v1")
    model_ultra: str = os.getenv("NVIDIA_MODEL_ULTRA", "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1")

    # AxisOS Sovereign Triad Edge & Cloud Run Outpost
    zero_core_url: str = os.getenv("AXISOS_ZERO_CORE_URL", "http://192.168.1.34:8081")
    lite_url: str = os.getenv("AXISOS_LITE_URL", "http://192.168.1.34:8080")
    axis_agent_url: str = os.getenv("AXISOS_AGENT_URL", "http://192.168.1.34:8082")
    zero_comms_url: str = os.getenv("AXISOS_COMMS_URL", "http://192.168.1.34:8085")
    cloud_outpost_url: str = os.getenv(
        "AXISOS_CLOUD_OUTPOST_URL",
        "https://axisos-sovereign-triad-4zye7tn3qq-uw.a.run.app",
    )


def get_config() -> NebulaConfig:
    return NebulaConfig()
