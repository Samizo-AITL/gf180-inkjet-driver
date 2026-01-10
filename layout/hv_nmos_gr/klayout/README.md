---
title: "HV_SW_UNIT – KLayout Generator & GDS Reference"
description: "Parametric KLayout (pya) generator and committed GDS reference for GF180 HV switch unit with DNWELL and guard ring"
---

# HV_SW_UNIT – KLayout Generator & GDS Reference

This directory provides a **minimum viable high-voltage switch unit (HV_SW_UNIT)**
for **GF180MCU-based inkjet driver exploration**.

It includes:

- A **parametric KLayout (pya) generator script**
- A **committed, inspectable GDS reference**
- Documentation aligned to layout-first HV design

This work is **GDS-oriented and layout-first**, prioritizing:
- DNWELL isolation strategy
- Guard ring continuity
- Replication-ready unit geometry

This is **not** a qualified device or production-ready IP.

---

## Directory Structure

```
layout/hv_nmos_gr/
├─ klayout/
│  ├─ hv_sw_unit.py     # KLayout (pya) generator script
│  └─ README.md
├─ gds/
│  ├─ hv_sw_unit.gds    # Generated and committed GDS reference
│  └─ .gitkeep
```

---

## What This Generator Does

The `hv_sw_unit.py` script generates a **self-contained HV switch unit skeleton**
with the following features:

- DNWELL enclosure
- P+ guard ring (continuous ring geometry)
- Central HV device placeholder
- Explicit pin markers (D / G / S / B)

The default implementation uses **PDK-independent placeholder geometry**
to ensure that:

- The script runs without requiring the GF180 PDK
- The generated GDS is always inspectable

A **PDK-provided HV nLDMOS cell** can be substituted later
as a drop-in replacement.

---

## Generated GDS Reference

- **File**: `gds/hv_sw_unit.gds`
- **Cell name**: `HV_SW_UNIT`
- **Status**: Committed, inspectable reference layout

This GDS serves as:

- A visual reference for HV isolation overhead
- A concrete example of DNWELL + guard ring interaction
- A baseline unit for array tiling and pitch studies

No DRC, LVS, or electrical guarantees are implied.

---

## Requirements (for Script Execution)

- **KLayout** (tested with 0.30.x)
- Python macro support enabled

Optional:
- **GF180MCU Open PDK** (only required when instantiating real HV devices)

---

## Usage

1. Open **KLayout**
2. Open **Macro Development**
3. Load and run:

```
klayout/hv_sw_unit.py
```

4. The following file will be generated:

```
C:\Users\<user>\KLayout\hv_sw_unit.gds
```

---

## Design Philosophy

- Layout-first, not schematic-driven
- Conservative spacing and explicit isolation
- No density or performance optimization
- Intended for:
  - Structural understanding
  - DRC iteration
  - Replication into multi-channel HV arrays

---

## Limitations

- No schematic or LVS intent
- No electrical performance claims
- Device physics delegated to future PDK substitution
- Dimensions are PoC-safe defaults only

---

## Relation to Project Documentation

This HV_SW_UNIT directly supports:

- `DesignRules_HV.md`
- `HV_SW_UNIT_Definition.md`
- `HV_SW_UNIT_Floorplan.md`
- `HV_SW_UNIT_Layout_Checklist.md`

These documents explain **why** this structure exists;
the GDS shows **what it looks like in reality**.

---

## Disclaimer

Provided **for educational and exploratory purposes only**.  
No guarantees of manufacturability or commercial suitability.

---

## Next Steps

- Pitch-constrained variant (≈63.5 µm @ 400 dpi)
- Array tiling experiments
- Guard ring sharing vs. isolation trade-offs
- PEX → SPICE → V–I (Id–Vd / Id–Vg) sanity checks
