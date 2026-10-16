# Private native-mapped store fixture correction

Frozen, unstaged suite-only change on reviewed/published
`67e3f88c9e60d1d7cc9c3cb8685e68fa47bdd7a5`, tree
`b3390be05ce2875101e34168e94775bb20d23234`. Session identity and live
retained roster revision 18 match; implementer0 retains Sol/xhigh and
workspace_write. Index empty; no other product path changed.

## Established cause and limits

Attempt `runtime-attempt.gv8q4a89` selected only upgrade-26.05, exited 1
with unexpected_failure, and retained `/tmp/ni.boon4yad`. The VM is stopped.
The old initial generation starts, but its readiness wait times out before
registration, old live switches or any preservation assertion. The diagnostic
wrapper records actual failed services and re-raises that original timeout.

`machine-shell.log:170-194` proves the host overlay store was shared with
map_ids=false, while the container is native with ns0 -> host1000000 and
its private `/nix` source has map_ids=true. Lines 3094-3096 show native maps
for ephemeral root, private `/nix`, and persistent root; there is no mapped
store source. The latter read-only bind overrides the mapped `/nix/store`
location with ordinary host IDs. Host root is outside the guest ID range.

`machine-shell.log:1032-1060` explicitly reports logrotate rejecting its
store configuration owner: it requires uid0. This is a concrete fixture
ownership-contract violation, before the behavior under test. The lead's
native read-only stat confirms host executable owners 0:0/mode555 and
configuration owner 0:0/mode444. My restricted tool namespace maps only the
caller UID/GID and displays these host-root owners as 65534; that view is
not additional native host ownership evidence.

The same diagnostics show nsncd/dhcpcd EXEC EACCES and dbus-broker's child
launch EACCES; dbus.socket fails after broker start limits. The old generated
units retain their actual User/Group and hardening, including NoNewPrivileges,
ProtectSystem and private mounts. Nothing here proves the exact kernel/service
permission path for every EXEC failure. No store noexec finding is established;
the logged noexec option belongs to the host's BPF filesystem. Those EXEC
failures remain runtime uncertainty until the corrected store fixture runs.
There is no justification to change services or accept degraded readiness.

## Existing source contract and change

The declarative NixOS setup at `os/modules/osctl/containers/nixos.nix:173-185`
copies closureInfo store-paths with cp -a while stopped; lines 208-215 supply
nix-path-registration and configure the system profile. The native map test
`tests/suite/osctl/ct-map-mode.nix` expects host private files 0:0 to appear
as guest 0:0, for both root and subdataset. CtPreMount calls map_and_push for
every map_ids mount; SharedDir uses util-linux X-mount.idmap with the actual
container user namespace. Native storage remains unshifted on disk.

Only `tests/suite/dist-config/nixos-persistence-upgrade.nix` changes:

- Build per-variant closureInfo from exactly that variant's existing generation
  roots and failure generations. Retain all roots as host extraDependencies
  and retain the corresponding closureInfo outputs there.
- Remove the unmapped host-overlay `/nix/store` bind.
- Before first boot, copy just that variant's closure paths with cp -a into
  the existing queried native-mapped `/nix` dataset private store. Copy its
  registration data to `/nix/nix-path-registration` there. No whole host-store
  copy, ID shift, ownership repair, remapping bypass or new API.
- At the original registration position, load that private registration file.

Source ownership/modes are preserved by the existing copy convention. No
guest definitions, releases, software, stateVersion, account/storage settings,
readiness/diagnostic semantics, switches or acceptance assertions change.
Profile/init seeding stays on its correct private source. All original
identity/map/payload/machine-id/metadata/mount checks and negative allocator
controls remain. This is test setup only, with no product guide change needed.

## Static evidence and dependent verification

`store-fixture.patch` is the exact 20-addition/6-deletion product diff.
`prepare-static-evidence.py` checks six explicit expected replacements and
reverses them to recover HEAD byte-for-byte. `scope-comparison.txt` records
both passing comparisons. `original-logs.json` hashes every retained log
and attempt metadata; all original hashes remain unchanged. Source/runtime
excerpts and actual old units are in `source-and-runtime-evidence.txt` and
`old-guest-units.txt`. Original artifacts remain in their original locations.

Parser, prepared nixfmt --check, prepared Ruby -c on the static combined
template, Bash -n on the copy fragment, and git diff --check all exited 0.
Static templates use inert Nix path placeholders, not an evaluated script.
No Nix evaluation/build/runtime, staging/commit/ref/push or lifecycle action
was performed. See `static-checks.txt` for exact commands and source hash.

Parent-owned next commands, from the product worktree, through its watcher:

```sh
./test-runner.sh ls 'dist-config/nixos-persistence-upgrade*'
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-store-fixture-diagnosis/generated-scripts.nix
nix develop --profile result/config-imports-dev-shell --command overcommit --run
```

The session evaluator exports all eight actual registered script strings for
prepared Ruby -c checks; it is not a new runner. Its evaluation has not been
executed. Product pure-check inputs and raw modules are unchanged. Use the
normal existing committed-review and runtime wrapper after quick verification
and folding; prepare a new owned attempt/state directory, metadata and exact
reviewed-head clearance, then run the ordinary `test-runner.sh test` with
`dist-config/nixos-persistence-upgrade#upgrade-26.05` first. The subsequent
full acceptance selection is `dist-config/nixos-persistence-upgrade#*`.
Preserve failed attempts and original directories; do not reuse or overwrite
their invocation/log/status records.

Success still requires healthy old boot, old live switches, candidate
adoption, repeat activation and restart with every preservation assertion.
Neither syntax checks nor correcting one established fixture defect proves
upgrade acceptance. The parent owns folding, review and runtime evidence.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-streamline-vpsadminos-config-imports/
