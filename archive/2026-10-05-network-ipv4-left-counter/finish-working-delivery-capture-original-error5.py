"""Same immutable public capture core, retaining its original error privately."""
import datetime,hashlib,json,os,pathlib,subprocess,sys
os.umask(0o077)
T=pathlib.Path(__file__).resolve().parent
p=json.loads((T/'finish-working-delivery-operator-capture-working5-preparation.json').read_text())
packet=json.loads(pathlib.Path(p['packet_path']).read_text())
s=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
root=pathlib.Path(packet['campaign_root']);ctx=root.parent/'capture-original-error-working5';ctx.mkdir(mode=0o700)
script=r'''const fs=require('fs'),path=require('path');
const [source,metadata,state,output,errorFile]=process.argv.slice(1);
const {main}=require(path.join(source,'runner/capture.cjs'));
const sourceMetadata=JSON.parse(fs.readFileSync(metadata));
main({argv:['--cluster','same-slug','--state-root',state,'--output-root',output,'--language','cs','--checkpoint','networking/ip-address-list'],sourceMetadata,defaultOutputRoot:process.cwd(),defaultStateRoot:path.join(process.cwd(),'.devcluster/v2')}).catch(error=>{
 fs.writeFileSync(errorFile,String(error.stack||error),{mode:0o600,flag:'wx'});
 process.stderr.write('Original capture error retained privately\n');process.exitCode=1;
});'''
argv=['node','-e',script,s['source'],s['metadata'],str(root/'state'),p['output_root'],str(ctx/'original-error.txt')]
with (ctx/'stdout').open('xb') as out,(ctx/'stderr').open('xb') as err:
 result=subprocess.run(argv,cwd=packet['cwd'],env=packet['environment'],stdin=subprocess.DEVNULL,stdout=out,stderr=err)
record={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':p['generator'],'native_exit_code':result.returncode,'complete':True,'original_error_private':(ctx/'original-error.txt').exists(),'context':str(ctx),'scope':'Separately selected diagnostic invocation of the identical exported main used by packaged capture, identical metadata/args/output/locks/lease/fixtures. Only catch retains original error privately. No source override/new VM/Campaign replay or passing-capture claim.'}
for name in ('stdout','stderr','original-error.txt'):
 if (ctx/name).exists():record[name+'_sha256']=hashlib.sha256((ctx/name).read_bytes()).hexdigest()
with (T/'finish-working-delivery-capture-original-error-working5.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'native_exit_code':result.returncode,'original_error_private':record['original_error_private']}),flush=True)
sys.exit(result.returncode)
