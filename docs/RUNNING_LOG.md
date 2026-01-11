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
  - **P+ guard ring outer boundary dominates cell footprint**, even for a minimal
    single-device probe.
  - **Poly gate over-extension** immediately interacts with perimeter structures
    and is likely to dominate achievable pitch in dense arrays.
  - **Metal1 edge stubs** create early spacing hotspots at cell boundaries,
    making naive tiling unsafe.
- **Unexpected interactions:**
  - Tight guard margin combined with aggressive poly extension causes
    perimeter congestion before any real routing strategy is introduced.
- **Area-dominating structures:**
  - Continuous P+ guard ring is the single largest mandatory structure.
- **Repeatability / tiling issues:**
  - Edge protrusions (metal stubs) are not tiling-safe without explicit
    inter-cell keepout definitions.

---

### 5) Decisions
- **Accepted compromises:**
  - Keep Run 001 geometry intentionally “bad” to surface dominant physical drivers.
- **Rejected options:**
  - Attempting to port or reconstruct a non-existent GF180 KLayout DRC deck
    for this exploratory phase.
- **Rationale:**
  - The purpose of Run 001 is constraint discovery, not rule closure.

---

### 6) Conclusion
- **Structurally acceptable as HV_SW_UNIT:** Not concluded (no formal DRC)
- **Arrayable (X):** No
- **Arrayable (Y):** Not evaluated
- **Recommended next action:**
  - Start **Run 002** with a single controlled change focused on guard strategy.

---

### 7) Artifacts
- **Python macro:** `layout/hv_nmos_gr/klayout/hv_sw_unit_run001_probe.py`
- **GDS filename:** `layout/hv_nmos_gr/gds/hv_sw_unit_run001_probe.gds`
- **Screenshot:** `docs/images/07_hv_sw_unit_run001_probe_gds.png`

---

## Run 002

### 1) Identification
- **Run ID:** 002
- **Date:** 2026-01-12
- **Designer:** Shinichi Mitsumizo
- **Tool:** KLayout 0.30.x (Windows)
- **PDK / Rule Deck version:** GF180MCU Open PDK (manual-rule driven)

---

### 2) Layout Conditions
- **Device Type:** HV NMOS (same as Run 001)
- **Nominal Max Voltage V (V):** 80 V
- **Nominal Current I (A):** Not specified
- **Target Pitch (µm):** TBD (measured by tiling experiment)
- **Array Direction (X / Y):** X
- **Guard Ring Structure:** Shared outer guard (array-level)
- **Power Strategy:** Same as Run 001

---

### 3) Verification Status
- **DRC / LVS:** NOT PERFORMED (by intent)

---

### 4) Observations
- Removal of per-cell guard ring **eliminated guard-dominated pitch inflation**.
- Cell boundary in X is no longer dictated by P+ guard geometry.

---

### 5) Conclusion
- **Arrayable (X):** Potentially yes (subject to poly / metal constraints)
- **Next dominant candidates:** Poly gate end, Metal1 edge stubs
- **Next action:** Run 003

---

### 6) Artifacts
- **Python macro:** `layout/hv_nmos_gr/klayout/hv_sw_unit_run002_guard_shared.py`
- **GDS filename:** `layout/hv_nmos_gr/gds/hv_sw_unit_run002_guard_shared.gds`
- **Screenshot:** `docs/images/08_hv_sw_unit_run002_guard_shared_gds.png`

---

## Run 003

### 1) Identification
- **Run ID:** 003
- **Date:** 2026-01-12
- **Designer:** Shinichi Mitsumizo
- **Tool:** KLayout 0.30.x (Windows)
- **PDK / Rule Deck version:** GF180MCU Open PDK (manual-rule driven)

---

### 2) Layout Conditions
- **Device Type:** HV NMOS (same primitive as Run 001/002)
- **Nominal Max Voltage V (V):** 80 V
- **Nominal Current I (A):** Not specified
- **Target Pitch (µm):** TBD (pending tiling)
- **Array Direction (X / Y):** X
- **Guard Ring Structure:** Shared outer guard (same as Run 002)
- **Power Strategy:** Same as Run 001/002

---

### 3) Change Introduced (Single Knob)
- **Poly gate end trimming**
  - Poly over-extension at cell boundary reduced
  - No change to guard, active diffusion, or Metal1 topology

---

### 4) Verification Status
- **DRC / LVS:** NOT PERFORMED (layout-first exploratory phase)
- **Other:** Visual inspection in KLayout; layer intent confirmed

---

### 5) Observations
- Poly gate end length is **visibly reduced** compared to Run 002.
- No new perimeter protrusions introduced.
- Guard no longer dominates cell boundary.
- **Dominant pitch limiter not conclusively removed without tiling.**

---

### 6) Conclusion
- **Arrayable (X):** Not concluded (requires X-tiling experiment)
- **Preliminary inference:**
  - If pitch improves → poly end was dominant limiter.
  - If unchanged → Metal1 edge stub / contact enclosure likely dominant.
- **Recommended next action:**
  - Perform X-direction tiling and pitch measurement (**Run 004 candidate**).

---

### 7) Artifacts
- **Python macro:** `layout/hv_nmos_gr/klayout/hv_sw_unit_run003_poly_trim.py`
- **GDS filename:** `layout/hv_nmos_gr/gds/hv_sw_unit_run003_poly_trim.gds`
- **Screenshot:** `docs/images/09_hv_sw_unit_run003_poly_trim_gds.png`

---

## Revision Notes (Meta-Changes to This Log)

| Rev | Date       | Change                                                        | Rationale |
|----:|------------|---------------------------------------------------------------|-----------|
| 1   | 2026-01-12 | Added operating rules + master table fields                   | Reduce ambiguity |
| 2   | 2026-01-12 | Added V–I fields                                              | Enforce V–I notation |
| 3   | 2026-01-12 | Locked Run 001 results                                        | Enable comparison |
| 4   | 2026-01-12 | Marked Run 002 as Done                                        | Guard factor isolated |
| 5   | 2026-01-12 | Marked Run 003 as Done; documented poly-trim results          | Single-knob isolation |

---

End of document.
