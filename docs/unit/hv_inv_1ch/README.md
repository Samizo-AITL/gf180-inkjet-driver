# HV Inverter 1ch Unit (300dpi)

## Status: **INCOMPLETE / UNDER DEFINITION**

This layout represents a **work-in-progress basic physical cell**
for a **high-voltage CMOS inverter** intended for inkjet printhead drivers.

This is **not a finished macro**.
It is a **physically grounded architectural baseline** used to make
design assumptions, limitations, and next actions explicit.

---

## Evidence Layout Snapshot

![HV Inverter 1ch Layout](/gf180-inkjet-driver/docs/images/15_hv_inv_1ch_260119.png)

**Figure 1 — Current HV Inverter 1ch layout (300dpi pitch)**  
This figure is the **authoritative evidence** for all statements in this document.

---

## Overview

- Target pitch: **300 dpi (≈84.7 µm)**
- Function: **1-channel HV CMOS inverter**
- Intended use: **inkjet nozzle driver array**
- Process class: **GF180-class open PDK (conceptual)**

The cell is designed to be **horizontally tileable** and to serve as the
**minimum physical unit** for a multi-channel HV driver array.

---

## Purpose

The purpose of this cell is **not tapeout readiness**, but to:

- Establish a **stable geometric reference** for array construction
- Visualize **HV-relevant physical layers**
- Separate *what is fixed* from *what is still undefined*
- Act as a **draft design contract** between
  circuit, layout, and process domains

---

## Pins (Logical Intent)

| Pin   | Description |
|------|-------------|
| VIN  | Logic-level input (routing not finalized) |
| VOUT | High-voltage output (center-aligned) |
| VDDH | High-voltage supply |
| VSSH | High-voltage ground |

> Electrical pin realization (pin layers, LVS intent)
> is **not finalized** in the current layout.

---

## Visible Physical Layers

The layout explicitly exposes the following layers to preserve
physical interpretability:

- dnwell  
- nwell / pwell  
- n+ diffusion / p+ diffusion  
- conceptual HV drift / LDD regions  
- poly (gate)  
- contact  
- metal1  
- cell boundary (bbox)

These layers are shown **for understanding and discussion**,  
not yet as exact PDK-compliant device definitions.

---

## Layout Design Principles

### 1. Single Geometric Reference (Cell Center)

![Center Alignment Evidence](/gf180-inkjet-driver/docs/images/15_hv_inv_1ch_260119.png)

**Figure 2 — VOUT trunk aligned to the cell center**

- The **cell center line (xc)** is defined as the **VOUT trunk**
- This vertical line is the **only global alignment reference**

This guarantees:
- no horizontal drift when cells are tiled
- stable VOUT alignment across large arrays
- predictable array-level routing

---

### 2. HV Asymmetry Without Cell Offset

![Gate Shift and Drift Evidence](/gf180-inkjet-driver/docs/images/15_hv_inv_1ch_260119.png)

**Figure 3 — Gate shift and drain-side drift region**

- Drain regions remain **centered on xc**
- The **gate is intentionally shifted** to one side
- HV intent is expressed by:
  - gate–drain spacing
  - conceptual drift / LDD regions

Cell geometry itself remains symmetric and tile-safe.

---

### 3. Guard Ring Strategy (Not Final)

- This 1ch cell includes **only minimal local structures**
- Guard rings are assumed to be:
  - implemented at the **array or top-cell level**
  - shared across multiple channels
- Substrate and well tie potentials are **not finalized**

---

## Arrayability

- **Horizontal tiling**: Geometrically supported  
  - Fixed 300dpi pitch
  - Center-aligned VOUT
  - Fixed power rail positions
- **Vertical tiling**: Not intended for this unit

Electrical continuity in arrays is **not yet guaranteed**.

---

## Known Incompleteness (Intentional)

The following aspects are **explicitly unfinished**:

- ❌ DRC compliance
- ❌ LVS readiness
- ❌ Final HV device layer mapping
- ❌ VIN routing definition
- ❌ Guard ring electrical definition
- ❌ Power distribution strategy

These are **design-stage omissions**, not oversights.

---

## Completion Criteria (Definition of “Done”)

This 1ch unit will be considered *complete* only when:

1. VIN / VOUT / VDDH / VSSH are electrically unambiguous
2. HV NMOS/PMOS match real PDK device definitions
3. Guard ring strategy (local vs shared) is fixed
4. Horizontal arrays automatically form valid power and signal connectivity
5. Top-level requirements are explicitly documented

---

## Next Steps

### Priority 1 — Interface Definition
Define a formal **HV_INV_1CH Interface Definition**:
- what this cell requires from the top level
- what it guarantees to the array

### Priority 2 — Array-Level Validation
- Generate 10ch / 300ch arrays
- Verify alignment, routing feasibility, and power integrity

### Priority 3 — Process Alignment
- Map conceptual layers to actual GF180 PDK layers
- Introduce minimum DRC-aware dimensions

---

## Summary

This layout is **intentionally incomplete but physically honest**.

The figures above are **evidence**, not decoration:
they show exactly what is fixed, what is assumed, and what is missing.

The next phase is not drawing more shapes,
but defining **how this cell integrates into a real product-level array**.
