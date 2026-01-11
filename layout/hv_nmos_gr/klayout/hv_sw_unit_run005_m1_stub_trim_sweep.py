# hv_sw_unit_run005_m1_stub_trim_sweep.py
#
# RUN005 (FINAL):
#   Single-knob experiment: Metal1 stub isolation
#   - Base cell: HV_SW_UNIT_RUN003 (geometry equivalent)
#   - ONLY Metal1 stub height is modified
#   - X-direction tiling with pitch sweep
#   - GDS output is FORCED into KLayout/macros
#
# DBU = 1 nm
#

import pya
import os

# ------------------------------------------------------------
# USER SETTINGS (EDIT ONLY HERE)
# ------------------------------------------------------------
TILES = 5
PITCH_LIST_UM = [16.0, 14.0, 12.0]   # pitch sweep
M1_STUB_HEIGHT_UM = 1.0              # trimmed Metal1 stub height

# ------------------------------------------------------------
# FORCE OUTPUT DIRECTORY (KLayout/macros)
# ------------------------------------------------------------
MACRO_DIR = os.path.dirname(__file__)
os.chdir(MACRO_DIR)

# ------------------------------------------------------------
# Layout setup
# ------------------------------------------------------------
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm

top = layout.create_cell("HV_SW_UNIT_RUN005_M1_TRIM")

# ------------------------------------------------------------
# Layer definitions (GF180 symbolic)
# ------------------------------------------------------------
L_PPLUS  = layout.layer(pya.LayerInfo(64, 44))
L_ACTIVE = layout.layer(pya.LayerInfo(65, 20))
L_POLY   = layout.layer(pya.LayerInfo(66, 20))
L_M1     = layout.layer(pya.LayerInfo(68, 20))

# ------------------------------------------------------------
# Base geometry (RUN003 equivalent)
# ------------------------------------------------------------
W_ACTIVE = 4.0
L_GATE   = 1.2

POLY_OVERHANG = 0.8
GUARD_MARGIN  = 4.0

def draw_unit(cell, x_offset_um):
    dx = int(x_offset_um * 1000)

    # Active
    cell.shapes(L_ACTIVE).insert(
        pya.Box(
            dx,
            0,
            dx + int(W_ACTIVE * 1000),
            int(L_GATE * 1000)
        )
    )

    # Poly
    cell.shapes(L_POLY).insert(
        pya.Box(
            dx + int(-POLY_OVERHANG * 1000),
            int(-0.6 * 1000),
            dx + int((W_ACTIVE + POLY_OVERHANG) * 1000),
            int((L_GATE + 0.6) * 1000)
        )
    )

    # Metal1 stub (TRIMMED ONLY HERE)
    cell.shapes(L_M1).insert(
        pya.Box(
            dx + int(1.0 * 1000),
            int((L_GATE + 0.5) * 1000),
            dx + int(3.0 * 1000),
            int((L_GATE + 0.5 + M1_STUB_HEIGHT_UM) * 1000)
        )
    )

    # Guard (shared outer concept)
    cell.shapes(L_PPLUS).insert(
        pya.Box(
            dx + int(-GUARD_MARGIN * 1000),
            int(-GUARD_MARGIN * 1000),
            dx + int((W_ACTIVE + GUARD_MARGIN) * 1000),
            int((L_GATE + GUARD_MARGIN) * 1000)
        )
    )

# ------------------------------------------------------------
# Pitch sweep execution
# ------------------------------------------------------------
print("=== RUN005 Metal1 Stub Trim Pitch Sweep ===")
print("Output dir :", MACRO_DIR)
print("Tiles      :", TILES)
print("M1 stub ht :", M1_STUB_HEIGHT_UM, "um")
print("")

for pitch_um in PITCH_LIST_UM:
    top.clear()

    for i in range(TILES):
        draw_unit(top, i * pitch_um)

    out_gds = f"hv_sw_unit_run005_m1_stub_trim_{int(pitch_um)}um.gds"
    layout.write(out_gds)

    print("RUN005 GDS generated:")
    print("  File :", out_gds)
    print("  Pitch:", pitch_um, "um")
    print("")

print("CWD =", os.getcwd())
print("=== RUN005 sweep COMPLETE ===")
