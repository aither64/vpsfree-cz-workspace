# H0 host launcher source package

Owner: implementer3. Lead released the isolated source package after architect0
accepted architect1's pi-host-launcher-plan.md and its Frozen v1 section.
This is candidate source and fake-check evidence. No host installation,
unit/policy activation, user-profile switch, live auth/model call, merge,
or session lifecycle action occurred.

## Scope and lineage

Investigated D base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
Source began atop P0 commit `ab9ce9234fe2b1f80367b7bb1836a81925b2a034`;
current P0-resume head before H0 commit is
`0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`.
H0 commit/head: `23b35d5368a27bd189ef7b895dbbfbde4dc0d331`, parent
`0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`. Lead granted the short index
window; exactly the ten owned paths were committed with normal `git commit -F
--only` handling. Index was empty before/after and owned paths are clean.
No declared hook framework, core.hooksPath or active non-sample hook exists.
D window closed and exact full head/parent reported to lead; an earlier report
contained a mistaken unverified full SHA and was explicitly corrected.
No migrations, old-state rewrites or history conversion. New launch/receipt
schemas are opt-in version 1; existing Codex paths and authorities are unchanged.

Owned files: `libexec/workspace-pi-host`, `workspace-pi-session-entry`,
`nix/pi-runtime-host.nix`, `pi-runtime-host-package.nix`,
`nix/tests/pi-runtime-host.nix`, `test/pi_runtime_host_test.rb`,
`test/fixtures/pi-host-launch-v1.json` and `.sha256`,
`docs/pi-runtime-host.md`. Existing `nix/host-module.nix` gains only the isolated
module import. Shared P0/P2/central entrypoints/pins/top-level exports untouched.

## Contracts and documentation

The fixed template uses the configured original User/primary group/initgroups,
original host user namespace and fixed disk scratch mounts. Root executes only
immutable host parser code. The payload selects the exact retained application
from the fixed feature manifest after UID drop. Native Running is not supervisor
readiness or installed Launch-ready. Exact-byte SHA256 is external to the JSON.
Durable intent precedes start; retained IDs never start twice. Terminal replay
precedes current descriptor lookup. A successor needs new request/generation,
matching stable scope and freshly proven predecessor drain.

Documentation placement: operator/runtime developer API, storage, contract,
permission/compatibility and recovery explanation lives in D
`docs/pi-runtime-host.md`. Individual check/rollout facts stay here. No site
configuration or deployment receipt was added to owning project docs.

## Quick checks

- D Nix environment: `nix develop --command ruby test/pi_runtime_host_test.rb`:
  17 tests, 72 assertions, zero failures/errors/skips; latest 0.69 seconds.
  Intent ordering, lost start reply/pre-call crash Unknown, read-only inspect,
  byte/schema/path/capability refusal, stale stop, empty versus unknown cgroup,
  terminal replay/successor guards, publication lock, receipt I/O failure and
  unprivileged fixed exec/standalone load are covered with disposable fakes.
- Nix parse: new package, module and VM definition pass.
- Enabled/disabled module and actual generated unit evaluated using pinned D
  nixpkgs with a configured `/srv/developer` home. Disabled unit absent;
  enabled User/Group/PrivateUsers/PrivateMounts/bind roots/stop and exact-store
  sudo policy match the brief. Ordinary evaluation emitted only expected root
  filesystem/bootloader assertions from the intentionally nonbootable fixture.
- VM test and fake payload Python compile through AST extraction; not executed.
- Owned whitespace and existing import diff pass checks.
- Fresh installed-catalog Luna/low full-access utility built the isolated tools
  derivation in 4s and syntax-checked both packaged scripts without executing
  them: `/nix/store/sm7m2v77jj73fl35qy6v49vfznqjz3kb-workspace-pi-host`.
  Initial logs: `h0-package-check.log`, status `h0-package-check.status` (0).
- Final fresh Luna/low utility rebuilt the exact frozen H0 source after those
  fixes: `/nix/store/8i60kxxc11n46vd8hz2xn13ybmdm7lwh-workspace-pi-host`,
  derivation `/nix/store/pd8a311x7jk7hik2d17pj9xfdlrb0b7f-workspace-pi-host.drv`,
  exit 0. VM derivation evaluation also passed without build or execution:
  `/nix/store/78n5iccqinkn2s5qh2z8c3mjl9kp5ply-vm-test-run-dev-workspace-pi-runtime-host.drv`.
  Logs: `h0-final-package-check.log`, `h0-vm-evaluation.log`. All commands joined;
  no unfinished effects. Installed watcher policy: selected package
  `/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, catalog
  `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
  Luna/low, danger-full-access/never, fresh operation utility outside roster.

Local check fixes: duplicate-key parse objects were initially reused for mutable
receipts, causing legitimate key replacement to fail; parsed output is now
converted to plain hashes after strict parsing. A failed-receipt-I/O fixture
caught block-local rescue scope; the entry variable is now bound before the
lock. Standalone bootstrap loading was made explicit for the extensionless
immutable helper file. All are within H0 source scope.

## Remaining gates and owner handoffs

Lead owns package acceptance, completed-deliverable independent
review and longer-check release. No intermediate-package automatic review was
invoked. Installed VM is defined but unrun; launch permissions/containment on the
actual deployment remain unproved. No live operations are implied.

P3/implementer1 received exact helper reply fields, shared byte fixture, state
preparation/GC-root/lock/freeze requirements and readiness distinction; no P0
interface collision. Production supervisor/client is a later lead allocation.
P7/implementer0 received exact fixed feature-manifest emission, explicit Ruby/VM
check exports, VM fast-CI exclusion and docs entry-point links. Current P7-C is
pins only; broader packaging remains a later allocation after capacity.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## Final source identity

Candidate build inputs remained unchanged through commit. File SHA256:

- helper: `03bcf8d34607e5c16d007fabefe1da9255914820b066f12b18bf364cc6522d80`;
- bootstrap: `4d78ade0515e4456fc3f4c3d37a664db136906619d78ae989d562edff8cbad44`;
- package expression: `2be1a172d57961b1b5e43ddd82379c7888b07943de3753c48fedf58b15bc7d91`;
- module: `44f2de59705e5fc957f5a48b117bf611f76d5a6729da95b49bbc100c66af4622`;
- VM definition: `4f1144704ca43347fac3f446b325cd40974538668c987cdc8afbbdf0f9f46f5f`.

The utility's expression-file checksums `51bb2d41...` and `435f651b...` name
`/tmp/pi-h0-package-check.nix` and `/tmp/pi-h0-vm-check.nix`, respectively,
not changed source. No VM build/run, feature publication or independent final
review was requested as part of this short index window. Shared branch
publication remains lead-sequenced with the other D packages.
