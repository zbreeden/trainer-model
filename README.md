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

## 🧾 Workflow logs & monitoring

This star now includes a lightweight workflow log pipeline that converts internal CSV logs into discoverable signals for monitoring and optional public broadcasting. The goal is to surface training progress in the star's UI and to make the same pattern reusable across other stars in the constellation.

What was added

- A generator script: `scripts/generate_funnel_progress.py` — parses CSV logs from `data/internal/` and the funnel specification in `seeds/funnel_spec.yml`, aggregates progress, and writes JSON outputs.
- Aggregated signal: `signals/funnel_progress.json` — contains per-training progress, percent complete, last activity, and step-level drilldowns.
- Per-log drilldowns: `signals/funnel_logs/` — contains per-CSV JSONs (e.g., `training_df.json`, `steps_df.json`) and `signals/funnel_logs/index.json` to let the UI discover available logs.
- UI integration: The star's `index.html` is updated to read `signals/funnel_progress.json` and show a "View logs" drilldown that fetches `signals/funnel_logs/index.json` and displays relevant events.
Why this pattern
- Keeps seeds (`seeds/funnel_spec.yml`) as the canonical funnel definitions while deriving runtime progress from logs.
- Produces signals that can be validated, archived, and displayed centrally by the hub.
- Provides a single dashboard with drilldowns, making it easy to monitor progress and inspect underlying events.

Run instructions

Install Python requirements for the script (recommended inside a venv):

```bash
pip install -r scripts/requirements.txt
```

Dry-run to validate parsing (no files written):

```bash
python scripts/generate_funnel_progress.py --dry-run --input-dir data/internal --funnel-spec seeds/funnel_spec.yml
3. Generate signals and per-log JSONs (writes to `signals/`):
```bash
python scripts/generate_funnel_progress.py --input-dir data/internal --funnel-spec seeds/funnel_spec.yml --out signals/funnel_progress.json --per-log
```

Notes & caveats

- The generator makes conservative attributions: if a step-only row is present it attempts to map the step to a parent training using `seeds/funnel_spec.yml`. Rows that cannot be attributed are listed under `orphans` in the generated JSON for manual review.
- `chapters_df.csv` and other auxiliary CSVs are parsed into per-log JSONs for drilldown but may not directly map to trainings without additional mapping rules.
- If you want to normalize legacy or inconsistent IDs, add an aliases file (e.g., `scripts/aliases.yml`) and we can wire it into the generator.

Portability

- This pattern (CSV logs -> generator -> `signals/` + UI discovery via `signals/*/index.json`) is intentionally generic and can be applied to other stars in the constellation. To reuse it for another star:

1. Add `scripts/generate_funnel_progress.py` or adapt it to the module's CSV shapes.
2. Point the script at that star's `seeds/*` funnel spec and `data/internal/` logs.
3. Wire that star's UI to read its own `signals/funnel_progress.json` and `signals/funnel_logs/index.json`.

Closing

- With these changes the Trainer star now exposes live progress and transparent drilldowns from your workflow logs. If you'd like, I can add alias mapping, schedule helpers, or a README snippet for publishing the `signals/funnel_progress.json` via the module's existing aggregation scripts.

---

*This star is part of the FourTwenty Analytics constellation - a modular analytics sandbox where each repository is a specialized "model" within an orbital system.*
