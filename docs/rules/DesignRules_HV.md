---
title: "Design Rules for HV MOS Layout (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# Design Rules for HV MOS Layout  
## GF180 Inkjet Driver – Minimum & Scalable Rule Set

This document defines **layout design rules for high-voltage MOS (HVMOS / LDMOS)**  
used in the GF180MCU-based inkjet driver project.

The goal is to establish a **clear, minimal, and safe rule set** before starting
layout design, while keeping the structure **scalable for future extensions**
(e.g. 400 dpi printhead drivers).

This rule set prioritizes:
- Safety and robustness
- Readability and structural clarity
- Reusability as a reference layout

Performance optimization is **not** the primary goal in the initial phase.

---

## 1. Power Domain Definition (Fixed)

| Domain | Voltage | Usage |
|------|--------|------|
| VDD_LV | 3.3 V | FSM / digital control |
| VDD_IO | 5–6 V | Pre-stage / level shifter |
| VDD_HV | 10 V | Inkjet actuator drive (HVMOS) |

Rules:
- **10 V is the only HV domain in the initial implementation**
- Higher-voltage operation (>10 V) is treated as a *separate derivative design*

---

## 2. Device Selection Policy (Tox)

### Basic Policy
- **Tox is not specified numerically**
- **Device type selection defines oxide thickness**

### Allowed Devices
- LV devices: 3.3 V MOS
- IO devices: 5 V / 6 V MOS
- HV devices: **10 V LDNMOS / 10 V LDPMOS (LDMOS)**

### Prohibited
- Mixing different voltage-class devices in the same layout region
- Placing HV devices directly inside LV logic regions

---

## 3. L / W Design Rules (Minimum Configuration)

### Design Philosophy
> Do not chase minimum dimensions.  
> Start with long, wide, and stable devices.

### HV LDMOS (10 V)
- **Channel Length (L)**
  - Do **not** use minimum L
  - Long-channel devices are preferred
  - Reduces hot-carrier effects and parasitic sensitivity
- **Channel Width (W)**
  - Define a **unit-width switch cell** (`HV_SW_UNIT`)
  - Drive current is scaled by **parallel replication**
  - Multi-finger layout is assumed

### LV / IO MOS
- Signal integrity and full swing have priority over speed
- Aggressive minimum sizing is discouraged

---

## 4. Layout Region Separation

### Core Rule
- **HV blocks must be isolated as independent islands**

### Implementation
- HV regions must be enclosed by **DNWELL**
- Clear separation from LV / IO regions
- Power and ground routing must be separated by domain

---

## 5. Guard Ring Rules (Critical)

### General Policy
- Guard rings are **mandatory** around HV devices
- Area efficiency is secondary to robustness

### LDNMOS (10 V)
- **P-substrate guard ring**
- **Non-broken (continuous) ring**
- Must fully surround the HV transistor region

### LDPMOS (10 V)
- DNWELL guard ring is required when DNWELL is used
- N-comp taps must be connected to the **highest potential**

### Tap Density
- HV regions require **dense and uniform** well/substrate contacts
- “Too many is better than too few”

---

## 6. Routing & Metal Policy (Simplified)

- HV supply routing must be **wide and short**
- Avoid sharp corners and narrow metal lines
- Maintain sufficient spacing between HV power and signal nets

---

## 7. Minimum Functional Block (1-Nozzle Equivalent)

The initial PoC implementation includes only:

1. **HV Switch**
   - 10 V LDMOS
   - Unit-cell-based structure
2. **Level Shifter**
   - 3.3 V → 6 V → 10 V
   - Slow is acceptable, correctness is mandatory
3. **Input Control**
   - Single external control signal
4. **Layout Template**
   - Includes power routing and guard rings

---

## 8. Future Scalability (Toward 400 dpi)

- Higher density is achieved by **replicating unit cells**
- Design rules remain unchanged
- Optimization is handled at routing and pitch levels

---

## 9. Pre-Layout Checklist

- [ ] Power domains are clearly separated (LV / IO / HV)
- [ ] Only 10 V LDMOS is used for HV
- [ ] HV region is isolated with DNWELL
- [ ] Guard rings fully surround HV devices
- [ ] Tap density is sufficient
- [ ] L/W follows the unit-cell scaling concept

---

## 10. Notes

- This rule set is intended for **education, structure exploration, and PoC**
- Not qualified for production or mass manufacturing
- Rules must be reviewed when the PDK is updated

---

**End of Document**
