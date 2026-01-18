---
title: "gf180-inkjet-driver"
description: "layout- and GDS-oriented design notes"
---

# RUNNING LOG (Production Phase)

This document is the **single source of truth** for production-phase execution in this repository.  
It records **what was done, what was observed, and what was decided** in a layout-first HV IC exploration.

- This is **NOT** a design specification.
- This is a **decision + result ledger** to make progress reproducible.

---

## How to Use This Log (Operating Rules)

1. Every significant action must be logged as a **Run** (Run ID increments).
2. A Run is valid even if it fails (e.g., DRC FAIL). Failure is still a result.
3. Do not overwrite history. When plans change, create a **new Run** or add a **Revision Note**.
4. Use **V–I notation** consistently for electrical discussion (Voltage–Current).

---

## Scope and Intent

- Target object: **HV_SW_UNIT**
- Process: **GF180MCU Open PDK**
- Focus: **Layout-first, GDS-oriented**
- Priority: **Physical robustness / arrayability > performance optimization**

### Explicitly Out of Scope
- Circuit-level performance optimization
- Tape-out readiness
- Reliability qualification
- Commercial usability / warranty

---

## Global Objectives

- Establish a **physically valid HV_SW_UNIT layout**
- Identify **layout-driven constraints** invisible at schematic level
- Accumulate reusable layout patterns and check items for future iterations

> Note: Formal DRC closure under GF180 is **not a requirement** in this phase due to the  
> absence of an official KLayout DRC deck in the current environment.

---

## Run Index (Master Table)

| Run ID | Date       | Target     | Description                                   | Status | DRC           | LVS           | Artifacts       | Notes |
|------:|------------|------------|-----------------------------------------------|--------|---------------|---------------|-----------------|-------|
| 001   | 2026-01-12 | HV_SW_UNIT | Probe layout to expose dominant constraints    | Done   | NOT PERFORMED | NOT PERFORMED | py / gds / png  | Guard dominance |
| 002   | 2026-01-12 | HV_SW_UNIT | Guard strategy: per-cell → shared              | Done   | NOT PERFORMED | NOT PERFORMED | py / gds / png  | Guard removed   |
| 003   | 2026-01-12 | HV_SW_UNIT | Poly gate end isolation                        | Done   | NOT PERFORMED | NOT PERFORMED | py / gds / png  | Poly isolated   |
| 004   | 2026-01-12 | HV_SW_UNIT | X-tiling & pitch evaluation (Run003 base)     | Done   | NOT PERFORMED | NOT PERFORMED | py / gds / png  | M1 emerges      |
| 005   | 2026-01-12 | HV_SW_UNIT | Metal1 stub trimming & pitch sweep             | Done   | NOT PERFORMED | NOT PERFORMED | py / gds / png  | Limiter fixed   |

---

## Run 001

### Identification
- **Run ID:** 001  
- **Date:** 2026-01-12  
- **Tool:** KLayout 0.30.x (Windows)

### Key Result
- P+ guard ring **dominates cell footprint**
- Naive tiling is impossible

### Conclusion
- **Arrayable (X):** No  
- **Next:** Guard strategy isolation (Run 002)

---

## Run 002

### Key Result
- Shared outer guard **removes guard-dominated pitch inflation**

### Conclusion
- **Arrayable (X):** Potentially yes  
- **Next:** Poly gate end isolation (Run 003)

---

## Run 003

### Key Result
- Poly gate over-extension trimmed
- No new boundary artifacts introduced

### Conclusion
- Poly is **not conclusively dominant**
- **Next:** Tiling-based pitch measurement (Run 004)

---

## Run 004

### Layout Conditions
- Base cell: **HV_SW_UNIT_RUN003**
- Tiling direction: X
- Tiles: N = 5
- Tested pitch: **16 µm**

### Observations
- 16 µm pitch is **geometrically feasible**
- Guard and poly no longer limit pitch
- **Metal1 edge stub approaches spacing limit**

### Conclusion
- **Arrayable (X) at 16 µm:** Yes (marginal)
- **Dominant pitch limiter:** **Metal1 stub**
- **Next:** Metal1-only single-knob experiment (Run 005)

---

## Run 005

### 1) Identification
- **Run ID:** 005  
- **Date:** 2026-01-12  
- **Tool:** KLayout 0.30.x (Windows)

---

### 2) Layout Conditions
- **Base cell:** HV_SW_UNIT_RUN003 (unchanged)
- **Single knob:** Metal1 stub geometry only
- **Array direction:** X
- **Tiles:** N = 5
- **Pitch sweep:** 16 µm → 14 µm → 12 µm
- **Guard / Poly:** Frozen (from Run 003)

---

### 3) Verification Status
- **DRC / LVS:** NOT PERFORMED  
- **Method:** Visual inspection + ruler-based spacing confirmation

---

### 4) Observations

#### 16 µm
- Fully clean margin
- No M1 proximity concern

#### 14 µm
- M1 stub spacing reduced but **still acceptable**
- No overlap or edge-touch

#### 12 µm
- Geometry remains **non-overlapping**
- M1 stub becomes **clear dominant limiter**
- Spacing margin approaches practical minimum

---

### 5) Conclusions

- **Minimum safe pitch (manual):** **≈12–14 µm**
- **Final dominant constraint:** **Metal1 stub geometry**
- Guard ring and poly gate end are **fully de-risked**
- Pitch scaling below 12 µm would require:
  - M1 topology redesign, or
  - Vertical routing layer migration (e.g., M2)

---

### 6) Artifacts

**Macros**
- `layout/hv_nmos_gr/klayout/hv_sw_unit_run005_m1_stub_trim.py`
- `layout/hv_nmos_gr/klayout/hv_sw_unit_run005_m1_stub_trim_sweep.py`

**GDS**
- `layout/hv_nmos_gr/gds/hv_sw_unit_run005_m1_stub_trim_16um.gds`
- `layout/hv_nmos_gr/gds/hv_sw_unit_run005_m1_stub_trim_14um.gds`
- `layout/hv_nmos_gr/gds/hv_sw_unit_run005_m1_stub_trim_12um.gds`

**Images**
- `docs/images/12_hv_sw_unit_run005_m1_stub_trim_16um_gds.png`
- `docs/images/13_hv_sw_unit_run005_m1_stub_trim_14um_gds.png`
- `docs/images/14_hv_sw_unit_run005_m1_stub_trim_12um_gds.png`

---

## Final Decision Summary

- **Pitch limiter progression:**  
  Guard → Poly → **Metal1**
- **HV_SW_UNIT is physically arrayable**
- **Layout-first objective achieved**

> This concludes the **HV_SW_UNIT pitch discovery phase**.  
> Any further run would be **architectural**, not exploratory.

---

## Revision Notes

| Rev | Date       | Change                                      |
|----:|------------|---------------------------------------------|
| 1   | 2026-01-12 | Initial structure                           |
| 2   | 2026-01-12 | Locked Run 001–003                          |
| 3   | 2026-01-12 | Added Run 004 (tiling evaluation)           |
| 4   | 2026-01-12 | Added Run 005 (Metal1 stub sweep)           |
| 5   | 2026-01-12 | Declared pitch discovery phase complete     |

---

End of document.
