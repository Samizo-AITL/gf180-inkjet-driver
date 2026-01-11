# hv_sw_unit_run005_m1_stub_trim.py
#
# RUN005:
#   Single-knob experiment: Metal1 stub isolation
#   - Base cell: HV_SW_UNIT_RUN003 (unchanged)
#   - ONLY Metal1 stub geometry is modified
#   - X-direction tiling + pitch reporting
#
# Canonical location:
#   layout/hv_nmos_gr/klayout/
#
# DBU = 1 nm
#

import pya
import os

# ------------------------------------------------------------
# User parameters (single knob)
# ------------------------------------------------------------
N_TILES = 5                 # Number of cells in X
X_PITCH_UM = 16.0           # Test pitch (µm)
M1_STUB_HEIGHT_UM = 1.0     # <<< SINGLE KNOB (Run003 was ~2.0–3.0)

# ------------------------------------------------------------
# Layout setup
# ------------------------------------------------------------
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm

top = layout.create_cell("HV_SW_UNIT_RUN005_M1_TRIM")

# ------------------------------------------------------------
# Layer definitions (symbolic)
# ------------------------------------------------------------
L_ACTIVE = layout.layer(pya.LayerInfo(65, 20))
L_POLY   = layout.layer(pya.LayerInfo(66, 20))
L_CONT   = layout.layer(pya.LayerInfo(67, 20))
L_M1     = layout.layer(pya.LayerInfo(68, 20))
L_PPLUS  = layout.layer(pya.LayerInfo(64, 44))

# ------------------------------------------------------------
# Base cell geometry (copied from Run003, UNCHANGED)
# ------------------------------------------------------------
W_ACTIVE = 4.0
L_GATE   = 1.2

POLY_OVERHANG_SRC = 0.8
POLY_OVERHANG_DRN = 0.8

# Active
active_box = pya.Box(
    pya.Point(0, 0),
    pya.Point(int(W_ACTIVE * 1000), int(L_GATE * 1000))
)

# Poly
poly_box = pya.Box(
    pya.Point(int(-POLY_OVERHANG_SRC * 1000), int(-0.6 * 1000)),
    pya.Point(int((W_ACTIVE + POLY_OVERHANG_DRN) * 1000),
              int((L_GATE + 0.6) * 1000))
)

# Guard (shared concept preserved)
guard_margin = 4.0
guard_box = pya.Box(
    pya.Point(int(-guard_margin * 1000), int(-guard_margin * 1000)),
    pya.Point(int((W_ACTIVE + guard_margin) * 1000),
              int((L_GATE + guard_margin) * 1000))
)

# ------------------------------------------------------------
# Metal1 stub (THIS IS THE ONLY MODIFIED STRUCTURE)
# ------------------------------------------------------------
m1_stub_box = pya.Box(
    pya.Point(1_000, int(L_GATE * 1000 + 500)),
    pya.Point(3_000, int(L_GATE * 1000 + 500 + M1_STUB_HEIGHT_UM * 1000))
)

# ------------------------------------------------------------
# Build tiled array
# ------------------------------------------------------------
for i in range(N_TILES):
    dx = int(i * X_PITCH_UM * 1000)

    top.shapes(L_ACTIVE).insert(active_box.moved(dx, 0))
    top.shapes(L_POLY).insert(poly_box.moved(dx, 0))
    top.shapes(L_PPLUS).insert(guard_box.moved(dx, 0))
    top.shapes(L_M1).insert(m1_stub_box.moved(dx, 0))

# ------------------------------------------------------------
# Write GDS
# ------------------------------------------------------------
out_gds = f"hv_sw_unit_run005_m1_stub_trim_{int(X_PITCH_UM)}um.gds"
layout.write(out_gds)

# ------------------------------------------------------------
# Console report (hard evidence)
# ------------------------------------------------------------
print("RUN005 GDS generated:")
print("  File :", out_gds)
print("  Tiles:", N_TILES)
print("  Pitch:", X_PITCH_UM, "um")
print("  M1 stub height:", M1_STUB_HEIGHT_UM, "um")
print("  CWD:", os.getcwd())
