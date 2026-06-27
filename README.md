# ml-research-template

CCDS + Hydra + modular AI research pipeline.

- Layout: [AGENTS.md](AGENTS.md)
- Research state: [research/README.md](research/README.md)

## Quick start

```bash
uv sync
uv run python src/train.py

# ML training stack (PyTorch + W&B)
uv sync --extra ml
uv run python src/train.py logger=wandb

# Only what you need
uv sync --extra torch
uv sync --extra wandb
uv sync --extra mlflow
uv sync --group dev
```

## License

MIT — [LICENSE](LICENSE), [NOTICE.md](NOTICE.md).
