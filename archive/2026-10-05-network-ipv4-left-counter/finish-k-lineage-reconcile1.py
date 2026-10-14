from pathlib import Path
import subprocess,json
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts')
t=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
old='abadbcc4849ec6f83274e145d47c88060ef499a4'
head=(t/'finish-k-consolidate1-head').read_text().strip()
def git(*args): return subprocess.check_output(['git','-C',str(r),*args])
assert git('rev-parse','HEAD').decode().strip()==old
assert git('branch','--show-current').decode().strip()=='2026-10-05-network-ipv4-left-counter'
assert git('status','--porcelain=v1','--untracked-files=all','--ignored=matching')==b''
assert git('diff','--cached','--binary')==b''
ref='refs/heads/preserve/finish-original-k-abad'
existing=subprocess.run(['git','-C',str(r),'rev-parse','--verify',ref],capture_output=True,text=True)
if existing.returncode==0: assert existing.stdout.strip()==old
else: git('update-ref',ref,old,'0'*40)
(t/'finish-k-lineage-reconcile1-old.history').write_bytes(git('log','--format=fuller','--reverse','873758fd6aec0c03f50a94600e0ceab97946f255..HEAD'))
(t/'finish-k-lineage-reconcile1-old.diff').write_bytes(git('diff','--binary','--full-index','873758fd6aec0c03f50a94600e0ceab97946f255','HEAD'))
result=subprocess.run(['git','-C',str(r),'rebase','--onto',head,old],capture_output=True,text=True,check=True)
print(result.stdout,end=''); print(result.stderr,end='')
assert git('rev-parse','HEAD').decode().strip()==head
assert git('status','--porcelain=v1','--untracked-files=all')==b''
(t/'finish-k-lineage-reconcile1.json').write_text(json.dumps({'historical_original_head':old,'historical_runtime_head':'68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e','authoritative_combined_head':head,'method':'normal clean feature rebase onto consolidated generator; preserve old refs','clean':True,'same_head_for_both_registered_K_feature_branches':True,'no_local_ci_or_lifecycle':True},indent=2)+'\n')
print('Both registered K worktrees now select the same authoritative generator '+head)
