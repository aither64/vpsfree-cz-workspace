#!/usr/bin/env python3
"""Launch and observe one specifically prepared public verification phase."""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time

tracking = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
preparation_path = tracking / sys.argv[1]
preparation = json.loads(preparation_path.read_text())
gate = json.loads((tracking / 'finish-lease-observation-review1-acceptance.json').read_text())
assert preparation['generator'] == '725c325e8b4971931e5d16df86bafa8584358ecb' and gate['source_gate_complete'] and preparation['harness_revision'] == gate['k']
assert preparation['real_admission'] is True, 'real qualification has not been admitted'
assert preparation['kind'] == 'retained-g725-bilingual-capture-v1', 'wrong evidence unit kind'
context = pathlib.Path(preparation['context'])
packet_path = context / 'packet.json'
assert hashlib.sha256(packet_path.read_bytes()).hexdigest() == preparation['packet_sha256']
packet = json.loads(packet_path.read_text())
assert packet['unit'] == preparation['unit']
assert not (context / 'admission.json').exists() and not (context / 'result.json').exists()
unit = packet['unit']
systemctl = packet['systemctl']
systemd_run = str(pathlib.Path(systemctl).with_name('systemd-run'))
existing = subprocess.run([systemctl, '--user', 'show', unit, '--property=LoadState'], capture_output=True, text=True)
assert 'LoadState=not-found' in existing.stdout, 'unit name already exists'
environment_bin = next(str(pathlib.Path(item) / 'env') for item in packet['environment']['PATH'].split(':') if pathlib.Path(item, 'env').is_file())
argv = [systemd_run, '--user', '--unit=' + unit, '--service-type=exec', '--expand-environment=no',
    '--property=ExitType=cgroup', '--property=RemainAfterExit=yes', '--property=Restart=no',
    '--property=CollectMode=inactive', '--property=KillMode=control-group', '--property=OOMPolicy=continue',
    '--property=TimeoutStartSec=90s', '--property=RuntimeMaxSec=infinity', '--property=WatchdogSec=0',
    '--property=StopWhenUnneeded=no', '--property=UMask=0077', '--property=StandardInput=null',
    '--property=StandardOutput=append:' + str(context / 'stdout.log'),
    '--property=StandardError=append:' + str(context / 'stderr.log'), '--working-directory=' + packet['cwd'],
    environment_bin, '-i']
argv += [key + '=' + value for key, value in packet['environment'].items()]
argv += [os.path.realpath(sys.executable), str(tracking / 'finish-continuation-service-phase2.py'), str(packet_path)]
admission = {'schema': 1, 'unit': unit, 'generator': packet['generator'], 'phase': packet['phase'],
    'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'argv': argv}
with (context / 'launch.stdout').open('xb') as output, (context / 'launch.stderr').open('xb') as error:
    launch = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=output, stderr=error)
admission['exit_code'] = launch.returncode
admission['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (context / 'admission.json').open('x') as output:
    json.dump(admission, output, indent=2)
    output.write('\n')
if launch.returncode:
    print(json.dumps({'admission': 'failed', 'exit_code': launch.returncode, 'private_context': str(context)}), flush=True)
    sys.exit(launch.returncode)
print(json.dumps({'admission': 'accepted', 'unit': unit, 'phase': packet['phase'], 'private_context': str(context)}), flush=True)
last_report = time.monotonic()
while not (context / 'result.json').exists():
    properties = subprocess.run([systemctl, '--user', 'show', unit,
        '--property=ActiveState,SubState,MainPID,Result,ExecMainCode,ExecMainStatus'], capture_output=True, text=True)
    values = dict(line.split('=', 1) for line in properties.stdout.splitlines() if '=' in line)
    if values.get('MainPID') == '0' and values.get('ActiveState') in ['active', 'failed', 'inactive'] and not (context / 'result.json').exists():
        with (context / 'incomplete.json').open('x') as output:
            json.dump({'unit': unit, 'properties': values, 'reason': 'no finite-wrapper result receipt'}, output, indent=2)
        print(json.dumps({'result': 'incomplete', 'private_context': str(context)}), flush=True)
        sys.exit(1)
    if time.monotonic() - last_report >= 60:
        print(json.dumps({'phase': packet['phase'], 'unit': unit, 'state': values.get('ActiveState'),
            'wrapper': values.get('MainPID'), 'native_result': 'pending'}), flush=True)
        last_report = time.monotonic()
    time.sleep(5)
result = json.loads((context / 'result.json').read_text())
accepted = result.get('complete') is True and result.get('exit_code') == 0 and not result.get('cancel_reason') and not result.get('wrapper_failure')
public = {'schema': 1, 'generator': packet['generator'], 'phase': packet['phase'], 'unit': unit,
    'accepted': accepted, 'native_exit_code': result.get('exit_code'), 'wrapper_complete': result.get('complete'),
    'cancel_reason': result.get('cancel_reason'), 'wrapper_failure': result.get('wrapper_failure'),
    'private_context': str(context), 'result_sha256': hashlib.sha256((context / 'result.json').read_bytes()).hexdigest(),
    'started_at': admission['started_at'], 'finished_at': result['finished_at'],
    'limit': 'Native phase result only; parent owns checkpoint/source/guest/media acceptance. No cleanup certified.'}
with (tracking / (preparation_path.stem.replace('-preparation', '') + '.json')).open('x') as output:
    json.dump(public, output, indent=2)
    output.write('\n')
print(json.dumps(public), flush=True)
sys.exit(0 if accepted else 1)
