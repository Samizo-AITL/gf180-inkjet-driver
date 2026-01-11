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
- Confirm **DRC-safe structure** under GF180 rules
- Identify **layout-driven constraints** invisible at schematic level
- Accumulate reusable layout patterns and check items for future iterations

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

| Run ID | Date | Target | Description | Status | DRC | LVS | Artifacts | Notes |
|------:|------|--------|-------------|--------|-----|-----|----------|------|
| 001 |  | HV_SW_UNIT | Initial layout trial | Running |  |  |  | Layout started |

---

## Result Form (Fill for Every Run)

### 1) Identification
- **Run ID:** 001
- **Date:** 2026-01-12
- **Designer:** Shinichi Mitsumizo
- **Tool:** KLayout 0.29.x (Windows)
- **PDK / Rule Deck version:** GF180MCU Open PDK (HV ruleset, exact revision unknown)

### 2) Layout Conditions
- **Device Type:** HV NMOS (GF180 native HV device)
- **Nominal Max Voltage V (V):** 80 V (exploration target, non-guaranteed)
- **Nominal Current I (A):** Not specified (physical constraints prioritized)
- **Target Pitch (µm):** 20 µm (initial hypothesis, expected to be violated)
- **Array Direction (X / Y):** X
- **Guard Ring Structure:** Yes (continuous P+ guard, shared)
- **Power Strategy (rails / isolation / sharing):**
  - Source: Shared across array
  - Drain: Individually routed per cell
  - Bulk: Fixed via guard ring

### 3) Verification Status
- DRC: PASS / FAIL / NOT CHECKED
  - Main violations (if FAIL):
- LVS: PASS / FAIL / NOT PERFORMED
  - Notes:
- Other checks (ERC / manual sanity / clearance review):

### 4) Observations
- Critical layout constraints discovered:
- Unexpected rule interactions:
- Area-dominating structures:
- Repeatability / tiling issues:

### 5) Decisions
- Accepted compromises:
- Rejected options:
- Rationale (why this was chosen):

### 6) Conclusion
- Structurally acceptable as HV_SW_UNIT: Yes / No
- Arrayable without modification: Yes / No
- Recommended next action:
  - Revise within same Run (minor) / Start next Run (major)
  - What to test next (DRC focus / pitch focus / guard focus etc.)

### 7) Artifacts
- GDS filename:
- Screenshots (paths):
- Notes for reproducibility (commands / settings / key parameters):

---

## Revision Notes (Meta-Changes to This Log)

Record changes to this RUNNING_LOG.md itself (so the log format evolution is traceable).

| Rev | Date | Change | Rationale |
|----:|------|--------|-----------|
| 1 |  | Added operating rules + master table fields (DRC/LVS/Artifacts) | Reduce ambiguity and make progress queryable |
| 2 |  | Added V–I fields (V and I) into layout conditions | Enforce consistent V–I discussion |
| 3 |  | Updated Run 001 status to Running | Mark production-phase execution start |

---

End of document.
