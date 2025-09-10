# Notebook-friendly merger (no CLI needed)
import os, csv, shutil
from typing import List, Dict, Any
import yaml

REQUIRED_FIELDS = {"key", "term", "definition"}
LIST_FIELDS = {"examples", "see_also", "tags"}
DICT_FIELDS = {"source"}

def _non_empty(v): return v not in (None, "", [], {})
def _merge_lists(a, b): return list(dict.fromkeys((a or []) + (b or [])))
def _merge_dicts(a, b): 
    out = dict(a or {})
    for k, v in (b or {}).items():
        if k not in out or not _non_empty(out[k]):
            out[k] = v
    return out

def _merge_entries(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    if not a: return dict(b)
    out = dict(a)
    for k, bv in b.items():
        av = out.get(k)
        if k in LIST_FIELDS:
            out[k] = _merge_lists(av, bv)
        elif k in DICT_FIELDS:
            out[k] = _merge_dicts(av, bv)
        elif not _non_empty(av) and _non_empty(bv):
            out[k] = bv
    return out

def _load_yaml_list(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    if not isinstance(data, list):
        raise ValueError(f"{path} must be a YAML list")
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"{path} item {i+1} is not a mapping")
        missing = REQUIRED_FIELDS - set(item.keys())
        if missing:
            raise ValueError(f"{path} item {i+1} missing: {', '.join(sorted(missing))}")
    return data

def _write_yaml(path: str, items: List[Dict[str, Any]]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        shutil.copy2(path, path + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(items, f, sort_keys=False, allow_unicode=True, width=1000)

def merge_glossaries(inputs: List[str], out: str = "trainer-model/seeds/glossary.yml", sort_by: str = "key", dry_run: bool = False):
    merged: Dict[str, Dict[str, Any]] = {}
    seen = 0
    for p in inputs:
        items = _load_yaml_list(p)
        for e in items:
            k = e["key"]
            merged[k] = _merge_entries(merged.get(k), e)
            seen += 1
    out_list = sorted(merged.values(), key=lambda d: (d.get(sort_by) or "").lower())
    print(f"[summary] files={len(inputs)} items_in={seen} unique={len(out_list)} deduped={seen-len(out_list)}")
    if not dry_run:
        _write_yaml(out, out_list)
        print(f"[ok] wrote {out}")
    return out_list

def merge_from_csv(csv_path: str, out: str = "trainer-model/seeds/glossary.yml", sort_by: str = "key", dry_run: bool = False):
    inputs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        # expect columns: The_Trainer_Artifact, Append_File
        for row in rdr:
            inputs.append(row["The_Trainer_Artifact"])
    return merge_glossaries(inputs, out=out, sort_by=sort_by, dry_run=dry_run)
