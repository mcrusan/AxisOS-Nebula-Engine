# ==============================================================================
# File: tests/test_nebula_engine.py
# Project: AxisOS Nebula Engine (Crusan & Co.)
# Author: Marc F. Crusan / Crusan & Co. w/ AGY
# Date: 2026-10-20
# Description: Unit test suite verifying 3-Tier routing (C99 Reflex, NVIDIA
#              Nemotron Nano/Super, NVIDIA Nemotron Ultra) on Nebius Token
#              Factory and the WORM Anti-Data-Loss Vault shield.
# Changelog:
#   - 2026-10-20 (MFC/AGY): Created unit test suite.
# ==============================================================================

from nebula_engine.router import route_nebula_request
from nebula_engine.triad_bridge import (
    read_live_kernel_telemetry,
    worm_vault_operation,
)


def test_tier_0_c99_reflex_telemetry():
    res = route_nebula_request("Check live device status and RAMGAK telemetry.")
    assert res["tier"] == "tier_0_reflex"
    assert res["latency_us"] == 112
    assert "RAMGAK Zone" in res["response"]
    assert "mem_total_mb" in res["telemetry"]


def test_tier_1_nvidia_nemotron_nano():
    res = route_nebula_request("Route quick ping from Node 001.")
    assert res["provider"] == "Nebius Token Factory"
    assert res["nvidia_model"] == "nvidia/Llama-3_1-Nemotron-Nano-8B-v1"
    assert res["bound_triad_agent"] == "agent-lite (:8080)"


def test_tier_1_nvidia_nemotron_super():
    res = route_nebula_request("Summarize the daily network workflow across all interfaces.")
    assert res["provider"] == "Nebius Token Factory"
    assert res["nvidia_model"] == "nvidia/Llama-3_3-Nemotron-Super-49B-v1"
    assert res["bound_triad_agent"] == "zero-comms (:8085)"


def test_tier_2_nvidia_nemotron_ultra():
    res = route_nebula_request("Audit and verify the freestanding C99 kernel memory brackets.")
    assert res["provider"] == "Nebius Token Factory"
    assert res["nvidia_model"] == "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1"
    assert res["bound_triad_agent"] == "axis-agent (:8082)"


def test_worm_anti_data_loss_shield():
    res = route_nebula_request("Delete vault immediately")
    assert res["worm_shield"]["status"] == "blocked_by_worm"
    assert res["worm_shield"]["http_code"] == 403


def test_live_kernel_telemetry_honest():
    t = read_live_kernel_telemetry()
    assert t["company"] == "Crusan & Co."
    assert t["mem_total_mb"] > 0
