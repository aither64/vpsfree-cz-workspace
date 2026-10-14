# Selected KB capture verification

Prepared only. Independent final source review and lead clearance come first.
No cluster, capture, wiki or staging command has been executed by implementer0.
The source pipeline ends at K `ef72876da07dae61449502e2d03856d1d3b133e4`
and vpsAdmin `6b3628af665049dc095ba985ef0fbe8a22286863` before review fixes.
Replace both command arguments with the exact reviewed heads if review changes them.

## Impact and scope

Regenerate only `networking/ip-address-list`, Czech and English. The new
Enabled column appears in every inventory row, so green semantic contract
checks do not establish unchanged screenshots. Preserve semantic IDs, page
bindings, fingerprints and the existing PNG/media filenames:

- `screenshots/cs/networking/ip-address-list.png`, used by `navody:vps:ip_adresy`;
- `screenshots/en/networking/ip-address-list.png`, used by `manuals:vps:ip_addresses`.

Both manifest variants are currently pending and can be replaced through the
normal capture workflow. No page prose or new screenshot concept is needed.
Inspect the resulting Enabled/Povoleno column, complete rows, controls, crop,
fonts and documentation-safe fixture values before accepting generated hashes.

The adjacent routed-addresses and interface-addresses captures select their
existing forms in `scenarios/networking.cjs:15` and `:21`. They add no visual
availability column. Their free-address selectors use the new optional filter,
which retains the same visible candidates with the default enabled fixtures.
The reverse-DNS capture selects its separate existing form. Traffic captures
are unaffected. A checkpoint selection writes only the selected bitmap, though
the scenario still visits these adjacent pages and checks the two forms.

## Cluster and tooling prerequisites

Read K `AGENTS.md`, `docs/webui-change-workflow.md`, `README.md`, full
`bin/devcluster`, the workspace session/lifecycle/verification procedures and
the installed vpsAdmin provider guide before cluster preparation. The current
installed catalog exposes `vpsadmin` and `vpsadminos`, not a KB provider.
K's repository-owned helper uses its own ignored `.devcluster` state. It is
not covered by the installed providers' workspace/socket ownership records or
package-transition gate. Do not register it as another provider or copy a
provider ownership record to make it look adopted.

Supported execution is blocked. Architect inspection confirmed that K's helper
does not satisfy the current lifecycle generation/socket ownership contract.
A fresh slug, absent local state and read-only collision preflight do not make
it safe. Its start calls `kill_socket_processes` and removes a workspace-independent
slug socket directory even without force. Do not start this helper. No package,
provider, helper or ownership-record change is authorized in this initiative.

The configured bridge is `br0`, services is `172.16.106.53`, and screenshots
topology includes nodes `.41`, `.42` and storage `.45`. Require `/dev/kvm`
access, executable `/run/wrappers/bin/qemu-bridge-helper`, its allowed bridge,
and working resolution for the K development hostnames to the owned services
VM. Confirm all guest addresses, not only the helper's services ping. Do not
stop another initiative's bridge cluster. Local mode requires separate lead
coordination if the bridge is genuinely unavailable; this prepared operation
accepts bridge only.

The prerequisite is a supported, session-owned execution environment that can
run these repository fixtures at the exact reviewed source revision while
meeting the current lifecycle generation and socket ownership contract.
Lead must resolve that environment outside this source task before assigning
capture execution. The `screenshots` topology is supported dynamically; the
helper's usage text omits it, which is separate from the ownership defect.
There is no proposed start command or automatic stop/reset. The capture wrapper
has no lifecycle or cleanup trap and remains unlaunched.

Fixtures require `base-vps` and `traffic-samples`: an enabled `Debian (latest)`
template, seeded `test-user1`, Production/Praha selection, its documentation
VPS, public interface address and reverse-record route, mounted `data` child,
and the preseeded NAS on `backuper1`. Fixture preparation may create these owned
objects through normal API actions and generate pings. It does not disable a
network. The pinned shell provides Chromium, Playwright, Node and Liberation
fonts; viewport is 1440 by 1100, scale 1, with Czech/English locales and
Europe/Prague timezone. No browser download or ambient npm install is needed.

K retains its existing vpsAdminOS override `6bdf458fd9105379860234ff33d352e55844f08f`.
No kernel input/configuration changes are part of this feature. The fresh
watcher must stop an unexpected local Linux kernel build and report the
derivation/cache miss to the lead, under the workspace verification procedure.
Cancellation is confined to that watcher's command; cancelling capture does
not authorize stopping the separately owned cluster or removing its state.

## Exact capture and validation operation

After review and resolution of the supported-environment blocker, revalidate
the capture wrapper's runtime contract before assigning a fresh Luna/low
watcher. The prepared command from the K worktree is:

```sh
DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
nix develop --command bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/run-network-kb-captures.sh \
  ef72876da07dae61449502e2d03856d1d3b133e4 \
  6b3628af665049dc095ba985ef0fbe8a22286863
```

The wrapper verifies exact clean K/V pin records, the live runner's user and
config/state/socket/PID/readiness tuple, screenshots topology and bridge mode.
It compares the actually served inventory PHP source in the webui guest with
the locked source before capture. A manifest/lock match alone does not prove
that a running guest has loaded that source. Its runtime check does not certify
the entire deployed API; normal capture exercises the isolated current API.

For each language it runs `bin/capture --scenario networking --checkpoint
networking/ip-address-list`, saves that language's result, and immediately runs
`bin/validate --update` then strict `bin/validate`. Each capture replaces
`tmp/capture-results.json`, so deferring update until both languages finish
would lose the first result. It then runs `bin/check`, creates both existing
networking contact sheets and checks that only the two selected variants'
dimensions, SHA-256 and capture provenance changed in the manifest. Only
`captures.json` and the two selected PNGs may change. Logs/results/sheets go
beneath the tracking `post-review-kb-ip-address-list` directory.

After completion, implementer/lead inspect both full images and contact sheets,
retain existing semantic/page bindings, and commit the three generated paths
through normal K guidance/hooks. Reconcile exact image checksums and branch
history in the final packet. Do not mark captures reviewed or uploaded based
only on command success. No production/staging write or upload is included.
