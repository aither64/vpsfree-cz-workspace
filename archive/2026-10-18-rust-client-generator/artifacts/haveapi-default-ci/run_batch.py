import json,subprocess,time
from pathlib import Path
root=Path(__file__).resolve().parent
started=time.monotonic()
remaining={r["databaseId"]:r for r in json.loads((root/"ci-runs.json").read_text())}
completed=[]
while remaining:
 for run_id,expected in list(remaining.items()):
  p=subprocess.run(["gh","run","view",str(run_id),"--repo","vpsfreecz/haveapi","--json","databaseId,headSha,headBranch,event,status,conclusion,workflowName,url,jobs"],text=True,capture_output=True)
  if p.returncode:
   (root/"ci-read-error.txt").write_text(p.stderr)
   raise SystemExit("Status read failed; preserve remaining explicit IDs, no retry")
  actual=json.loads(p.stdout)
  assert all(actual[k]==expected[k] for k in ["headSha","headBranch","event"])
  (root/f"run-{run_id}.json").write_text(json.dumps(actual,indent=2)+"\n")
  if actual["status"]=="completed":
   completed.append(actual);del remaining[run_id]
   print(run_id,actual["workflowName"],actual["conclusion"],flush=True)
   if actual["conclusion"]!="success":
    with (root/f"failed-{run_id}.log").open("w") as log:subprocess.run(["gh","run","view",str(run_id),"--repo","vpsfreecz/haveapi","--log-failed"],stdout=log,stderr=subprocess.STDOUT)
 if remaining:time.sleep(30)
result={"result":"passed" if all(r["conclusion"]=="success" for r in completed) else "failed","runs":completed,"elapsed_seconds":round(time.monotonic()-started,3),"active_operations":[]}
(root/"result.json").write_text(json.dumps(result,indent=2)+"\n")
print("Result:",result["result"],flush=True)
raise SystemExit(0 if result["result"]=="passed" else 1)
