# RUNNING LOG (Production Phase)

This document records **actual design runs** conducted during the
production-oriented phase of the gf180-inkjet-driver project.

This is **not a design specification**.
This is a **decision and result log** for layout-first HV IC exploration.

---

## Scope and Intent

- Target object: **HV_SW_UNIT**
- Process: **GF180MCU Open PDK**
- Focus: **Layout-first, GDS-oriented design**
- Priority: **Physical robustness over performance optimization**

### Explicitly Out of Scope
- Circuit-level performance optimization
- Tape-out readiness
- Reliability qualification
- Commercial usability

---

## Global Objectives

- Establish a **physically valid HV_SW_UNIT layout**
- Confirm **DRC-safe structure** under GF180 rules
- Identify **layout-driven constraints** invisible in schematic-level design
- Accumulate reusable knowledge for future iterations

---

## Run Index

| Run ID | Target | Description | Status | Notes |
|------:|--------|-------------|--------|-------|
| 001 | HV_SW_UNIT | Initial layout trial | Planned | First production-style run |

---

## Result Form (Template)

This form must be filled for **every run**.

### Identification
- Run ID:
- Date:
- Designer:
- Tool (e.g. KLayout):

### Layout Conditions
- Device Type:
- Nominal Max HV (V):
- Target Pitch (µm):
- Guard Ring Structure (Yes / No / Partial):

### Verification Status
- DRC: PASS / FAIL / NOT CHECKED  
- LVS: PASS / FAIL / NOT PERFORMED  
- ERC / Other Checks:

### Observations
- Critical layout constraints:
- Unexpected rule interactions:
- Area-consuming structures:
- Reusability concerns:

### Decisions
- Accepted compromises:
- Rejected options:
- Rationale:

### Conclusion
- Is this layout **structurally acceptable**? (Yes / No)
- Can this unit be **arrayed** without modification? (Yes / No)
- Recommended next action:

---

## Notes

- Failure is an **expected outcome** in early runs.
- A failed run is still a **valid result** if documented.
- This log is the **authoritative timeline** of the project’s physical design activity.

---

End of document.
