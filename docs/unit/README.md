# HV_SW_UNIT – Unit-Level Design Materials

This directory contains **reusable, unit-level design knowledge**
for the HV_SW_UNIT used in GF180-based inkjet driver exploration.

The documents here describe **what the unit is**, **how it is physically built**,
and **what constraints apply**, without freezing architectural decisions.

---

## What This Directory Is

- Unit-level physical and layout knowledge
- Reusable design patterns and checklists
- Observations that remain valid across array configurations

These files may reference exploration results,
but they do **not** define final architectures.

---

## What This Directory Is NOT

- A running log
- An architecture freeze
- A design specification
- A complete circuit definition

Final, frozen decisions are documented in `docs/architecture/`.

---

## Contents Overview

- **HV_SW_UNIT_Definition.md**  
  Defines the purpose and boundary of the HV_SW_UNIT.

- **HV_SW_UNIT_Floorplan.md**  
  Describes physical block placement and well strategy.

- **HV_SW_UNIT_LW_Proposal.md**  
  Conservative layout dimensions derived from exploration.

- **HV_SW_UNIT_IV_Expectations.md**  
  Sanity-level V–I expectations for the unit.

- **HV_SW_UNIT_Layout_Checklist.md**  
  Practical checklist for manual GDS implementation.

- **hv-devices.md**  
  Overview of applicable HV devices in GF180MCU.

---

## Relationship to Other Documentation

- Frozen decisions → `docs/architecture/`
- Execution history → `docs/logs/`
- Process constraints → `docs/rules/`

This separation is intentional.

---

**End of unit/README.md**
