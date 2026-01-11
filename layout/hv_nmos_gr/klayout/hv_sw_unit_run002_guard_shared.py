# hv_sw_unit_run002_guard_shared.py
# Run 002: Guard strategy split
# Goal: remove per-cell guard ring, use shared outer guard for a 2-cell X-tiling probe

import pya

# ----------------------------
# Layout setup
# ----------------------------
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm
top = layout.create_cell("HV_SW_UNIT_RUN002_TOP")

# ----------------------------
# Layer definitions (same rough set as Run 001)
# ----------------------------
L_ACTIVE = layout.layer(65, 20)
L_POLY   = layout.layer(30, 0)
L_NPLUS  = layout.layer(66, 44)
L_PPLUS  = layout.layer(67, 44)
L_MET1   = layout.layer(68, 20)

# ----------------------------
# Geometry parameters (kept same intent as Run 001)
# ----------------------------
active_w = 6_000
active_h = 4_000

gate_l   = 1_000
gate_ext = 1_000

metal_stub = 500
sd_w = 1_200

# Tiling probe
pitch_x = 20_000  # 20 um hypothesis (same as Run 001)
n_cells = 2       # minimal tiling probe

# Shared outer guard parameters (this is the knob)
outer_guard_margin = 3_000  # intentionally moderate; tune later

# ----------------------------
# Unit cell (NO per-cell guard)
# ----------------------------
unit = layout.create_cell("HV_SW_UNIT_RUN002_UNIT")

# Active
unit.shapes(L_ACTIVE).insert(pya.Box(0, 0, active_w, active_h))

# N+ source / drain
unit.shapes(L_NPLUS).insert(pya.Box(0, 0, sd_w, active_h))
unit.shapes(L_NPLUS).insert(pya.Box(active_w - sd_w, 0, active_w, active_h))

# Poly gate (over-extended, same as Run 001)
unit.shapes(L_POLY).insert(
    pya.Box(
        active_w // 2 - gate_l // 2,
        -gate_ext,
        active_w // 2 + gate_l // 2,
        active_h + gate_ext
    )
)

# Metal1 stubs (kept to test edge interaction)
unit.shapes(L_MET1).insert(
    pya.Box(-metal_stub, active_h // 2 - metal_stub,
            metal_stub, active_h // 2 + metal_stub)
)
unit.shapes(L_MET1).insert(
    pya.Box(active_w - metal_stub, active_h // 2 - metal_stub,
            active_w + metal_stub, active_h // 2 + metal_stub)
)

# ----------------------------
# Place 2 units in X (tiling probe)
# ----------------------------
for i in range(n_cells):
    t = pya.Trans(pya.Point(i * pitch_x, 0))
    top.insert(pya.CellInstArray(unit.cell_index(), t))

# ----------------------------
# Shared outer guard around the whole 2-cell block
# ----------------------------
block_w = (n_cells - 1) * pitch_x + active_w
block_h = active_h

guard_box = pya.Box(
    -outer_guard_margin,
    -outer_guard_margin,
    block_w + outer_guard_margin,
    block_h + outer_guard_margin
)
top.shapes(L_PPLUS).insert(guard_box)

# ----------------------------
# Write GDS (ABSOLUTE PATH)
# ----------------------------
gds_path = r"C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run002_guard_shared.gds"
layout.write(gds_path)

print(f"Run 002 GDS generated: {gds_path}")
print(f"Probe: {n_cells} cells, pitch_x = {pitch_x/1000:.3f} um, shared outer guard only.")
