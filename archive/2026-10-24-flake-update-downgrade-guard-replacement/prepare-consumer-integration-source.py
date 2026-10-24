import hashlib,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
w=Path("/home/aither/workspace/ai/vpsfree.cz")
slug="2026-10-24-flake-update-downgrade-guard-replacement"
s=w/"work"/slug
name=sys.argv[1]
allowed={"terraform-provider-vpsadmin","vpsadminos","vpsf-status","vpsfree-irc-bot","vpsadminos-org-configuration"}
assert name in allowed
r=w/"worktrees"/slug/name
p=s/"verification/integration-preparation"/name
p.mkdir(parents=True,mode=0o700)
inv=s/"git-rework-final-source-inventory.json"
review=s/"review-git-cache-report.md"
assert hashlib.sha256(inv.read_bytes()).hexdigest()=="821181a5dad2340b149f1013846cf1430c8373bec8258c881da49caf6bc833ab"
assert hashlib.sha256(review.read_bytes()).hexdigest()=="6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd"
e=next(x for x in json.loads(inv.read_text())["sources"] if x["repository"]==name)
def git(*args):return subprocess.check_output(["git","-C",str(r),*args],text=True)
assert git("rev-parse","HEAD").strip()==e["head"]
assert git("status","--porcelain=v1")==""
series=git("log","--reverse","--format=fuller",e["base"]+"..HEAD")
diff=git("diff","--full-index","--binary",e["base"],"HEAD")
assert series==e["series"] and diff==e["final_diff"]
assert git("diff","--name-status",e["base"],"HEAD")==e["name_status"]
assert git("rev-parse",e["base"]+":flake.lock")==git("rev-parse",e["head"]+":flake.lock")
(p/"full-series.txt").write_text(series); (p/"full.diff").write_text(diff)
remote="git@github.com:vpsfreecz/"+name+".git"
feature="refs/heads/"+slug
target="refs/heads/"+e["target"]
c=subprocess.run(["git","ls-remote","--symref",remote,"HEAD",target,feature],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(p/"ssh.stdout").write_text(c.stdout); (p/"ssh.stderr").write_text(c.stderr)
assert c.returncode==0,"SSH observation failed; stop affected repository"
refs={name:value for value,name in (line.split("\t") for line in c.stdout.splitlines())}
assert refs.get(target)==e["base"] and refs.get(feature)==e["head"],"Target or feature moved; stop before repair"
fetch=["git","--git-dir="+str(w/"repos"/(name+".git")),"fetch","--no-tags",remote,target+":refs/remotes/origin/"+e["target"],feature+":refs/remotes/origin/"+slug]
f=subprocess.run(fetch,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(p/"fetch.stdout").write_text(f.stdout); (p/"fetch.stderr").write_text(f.stderr)
assert f.returncode==0,"Fetch failed; reconcile"
assert git("rev-parse","refs/remotes/origin/"+e["target"]).strip()==e["base"],"Fetched target moved"
assert git("rev-parse","refs/remotes/origin/"+slug).strip()==e["head"],"Fetched feature moved"
d={"observed_utc":datetime.now(timezone.utc).isoformat(),"repository":name,"canonical_ssh":remote,"target":e["target"],"base":e["base"],"head":e["head"],"tree":e["tree"],"source_worktree":str(r),"target_worktree":str(r.parent/(name+"-integration-target")),"source_clean":True,"series_and_diff_match_reviewed_inventory":True,"lock_unchanged":True,"ssh_refs":refs,"review_sha256":hashlib.sha256(review.read_bytes()).hexdigest(),"inventory_sha256":hashlib.sha256(inv.read_bytes()).hexdigest(),"claim":"none; preparation only"}
(p/"source.json").write_text(json.dumps(d,indent=2)+"\n")
print(json.dumps(d,indent=2))
