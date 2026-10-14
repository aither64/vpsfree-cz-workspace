#!/usr/bin/env bash
# Prepared operation only. Lead must clear final review and ready-cluster ownership.
# Invoke from K's pinned Nix shell; this script never starts or stops a cluster.
set -euo pipefail

workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-05-network-ipv4-left-counter
tracking="$workspace/work/$slug"
repo="$workspace/worktrees/$slug/vpsfree-kb-contracts"
expected_k=${1:?provide the independently reviewed exact K head}
expected_v=${2:?provide the independently reviewed exact vpsAdmin head}
[[ $# == 2 && $expected_k =~ ^[0-9a-f]{40}$ && $expected_v =~ ^[0-9a-f]{40}$ ]]
[[ ${DEV_SESSION_SLUG-} == "$slug" && ${DEV_SESSION_WORKSPACE-} == "$workspace" ]]
cd "$tracking"
[[ $(dev-session current) == "$slug" ]]
cd "$repo"
[[ $(git rev-parse HEAD) == "$expected_k" ]]
[[ $(git branch --show-current) == "$slug" ]]
[[ -z $(git status --porcelain) ]]
: "${VPSADMIN_KB_VPSADMIN_SOURCE:?enter the K pinned Nix shell}"
[[ $(jq -r .vpsadmin_commit captures.json) == "$expected_v" ]]
[[ $(jq -r '.nodes[.nodes.root.inputs.vpsadmin].locked.rev' flake.lock) == "$expected_v" ]]

out="$tracking/post-review-kb-ip-address-list"
[[ ! -e $out ]] || { printf 'Artifact directory already exists; inspect before retry.\n' >&2; exit 1; }
mkdir -m 700 "$out"
cp captures.json "$out/captures-before.json"

check_runner() {
  node - "$repo" "$slug" <<'JS'
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const [repo, slug] = process.argv.slice(2);
const dir = path.join(repo, '.devcluster/clusters', slug);
if (fs.realpathSync(dir) !== dir) throw new Error('Unexpected cluster directory identity');
for (const name of ['ready', 'runner.pid', 'config.json']) {
  const file = path.join(dir, name);
  const info = fs.lstatSync(file);
  if (!info.isFile() || info.uid !== process.getuid()) throw new Error(`Unowned ${name}`);
}
if (fs.readFileSync(path.join(dir, 'network'), 'utf8').trim() !== 'bridge') {
  throw new Error('This prepared operation requires the owned bridge cluster');
}
if (fs.readFileSync(path.join(dir, 'topology'), 'utf8').trim() !== 'screenshots') {
  throw new Error('This prepared operation requires screenshots topology');
}
const pid = fs.readFileSync(path.join(dir, 'runner.pid'), 'utf8').trim();
if (!/^[1-9][0-9]*$/.test(pid)) throw new Error('Invalid runner PID');
if (fs.statSync(`/proc/${pid}`).uid !== process.getuid()) throw new Error('Runner user mismatch');
const argv = fs.readFileSync(`/proc/${pid}/cmdline`, 'utf8').split('\0');
const digest = crypto.createHash('sha256').update(slug).digest('hex').slice(0, 12);
for (const [option, value] of [
  ['--state-dir', path.join(dir, 'state')],
  ['--sock-dir', `/tmp/vpsfree-devcluster-${digest}`],
  ['--pid-file', path.join(dir, 'runner.pid')],
  ['--ready-file', path.join(dir, 'ready')],
  ['--config', fs.realpathSync(path.join(dir, 'result-config'))],
]) {
  if (argv.filter(arg => arg === option).length !== 1 || argv[argv.indexOf(option) + 1] !== value) {
    throw new Error(`Runner tuple mismatch: ${option}`);
  }
}
JS
}

run_step() {
  local label=$1
  shift
  local status=0
  "$@" >"$out/$label.log" 2>&1 || status=$?
  printf '%s\n' "$status" >"$out/$label.exit"
  [[ $status == 0 ]] || { printf '%s failed with exit %s; inspect the retained log.\n' "$label" "$status" >&2; return "$status"; }
}

check_runner
run_step runtime-webui-source bin/devcluster ssh "$slug" services -- \
  nixos-container run webui -- sha256sum /run/vpsadmin-live-webui/forms/networking.forms.php
read -r served_hash _ <"$out/runtime-webui-source.log"
read -r pinned_hash _ < <(sha256sum "$VPSADMIN_KB_VPSADMIN_SOURCE/webui/forms/networking.forms.php")
[[ $served_hash == "$pinned_hash" ]] || { printf 'Served PHP source differs from the pinned source.\n' >&2; exit 1; }

for language in cs en; do
  check_runner
  run_step "capture-$language" bin/capture --cluster "$slug" --language "$language" \
    --scenario networking --checkpoint networking/ip-address-list
  cp tmp/capture-results.json "$out/capture-results-$language.json"
  run_step "validate-update-$language" bin/validate --update
  run_step "validate-$language" bin/validate
done

node - "$out/captures-before.json" captures.json <<'JS'
const fs = require('fs');
const assert = require('assert/strict');
const [before, after] = process.argv.slice(2).map(file => JSON.parse(fs.readFileSync(file)));
for (const manifest of [before, after]) {
  const asset = manifest.assets.find(item => item.id === 'networking/ip-address-list');
  for (const language of ['cs', 'en']) {
    for (const field of ['dimensions', 'sha256', 'capture']) delete asset.variants[language][field];
  }
}
assert.deepEqual(after, before, 'Capture update changed unrelated inventory or semantic bindings');
JS
run_step contract-check bin/check
for language in cs en; do
  run_step "contact-sheet-$language" bin/contact-sheet networking "$language"
  cp "tmp/contact-sheet-$language-networking.png" "$out/"
done
git diff --check
git diff --name-only >"$out/changed-paths.txt"
while IFS= read -r changed; do
  case "$changed" in
    captures.json|screenshots/cs/networking/ip-address-list.png|screenshots/en/networking/ip-address-list.png) ;;
    *) printf 'Unexpected changed path: %s\n' "$changed" >&2; exit 1 ;;
  esac
done <"$out/changed-paths.txt"
git diff -- captures.json >"$out/capture-manifest.diff"
printf 'Bilingual capture and validation completed; inspect images before committing.\n'
