---
title: "GF180 HV NMOS Layout Study"
description: "Single high-voltage NMOS layout study with guard ring using GF180MCU Open PDK"
---

# GF180 HV NMOS Layout Study (with Guard Ring)

This directory contains a **single high-voltage NMOS layout study**
implemented using the **GF180MCU open PDK**.

The purpose of this layout is **not functional verification**,
but **GDS-level understanding** of high-voltage device structures,
guard rings, and isolation strategies required for
inkjet printhead driver ICs.

> **Positioning Note**  
> This layout represents an early, manually created HV NMOS GDS reference.
> It serves as a *baseline structural study* and **was intentionally created
> prior to generator-based HV unit layouts (HV_SW_UNIT)** that were later used for
> array construction and pitch-constrained feasibility exploration.

---

## Objective

The objectives of this layout study are:

- To confirm how **high-voltage NMOS devices** are physically realized in GF180MCU
- To study **guard ring placement and continuity**
- To understand **spacing and enclosure constraints** at the GDS level
- To establish a **reusable device-level GDS reference**
  for future mixed-signal / inkjet driver layouts

This layout serves as the **first concrete GDS artifact**
in the gf180-inkjet-driver exploration and acts as a
**reference point for later generator-based HV unit layouts**.

---

## Layout Overview

- **Device type**: High-voltage NMOS (single device)
- **Topology**: Standalone transistor (no functional circuit)
- **Guard ring**: P+ guard ring surrounding the device
- **Routing**:
  - Minimal Metal1 routing
  - Gate, drain, and source brought out for visibility
- **Substrate**: P-substrate with explicit isolation awareness

No attempt is made to optimize performance, area, or matching.

---

## GDS Artifact

- **File**: `gf180_hv_nmos_gr.gds`
- **Cell name**: `gf180_hv_nmos_gr`
- **Generation method**:
  - Manual layout using GF180MCU layers
  - No automated digital flow
  - No OpenLane involvement

### Verification Status

- DRC: *Not enforced*
- LVS: *Not applicable*
- Electrical simulation: *Not performed*

The GDS is intended for **structural inspection and educational use only**.

---

## Relation to Documentation

This layout directly corresponds to the following documents:

- `docs/hv-devices.md`  
  → Device selection rationale and HV constraints

- `docs/layout-notes.md`  
  → Guard ring strategy and spacing considerations

The documents explain **why this structure exists**;
this directory shows **what it looks like in GDS**.

---

## Design Notes

Key observations captured by this layout:

- High-voltage devices impose **significant spacing overhead**
- Guard ring geometry strongly influences layout density
- Even a single HV transistor dominates local floorplanning

These characteristics explain why
**inkjet driver ICs require layout-first design decisions**.

---

## Scope and Limitations

This layout intentionally excludes:

- Functional driver circuitry
- Level shifters or logic interfaces
- Pad structures or ESD networks
- Generator-based or array-oriented layouts  
  (handled separately in **HV_SW_UNIT**)
- **Array-level feasibility or pitch-constrained studies**  
  (explicitly handled in **HV_SW_UNIT** and related array exploration documents)
- Any claim of manufacturability

Its sole role is to function as a **minimal, inspectable GDS unit**.

---

## Disclaimer

This GDS and accompanying notes are provided
**for educational and exploratory purposes only**.

No guarantees are made regarding electrical behavior,
reliability, or suitability for fabrication or commercial use.
