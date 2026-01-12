---
title: "HV_SW_UNIT Definition (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT Definition  
## Unit High-Voltage Switch Cell for Inkjet Driver

This document defines the **HV_SW_UNIT**, the minimum scalable
high-voltage switch cell used in the GF180-based inkjet driver project.

The HV_SW_UNIT is designed to be:
- Easy to understand
- Layout-safe for HV operation
- Linearly scalable toward higher density (e.g. 400 dpi)

---

## 1. Purpose of HV_SW_UNIT

The HV_SW_UNIT represents:
- The **minimum controllable HV current source**
- A **replicable layout primitive**
- A **reference structure** for all future HV driver expansion

All higher-current or higher-density drivers must be constructed by
**replicating this unit cell**, not by resizing it arbitrarily.

---

## 2. Target Device Type

| Item | Selection |
|----|----------|
| Process | GF180MCU Open PDK |
| Device | 10 V LDNMOS (LDMOS) |
| Role | Inkjet actuator switch |
| Mode | Low-side switch (initial PoC) |

Notes:
- High-side configurations are out of scope for the first iteration
- PMOS-based HV switches are treated as a separate variant

---

## 3. Electrical Design Philosophy

> The first HV_SW_UNIT must be **boringly safe**.

Design priorities:
1. Reliability
2. Predictable behavior
3. Layout readability
4. Scalability

Performance optimization is intentionally postponed.

---

## 4. Channel Length (L) Policy

### Rule
- **Do NOT use minimum channel length**
- Use a **long-channel configuration**

### Rationale
- Reduces hot-carrier degradation
- Improves matching between replicated units
- Makes parasitic effects easier to reason about

### Guideline
- L shall be **significantly larger than minimum**
- Once selected, **L is fixed for all HV_SW_UNIT instances**

---

## 5. Channel Width (W) Policy

### Rule
- W defines the **unit current**
- Current scaling is achieved by **parallel replication**

### Implementation
- HV_SW_UNIT has a **fixed W**
- Larger drive strength = N × HV_SW_UNIT

### Layout Assumption
- Multi-finger structure
- Symmetric source/drain routing
- Shared diffusion where possible

---

## 6. Finger Configuration

| Item | Policy |
|---|---|
| Finger count | ≥ 2 |
| Symmetry | Mandatory |
| Gate routing | Centralized |
| Source routing | Short, wide, local |
| Drain routing | Directed toward HV load |

Notes:
- Single-finger layouts are discouraged
- Finger count may be adjusted *only* if symmetry is preserved

---

## 7. Guard Ring Integration

HV_SW_UNIT **always includes guard rings** as part of the cell.

### Rules
- P-substrate guard ring is mandatory
- Guard ring is **continuous (non-broken)**
- Guard ring dimensions scale with the unit cell

This guarantees that:
- Replicating HV_SW_UNIT automatically preserves HV safety
- No “naked HV transistor” can exist by construction

---

## 8. Power and Signal Interface

### Ports (Conceptual)

| Port | Description |
|----|------------|
| D | HV output to actuator |
| S | Ground / return |
| G | Gate control (from level shifter) |
| BULK | Substrate / well reference |

Rules:
- Gate routing must avoid parallel run with HV drain metal
- HV drain metal must be isolated and wide

---

## 9. Physical Size Philosophy

- Area efficiency is **not** a goal in v0.x
- White space is acceptable and encouraged
- The cell outline must be **rectangular and tilable**

---

## 10. Replication Strategy (Toward 400 dpi)

- 1 nozzle = N × HV_SW_UNIT
- N is chosen based on required energy / current
- Spacing rules are preserved during tiling
- Guard rings merge naturally between adjacent units

---

## 11. Checklist (Before First Layout)

- [ ] Device is 10 V LDNMOS
- [ ] Channel length is non-minimum
- [ ] Width is fixed and unitized
- [ ] Multi-finger structure is used
- [ ] Guard ring is included in the cell
- [ ] Cell is rectangular and tilable

---

## 12. Next Steps

After this definition:
1. Fix tentative **L/W numeric candidates**
2. Draw **HV_SW_UNIT floorplan**
3. Integrate DNWELL boundary
4. Run basic DC / transient simulations

---

**End of Document**
