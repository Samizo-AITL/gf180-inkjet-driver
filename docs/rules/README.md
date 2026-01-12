# Rules and Constraints

This directory collects **process- and layout-level constraints**
that bound the design space of the GF180-based HV_SW_UNIT
and its array implementations.

The documents here define **what cannot be changed or exceeded**
without moving to a different process, device set, or architecture.

---

## What This Directory Is

- External constraints imposed by the process or physics
- Layout rules that dominate feasibility
- Analyses that demonstrate **infeasible regions** of the design space

These rules apply across multiple units and architectures.

---

## What This Directory Is NOT

- A running log
- A frozen architecture definition
- A unit-level design description
- An optimization guideline

Final architectural decisions are documented in `docs/architecture/`.

---

## Contents Overview

- **DesignRules_HV.md**  
  High-voltage related layout and isolation rules
  derived from the GF180MCU Open PDK.

- **HV_SW_UNIT_400dpi_Pitch_Analysis.md**  
  Analysis demonstrating why 400 dpi array pitch
  is structurally infeasible under GF180 DNWELL assumptions.

---

## Relationship to Other Documentation

- Architecture freezes → `docs/architecture/`
- Execution history → `docs/logs/`
- Unit-level design knowledge → `docs/unit/`

This separation prevents accidental re-exploration
of already-established constraints.

---

**End of rules/README.md**
