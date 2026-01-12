---
title: "HV_SW_UNIT V–I Expectations (Pre-SPICE) (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT V–I Expectations (Pre-SPICE)  
## What We Expect Before Running Simulations

This document defines **expected V–I behaviors and sanity ranges**
for the `HV_SW_UNIT` *before* detailed SPICE validation.

It is not a specification.
It is a **pre-check framework** to prevent “nonsense layouts” from progressing.

---

## 1. Scope

Applies to:
- Process: GF180MCU Open PDK
- Device: 10 V LDNMOS (LDMOS)
- Unit sizing (v0.x): L = 1.0 µm, W = 10 µm (effective), multi-finger
- Topology: HV low-side switch (initial PoC)

---

## 2. Why Define Expectations First?

> If we do not define expectations, we cannot detect mistakes early.

Common early-stage failures:
- Source/drain swapped
- Floating bulk / missing taps
- Gate net not actually reaching all fingers
- Guard ring not tied to the intended reference
- Severe parasitics from poor routing

V–I expectations help detect these with minimal effort.

---

## 3. Measurement Set (Minimum)

All measurements use **V–I (Voltage–Current)** notation explicitly.

### A) Output Characteristics: Id–Vd (at multiple Vg)
- Sweep: Vd from 0 → 10 V
- Step: Vg (e.g., 0 V, 2 V, 4 V, 6 V, 8 V, 10 V)
- Observe: linear region → saturation behavior → HV effects

### B) Transfer Characteristics: Id–Vg (at fixed Vd)
- Fix: Vd = 10 V (HV worst-ish)
- Sweep: Vg from 0 → 10 V
- Observe: turn-on, subthreshold, strong inversion region

### C) Leakage Checks (critical in HV)
- Vg = 0 V, Vd = 10 V : off-state leakage
- Vg = 0 V, Vd = small : near-zero baseline
- Optional: temperature sweep later (not in v0.x)

---

## 4. Shape-Based Sanity Expectations (No Numbers Yet)

### 4.1 Id–Vd (Vg stepped)
Expected qualitative shape:
- For low Vg: Id stays near leakage (flat, tiny)
- For moderate Vg: Id increases roughly linearly at low Vd, then bends
- For high Vg: Id shows strong drive, with clear region transition

Red flags:
- Id decreases with increasing Vd (non-physical in normal region)
- Id is ~0 for all Vg (gate disconnected / wrong device)
- Id is huge even at Vg = 0 (short / wrong net / missing bulk tie)

### 4.2 Id–Vg (Vd fixed at 10 V)
Expected qualitative shape:
- Very low Id at low Vg
- Smooth monotonic increase with Vg
- Strong increase after threshold region

Red flags:
- Non-monotonic Id–Vg
- Sudden discontinuities (often connectivity or convergence issues)
- Strong conduction at Vg = 0 (short or body diode path unintended)

---

## 5. Rule-of-Thumb Numeric Boundaries (Loose)

> Numbers below are intentionally wide to avoid false alarms.

### 5.1 Off-State Leakage (Vg = 0 V, Vd = 10 V)
Expectation:
- “Small” current, orders of magnitude below on-current

Alarm condition:
- Leakage is within one or two orders of magnitude of on-current  
  (likely a short, wrong orientation, or missing isolation)

### 5.2 On-State Current (Vg high, Vd moderate-to-high)
Expectation:
- Clearly measurable conduction
- Scales approximately with **N × HV_SW_UNIT** replication

Alarm condition:
- Doubling unit count does not roughly increase current  
  (indicates routing bottleneck, contact limitation, or connectivity error)

---

## 6. Replication Consistency Expectations

If we tile `HV_SW_UNIT`:
- Current should scale approximately linearly with the number of units
- Variance between identical units should be small (layout symmetry helps)

Red flags:
- One unit “dominates” the current (local short / unequal routing)
- Current scaling saturates too early (metal/via limiting)

---

## 7. Body / Bulk Reference Expectations

For a robust HV switch:
- Bulk / substrate reference must be explicit and stable
- Guard rings must be tied to the intended reference potential

Red flags:
- V–I curves change dramatically with tiny bulk reference modifications
- Convergence depends on artificial gmin too heavily  
  (often floating bodies or missing taps)

---

## 8. Parasitic Awareness (Layout-Driven)

Even before extraction:
- Long/narrow drain routing can reduce effective on-current
- Gate resistance can distort switching behavior (later transient)
- Poor tap density can shift apparent threshold or leakage

Expectation:
- v0.x prioritizes robust geometry, so parasitic sensitivity should be reduced

---

## 9. Acceptance Gate (Pre-SPICE → SPICE)

We proceed to extracted simulations only if:
- [ ] Id–Vd curves look physically plausible
- [ ] Id–Vg is monotonic and clean
- [ ] Off-state leakage is clearly “small”
- [ ] Replication roughly increases current
- [ ] No signs of floating bulk / missing taps

---

## 10. Next Steps

After these expectations are documented:
1. Run schematic-level SPICE (no parasitics)
2. Confirm shapes and rough magnitudes
3. Run extracted SPICE
4. Update this document with measured ranges (v0.2)

---

**End of Document**
