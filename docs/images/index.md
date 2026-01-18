---
title: "gf180-inkjet-driver"
description: "layout- and GDS-oriented design notes"
---

# GDS Screenshot Index

This page lists **all screenshot PNGs** generated during the
**GF180 HV layout and GDS-oriented exploration**.

Each image corresponds to a **concrete GDS artifact**
and a **documented Run or structural milestone**.
This index exists purely to make visual inspection easy.

---

## Environment

<img src="01_gf180_inkjet_env_klayout.png" width="80%" />

- KLayout environment used for all manual and macro-based layout work

---

## HV_SW_UNIT – Single / Array (Baseline)

<img src="02_hv_sw_unit_gds.png" width="80%" />

- Single HV_SW_UNIT with DNWELL and guard ring

<img src="03_hv_unit_array_full_gds.png" width="80%" />

- Naive array with per-unit DNWELL and guard ring  
- Pitch dominated by guard ring enclosure

---

## Guard Ring Sharing Study

<img src="04_hv_sw_unit_array_gr_shared_FIXED_gds.png" width="80%" />

- Column-wise guard ring sharing (intermediate state)

<img src="05_hv_sw_unit_array_gr_shared_clean_gds.png" width="80%" />

- Guard-ring-clean shared configuration  
- Guard ring no longer dominant pitch limiter

---

## 300 dpi Array (Golden Baseline)

<img src="06_hv_sw_unit_array_gr_shared_300dpi.png" width="80%" />

- 300 dpi (~85 µm pitch) array  
- Structurally feasible under GF180 DNWELL constraints  
- Treated as **golden baseline**

---

## Run 001 – Probe Layout

<img src="07_hv_sw_unit_run001_probe_gds.png" width="80%" />

- Aggressive probe layout to expose dominant HV constraints

---

## Run 002 – Guard Strategy Change

<img src="08_hv_sw_unit_run002_guard_share.png" width="80%" />

- Per-cell guard ring → shared outer guard ring

---

## Run 003 – Poly Gate Trim

<img src="09_hv_sw_unit_run003_poly_trim_gds.png" width="80%" />

- Poly gate end isolation study  
- Guard ring no longer pitch-dominant

---

## Run 004 – X-Direction Tiling Evaluation

<img src="10_hv_sw_unit_run004_x_tiling_eval_gds.png" width="80%" />

- X-tiling evaluation based on Run 003

<img src="11_hv_sw_unit_run004_x_tiling_eval_16um_gds.png" width="80%" />

- 16 µm pitch confirmed geometrically feasible (marginal)

---

## Run 005 – Metal1 Stub Trim (Pitch Sweep)

<img src="12_hv_sw_unit_run005_m1_stub_trim_16um_gds.png" width="80%" />

- Metal1 stub trim, 16 µm pitch

<img src="13_hv_sw_unit_run005_m1_stub_trim_12um_gds.png" width="80%" />

- Metal1 stub trim, 12 µm pitch

<img src="14_hv_sw_unit_run005_m1_stub_trim_14um.gds.png" width="80%" />

- Metal1 stub trim, 14 µm pitch

---

## Notes

- All images are **direct screenshots from KLayout**
- No DRC/LVS deck was applied (layout-first exploration)
- Image order matches **RUNNING_LOG.md** progression
- This index is **purely visual** and contains no design intent beyond what is logged

---

End of document.
