# Research

Состояние research-pipeline для агентов: вопросы, гипотезы, план, связь с экспериментами. Код обучения — в `src/`, конфиги runs — в `configs/`.

## Файлы

| Файл | Назначение |
|------|------------|
| `passport.yaml` | Тема, claims, связь с experiment_id |
| `research_state.yaml` | Режим (`hitl` / `autonomous`), текущая фаза, approvals |
| `pipeline.yaml` | Активный профиль pipeline |
| `pipeline_profiles.yaml` | Пресеты (`hypothesis-only`, `full-hitl`, …) |
| `hypotheses.yaml` | Гипотезы |
| `methodology.md` | План методологии |
| `experiment_provenance.yaml` | Журнал запусков (Hydra, W&B) |
| `decision_log.md` | Решения (user / ai) |
| `literature/` | Обзор литературы по темам; шаблон — `_example/` |
| `to_human/` | Краткие отчёты в autonomous-режиме |
| `manuscript/` | Publication track: draft, reviews, revision — [manuscript/README.md](manuscript/README.md) |

Схемы: `shared/schemas/`. Агенты: [AGENTS.md](../AGENTS.md), playbooks — `.cursor/agents/playbooks/`.
