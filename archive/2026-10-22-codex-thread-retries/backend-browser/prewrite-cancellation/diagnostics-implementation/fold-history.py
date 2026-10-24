
from pathlib import Path
import subprocess,json,time,hashlib,os
repo=Path.cwd(); session=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries'); out=session/'backend-browser/prewrite-cancellation/diagnostics-implementation'; baseline=json.loads((out/'baseline.json').read_text()); old=baseline['head']; base='bf6d4b0c49600c15e17fe71248807ef43424e932'; e22='e22eecab01a691225f7464f0c8965526648f442a'
def git(*args):return subprocess.check_output(['git',*args])
def run(name,argv,env=None):
 start=time.monotonic();r=subprocess.run(argv,capture_output=True,env=env);(out/(name+'.stdout')).write_bytes(r.stdout);(out/(name+'.stderr')).write_bytes(r.stderr);(out/(name+'.json')).write_text(json.dumps({'argv':argv,'exit':r.returncode,'wallSeconds':time.monotonic()-start},indent=2)+'\n');assert r.returncode==0,(name,r.stderr.decode());return r.stdout
assert git('rev-parse','HEAD').decode().strip()==old and not git('diff','--cached','--name-only')
assert sorted(git('diff','--name-only').decode().splitlines())==sorted(baseline['ownedPaths'])
for name in ['normal','race']:
 r=json.loads((out/(name+'.json')).read_text());assert r['exit']==0 and r['passCount']==13 and not r['failSkip']
inputs=json.loads((out/'quick-inputs-before.json').read_text());assert all(hashlib.sha256((repo/p).read_bytes()).hexdigest()==h for p,h in inputs.items())
pp=session/'backend-browser/prewrite-cancellation/b-adoption/final-source-packet.json'; assert hashlib.sha256(pp.read_bytes()).hexdigest()==baseline['preservedPinPacketSHA256']; packet=json.loads(pp.read_text()); assert all(hashlib.sha256((session/p).read_bytes()).hexdigest()==h for p,h in packet['artifactHashes'].items())
oldseries=git('rev-list','--reverse',base+'..'+old).decode().splitlines();assert len(oldseries)==18
(out/'old18.series.txt').write_bytes(git('log','--reverse','--format=%H %s',base+'..'+old));(out/'owned.patch').write_bytes(git('diff','--binary','--full-index'))
run('final-diff-check',['git','diff','--check']);run('stage',['git','add','--',*baseline['ownedPaths']]);run('cached-diff-check',['git','diff','--cached','--check'])
candidate=git('write-tree').decode().strip();(out/'tested-candidate-tree.txt').write_text(candidate+'\n')
message=out/'commit-message.txt'; message.write_text('fixup! test: connect retry browser controls to the real backend\n\nCorrelate exact browser requests with forwarding server stages so a failed\nqueue observation retains its typed context evidence without changing RPCs.\n')
run('commit',['git','commit','-F',str(message)]);fixup=git('rev-parse','HEAD').decode().strip();run('autosquash',['git','rebase','--interactive','--autosquash',oldseries[13]],dict(os.environ,GIT_SEQUENCE_EDITOR='true',GIT_EDITOR='true'))
head=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip();assert tree==candidate and not git('status','--porcelain')
newseries=git('rev-list','--reverse',base+'..'+head).decode().splitlines();assert len(newseries)==18 and newseries[:14]==oldseries[:14]
def patch(c):return git('diff','--binary','--full-index',c+'^',c)
def msg(c):return git('cat-file','commit',c).split(b'\n\n',1)[1]
replay=[]
for i in range(15,18):
 assert patch(oldseries[i])==patch(newseries[i]) and msg(oldseries[i])==msg(newseries[i]);replay.append({'logical':i+1,'old':oldseries[i],'new':newseries[i],'rawPatchAndMessageExact':True,'patchSHA256':hashlib.sha256(patch(newseries[i])).hexdigest()})
changed=git('diff','--name-only',old,head).decode().splitlines();assert sorted(changed)==sorted(baseline['ownedPaths'])
def blobs(c):return {line.split(b'\t',1)[1].decode():line.split(b'\t',1)[0].decode() for line in git('ls-tree','-r',c).splitlines()}
a,b=blobs(old),blobs(head);assert a.keys()==b.keys() and all(a[p]==b[p] for p in a if p not in baseline['ownedPaths'])
changedE22=git('diff','--name-only',e22,head).decode().splitlines();pinpaths=json.loads((session/'backend-browser/prewrite-cancellation/b-adoption/baseline.json').read_text())['paths'];assert sorted(changedE22)==sorted(pinpaths+baseline['ownedPaths'])
assert all(hashlib.sha256(git('show',head+':'+p)).hexdigest()==h for p,h in inputs.items())
proof={'head':head,'tree':tree,'clean':True,'base':base,'oldPinHead':old,'oldPinTree':baseline['tree'],'testedCandidateTreeEqual':True,'all274NewQuickInputsEqualCommitted':True,'old11QuickNotClaimedOnNewBytes':True,'commitCount':18,'first14Exact':True,'owning15Old':oldseries[14],'owning15New':newseries[14],'transientFixupFolded':fixup,'replay16To18':replay,'changedVsPinHead':changed,'changedVsReviewedE22':changedE22,'allOtherBlobModesEqualPinHead':True,'all117PreservedPinPacketArtifactsUnchanged':len(packet['artifactHashes'])==117,'samePathInventory':True,'migrations':'No database migrations or persisted-state change from diagnostics; previous branch history/lineage remains retained'}
(out/'history-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
for name,args in [('final18.series.txt',('log','--reverse','--format=%H %s',base+'..'+head)),('full-final.diff',('diff','--binary','--full-index',base,head)),('full-final.paths.txt',('diff','--name-status',base,head)),('pin-head.delta.diff',('diff','--binary','--full-index',old,head)),('e22.delta.diff',('diff','--binary','--full-index',e22,head)),('range-diff.txt',('range-diff','--no-color',base+'..'+old,base+'..'+head)),('final-tree.txt',('ls-tree','-r',head)),('graph.txt',('log','--graph','--oneline',base+'..'+head))]:(out/name).write_bytes(git(*args))
print(json.dumps(proof))
