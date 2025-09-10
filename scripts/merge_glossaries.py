#!/usr/bin/env python3
"""
Merge multiple glossary .yml files into seeds/glossary.yml with de-duplication.

Supports:
  - Passing YAML files directly
  - Passing a 2-column CSV mapping (The_Trainer_Artifact, Append_File)

Usage examples:
  python scripts/merge_glossaries.py --out trainer-model/seeds/glossary.yml trainer-model/pages/cbap/definitions-glossary.yml trainer-model/pages/ibm/data-ecosystem.yml
  python scripts/merge_glossaries.py --csv merge_map.csv
"""

import argparse, os, sys, csv, shutil
from collections import defaultdict
import yaml

REQUIRED_FIELDS = {"key", "term", "definition"}
LIST_FIELDS = {"examples", "see_also", "tags"}
DICT_FIELDS = {"source"}

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    if not isinstance(data, list):
        raise ValueError(f"{path} does not contain a YAML list")
    return data

def non_empty(v): return v not in (None, "", [], {})
def merge_lists(a, b): return list(dict.fromkeys((a or []) + (b or [])))
def merge_dicts(a, b): return {**(a or {}), **(b or {})}

def merge_entries(a, b):
    out = dict(a)
    for k, bv in b.items():
        av = out.get(k)
        if k in LIST_FIELDS: out[k] = merge_lists(av or [], bv or [])
        elif k in DICT_FIELDS: out[k] = merge_dicts(av or {}, bv or {})
        elif not non_empty(av) and non_empty(bv): out[k] = bv
    return out

def backup(path):
    if os.path.exists(path):
        shutil.copy2(path, path + ".bak")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="*", help="Input YAML files (ignored if --csv)")
    ap.add_argument("--out", default="trainer-model/seeds/glossary.yml")
    ap.add_argument("--csv", help="Optional 2-col CSV (artifact, append_file)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = []
    if args.csv:
        with open(args.csv, newline="", encoding="utf-8") as f:
            rdr = csv.DictReader(f)
            for row in rdr:
                files.append(row["The_Trainer_Artifact"])
    else:
        files = args.inputs

    merged = {}
    total = 0
    for path in files:
        items = load_yaml(path)
        for entry in items:
            if not REQUIRED_FIELDS <= entry.keys():
                raise ValueError(f"{path}: missing required fields in {entry}")
            k = entry["key"]
            total += 1
            merged[k] = merge_entries(merged[k], entry) if k in merged else entry

    merged_list = sorted(merged.values(), key=lambda x: x["key"])
    print(f"[summary] {len(files)} files → {total} items → {len(merged_list)} unique keys")

    if args.dry_run:
        return
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    backup(args.out)
    with open(args.out, "w", encoding="utf-8") as f:
        yaml.safe_dump(merged_list, f, sort_keys=False, allow_unicode=True)
    print(f"[ok] Wrote {args.out}")

if __name__ == "__main__":
    main()
