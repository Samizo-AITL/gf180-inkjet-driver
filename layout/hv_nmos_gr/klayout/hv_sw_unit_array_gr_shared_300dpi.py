def main():

    # ==================================================
    # 300 dpi configuration
    # ==================================================
    n_col = 2
    n_row = 4

    # 300 dpi ≒ 84.7 um → margin込みで 85.0 um
    pitch_x = um(85.0, layout.dbu)
    pitch_y = um(85.0, layout.dbu)

    # ==================================================
    # Build unit & array
    # ※ 400dpi と同一レイヤ構成にする
    # ==================================================
    unit = build_hv_sw_unit(
        layout,
        "HV_SW_UNIT",
    )

    build_top_gr_shared(
        layout,
        unit,
        P,
        n_col,
        n_row,
        pitch_x,
        pitch_y,
    )

    # ==================================================
    # Write GDS
    # ※ 400dpi と同じファイル名で上書き
    # ==================================================
    out = os.path.join(
        os.path.expanduser("~"),
        "KLayout",
        "hv_sw_unit_array_gr_shared.gds",
    )

    os.makedirs(os.path.dirname(out), exist_ok=True)
    layout.write(out)
    print("GDS overwritten:", out)
