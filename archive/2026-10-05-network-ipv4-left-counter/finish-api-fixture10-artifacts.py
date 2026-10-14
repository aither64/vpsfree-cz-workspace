from pathlib import Path
import subprocess,json,hashlib,zipfile,io,datetime
T=Path(__file__).resolve().parent
runs=json.loads((T/'finish-api-fixture10-hosted/summary.json').read_text())['runs']
selected=next(r for r in runs if r['name']=='API Specs (topic parallel)')
R=T/'finish-api-fixture10-hosted'/selected['key']
run=json.loads((R/'final.json').read_text())
assert run['id']==selected['id'] and run['head_sha']==(T/'finish-api-fixture10.head').read_text().strip()
assert run['status']=='completed' and run['conclusion'] in ('success','failure')
metadata=json.loads((R/'artifacts.json').read_text())
D=T/'finish-api-fixture10-artifacts';D.mkdir()
GH='/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
rows=[];hashes={}
for mode in ('core','full'):
 name='rspec-results-'+mode+'-foundation'
 a=next(x for x in metadata['artifacts'] if x['name']==name)
 assert not a['expired'] and a['workflow_run']['id']==run['id'] and a['workflow_run']['head_sha']==run['head_sha']
 result=subprocess.run([GH,'api','repos/vpsfreecz/vpsadmin/actions/artifacts/'+str(a['id'])+'/zip'],capture_output=True)
 assert result.returncode==0,(name,result.returncode)
 digest=hashlib.sha256(result.stdout).hexdigest();assert a['digest']=='sha256:'+digest
 p=D/(mode+'-foundation.zip');p.write_bytes(result.stdout);hashes[p.name]=digest
 z=zipfile.ZipFile(io.BytesIO(result.stdout));assert z.testzip() is None
 expected={'rspec-results-'+mode+'-foundation.json','rspec-environment-'+mode+'-foundation.json'}
 assert set(z.namelist())==expected,z.namelist()
 for member in expected:
  data=z.read(member);json.loads(data);(D/member).write_bytes(data);hashes[member]=hashlib.sha256(data).hexdigest()
 rows.append({'mode':mode,'artifact_id':a['id'],'artifact_name':name,'digest':a['digest'],'collection_exit':result.returncode})
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'run':run['id'],'head':run['head_sha'],'attempt':run['run_attempt'],'artifacts':rows,'sha256':hashes}
(D/'manifest.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v))
