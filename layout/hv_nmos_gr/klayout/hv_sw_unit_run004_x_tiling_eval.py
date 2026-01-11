# hv_sw_unit_run004_x_tiling_eval.py
#
# RUN004:
#   X-direction tiling + pitch measurement
#
#   - Base cell: HV_SW_UNIT_RUN003 (geometry fixed)
#   - Single-knob: placement only (arrayability evaluation)
#   - No geometry modification inside unit cell
#
# Output:
#   - GDS with X-tiled cells
#   - Console report of measured pitch
#
# DBU = 1 nm
#

import pya
import os

# ------------------------------------------------------------
# User parameters (SAFE TO EDIT)
# ------------------------------------------------------------
N_TILES = 5           # number of units in X
TARGET_PITCH = 20.0  # um, initial guess for tiling
MARGIN_X = 0.0        # um, extra margin if needed

# ------------------------------------------------------------
# Fixed paths (Run 003 is the baseline)
# ------------------------------------------------------------
BASE_GDS = r"C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run003_poly_trim.gds"
OUT_GDS  = r"C:\Users\Lenovo\KLayout\macros\hv_sw_unit_run004_x_tiling_eval.gds"

BASE_CELL_NAME = "HV_SW_UNIT_RUN003"
TOP_CELL_NAME  = "HV_SW_UNIT_RUN004_XTILE"

# ------------------------------------------------------------
# Load Run003 GDS
# ------------------------------------------------------------
layout = pya.Layout()
layout.read(BASE_GDS)

layout.dbu = 0.001  # 1 nm

base_cell = layout.cell(BASE_CELL_NAME)
if base_cell is None:
    raise RuntimeError("Base cell not found: " + BASE_CELL_NAME)

top = layout.create_cell(TOP_CELL_NAME)

# ------------------------------------------------------------
# Measure base cell bounding box
# ------------------------------------------------------------
bbox = base_cell.bbox()
cell_width_um  = bbox.width()  * layout.dbu
cell_height_um = bbox.height() * layout.dbu

print("=== RUN004 BASE CELL METRICS ===")
print("Base cell width  (X): {:.3f} um".format(cell_width_um))
print("Base cell height (Y): {:.3f} um".format(cell_height_um))

# ------------------------------------------------------------
# Determine pitch (manual + measured hybrid)
# ------------------------------------------------------------
pitch_um = max(TARGET_PITCH, cell_width_um) + MARGIN_X
pitch_dbu = int(pitch_um / layout.dbu)

print("Requested pitch     : {:.3f} um".format(TARGET_PITCH))
print("Effective pitch used: {:.3f} um".format(pitch_um))

# ------------------------------------------------------------
# Place tiled instances
# ------------------------------------------------------------
for i in range(N_TILES):
    dx = i * pitch_dbu
    trans = pya.Trans(dx, 0)
    top.insert(pya.CellInstArray(base_cell.cell_index(), trans))

# ------------------------------------------------------------
# Post-placement pitch verification
# ------------------------------------------------------------
inst_bboxes = []
for inst in top.each_inst():
    bb = inst.bbox()
    inst_bboxes.append(bb)

measured_pitches = []
for i in range(1, len(inst_bboxes)):
    prev = inst_bboxes[i-1]
    curr = inst_bboxes[i]
    dx_um = (curr.left - prev.left) * layout.dbu
    measured_pitches.append(dx_um)

print("\n=== RUN004 MEASURED PITCHES ===")
for i, p in enumerate(measured_pitches):
    print("Pitch [{}→{}]: {:.3f} um".format(i, i+1, p))

if measured_pitches:
    print("Min pitch: {:.3f} um".format(min(measured_pitches)))
    print("Max pitch: {:.3f} um".format(max(measured_pitches)))

# ------------------------------------------------------------
# Write output GDS
# ------------------------------------------------------------
layout.write(OUT_GDS)

print("\nRUN004 GDS generated:")
print(OUT_GDS)
print("CWD =", os.getcwd())
