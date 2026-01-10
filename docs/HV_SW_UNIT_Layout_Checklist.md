---
title: "HV_SW_UNIT Layout Checklist (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT Layout Checklist  
## Step-by-Step Guide Before and During Layout

This document provides a **practical, ordered checklist**
for laying out the `HV_SW_UNIT` safely and consistently.

It is intended to be used **while the layout tool is open**.

---

## 1. Pre-Layout Confirmation (Before Drawing Anything)

### Design Rule Alignment
- [ ] `DesignRules_HV.md` reviewed
- [ ] `HV_SW_UNIT_Definition.md` reviewed
- [ ] `HV_SW_UNIT_Floorplan.md` reviewed
- [ ] `HV_SW_UNIT_LW_Proposal.md` reviewed

### Fixed Parameters
- [ ] Device type: **10 V LDNMOS**
- [ ] Channel length L = **1.0 µm**
- [ ] Channel width W = **10 µm (unit)**
- [ ] Multi-finger structure selected

---

## 2. Define Cell Boundary First

> Never start with transistors.

- [ ] Draw **rectangular cell boundary**
- [ ] Cell size is intentionally generous
- [ ] Boundary supports horizontal and vertical tiling
- [ ] No shapes allowed to cross boundary later

---

## 3. Place DNWELL (Isolation Comes First)

- [ ] DNWELL fully encloses the cell
- [ ] DNWELL edge aligned with cell boundary
- [ ] DNWELL spacing is not minimized
- [ ] DNWELL is clearly isolated from LV regions

---

## 4. Place Guard Ring Structure

### P-Substrate Guard Ring
- [ ] Continuous (non-broken) loop
- [ ] Uniform width on all sides
- [ ] Fully inside DNWELL
- [ ] Corners are clean and orthogonal

### Guard Ring Philosophy Check
- [ ] Guard ring is part of the cell, not optional
- [ ] Guard ring survives cell tiling

---

## 5. Place Active LDMOS Device

### Geometry
- [ ] Multi-finger structure implemented
- [ ] Finger widths are equal
- [ ] Total effective W = 10 µm
- [ ] L = 1.0 µm confirmed

### Placement
- [ ] Device centered within guard ring
- [ ] No diffusion touches guard ring
- [ ] Symmetry preserved

---

## 6. Source / Drain Orientation Check

- [ ] Source faces local ground rail
- [ ] Drain faces HV output direction
- [ ] Orientation consistent with floorplan
- [ ] No accidental source/drain swap

---

## 7. Source Routing (Ground)

- [ ] Short, wide metal
- [ ] Minimal via stack height
- [ ] Ground routing does not cross HV drain metal
- [ ] Designed to merge cleanly when tiled

---

## 8. Drain Routing (HV Output)

- [ ] Metal width larger than signal nets
- [ ] Direct path to cell edge
- [ ] No parallel run with gate metal
- [ ] Spacing from gate respected

---

## 9. Gate Routing (Control Signal)

- [ ] Central or top-entry routing
- [ ] Symmetric gate connection
- [ ] Shielded from HV drain where possible
- [ ] Gate metal does not cross guard ring breaks

---

## 10. Well / Substrate Contacts

### P-Substrate Contacts
- [ ] Dense placement
- [ ] Uniform distribution
- [ ] Located inside guard ring

### DNWELL Contacts
- [ ] Proper reference potential connected
- [ ] Not shared with LV domain
- [ ] Clear visibility in layout

---

## 11. Metal Density & Geometry Sanity

- [ ] No extremely narrow metal segments
- [ ] No sharp acute angles
- [ ] Metal density visually balanced
- [ ] White space accepted where helpful

---

## 12. Tiling Dry-Run (Mental or Copy Test)

- [ ] Copy cell horizontally
- [ ] Copy cell vertically
- [ ] Guard rings align or merge cleanly
- [ ] Power rails connect naturally
- [ ] No DRC spacing violations appear obvious

---

## 13. Pre-DRC Sanity Check

> Run this before the first DRC.

- [ ] All shapes are inside intended layers
- [ ] No forgotten floating regions
- [ ] All contacts are connected
- [ ] Net names are consistent

---

## 14. First DRC Run

- [ ] DRC run with **full margins**
- [ ] Violations reviewed one by one
- [ ] No “waived by assumption” items

---

## 15. Post-DRC Reflection

- [ ] Layout is readable at zoom-out
- [ ] HV structure is visually obvious
- [ ] Guard rings are unmistakable
- [ ] Cell looks safe, not aggressive

If the layout looks *too tight*, it probably is.

---

## 16. Next Actions After Clean DRC

1. Extract parasitics
2. Run basic DC simulations
3. Verify Id–Vg / Id–Vd behavior
4. Document any layout-driven assumptions

---

## 17. Rule of Thumb (Final Reminder)

> If something feels unclear in layout,  
> future-you will not understand it either.

Clarity beats cleverness.

---

**End of Document**
