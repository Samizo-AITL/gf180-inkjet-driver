# HV Inverter 1ch Unit (300dpi)

This directory defines a single-channel HV CMOS inverter
designed to be tileable at 300dpi pitch.

## Purpose
- Minimal physical unit for inkjet driver array
- 300 units can be arrayed to form a complete driver block

## Pins
- VIN   : Logic input
- VOUT  : HV output
- VDDH  : High-voltage supply
- VSSH  : HV ground

## Layout Assumptions
- Guard ring is shared at array/top level
- This cell contains only active devices and local routing

## Arrayability
- Horizontal tiling: OK
- Vertical power rail alignment: fixed

