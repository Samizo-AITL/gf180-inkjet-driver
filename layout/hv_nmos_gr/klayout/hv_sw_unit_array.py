# hv_sw_unit_array.py
# KLayout (pya) macro/script
# Generates: HV_SW_UNIT (placeholder) + TOP array (2xN etc.)
#
# Usage (KLayout GUI):
#   Macro Development -> Load -> Run
#
# Usage (batch):
#   klayout -b -r hv_sw_unit_array.py

import os
import pya


# ----------------------------
# Unit helpers
# ----------------------------
def um_to_dbu(val_um: float, dbu: float) -> int:
    """Convert micron to integer database units."""
    return int(round(val_um / dbu))


def rect(box_layer: pya.LayerIndex, cell: pya.Cell, x0, y0, x1, y1):
    cell.shapes(box_layer).insert(pya.Box(x0, y0, x1, y1))


def text(text_layer: pya.LayerIndex, cell: pya.Cell, s: str, x, y, height_um: float, dbu: float):
    # KLayout text size is in database units-ish via Trans + TextSize; simplest: use pya.Text with magnification
    t = pya.Text(s, pya.Trans(pya.Point(x, y)))
    cell.shapes(text_layer).insert(t)
    # (Optional) If you want scalable text, replace with DText in micron space, but keep it simple for now.


# ----------------------------
# HV_SW_UNIT generator (placeholder)
# ----------------------------
def build_hv_sw_unit(ly: pya.Layout, cell_name: str, p: dict) -> pya.Cell:
    """
    Create HV_SW_UNIT cell:
      - DNWELL enclosure rectangle
      - P+ guard ring (continuous ring) as 4 rectangles
      - central device placeholder rectangle
      - D/G/S/B pin markers (small squares + labels)
    """
    dbu = ly.dbu

    # Layers (placeholder; you can remap later to GF180 layers)
    L_DNWELL = ly.layer(p.get("layer_dnw", 10), p.get("dt_dnw", 0))
    L_GR     = ly.layer(p.get("layer_gr", 20),  p.get("dt_gr", 0))
    L_DEV    = ly.layer(p.get("layer_dev", 30), p.get("dt_dev", 0))
    L_PIN    = ly.layer(p.get("layer_pin", 40), p.get("dt_pin", 0))
    L_TXT    = ly.layer(p.get("layer_txt", 41), p.get("dt_txt", 0))

    c = ly.create_cell(cell_name)

    # Parameters (micron)
    unit_w_um     = p.get("unit_w_um", 80.0)
    unit_h_um     = p.get("unit_h_um", 80.0)
    dnw_margin_um = p.get("dnw_margin_um", 4.0)

    gr_gap_um     = p.get("gr_gap_um", 2.0)    # gap between DNWELL edge and guard ring inner edge
    gr_w_um       = p.get("gr_w_um", 3.0)      # guard ring width

    dev_w_um      = p.get("dev_w_um", 20.0)
    dev_h_um      = p.get("dev_h_um", 30.0)

    pin_size_um   = p.get("pin_size_um", 2.0)

    # Convert to dbu ints
    unit_w = um_to_dbu(unit_w_um, dbu)
    unit_h = um_to_dbu(unit_h_um, dbu)

    dnw_m  = um_to_dbu(dnw_margin_um, dbu)
    gr_gap = um_to_dbu(gr_gap_um, dbu)
    gr_w   = um_to_dbu(gr_w_um, dbu)

    dev_w  = um_to_dbu(dev_w_um, dbu)
    dev_h  = um_to_dbu(dev_h_um, dbu)

    pin_s  = um_to_dbu(pin_size_um, dbu)

    # Coordinate system: (0,0) to (unit_w, unit_h)
    # DNWELL box (placeholder)
    dnw_x0 = dnw_m
    dnw_y0 = dnw_m
    dnw_x1 = unit_w - dnw_m
    dnw_y1 = unit_h - dnw_m
    rect(L_DNWELL, c, dnw_x0, dnw_y0, dnw_x1, dnw_y1)

    # Guard ring (continuous ring = 4 rectangles)
    # Inner edge is offset from DNWELL by gr_gap
    gr_in_x0 = dnw_x0 + gr_gap
    gr_in_y0 = dnw_y0 + gr_gap
    gr_in_x1 = dnw_x1 - gr_gap
    gr_in_y1 = dnw_y1 - gr_gap

    gr_out_x0 = gr_in_x0 - gr_w
    gr_out_y0 = gr_in_y0 - gr_w
    gr_out_x1 = gr_in_x1 + gr_w
    gr_out_y1 = gr_in_y1 + gr_w

    # bottom
    rect(L_GR, c, gr_out_x0, gr_out_y0, gr_out_x1, gr_in_y0)
    # top
    rect(L_GR, c, gr_out_x0, gr_in_y1, gr_out_x1, gr_out_y1)
    # left
    rect(L_GR, c, gr_out_x0, gr_in_y0, gr_in_x0, gr_in_y1)
    # right
    rect(L_GR, c, gr_in_x1, gr_in_y0, gr_out_x1, gr_in_y1)

    # Central device placeholder
    cx = unit_w // 2
    cy = unit_h // 2
    dev_x0 = cx - dev_w // 2
    dev_y0 = cy - dev_h // 2
    dev_x1 = cx + dev_w // 2
    dev_y1 = cy + dev_h // 2
    rect(L_DEV, c, dev_x0, dev_y0, dev_x1, dev_y1)

    # Pins (D/G/S/B) markers + labels (placeholder convention)
    # Convention:
    #   D: top center, G: right center, S: bottom center, B: left center
    pins = {
        "D": (cx - pin_s//2, unit_h - dnw_m - pin_s*2),
        "G": (unit_w - dnw_m - pin_s*2, cy - pin_s//2),
        "S": (cx - pin_s//2, dnw_m + pin_s),
        "B": (dnw_m + pin_s, cy - pin_s//2),
    }
    for name, (px, py) in pins.items():
        rect(L_PIN, c, px, py, px + pin_s, py + pin_s)
        text(L_TXT, c, name, px + pin_s, py + pin_s, 2.0, dbu)

    # Add cell outline marker (optional) on PIN layer
    if p.get("draw_bbox", True):
        rect(L_PIN, c, 0, 0, unit_w, um_to_dbu(0.2, dbu))  # small line bottom
        rect(L_PIN, c, 0, 0, um_to_dbu(0.2, dbu), unit_h)  # small line left

    return c


# ----------------------------
# Array builder
# ----------------------------
def build_array(ly: pya.Layout, top_name: str, unit_cell: pya.Cell, a: dict) -> pya.Cell:
    """
    Place unit_cell in a TOP cell in n_col x n_row array with pitch_x/y.
    """
    dbu = ly.dbu

    n_col = int(a.get("n_col", 2))
    n_row = int(a.get("n_row", 4))

    pitch_x_um = float(a.get("pitch_x_um", 85.0))
    pitch_y_um = float(a.get("pitch_y_um", 85.0))

    pitch_x = um_to_dbu(pitch_x_um, dbu)
    pitch_y = um_to_dbu(pitch_y_um, dbu)

    top = ly.create_cell(top_name)

    # Place instances
    for r in range(n_row):
        for c in range(n_col):
            dx = c * pitch_x
            dy = r * pitch_y
            top.insert(pya.CellInstArray(unit_cell.cell_index(), pya.Trans(pya.Point(dx, dy))))

    return top


# ----------------------------
# Main
# ----------------------------
def main():
    ly = pya.Layout()
    ly.dbu = 0.001  # 1 nm DBU (扱いやすい)

    # --- HV_SW_UNIT params ---
    unit_params = dict(
        unit_w_um=80.0,
        unit_h_um=80.0,
        dnw_margin_um=4.0,
        gr_gap_um=2.0,
        gr_w_um=3.0,
        dev_w_um=20.0,
        dev_h_um=30.0,
        pin_size_um=2.0,

        # placeholder layers (LAYER/DATATYPE)
        layer_dnw=10, dt_dnw=0,
        layer_gr=20,  dt_gr=0,
        layer_dev=30, dt_dev=0,
        layer_pin=40, dt_pin=0,
        layer_txt=41, dt_txt=0,
        draw_bbox=True,
    )

    # --- Array params ---
    # 400 dpi pitch is ~63.5 um. まずは「ピッチ線に当てる」ために pitch_x=63.5 を試す。
    array_params = dict(
        n_col=2,
        n_row=4,
        pitch_x_um=63.5,  # 400 dpi direction（ここで当たる場所をGDSで見る）
        pitch_y_um=85.0,  # ひとまず余裕を持たせる（後で詰める）
    )

    hv = build_hv_sw_unit(ly, "HV_SW_UNIT", unit_params)
    top = build_array(ly, "TOP_HV_SW_UNIT_ARRAY", hv, array_params)

    # Optional: Add pitch guide lines on a guide layer
    L_GUIDE = ly.layer(99, 0)
    dbu = ly.dbu
    pitch_x = um_to_dbu(array_params["pitch_x_um"], dbu)
    pitch_y = um_to_dbu(array_params["pitch_y_um"], dbu)
    n_col = int(array_params["n_col"])
    n_row = int(array_params["n_row"])
    unit_w = um_to_dbu(unit_params["unit_w_um"], dbu)
    unit_h = um_to_dbu(unit_params["unit_h_um"], dbu)

    # Vertical pitch lines
    for c in range(n_col + 1):
        x = c * pitch_x
        rect(L_GUIDE, top, x, 0, x + um_to_dbu(0.2, dbu), (n_row - 1) * pitch_y + unit_h)

    # Horizontal pitch lines
    for r in range(n_row + 1):
        y = r * pitch_y
        rect(L_GUIDE, top, 0, y, (n_col - 1) * pitch_x + unit_w, y + um_to_dbu(0.2, dbu))

    # Output path
    # KLayout macro default folder例: C:\Users\<user>\KLayout\
    out_dir = os.path.join(os.path.expanduser("~"), "KLayout")
    os.makedirs(out_dir, exist_ok=True)
    out_gds = os.path.join(out_dir, "hv_sw_unit_array.gds")

    ly.write(out_gds)
    print("Wrote:", out_gds)


if __name__ == "__main__":
    main()
