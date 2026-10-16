#!/usr/bin/env python3
"""Bounded parent fallback: observe only the recorded exact CI runs."""
import json, subprocess, time
from pathlib import Path
record = Path(__file__).resolve().parent
out = record / 'compatibility-ci-observation'
out.mkdir(exist_ok=True)
runs = json.loads((record / 'compatibility-ci-runs.json').read_text())
completed = set()
last = {}
started = time.monotonic()
while True:
    for repo, entry in runs.items():
        for label, run in entry['runs'].items():
            if run in completed:
                continue
            directory = out / str(run)
            directory.mkdir(exist_ok=True)
            proc = subprocess.run(['gh', 'run', 'view', str(run), '--repo', repo,
                '--json', 'headSha,status,conclusion,jobs,url'], capture_output=True, text=True)
            if proc.returncode:
                (directory / 'api-error.log').write_text(proc.stderr)
                print(json.dumps({'run':run, 'api_error':proc.returncode}), flush=True)
                continue
            status = json.loads(proc.stdout)
            if status['headSha'] != entry['head']:
                raise RuntimeError(f'Run {run} head does not match authorized source')
            (directory / 'status.json').write_text(proc.stdout)
            summary = {'repo':repo, 'label':label, 'run':run, 'head':status['headSha'],
                'status':status['status'], 'conclusion':status['conclusion'],
                'jobs':[{k:j[k] for k in ('name','databaseId','status','conclusion')} for j in status['jobs']]}
            if last.get(run) != summary:
                print(json.dumps(summary), flush=True)
                with (out / 'transitions.jsonl').open('a') as f:
                    f.write(json.dumps(summary)+'\n')
                last[run] = summary
            if status['status'] != 'completed':
                continue
            log = subprocess.run(['gh','run','view',str(run),'--repo',repo,'--log'],capture_output=True,text=True)
            (directory / 'workflow.log').write_text(log.stdout)
            (directory / 'log-error.log').write_text(log.stderr)
            (directory / 'log-status').write_text(str(log.returncode)+'\n')
            artifact = subprocess.run(['gh','api',f'repos/{repo}/actions/runs/{run}/artifacts'],capture_output=True,text=True)
            (directory / 'artifacts.json').write_text(artifact.stdout)
            if status['conclusion'] not in ('success','skipped'):
                failure = subprocess.run(['gh','run','view',str(run),'--repo',repo,'--log-failed'],capture_output=True,text=True)
                (directory / 'failed.log').write_text(failure.stdout)
                download = subprocess.run(['gh','run','download',str(run),'--repo',repo,'--dir',str(directory/'artifacts')],capture_output=True,text=True)
                (directory / 'download.log').write_text(download.stdout+download.stderr)
            completed.add(run)
            print(json.dumps({'terminal':run,'conclusion':status['conclusion'],'evidence':str(directory)}),flush=True)
    if len(completed) == sum(len(e['runs']) for e in runs.values()):
        final = {'elapsed_seconds':round(time.monotonic()-started),'runs':list(last.values())}
        (out/'result.json').write_text(json.dumps(final,indent=2)+'\n')
        raise SystemExit(0 if all(s['conclusion']=='success' for s in last.values()) else 1)
    time.sleep(45)
