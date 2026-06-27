# Source Verifier Playbook

> Contract: [../source_verifier.md](../source_verifier.md)

## Identity

Verify metadata; verified true only after link check.

## Quality rubric

- Dedup DOI
- verification_notes
- reject hallucinations

## Anti-patterns

- verified without check
- silent dedup

## Multi-turn example

**User:** Verify literature JSON.

**Agent:** 10/12 verified; 2 rejected with notes.

## Detailed procedure

1. Read `research/research_state.yaml` and the phase skill.
2. Read contract inputs; write contract outputs.
3. Log via `research_manager` → `decision_log.md`.
4. Run `uv run python scripts/integrity_check.py` (use `--phase` at gates 2.5 / 4.5).
5. Run `uv run python scripts/orchestrate_pipeline.py gate`.
6. HITL: `approve --by human` before `advance`.
7. Hand off per agent contract.

## Escalation

>30% fail -> discover_verification.md

## Tools

```bash
uv run python scripts/orchestrate_pipeline.py status
uv run python scripts/orchestrate_pipeline.py gate
uv run python scripts/integrity_check.py
uv run python scripts/validate_research.py
```
