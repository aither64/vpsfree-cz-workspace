
from pathlib import Path
import json, hashlib, subprocess, time, os
repo=Path.cwd(); out=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-browser/prewrite-cancellation/b-adoption')
old='e22eecab01a691225f7464f0c8965526648f442a'; base='bf6d4b0c49600c15e17fe71248807ef43424e932'; ancestor='aafaf4195d695c4641ce4f9342d56a1786f237c3'
def git(*a): return subprocess.check_output(['git',*a])
def run(name,argv,env=None):
    start=time.monotonic(); p=subprocess.run(argv,capture_output=True,env=env)
    (out/(name+'.stdout')).write_bytes(p.stdout); (out/(name+'.stderr')).write_bytes(p.stderr)
    (out/(name+'.json')).write_text(json.dumps({'argv':argv,'exit':p.returncode,'elapsed':time.monotonic()-start},indent=2)+'\n')
    assert p.returncode==0,(name,p.returncode)
    return p.stdout
assert git('rev-parse','HEAD').decode().strip()==old
assert git('rev-parse','2026-10-22-codex-thread-retries-reviewed-e22eecab').decode().strip()==old
assert not git('diff','--cached','--name-only')
paths=json.loads((out/'baseline.json').read_text())['paths']
assert sorted(git('diff','--name-only').decode().splitlines())==sorted(paths)
quick=json.loads((out/'quick.json').read_text()); assert quick['exit']==0 and quick['passCount']==11 and not quick['failSkip']
inputs=json.loads((out/'quick-inputs-after.json').read_text()); assert all(hashlib.sha256((repo/p).read_bytes()).hexdigest()==h for p,h in inputs.items())
oldseries=git('rev-list','--reverse',base+'..'+old).decode().splitlines(); assert len(oldseries)==18
(out/'old18.series.txt').write_bytes(git('log','--reverse','--format=%H %s',base+'..'+old))
(out/'five-path-adoption.diff').write_bytes(git('diff','--binary','--full-index'))
run('diff-check',['git','diff','--check'])
run('stage',['git','add','--',*paths]); run('cached-diff-check',['git','diff','--cached','--check'])
candidate=git('write-tree').decode().strip(); (out/'tested-candidate-tree.txt').write_text(candidate+'\n')
message=out/'commit-message.txt'; message.write_text('fixup! deps: select codex-web retry activity support\n\nKeep Nix, Go and the vendor digest on the accepted transport successor.\nIt preserves the live connection when cancellation is known before Write.\n')
run('commit',['git','commit','-F',str(message)])
transient=git('rev-parse','HEAD').decode().strip()
run('autosquash',['git','rebase','--interactive','--autosquash',ancestor],dict(os.environ,GIT_SEQUENCE_EDITOR='true',GIT_EDITOR='true'))
head=git('rev-parse','HEAD').decode().strip(); tree=git('rev-parse','HEAD^{tree}').decode().strip()
assert tree==candidate; assert not git('status','--porcelain')
newseries=git('rev-list','--reverse',base+'..'+head).decode().splitlines(); assert len(newseries)==18 and newseries[:3]==oldseries[:3]
def patch(c): return git('diff','--binary','--full-index',c+'^',c)
def msg(c): return git('cat-file','commit',c).split(b'\n\n',1)[1]
replay=[]
for i in range(4,18):
    assert patch(oldseries[i])==patch(newseries[i]),i+1
    assert msg(oldseries[i])==msg(newseries[i]),i+1
    replay.append({'logical':i+1,'old':oldseries[i],'new':newseries[i],'rawPatchAndMessageEqual':True,'patchSHA256':hashlib.sha256(patch(newseries[i])).hexdigest()})
changed=git('diff','--name-only',old,head).decode().splitlines(); assert sorted(changed)==sorted(paths)
def blobs(c):
    return {line.split(b'\t',1)[1].decode():line.split(b'\t',1)[0].decode() for line in git('ls-tree','-r',c).splitlines()}
a,b=blobs(old),blobs(head); assert a.keys()==b.keys(); assert all(a[p]==b[p] for p in a if p not in paths)
assert all(hashlib.sha256(git('show',head+':'+p)).hexdigest()==h for p,h in inputs.items())
proof={'base':base,'old':old,'head':head,'tree':tree,'clean':True,'testedCandidateTreeEqual':True,'quickInputsEqualFinalCommitted':True,'commitCount':18,'first3Exact':True,'owning4Old':oldseries[3],'owning4New':newseries[3],'transientFixupFolded':transient,'replay5To18':replay,'changedVsE22':changed,'allOtherBlobModesEqual':True,'samePathInventory':True,'noNewMigrations':'No schema or database migration; one consolidated A dependency stream'}
(out/'history-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
for name,args in [('final18.series.txt',('log','--reverse','--format=%H %s',base+'..'+head)),('full-final.diff',('diff','--binary','--full-index',base,head)),('full-final.paths.txt',('diff','--name-status',base,head)),('e22.delta.diff',('diff','--binary','--full-index',old,head)),('range-diff.txt',('range-diff','--no-color',base+'..'+old,base+'..'+head)),('final-tree.txt',('ls-tree','-r',head)),('graph.txt',('log','--graph','--oneline',base+'..'+head))]:
    (out/name).write_bytes(git(*args))
print(json.dumps({'head':head,'tree':tree,'clean':True,'first3Exact':True,'replay5To18Exact':True,'testedTreeEqual':True,'changed':changed}))
