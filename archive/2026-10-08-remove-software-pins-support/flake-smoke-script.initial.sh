#!/usr/bin/env bash
set -euo pipefail

smoke_repo=$(realpath "${1:?usage: confctl-flake-smoke.sh CONFCTL_WORKTREE}")
smoke_fixture=$(mktemp -d /tmp/confctl-flake-smoke.XXXXXX)
smoke_source="$smoke_fixture/confctl-source"
smoke_cluster="$smoke_fixture/cluster-config"
smoke_lock_before=$(sha256sum "$smoke_repo/flake.lock")
export BUNDLE_GEMFILE="$smoke_repo/Gemfile"
export RUBYLIB="$smoke_repo/lib"
export CONFCTL_TTY=0 NO_COLOR=1 PAGER=

printf 'Disposable evaluation fixture: %s\n' "$smoke_fixture"

# Snapshot only tracked working-tree content, including intent-to-add files.
# Keep Bundler caches and all session records outside the flake source.
python3 - "$smoke_repo" "$smoke_source" <<'PY'
import os
import pathlib
import shutil
import subprocess
import sys

repo, target = map(pathlib.Path, sys.argv[1:])
paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=repo).decode().split('\0')
for name in paths:
    if not name:
        continue
    source = repo / name
    if not source.exists() and not source.is_symlink():
        continue
    destination = target / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_symlink():
        os.symlink(os.readlink(source), destination)
    elif source.is_file():
        shutil.copy2(source, destination)
PY

smoke_nix=(nix --extra-experimental-features 'nix-command flakes')
smoke_nixpkgs=$("${smoke_nix[@]}" eval --raw --impure --no-write-lock-file --no-update-lock-file \
  --expr "(builtins.getFlake \"$smoke_source\").inputs.nixpkgs.outPath")

python3 - "$smoke_cluster" "$smoke_source" "$smoke_nixpkgs" <<'PY'
import json
import pathlib
import sys

cluster, source, nixpkgs = map(pathlib.Path, sys.argv[1:])
for name in ('cluster', 'configs', 'data', 'modules/cluster', 'rawFirst', 'rawLater', 'rawOverride'):
    (cluster / name).mkdir(parents=True, exist_ok=True)
for name, marker in (('rawFirst', 'first'), ('rawLater', 'later'), ('rawOverride', 'override')):
    (cluster / name / 'default.nix').write_text('{ marker = "' + marker + '"; }\n')
(cluster / 'cluster/module-list.nix').write_text('[ ./machines.nix ]\n')
(cluster / 'cluster/machines.nix').write_text('''{ ... }: {
  cluster."nested/later" = {
    spin = "nixos";
    inputs.channels = [ "first" "later" ];
    smokeTag = "channel";
  };
  cluster."nested/overridden" = {
    spin = "nixos";
    inputs.channels = [ "first" "later" ];
    inputs.overrides.raw = "rawOverride";
    smokeTag = "machine";
  };
}
''')
(cluster / 'modules/cluster/default.nix').write_text('''{ lib, ... }: {
  options.cluster = lib.mkOption {
    type = lib.types.attrsOf (lib.types.submodule {
      options.smokeTag = lib.mkOption {
        type = lib.types.str;
        default = "unset";
        description = "Custom smoke metadata.";
      };
    });
  };
}
''')
(cluster / 'data/default.nix').write_text('{ lib }: {}\n')
(cluster / 'configs/confctl.nix').write_text('''{ ... }: {
  confctl.nix.impureEval = true;
  confctl.nix.legacyNixPath = true;
  confctl.nix.legacyNixPathMap = [ "nixpkgs" "raw" ];
}
''')
flake = '''{
  inputs = {
    confctl.url = @CONFCTL_URL@;
    confctl.inputs.nixpkgs.follows = "nixpkgs";
    nixpkgs.url = @NIXPKGS_URL@;
    rawFirst = { url = "path:./rawFirst"; flake = false; };
    rawLater = { url = "path:./rawLater"; flake = false; };
    rawOverride = { url = "path:./rawOverride"; flake = false; };
    rawAlias.follows = "rawFirst";
  };
  outputs = inputs@{ self, confctl, ... }:
    let
      outputs = confctl.lib.mkConfctlOutputs {
        confDir = ./.;
        inherit inputs;
        channels = {
          first = { nixpkgs = "nixpkgs"; raw = "rawFirst"; alias = "rawAlias"; };
          later = { raw = "rawLater"; };
        };
      };
    in {
      confctl = outputs;
      smoke = {
        inherit (outputs) settings machineNames machineKeys buildPlan inputs;
        moduleOptions = outputs.moduleOptions;
        sources = {
          first = inputs.rawFirst.outPath;
          later = inputs.rawLater.outPath;
          override = inputs.rawOverride.outPath;
          alias = inputs.rawAlias.outPath;
        };
      };
    };
}
'''
flake = flake.replace('@CONFCTL_URL@', json.dumps('path:' + str(source)))
flake = flake.replace('@NIXPKGS_URL@', json.dumps('path:' + str(nixpkgs)))
(cluster / 'flake.nix').write_text(flake)
PY

"${smoke_nix[@]}" flake lock "$smoke_cluster"
smoke_fixture_lock_before=$(sha256sum "$smoke_cluster/flake.lock")
"${smoke_nix[@]}" eval --json --no-write-lock-file --no-update-lock-file \
  "$smoke_cluster#smoke" > "$smoke_fixture/evaluation.json"

(
  cd "$smoke_cluster"
  bundle exec ruby "$smoke_repo/bin/confctl" ls -L > "$smoke_fixture/metadata-columns.txt"
  bundle exec ruby - "$smoke_fixture" <<'RUBY'
require 'confctl'
require 'confctl/cli'
require 'json'

fixture = ARGV.fetch(0)
ConfCtl::Logger.open('smoke', output: $stderr)
nix = ConfCtl::Nix.stateless
paths = nix.eval_host_inputs(%w[nested/later nested/overridden])
command = ConfCtl::Cli::Cluster.new({ color: 'never' }, {}, [])
groups = command.send(:input_build_groups, paths, nix)
raise 'conflicting raw role paths must form separate legacy NIX_PATH groups' unless groups.length == 2

eval_args = ConfCtl::Nix::Args.new(settings: nix.confctl_settings).eval_args
raise 'impure evaluation argument missing' unless eval_args.include?('--impure')
raise 'lock write guard missing' unless eval_args.include?('--no-write-lock-file')
raise 'lock update guard missing' unless eval_args.include?('--no-update-lock-file')

legacy = %w[nested/later nested/overridden].to_h do |name|
  [name, nix.send(:legacy_nix_path_args, [name])]
end
File.write(File.join(fixture, 'legacy-args.json'), JSON.generate(eval_args: eval_args, legacy: legacy))
RUBY
)

python3 - "$smoke_fixture" <<'PY'
import json
import pathlib
import subprocess
import sys

fixture = pathlib.Path(sys.argv[1])
evaluation = json.loads((fixture / 'evaluation.json').read_text())
sources = evaluation['sources']
plans = evaluation['buildPlan']
assert sources['first'] == sources['alias'], 'follows must resolve the same source path'
assert set(evaluation['machineNames']) == {'nested/later', 'nested/overridden'}
assert plans['nested/later']['inputs']['raw'] == sources['later'], 'later channel must override the first'
assert plans['nested/overridden']['inputs']['raw'] == sources['override'], 'machine override must win'
for name, plan in plans.items():
    assert plan['inputs']['alias'] == sources['first']
    assert evaluation['inputs'][evaluation['machineKeys'][name]] == plan['inputs']
    assert plan['inputsInfo']['raw']['rev'] is None, 'raw paths need no Git revision'
    assert 'swpins' not in plan
names = {option['name'] for option in evaluation['moduleOptions']}
assert 'cluster.<name>.smokeTag' in names, 'custom cluster options must be documented'
assert not any('swpin' in name for name in names), 'pin options must be absent'
columns = (fixture / 'metadata-columns.txt').read_text().splitlines()
assert 'smokeTag' in columns, 'actual confctl ls -L must list custom metadata'
settings = evaluation['settings']['nix']
assert settings['impureEval'] is True and settings['legacyNixPath'] is True
args = json.loads((fixture / 'legacy-args.json').read_text())
for machine, expected in [('nested/later', 'later'), ('nested/overridden', 'override')]:
    legacy = args['legacy'][machine]
    assert len(legacy) == 4 and legacy[0] == '-I' and legacy[2] == '-I'
    command = ['nix', '--extra-experimental-features', 'nix-command flakes', 'eval', '--json']
    command += args['eval_args'] + legacy + ['--expr', 'import <raw>']
    result = subprocess.check_output(command, cwd=fixture / 'cluster-config', text=True)
    assert json.loads(result)['marker'] == expected, 'legacy -I mapping must evaluate the selected raw role'
print('PASS: custom ls -L, raw path inputs, follows, channel precedence, overrides, machine keys, impure args and legacy NIX_PATH evaluation')
PY

test "$smoke_fixture_lock_before" = "$(sha256sum "$smoke_cluster/flake.lock")"
test "$smoke_lock_before" = "$(sha256sum "$smoke_repo/flake.lock")"
printf 'PASS: repository and disposable lock files were unchanged by evaluation\n'
printf 'Evidence retained at %s\n' "$smoke_fixture"
