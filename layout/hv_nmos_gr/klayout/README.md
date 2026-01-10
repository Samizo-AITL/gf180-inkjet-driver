---
title: "HV_SW_UNIT – KLayout Generator"
description: "Parametric KLayout (pya) script for GF180 HV nLDMOS switch unit with DNWELL and guard ring"
---

# HV_SW_UNIT – KLayout Generator

This directory contains a **KLayout (pya) script** that generates a
**minimum viable high-voltage switch unit (HV_SW_UNIT)** for
GF180MCU-based inkjet driver exploration.

The layout is **GDS-oriented and layout-first**, focusing on:
- DNWELL isolation
- Guard ring continuity
- Replication-friendly unit structure

This is **not** a complete IC or qualified device layout.
It is a **layout exploration scaffold** intended for educational and PoC use.

---

## Contents

```
klayout/
├─ hv_sw_unit.py     # Main KLayout (pya) generator script
└─ README.md         # This document
```

Generated files (example):
```
gds/
└─ hv_sw_unit.gds    # Generated GDS (not committed)
```

---

## What This Script Does

- Instantiates a **PDK-provided HV nLDMOS cell** (10 V class)
- Automatically generates:
  - DNWELL enclosure
  - Guard ring (P+ diffusion)
  - Basic pin markers (D / G / S / B)
- Produces a **tileable HV switch unit skeleton**

Electrical optimization is **explicitly out of scope**.

---

## Requirements

- **KLayout**
- **GF180MCU open PDK** loaded into KLayout
- Access to a **HV nLDMOS PDK cell** (example: 10 V nLDMOS)

---

## Usage

1. Open **KLayout**
2. Ensure the **GF180 PDK** is loaded
3. Edit `hv_sw_unit.py` and set the correct PDK cell name:

```python
lib_name  = "gf180mcu"
cell_name = "nldmos_10v"  # replace with actual PDK cell name
```

4. Run the script:

```
Tools → Run Script → hv_sw_unit.py
```

5. The following file will be generated:

```
hv_sw_unit.gds
```

---

## Design Philosophy

- **Layout-first**
- Conservative spacing and isolation
- Explicit avoidance of density optimization
- Structures chosen for:
  - Visual inspection
  - DRC iteration
  - Replication into multi-channel arrays

All decisions are driven by **downstream GDS feasibility**.

---

## Limitations

- No schematic or LVS intent
- No guaranteed electrical performance
- Device physics fully delegated to **PDK-defined cells**
- Dimensions are **PoC-safe defaults**, not optimized values

---

## Relation to Project Docs

This script directly supports the following documents:

- `DesignRules_HV.md`
- `HV_SW_UNIT_Definition.md`
- `HV_SW_UNIT_Floorplan.md`
- `HV_SW_UNIT_Layout_Checklist.md`

---

## Disclaimer

For **educational and exploratory use only**.  
No guarantees of manufacturability, reliability, or commercial suitability.

---

## Next Steps

- Pitch-constrained version (≈63.5 µm @ 400 dpi)
- Automated spacing rules tied to DRC feedback
- Multi-unit tiling experiments
- PEX → SPICE → V–I (Id–Vd / Id–Vg) sanity checks
