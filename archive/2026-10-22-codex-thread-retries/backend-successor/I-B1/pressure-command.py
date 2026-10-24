#!/usr/bin/env python3
from pathlib import Path
import datetime, json, subprocess, time, sys
worktree=Path("/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace")
tracking=Path("/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-successor/I-B1")
expected="45e14be3d34a9ca2d3b418c310da927351b7f330"
head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=worktree,text=True).strip()
if head!=expected or subprocess.check_output(["git","status","--porcelain"],cwd=worktree):
 raise SystemExit("Frozen source identity or cleanliness changed")
out=tracking/"pressure-attempt-1"
out.mkdir()
argv=["nix","develop","--no-update-lock-file","--command","go","-C","portal","test","-mod=readonly","./internal/workspacecodex","-run","^TestRetry","-count=1","-timeout=180s","-json"]
start=time.monotonic();at=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (out/"stdout.jsonl").open("w") as stdout,(out/"stderr.log").open("w") as stderr:
 proc=subprocess.run(argv,cwd=worktree,stdout=stdout,stderr=stderr)
after=subprocess.check_output(["git","rev-parse","HEAD"],cwd=worktree,text=True).strip()
clean=not subprocess.check_output(["git","status","--porcelain"],cwd=worktree)
manifest=json.loads((tracking/"pressure-manifest.json").read_text())
passed=set();skipped=[];failed=[]
for line in (out/"stdout.jsonl").read_text().splitlines():
 try: event=json.loads(line)
 except json.JSONDecodeError: continue
 if event.get("Action")=="pass" and "Test" in event:passed.add(event["Test"])
 if event.get("Action")=="skip":skipped.append(event.get("Test","package"))
 if event.get("Action")=="fail":failed.append(event.get("Test","package"))
missing=sorted((set(manifest["topLevelNames"])|set(manifest["requiredPressureLeaves"]))-passed)
receipt={"command":argv,"cwd":str(worktree),"startedAt":at,"elapsed":time.monotonic()-start,"actualExit":proc.returncode,"before":head,"after":after,"clean":clean,"missingRequiredCases":missing,"skipped":skipped,"failed":failed,"pass":proc.returncode==0 and not missing and not skipped and after==expected and clean}
(out/"result.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt),flush=True)
sys.exit(0 if receipt["pass"] else (proc.returncode or 1))
