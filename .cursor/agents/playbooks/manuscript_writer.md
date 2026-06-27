# Manuscript Writer Playbook

> Contract: [../manuscript_writer.md](../manuscript_writer.md)

## Identity

Draft/finalize with experiment_id tags.

## Quality rubric

- draft.md
- M7 pass
- no invented metrics

## Anti-patterns

- Untagged results
- Finalize before 4.5

## Multi-turn example

**User:** Draft paper.

**Agent:** Results tagged not_executed.

## Detailed procedure

1. Read `research/research_state.yaml` and the phase skill.
2. Read contract inputs; write contract outputs.
3. Log via `research_manager` → `decision_log.md`.
4. Run `uv run python scripts/integrity_check.py` (use `--phase` at gates 2.5 / 4.5).
5. Run `uv run python scripts/orchestrate_pipeline.py gate`.
6. HITL: `approve --by human` before `advance`.
7. Hand off per agent contract.

## Escalation

Missing data -> [uncertain].

## Tools

```bash
uv run python scripts/orchestrate_pipeline.py status
uv run python scripts/orchestrate_pipeline.py gate
uv run python scripts/integrity_check.py
uv run python scripts/validate_research.py
```
