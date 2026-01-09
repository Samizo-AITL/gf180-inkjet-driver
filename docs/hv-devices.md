# High-Voltage Devices in GF180MCU

## Purpose

Summarize considerations when using **high-voltage MOS devices**
available in the GF180MCU open PDK.

---

## Key Considerations

- Drain-to-source voltage limits
- Gate oxide reliability
- SOA (Safe Operating Area)
- Layout-driven constraints dominate performance

---

## Usage Philosophy

- Prefer simple, robust device stacking
- Avoid aggressive overdrive
- Let layout spacing define reliability margin

---

## Open Questions

- Optimal device selection for repetitive pulse stress
- Trade-offs between area and lifetime
- Substrate coupling impact in mixed-signal context
