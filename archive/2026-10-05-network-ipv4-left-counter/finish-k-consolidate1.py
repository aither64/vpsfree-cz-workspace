from pathlib import Path
import subprocess,json,hashlib,stat
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime')
t=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
base='873758fd6aec0c03f50a94600e0ceab97946f255'
oldhead='68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e'
oldpin='a50f8c1a11ea642edf823f04521f9eaa97132fd2'
oldv=b'5d5527a67315c18b595345aa6996d7724c1ed071'
newv=b'ebe4fab3d50a51bda1f94014ca95c73ba2a967a8'
def git(*args,input=None):
 result=subprocess.run(['git','-C',str(r),*args],input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 if result.stderr: print(result.stderr.decode(),end='',flush=True)
 return result.stdout
assert git('rev-parse','HEAD').decode().strip()==oldhead
assert git('rev-parse','origin/master').decode().strip()==base
assert git('branch','--show-current').decode().strip()=='2026-10-05-network-ipv4-left-counter-kb-runtime'
assert git('diff','--cached','--binary')==b''
expected=json.loads((t/'finish-k-pin1-final.files.json').read_text())
paths=(t/'finish-k-pin1-final.paths').read_text().splitlines()
for name,value in expected.items():
 p=r/name; assert p.is_file() and not p.is_symlink()
 assert hashlib.sha256(p.read_bytes()).hexdigest()==value['sha256'],name
 assert oct(p.stat().st_mode&0o777)==value['mode'],name
assert {line[3:] for line in git('status','--porcelain=v1','--untracked-files=all').decode().splitlines()}==set(paths)
for name in set(paths)-set(expected): assert not (r/name).exists(),name
for ref in ['refs/heads/preserve/finish-k68','refs/tags/kb-runtime-predecessor-68aa33b']:
 existing=subprocess.run(['git','-C',str(r),'rev-parse','--verify',ref],capture_output=True,text=True)
 if existing.returncode==0: assert existing.stdout.strip()==oldhead,(ref,existing.stdout)
 else: git('update-ref',ref,oldhead,'0'*40)
(t/'finish-k-consolidate1-before.diff').write_bytes(git('diff','--binary','--full-index','HEAD'))
pin_paths=['captures.json','contract/navigation.yml','contract/pages.yml','flake.nix','flake.lock']
for name in pin_paths:
 if name=='flake.lock': content=(r/name).read_bytes()
 else:
  content=git('show',f'{oldhead}:{name}'); assert content.count(oldv)==1,name; content=content.replace(oldv,newv)
 blob=git('hash-object','-w','--stdin',input=content).decode().strip()
 git('update-index','--add','--cacheinfo',f'100644,{blob},{name}')
assert sorted(git('diff','--cached','--name-only').decode().splitlines())==sorted(pin_paths)
(t/'finish-k-consolidate1-pin.staged.diff').write_bytes(git('diff','--cached','--binary','--full-index'))
print(git('commit','-F',str(t/'finish-k-pin-fixup.message')).decode(),flush=True)
git('add','-A','--',*paths)
assert set(git('diff','--cached','--name-only').decode().splitlines())==set(paths)-{'flake.lock','contract/navigation.yml','contract/pages.yml'}
for name,value in expected.items(): assert hashlib.sha256(git('show',f':{name}')).hexdigest()==value['sha256'],name
for name in set(paths)-set(expected): assert subprocess.run(['git','-C',str(r),'cat-file','-e',f':{name}'],capture_output=True).returncode!=0,name
(t/'finish-k-consolidate1-functional.staged.diff').write_bytes(git('diff','--cached','--binary','--full-index'))
accepted_tree=git('write-tree').decode().strip()
(t/'finish-k-consolidate1-tree').write_text(accepted_tree+'\n')
print(git('commit','-F',str(t/'finish-k-runtime-fixup.message')).decode(),flush=True)
# All changes are committed before rewriting the two unmerged owning commits.
assert git('status','--porcelain=v1','--untracked-files=all')==b''
print(subprocess.run(['git','-C',str(r),'-c','sequence.editor=true','rebase','-i','--autosquash',base],capture_output=True,text=True,check=True).stdout,flush=True)
assert git('rev-parse','HEAD^{tree}').decode().strip()==accepted_tree
print(git('commit','--amend','-F',str(t/'finish-k-combined-runtime.message')).decode(),flush=True)
assert git('rev-parse','HEAD^{tree}').decode().strip()==accepted_tree
assert git('status','--porcelain=v1','--untracked-files=all')==b''
assert git('rev-list','--count',f'{base}..HEAD').decode().strip()=='2'
assert git('rev-list','--merges',f'{base}..HEAD')==b''
for name,value in expected.items(): assert hashlib.sha256(git('show',f'HEAD:{name}')).hexdigest()==value['sha256'],name
assert git('diff','--name-only',oldhead,'HEAD','--','screenshots','cluster/lib/kb_state.rb','cluster/lib/kb_source.rb','cluster/lib/kb_closure.rb','cluster/lib/kb_machine.rb','.github/workflows/page-runtime.yml')==b''
head=git('rev-parse','HEAD').decode().strip()
(t/'finish-k-consolidate1-head').write_text(head+'\n')
(t/'finish-k-consolidate1-history').write_bytes(git('log','--reverse','--format=fuller',f'{base}..HEAD'))
(t/'finish-k-consolidate1-final.diff').write_bytes(git('diff','--binary','--full-index',base,'HEAD'))
(t/'finish-k-consolidate1-range-diff').write_bytes(git('range-diff',f'{base}..{oldhead}',f'{base}..HEAD'))
(t/'finish-k-consolidate1-final.json').write_text(json.dumps({'base':base,'head':head,'tree':accepted_tree,'commits':2,'merges':0,'clean':True,'checked_frozen_extant_paths':len(expected),'source2_plus_mechanical_v_pin_exact':True,'normal_hooks_enabled':True,'declared_hook_framework':'none','local_ci_run':False},indent=2)+'\n')
print('Combined generator committed with exact frozen source and canonical V pin: '+head,flush=True)
