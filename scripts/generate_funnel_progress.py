#!/usr/bin/env python3
"""
Generate signals/funnel_progress.json from CSV logs in data/internal/ using seeds/funnel_spec.yml.

Usage:
  python scripts/generate_funnel_progress.py [--input-dir data/internal] [--funnel-spec seeds/funnel_spec.yml] [--out signals/funnel_progress.json] [--per-log]

By default this is read-only with respect to seeds; it writes only to signals/.
"""

import argparse
import csv
import json
import os
from datetime import datetime
from glob import glob
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None


ISO_FORMATS = [
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
]


def parse_ts(s):
    if not s:
        return None
    s = s.strip()
    for fmt in ISO_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    # fallback: try fromisoformat
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return None


def load_funnel_spec(path):
    if not Path(path).exists():
        return {}
    if yaml is None:
        raise RuntimeError('PyYAML required to read funnel_spec.yml; install from requirements.txt')
    with open(path, 'r') as f:
        doc = yaml.safe_load(f)
    trainings = {}
    # supports the funnel_spec.yml structure used in repo: top-level 'funnels'
    for entry in (doc.get('funnels') or []):
        # normalize possible keys
        tid = entry.get('training_id') or entry.get('id') or entry.get('training_id_name') or entry.get('title')
        if not tid:
            continue
        # prefer training_id or id as key
        key = entry.get('training_id') or entry.get('id') or tid
        steps = []
        for s in (entry.get('steps') or []):
            sid = s.get('step_id') or s.get('id') or s.get('step_id_name') or s.get('name')
            if sid:
                steps.append(sid)
        trainings[key] = {
            'id': key,
            'title': entry.get('training_id_name') or entry.get('title') or tid,
            'steps': steps,
        }
    return trainings


def collect_csv_events(input_dir):
    events = []
    per_log = {}
    files = sorted(glob(os.path.join(input_dir, '*.csv')))
    for path in files:
        rows = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = [h.lower() for h in (reader.fieldnames or [])]
            # detect known shapes
            fname = os.path.basename(path)
            if 'training_df' in fname or ('training_id' in headers and 'training_is_completed' in headers):
                for r in reader:
                    ts = r.get('last_update_date') or r.get('training_last_update_date') or r.get('last_update')
                    training_id = r.get('training_id') or r.get('training') or r.get('training_id')
                    completed = r.get('training_is_completed') or r.get('training_completed') or r.get('training_status')
                    event = 'completed' if str(completed).lower() in ('true', '1', 'yes') else ''
                    parsed = parse_ts(ts)
                    iso = parsed.isoformat() + 'Z' if parsed else None
                    ev = {
                        'ts': iso,
                        'training_id': training_id,
                        'step_id': None,
                        'event': event,
                        'notes': '',
                        'source_file': fname,
                    }
                    rows.append(ev)
                    events.append(ev)
            elif 'steps_df' in fname or ('step_id' in headers and 'step_is_completed' in headers):
                for r in reader:
                    ts = r.get('step_last_update_date') or r.get('last_update_date') or r.get('last_update')
                    step_id = r.get('step_id') or r.get('id') or r.get('step')
                    completed = r.get('step_is_completed') or r.get('step_completed') or r.get('step_status')
                    event = 'completed' if str(completed).lower() in ('true', '1', 'yes', 'completed') else ''
                    parsed = parse_ts(ts)
                    iso = parsed.isoformat() + 'Z' if parsed else None
                    ev = {
                        'ts': iso,
                        'training_id': None,
                        'step_id': step_id,
                        'event': event,
                        'notes': '',
                        'source_file': fname,
                    }
                    rows.append(ev)
                    events.append(ev)
            else:
                for r in reader:
                    # generic fallback: preserve raw fields
                    ts = r.get('ts') or r.get('timestamp') or r.get('time') or r.get('date')
                    training_id = r.get('training_id') or r.get('training') or r.get('training_id_name')
                    step_id = r.get('step_id') or r.get('step') or r.get('step_id_name') or r.get('id')
                    event = (r.get('event') or r.get('status') or '').lower()
                    notes = r.get('notes') or r.get('note') or r.get('summary') or ''
                    parsed = parse_ts(ts)
                    iso = parsed.isoformat() + 'Z' if parsed else None
                    ev = {
                        'ts': iso,
                        'training_id': training_id,
                        'step_id': step_id,
                        'event': event,
                        'notes': notes,
                        'source_file': fname,
                    }
                    rows.append(ev)
                    events.append(ev)
        per_log[os.path.basename(path)] = rows
    return events, per_log


def aggregate(events, funnel_map):
    # build step->training map for attribution when events only include step_id
    step_to_training = {}
    for tkey, tval in funnel_map.items():
        for sid in (tval.get('steps') or []):
            if sid:
                step_to_training[sid.upper()] = tkey

    # for each training, track steps seen and last activity
    trainings = {}
    orphans = []
    for ev in sorted(events, key=lambda e: e.get('ts') or ''):
        tid = ev.get('training_id')
        sid = ev.get('step_id')
        ts = ev.get('ts')
        # if tid is missing but sid is present, try to attribute via step->training map
        if (not tid or tid not in funnel_map) and sid:
            mapped = step_to_training.get(sid.upper())
            if mapped:
                tid = mapped

        if not tid or tid not in funnel_map:
            orphans.append({'ts': ts, 'raw': ev, 'reason': 'unknown_training'})
            continue
        t = trainings.setdefault(tid, {
            'id': tid,
            'title': funnel_map[tid].get('title'),
            'steps_total': len(funnel_map[tid].get('steps') or []),
            'steps_completed': set(),
            'steps': [],
            'last_activity': None,
            'notes': None,
        })
        # update last activity
        if ts:
            try:
                t_ts = datetime.fromisoformat(ts.replace('Z', ''))
                if not t['last_activity'] or t_ts > datetime.fromisoformat(t['last_activity'].replace('Z', '')):
                    t['last_activity'] = ts
            except Exception:
                pass
        # interpret event
        if ev.get('event') in ('completed', 'complete', 'done', 'c') or ev.get('event') == '1':
            if sid:
                t['steps_completed'].add(sid)
        # keep a simple step list for drilldowns; preserve event metadata
        t['steps'].append({'id': sid, 'event': ev.get('event'), 'ts': ts, 'notes': ev.get('notes')})
    # finalize
    out = {}
    for k, v in trainings.items():
        steps_completed = sorted(list(v['steps_completed']))
        total = v['steps_total'] or 0
        percent = (len(steps_completed) / total * 100) if total else 0
        out[k] = {
            'id': k,
            'title': v.get('title'),
            'steps_total': total,
            'steps_completed': steps_completed,
            'percent_complete': round(percent, 4),
            'last_activity': v.get('last_activity'),
            'notes': v.get('notes'),
            'steps': v.get('steps'),
        }
    return out, orphans


def write_outputs(out_path, signals_dir, trainings, per_log=None, orphans=None):
    payload = {
        'generated_at': datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
        'trainings': trainings,
        'orphans': orphans or [],
    }
    # ensure signals dir
    Path(signals_dir).mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(payload, f, indent=2)
    # optionally write per-log
    if per_log:
        logs_dir = os.path.join(signals_dir, 'funnel_logs')
        Path(logs_dir).mkdir(parents=True, exist_ok=True)
        created = []
        for name, rows in per_log.items():
            safe_name = name.replace('.csv', '') + '.json'
            outp = os.path.join(logs_dir, safe_name)
            with open(outp, 'w') as lf:
                json.dump(rows, lf, indent=2)
            created.append(safe_name)
        # write index.json for UI discovery
        with open(os.path.join(logs_dir, 'index.json'), 'w') as idxf:
            json.dump({'files': created, 'generated_at': datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'}, idxf, indent=2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input-dir', default='data/internal', help='Directory with CSV logs')
    p.add_argument('--funnel-spec', default='seeds/funnel_spec.yml', help='Path to funnel_spec.yml')
    p.add_argument('--out', default='signals/funnel_progress.json', help='Output path for aggregated JSON')
    p.add_argument('--per-log', action='store_true', help='Also emit per-log JSON files under signals/funnel_logs/')
    p.add_argument('--dry-run', action='store_true', help="Don't write outputs; just print summary")
    args = p.parse_args()

    funnel_map = load_funnel_spec(args.funnel_spec)
    events, per_log = collect_csv_events(args.input_dir)
    trainings, orphans = aggregate(events, funnel_map)

    if args.dry_run:
        print('Found', len(events), 'events from CSVs')
        print('Trainings discovered:', ', '.join(trainings.keys()))
        print('Orphans:', len(orphans))
        return

    out_path = args.out
    signals_dir = os.path.dirname(out_path) or 'signals'
    write_outputs(out_path, signals_dir, trainings, per_log if args.per_log else None, orphans)
    print('Wrote', out_path)


if __name__ == '__main__':
    main()
