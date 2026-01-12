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

- **Initial exploration is based on NMOS-centered HV devices.**  
  In GF180MCU, array-level feasibility is primarily constrained by
  **DNWELL enclosure, spacing, and guard-ring requirements** rather than
  intrinsic device characteristics.
  NMOS-based low-side configurations are therefore used as a
  conservative baseline for physical evaluation.

- Device and topology conclusions are derived from
  **array-level layout behavior** (DNWELL continuity, spacing propagation,
  guard-ring sharing), not from single-device schematic metrics.

---

## Open Questions

- Optimal device selection for repetitive pulse stress
- Trade-offs between area and lifetime
- Substrate coupling impact in mixed-signal context
