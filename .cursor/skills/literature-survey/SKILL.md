---
name: literature-survey
description: Discover phase — structured literature search with outline, fields, and JSON results
---

# Literature survey

**Phase:** `discover`  
**Agents:** `literature_scout`, `source_verifier`, `synthesis_agent`

## When to use

- Phase `discover` is enabled
- User asks for related work, literature review, or bibliography

## Prerequisites

- `research/passport.yaml` with `research_question`
- Template: `research/literature/_example/`

## Steps

### 1. Scope

- Choose `topic_slug` (e.g. `contrastive_reranking`)
- Create `research/literature/{topic_slug}/`

### 2. Outline (`outline.yaml`)

```yaml
topic: <topic_slug>
items:
  - id: item_001
    title: "<search theme>"
    query_hints: ["keywords", "authors"]
    priority: 1
execution:
  batch_size: 5
  items_per_agent: 1
  output_dir: ./results
```

### 3. Fields (`fields.yaml`)

Define extraction schema per paper:

```yaml
fields:
  - name: method
    description: "Core approach"
    detail_level: moderate
  - name: metrics
    description: "Reported metrics and datasets"
    detail_level: detailed
  - name: limitations
    description: "Stated limitations"
    detail_level: brief
```

### 4. Search and record (`results/*.json`)

Per source batch, write JSON:

```json
{
  "id": "src_001",
  "title": "...",
  "year": 2024,
  "doi": "...",
  "url": "...",
  "verified": false,
  "fields": { "method": "...", "metrics": "..." },
  "notes": ""
}
```

### 5. Verify (`source_verifier`)

- Set `verified: true` only after DOI/URL check
- Deduplicate; log rejections in `decision_log.md`

### 6. Synthesize gaps (`synthesis_agent`)

- Optional `research/literature/{topic}/README.md` — gaps and trends
- Update `passport.claims[]` only from verified sources

### 7. State update

- `passport.phase: discover`
- Run `integrity-check` (M1)
- **HITL gate:** `pending_approval: true` until human approves literature pack

## Optional external tools

See `docs/REFERENCES.md` — Orchestra `paper-lookup`, K-Dense literature skills (MIT, optional install).

## Handoff

→ `hypothesis-ideation` (ideate)
