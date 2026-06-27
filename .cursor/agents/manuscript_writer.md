---
name: manuscript_writer
description: Write and finalize phases — manuscript draft from passport and provenance
---

# Manuscript Writer

**Phases:** `write`, `finalize` | **Skills:** `manuscript-draft`, `manuscript-finalize`

**Deep playbook:** [playbooks/manuscript_writer.md](playbooks/manuscript_writer.md)

## Role

Produce `research/manuscript/draft.md` from research state. Tag every experimental claim with `experiment_id`. No fabricated metrics.

## Reads / writes

| Read | Write |
|------|-------|
| `passport.yaml`, `methodology.md`, `reports/benchmarks/` | `manuscript/draft.md` |
| `experiment_provenance.yaml` | `passport.write_status` |

## Gates

- Before review: advance to `integrity_pre_review` (gate 2.5, M1–M7)
- Before finalize: `integrity_final` (gate 4.5)

## Handoff

→ `integrity_auditor` (2.5) → `editor_in_chief`
