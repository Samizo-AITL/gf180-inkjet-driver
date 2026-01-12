---
title: "ARRAY_REFERENCE_ARTIFACT_300DPI_V1"
description: "Reference GDS Artifact Definition for HV_SW_UNIT Array (300 dpi)"
---

# ARRAY_REFERENCE_ARTIFACT_300DPI_V1  
**HV_SW_UNIT Array – Reference GDS Artifact (300 dpi)**

This document designates the **authoritative reference GDS artifacts**  
for the **300 dpi HV_SW_UNIT array**, derived from frozen architectures.

- This is **NOT** a running log.
- This is **NOT** a design exploration.
- This document **locks reference artifacts** used for validation and reuse.

Once frozen, these artifacts **must not be regenerated or modified**.  
Any change requires a **new reference artifact revision**.

---

## 1. Purpose

- Define a **single, authoritative GDS reference** for the 300 dpi array
- Prevent silent divergence between scripts, layouts, and documentation
- Provide a stable **visual and geometric anchor** for downstream work

---

## 2. Reference Architectures

- `ARCHITECTURE.md`  
  - **HV_SW_UNIT_ARCH_V1**
- `ARRAY_ARCH_300DPI_V1.md`  
  - **HV_SW_UNIT_ARRAY_300DPI_ARCH_V1**

These architectures fully constrain the reference artifacts.

---

## 3. Reference Artifact ID

- **Artifact Name:** `HV_SW_UNIT_ARRAY_300DPI_REF_GDS_V1`
- **Status:** ACTIVE
- **Date Frozen:** 2026-01-12
- **Architecture Binding:**
  - HV_SW_UNIT_ARCH_V1
  - HV_SW_UNIT_ARRAY_300DPI_ARCH_V1

---

## 4. Designated Reference Files

### 4.1 Generator (Frozen)

- `layout/hv_nmos_gr/klayout/hv_sw_unit_array_gr_shared_300dpi.py`

**Rule:**  
This generator script is **frozen by reference**.  
Execution is allowed **only** to reproduce the identical GDS.

---

### 4.2 GDS (Authoritative)

- `layout/hv_nmos_gr/gds/hv_sw_unit_array_gr_shared_300dpi.gds`

This file is the **single source of geometric truth** for the array.

---

### 4.3 Visual Reference (Non-authoritative)

- `docs/images/06_hv_sw_unit_array_gr_shared_300dpi.png`

Images are **illustrative only** and must not be used for measurement.

---

## 5. Validity Conditions

The reference GDS is considered valid **only if**:

- Generated with the frozen script listed above
- Matches the following properties:
  - Pitch: **85.0 µm**
  - Guard topology: **column-wise shared P+ guard ring**
  - Metal usage: **Metal1 only**
  - DNWELL enclosure consistent with ARCH_V1 assumptions

Any deviation invalidates the reference.

---

## 6. Allowed Usage

The reference artifact may be used for:

- Array-level floorplanning
- Documentation and explanation
- Visual inspection and education
- Boundary definition for higher-level blocks

---

## 7. Explicitly Forbidden Usage

The reference artifact must **NOT** be used for:

- Electrical performance claims
- Reliability or EM qualification
- Tape-out or signoff
- LVS / DRC certification
- Commercial or production guarantees

---

## 8. Change Control

### Allowed
- Re-running the generator to reproduce the **identical** GDS
- Copying the GDS for **read-only** inspection

### Forbidden (require new REF)

- Modifying the generator
- Editing the GDS
- Changing pitch, routing, guard, or metal usage
- Regenerating under a different architecture

---

## 9. Supersession Policy

This reference artifact remains valid unless explicitly superseded by:

- `HV_SW_UNIT_ARRAY_300DPI_REF_GDS_V2`
- A new array architecture definition

---

## 10. Final Statement

This document freezes the **visual and geometric baseline**  
for the **300 dpi HV_SW_UNIT array**.

All future work must treat this GDS as **read-only reference**  
unless a new architecture or reference revision is formally defined.

---

**End of ARRAY_REFERENCE_ARTIFACT_300DPI_V1.md**
