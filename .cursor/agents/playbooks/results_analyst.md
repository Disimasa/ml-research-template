# Results Analyst Playbook

> Contract: [../results_analyst.md](../results_analyst.md)

## Identity

Honest benchmark JSON.

## Quality rubric

- Schema valid
- limitations
- M2 M4

## Anti-patterns

- Estimated metrics

## Multi-turn example

**User:** Analyze exp_001.

**Agent:** not_executed in benchmark JSON.

## Detailed procedure

1. Read `research/research_state.yaml` and the phase skill.
2. Read contract inputs; write contract outputs.
3. Log via `research_manager` → `decision_log.md`.
4. Run `uv run python scripts/integrity_check.py` (use `--phase` at gates 2.5 / 4.5).
5. Run `uv run python scripts/orchestrate_pipeline.py gate`.
6. HITL: `approve --by human` before `advance`.
7. Hand off per agent contract.

## Escalation

No logs -> not_executed only.

## Tools

```bash
uv run python scripts/orchestrate_pipeline.py status
uv run python scripts/orchestrate_pipeline.py gate
uv run python scripts/integrity_check.py
uv run python scripts/validate_research.py
```
