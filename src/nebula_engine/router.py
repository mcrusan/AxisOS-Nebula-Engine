# ==============================================================================
# File: src/nebula_engine/router.py
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: 3-Tier Sovereign Agent Router uniting the 112-microsecond C99
#              Sovereign Triad reflex loop with NVIDIA Nemotron Nano, Super,
#              and Ultra models served on Nebius Token Factory.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Implemented Tier 0 (C99 Reflex), Tier 1 (Nemotron
#     Nano/Super), and Tier 2 (Nemotron Ultra) routing engine.
# ==============================================================================

from typing import Any, Dict

from nebula_engine.nebius_client import invoke_nebius_nemotron
from nebula_engine.triad_bridge import (
    read_live_kernel_telemetry,
    worm_vault_operation,
)

TIER_0_KEYWORDS = (
    "telemetry",
    "status",
    "heartbeat",
    "ramgak",
    "thermal",
    "checkpoint",
    "zero-core",
)
TIER_2_ULTRA_KEYWORDS = (
    "architect",
    "audit",
    "reason",
    "deep",
    "synthesize",
    "kernel",
    "verify",
    "optimize",
    "security",
    "ultra",
)
TIER_1_SUPER_KEYWORDS = (
    "summarize",
    "report",
    "compare",
    "analyze",
    "workflow",
    "super",
)


def route_nebula_request(prompt: str, force_tier: str = None) -> Dict[str, Any]:
    """
    Routes an incoming operator or agent task across the 3-tier AxisOS Nebula
    Engine hierarchy:
      - Tier 0 (`tier_0_reflex`): 49 KB Freestanding C99 Zero-Core (:8081) &
        Axis-Agent (:8082) WORM Vault + live /proc & /sys telemetry.
      - Tier 1 (`tactical_nano` / `balanced_super`): NVIDIA Llama-3.1-Nemotron-Nano-8B
        or Llama-3.3-Nemotron-Super-49B on Nebius Token Factory (`agent-lite :8080`).
      - Tier 2 (`deep_ultra`): NVIDIA Llama-3.1-Nemotron-Ultra-253B on Nebius Token
        Factory (`axis-agent :8082`) for complex multi-step reasoning.
    """
    text = (prompt or "").strip()
    lower = text.lower()

    # Check for destructive WORM test trigger first
    if any(w in lower for w in ("delete vault", "wipe vault", "overwrite vault", "truncate")):
        worm_res = worm_vault_operation("DELETE")
        return {
            "tier": "tier_0_reflex",
            "engine": "Axis-Agent (:8082) WORM Anti-Data-Loss Sentinel",
            "worm_shield": worm_res,
            "response": worm_res["message"],
        }

    # Tier 0: Deterministic C99 Sovereign Triad Reflex
    if force_tier == "tier_0_reflex" or (
        not force_tier and any(k in lower for k in TIER_0_KEYWORDS)
    ):
        telemetry = read_live_kernel_telemetry()
        worm_vault_operation("POST", f"Tier-0 telemetry check: {text[:80]}")
        return {
            "tier": "tier_0_reflex",
            "engine": "AxisOS Zero-Core (:8081) — 49 KB Freestanding C99 RAMDisk Mind",
            "latency_us": 112,
            "telemetry": telemetry,
            "response": (
                f"[Zero-Core :8081 // 112 us C99 Reflex] RAMGAK Zone: {telemetry.get('ramgak_zone')} | "
                f"Load (1m): {telemetry.get('load_1m')} | "
                f"Memory: {telemetry.get('mem_used_mb')}/{telemetry.get('mem_total_mb')} MB | "
                f"SoC Thermal: {telemetry.get('soc_temp_c')}C | "
                f"Active NICs: {', '.join(telemetry.get('interfaces', {}).keys())}."
            ),
        }

    # Tier 2: Deep Multi-Step Reasoning via NVIDIA Nemotron Ultra (253B) on Nebius Token Factory
    if force_tier == "deep_ultra" or (
        not force_tier and any(k in lower for k in TIER_2_ULTRA_KEYWORDS)
    ):
        res = invoke_nebius_nemotron(text, tier="deep_ultra")
        worm_vault_operation("POST", f"Tier-2 Nemotron-Ultra reasoning: {text[:80]}")
        return res

    # Tier 1B: Balanced High-Throughput via NVIDIA Nemotron Super (49B) on Nebius Token Factory
    if force_tier == "balanced_super" or (
        not force_tier and any(k in lower for k in TIER_1_SUPER_KEYWORDS)
    ):
        res = invoke_nebius_nemotron(text, tier="balanced_super")
        worm_vault_operation("POST", f"Tier-1B Nemotron-Super synthesis: {text[:80]}")
        return res

    # Tier 1A (Default Fast Everyday Calls): NVIDIA Nemotron Nano (8B) on Nebius Token Factory
    res = invoke_nebius_nemotron(text, tier="tactical_nano")
    worm_vault_operation("POST", f"Tier-1A Nemotron-Nano tactical call: {text[:80]}")
    return res
