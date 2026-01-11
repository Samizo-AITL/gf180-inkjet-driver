# hv_sw_unit_array_gr_shared_clean.py
# KLayout (pya) macro
# CLEAN version:
# - HV_SW_UNIT has NO guard ring
# - Guard ring exists ONLY at TOP level (shared per column)
# - Purpose: determine if 400 dpi is saved purely by GR sharing

import os
import pya

# ----------------------------
# Utility
# ----------------------------
def um(val_um, dbu):
    return int(round(val_um / dbu))

def rect(cell, layer, x0, y0, x1, y1):
    cell.shapes(layer).insert(pya.Box(x0, y0, x1, y1))

def add_pitch_guides(cell, layer,
                     n_col, n_row, pitch_x, pitch_y,
                     unit_w, unit_h, dbu):
    guide_w = um(0.2, dbu)
    for c in range(n_col + 1):
        x = c * pitch_x
        rect(cell, layer, x, 0, x + guide_w,
             (n_row - 1) * pitch_y + unit_h)
    for r in range(n_row + 1):
        y = r * pitch_y
        rect(cell, layer, 0, y,
             (n_col - 1) * pitch_x + unit_w, y + guide_w)

# ----------------------------
# HV_SW_UNIT (NO GUARD RING)
# ----------------------------
def build_hv_sw_unit_no_gr(layout, name, P):
    dbu = layout.dbu

    L_DNW = layout.layer(P["L_DNW"][0], P["L_DNW"][1])
    L_DEV = layout.layer(P["L_DEV"][0], P["L_DEV"][1])
    L_PIN = layout.layer(P["L_PIN"][0], P["L_PIN"][1])
    L_TXT = layout.layer(P["L_TXT"][0], P["L_TXT"][1])

    UNIT_W = um(P["UNIT_W_UM"], dbu)
    UNIT_H = um(P["UNIT_H_UM"], dbu)

    DNW_M  = um(P["DNW_MARGIN_UM"], dbu)
    DEV_W  = um(P["DEV_W_UM"], dbu)
    DEV_H  = um(P["DEV_H_UM"], dbu)
    PIN_S  = um(P["PIN_SIZE_UM"], dbu)

    c = layout.create_cell(name)

    # DNWELL only (no GR)
    rect(c, L_DNW,
         DNW_M, DNW_M,
         UNIT_W - DNW_M, UNIT_H - DNW_M)

    # Device placeholder
    cx = UNIT_W // 2
    cy = UNIT_H // 2
    rect(c, L_DEV,
         cx - DEV_W // 2, cy - DEV_H // 2,
         cx + DEV_W // 2, cy + DEV_H // 2)

    # Pins
    pins = {
        "D": (cx, UNIT_H - DNW_M - PIN_S * 2),
        "S": (cx, DNW_M + PIN_S),
        "G": (UNIT_W - DNW_M - PIN_S * 2, cy),
        "B": (DNW_M + PIN_S, cy),
    }
    for k in pins:
        px, py = pins[k]
        rect(c, L_PIN,
             px - PIN_S // 2, py - PIN_S // 2,
             px + PIN_S // 2, py + PIN_S // 2)
        c.shapes(L_TXT).insert(
            pya.Text(k, pya.Trans(px + PIN_S, py + PIN_S))
        )

    return c

# ----------------------------
# TOP: GR shared by column
# ----------------------------
def build_top_gr_shared(layout, unit, P,
                        n_col, n_row, pitch_x, pitch_y):
    dbu = layout.dbu
    top = layout.create_cell("TOP_GR_SHARED_COL_CLEAN")

    unit_w = um(P["UNIT_W_UM"], dbu)
    unit_h = um(P["UNIT_H_UM"], dbu)

    dnw_m  = um(P["DNW_MARGIN_UM"], dbu)
    gr_gap = um(P["GR_GAP_UM"], dbu)
    gr_w   = um(P["GR_W_UM"], dbu)

    L_GR   = layout.layer(P["L_GR"][0],    P["L_GR"][1])
    L_GUID = layout.layer(P["L_GUIDE"][0], P["L_GUIDE"][1])

    # place units
    for r in range(n_row):
        for c in range(n_col):
            top.insert(
                pya.CellInstArray(
                    unit.cell_index(),
                    pya.Trans(pya.Point(c * pitch_x, r * pitch_y))
                )
            )

    # shared GR per column
    col_h = (n_row - 1) * pitch_y + unit_h
    for c in range(n_col):
        x0 = c * pitch_x
        x1 = x0 + unit_w

        ix0 = x0 + dnw_m + gr_gap
        ix1 = x1 - dnw_m - gr_gap
        iy0 = dnw_m + gr_gap
        iy1 = col_h - dnw_m - gr_gap

        ox0 = ix0 - gr_w
        oy0 = iy0 - gr_w
        ox1 = ix1 + gr_w
        oy1 = iy1 + gr_w

        rect(top, L_GR, ox0, oy0, ox1, iy0)
        rect(top, L_GR, ox0, iy1, ox1, oy1)
        rect(top, L_GR, ox0, iy0, ix0, iy1)
        rect(top, L_GR, ix1, iy0, ox1, iy1)

    add_pitch_guides(top, L_GUID,
                     n_col, n_row, pitch_x, pitch_y,
                     unit_w, unit_h, dbu)

    return top

# ----------------------------
# Main
# ----------------------------
def main():
    layout = pya.Layout()
    layout.dbu = 0.001

    P = {
        "UNIT_W_UM": 80.0,
        "UNIT_H_UM": 80.0,
        "DNW_MARGIN_UM": 4.0,
        "GR_GAP_UM": 2.0,
        "GR_W_UM": 3.0,
        "DEV_W_UM": 20.0,
        "DEV_H_UM": 30.0,
        "PIN_SIZE_UM": 2.0,
        "L_DNW": (10, 0),
        "L_GR":  (20, 0),
        "L_DEV": (30, 0),
        "L_PIN": (40, 0),
        "L_TXT": (41, 0),
        "L_GUIDE": (99, 0),
    }

    n_col = 2
    n_row = 4
    pitch_x = um(63.5, layout.dbu)   # 400 dpi
    pitch_y = um(85.0, layout.dbu)

    unit = build_hv_sw_unit_no_gr(layout, "HV_SW_UNIT_NO_GR", P)
    build_top_gr_shared(layout, unit, P,
                        n_col, n_row, pitch_x, pitch_y)

    out = os.path.join(
        os.path.expanduser("~"),
        "KLayout",
        "hv_sw_unit_array_gr_shared_clean.gds"
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    layout.write(out)
    print("GDS written to:", out)

if __name__ == "__main__":
    main()
