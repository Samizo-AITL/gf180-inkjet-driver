---
title: "HV_SW_UNIT L/W Proposal (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT L/W Proposal  
## Tentative Channel Dimensions for Initial PoC

This document proposes **tentative channel length (L) and width (W) values**
for the `HV_SW_UNIT` defined in previous documents.

These values are intended for:
- Initial layout and simulation
- Structural understanding
- Safe high-voltage operation

They are **not optimized** for performance, area, or power.

---

## 1. Design Intent

> The first numeric choice must be conservative and explainable.

Key intentions:
- Avoid minimum geometry
- Reduce sensitivity to process variation
- Enable clean scaling by replication
- Provide a stable reference for future tuning

---

## 2. Target Device Recap

| Item | Value |
|---|---|
| Process | GF180MCU Open PDK |
| Device | 10 V LDNMOS (LDMOS) |
| Role | HV low-side switch |
| Operating voltage | VDD_HV = 10 V |

---

## 3. Channel Length (L) Selection

### Policy
- **Do not use minimum L**
- Prefer long-channel behavior

### Tentative Proposal
- **L = 1.0 µm**

### Rationale
- Significantly larger than minimum geometry
- Reduces electric field peak near drain
- Improves matching across replicated units
- Easier to correlate layout with device behavior

### Rule
- L is **fixed** for all HV_SW_UNIT instances in v0.x

---

## 4. Channel Width (W) Selection

### Policy
- W defines **unit current**
- Scaling is achieved by replication, not resizing

### Tentative Proposal
- **W = 10 µm per HV_SW_UNIT**

### Rationale
- Wide enough to carry meaningful current
- Narrow enough to keep the unit cell readable
- Compatible with multi-finger layout
- Allows intuitive scaling (e.g. 4×, 8× units)

---

## 5. Finger Configuration Example

Given:
- L = 1.0 µm
- W = 10 µm

Recommended structure:
- 4 fingers × 2.5 µm each  
  or  
- 5 fingers × 2.0 µm each

Rules:
- Symmetry is mandatory
- Finger widths should be equal
- Gate routing must be balanced

---

## 6. Effective Scaling Strategy

### Unit Definition
- **1 HV_SW_UNIT = 10 µm effective width**

### Scaling Examples
| Units | Effective W |
|---|---|
| 1 | 10 µm |
| 2 | 20 µm |
| 4 | 40 µm |
| 8 | 80 µm |

This keeps:
- Layout rules unchanged
- Guard ring strategy intact
- Floorplan reusable

---

## 7. Why These Numbers Are Intentionally “Loose”

- Long L sacrifices speed → acceptable for inkjet timing
- Large W increases area → acceptable in PoC
- Conservative sizing improves first-pass DRC success
- Numbers are easy to remember and communicate

---

## 8. What This Does *Not* Guarantee

- Final drive current accuracy
- Thermal optimization
- Minimum cell pitch
- 400 dpi density compliance

These are **future optimization tasks**.

---

## 9. Review Checklist

- [ ] L is not minimum
- [ ] W is unitized and fixed
- [ ] Finger count preserves symmetry
- [ ] Scaling uses replication only
- [ ] Numbers are documented and traceable

---

## 10. Next Steps

After adopting this proposal:
1. Draw the first **HV_SW_UNIT layout**
2. Run DRC with full margins
3. Perform DC sweep (Id–Vd, Id–Vg)
4. Estimate current per unit at 10 V
5. Adjust W only if *clearly necessary*

---

## 11. Versioning Policy

- Changes to L/W require:
  - Version increment
  - Simulation evidence
  - Layout impact review

---

**End of Document**
