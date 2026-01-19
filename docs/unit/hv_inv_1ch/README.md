# HV Inverter 1ch Unit (300dpi)

## Status: **INCOMPLETE / UNDER DEFINITION**

This layout represents a **work-in-progress basic physical cell**
for a **high-voltage CMOS inverter** intended for inkjet printhead drivers.

This is **not a finished macro**.
It is a **physically grounded architectural baseline** whose purpose is
to make design assumptions and limitations explicit.

---

## Evidence Layout Snapshot

![HV Inverter 1ch Layout (Current State)](../images/15_hv_inv_1ch_260119.png)

**Figure 1 — Current HV Inverter 1ch layout (300dpi pitch)**  
This snapshot is the *authoritative reference* for all statements in this document.

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

This cell exists to:

- Establish a **stable geometric reference** for array construction
- Visualize **HV-relevant physical layers**
- Separate *what is already fixed* from *what is still undecided*
- Act as a **design contract draft** between circuit, layout, and process

It does **not** aim to be DRC/LVS clean at this stage.

---

## Pins (Logical Intent)

| Pin   | Description |
|------|-------------|
| VIN  | Logic-level input (routing incomplete) |
| VOUT | High-voltage output |
| VDDH | High-voltage supply |
| VSSH | High-voltage ground |

> The electrical realization of these pins is **not finalized**.
> Their intent is shown, but pin shapes and LVS meaning are incomplete.

---

## Evidence of Key Design Decisions

### 1. Single Geometric Reference (Cell Center)

![VOUT Center Alignment](../images/15_hv_inv_1ch_260119.png)

**Figure 2 — VOUT trunk aligned to cell center**

- The vertical center line of the cell is used as the **sole geometric reference**
- The **VOUT metal trunk is placed on this center line**
- PMOS and NMOS drain regions are symmetrically aligned to this line

This guarantees **horizontal arrayability without cumulative offset**.

---

### 2. HV Asymmetry Without Cell Offset

![Gate Shift and Drift Region](../images/15_hv_inv_1ch_260119.png)

**Figure 3 — Gate offset and drain-side drift region**

- Drain diffusion remains centered
- The **gate is intentionally shifted to one side**
- HV intent is expressed through:
  - gate–drain spacing
  - conceptual LDD / drift region

The cell boundary itself remains symmetric and tile-safe.

---

### 3. Explicit Physical Layer Visibility

![Well and Diffusion Visibility](../images/15_hv_inv_1ch_260119.png)

**Figure 4 — Wells, diffusions, and active regions explicitly visible**

The layout intentionally exposes:

- dnwell
- nwell / pwell
- n+ / p+ diffusions
- poly gate
- contacts
- metal routing

This avoids abstract “symbolic” layouts that hide HV behavior.

---

## Visible Layers (Current)

The following layers are explicitly included **for physical interpretability**:

- dnwell  
- nwell / pwell  
- n+ diffusion / p+ diffusion  
- conceptual HV drift / LDD regions  
- poly (gate)  
- contact  
- metal1  
- cell boundary (bbox)

> Layer usage is **conceptual** and not yet mapped 1:1 to final PDK definitions.

---

## Arrayability

- **Horizontal tiling**: Supported geometrically  
  - Fixed 300dpi pitch
  - Center-aligned VOUT
  - Fixed power rail positions
- **Vertical tiling**: Not intended for this unit

Electrical continuity in arrays is **not yet guaranteed**.

---

## Known Incompleteness (By Design)

The following are **explicitly unfinished**:

- ❌ DRC compliance
- ❌ LVS readiness
- ❌ Final HV device layer mapping
- ❌ VIN routing strategy
- ❌ Guard ring electrical definition
- ❌ Power distribution strategy

These omissions are **intentional** at this stage.

---

## Completion Criteria (Definition of “Done”)

This 1ch unit will be considered *complete* only when:

1. VIN / VOUT / VDDH / VSSH are electrically unambiguous
2. HV NMOS/PMOS match real PDK device definitions
3. Guard ring strategy (local vs shared) is fixed
4. Horizontal arrays auto-form valid power and signal connectivity
5. Top-level requirements are explicitly documented

---

## Next Steps

### Priority 1 — Interface Definition
Define a formal **HV_INV_1CH Interface Definition**:
- what the cell requires from the top level
- what the cell guarantees to the array

### Priority 2 — Array-Level Validation
- Generate 10ch / 300ch arrays
- Verify alignment, routing feasibility, and power integrity

### Priority 3 — Process Alignment
- Map conceptual layers to GF180 PDK layers
- Introduce minimum DRC-aware dimensions

---

## Summary

This layout is **intentionally incomplete but physically honest**.

The figures above serve as **evidence**, not decoration:
they show exactly what is fixed, what is assumed, and what is missing.

The next phase is not drawing more shapes,
but defining **how this cell integrates into a real product-level array**.
