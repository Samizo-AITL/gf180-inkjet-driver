# ARCHITECTURE.md  
**HV_SW_UNIT – Physical Architecture Definition**

This document defines the **fixed physical architecture** of HV_SW_UNIT.  
It is derived from RUNNING_LOG.md and represents **post-exploration decisions**.

- This is **NOT** a running log.
- This is **NOT** an experiment record.
- This document **freezes structural choices** based on observed constraints.

Once written, this file **must not be modified retroactively**.  
Architectural changes require a **new ARCHITECTURE revision**.

---

## 1. Purpose

- Convert layout-first exploration results into **explicit architectural decisions**
- Prevent accidental re-exploration of already-resolved constraints
- Serve as the **reference baseline** for all derived layouts and cells

---

## 2. Reference Documents

- `RUNNING_LOG.md`  
  - Runs 001–005 (Pitch discovery phase)
- Process: **GF180MCU Open PDK**
- Tooling: **KLayout 0.30.x**

---

## 3. Architecture ID

- **Architecture Name:** `HV_SW_UNIT_ARCH_V1`
- **Status:** ACTIVE
- **Date Frozen:** 2026-01-12
- **Derived From:** Run 005 conclusions

---

## 4. Fixed Architectural Decisions

### 4.1 Array Direction

- **Primary array direction:** X
- Y-array behavior is **out of scope** for this architecture

---

### 4.2 Pitch Definition

- **Nominal pitch:** **14 µm**
- **Rationale:**
  - 12 µm is geometrically possible but margin-poor
  - 14 µm provides stable physical margin under manual inspection
- **Rule:**
  - Pitch < 14 µm is **explicitly forbidden** in this architecture

---

### 4.3 Dominant Physical Constraint

- **Final dominant constraint:** **Metal1 stub geometry**
- Guard ring and poly gate end are **non-dominant** and considered resolved

---

### 4.4 Metal1 Strategy

- **Metal1 stub topology:** ACCEPTED AS-IS
- No M1 shortening, folding, or rerouting allowed
- No vertical (M2+) escape permitted

**Implication:**  
Metal1 spacing margin is protected by pitch choice, not topology change.

---

### 4.5 Guard Ring Strategy

- **Guard type:** Shared outer guard
- Per-cell guard rings are **architecturally prohibited**
- Guard geometry is considered **non-limiting**

---

### 4.6 Poly Gate End Handling

- Poly over-extension trimmed (Run 003)
- Poly is **not a pitch limiter**
- No further poly optimization allowed

---

## 5. Explicit Non-Goals

This architecture explicitly does **NOT** aim to address:

- Pitch scaling below 14 µm
- Circuit performance optimization
- LVS / SPICE correctness
- Tape-out readiness
- Reliability qualification
- Commercial PDK compliance

---

## 6. Allowed and Forbidden Changes

### Allowed (within ARCH_V1)
- Device count scaling
- X-array length variation
- Routing fan-out outside the unit cell
- Documentation and annotation improvements

### Forbidden (require new ARCH)
- Pitch reduction
- Metal1 topology change
- Metal2 or higher routing introduction
- Guard topology modification
- Poly geometry modification

---

## 7. Architectural Upgrade Path (Informational)

If future work requires pitch < 14 µm, a **new architecture** must be defined:

- `HV_SW_UNIT_ARCH_V2_M1_REDESIGN`
- `HV_SW_UNIT_ARCH_V2_M2_ESCAPE`

Such work is **out of scope** for ARCH_V1.

---

## 8. Final Statement

This architecture represents a **deliberate stop point** in physical exploration.

All future work based on HV_SW_UNIT_ARCH_V1 is **design execution**,  
not constraint discovery.

---

**End of ARCHITECTURE.md**
