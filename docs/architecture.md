# Architecture Overview

## Objective

Define a **minimal inkjet printhead driver IC architecture**
suitable for exploration on the **GF180MCU open PDK**.

The goal is to understand how **logic, level shifting, and high-voltage
driver stages** coexist on a single die.

---

## High-Level Block Concept

```
+-----------------------------+
|        Control Logic        |
|  (FSM / Timing Generator)   |
+-------------+---------------+
              |
              | LV signals
              v
+-------------+---------------+
|       Level Shifter          |
|   LV → HV domain crossing    |
+-------------+---------------+
              |
              | HV gate drive
              v
+-------------+---------------+
|     HV Driver Stage          |
|  (Inkjet actuator drive)    |
+-------------+---------------+
              |
              v
         Printhead Load
```

---

## Key Partitions

### 1. Low-Voltage Logic
- Finite state machine (FSM)
- Timing and pulse shaping
- IO control interface

### 2. Level Shifting
- Domain isolation
- Gate-oxide reliability awareness
- Minimal topology preferred

### 3. High-Voltage Driver
- Uses GF180 HV MOS devices
- Layout-dominant design
- Emphasis on spacing and guard structures

---

## Design Assumptions

- No closed-loop sensing (open-loop drive)
- Single-channel or few-channel focus
- Educational / exploratory scale

---

- **Baseline HV driver topology assumes an NMOS-centered low-side switch.**  
  This choice reflects a layout-first exploration strategy under
  GF180MCU **DNWELL and guard-ring constraints**, where substrate isolation
  dominates array pitch feasibility.

- **Array feasibility is evaluated using a minimal 4×2 HV switch block.**  
  This configuration is sufficient to expose DNWELL continuity,
  guard-ring sharing, and edge effects while approximating
  an infinite array in its central region.

- Architectural conclusions are drawn from **worst-case physical constraints**
  rather than schematic optimality.

