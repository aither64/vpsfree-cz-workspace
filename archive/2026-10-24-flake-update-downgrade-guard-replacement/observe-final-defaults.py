import hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
w=Path("/home/aither/workspace/ai/vpsfree.cz"); s=w/"work/2026-10-24-flake-update-downgrade-guard-replacement"; root=s/"verification/post-integration-final-observation"
rows=json.loads((root/"source-inventory.json").read_text())["repositories"]
fields="databaseId,headSha,headBranch,status,conclusion,name,workflowName,url,createdAt,updatedAt,event"
all_results=[]
for row in rows:
 p=root/row["repository"]; commands=[]
 def run(label,argv):
  c=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  (p/(label+".stdout")).write_bytes(c.stdout); (p/(label+".stderr")).write_bytes(c.stderr)
  commands.append({"label":label,"argv":argv,"exit_status":c.returncode,"observed_utc":datetime.now(timezone.utc).isoformat(),"stdout_sha256":hashlib.sha256(c.stdout).hexdigest(),"stderr_sha256":hashlib.sha256(c.stderr).hexdigest()})
  (p/"commands.json").write_text(json.dumps(commands,indent=2)+"\n")
  return c
 repo=Path(row["worktree"]); bare=w/"repos"/(row["repository"]+".git"); target="refs/heads/"+row["target"]; feature=row["feature_ref"]
 result={"repository":row["repository"],"final_head":row["final_head"],"target":row["target"],"source_review_verified":True}
 try:
  fetch=run("tracking-fetch",["git","--git-dir="+str(bare),"fetch","--no-tags",row["canonical_ssh"],"+"+target+":refs/remotes/origin/"+row["target"],"+"+feature+":refs/remotes/origin/2026-10-24-flake-update-downgrade-guard-replacement"])
  assert fetch.returncode==0,"Tracking fetch failed"
  requested=["HEAD",target,feature]
  if row["repository"]=="confctl":requested.append(feature+"-provider-r-evidence")
  ssh=run("ssh-refs",["git","ls-remote","--symref",row["canonical_ssh"],*requested]); assert ssh.returncode==0,"SSH proof unavailable"
  lines=[line.split("\t") for line in ssh.stdout.decode().splitlines()]; refs={name:value for value,name in lines}; result["ssh_refs"]=refs
  fetched=run("fetched-default",["git","--git-dir="+str(bare),"rev-parse","refs/remotes/origin/"+row["target"]]); assert fetched.returncode==0
  default=fetched.stdout.decode().strip(); result["fetched_default"]=default
  assert refs[target]==default,"Target moved between fetch and SSH observation"
  assert ["ref: "+target,"HEAD"] in lines,"Unexpected canonical default target"
  assert refs[feature]==row["final_head"],"Remote feature changed"
  if row["repository"]=="confctl":assert refs[feature+"-provider-r-evidence"]=="5436d3d7c36d3d5174eab3c44e3578830749d3db","R evidence changed"
  ancestry=run("final-head-ancestry",["git","--git-dir="+str(bare),"merge-base","--is-ancestor",row["final_head"],"refs/remotes/origin/"+row["target"]]); result["final_head_ancestor_exit"]=ancestry.returncode
  assert ancestry.returncode==0,"Final head is not a proven ancestor of fetched default"
  result["default_equals_final_head"]=default==row["final_head"]
  if "old_range" in row["lineage"]:
   legacy=run("old-head-ancestry",["git","--git-dir="+str(bare),"merge-base","--is-ancestor",row["lineage"]["old_range"]["head"],"refs/remotes/origin/"+row["target"]]); result["old_head_ancestor_exit"]=legacy.returncode
   assert legacy.returncode==1,"Unexpected legacy lineage; inspect before describing it"
  status=run("final-feature-status",["git","-C",str(repo),"status","--porcelain=v1"]); head=run("final-feature-head",["git","-C",str(repo),"rev-parse","HEAD"])
  assert status.returncode==0 and not status.stdout and head.returncode==0 and head.stdout.decode().strip()==row["final_head"]
  result["feature_still_clean_exact"]=True; result["source_proof"]="passed"
 except Exception as error:
  result["source_proof"]="error"; result["source_error"]=str(error)
 # Exactly one default-branch/exact-integrated-head snapshot; no feature query/poll.
 ci=run("default-head-ci",["gh","run","list","--repo","vpsfreecz/"+row["repository"],"--branch",row["target"],"--commit",row["final_head"],"--limit","50","--json",fields])
 result["ci_snapshot_exit"]=ci.returncode; result["ci_query_count"]=1
 if ci.returncode==0:
  runs=json.loads(ci.stdout); assert all(x["headBranch"]==row["target"] and x["headSha"]==row["final_head"] for x in runs)
  result["ci_runs"]=runs
  result["ci_pending"]=[x for x in runs if x["status"]!="completed"]
  result["ci_unsuccessful_completed"]=[x for x in runs if x["status"]=="completed" and x["conclusion"] not in ("success","skipped","neutral")]
 else:result["ci_unavailable"]=True
 result["observed_utc"]=datetime.now(timezone.utc).isoformat(); result["commands"]=commands
 (p/"proof.json").write_text(json.dumps(result,indent=2)+"\n"); all_results.append(result)
 (root/"proofs.json").write_text(json.dumps({"repositories":all_results,"complete":len(all_results)==len(rows)},indent=2)+"\n")
 print(json.dumps({"repository":row["repository"],"source":result["source_proof"],"default_equals_final_head":result.get("default_equals_final_head"),"ci_runs":len(result.get("ci_runs",[])),"pending":[x["databaseId"] for x in result.get("ci_pending",[])],"unsuccessful":[x["databaseId"] for x in result.get("ci_unsuccessful_completed",[])]}),flush=True)
