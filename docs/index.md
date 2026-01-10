---
title: "gf180-inkjet-driver"
description: "Documentation for GF180-based inkjet printhead driver IC exploration"
---

# Documentation – gf180-inkjet-driver

This directory contains **layout- and GDS-oriented design notes**
for the **GF180-based inkjet printhead driver IC exploration**.

The documents focus on **architecture definition**, **high-voltage device usage**,
and **layout-driven mixed-signal design**, with the explicit goal of
supporting **manual GDS generation** using the GF180MCU open PDK.

These materials are intended to function as **design rationale and
layout justification**, rather than as a complete IC specification.

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/gf180-inkjet-driver/docs/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/gf180-inkjet-driver/tree/main/docs) |

---

## Document Index (GDS-Oriented)

Each document in this directory is written with a **clear downstream GDS target**
in mind. Conceptual discussion is intentionally limited to what directly
influences layout decisions.

- **architecture.md**  
  System-level partitioning and block definition for
  **manual layout boundaries**, with emphasis on:
  - High-voltage domain separation
  - Logic vs HV interaction points
  - Floorplanning implications for mixed-signal ICs

- **hv-devices.md**  
  High-voltage MOS devices available in GF180MCU and their
  layout-related constraints.
  This document directly supports:
  - **Single-device GDS cell generation**
  - Guard ring and substrate isolation experiments
  - Device-level spacing and topology comparison

- **driver-topology.md**  
  Minimal inkjet driver stage concepts focused on
  **layout feasibility rather than schematic completeness**.
  Intended GDS targets include:
  - One-channel driver layout blocks
  - HV routing patterns toward actuator loads
  - Logic-to-HV signal handoff structures

- **layout-notes.md**  
  Practical layout observations derived from GF180MCU rules and
  mixed-signal constraints, including:
  - Spacing strategies for high-voltage nets
  - Guard ring placement and continuity
  - Substrate noise awareness and mitigation

  This document serves as a **direct reference during manual layout work**.

- **roadmap.md**  
  A stepwise exploration plan describing the transition from
  architectural concepts to **actual GDS artifacts**, including:
  - Device-level GDS milestones
  - Isolation and pad structure studies
  - Incremental expansion toward multi-channel layouts

---

## Design Philosophy

This documentation prioritizes:

- **Layout-first decision making**
- GDS-level understanding over schematic or RTL completeness
- Minimal structures that can be **directly translated into layout**
- Educational clarity grounded in **actual physical constraints**

The intent is not to demonstrate a finished inkjet driver IC,
but to document **how and why specific layout decisions are made**
when designing high-voltage, mixed-signal ICs using an open PDK.

---

## Status

- ✅ Automated digital flow feasibility evaluation completed
- 📐 Manual, layout-centric exploration phase (HV-focused)
- 🧩 GDS targets defined at the **device and structure level**

Individual documents may reference incomplete circuits or
partial topologies; this is intentional and reflects the
layout-driven nature of the exploration.

---

## Disclaimer

This documentation is provided **for educational and exploratory purposes only**.

No guarantees are made regarding manufacturability, electrical performance,
reliability, or suitability for any commercial application.

---

## Layout Design Environment

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/01_gf180_inkjet_env_klayout.png"
  alt="GF180 Inkjet Driver – KLayout Environment"
  width="80%"
/>

---

## Next Step

- Single **HV MOS device layout** generation using KLayout
- Guard ring and isolation structure comparison
- Transition toward **minimum viable inkjet driver cell**

