---
title: "HV_SW_UNIT 400 dpi Pitch Analysis (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT 400 dpi Pitch Analysis  
## Reverse Calculation of Cell Pitch and Bottleneck Identification

This document analyzes **whether the HV_SW_UNIT concept can scale toward
a 400 dpi inkjet printhead**, by reverse-calculating the available pitch
and identifying **layout bottlenecks in advance**.

This is a **feasibility and risk-identification document**, not a final layout plan.

---

## 1. What “400 dpi” Means Physically

### Definition
- 400 dpi = 400 dots per inch
- 1 inch = 25.4 mm

### Pitch Calculation
\[
\text{Pitch}_{400dpi} = \frac{25.4\ \text{mm}}{400}
\approx 63.5\ \mu\text{m}
\]

**Result:**
- **One nozzle center-to-center pitch ≈ 63.5 µm**

This pitch must accommodate:
- HV driver circuitry
- Routing
- Isolation structures
- Process margins

---

## 2. Practical Interpretation for Driver Layout

In a monolithic driver-per-nozzle concept:
- **All circuitry associated with one nozzle must fit within ~63.5 µm**
  in the nozzle-array direction.

This includes:
- HV switch(es)
- Guard rings
- DNWELL
- Power routing
- Spacing to neighboring cells

---

## 3. HV_SW_UNIT vs. 400 dpi Pitch

### Current v0.x Philosophy
- Conservative spacing
- DNWELL-enclosed HV island
- Continuous guard rings
- White space accepted

This is **intentionally incompatible** with direct 400 dpi packing.

That is acceptable.

---

## 4. Decomposition Strategy (Critical Insight)

> 400 dpi does **not** mean one HV_SW_UNIT equals one nozzle.

Instead, decompose:

- **Electrical unit**: HV_SW_UNIT (scalable, safe)
- **Geometric unit**: Nozzle pitch (tight, fixed)

Therefore:
- One nozzle may be driven by **fractional or shared HV structures**
- Or multiple HV_SW_UNITs may be placed **outside the nozzle pitch direction**

---

## 5. Likely Bottlenecks When Approaching 63.5 µm

### 5.1 Guard Rings
- Continuous guard rings consume lateral space
- Double guard rings between adjacent HV cells are wasteful
- Merging guard rings becomes mandatory at high density

**Risk:** Guard rings dominate pitch before devices do.

---

### 5.2 DNWELL Spacing
- DNWELL-to-DNWELL spacing rules are non-trivial
- Independent DNWELL islands per nozzle are unrealistic at 400 dpi

**Implication:**  
HV regions must be **shared DNWELL blocks**, not per-nozzle islands.

---

### 5.3 Power Routing Width
- HV drain metal must be wide
- Shared HV rails are required
- Individual HV routing per nozzle does not scale

---

### 5.4 Tap Density
- High-density taps consume area
- Per-unit conservative tap rules break down at high dpi

**Mitigation:**  
Move from “per-cell tap completeness” to “regional tap sufficiency”.

---

## 6. Architectural Consequence

To reach 400 dpi, the architecture must evolve:

### From (v0.x)
- Self-contained HV_SW_UNIT
- Fully enclosed guard rings
- Maximum isolation

### To (future)
- **Shared HV blocks**
- **Merged guard rings**
- **Common DNWELL regions**
- HV devices placed orthogonal to nozzle pitch where possible

This is an **architectural shift**, not a layout tweak.

---

## 7. Directional Placement Strategy

A common high-density strategy:

- **Nozzle pitch direction (tight):**
  - Minimal logic
  - Routing only
- **Orthogonal direction (looser):**
  - HV devices
  - Guard rings
  - DNWELL boundaries

This decouples:
- Electrical scaling
- Geometrical constraints

---

## 8. What v0.x Is *Not* Trying to Prove

- That a single HV_SW_UNIT fits inside 63.5 µm
- That 400 dpi is achievable with conservative rules
- That this PDK is production-optimal for inkjet

v0.x proves:
- Structural correctness
- Understanding of constraints
- A clean migration path

---

## 9. Early “Go / No-Go” Indicators

As layout progresses, watch for:
- Guard ring width approaching nozzle pitch fraction
- DNWELL spacing becoming dominant
- HV rail width exceeding allowable pitch

If these appear:
> The architecture must change — **not** the design rules.

---

## 10. Summary

- 400 dpi ⇒ ~63.5 µm pitch
- Conservative HV_SW_UNIT will not fit directly
- This is expected and acceptable
- Scaling requires **shared structures and architectural refactoring**
- v0.x exists to make that refactoring *informed*, not speculative

---

## 11. Next Steps

Logical continuations:
1. Define **shared HV block concept** (post-v0.x)
2. Separate **electrical unit vs. geometric unit** formally
3. Draft a **400 dpi target architecture diagram**
4. Decide where the HV driver physically lives relative to nozzles

---

**End of Document**
