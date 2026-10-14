#!/usr/bin/env python3
"""Retire only the explicitly accepted, failed isolation3 A/B via public commands."""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import sys

TRACKING = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
PRIVATE = pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g7')
SELECTION = pathlib.Path('/nix/store/kn0lvm348d4m4sk3l7jwpi6hf5aahwzw-vpsfree-kb-verify-selection.json')
UNIT = 'kb-verify-network-counter-g11-isolation3.service'
SYSTEMCTL = '/nix/store/khnfirshq5j299s6sfj0laxj0vr7gaa6-systemd-260.2/bin/systemctl'
EXPECTED = {
    'a': ('73730841-799a-4f8e-89ec-0d3b18e1d0ee', '8847d318-bc0c-4795-8e23-603118d24468', '0271532264adf5eeb33123d136d9a0663faf21b0'),
    'b': ('0ebf3601-314a-49d4-989f-fa468c13fcc3', 'c7d285c9-2ff7-4414-b57f-8c09650c25f5', '68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e'),
}
SDK = r'''
require 'json'
require 'digest'
require_relative './cluster/lib/kb_state'
require_relative './cluster/lib/kb_process'
root, instance, run, revision, mode, evidence = ARGV
state = KbRuntime::State.new(root, 'same-slug')
result = state.transaction(wait: false) do
  identity = state.identity
  phase = state.read(state.path('phase.json'))
  raise 'instance or run differs' unless identity['instance_id'] == instance && phase['run_id'] == run
  launch_path = state.path("launch-#{run}.json")
  launch = state.read(launch_path)
  raise 'launch identity differs' unless launch['instance_id'] == instance && launch['run_id'] == run && launch['state_root'] == root && launch['owner_uid'] == Process.uid && launch.dig('source', 'revision') == revision
  processes = state.read(state.path("processes-#{run}.json"))
  raise 'process identity differs' unless %w[instance_id run_id artifact_id artifact_sha256].all? { |key| processes[key] == launch[key] }
  tuples = [processes.fetch('runner'), *processes.fetch('children')]
  live = tuples.map { |tuple| KbRuntime::ProcessIdentity.matches?(tuple) }
  gone = tuples.map { |tuple| KbRuntime::ProcessIdentity.gone?(tuple) }
  cgroups = tuples.map do |tuple|
    live[tuples.index(tuple)] ? File.read("/proc/#{tuple.fetch('pid')}/cgroup").strip : nil
  end
  if mode == 'before'
    raise 'current launch is not proven live' unless KbRuntime::ProcessIdentity.runner_matches?(processes.fetch('runner'), launch) && live.all? && processes['complete'] == false
  else
    raise 'shutdown is not complete/stopped' unless phase['phase'] == 'stopped' && processes['complete'] == true && gone.all?
  end
  # Projection deliberately excludes build_inputs, input files, accounts and credentials.
  selected_launch = launch.slice('schema', 'instance_id', 'run_id', 'artifact_id', 'artifact_sha256', 'state_root', 'slug', 'owner_uid', 'socket_dir', 'source', 'runner_identity', 'boot_id')
  saved = { 'identity' => identity, 'phase' => phase, 'launch' => selected_launch, 'launch_sha256' => Digest::SHA256.hexdigest(state.file(launch_path)), 'processes' => processes }
  File.open(evidence, File::WRONLY | File::CREAT | File::EXCL | File::NOFOLLOW, 0o600) { |file| file.write(JSON.pretty_generate(saved) + "\n") }
  { 'instance_id' => instance, 'run_id' => run, 'source_revision' => revision, 'phase' => phase['phase'], 'artifact_id' => launch['artifact_id'], 'complete' => processes['complete'], 'recorded_child_count' => processes['children'].size, 'runner_matches_launch' => KbRuntime::ProcessIdentity.runner_matches?(processes.fetch('runner'), launch), 'all_named_tuples_match' => live.all?, 'all_named_tuples_gone' => gone.all?, 'live_cgroups' => cgroups.compact.uniq, 'private_evidence' => evidence, 'evidence_sha256' => Digest::SHA256.file(evidence).hexdigest }
end
puts JSON.generate(result)
'''

def write_new(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')
    os.chmod(path, 0o600)

def main():
    os.umask(0o077)
    acceptance = json.loads((TRACKING / 'finish-direct-runtime-baseline-source-acceptance1.json').read_text())
    assert acceptance['retirement']['authorized'] is True
    selection = json.loads(SELECTION.read_text())
    assert selection['runtime'] == '/nix/store/lgx08vhysb73ja1m91xhcdcw6f87lr7d-vpsfree-kb-devcluster'
    env = {key: os.environ[key] for key in ['HOME', 'USER', 'LOGNAME', 'XDG_RUNTIME_DIR'] if key in os.environ}
    assert env.get('XDG_RUNTIME_DIR') == '/run/user/1000'
    env.update(PATH=selection['path'], LANG='C.UTF-8', SSL_CERT_FILE=selection['certificates'], GEM_HOME=selection['gem_home'], GEM_PATH=selection['gem_home'])
    destination = PRIVATE / 'retirement-isolation3'
    destination.mkdir(mode=0o700)
    summary = {'schema': 1, 'unit': UNIT, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'instances': {}, 'accepted': False}
    write_new(destination / 'selection.json', {'path': str(SELECTION), 'sha256': hashlib.sha256(SELECTION.read_bytes()).hexdigest()})
    ruby = str(pathlib.Path(selection['gem_home']).parents[3] / 'bin/ruby')
    assert pathlib.Path(ruby).is_file()
    for name, (instance, run, revision) in EXPECTED.items():
        root = PRIVATE / 'campaign' / ('state-' + name)
        show = subprocess.run([SYSTEMCTL, '--user', 'show', UNIT, '--property=ActiveState,SubState,InvocationID,ControlGroup,ExitType,MainPID'], capture_output=True, text=True, check=True)
        properties = dict(line.split('=', 1) for line in show.stdout.splitlines() if '=' in line)
        assert properties['ActiveState'] == 'active' and properties['SubState'] == 'running'
        assert properties['InvocationID'] == '7d48dadad272465fbfc29a3e1cdc21d1' and properties['ExitType'] == 'cgroup'
        item = {'unit_before': properties}
        summary['instances'][name] = item
        for mode in ['before', 'after']:
            evidence = destination / (name + '-' + mode + '-records.json')
            observation = subprocess.run([ruby, '-', str(root), instance, run, revision, mode, str(evidence)], input=SDK, text=True, capture_output=True, cwd=selection['source'], env=env)
            if observation.returncode:
                with (destination / (name + '-' + mode + '-observation.stderr')).open('xb') as stream:
                    stream.write(observation.stderr.encode())
                raise RuntimeError('named SDK observation refused for ' + name + '/' + mode)
            item[mode] = json.loads(observation.stdout)
            if mode == 'before':
                assert item[mode]['live_cgroups'] == ['0::' + properties['ControlGroup']]
                operation = 'stop'
                argv = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root), operation, 'same-slug', '--timeout', '120']
            else:
                operation = 'reset'
                argv = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root), operation, 'same-slug']
            command = {'argv': argv, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
            with (destination / (name + '-' + operation + '.stdout')).open('xb') as output, (destination / (name + '-' + operation + '.stderr')).open('xb') as error:
                completed = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=output, stderr=error, env=env, cwd=destination)
            command.update(exit_code=completed.returncode, finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
            write_new(destination / (name + '-' + operation + '.json'), command)
            item[operation] = command
            print(json.dumps({'instance': name, 'operation': operation, 'native_exit': completed.returncode}), flush=True)
            if completed.returncode:
                raise RuntimeError('public ' + operation + ' refused for ' + name + '; no further command allowed')
        assert not (root / 'clusters' / 'same-slug').exists()
        item['owned_cluster_tree_absent'] = True
    summary['accepted'] = True
    summary['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    write_new(destination / 'result.json', summary)
    write_new(TRACKING / 'finish-direct-isolation3-retirement1.json', summary)
    print(json.dumps({'accepted': True, 'private_evidence': str(destination), 'unit_action': 'none', 'G4_G6_preview': 'untouched'}), flush=True)

if __name__ == '__main__':
    main()
