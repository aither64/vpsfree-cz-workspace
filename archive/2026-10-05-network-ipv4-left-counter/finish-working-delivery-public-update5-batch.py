import json,pathlib,subprocess,sys
T=pathlib.Path(__file__).resolve().parent
prep=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
commands=[
 [sys.executable,str(T/'finish-working-delivery-public-update5.py'),'preflight'],
 [sys.executable,str(T/'finish-working-delivery-service-launch5.py'),'finish-working-delivery-public-update5-preparation.json'],
 [sys.executable,str(T/'finish-working-delivery-public-update5.py'),'post']]
for stage,argv in zip(['read-only-preflight','one-public-update','read-only-new-source-proof'],commands):
 print(json.dumps({'stage':stage,'generator':prep['generator']}),flush=True)
 result=subprocess.run(argv,cwd=str(T))
 if result.returncode:
  print(json.dumps({'complete':False,'failed_stage':stage,'native_exit_code':result.returncode,'dependent_capture':'held'}),flush=True)
  sys.exit(result.returncode)
print(json.dumps({'complete':True,'update_and_post_read_lease_proof':True,'capture':'not started'}),flush=True)
