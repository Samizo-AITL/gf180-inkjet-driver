# hv_sw_unit_run001_probe.py
# Run 001 probe layout
# Purpose: identify dominant HV DRC constraints (FAIL expected)

import pya

# ----------------------------
# Layout setup
# ----------------------------
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm database unit
top = layout.create_cell("HV_SW_UNIT_RUN001_PROBE")

# ----------------------------
# Layer definitions (GF180 rough guess)
# ----------------------------
L_ACTIVE = layout.layer(65, 20)   # Active / diffusion
L_POLY   = layout.layer(30, 0)    # Poly gate
L_NPLUS  = layout.layer(66, 44)   # N+ implant
L_PPLUS  = layout.layer(67, 44)   # P+ implant (guard)
L_MET1   = layout.layer(68, 20)   # Metal1

# ----------------------------
# Aggressive parameters (on purpose)
# ----------------------------
active_w = 6_000   # nm
active_h = 4_000   # nm

gate_l   = 1_000   # nm
gate_ext = 1_000   # nm

guard_margin = 1_500   # nm (intentionally too small)
metal_stub   = 500     # nm

# ----------------------------
# Geometry
# ----------------------------

# Active (NMOS body)
top.shapes(L_ACTIVE).insert(
    pya.Box(0, 0, active_w, active_h)
)

# N+ source / drain
top.shapes(L_NPLUS).insert(
    pya.Box(0, 0, 1_200, active_h)
)
top.shapes(L_NPLUS).insert(
    pya.Box(active_w - 1_200, 0, active_w, active_h)
)

# Poly gate (intentionally over-extended)
top.shapes(L_POLY).insert(
    pya.Box(
        active_w // 2 - gate_l // 2,
        -gate_ext,
        active_w // 2 + gate_l // 2,
        active_h + gate_ext
    )
)

# P+ guard ring (too tight by design)
top.shapes(L_PPLUS).insert(
    pya.Box(
        -guard_margin,
        -guard_margin,
        active_w + guard_margin,
        active_h + guard_margin
    )
)

# Metal1 stubs (spacing bait)
top.shapes(L_MET1).insert(
    pya.Box(
        -metal_stub,
        active_h // 2 - metal_stub,
        metal_stub,
        active_h // 2 + metal_stub
    )
)
top.shapes(L_MET1).insert(
    pya.Box(
        active_w - metal_stub,
        active_h // 2 - metal_stub,
        active_w + metal_stub,
        active_h // 2 + metal_stub
    )
)

# ----------------------------
# Write GDS (ABSOLUTE PATH)
# ----------------------------
gds_path = r"C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run001_probe.gds"
layout.write(gds_path)

print(f"Run 001 probe GDS generated: {gds_path}")
