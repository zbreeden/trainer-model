# Trainer Model

> **The Trainer is the upskiller**

## 🌌 Constellation Information

- **Module Key**: `trainer_model`  
- **Repository**: `trainer-model`
- **Orbit**: 🧪
- **Status**: 🔥
- **Emoji**: 🏋️

## 🚀 Quick Start

1. **Review seeds/**: Adapt seeded data for this module
2. **Configure schemas/**: Update schema definitions as needed  
3. **Generate signals/**: Create latest.json broadcast file

## 📡 Broadcasting

This module produces a `signals/latest.json` file conforming to the constellation's broadcast schema. The Signal (📡) aggregates these across all stars.

## 🔗 Constellation Links

- **Hub**: [FourTwenty Analytics](https://github.com/zbreeden/FourTwentyAnalytics)
- **Archive**: Glossary, tags, and canonical definitions
- **Signal**: Cross-constellation broadcasting and telemetry

## 🧾 Workflow progress

This star exposes a lightweight workflow progress generator that converts the canonical funnel specification into a single discoverable signal for the UI.

What was added

- A YAML-first generator: `scripts/generate_funnel_progress.py` — reads `seeds/funnel_spec.yml` and emits `signals/funnel_progress.json` (per-training progress, percent complete, last activity, and step-level details).
- Aggregated signal: `signals/funnel_progress.json` — used directly by the star's UI to render training cards and step lists.

Why this pattern

- Keeps `seeds/funnel_spec.yml` as the canonical source-of-truth for funnel definitions and progress metadata.
- Simplifies the runtime pipeline: no CSV ingestion is required by default, and the UI reads a single JSON artifact.

Run instructions

Generate the progress JSON from the funnel spec:

```bash
python scripts/generate_funnel_progress.py --funnel-spec seeds/funnel_spec.yml --out signals/funnel_progress.json
```

Dry-run (print discovered trainings, no file written):

```bash
python scripts/generate_funnel_progress.py --dry-run
```

Notes & caveats

- The generator is YAML-first; legacy CSV support and per-log drilldowns were removed. If you need to reintroduce CSV-based inputs, we can add an explicit compatibility mode.
- The output schema is intentionally simple (trainings mapping) to keep the UI rendering straightforward.

Portability

- To reuse this pattern in another star, point the generator at that star's funnel spec and have the UI read its `signals/funnel_progress.json`.

Closing

- The Trainer star now renders progress directly from `signals/funnel_progress.json`. I can add alias mapping, scheduled generation (cron), or CI steps to produce this artifact automatically if you want.

---

*This star is part of the FourTwenty Analytics constellation - a modular analytics sandbox where each repository is a specialized "model" within an orbital system.*
