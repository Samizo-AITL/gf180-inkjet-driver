---
title: "gf180-inkjet-driver"
description: "Minimal inkjet printhead driver IC exploration"
---

# 🧠 gf180-inkjet-driver

[![Back to Portal (EN)](https://img.shields.io/badge/Back%20to%20Portal-0B5FFF?style=for-the-badge&logo=homeassistant&logoColor=white)](https://samizo-aitl.github.io/portal/en/)

Minimal inkjet printhead driver IC exploration using the  
**GF180MCU open PDK**, with a focus on:

- ⚡ **high-voltage device layout**
- 🧩 **mixed-signal integration**

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/gf180-inkjet-driver/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/gf180-inkjet-driver/tree/main) |

---

## 📘 Design Documentation

The core technical documentation for this project lives under the **docs/**
directory and is published via **GitHub Pages**.

- 🌐 **GitHub Pages (rendered docs)**  
  👉 [**Design Documentation (GitHub Pages)**](https://samizo-aitl.github.io/gf180-inkjet-driver/docs/)

- 📂 **docs/** *(design rationale, architecture, HV layout notes)*  
  👉 [**GitHub Repository – docs/**](https://github.com/Samizo-AITL/gf180-inkjet-driver/tree/main/docs)

All layout- and GDS-oriented discussions are intentionally centralized there.

---

## 🧭 Overview

This repository explores a **minimal inkjet printhead driver IC architecture**
implemented on the **GF180MCU open PDK**.

Primary goals:

- ⚡ Understanding **high-voltage device usage** in GF180  
- 📐 Investigating **layout strategies** for HV + logic coexistence  
- 🔀 Studying **mixed-signal partitioning** for inkjet drivers  
- 🧱 Building a reusable **architectural reference**

This is **not a production-ready design**,  
but a technical exploration and educational reference.

---

## 🧪 Target Process

- **Process**: GF180MCU (Open PDK)
- **Voltage Domains**:
  - Low-voltage logic (core / IO)
  - High-voltage devices for inkjet actuation
- **Design Style**:
  - Mixed-signal
  - Layout-driven learning
  - Minimal functional blocks

---

## 🔍 Scope of Exploration

- High-voltage MOS device selection and constraints  
- Level-shift and isolation concepts  
- Simple driver stage topologies  
- Layout considerations:
  - Spacing rules  
  - Guard rings  
  - Substrate noise awareness  
- Mixed-signal floorplanning concepts  

---

## 🎯 Motivation

Inkjet printhead drivers sit at the intersection of:

- ⚡ High-voltage analog devices  
- 🧠 Digital control logic  
- 📐 Tight layout and reliability constraints  

GF180MCU provides a rare opportunity to study this  
**using a fully open PDK**.

This repository serves as a **sandbox** for that purpose.

---

## 🚧 Status

- ✅ **Flow feasibility evaluation completed**
- 📐 **Manual layout exploration phase (HV-focused)**
- 🧩 **GDS targets identified (device- and structure-level)**

This project has completed evaluation of automated digital flows  
and has transitioned to **layout-centric exploration**.

No attempt is made to converge toward a production-ready IC.  
The outcome is the **identification of feasible and infeasible
design regions at the GDS level**.

---

## ✅ Results & Findings

This project **did not fail**.

It successfully identified the **practical design boundary** between:

- automated digital P&R flows, and  
- **manual mixed-signal / high-voltage IC design**

using the GF180MCU open PDK.

### 1️⃣ Automated Digital Flow Evaluation

- ❌ GF180MCU Open PDK is **not compatible** with OpenLane’s OpenPDK flow  
- Fully automated synthesis → P&R → GDS  
  **is not a viable approach** for this process

### 2️⃣ Architectural Implications for Inkjet Driver ICs

Inkjet printhead drivers inherently require:

- High-voltage device utilization  
- Mixed-signal integration (logic + HV analog)  
- Layout-driven decision making  

These characteristics place such designs **outside the effective scope**
of fully automated digital flows.

### 3️⃣ Domains Where GF180MCU Is Effective

- Manual / semi-manual layout exploration  
- High-voltage device and isolation studies  
- Mixed-signal floorplanning  
- Educational and architectural research  

---

### 🧱 Representative GDS Artifact

The following image shows a **representative high-voltage switch unit GDS**
generated during this exploration.

It demonstrates:

- DNWELL isolation  
- Continuous P+ guard ring  
- Central HV device structure  
- Explicit D / G / S / B pin exposure  

<img
  src="https://samizo-aitl.github.io/gf180-inkjet-driver/docs/images/02_hv_sw_unit_gds.png"
  alt="HV_SW_UNIT – DNWELL and Guard Ring GDS"
  width="80%"
/>

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>Printhead productization, BOM management, ISO training |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-black?logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/gf180-inkjet-driver/#---license)

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
