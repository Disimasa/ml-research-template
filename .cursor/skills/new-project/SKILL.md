---
name: new-project
description: Bootstrap phase — initialize research state from setup.md into passport and pipeline config
---

# New project (bootstrap)

**Phase:** `bootstrap`  
**Agent:** `intake_agent`

## When to use

- Fresh fork of the template
- User says "start research", "new project", or completes `setup.md`
- Profile includes `bootstrap` phase

## Prerequisites

Read `setup.md`, `research/pipeline_profiles.yaml`, `shared/schemas/passport.schema.json`.

## Steps

1. **Collect inputs** (from user or `setup.md`):
   - Working title / research question
   - `mode`: `hitl` | `autonomous`
   - `pipeline_profile`: e.g. `hypothesis-only`, `full-hitl`, `full-autonomous`, `custom`
   - Primary metric, logger preference, DVC yes/no

2. **Resolve profile** in `research/pipeline_profiles.yaml`:
   - Copy `mode` and `phases` into `research/pipeline.yaml`
   - Set `phases_enabled` in `research/research_state.yaml`

3. **Write `research/passport.yaml`:**
   ```yaml
   research_question: "<one sentence>"
   phase: bootstrap
   claims: []
   planned_experiment_ids: []
   experiment_intake_declaration: no_experiments_declared
   ```

4. **Write `research/research_state.yaml`:**
   ```yaml
   mode: hitl  # or autonomous
   pipeline_profile: <profile>
   phases_enabled: [...]
   current_phase: bootstrap
   pending_approval: true
   approved_by: null
   approved_at: null
   autonomous:
     max_iterations: 20
     max_wall_time_hours: 8
     metric_primary: null
     stop_on_plateau: 3
   ```

5. **Log** in `research/decision_log.md` with `source: user|ai`.

6. **Gate:**
   - HITL: stop; ask human to confirm passport → set `approved_by: human`, `pending_approval: false`
   - Autonomous: set `approved_by: ai`, advance `current_phase` to first enabled phase

7. **Handoff** to `research-pipeline` or `literature-survey` / next phase skill.

## Do not

- Run experiments in bootstrap
- Commit secrets or fill fake metrics
