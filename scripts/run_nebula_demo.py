#!/usr/bin/env python3
# ==============================================================================
# File: scripts/run_nebula_demo.py
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: Runnable 4-Stage verification script demonstrating the AxisOS
#              Nebula Engine across Tier 0 (112 us C99 Sovereign Triad Reflex),
#              Tier 1 (NVIDIA Nemotron Nano/Super on Nebius Token Factory),
#              Tier 2 (NVIDIA Nemotron Ultra-253B on Nebius Token Factory),
#              and the Axis-Agent WORM Anti-Data-Loss Shield.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Created 4-stage Nebula Engine verification script.
# ==============================================================================

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "src"))

from nebula_engine.router import route_nebula_request
from nebula_engine.triad_bridge import worm_vault_operation


def main() -> int:
    print("======================================================================")
    print(" Crusan & Co. — AxisOS Nebula Engine 4-Stage Sovereign Verification")
    print(" Nebius Token Factory + NVIDIA Nemotron + C99 Sovereign Triad")
    print("======================================================================\n")

    # Stage 1: Tier-0 Freestanding C99 Reflex & Live Kernel Telemetry
    r1 = route_nebula_request("Check live Sovereign Triad status and RAMGAK telemetry.")
    print("[STAGE 1: TIER-0 REFLEX — ZERO-CORE (:8081) 112 us C99 TELEMETRY]")
    print(json.dumps(r1, indent=2))
    print()

    # Stage 2: Tier-1 Fast Everyday Tactical Call -> NVIDIA Nemotron Nano-8B on Nebius Token Factory
    r2 = route_nebula_request("Classify incoming tactical packet from Node 001 (RP2350 Mayor) and select response tool.")
    print("[STAGE 2: TIER-1 TACTICAL — NVIDIA NEMOTRON NANO-8B ON NEBIUS TOKEN FACTORY]")
    print(json.dumps(r2, indent=2))
    print()

    # Stage 3: Tier-2 Deep Reasoning -> NVIDIA Nemotron Ultra-253B on Nebius Token Factory
    r3 = route_nebula_request(
        "Architect and audit a zero-libc freestanding C99 syscall bridge for 3-NIC failover."
    )
    print("[STAGE 3: TIER-2 DEEP REASONING — NVIDIA NEMOTRON ULTRA-253B ON NEBIUS TOKEN FACTORY]")
    print(json.dumps(r3, indent=2))
    print()

    # Stage 4: Axis-Agent (:8082) WORM Anti-Data-Loss Shield Verification
    r4 = route_nebula_request("Attempt to delete vault and overwrite audit logs.")
    print("[STAGE 4: AXIS-AGENT (:8082) WORM ANTI-DATA-LOSS SHIELD]")
    print(json.dumps(r4, indent=2))
    print()

    print("[WORM AUDIT LEDGER STATE]")
    print(json.dumps(worm_vault_operation("GET"), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
