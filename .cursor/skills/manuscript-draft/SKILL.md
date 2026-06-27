---
name: manuscript-draft
description: Write phase — build manuscript draft from research artifacts
---

# Manuscript draft

**Phase:** `write` | **Agent:** `manuscript_writer`

## Prerequisites

- `synthesize` complete; M1–M5 PASS on research track
- `passport.claims`, `methodology.md`, `reports/benchmarks/`

## Steps

1. Copy `research/manuscript/draft.template.md` → `draft.md`.
2. Fill sections from passport and methodology only.
3. Results: copy metrics from benchmark JSON; tag `<!-- experiment_id: exp_XXX -->`.
4. If no run: state `[not executed]` — do not invent numbers.
5. Set `passport.write_status: draft`.
6. `uv run python scripts/integrity_check.py --modes M7`.
7. HITL: human approves draft → advance to `integrity_pre_review`.

## Gate 2.5

At `integrity_pre_review`:

```bash
uv run python scripts/orchestrate_pipeline.py gate
# profile: gate_2_5_pre_review — M1–M7
```

## Handoff

→ `peer-review` after gate PASS + human ack
