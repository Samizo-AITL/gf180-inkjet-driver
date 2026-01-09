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
