import hashlib,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
w=Path("/home/aither/workspace/ai/vpsfree.cz"); s=w/"work/2026-10-24-flake-update-downgrade-guard-replacement"
name=sys.argv[1]
assert name in {"terraform-provider-vpsadmin","vpsadminos","vpsf-status","vpsfree-irc-bot","vpsadminos-org-configuration"}
p=s/"verification/integration-preparation"/name
d=json.loads((p/"source.json").read_text())
r=Path(d["source_worktree"]); t=Path(d["target_worktree"])
def git(path,*a):return subprocess.check_output(["git","-C",str(path),*a],text=True).strip()
assert git(r,"rev-parse","HEAD")==d["head"] and not git(r,"status","--porcelain=v1")
assert git(t,"rev-parse","HEAD")==d["base"] and not git(t,"status","--porcelain=v1")
assert subprocess.run(["git","-C",str(t),"symbolic-ref","-q","HEAD"],stdout=subprocess.DEVNULL).returncode==1
hookdir=Path(git(t,"rev-parse","--git-path","hooks"))
hooks={}
for h in sorted(hookdir.iterdir()) if hookdir.exists() else []:
 if h.is_file() and not h.name.endswith(".sample"):
  assert h.stat().st_mode&0o111,h.name
  hooks[h.name]={"path":str(h),"sha256":hashlib.sha256(h.read_bytes()).hexdigest(),"executable":True}
assert (p/"environment.log").is_file()
d.update({"ready_at":datetime.now(timezone.utc).isoformat(),"target_detached":True,"target_clean":True,"hooks":hooks,"environment":"Declared Nix environment prepared; see environment.log. No source tests or package/live builds rerun.","readiness":"ready for lead-only one-repository claim and critical section; no claim/merge/default push by implementer","capture_comparison":"separate normal dev-session capture; see capture-comparison.json when present","log_hashes":{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file()}})
(p/"ready.json").write_text(json.dumps(d,indent=2)+"\n")
plan=f"""# {name}: prepared target and lead-only merge plan

Ready, unclaimed. Target `{t}` is detached, clean at `{d['base']}`.
Feature `{r}` is clean at exact reviewed `{d['head']}`. Fresh SSH/fetch and
full-series/full-index binary diff/lock identity are in source.json and ready.json,
bound to review6bb7af and inventory821181. No source/head/pin change or test rerun.

Installed executable hooks: {', '.join(hooks) if hooks else 'none; no repository hook framework or active hook is declared/installed'}.
Declared environment and normal hook setup are recorded in environment.log.

The lead enters `nix develop --no-write-lock-file -c bash` in the target before
acquiring one `{name}` repository claim. Resolve any dependency/trust issue
unclaimed. Read authoritative exact claim status and proceed only when held.
No machine claim or shared workspace tracking lock is needed for this target.

Inside that already prepared shell and held claim:

```sh
cd {t}
[[ $(git rev-parse HEAD) == {d['base']} ]]
[[ -z $(git status --porcelain=v1) ]]
[[ $(git -C {r} rev-parse HEAD) == {d['head']} ]]
[[ -z $(git -C {r} status --porcelain=v1) ]]
git ls-remote --symref {d['canonical_ssh']} HEAD refs/heads/{d['target']} refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
```

Inspect the fresh target/feature equality before merging. Any movement stops
this attempt; reconcile effects and release before repair/rebase decisions.
Then ordinary fast-forward merge (retain full stdout/stderr):

```sh
git merge --ff-only {d['head']}
[[ $(git rev-parse HEAD) == {d['head']} ]]
[[ -z $(git status --porcelain=v1) ]]
```

Inspect actual complete merge/hook output even if Git exits0; post-merge hooks
can fail without failing Git. On hook failure, inspect effects, release once
known safe, repair unlocked. Never bypass hooks or silently retry.
Before push freshly prove remote target still exact `{d['base']}`:

```sh
git ls-remote {d['canonical_ssh']} refs/heads/{d['target']}
# Lead verifies exact expected target before proceeding.
git push --porcelain {d['canonical_ssh']} HEAD:refs/heads/{d['target']}
git ls-remote --symref {d['canonical_ssh']} HEAD refs/heads/{d['target']} refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
[[ $(git rev-parse HEAD) == {d['head']} ]]
[[ -z $(git status --porcelain=v1) ]]
```

Final target and feature must both equal exact `{d['head']}`. No force push or
feature deletion. A rejected/interrupted push requires actual ref/effect
reconciliation before release/retry; do not reset the target or hide uncertainty.
Verify authoritative exact owned claim, release, and prove released state before
CI, records or any subsequent work. Do not hold ownership for CI waits/tests.
No cleanup, deployment or lifecycle action is authorized. Preserve target,
feature refs and existing roots. Lead records integration effects and receipts.
"""
(p/"plan.md").write_text(plan)
print(json.dumps({"repository":name,"base":d["base"],"head":d["head"],"target":str(t),"hooks":list(hooks),"ready":True},indent=2))
