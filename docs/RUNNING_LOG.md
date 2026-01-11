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

## Quick Links (Project Docs)

- Rules / Constraints:
  - DesignRules_HV.md
  - hv-devices.md
- HV_SW_UNIT Core Docs:
  - HV_SW_UNIT_Definition.md
  - HV_SW_UNIT_Floorplan.md
  - HV_SW_UNIT_Layout_Checklist.md
  - HV_SW_UNIT_IV_Expectations.md
  - HV_SW_UNIT_400dpi_Pitch_Analysis.md

(Keep this list minimal. Add links only when they become truly “frequently used.”)

---

## Run Index (Master Table)

Status meaning:
- Planned: not started yet
- Running: currently executing / collecting results
- Done: concluded with documented outcomes
- Parked: intentionally paused (reason required)

| Run ID | Date       | Target     | Description                                               | Status | DRC            | LVS            | Artifacts       | Notes |
|------:|------------|------------|-----------------------------------------------------------|--------|----------------|----------------|-----------------|-------|
| 001   | 2026-01-12 | HV_SW_UNIT | Probe layout to expose dominant HV physical constraints    | Done   | NOT PERFORMED* | NOT PERFORMED  | py / gds / png  | *Official GF180 KLayout DRC not available |
| 002   | 2026-01-12 | HV_SW_UNIT | Guard strategy: per-cell → shared outer                   | Done   | NOT PERFORMED  | NOT PERFORMED  | py / gds / png  | Guard dominance removed |
| 003   | 2026-01-12 | HV_SW_UNIT | Poly gate end treatment isolation                         | Done   | NOT PERFORMED  | NOT PERFORMED  | py / gds / png  | Poly-only single-knob |
| 004   | 2026-01-12 | HV_SW_UNIT | X-direction tiling & pitch measurement (Run003 base)      | Done   | NOT PERFORMED  | NOT PERFORMED  | py / gds / png  | 20 µm: no conflict |

---

## Result Form (Fill for Every Run)

---

## Run 001

### 1) Identification
- **Run ID:** 001
- **Date:** 2026-01-12
- **Designer:** Shinichi Mitsumizo
- **Tool:** KLayout 0.30.x (Windows)
- **PDK / Rule Deck version:** GF180MCU Open PDK  
  (No official KLayout Technology / DRC deck available in this environment)

---

### 2) Layout Conditions
- **Device Type:** HV NMOS (GF180 native HV device)
- **Nominal Max Voltage V (V):** 80 V (exploration target, non-guaranteed)
- **Nominal Current I (A):** Not specified (physical constraints prioritized)
- **Target Pitch (µm):** 20 µm (initial hypothesis, expected to be violated)
- **Array Direction (X / Y):** X
- **Guard Ring Structure:** Yes (continuous P+ guard, per-cell)
- **Power Strategy (rails / isolation / sharing):**
  - Source: Shared across array
  - Drain: Individually routed per cell
  - Bulk: Fixed via P+ guard ring

---

### 3) Verification Status
- **DRC:** NOT PERFORMED  
  - Reason: Official GF180 KLayout DRC deck (`tech.lyt`, `*.drc`) is not distributed
    with `gf180mcu-pdk` and is not available via KLayout package repositories.
  - Substitution: Manual HV constraint probing via aggressive geometry,
    visual inspection, and ruler-based spacing review.
- **LVS:** NOT PERFORMED  
  - Notes: Layout-only exploratory run; no schematic reference.
- **Other checks:**
  - Manual visual sanity check completed (layer intent confirmed)
  - GDS export verified and reproducible

---

### 4) Observations
- **Critical layout constraints discovered (manual, rule-agnostic):**
  - **P+ guard ring outer boundary dominates cell footprint**.
  - **Poly gate over-extension** likely dominates achievable pitch.
  - **Metal1 edge stubs** create early spacing hotspots.
- **Repeatability issues:**
  - Edge protrusions are not tiling-safe without keepout definition.

---

### 5) Decisions
- Keep geometry intentionally aggressive to surface dominant drivers.
- Do not attempt DRC deck reconstruction in this phase.

---

### 6) Conclusion
- **Arrayable (X):** No
- **Next action:** Run 002

---

### 7) Artifacts
- `layout/hv_nmos_gr/klayout/hv_sw_unit_run001_probe.py`
- `layout/hv_nmos_gr/gds/hv_sw_unit_run001_probe.gds`
- `docs/images/07_hv_sw_unit_run001_probe_gds.png`

---

## Run 002

### 1) Identification
- **Run ID:** 002
- **Date:** 2026-01-12

---

### 2) Observations
- Shared outer guard removed guard-dominated pitch inflation.

---

### 3) Conclusion
- **Arrayable (X):** Potentially yes
- **Next action:** Run 003

---

### 4) Artifacts
- `layout/hv_nmos_gr/klayout/hv_sw_unit_run002_guard_shared.py`
- `layout/hv_nmos_gr/gds/hv_sw_unit_run002_guard_shared.gds`
- `docs/images/08_hv_sw_unit_run002_guard_shared_gds.png`

---

## Run 003

### 1) Identification
- **Run ID:** 003
- **Date:** 2026-01-12

---

### 2) Observations
- Poly gate end length reduced.
- No new perimeter protrusions.
- Guard no longer dominates pitch.

---

### 3) Conclusion
- **Arrayable (X):** Not concluded without tiling
- **Next action:** Run 004

---

### 4) Artifacts
- `layout/hv_nmos_gr/klayout/hv_sw_unit_run003_poly_trim.py`
- `layout/hv_nmos_gr/gds/hv_sw_unit_run003_poly_trim.gds`
- `docs/images/09_hv_sw_unit_run003_poly_trim_gds.png`

---

## Run 004

### 1) Identification
- **Run ID:** 004  
- **Date:** 2026-01-12  
- **Designer:** Shinichi Mitsumizo  
- **Tool:** KLayout 0.30.x (Windows)  
- **PDK / Rule Deck version:** GF180MCU Open PDK (manual-rule driven)

---

### 2) Layout Conditions
- **Base cell:** HV_SW_UNIT_RUN003  
- **Device Type:** HV NMOS  
- **Nominal Max Voltage V (V):** 80 V  
- **Nominal Current I (A):** Not specified  
- **Array Direction:** X  
- **Number of tiles:** N = 5  
- **Tested pitch:** **16 µm**  
- **Guard Ring Structure:** Shared outer guard (same as Run 002/003)  
- **Power Strategy:** Same as Run 001–003 (held constant)

---

### 3) Verification Status
- **DRC / LVS:** NOT PERFORMED  
  - Reason: Layout-first exploratory phase; no official GF180 KLayout DRC deck available
- **Other checks:**
  - Visual inspection in KLayout
  - Ruler-based spacing confirmation

---

### 4) Observations
- X-direction tiling at **16 µm pitch is geometrically feasible** (no hard overlaps).
- **Poly ↔ poly spacing retains margin**; poly end trimming does not introduce conflicts.
- **Guard ring geometry does not participate** in pitch limitation.
- The **first structure approaching the limiting condition is Metal1 edge stub**:
  - Lower Metal1 stub shows visibly reduced inter-cell clearance.
  - No short or overlap observed, but spacing margin is minimal.
- No tiling-induced artifacts (placement, mirroring, or orientation errors).

---

### 5) Conclusion
- **Arrayable (X) at 16 µm:** Yes (marginal)
- **Dominant pitch limiter:** **Metal1 stub geometry**
- **Poly gate end:** Confirmed **non-dominant** at this pitch
- **Guard strategy:** Confirmed **non-dominant**
- **Key inference:**
  - Pitch limitation has transitioned from guard → poly → **Metal1**.
- **Recommended next action:**
  - Execute **Run 005: Metal1 stub isolation** (single-knob experiment)
    to determine dominant Metal1 constraint (length / width / vertical offset).

---

### 6) Artifacts
- **Python macro:**  
  `layout/hv_nmos_gr/klayout/hv_sw_unit_run004_x_tiling_eval.py`
- **GDS filename:**  
  `layout/hv_nmos_gr/gds/hv_sw_unit_run004_x_tiling_eval.gds`
- **Screenshot:**
  `docs/images/11_hv_sw_unit_run004_x_tiling_eval_gds.png`
  `docs/images/11_hv_sw_unit_run004_x_tiling_eval_16um_gds.png`

---

### 7) Decision Lock
- Run 004 **closes the poly gate investigation thread**.
- All subsequent pitch optimization must treat **Metal1 stub geometry** as the primary variable.

---

## Revision Notes (Meta-Changes to This Log)

| Rev | Date       | Change                                                        | Rationale |
|----:|------------|---------------------------------------------------------------|-----------|
| 1   | 2026-01-12 | Added operating rules + master table fields                   | Reduce ambiguity |
| 2   | 2026-01-12 | Added V–I fields                                              | Enforce V–I notation |
| 3   | 2026-01-12 | Locked Run 001 results                                        | Enable comparison |
| 4   | 2026-01-12 | Marked Run 002 as Done                                        | Guard factor isolated |
| 5   | 2026-01-12 | Marked Run 003 as Done                                        | Poly factor isolated |
| 6   | 2026-01-12 | Marked Run 004 as Done; 20 µm tiling verified                 | Baseline arrayability |

---

End of document.
