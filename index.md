---
title: "gf180-inkjet-driver"
description: "Minimal inkjet printhead driver IC exploration"
---

# gf180-inkjet-driver

Minimal inkjet printhead driver IC exploration using the **GF180MCU open PDK**,  
with a focus on **high-voltage device layout** and **mixed-signal integration**.

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/gf180-inkjet-driver/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/gf180-inkjet-driver/tree/main) |

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back%20to%20Samizo--AITL%20Portal-brightgreen)](https://samizo-aitl.github.io)

---

## Overview

This repository explores a **minimal inkjet printhead driver IC architecture**
implemented on the **GF180MCU open PDK**.

The primary goals are:

- Understanding **high-voltage device usage** in GF180
- Investigating **layout strategies** for HV + logic coexistence
- Studying **mixed-signal partitioning** suitable for inkjet drive circuits
- Building a reusable reference for future printhead / actuator drivers

This is **not a production-ready design**, but a technical exploration and
educational reference.

---

## Target Process

- **Process**: GF180MCU (Open PDK)
- **Voltage Domains**:
  - Low-voltage logic (core / IO)
  - High-voltage devices for inkjet actuation
- **Design Style**:
  - Mixed-signal
  - Layout-driven learning
  - Minimal functional blocks

---

## Scope of Exploration

- High-voltage MOS device selection and constraints
- Level-shift and isolation concepts
- Simple driver stage topologies
- Layout considerations:
  - Spacing rules
  - Guard rings
  - Substrate noise awareness
- Mixed-signal floorplanning concepts

---

## Repository Structure (planned)

```
gf180-inkjet-driver/
├── docs/        # Architecture notes, diagrams, design rationale
├── schematics/  # Schematic-level explorations
├── layout/      # Layout experiments (HV focus)
├── sim/         # Basic simulation setups
└── README.md
```

(Structure may evolve as the exploration progresses.)

---

## Motivation

Inkjet printhead drivers sit at the intersection of:

- High-voltage analog devices
- Digital control logic
- Tight layout and reliability constraints

GF180MCU provides a rare opportunity to study this **using an open PDK**.
This repository serves as a sandbox for that purpose.

---

## Status

- 🚧 Early exploration phase
- 📐 Layout-centric learning
- 🧪 Experiments may be incomplete or schematic-only

---

## Disclaimer

This project is provided **for educational and exploratory purposes only**.
No guarantees are made regarding manufacturability, reliability, or fitness
for any commercial application.

---


## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>PrecisionCore printhead productization, BOM management, ISO training |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/gf180-inkjet-driver//#-license)

| 📌 Item | License | Description |
|--------|---------|-------------|
| **Source Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text Materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required; share-alike applies for BY-SA |
| **Figures & Diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External References** | Follow the original license | Cite the original source properly |

---

## 💬　Feedback

> Suggestions, improvements, and discussions are welcome via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/gf180-inkjet-driver/discussions)
