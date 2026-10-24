#!/usr/bin/env bash
set -Eeuo pipefail

readonly repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/haveapi
readonly expected_head=349aacd53790c6c820fe2dacc8cb6d151c92d0fc
readonly expected_tree=c80eaddb6e42633d154c15b020e4e74b9faa8d76
export EXPECTED_HEAD="$expected_head"
export BASELINE=f94e65e35166a0bf8048a27c9d57c7d36957d65b
: "${OUT:?Export an absolute fresh owned /tmp/2026-10-19-haveapi-async-client-release-smoke.* directory}"
[[ "$OUT" == /tmp/2026-10-19-haveapi-async-client-release-smoke.* && -d "$OUT" && -O "$OUT" && ! -L "$OUT" ]]
[[ "$(realpath "$OUT")" == "$OUT" && -z "$(find "$OUT" -mindepth 1 -print -quit)" ]]
export OUT
readonly started=$SECONDS
printf 'OUT=%s\n' "$OUT"
exec > "$OUT/operation.log" 2>&1
cd "$repo"
finish() {
  local rc=$?
  trap - EXIT
  set +e
  git status --porcelain=v1 > "$OUT/status-after.txt"
  git rev-parse HEAD HEAD^{tree} > "$OUT/identity-after.txt"
  if [[ $rc == 0 ]] && { [[ -s "$OUT/status-after.txt" ]] || [[ "$(git rev-parse HEAD)" != "$expected_head" ]] || [[ "$(git rev-parse HEAD^{tree})" != "$expected_tree" ]]; }; then rc=74; fi
  printf '%s\n' "$rc" > "$OUT/operation.exit"
  printf '%s\n' "$((SECONDS - started))" > "$OUT/elapsed-seconds.txt"
  date -u +'%Y-%m-%dT%H:%M:%SZ' > "$OUT/finished-utc.txt"
  exit "$rc"
}
trap finish EXIT
date -u +'%Y-%m-%dT%H:%M:%SZ' > "$OUT/started-utc.txt"
cp -- "${BASH_SOURCE[0]}" "$OUT/proof-script.sh"
sha256sum "$OUT/proof-script.sh" > "$OUT/proof-script.sha256"
[[ "$(dev-session current)" == 2026-10-19-haveapi-async-client ]]
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  [[ "${DEV_SESSION_SLUG:-}" == 2026-10-19-haveapi-async-client && "${DEV_SESSION_WORKSPACE:-}" == /home/aither/workspace/ai/vpsfree.cz ]]
fi
git status --porcelain=v1 > "$OUT/status-before.txt"
git rev-parse HEAD HEAD^{tree} > "$OUT/identity-before.txt"
[[ ! -s "$OUT/status-before.txt" && "$(git rev-parse HEAD)" == "$expected_head" && "$(git rev-parse HEAD^{tree})" == "$expected_tree" ]]
cat > "$OUT/inputs.sha256" <<'HASHES'
922570e28119697ac47ab550f951e5badb9915f41bfaab6b9015d3a942c06254  flake.lock
3a39c0b607d79756aee34adaf67f98bfdca8bd35027398aea165515f7e34e71b  clients/js/package.json
1c7f66cccadc6abf9474d3403db38ce524aa49d3352efb19596aa86ffeaaaec6  clients/js/package-lock.json
f52e29eefd771f5a5147f35bd1b82b602075b88e2c57cf82bbfc311f64b6c1ac  clients/js/gulpfile.js
979e91b63f0c070f6445933605b03e054d25c850e74779186f78997f42b783b4  clients/js/tsconfig.json
4966047366e2cec83e1be3443517712c0b5c361bd58b4b324277ca36c9f9fb69  utils/release/artifacts.rb
73e1964b419c815963af6124edee36ed23686d73cc52b31f01c24bc7431cfae2  utils/release/npm-consumer.ts
c618cc8c0e97734340ce323504ad986cde595649926024687c89bdc241f0948b  clients/js/node_modules/.package-lock.json
8d5fa5bd883fec0979fc2004f1fe1d99aef40570155d550eadc0b03b55513bf0  clients/js/node_modules/typescript/bin/tsc
822ef7ca6452205657b6288b066481ecf508bfbf43455d715cf7d3ec457561e6  clients/js/node_modules/typescript/package.json
2cffde0b8c6760dfb0b5b0382bbb7e00ba6a8b2d981b9205b256a700a481d983  clients/js/node_modules/typescript/lib/tsc.js
e8f349eabd48486bdb2bf9dc1a00c89d58297270c54b745838879e2859194419  clients/js/node_modules/typescript/lib/_tsc.js
036cd852cf02c7a55c901c4aa87c9358cc12379252b09add73e083d6983a398f  clients/js/node_modules/rollup/dist/bin/rollup
d15b18cf4101c4795549e7b3a2c4c89aff2e7b86276463a3ceddd56e79348813  clients/js/node_modules/rollup/package.json
defe1e406d4a3cf5771901efd54e71c11f83d10d065ebac85092417200f45d7f  clients/js/node_modules/gulp/bin/gulp.js
a07364a32fc8ef7706f2b3289fa211a39c69163fec7de4b27592205f3ca2ef21  clients/js/node_modules/gulp/package.json
HASHES
sha256sum --check "$OUT/inputs.sha256" > "$OUT/inputs-before.log"
printf '%s\n' 'nix develop --command bash -Eeuo pipefail (exact heredoc retained in proof-script.sh)' > "$OUT/command.txt"
nix develop --command bash -Eeuo pipefail <<'SHELL' 2>&1 | tee "$OUT/nix.log"
set -x
phase=tools
trap 'rc=$?; printf "%s\n" "$rc" > "$OUT/$phase.exit"' EXIT
{ command -v node npm ruby; node --version; npm --version; ruby --version; sha256sum "$(command -v node)" "$(readlink -f "$(command -v npm)")"; } > "$OUT/tools.txt"
printf '0\n' > "$OUT/$phase.exit"
phase=build
(cd clients/js && npm run build) 2>&1 | tee "$OUT/build.log"
printf '0\n' > "$OUT/$phase.exit"
[[ -z "$(git status --porcelain=v1)" ]]
phase=pack
(cd clients/js && npm pack --ignore-scripts --json --pack-destination "$OUT") > "$OUT/npm-pack.json" 2> "$OUT/pack.stderr"
cp clients/js/dist/haveapi-client.js "$OUT/haveapi-client.js"
printf '0\n' > "$OUT/$phase.exit"
phase=inventory
ruby -r ./utils/release/artifacts.rb <<'RUBY' 2>&1 | tee "$OUT/inventory.log"
include HaveAPI
out, head, baseline = ENV.values_at('OUT', 'EXPECTED_HEAD', 'BASELINE')
artifacts = Release::Artifacts.new(Dir.pwd)
pack = JSON.parse(File.read(File.join(out, 'npm-pack.json')))
raise 'Unexpected npm pack result' unless pack.size == 1 && pack.first.fetch('filename') == "haveapi-client-#{artifacts.version}.tgz"
path = File.join(out, pack.first.fetch('filename'))
files = artifacts.tar_files(path, gzip: true)
runtime = files.keys.grep(%r{\Apackage/dist/}).map { |name| name.delete_prefix('package/') }.sort
expected = Release.capture('git', 'ls-tree', '-r', '--name-only', baseline, '--', 'clients/js/dist').lines.map { |name| name.strip.delete_prefix('clients/js/') }.sort
raise 'Runtime/declaration inventory differs from f94' unless runtime == expected && runtime.size == 45 && files.size == 51
changes = []
inventory = files.sort.map do |name, (content, _mode)|
  raise 'Unexpected package prefix' unless name.start_with?('package/')
  relative = name.delete_prefix('package/')
  current = Release.capture('git', 'show', "#{head}:clients/js/#{relative}").b
  old = Release.capture('git', 'show', "#{baseline}:clients/js/#{relative}").b
  raise "Packed file differs from final commit: #{relative}" unless content.b == current
  changes << relative unless content.b == old
  { path: relative, bytes: content.bytesize, sha256: Digest::SHA256.hexdigest(content), matches_f94: content.b == old }
end
raise "Unexpected packed changes from f94: #{changes}" unless changes == ['README.md']
integrity = "sha512-#{Digest::SHA512.file(path).base64digest}"
raise 'npm integrity differs from actual tar bytes' unless integrity == pack.first.fetch('integrity')
raise 'Standalone bundle differs' unless File.binread(File.join(out, 'haveapi-client.js')) == files.fetch('package/dist/haveapi-client.js').first
result = { head: head, baseline: baseline, sha256: Digest::SHA256.file(path).hexdigest, integrity: integrity, bytes: File.size(path), changed_from_f94: changes, files: inventory }
File.write(File.join(out, 'inventory.json'), "#{JSON.pretty_generate(result)}\n")
puts "Packed 51 files; runtime + 44 declarations identical to f94; only README changed; SHA256 #{result.fetch(:sha256)}"
RUBY
printf '0\n' > "$OUT/$phase.exit"
phase=smoke
ruby -r ./utils/release/artifacts.rb -e 'HaveAPI::Release::Artifacts.new(Dir.pwd).smoke_npm(ENV.fetch("OUT"))' 2>&1 | tee "$OUT/smoke.log"
printf '0\n' > "$OUT/$phase.exit"
phase=postcheck
sha256sum --check "$OUT/inputs.sha256" > "$OUT/inputs-after.log"
[[ -z "$(git status --porcelain=v1)" && "$(git rev-parse HEAD)" == "$EXPECTED_HEAD" ]]
SHELL
