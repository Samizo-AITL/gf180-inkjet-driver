# Execution Logs

This directory contains **execution records**, not design documents.

The files under `logs/` record **what was actually done, observed, and decided**
during layout-first exploration and implementation phases.

---

## What These Logs Are

- Chronological records of **executed actions**
- Explicit documentation of **observations and decisions**
- A **single source of truth** for historical facts

Failures, dead ends, and abandoned paths are considered **valid results**  
and are intentionally preserved.

---

## What These Logs Are NOT

- Design specifications
- Architecture definitions
- Tutorials or explanatory material
- Optimized or cleaned summaries

If a constraint or decision is finalized, it is promoted to
`docs/architecture/`, **not kept here**.

---

## Directory Structure

- `30_runs/`
  - Contains the **primary exploration-phase running log**
  - Includes `RUNNING_LOG.md` as the authoritative record

Additional log directories may be added **only** for new phases
(e.g., implementation or integration),
without modifying existing logs.

---

## Modification Rules

- Existing log entries must **not** be rewritten or deleted
- Corrections or changes require **new entries**, not edits
- Log files are append-only by intent

---

## Relationship to Other Documentation

- Final architectural decisions → `docs/architecture/`
- Reusable design knowledge → `docs/unit/`
- Process and layout constraints → `docs/rules/`

This separation is intentional and enforced.

---

**End of logs/README.md**

