# hv_sw_unit_run003_poly_trim.py
#
# RUN003:
#   Single-knob experiment: Poly gate end treatment isolation
#   - Guard strategy: SAME as Run002
#   - Active / Metal topology: SAME
#   - Only poly gate end over-extension is reduced
#
# Canonical macro location:
#   C:\Users\Lenovo\KLayout\macros\
#
# Output GDS (FIXED, ABSOLUTE PATH):
#   C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run003_poly_trim.gds
#
# DBU = 1 nm
#

import pya
import os

# ------------------------------------------------------------
# Layout / Cell setup
# ------------------------------------------------------------
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm

top = layout.create_cell("HV_SW_UNIT_RUN003")

# ------------------------------------------------------------
# Layer definitions (GF180 symbolic, manual)
# ------------------------------------------------------------
L_ACTIVE = layout.layer(pya.LayerInfo(65, 20))   # active
L_POLY   = layout.layer(pya.LayerInfo(66, 20))   # poly
L_CONT   = layout.layer(pya.LayerInfo(67, 20))   # contact
L_M1     = layout.layer(pya.LayerInfo(68, 20))   # metal1
L_PPLUS  = layout.layer(pya.LayerInfo(64, 44))   # p+ guard (shared, Run002 style)

# ------------------------------------------------------------
# Parameters (ONLY poly-end differs from Run002)
# ------------------------------------------------------------
W_ACTIVE = 4.0    # um
L_GATE   = 1.2    # um

POLY_OVERHANG_SRC = 0.8   # um (trimmed)
POLY_OVERHANG_DRN = 0.8

CELL_X = 20.0    # um (provisional)
CELL_Y = 30.0

# ------------------------------------------------------------
# Active region
# ------------------------------------------------------------
active_box = pya.Box(
    pya.Point(0, 0),
    pya.Point(int(W_ACTIVE * 1000), int(L_GATE * 1000))
)
top.shapes(L_ACTIVE).insert(active_box)

# ------------------------------------------------------------
# Poly gate (trimmed ends)
# ------------------------------------------------------------
poly_x0 = -POLY_OVERHANG_SRC
poly_x1 = W_ACTIVE + POLY_OVERHANG_DRN
poly_y0 = -0.6
poly_y1 = L_GATE + 0.6

poly_box = pya.Box(
    pya.Point(int(poly_x0 * 1000), int(poly_y0 * 1000)),
    pya.Point(int(poly_x1 * 1000), int(poly_y1 * 1000))
)
top.shapes(L_POLY).insert(poly_box)

# ------------------------------------------------------------
# Dummy Metal1 stub (INTENTIONALLY unchanged vs Run002)
# ------------------------------------------------------------
m1_stub = pya.Box(
    pya.Point(1_000, int(L_GATE * 1000 + 1_000)),
    pya.Point(3_000, int(L_GATE * 1000 + 3_000))
)
top.shapes(L_M1).insert(m1_stub)

# ------------------------------------------------------------
# Guard ring (shared / partial, same concept as Run002)
# ------------------------------------------------------------
guard_margin = 4.0  # um

guard_box = pya.Box(
    pya.Point(int(-guard_margin * 1000), int(-guard_margin * 1000)),
    pya.Point(
        int((W_ACTIVE + guard_margin) * 1000),
        int((L_GATE + guard_margin) * 1000)
    )
)
top.shapes(L_PPLUS).insert(guard_box)

# ------------------------------------------------------------
# Write GDS (ABSOLUTE PATH – SPEC OVERRIDE)
# ------------------------------------------------------------
out_gds = r"C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run003_poly_trim.gds"
layout.write(out_gds)

# ------------------------------------------------------------
# Console confirmation (hard evidence)
# ------------------------------------------------------------
print("RUN003 GDS generated:")
print(out_gds)
print("CWD =", os.getcwd())
