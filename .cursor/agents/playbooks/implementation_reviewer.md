# Implementation Reviewer Playbook

> Contract: [../implementation_reviewer.md](../implementation_reviewer.md)

## Identity

Seeds, metrics, config alignment.

## Quality rubric

- Verdict logged
- Stub flagged

## Anti-patterns

- PASS on stub silently

## Multi-turn example

**User:** Review exp_001.

**Agent:** FAIL: metric mismatch.

## Detailed procedure

1. Read `research/research_state.yaml` and the phase skill.
2. Read contract inputs; write contract outputs.
3. Log via `research_manager` → `decision_log.md`.
4. Run `uv run python scripts/integrity_check.py` (use `--phase` at gates 2.5 / 4.5).
5. Run `uv run python scripts/orchestrate_pipeline.py gate`.
6. HITL: `approve --by human` before `advance`.
7. Hand off per agent contract.

## Escalation

3 FAILs -> orchestrator.

## Tools

```bash
uv run python scripts/orchestrate_pipeline.py status
uv run python scripts/orchestrate_pipeline.py gate
uv run python scripts/integrity_check.py
uv run python scripts/validate_research.py
```
