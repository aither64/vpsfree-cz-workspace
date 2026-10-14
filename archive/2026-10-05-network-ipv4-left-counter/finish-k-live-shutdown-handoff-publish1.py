from pathlib import Path
import subprocess,json,hashlib,datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-kb-contracts-runtime';O=R.parent/'vpsfree-kb-contracts';OLD='74b0717db8d8686d99fac51052a99908c41dad19';BASE='873758fd6aec0c03f50a94600e0ceab97946f255';BRANCHES=[T.name,T.name+'-kb-runtime'];PREFIX='finish-k-live-shutdown-handoff-publish1-'
def git(*args,repo=R):
 p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if p.stderr:print(p.stderr.decode(),end='',flush=True)
 return p.stdout
def save(name,data):
 if isinstance(data,str):data=data.encode()
 with (T/(PREFIX+name)).open('xb') as f:f.write(data)
paths=sorted(f['path'] for f in json.loads((T/'finish-k-live-shutdown-handoff-publish1-files.json').read_text()));expected={f['path']:f['sha256'] for f in json.loads((T/'finish-k-live-shutdown-handoff-publish1-files.json').read_text())}
assert git('rev-parse','HEAD').decode().strip()==OLD and git('branch','--show-current').decode().strip()==BRANCHES[1]
assert git('diff','--cached','--binary')==b''
assert git('status','--porcelain=v1','--untracked-files=all').decode()==''.join(' M '+p+'\n' for p in paths)
assert git('diff','--binary','--full-index')==(T/'finish-k-live-shutdown-handoff-publish1-working.diff').read_bytes()
for path,sha in expected.items():assert hashlib.sha256((R/path).read_bytes()).hexdigest()==sha,path
assert git('rev-parse','HEAD',repo=O).decode().strip()==OLD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('remote','get-url','origin').decode().strip()=='git@github.com:vpsfreecz/vpsfree-kb-contracts.git'
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
for branch in BRANCHES:assert git('ls-remote','origin','refs/heads/'+branch).decode()==OLD+'\trefs/heads/'+branch+'\n'
hooks=Path(git('rev-parse','--git-path','hooks').decode().strip());assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
assert subprocess.run(['git','-C',str(R),'config','--get','core.hooksPath'],capture_output=True).returncode==1
assert not any(Path(n).name in {'.overcommit.yml','.pre-commit-config.yaml','lefthook.yml','lefthook.yaml'} or '/.husky/' in '/'+n for n in git('ls-files').decode().splitlines())
save('old.diff',git('diff','--binary','--full-index',BASE,OLD));save('old.history',git('log','--reverse','--format=fuller',BASE+'..'+OLD));save('accepted.diff',git('diff','--binary','--full-index'))
git('update-ref','refs/heads/preserve/finish-generator-g9',OLD,'0'*40)
message=T/(PREFIX+'message');message.write_text('runtime: add portable KB launcher and capture leases\n\nUse one standalone engine for checkout and packaged cluster commands. Private\nversioned identities, prepared artifacts and fresh run receipts bind owned\nresources to immutable source and full-lifetime capture leases. Cold resume\nretains the accepted artifact; updates prepare exact guest closures before\nstopping and preserve owned disks and credentials. Require unchanged resolved\nSSH endpoints so retained host-key trust remains valid after the restart.\nPublic lifecycle contention refuses before mutation rather than queuing it.\n\nCapture and validation share explicit connection and artifact-root contracts,\nwith canonical source proof and bilingual result preservation. Keep the\nartifact flock in the writing process through publication and cleanup so a\nhelper failure cannot admit a competing writer during synchronous writes.\nObserved lease loss cancels capture and prevents subsequent publication.\n\nVerify the installed tools directly on an ordinary Linux/Nix/KVM host through\npublic commands, with exact predecessor continuity and measured capacity.\nThe selected IP inventory fixture uses a small member VPS and dedicated\nadministrator API provisioning while retaining a proved member browser.\nExpose a separate strict hosted check for the accepted committed media.\n\nDiscover all machine SSH keys within one readiness deadline, retaining private\nnative diagnostics and refusing partial or changed trust. Give the runner its\nown POSIX session before machine creation; containing cgroup and host failures\nstill require complete ownership and exit proof. Quiesce its control thread\nbefore closing the listener, and preserve primary fixture failures and native\nprivate diagnostics without accepting unknown socket contents.\n\nPin the private directory and socket inode during authenticated live shutdown.\nThe same locked stop or update may retire only that unchanged control socket\nafter acknowledged shutdown and complete exit proof for the same launch and\nrunner. The verifier uses final-controller stop, genuine predecessor resume\nand final-controller update. Interruption discards this permission; a dead\nresidual cannot reconstruct it from saved path or inode facts.\n\nLegacy state and sockets remain untouched rather than being adopted by the\nnew engine.\n');assert all(len(line)<=80 for line in message.read_text().splitlines())
git('add','--',*paths);assert git('diff','--cached','--name-only').decode().splitlines()==paths
TREE=git('write-tree').decode().strip();print(git('commit','--amend','-F',str(message)).decode(),flush=True)
HEAD=git('rev-parse','HEAD').decode().strip();assert git('rev-parse','HEAD^{tree}').decode().strip()==TREE and git('rev-parse','HEAD^')==git('rev-parse',OLD+'^')
assert git('diff','--name-only',OLD,HEAD).decode().splitlines()==paths and git('status','--porcelain=v1','--untracked-files=all')==b''
print(git('rebase','--onto',HEAD,OLD,repo=O).decode(),flush=True);assert git('rev-parse','HEAD',repo=O).decode().strip()==HEAD and git('status','--porcelain=v1','--untracked-files=all',repo=O)==b''
assert git('rev-list','--count',BASE+'..HEAD').decode().strip()=='2' and git('rev-list','--merges',BASE+'..HEAD')==b''
save('head',HEAD+'\n');save('history',git('log','--reverse','--format=fuller',BASE+'..HEAD'));save('diff',git('diff','--binary','--full-index',BASE,HEAD));save('correction.diff',git('diff','--binary','--full-index',OLD,HEAD))
save('proof.json',json.dumps(dict(base=BASE,old=OLD,head=HEAD,tree=TREE,paths=paths,sha256=expected,commits=2,both_worktrees_clean_same_head=True,old_generator_preserved='preserve/finish-generator-g9',old_real_campaign_retained=True,local_ci=False,normal_hooks=True),indent=2)+'\n')
git('fetch','origin','master');assert git('rev-parse','FETCH_HEAD').decode().strip()==BASE
push=['push','--atomic']+['--force-with-lease=refs/heads/'+b+':'+OLD for b in BRANCHES]+['origin']+[HEAD+':refs/heads/'+b for b in BRANCHES]
print(git(*push).decode(),flush=True);remote=git('ls-remote','origin',*['refs/heads/'+b for b in BRANCHES]);save('remote',remote);assert sorted(remote.decode().splitlines())==sorted(HEAD+'\trefs/heads/'+b for b in BRANCHES)
print('Published corrected combined generator '+HEAD,flush=True)
