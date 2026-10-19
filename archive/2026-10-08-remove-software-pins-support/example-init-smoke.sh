#!/usr/bin/env bash
set -euo pipefail
fixture_repo=${1:?confctl worktree}
fixture_base=${2:?completed custom smoke directory}
fixture_source="$fixture_base/confctl-source"
export BUNDLE_GEMFILE="$fixture_repo/Gemfile" RUBYLIB="$fixture_repo/lib"
export CONFCTL_TTY=0 NO_COLOR=1 PAGER=
fixture_nixpkgs=$(nix eval --raw --impure --expr "(builtins.getFlake \"path:$fixture_source\").inputs.nixpkgs.outPath")
fixture_vpsadminos=$(nix eval --raw --impure --expr "(builtins.getFlake \"path:$fixture_source\").inputs.vpsadminos.outPath")
cp -r "$fixture_source/example" "$fixture_base/renamed-example"
chmod -R u+w "$fixture_base/renamed-example"
mkdir "$fixture_base/initialized"
(
  cd "$fixture_base/initialized"
  bundle exec ruby "$fixture_repo/bin/confctl" init
  bundle exec ruby "$fixture_repo/bin/confctl" add nested/smoke
)
python3 - "$fixture_base" "$fixture_source" "$fixture_nixpkgs" "$fixture_vpsadminos" <<'PY'
import json
from pathlib import Path
import sys
base, source, nixpkgs, vpsadminos = sys.argv[1:]
for name in ('renamed-example', 'initialized'):
    file = Path(base) / name / 'flake.nix'
    text = file.read_text()
    old = 'path:..' if name == 'renamed-example' else 'github:vpsfreecz/confctl'
    text = text.replace('confctl.url = '+json.dumps(old)+';', 'confctl.url = '+json.dumps('path:'+source)+';')
    text = text.replace('nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";', 'nixpkgs.url = '+json.dumps('path:'+nixpkgs)+';')
    text = text.replace('vpsadminos.url = "github:vpsfreecz/vpsadminos/staging";', 'vpsadminos.url = '+json.dumps('path:'+vpsadminos)+';')
    file.write_text(text)
PY
for fixture_name in renamed-example initialized; do
  fixture_dir="$fixture_base/$fixture_name"
  git -C "$fixture_dir" init --quiet
  git -C "$fixture_dir" add .
  nix flake lock "path:$fixture_dir"
  git -C "$fixture_dir" add flake.lock
  fixture_lock_before=$(sha256sum "$fixture_dir/flake.lock")
  nix eval --json --no-write-lock-file --no-update-lock-file "path:$fixture_dir#confctl.machineNames" > "$fixture_dir/names.json"
  nix eval --json --no-write-lock-file --no-update-lock-file "path:$fixture_dir#confctl.machineKeys" > "$fixture_dir/keys.json"
  nix eval --json --no-write-lock-file --no-update-lock-file "path:$fixture_dir#confctl.buildPlan" > "$fixture_dir/plan.json"
  (
    cd "$fixture_dir"
    bundle exec ruby "$fixture_repo/bin/confctl" ls > listing.txt
    bundle exec ruby "$fixture_repo/bin/confctl" ls -L > columns.txt
    bundle exec ruby "$fixture_repo/bin/confctl" inputs ls > inputs.txt
  )
  test "$fixture_lock_before" = "$(sha256sum "$fixture_dir/flake.lock")"
done
python3 - "$fixture_base" <<'PY'
import json
from pathlib import Path
import sys
base = Path(sys.argv[1])
expected = {
    'renamed-example': {'nixos-machine', 'nested/nixos-machine'},
    'initialized': {'nested/smoke'},
}
for name, names in expected.items():
    folder = base / name
    assert set(json.loads((folder/'names.json').read_text())) == names
    keys = json.loads((folder/'keys.json').read_text())
    plan = json.loads((folder/'plan.json').read_text())
    assert set(keys) == set(plan) == names
    assert len(set(keys.values())) == len(names)
    for machine in names:
        assert machine in (folder/'listing.txt').read_text()
        assert 'nixpkgs' in plan[machine]['inputs']
        assert 'swpins' not in plan[machine]
    assert 'spin' in (folder/'columns.txt').read_text()
    assert 'nixpkgs' in (folder/'inputs.txt').read_text()
print('PASS: renamed example and actual init/add clusters evaluate and list machines/keys/inputs/metadata without updating locks')
PY
