#!/usr/bin/env python3
import json, os, pathlib, subprocess, sys
T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
P = pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-working1')
os.umask(0o077)
selection_path = '/nix/store/1jcz8fb6zbvniw7xzww91jc6b3i07pqc-vpsfree-kb-verify-selection.json'
selection = json.loads(pathlib.Path(selection_path).read_text())
context = P / 'api-diagnosis1'
context.mkdir(mode=0o700)
environment = {k: os.environ[k] for k in ['HOME', 'USER', 'LOGNAME'] if k in os.environ}
environment.update(PATH=selection['path'], GEM_HOME=selection['gem_home'], NODE_PATH=selection['node_path'], LANG='C.UTF-8',
    XDG_RUNTIME_DIR='/run/user/1000', PLAYWRIGHT_BROWSERS_PATH=selection['browsers'], FONTCONFIG_FILE=selection['fonts'],
    SSL_CERT_FILE=selection['certificates'], NIX_SSL_CERT_FILE=selection['certificates'])
with (context/'stdout.json').open('xb') as out, (context/'stderr.log').open('xb') as err:
    result = subprocess.run(['node', str(T/'finish-working-delivery-api-diagnosis1.cjs'), selection_path,
        str(P/'campaign2/smoke-connection.json'), str(context)], cwd=str(P/'ordinary-cwd2'), env=environment,
        stdin=subprocess.DEVNULL, stdout=out, stderr=err)
print(json.dumps({'exit_code':result.returncode, 'private_context':str(context)}))
if result.returncode == 0:
    report=json.loads((context/'stdout.json').read_text())
    with (T/'finish-working-delivery-api-diagnosis1.json').open('x') as out: json.dump(report,out,indent=2);out.write('\n')
    print(json.dumps(report))
sys.exit(result.returncode)
