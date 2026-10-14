"""One selected public stop and complete owned-exit proof; no reset."""
import datetime,hashlib,json,os,pathlib,subprocess,sys
os.umask(0o077);T=pathlib.Path(__file__).resolve().parent
prep=json.loads((T/'finish-working-delivery-operator-capture-working5-preparation.json').read_text())
packet=json.loads(pathlib.Path(prep['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
selection=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
expected=json.loads((T/'finish-working-delivery-public-update5-proof.json').read_text())['source_ids']
context=root.parent/'ordinary-public-stop6';context.mkdir(mode=0o700)
records=[];stage='connection';failure=None;proof=None
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def call(name,argv):
 d=context/name;d.mkdir(mode=0o700)
 with (d/'stdout').open('xb') as out,(d/'stderr').open('xb') as err:r=subprocess.run(argv,env=packet['environment'],cwd=packet['cwd'],stdin=subprocess.DEVNULL,stdout=out,stderr=err)
 records.append({'name':name,'exit_code':r.returncode,'stdout_sha256':sha(d/'stdout'),'stderr_sha256':sha(d/'stderr')})
 if r.returncode:raise RuntimeError('native public command refused; private diagnostics retained')
 return (d/'stdout').read_bytes()
def engine(name,args):return call(name,[selection['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),args[0],'same-slug',*args[1:]])
try:
 current=json.loads(engine('connection',['connection']));assert all(current[k]==expected[k] for k in expected)
 assert current['provenance']['source']['revision']=='b5e39e6fe9b44d2c31800dce75ad287d85981844'
 stage='ordinary-public-stop';engine('stop',['stop','--timeout','900'])
 stage='complete-exit';status=json.loads(engine('status',['status']));assert status['found'] and status['state']=='stopped' and not status['ready']
 body='''require File.join(ARGV[0], 'cluster/lib/kb_runtime')
s=KbRuntime::State.new(ARGV[1], 'same-slug')
s.lock('gate') do
 p=s.read(s.path("processes-#{ARGV[2]}.json")); l=s.read(s.path("launch-#{ARGV[2]}.json"))
 raise 'incomplete exit' unless p['schema']==1 && p['complete']==true && p['run_id']==ARGV[2]
 raise 'owned process not gone' unless [p['runner'],*p['children']].all? { |x| KbRuntime::ProcessIdentity.gone?(x) }
 r=KbRuntime::Resources.new(s);claim=File.join(r.root,"#{p['instance_id']}-#{p['run_id']}.json")
 raise 'retained claim' if File.exist?(claim) || File.symlink?(claim)
 raise 'retained socket' if File.exist?(l.fetch('socket_dir')) || File.symlink?(l.fetch('socket_dir'))
 puts JSON.generate({complete:true,runner_gone:true,children_gone:p['children'].length,own_claim_absent:true,socket_namespace_absent:true,instance_id:p['instance_id'],run_id:p['run_id'],artifact_id:p['artifact_id'],artifact_sha256:p['artifact_sha256']})
end'''
 proof=json.loads(call('complete-exit',['ruby','-e',body,selection['source'],str(root/'state'),expected['run_id']]));assert all(proof[k]==expected[k] for k in expected)
except BaseException as error:failure={'stage':stage,'class':type(error).__name__}
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':failure is None,'source_ids':expected,'proof':proof,'commands':records,'failure':failure,'reset_performed':False,'limits':'Only selected ordinary public stop and complete owned-exit proof at B5. Disks retained; no replacement/GC/integration/cleanup claim.'}
(context/'proof.json').write_text(json.dumps(v,indent=2)+'\n');(T/'finish-working-delivery-working5-stop6-proof.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'complete':v['complete'],'failure':failure,'reset_performed':False}));sys.exit(0 if v['complete'] else 1)
