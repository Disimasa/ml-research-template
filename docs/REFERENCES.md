# References

Upstream patterns and optional MIT skill installs by pipeline phase.

## Layout and training

- [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) — CCDS layout
- [lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template) — Hydra structure
- [Hydra docs](https://hydra.cc/docs/intro/)
- [uv docs](https://docs.astral.sh/uv/)

## Optional installs by phase

Template ships **own** `.cursor/agents/` + `.cursor/skills/` (MIT). External repos are optional accelerators.

| Phase | Template skill | Optional external (license) |
|-------|----------------|----------------------------|
| bootstrap | `new-project` | — |
| discover | `literature-survey` | [Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills); K-Dense paper-lookup (MIT) |
| ideate | `hypothesis-ideation` | Orchestra ideation lenses (MIT) |
| plan | `research-plan` | K-Dense scientific brainstorming (MIT) |
| execute | `run-experiment`, `autonomous-loop` | [Orchestra AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) — PEFT, TRL, W&B, lm-eval (MIT); [experiment-agent](https://github.com/Imbad0202/experiment-agent) (alt loop) |
| analyze | `analyze-results` | Orchestra eval skills (MIT) |
| synthesize | `log-decision`, `integrity-check` | — |
| write (deferred) | — | [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (CC BY-NC — separate install) |

## Orchestra bridge (execute)

When `uv sync --extra ml` and Orchestra skills installed locally:

- Route engineering tasks to Orchestra tool-skills (training, logging, eval)
- Keep **process gates** from this template (`integrity-check`, HITL approvals)
- Log session in `research/decision_log.md` (ARA-style via `research_manager`)

## K-Dense bridge (domain)

For bio/chem/domain libs, discover skills from [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — no bundled orchestrator; `research-pipeline` skill composes the chain.

## Licensing

See [NOTICE.md](../NOTICE.md). ARS NC content is **not** bundled — ideas only, own MIT agents/skills in this repo.
