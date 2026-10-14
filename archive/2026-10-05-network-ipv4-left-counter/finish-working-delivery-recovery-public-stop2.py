"""Post-authorized recovery: one public stop and exact exit proof; no Campaign replay."""
import os,json,hashlib,subprocess,datetime,sys
from pathlib import Path
os.umask(0o077)
tracking=Path(__file__).resolve().parent
preparation=json.loads((tracking/'finish-working-delivery-recovery-public-stop2-preparation.json').read_text())
packet=json.loads(Path(preparation['packet_path']).read_text());context=Path(packet['context'])/'operation';context.mkdir(mode=0o700)
package=json.loads((tracking/'finish-working-delivery-package-realize2-acceptance.json').read_text());selection=package['selection'];root=Path(packet['campaign_root']);ids=preparation['source_ids']
original=json.loads((tracking/'finish-working-delivery-browser-path-diagnosis1.json').read_text());failed=root/'receipts/runtime-smoke-attempt.json';assert hashlib.sha256(failed.read_bytes()).hexdigest()==original['failed_attempt_sha256'];assert not (root/'receipts/runtime-smoke.json').exists()
records=[];stage='public-stop-after-owned-QEMU-termination'
def call(name,argv):
 d=context/name;d.mkdir(mode=0o700)
 with (d/'stdout').open('xb') as out,(d/'stderr').open('xb') as err:r=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=out,stderr=err,env=packet['environment'],cwd=packet['cwd'])
 value={'name':name,'stage':stage,'exit_code':r.returncode,'stdout_sha256':hashlib.sha256((d/'stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((d/'stderr').read_bytes()).hexdigest()};(d/'native.json').write_text(json.dumps(value,indent=2)+'\n');records.append(value)
 if r.returncode:raise RuntimeError('Native public command failed; private diagnostics retained')
 return (d/'stdout').read_bytes()
try:
 approved=json.loads((tracking/'finish-working-delivery-services-qemu-stop2-result.json').read_text());assert approved['native_exit']==0 and approved['signal_receipt']['signal_sent']=='SIGTERM' and approved['signal_receipt']['ownership_confirmed']
 runtime=[selection['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state')]
 call('public-stop',runtime+['stop','same-slug','--timeout','900'])
 status=json.loads(call('stopped-status',runtime+['status','same-slug']));assert status['found'] and status['state']=='stopped' and not status['ready']
 stage='complete-exit-and-retained-data-proof'
 proof_script=r"""require File.join(ARGV[0], 'cluster/lib/kb_runtime')
s = KbRuntime::State.new(ARGV[1], 'same-slug'); ids = JSON.parse(ARGV[2])
s.lock('gate') do
  p = s.read(s.path("processes-#{ids.fetch('run_id')}.json")); l = s.read(s.path("launch-#{ids.fetch('run_id')}.json"))
  raise 'foreign exit proof' unless ids.all? { |k,v| p[k] == v && l[k] == v }
  raise 'not stopped' unless s.read(s.path('phase.json'))['phase'] == 'stopped'
  raise 'incomplete exit' unless p['schema'] == 1 && p['complete'] == true
  raise 'owned process not gone' unless [p.fetch('runner'), *p.fetch('children')].all? { |t| KbRuntime::ProcessIdentity.gone?(t) }
  r = KbRuntime::Resources.new(s); claim = File.join(r.root, "#{p['instance_id']}-#{p['run_id']}.json")
  raise 'own claim retained' if File.exist?(claim) || File.symlink?(claim)
  raise 'socket namespace retained' if File.exist?(l.fetch('socket_dir')) || File.symlink?(l.fetch('socket_dir'))
  raise 'disks missing' unless %w[services-root.img node1-tank.img].all? { |n| File.file?(File.join(s.path('disks'),n)) }
  puts JSON.generate(ids.merge(complete: true, runner_gone: true, children_gone: p['children'].length, own_claim_absent: true, socket_namespace_absent: true, disks_retained: true))
end"""
 proof=json.loads(call('complete-exit',['ruby','-e',proof_script,selection['source'],str(root/'state'),json.dumps(ids)]))
 assert hashlib.sha256(failed.read_bytes()).hexdigest()==original['failed_attempt_sha256'] and not (root/'receipts/runtime-smoke.json').exists()
 value={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':True,'generator':preparation['generator'],'source_ids':ids,'public_stop_native0':True,'forced_QEMU_recovery_before_stop':True,'complete_exit':proof,'commands':records,'original_failed_attempt_sha256':original['failed_attempt_sha256'],'original_campaign_completed':False,'reset_or_launch_performed':False}
 (context/'completed.json').write_text(json.dumps(value,indent=2)+'\n');(tracking/'finish-working-delivery-recovery-public-stop2-proof.json').write_text(json.dumps(value,indent=2)+'\n');print(json.dumps({'complete':True,'children_gone':proof['children_gone'],'public_stop_native0':True,'forced_recovery':True}),flush=True)
except BaseException as error:
 value={'schema':1,'complete':False,'stage':stage,'failure_class':type(error).__name__,'source_ids':ids,'commands':records,'reset_or_launch_performed':False};(context/'failed.json').write_text(json.dumps(value,indent=2)+'\n');(tracking/'finish-working-delivery-recovery-public-stop2-proof.json').write_text(json.dumps(value,indent=2)+'\n');print(json.dumps({'complete':False,'stage':stage,'failure_class':type(error).__name__}),flush=True);sys.exit(1)
