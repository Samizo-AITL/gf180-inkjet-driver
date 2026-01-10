# hv_sw_unit_400dpi.py
# GF180 HV nLDMOS switch unit @ 400 dpi (63.5 µm pitch)
# 実行: KLayout → Tools → Run Script

import pya

# === Layout init ===
ly = pya.Layout()
ly.dbu = 0.001  # 1 nm grid
top = ly.create_cell("HV_SW_UNIT_400DPI")

def um(x): return int(x / ly.dbu)

# === Fixed pitch (400 dpi) ===
PITCH_X = um(63.5)   # 横方向ピッチ固定
PITCH_Y = um(80.0)   # 縦は余裕を持たせる（後で詰める前提）

# === Layers (GF180想定：要PDK整合) ===
L_PDIFF  = ly.layer(64, 20)   # guard ring
L_NDIFF  = ly.layer(65, 20)
L_POLY   = ly.layer(66, 20)
L_CONT   = ly.layer(67, 20)
L_MET1   = ly.layer(68, 20)
L_DNWELL = ly.layer(12, 0)

# === Conservative HV parameters ===
GR_W   = um(2.0)    # guard ring width
DN_OFF = um(3.0)    # DNWELL enclosure margin

# === Unit bounding box (must fit in pitch) ===
W_UNIT = PITCH_X
H_UNIT = PITCH_Y

# === Guard Ring ===
outer = pya.Box(0, 0, W_UNIT, H_UNIT)
inner = pya.Box(GR_W, GR_W, W_UNIT-GR_W, H_UNIT-GR_W)
top.shapes(L_PDIFF).insert(outer)
top.shapes(L_PDIFF).insert(inner)

# === DNWELL ===
dn = pya.Box(-DN_OFF, -DN_OFF, W_UNIT+DN_OFF, H_UNIT+DN_OFF)
top.shapes(L_DNWELL).insert(dn)

# === HV nLDMOS (PDK cell instance) ===
# ★ 実セル名だけ必ず合わせる ★
lib_name  = "gf180mcu"
cell_name = "nldmos_10v"   # ← 実際のGF180 HV nLDMOS名に変更

cx = um(31.75)   # ピッチ中央
cy = um(40.0)

if ly.has_cell(cell_name):
    hv = ly.cell(cell_name)
    top.insert(pya.CellInstArray(
        hv.cell_index(),
        pya.Trans(pya.Point(cx, cy))
    ))
else:
    # PDK未ロード時のプレースホルダ
    top.shapes(L_NDIFF).insert(
        pya.Box(cx-um(5), cy-um(15), cx+um(5), cy+um(15))
    )
    top.shapes(L_POLY).insert(
        pya.Box(cx-um(1), cy-um(15), cx+um(1), cy+um(15))
    )

# === Pin helper ===
def pin(x1, y1, x2, y2, name):
    b = pya.Box(um(x1), um(y1), um(x2), um(y2))
    top.shapes(L_MET1).insert(b)
    top.shapes(L_MET1).insert(pya.Text(name, b.center()))

# === Pins (400 dpi 前提配置) ===
pin(2.0,  30.0, 5.0,  34.0, "D")   # 左：Drain
pin(58.5, 30.0, 61.5, 34.0, "S")   # 右：Source
pin(30.5, 70.0, 33.0, 73.0, "G")   # 上：Gate
pin(30.5, 2.0,  33.0, 5.0,  "B")   # 下：Body

# === Array sanity (横タイル確認用：コメントアウト可) ===
# nx = 3
# arr = pya.CellInstArray(
#     top.cell_index(),
#     pya.Trans(),
#     pya.Vector(PITCH_X, 0),
#     pya.Vector(0, PITCH_Y),
#     nx, 1
# )
# ly.top_cell().insert(arr)

# === Write GDS ===
ly.write("hv_sw_unit_400dpi.gds")
print("hv_sw_unit_400dpi.gds generated (pitch = 63.5 µm)")
