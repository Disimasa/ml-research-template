# Manuscript

Publication track artifacts (phases `write` → `finalize`).

| File | Purpose |
|------|---------|
| `draft.md` | Working manuscript (copy from `draft.template.md`) |
| `reviews.yaml` | R1–R3 reviews + editorial decision |
| `revision_log.md` | Socratic revision rounds |

Integrity **gate 2.5** (`integrity_pre_review`) and **gate 4.5** (`integrity_final`) run M1–M7 via:

```bash
uv run python scripts/orchestrate_pipeline.py gate
```
