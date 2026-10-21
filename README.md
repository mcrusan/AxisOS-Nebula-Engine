<!--
==============================================================================
File: README.md
Project: AxisOS Nebula Engine (Crusan & Co.)
Author: Marc F. Crusan / Crusan & Co. w/ AGY
Date: 2026-10-20
Description: Production README for AxisOS Nebula Engine — Nebius x NVIDIA
             Global AI Hackathon Submission.
Changelog:
  - 2026-10-20 (MFC/AGY): Created complete technical README with MIT license
    badge, Nebius Token Factory + NVIDIA Nemotron architecture, and setup guide.
==============================================================================
-->

# Crusan & Co. — AxisOS Nebula Engine
### **Sovereign Multi-Agent Orchestrator Powered by Nebius Token Factory, NVIDIA Nemotron & the Freestanding C99 AxisOS Triad**

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Pillars: HONEST • AUDITABLE • OWNED](https://img.shields.io/badge/AxisOS-HONEST%20%E2%80%A2%20AUDITABLE%20%E2%80%A2%20OWNED-brightgreen.svg)](https://axisos.pro)

**Parent Entity:** Crusan & Co.  
**Flagship Platform:** AxisOS (`HONEST` • `AUDITABLE` • `OWNED`)  
**Architect:** Marc F. Crusan (w/ AGY)  
**Hackathon:** Nebius x NVIDIA Global AI Hackathon  
**Open Source License:** [MIT License](LICENSE) *(Visible at top of repository)*  

---

## 1. Executive Summary

> *"Build a working AI system on open, independent infrastructure, and own the whole thing."*

**AxisOS Nebula Engine** (built by **Crusan & Co.**) is a sovereign, multi-tier agentic operating engine that unites **100% freestanding, zero-`libc` C99 edge & cloud binaries (`~112 µs` reflex latency)** with **NVIDIA's open-source Nemotron model family (`Llama-3.1-Nemotron-Ultra-253B`, `Llama-3.3-Nemotron-Super-49B`, and `Llama-3.1-Nemotron-Nano-8B`)** served on **Nebius Token Factory** and **Nebius Serverless Endpoints**.

Most agent frameworks suffer from two fatal flaws: they waste massive LLM compute on trivial telemetry checks, and they run atop bloated, opaque middleware that operators do not truly own. **AxisOS Nebula Engine** solves both through a **3-Tier Sovereign Routing Hierarchy**:

1. **Tier 0 — `112 µs` Freestanding C99 Reflex (`zero-core :8081` & `axis-agent :8082` WORM Vault)**:
   - Deterministic system telemetry (`/proc/loadavg`, `/proc/meminfo`, `/sys/class/thermal`, `/proc/net/dev`), `RAMGAK`-bracketed DDR4 memory checks, and Write-Once-Read-Many (**WORM**) Anti-Data-Loss enforcement execute natively in **49 KB of freestanding C99 (`svc #0` / `syscall`)** in **112 microseconds**—burning zero GPU tokens.
2. **Tier 1 — Fast Everyday Tactical Intelligence (`agent-lite :8080` & `zero-comms :8085` -> NVIDIA Nemotron Nano-8B & Super-49B on Nebius Token Factory)**:
   - High-frequency intent classification, mesh node coordination (`Node 001` RP2350 Mayor `[💃🍪🕺]`), and daily workflow synthesis route to **`nvidia/Llama-3_1-Nemotron-Nano-8B-v1`** and **`nvidia/Llama-3_3-Nemotron-Super-49B-v1`** via **Nebius Token Factory** (`https://api.studio.nebius.com/v1`), keeping responses sub-second and stretching inference credits to the maximum.
3. **Tier 2 — Deep Multi-Step Reasoning (`axis-agent :8082` -> NVIDIA Nemotron Ultra-253B on Nebius Token Factory)**:
   - Complex architectural synthesis, bare-metal C99 code auditing, and multi-agent recovery planning escalate automatically to **`nvidia/Llama-3_1-Nemotron-Ultra-253B-v1`** on **Nebius Token Factory**.

---

## 2. System Architecture

```text
                   ┌────────────────────────────────────────────────────────┐
                   │          Operator / Edge Mesh / API Ingress            │
                   │   AxisOS Console (axisos.pro) • Node 001 [💃🍪🕺]      │
                   └───────────────────────────┬────────────────────────────┘
                                               │
                                               ▼
                   ┌────────────────────────────────────────────────────────┐
                   │         AxisOS Nebula Engine 3-Tier Router             │
                   │   Deterministic Intent & Complexity Classifier         │
                   └──────┬────────────────────┬─────────────────────┬──────┘
                          │                    │                     │
         ┌────────────────┘                    │                     └────────────────┐
         ▼                                     ▼                                      ▼
┌─────────────────────────┐       ┌──────────────────────────┐       ┌──────────────────────────┐
│ TIER 0: C99 REFLEX      │       │ TIER 1: TACTICAL NANO    │       │ TIER 2: DEEP REASONING   │
│ • zero-core (:8081)     │       │ • Nebius Token Factory   │       │ • Nebius Token Factory   │
│ • 49 KB Freestanding C99│       │ • Nemotron-Nano-8B-v1    │       │ • Nemotron-Ultra-253B-v1 │
│ • 112 us DDR4 RAMDisk   │       │ • Nemotron-Super-49B-v1  │       │ • Multi-step code &      │
│ • Live /proc & /sys     │       │ • Bound: agent-lite:8080 │       │   architecture synthesis │
└────────────┬────────────┘       └────────────┬─────────────┘       └────────────┬─────────────┘
             │                                 │                                  │
             └─────────────────────────────────┼──────────────────────────────────┘
                                               ▼
                   ┌────────────────────────────────────────────────────────┐
                   │     Axis-Agent (:8082) WORM Anti-Data-Loss Vault       │
                   │  Strict Append-Only Ledger (HTTP 403 on DELETE/WIPE)   │
                   └────────────────────────────────────────────────────────┘
```

---

## 3. Quick Start & Verification

### 1. Clone & Configure Environment
```bash
git clone https://github.com/mcrusan/AxisOS-Nebula-Engine.git
cd AxisOS-Nebula-Engine
cp .env.example .env
# Add your NEBIUS_API_KEY in .env (or run in built-in deterministic audit mode)
```

### 2. Run the 4-Stage Sovereign Verification Demo
```bash
PYTHONPATH=src python3 scripts/run_nebula_demo.py
```
This executes all four stages:
- **Stage 1 (`Tier 0`)**: Reads live `/proc` and `/sys` kernel telemetry via the `zero-core` reflex bridge (`112 µs` latency, `RAMGAK` memory bracket, SoC thermal `°C`, `3-NIC` packet counters).
- **Stage 2 (`Tier 1`)**: Dispatches a fast tactical classification call to **`nvidia/Llama-3_1-Nemotron-Nano-8B-v1`** on **Nebius Token Factory** via `agent-lite (:8080)`.
- **Stage 3 (`Tier 2`)**: Escalates a complex kernel & 3-NIC failover audit to **`nvidia/Llama-3_1-Nemotron-Ultra-253B-v1`** on **Nebius Token Factory** via `axis-agent (:8082)`.
- **Stage 4 (`WORM Shield`)**: Proves that destructive `DELETE` / `OVERWRITE` commands against the audit vault are deterministically rejected (`HTTP 403 blocked_by_worm`).

### 3. Run the Unit Test Suite
```bash
PYTHONPATH=src pytest -v
```

### 4. Start the FastAPI Nebula Server
```bash
PYTHONPATH=src uvicorn nebula_engine.main:app --host 0.0.0.0 --port 8090
```

---

## 4. Live Links & Resources
- **Live Sovereign Triad Outpost (`127 KB` uncompressed / `87 KB` compressed `FROM scratch` C99 container):** [https://axisos-sovereign-triad-4zye7tn3qq-uw.a.run.app](https://axisos-sovereign-triad-4zye7tn3qq-uw.a.run.app)
- **Live AxisOS Fleet Deck & Console:** [https://axisos.pro/console/](https://axisos.pro/console/)
- **Three Pillars of AxisOS:** `HONEST` • `AUDITABLE` • `OWNED`
