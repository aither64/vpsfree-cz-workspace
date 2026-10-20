import json, os, subprocess
from pathlib import Path

OUT = Path(__file__).parent
SOURCE = Path('/home/aither/.local/state/dev-workspaces/coordination/sources/e6ceb642878dd97546174217676d9861afc38d4e/checkout')
assert not os.environ.get('RUBYOPT'), 'preserve and review an existing RUBYOPT instead of replacing it'
env = dict(os.environ, RUBYOPT='-rbundler/setup')
result = subprocess.run(['dev-session', 'current'], env=env, text=True, capture_output=True)
(OUT / 'bundler-preload-current.log').write_text(result.stdout + result.stderr)
assert result.returncode == 0 and result.stdout.strip() == '2026-10-19-vpsadmin-kernel-cves'
for key in ['GEM_HOME', 'GEM_PATH', 'BUNDLE_GEMFILE', 'BUNDLE_PATH', 'BUNDLE_APP_CONFIG', 'BUNDLER_VERSION']:
    env.pop(key, None)
program = "require 'json'; require 'bundler'; Bundler.setup; require 'overcommit'; puts JSON.generate({ruby: RUBY_VERSION, json: JSON::VERSION, bundler: Bundler::VERSION, overcommit: Overcommit::VERSION, locked_bundle_activated_before_probe: true})"
result = subprocess.run(['nix', 'develop', str(SOURCE), '--command', 'ruby', '-e', program], cwd=SOURCE, env=env, text=True, capture_output=True)
(OUT / 'bundler-preload-retained-Nix-probe.log').write_text(result.stdout + result.stderr)
assert result.returncode == 0, 'declared retained Nix probe failed; stop before coordinator retry'
rows = [json.loads(line) for line in result.stdout.splitlines() if line.startswith('{')]
assert len(rows) == 1 and rows[0]['json'] == '2.21.1' and rows[0]['locked_bundle_activated_before_probe']
(OUT / 'environment-diagnosis.json').write_text(json.dumps({'cause': 'Selected coordinator probe requires json before Bundler.setup, activating default json2.9.1 instead of locked2.21.1.', 'normal_mechanism': 'Subprocess-scoped RUBYOPT=-rbundler/setup, activating the declared repository bundle before the probe require-json.', 'read_only_selected_dev_session_current_with_preload': 'PASS', 'retained_declared_Nix_shell_exact_probe_with_preload': rows[0], 'caller_GEM_BUNDLE_variables_removed_for_probe': True, 'source_or_runtime_edits': False, 'hook_bypass': False, 'retry_not_yet_executed': True}, indent=2) + '\n')
print(json.dumps({'environment_probe': 'PASS', 'versions': rows[0], 'supported_retry': 'same public coordinator prepare request, subprocess-scoped RUBYOPT=-rbundler/setup; no source edits or disabled hooks'}, indent=2), flush=True)
