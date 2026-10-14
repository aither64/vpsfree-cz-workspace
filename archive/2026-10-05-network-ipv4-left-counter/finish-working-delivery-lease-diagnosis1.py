#!/usr/bin/env python3
import json, os, pathlib, subprocess, sys
tracking = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
parent = pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-working1')
os.umask(0o077)
context = parent / 'lease-diagnosis1'
context.mkdir(mode=0o700)
packet = json.loads((parent/'owned-lifecycle1/packet.json').read_text())
selection_path = '/nix/store/1jcz8fb6zbvniw7xzww91jc6b3i07pqc-vpsfree-kb-verify-selection.json'
with (context/'stdout').open('xb') as out, (context/'stderr').open('xb') as err:
    result = subprocess.run(['node', str(tracking/'finish-working-delivery-lease-diagnosis1.cjs'), selection_path,
        str(parent/'owned-lifecycle1/connection-before.json'), str(parent/'campaign2/state'), str(context)],
        cwd=packet['cwd'], env=packet['environment'], stdin=subprocess.DEVNULL, stdout=out, stderr=err)
print(json.dumps({'exit_code':result.returncode, 'private_context':str(context)}))
sys.exit(result.returncode)
