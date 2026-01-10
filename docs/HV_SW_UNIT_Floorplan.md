---
title: "HV_SW_UNIT Floorplan Definition (GF180 Inkjet Driver)"
author: "Shinichi Samizo"
date: 2026-01-10
version: v0.1
status: draft
---

# HV_SW_UNIT Floorplan Definition  
## Standard Physical Structure for HV Switch Unit

This document defines the **physical floorplan structure** of the
`HV_SW_UNIT`, the minimum high-voltage switch cell used in the
GF180 inkjet driver project.

The floorplan is designed to be:
- Layout-safe for 10 V operation
- Readable and educational
- Naturally scalable by tiling
- Robust against latch-up and substrate noise

---

## 1. Floorplan Design Philosophy

> The floorplan must explain itself.

Core principles:
- Explicit separation of functions
- Guard rings and wells are **structural elements**, not afterthoughts
- Geometry favors safety and clarity over density

---

## 2. Overall Cell Structure

The HV_SW_UNIT is a **rectangular, tilable cell** composed of:

1. Active HV device region (LDMOS)
2. Guard ring structure
3. Well / substrate isolation
4. Power and signal routing corridors

All elements are **contained within the unit cell boundary**.

---

## 3. Well and Isolation Structure

### DNWELL Policy
- The entire HV_SW_UNIT is enclosed by **DNWELL**
- DNWELL boundary is aligned to the cell outline
- DNWELL spacing is **never minimized** in v0.x

Purpose:
- Electrical isolation from LV / IO regions
- Improved latch-up immunity
- Predictable substrate behavior when tiled

---

## 4. Guard Ring Placement

### Primary Guard Ring
- **P-substrate guard ring**
- Continuous (non-broken) loop
- Located **inside DNWELL**, surrounding the active device

### Guard Ring Geometry
- Uniform width on all sides
- Corner shapes kept simple (orthogonal)
- Guard ring encloses:
  - Active device
  - Source/drain diffusion edges
  - First-level contacts

### Integration Rule
- Guard ring is part of the cell, not optional
- When cells are tiled, guard rings may **merge seamlessly**

---

## 5. Active Device Placement

### LDMOS Orientation
- Source side oriented toward **local ground rail**
- Drain side oriented toward **HV output direction**
- Gate located centrally for symmetric routing

### Placement Rules
- Active device is centered within the guard ring
- No diffusion edge touches the guard ring directly
- Adequate spacing is preserved on all sides

---

## 6. Source / Drain / Gate Routing Zones

### Source (S)
- Connected to local ground
- Short, wide metal
- Prefer vertical routing for tiling consistency

### Drain (D)
- Routed toward HV load side
- Metal width is larger than signal nets
- Avoids crossing gate routing

### Gate (G)
- Routed from the top or center
- Shielded from HV drain metal where possible
- Gate routing corridor is reserved explicitly

---

## 7. Tap and Contact Strategy

### Substrate / Well Contacts
- High-density contacts around HV device
- Uniform distribution on all sides
- Contacts are **inside the guard ring**

### DNWELL Contacts
- Connected to defined reference potential
- Not shared with LV domains

Policy:
> Electrical reference points must be obvious in the layout.

---

## 8. Power Rail Placement

### Ground Rail
- Placed on one side of the cell
- Shared naturally when cells are tiled

### HV Output Rail
- Placed on the opposite side of the cell
- Designed for aggregation across multiple units

This opposing-rail structure simplifies scaling.

---

## 9. Cell Boundary and Tiling

### Boundary Rules
- Cell outline is rectangular
- No shapes cross the boundary
- Boundary aligns with DNWELL edge

### Tiling Behavior
- Horizontal and vertical tiling supported
- Guard rings merge or align without gaps
- Power rails connect automatically

---

## 10. Area Philosophy

- White space is acceptable
- Density optimization is deferred
- Floorplan must remain readable at a glance

---

## 11. Floorplan Sanity Checklist

- [ ] DNWELL fully encloses the unit cell
- [ ] Guard ring is continuous and internal
- [ ] Active device is centered
- [ ] Source and drain directions are consistent
- [ ] Gate routing is isolated from HV metal
- [ ] Cell tiles without rule violations

---

## 12. Next Steps

After fixing this floorplan:
1. Assign **tentative L/W numeric values**
2. Draw actual layout in PDK tools
3. Run DRC with exaggerated margins
4. Perform basic DC and transient checks

---

**End of Document**
