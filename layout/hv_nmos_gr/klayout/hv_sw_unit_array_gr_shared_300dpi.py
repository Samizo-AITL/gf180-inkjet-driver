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
    # Build unit & array (GR shared)
    # ==================================================
    unit = build_hv_sw_unit_no_gr(
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
    # ==================================================
    out = os.path.join(
        os.path.expanduser("~"),
        "KLayout",
        "hv_sw_unit_array_gr_shared_300dpi.gds",
    )

    os.makedirs(os.path.dirname(out), exist_ok=True)
    layout.write(out)
    print("GDS written to:", out)
