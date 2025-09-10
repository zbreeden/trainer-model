# The Trainer

A living training ground for FourTwenty. Each **scroll** is a focused learning arc with:
- **Orbit** (where this belongs in the constellation)
- **Glyph** (emoji)
- **Ritual** (cadence & streak)
- **Quests** (bite‑size tasks)
- **Artifacts** (what you produce)
- **XP** (light gamification)

### How it works
1. Edit `/data/scrolls.yml` to add/modify scrolls.
2. Push to GitHub; **GitHub Pages** serves `index.html`.
3. The page reads your YAML and renders interactive cards.
4. Progress is stored in `localStorage` (your machine only).
5. Optional: GA4/GTM events fire on interactions.

### Constellation links
- ← Back to **Sandbox** (hub)
- → **The Launch**, **The Archive**, **The Signal**, **The Grower**, ...

---

## Rituals & Rules of Play
- **Daily Pulse** (10–30 min): move at least one quest forward.
- **WIP Limit = 3** active scrolls.
- **Weekly Retro**: log what shipped; queue next quests.
- **Boss Fight**: mock interview or live demo at end of a scroll.

## Broadcasts

<!-- SIGNAL:START
id: 2025-09-10-trainer-glossary-merge
ts_utc: 2025-09-10T10:42:00Z
title: "Trainer: Glossary_Merge notebook aligns module glossaries to hub"
summary: >
  Glossary_Merge.ipynb (built and proven in The Trainer) merges multiple module
  glossary files into a single canonical `seeds/glossary.yml`. It deduplicates
  by `key`, unions list fields (`examples`, `see_also`, `tags`), shallow-merges
  `source`, and writes a clean, sorted output. The process runs in Jupyter or
  Colab and can be lifted into the hub as a reusable action for constellation-wide
  seed hygiene.
tags: [learning, jupyter, colab, automation, glossary, seeds, merge, trainer]
links:
  - label: "Glossary_Merge.ipynb (Trainer)"
    url: "https://github.com/zbreeden/trainer-model/blob/main/notebooks/Glossary_Merge.ipynb"
  - label: "merge_glossaries.py (script)"
    url: "https://github.com/zbreeden/trainer-model/blob/main/scripts/merge_glossaries.py"
  - label: "merge_map.csv (inputs map)"
    url: "https://github.com/zbreeden/trainer-model/blob/main/data/merge_map.csv"
  - label: "seeds/glossary.yml (target)"
    url: "https://github.com/zbreeden/trainer-model/blob/main/seeds/glossary.yml"
SIGNAL:END -->

License: MIT (or your choice).
