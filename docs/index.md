---
title: "gf180-inkjet-driver"
description: "layout and GDS-oriented design notes"
---

# Documentation – gf180-inkjet-driver

This directory contains **layout- and GDS-oriented design notes**
for the **GF180-based inkjet printhead driver IC exploration**.

The documents focus on **architecture definition**, **high-voltage device usage**,
and **layout-driven mixed-signal design**, with the explicit goal of
supporting **manual GDS generation** using the GF180MCU open PDK.

These materials function as **design rationale and layout justification**.
In addition to documenting viable structures, they explicitly record
**architectural limits identified through GDS-level exploration**,
rather than serving as a complete IC specification.

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/gf180-inkjet-driver/docs/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/gf180-inkjet-driver/tree/main/docs) |

---

## 🗺 Layout Map (GDS-Oriented Overview)

> 📌 **Mermaid rendering note**  
> This diagram is written in Mermaid syntax and is rendered correctly on GitHub.  
> GitHub Pages does not render Mermaid diagrams by default.
>
> 👉 Please view the rendered diagram on GitHub:  
[View on GitHub (docs/index.md)](https://github.com/Samizo-AITL/gf180-inkjet-driver/blob/main/docs/index.md)

```mermaid
flowchart LR
  A[docs/ : GDS-oriented design notes] --> B[Core Architecture Docs]
  A --> C[HV Layout Rule Chain]
  A --> D[Status / Outcome]

  B --> B1[architecture.md\nSystem partitioning / floorplanning]
  B --> B2[hv-devices.md\nHV MOS options & layout constraints]
  B --> B3[driver-topology.md\nLayout-feasible driver blocks]
  B --> B4[layout-notes.md\nGuard ring / spacing / substrate]
  B --> B5[roadmap.md\nPath toward actual GDS]

  C --> C1[DesignRules_HV.md\nHV domain & isolation rules]
  C --> C2[HV_SW_UNIT_Definition.md\nMinimum scalable HV cell]
  C --> C3[HV_SW_UNIT_Floorplan.md\nDNWELL & GR continuity]
  C --> C4[HV_SW_UNIT_LW_Proposal.md\nConservative L/W sizing]
  C --> C5[HV_SW_UNIT_Layout_Checklist.md\nActual layout order]
  C --> C6[HV_SW_UNIT_IV_Expectations.md\nV–I sanity checks]
  C --> C7[HV_SW_UNIT_400dpi_Pitch_Analysis.md\n~63.5 µm pitch limit]

  D --> D1[Digital flow feasibility: completed]
  D --> D2[Manual HV layout exploration: completed]
  D --> D3[400 dpi array feasibility: evaluated and concluded]
```

---

## Representative GDS Artifact

The following image shows a **representative HV switch unit GDS**
generated during this exploration.

It demonstrates:
- DNWELL enclosure
- Continuous P+ guard ring
- Central HV device structure
- Explicit D / G / S / B pin exposure

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/02_hv_sw_unit_gds.png"
  alt="HV_SW_UNIT – DNWELL and Guard Ring GDS"
  width="80%"
/>

This GDS serves as a **visual anchor**
for the unit- and array-level documents listed below.

---

## Array Layout Evolution (400 dpi Study)

The following snapshots document the **stepwise evolution**
of the HV_SW_UNIT array toward **400 dpi pitch (63.5 µm)**.
Each image corresponds to a concrete layout decision
and captures the moment where a design assumption
was either validated or rejected.

### Independent Unit Isolation (Baseline)

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/03_hv_unit_array_full_gds.png"
  alt="HV_SW_UNIT Array – Independent DNWELL and Guard Ring"
  width="80%"
/>

- DNWELL and guard ring are isolated per HV_SW_UNIT
- Guard ring outer boundary dominates pitch
- **400 dpi is clearly infeasible**

---

### Column-wise Guard Ring Sharing

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/04_hv_sw_unit_array_gr_shared_FIXED_gds.png"
  alt="HV_SW_UNIT Array – Column-wise Guard Ring Sharing"
  width="80%"
/>

- Guard ring redundancy reduced at array level
- Pitch pressure partially relieved
- Unit-level guard ring remnants still interfere

---

### Guard-Ring-Clean Shared Array (Final Check)

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/05_hv_sw_unit_array_gr_shared_clean_gds.png"
  alt="HV_SW_UNIT Array – Guard Ring Clean Shared Configuration"
  width="80%"
/>

- Unit-level guard rings completely removed
- Guard ring no longer the dominant limiter
- **DNWELL enclosure and spacing become decisive**

---

## Document Index (GDS-Oriented)

Each document in this directory is written with a **clear downstream GDS target**
in mind. Conceptual discussion is intentionally limited to what directly
influences layout decisions.

### Core Architecture Documents

- **architecture.md**  
  System-level partitioning and block definition for
  **manual layout boundaries**, with emphasis on:
  - High-voltage domain separation
  - Logic vs HV interaction points
  - Floorplanning implications for mixed-signal ICs

- **hv-devices.md**  
  High-voltage MOS devices available in GF180MCU and their
  layout-related constraints.

- **driver-topology.md**  
  Minimal inkjet driver stage concepts focused on
  **layout feasibility rather than schematic completeness**.

- **layout-notes.md**  
  Practical layout observations derived from GF180MCU rules and
  mixed-signal constraints.

- **roadmap.md**  
  A stepwise exploration plan documenting the transition from
  architectural concepts to **actual GDS artifacts**.

---

## High-Voltage Layout Rule Set (Inkjet-Focused)

- **DesignRules_HV.md**
- **HV_SW_UNIT_Definition.md**
- **HV_SW_UNIT_Floorplan.md**
- **HV_SW_UNIT_LW_Proposal.md**
- **HV_SW_UNIT_Layout_Checklist.md**
- **HV_SW_UNIT_IV_Expectations.md**
- **HV_SW_UNIT_400dpi_Pitch_Analysis.md**

Together, these documents capture both
**feasible layout structures**
and **architectural limits identified at the GDS level**.

---

## Design Philosophy

This documentation prioritizes:

- **Layout-first decision making**
- GDS-level understanding over schematic or RTL completeness
- Minimal structures that can be **directly translated into layout**
- Explicit recording of **why certain approaches fail**

The intent is not to demonstrate a finished inkjet driver IC,
but to preserve **design reasoning grounded in physical layout reality**.

---

## Status

- ✅ Automated digital flow feasibility evaluation completed
- ✅ Manual HV device and unit layout completed
- ✅ HV_SW_UNIT array and guard ring sharing studies completed
- ❌ 400 dpi (63.5 µm) array feasibility: **structurally infeasible under GF180 DNWELL assumptions**

---

## ✅ 300 dpi Array Implementation (Final Outcome)

Based on the GDS-level exploration documented above, a **300 dpi pitch
(~85.0 µm)** configuration was selected as the **minimum viable and
structurally consistent solution** under GF180MCU HV and DNWELL rules.

### Implemented Artifact

- **Generator**
  - `layout/hv_nmos_gr/klayout/hv_sw_unit_array_gr_shared_300dpi.py`
- **Generated GDS**
  - `layout/hv_nmos_gr/gds/hv_sw_unit_array_gr_shared_300dpi.gds`
- **Pitch**
  - 85.0 µm (300 dpi, margin included)
- **Guard Ring Strategy**
  - Column-wise shared P+ guard ring
  - Unit-level guard rings removed
- **Status**
  - ✅ GDS successfully generated and verified in KLayout

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/06_hv_sw_unit_array_gr_shared_300dpi.png"
  alt="HV_SW_UNIT Array – 300 dpi Guard-Ring-Shared Implementation"
  width="80%"
/>

### Conclusion

While 400 dpi (63.5 µm) configurations fail due to unavoidable
DNWELL enclosure and spacing constraints, the **300 dpi array
represents a physically realizable layout point** for GF180-based
inkjet driver exploration.

This configuration is treated as the **baseline (golden) array**
for any subsequent device sizing, electrical evaluation,
or architectural extension.

---

## Disclaimer

This documentation is provided **for educational and exploratory purposes only**.

No guarantees are made regarding manufacturability, electrical performance,
reliability, or suitability for any commercial application.
