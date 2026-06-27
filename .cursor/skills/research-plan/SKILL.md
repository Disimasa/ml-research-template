---
name: research-plan
description: Plan phase — methodology, ethics review, and experiment intake declaration
---

# Research plan

**Phase:** `plan`  
**Agents:** `methodology_critic`, `devils_advocate`, `ethics_reviewer`

## When to use

- Phase `plan` enabled
- Before any `execute` work

## Prerequisites

- Selected hypothesis in `research/hypotheses.yaml` (`status: selected`)
- `research/passport.yaml`

## Steps

### 1. Write `research/methodology.md`

Sections (minimum):

1. **Research question** — from passport
2. **Hypothesis under test** — `hyp_00X`
3. **Data** — sources, splits, preprocessing (`data/` paths)
4. **Model / method** — maps to future `configs/model/`
5. **Baselines** — fair comparison rationale
6. **Metrics** — primary + secondary; align with `research_state.autonomous.metric_primary`
7. **Ablations** — planned variations
8. **Ethics & data** — licenses, PII (ethics reviewer fills gaps)

### 2. Experiment plan

For each experiment:

| experiment_id | config | purpose |
|---------------|--------|---------|
| exp_001 | configs/experiment/foo.yaml | main |

Create **config filename stubs only** if execute approved — do not implement training unless task is execute.

### 3. Devil's advocate (plan)

Challenge baselines, metric choice, sample size; log in `decision_log.md`.

### 4. Ethics reviewer checklist

- Data license OK
- No secrets in repo
- Primary metric pre-registered in methodology

### 5. Update passport

```yaml
experiment_intake_declaration: experiments_declared
planned_experiment_ids: [exp_001, ...]
phase: plan
```

### 6. Gate

- HITL: human approves methodology → `approved_by: human`
- Autonomous: proceed if ethics PASS and DA does not block

## Handoff

→ `run-experiment` (execute)
