import datetime,hashlib,json,os,pathlib,subprocess,sys
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
launcher=T/'finish-working-delivery-service-launch4.py';prep='finish-working-delivery-bilingual-capture5-preparation.json'
r=subprocess.run([sys.executable,str(launcher),prep],cwd=T,check=False)
if r.returncode:raise SystemExit(r.returncode)
p=json.loads((T/prep).read_text());packet=json.loads(pathlib.Path(p['packet_path']).read_text());root=pathlib.Path(packet['campaign_root']);a=json.loads((T/'finish-working-delivery-package-realize4-acceptance.json').read_text());s=a['selection'];context=pathlib.Path(p['context']);env=packet['environment'].copy();env.update(NODE_PATH=s['node_path'],GEM_HOME=s['gem_home'],GEM_PATH=s['gem_home'])
node=next(str(pathlib.Path(x)/'node') for x in s['path'].split(':') if pathlib.Path(x,'node').is_file())
script=T/'finish-working-delivery-fixture-resource-proof5.cjs';argv=[node,str(script),a['source'],s['metadata'],str(root/'capture-connection.json'),str(root/'output')]
record={'schema':1,'generator':a['generator'],'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Read-only same-run typed numeric inventory/disabled-network proof; no browser or inventory mutation','script_sha256':hashlib.sha256(script.read_bytes()).hexdigest()}
with (context/'typed-resource.stdout').open('xb') as out,(context/'typed-resource.stderr').open('xb') as err:
 q=subprocess.run(argv,cwd=packet['cwd'],env=env,stdin=subprocess.DEVNULL,stdout=out,stderr=err,check=False)
record.update(native_exit_code=q.returncode,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),evidence_sha256={n:hashlib.sha256((context/n).read_bytes()).hexdigest() for n in ['typed-resource.stdout','typed-resource.stderr']})
with (T/'finish-working-delivery-fixture-resource-proof5.json').open('x') as out:json.dump(record,out,indent=2);out.write('\n')
print(json.dumps({'typed_resource_native_exit':q.returncode,'proof_receipt':'finish-working-delivery-fixture-resource-proof5.json'}),flush=True)
raise SystemExit(q.returncode)
