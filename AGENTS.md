# AGENTS.md

Точка входа для AI-ассистентов: карта репозитория. Правила поведения — в `.cursor/rules/`, сценарии — в `.cursor/skills/`.

## Layout

| Path | Purpose |
|------|---------|
| `configs/` | Hydra configs |
| `src/modeling/` | Training code |
| `src/train.py`, `src/eval.py` | Hydra entry points |
| `research/` | Research pipeline state — [research/README.md](research/README.md) |
| `.cursor/rules/` | Project rules |
| `.cursor/skills/` | Task skills |
| `.cursor/agents/` | Agent roles |
| `shared/schemas/` | JSON schemas for `research/` |

## Research pipeline

Режим и фаза: `research/research_state.yaml`. Пресеты фаз: `research/pipeline_profiles.yaml`.

## Commands

```bash
uv sync
uv sync --extra ml          # torch + wandb
uv sync --extra torch       # training only
uv sync --extra wandb       # W&B logger only
uv sync --extra mlflow      # MLflow logger
uv sync --group dev         # ruff, pre-commit, pytest
uv run python src/train.py
uv run python src/eval.py
uv sync --group dev && uv run ruff check src tests
```

Логгер по умолчанию: `logger=csv`. W&B: `uv sync --extra wandb` и `logger=wandb`.
