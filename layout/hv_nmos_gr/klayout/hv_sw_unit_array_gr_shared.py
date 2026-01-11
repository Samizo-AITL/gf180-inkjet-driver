# hv_sw_unit_array_gr_shared.py
# KLayout (pya) macro
# - Generates HV_SW_UNIT placeholder
# - Generates two TOP cells:
#     1) TOP_ISO: each unit has its own guard ring (baseline)
#     2) TOP_GR_SHARED_COL: guard ring is shared per column (concept)
# - Adds pitch guide lines on layer 99/0
#
# Output:
#   ~/KLayout/hv_sw_unit_array_gr_shared.gds
#
# Run:
#   KLayout -> Macro Development -> Load -> Run

import os
import pya


# ----------------------------
# Utility
# ----------------------------
def um(val_um: float, dbu: float) -> int:
    return int(round(val_um / dbu))


def rect(cell: pya.Cell, layer: pya.LayerIndex, x0: int, y0: int, x1: int, y1: int):
    cell.shapes(layer).insert(pya.Box(x0, y0, x1, y1))


def add_pitch_guides(cell: pya.Cell, layer: pya.LayerIndex,
                     n_col: int, n_row: int, pitch_x: int, pitch_y: int,
                     unit_w: int, unit_h: int, dbu: float):
    guide_w = um(0.2, dbu)
    # vertical lines
    for c in range(n_col + 1):
        x = c * pitch_x
        rect(cell, layer, x, 0, x + guide_w, (n_row - 1) * pitch_y + unit_h)
    # horizontal lines
    for r in range(n_row + 1):
        y = r * pitch_y
        rect(cell, layer, 0, y, (n_col - 1) * pitch_x + unit_w, y + guide_w)


# ----------------------------
# HV_SW_UNIT (placeholder)
# ----------------------------
def build_hv_sw_unit(ly: pya.Layout, name: str, p: dict) -> pya.Cell:
    dbu = ly.dbu

    # Placeholder layers
    L_DNW = ly.layer(p["L_DNW"][0], p["L_DNW"][1])
    L_GR  = ly.layer(p["L_GR"][0],  p["L_GR"][1])
    L_DEV = ly.layer(p["L_DEV"][0], p["L_DEV"][1])
    L_PIN = ly.layer(p["L_PIN"][0], p["L_PIN"][1])
    L_TXT = ly.layer(p["L_TXT"][0], p["L_TXT"][1])

    UNIT_W = um(p["UNIT_W_UM"], dbu)
    UNIT_H = um(p["UNIT_H_UM"], dbu)

    DNW_M  = um(p["DNW_MARGIN_UM"], dbu)
    GR_GAP = um(p["GR_GAP_UM"], dbu)
    GR_W   = um(p["GR_W_UM"], dbu)

    DEV_W  = um(p["DEV_W_UM"], dbu)
    DEV_H  = um(p["DEV_H_UM"], dbu)

    PIN_S  = um(p["PIN_SIZE_UM"], dbu)

    c = ly.create_cell(name)

    # DNWELL rectangle
    rect(c, L_DNW, DNW_M, DNW_M, UNIT_W - DNW_M, UNIT_H - DNW_M)

    # Guard ring as continuous ring (4 rectangles)
    ix0 = DNW_M + GR_GAP
    iy0 = DNW_M + GR_GAP
    ix1 = UNIT_W - DNW_M - GR_GAP
    iy1 = UNIT_H - DNW_M - GR_GAP

    ox0 = ix0 - GR_W
    oy0 = iy0 - GR_W
    ox1 = ix1 + GR_W
    oy1 = iy1 + GR_W

    rect(c, L_GR, ox0, oy0, ox1, iy0)  # bottom
    rect(c, L_GR, ox0, iy1, ox1, oy1)  # top
    rect(c, L_GR, ox0, iy0, ix0, iy1)  # left
    rect(c, L_GR, ix1, iy0, ox1, iy1)  # right

    # Device placeholder
    cx = UNIT_W // 2
    cy = UNIT_H // 2
    rect(c, L_DEV, cx - DEV_W // 2, cy - DEV_H // 2, cx + DEV_W // 2, cy + DEV_H // 2)

    # Pin markers (D/G/S/B)
    pins = {
        "D": (cx, UNIT_H - DNW_M - PIN_S * 2),
        "S": (cx, DNW_M + PIN_S),
        "G": (UNIT_W - DNW_M - PIN_S * 2, cy),
        "B": (DNW_M + PIN_S, cy),
    }
    for name, (px, py) in pins.items():
        rect(c, L_PIN, px - PIN_S // 2, py - PIN_S // 2, px + PIN_S // 2, py + PIN_S // 2)
        c.shapes(L_TXT).insert(pya.Text(name, pya.Trans(px + PIN_S, py + PIN_S)))

    return c


# ----------------------------
# TOP builders
# ----------------------------
def build_top_iso(ly: pya.Layout, top_name: str, unit_cell: pya.Cell,
                  n_col: int, n_row: int, pitch_x: int, pitch_y: int) -> pya.Cell:
    top = ly.create_cell(top_name)
    for r in range(n_row):
        for c in range(n_col):
            dx = c * pitch_x
            dy = r * pitch_y
            top.insert(pya.CellInstArray(unit_cell.cell_index(), pya.Trans(pya.Point(dx, dy))))
    return top


def build_top_gr_shared_by_column(ly: pya.Layout, top_name: str, unit_cell: pya.Cell,
                                  n_col: int, n_row: int, pitch_x: int, pitch_y: int,
                                  unit_w: int, unit_h: int,
                                  gr_layer: pya.LayerIndex,
                                  dnw_margin: int, gr_gap: int, gr_w: int) -> pya.Cell:
    """
    Concept:
      - Place the units as-is (still contains GR in unit cell)
      - Additionally draw ONE guard ring per column on TOP (shared GR)
      - In real implementation you'd remove GR from unit or make it optional.
        Here we keep unit GR and "overlay" shared GR to visualize footprint savings conceptually.
    """
    top = ly.create_cell(top_name)

    # 1) Place instances
    for r in range(n_row):
        for c in range(n_col):
            dx = c * pitch_x
            dy = r * pitch_y
            top.insert(pya.CellInstArray(unit_cell.cell_index(), pya.Trans(pya.Point(dx, dy))))

    # 2) Draw shared GR per column (outer ring around the whole column stack)
    # Column bounding box in local TOP coordinates:
    col_h = (n_row - 1) * pitch_y + unit_h
    for c in range(n_col):
        x0 = c * pitch_x
        y0 = 0
        x1 = x0 + unit_w
        y1 = y0 + col_h

        # Mirror the same "DNW + gap + GR" logic but at column scale.
        # We only draw GR here (DNW sharing is NOT done).
        # Inner ring reference based on "unit" DNW margin and GR gap, expanded to column bbox.
        ix0 = x0 + dnw_margin + gr_gap
        iy0 = y0 + dnw_margin + gr_gap
        ix1 = x1 - dnw_margin - gr_gap
        iy1 = y1 - dnw_margin - gr_gap

        ox0 = ix0 - gr_w
        oy0 = iy0 - gr_w
        ox1 = ix1 + gr_w
        oy1 = iy1 + gr_w

        # Guard ring rectangles
        rect(top, gr_layer, ox0, oy0, ox1, iy0)  # bottom
        rect(top, gr_layer, ox0, iy1, ox1, oy1)  # top
        rect(top, gr_layer, ox0, iy0, ix0, iy1)  # left
        rect(top, gr_layer, ix1, iy0, ox1, iy1)  # right

    return top


# ----------------------------
# Main
# ----------------------------
def main():
    ly = pya.Layout()
    ly.dbu = 0.001  # 1 nm

    dbu = ly.dbu

    # Parameters (micron)
    P = {
        "UNIT_W_UM": 80.0,
        "UNIT_H_UM": 80.0,
        "DNW_MARGIN_UM": 4.0,
        "GR_GAP_UM": 2.0,
        "GR_W_UM": 3.0,
        "DEV_W_UM": 20.0,
        "DEV_H_UM": 30.0,
        "PIN_SIZE_UM": 2.0,

        # layer/datatype
        "L_DNW": (10, 0),
        "L_GR":  (20, 0),
        "L_DEV": (30, 0),
        "L_PIN": (40, 0),
        "L_TXT": (41, 0),
        "L_GUIDE": (99, 0),
    }

    # Array setup
    N_COL = 2
    N_ROW = 4
    PITCH_X_UM = 63.5   # 400 dpi
    PITCH_Y_UM = 85.0

    pitch_x = um(PITCH_X_UM, dbu)
    pitch_y = um(PITCH_Y_UM, dbu)

    unit_w = um(P["UNIT_W_UM"], dbu)
    unit_h = um(P["UNIT_H_UM"], dbu)

    dnw_margin = um(P["DNW_MARGIN_UM"], dbu)
    gr_gap     = um(P["GR_GAP_UM"], dbu)
    gr_w       = um(P["GR_W_UM"], dbu)

    L_GUIDE = ly.layer(P["L_GUIDE"][0], P["L_GUIDE"][1])
    L_GR    = ly.layer(P["L_GR"][0],    P["L_GR"][1])

    # Build unit
    unit = build_hv_sw_unit(ly, "HV_SW_UNIT", P)

    # Build tops
    top_iso = build_top_iso(ly, "TOP_ISO", unit, N_COL, N_ROW, pitch_x, pitch_y)
    add_pitch_guides(top_iso, L_GUIDE, N_COL, N_ROW, pitch_x, pitch_y, unit_w, unit_h, dbu)

    top_shared = build_top_gr_shared_by_column(
        ly, "TOP_GR_SHARED_COL", unit,
        N_COL, N_ROW, pitch_x, pitch_y,
        unit_w, unit_h,
        L_GR,
        dnw_margin, gr_gap, gr_w
    )
    add_pitch_guides(top_shared, L_GUIDE, N_COL, N_ROW, pitch_x, pitch_y, unit_w, unit_h, dbu)

    # Write GDS
    out_dir = os.path.join(os.path.expanduser("~"), "KLayout")
    os.makedirs(out_dir, exist_ok=True)
    out_gds = os.path.join(out_dir, "hv_sw_unit_array_gr_shared.gds")
    ly.write(out_gds)
    print("GDS written to:", out_gds)


if __name__ == "__main__":
    main()
