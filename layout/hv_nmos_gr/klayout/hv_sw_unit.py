# klayout_hv_sw_unit.py
# 実行方法: KLayout → Tools → Run Script

import pya

ly = pya.Layout()
ly.dbu = 0.001  # 1 nm grid

top = ly.create_cell("HV_SW_UNIT")

# === レイヤ定義（GF180想定：番号は例、PDKに合わせて調整）===
L_NDIFF  = ly.layer(65, 20)
L_PDIFF  = ly.layer(64, 20)
L_POLY   = ly.layer(66, 20)
L_MET1   = ly.layer(68, 20)
L_CONT   = ly.layer(67, 20)
L_DNWELL = ly.layer(12, 0)
L_NWELL  = ly.layer(64, 0)

# === 寸法（µm → dbu変換）===
def um(x): return int(x / ly.dbu)

W_UNIT = um(20.0)
H_UNIT = um(40.0)
GR_W   = um(2.0)
DN_OFF = um(3.0)

# === Guard Ring ===
outer = pya.Box(0, 0, W_UNIT, H_UNIT)
inner = pya.Box(GR_W, GR_W, W_UNIT-GR_W, H_UNIT-GR_W)
top.shapes(L_PDIFF).insert(outer)
top.shapes(L_PDIFF).insert(inner)

# === DNWELL ===
dn = pya.Box(-DN_OFF, -DN_OFF, W_UNIT+DN_OFF, H_UNIT+DN_OFF)
top.shapes(L_DNWELL).insert(dn)

# === HV nLDMOS（既存PDKセルを呼ぶ）===
# ★ここが唯一の差し替え点★
# 例: lib="gf180mcu", cell="nldmos_10v"
lib_name  = "gf180mcu"
cell_name = "nldmos_10v"   # ← PDKの実セル名に変更

if ly.has_cell(cell_name):
    hv = ly.cell(cell_name)
    trans = pya.Trans(pya.Point(um(10), um(10)))
    top.insert(pya.CellInstArray(hv.cell_index(), trans))
else:
    # 仮プレースホルダ（PDK未ロード時）
    top.shapes(L_NDIFF).insert(pya.Box(um(6), um(6), um(14), um(30)))
    top.shapes(L_POLY).insert(pya.Box(um(9), um(6), um(11), um(30)))

# === ピン（M1）===
def pin(box, name):
    top.shapes(L_MET1).insert(box)
    top.shapes(L_MET1).insert(pya.Text(name, box.center()))

pin(pya.Box(um(1), um(18), um(4), um(22)), "D")
pin(pya.Box(um(16), um(18), um(19), um(22)), "S")
pin(pya.Box(um(9), um(32), um(11), um(35)), "G")
pin(pya.Box(um(9), um(1),  um(11), um(4)),  "B")

# === 出力 ===
ly.write("hv_sw_unit.gds")
print("hv_sw_unit.gds generated")
