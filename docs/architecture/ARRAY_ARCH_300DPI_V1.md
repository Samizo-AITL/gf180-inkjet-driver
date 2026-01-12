---
title: "ARRAY_ARCH_300DPI_V1"
description: "HV_SW_UNIT Array – Physical Architecture Definition (300 dpi)"
---

# ARRAY_ARCH_300DPI_V1  
**HV_SW_UNIT Array – Physical Architecture Definition (300 dpi)**

This document defines the **fixed physical array architecture** for  
HV_SW_UNIT at **300 dpi resolution**.

It is derived from **HV_SW_UNIT_ARCH_V1** and represents  
**post-feasibility, post-exploration architectural decisions**.

- This is **NOT** a running log.
- This is **NOT** an experiment record.
- This document **freezes array-level structural choices**.

Once written, this file **must not be modified retroactively**.  
Any architectural change requires a **new ARRAY_ARCH revision**.

---

## 1. Purpose

- Elevate HV_SW_UNIT from a unit cell to a **physically defined array structure**
- Freeze **array-level physical constraints** invisible at the unit level
- Ensure all subsequent work is **design execution**, not constraint discovery

---

## 2. Reference Documents

- `ARCHITECTURE.md`  
  - **HV_SW_UNIT_ARCH_V1**
- `RUNNING_LOG.md`  
  - Runs 001–005 (Pitch discovery phase)
- Process: **GF180MCU Open PDK**
- Tooling: **KLayout 0.30.x**

---

## 3. Array Architecture ID

- **Architecture Name:** `HV_SW_UNIT_ARRAY_300DPI_ARCH_V1`
- **Status:** ACTIVE
- **Date Frozen:** 2026-01-12
- **Derived From:**
  - HV_SW_UNIT_ARCH_V1
  - 300 dpi array feasibility conclusion

---

## 4. Fixed Array Parameters

### 4.1 Resolution and Pitch

- **Target resolution:** 300 dpi
- **Physical pitch:** **85.0 µm**
- Pitch includes:
  - DNWELL enclosure margin
  - Shared guard ring clearance
  - Array-level routing tolerance

**Rule:**  
Pitch < **85.0 µm** is **explicitly forbidden** in this architecture.

---

### 4.2 Array Directionality

- **Primary array axis:** X
- **Secondary axis (Y):**
  - Used only for replication
  - No independent pitch optimization permitted

---

## 5. Guard Ring Architecture (Array Level)

- **Guard topology:** Column-wise shared P+ guard ring
- Guard continuity is **mandatory across the full column**
- Guard interruption or per-cell guard rings are **architecturally prohibited**

**Rationale:**
- Unit-level guard rings are removed
- The array-level guard defines the isolation domain

---

## 6. Power and Return Distribution

### 6.1 High-Voltage Supply (V)

- HV supply rail runs **parallel to the array direction**
- No per-cell HV segmentation allowed
- Local decoupling strategy is **out of scope**

---

### 6.2 Return Path (I)

- Return current continuity is prioritized over symmetry
- No shared return with logic or low-voltage domains

---

## 7. Edge and Termination Policy

### 7.1 Array Edge Cells

- Edge cells are **not functionally representative**
- Dummy or filler structures are **mandatory**

---

### 7.2 Guard Ring Termination

- Guard ring must fully enclose:
  - Active array region
  - Dummy edge region
- Partial or open guard termination is **forbidden**

---

## 8. Routing Policy

- **Inside HV_SW_UNIT:** Frozen by `HV_SW_UNIT_ARCH_V1`
- **Outside the unit cell:**
  - Horizontal routing preferred
  - Vertical jogs minimized
- **Metal usage:** Metal1 only  
  Metal2 or higher layers are **explicitly forbidden**

---

## 9. Explicit Non-Goals

This array architecture does **NOT** aim to address:

- Resolution scaling beyond 300 dpi
- Power integrity optimization
- Thermal behavior
- Reliability or electromigration
- LVS, SPICE correctness, or tape-out readiness
- Commercial PDK compliance

---

## 10. Allowed and Forbidden Changes

### Allowed (within ARRAY_ARCH_V1)

- Array length (number of HV_SW_UNIT instances)
- Placement of pads or bumps outside the array envelope
- Documentation and annotation updates

---

### Forbidden (require new ARRAY_ARCH)

- Pitch modification
- Guard topology changes
- Vertical metal (M2+) routing introduction
- HV_SW_UNIT internal geometry changes

---

## 11. Architectural Upgrade Path (Informational)

If future work requires:

- Resolution > 300 dpi  
- Pitch < 85.0 µm  
- Metal2 or higher routing  
- Alternative guard strategies  

A **new array architecture** must be defined, e.g.:

- `HV_SW_UNIT_ARRAY_400DPI_ARCH_V2`
- `HV_SW_UNIT_ARRAY_M2_ESCAPE_ARCH_V2`

Such work is **out of scope** for ARRAY_ARCH_V1.

---

## 12. Final Statement

This document marks a **deliberate stop point** in array-level physical exploration.

All future work based on `HV_SW_UNIT_ARRAY_300DPI_ARCH_V1` is  
**design execution**, not constraint discovery.

---

**End of ARRAY_ARCH_300DPI_V1.md**
