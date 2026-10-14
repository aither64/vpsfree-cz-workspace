#!/usr/bin/env python3
"""One targeted immutable package construction plan, after the review gate."""
import datetime, hashlib, json, os, pathlib, subprocess, sys
TRACKING = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
NIX = '/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
GENERATOR = 'ab09bd437b310f57e4ff2453ec0432555d85eaca'
REF = 'github:vpsfreecz/vpsfree-kb-contracts/' + GENERATOR + '#runtime-verify'
PREFIX = TRACKING / 'finish-direct-package-plan1'
# The parent must create this acceptance from the completed independent report.
gate = json.loads((TRACKING / 'finish-source-review4-acceptance.json').read_text())
assert gate['generator'] == GENERATOR and gate['construction_may_proceed'] is True
assert pathlib.Path(NIX).is_file()
env = {k: os.environ[k] for k in ('HOME', 'USER', 'LOGNAME', 'XDG_RUNTIME_DIR') if k in os.environ}
env['PATH'] = str(pathlib.Path(NIX).parent) + ':/run/current-system/sw/bin'
env['NIX_CONFIG'] = ('experimental-features = nix-command flakes\n'
    'max-jobs = 1\ncores = 4\n'
    'extra-substituters = https://cache.vpsadminos.org\n'
    'extra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
argv = [NIX, 'build', '--dry-run', '--no-link', '--no-write-lock-file', '--json', REF]
record = {'schema': 1, 'generator': GENERATOR, 'argv': argv,
    'scope': 'Targeted public package plan; no realization, CI, suite or guest launch.',
    'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
with pathlib.Path(str(PREFIX) + '.stdout').open('xb') as out, pathlib.Path(str(PREFIX) + '.stderr').open('xb') as err:
    result = subprocess.run(argv, cwd='/home/aither', env=env, stdout=out, stderr=err)
record['exit_code'] = result.returncode
record['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
record['evidence'] = {str(x): hashlib.sha256(x.read_bytes()).hexdigest() for x in
    [pathlib.Path(str(PREFIX) + '.stdout'), pathlib.Path(str(PREFIX) + '.stderr')]}
with pathlib.Path(str(PREFIX) + '.json').open('x') as out:
    json.dump(record, out, indent=2); out.write('\n')
with pathlib.Path(str(PREFIX) + '.exit').open('x') as out: out.write(str(result.returncode) + '\n')
print(json.dumps({'exit_code': result.returncode, 'receipt': str(PREFIX) + '.json'}))
sys.exit(result.returncode)
