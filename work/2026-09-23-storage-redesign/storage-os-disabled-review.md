# Final OS review: storage activity and disabled startup

## Exact committed deliverable

Session: 2026-09-23-storage-redesign. Registered OS worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadminos`.
Default target is staging; no integration approval for this branch.
Base: cbfc283d233f77cd6823893f97cf843f69c995a1.
Head: 09786fbc20a2d8e134e2e3001d53ef287646e74b.
Tree: 523c25edbb0bb2675c88b3c5d083aab907d6703a.

Inspect the COMPLETE base-to-head range, both commits/messages and final diff:
[Inventory](storage-os-disabled-inventory.json),
[complete diff](storage-os-disabled-complete.diff),
[new unit](storage-os-disabled-unit.diff).
Two commits,22 paths,1265 additions/49 deletions. Complete binary/full-index
SHA25627831036572eaed0648b5449c8fbf66367666d30013dea3dc2048b19ce84389e;
unitSHAef3993f1271891133ffcba699fbf0dc2d980b6e3c3654bd6cfdefea02eb5efd7.
All intended files committed; tracked/index clean,64 foreign regular files and17
descendant directories untouched. No symlinks in that foreign inventory.

1. 7f85b137: bounded pool storage-activity reporting. Normal equivalent replay
   of consumed8d05 onto cbfc; all15 feature blobs/message equal, range-diff1=1.
   Upstream five commits, lock and OSVM changes are retained. Original8d05
   backup/remote feature and current Admin pin are preserved. Earlier36/0 specs,
   independent review and storage-activity VM3/0 are historical evidence at their
   original composition, not fresh checks of this head.
2. 09786fbc: generic default-true osctld.enable plus its pool/activation consumers,
   actual-module/activation check, extension of existing owning switch scenario
   and runlevels guide. These7 paths form one behavior unit; a runlevel-only
   toggle would leave pool wait and activation calls. New source is382+/26-.
   Original0ccf commit was unpublished and replaced only to wrap two message
   lines to the hook72 preference; identical tree/parent/content, no fixup remains.

Verify the whole-history conclusion, obsolete approaches and supported
compatibility explicitly. No SQL/schema migrations are present in this OS range;
verify this conclusion and retained-format claims. Do not confuse the companion
Admin's three migrations with this repository. No input/lock update belongs to
this new unit; flake.nix adds only four focused-check lines. The inherited lock
is exact stagingcbfc. See the earlier
[replay inventory](storage-os-cbfc-rebase-inventory.json) and
[range diff](storage-os-cbfc-rebase-range-diff.txt).

## Requested outcome and owners

Read plan.md/state.md, and design.md's “Next common G1b slice: an osctld-disabled
generation prerequisite,2026-10-06” and bounded verification-selection decision.
The independently accepted Admin composition brief remains unreleased and is
context, not an implemented consumer.

Default/omission and enabled custom runlevel precedence remain supported.
Opting out omits automatic osctld starts from every generated runlevel, retaining
its service definition/configuration/tools. Final contradictory membership,
osctl pools/exportfs and pool installation refuse. Raw ZFS import/mount/property
behavior remains; only osctl association/wait/import/install/parallel settings
are compiled out. Activation uses the existing parsed destination membership
and preserves restart/skip behavior. It does not certify service/child stops.

The new check evaluates actual modules and executes the owning activation
classes with captured external commands. The existing switch scenario retains
all seven previous examples/helpers and adds one ordered normal-to-disabled
activation/fresh-disabled-boot/ordinary-return example on the same machine/disks.
It asserts actual current/booted closure and boot ID, absent automatic daemon,
pool completion and exact pool/dataset GUID, active property and known payload.
OSVM's existing last init parameter selects the resident generation; no OSVM
change or second VM engine. This direct boot is not production bootloader
persistence proof. Review that boundary and the final owning guide.

Discover actual consumers from source and current pins. Companion Admin worktree
is `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin`,
HEAD425d399afb3876bde4f3f4023f3810a45bee6f3f, still pinning consumed OS8d05.
Its nodectld integration and generated modules will later compose this option;
no new generation/package is delivered. Provider e33 remains independently
reviewed source, actual retained guest is historical Admin290f. Existing activity
report/RPC consumers and runlevels/services readers remain part of whole-branch
compatibility review. Inspect representative imports and versions, not a copied
consumer list alone.

No fleet-wide coordinated update or on-disk conversion is requested. Old sources
lack the option and refuse it; booting ordinary old generations can restart
writers and is unsupported under future physical ownership. Building this
configuration supplies no API owner, physical exclusion, descendant/delegated
GC reap, signed5290 executor, capture binding, G2 approval/action journal or alias
repair. API contract1 remains API-only. No default/pin/package/live action,
retirement, scheduler restart, retry, cleanup, rename/adoption/delete or repair
is authorized. Existing DIP5/DIP12 alias and NAS-history uncertainty remain held.

## Verification and limitations

Parent/watcher evidence, not reviewer execution:

- Member static Ruby runtime/two extracted script syntax, five Nix parses,
  five nixfmt1.5 checks and scoped whitespace checks passed.
- Actual focused Nix build passed0/55.664s, printed module_checks19 and
  activation_checks6, exact-source parity1.
- Ordinary flake check --no-build --print-build-logs failed1/0.195s before checks:
  preexisting overlays.all exports a list; Nix2.34.8 expects a function.
  Immutable7f85 baseline reproduces the same error1/0.599s; its flake/lock equal
  upstreamcbfc. This broad gate remains BLOCKED; do not report it green.
- Architect/lead accepted exactly two bounded no-build alternatives: evaluate
  all5 checks.x86_64-linux drvPaths and the exact registered
  tests.x86_64-linux."system/switch-to-configuration" JSON drvPath. Both passed,
  total183.911s/parity1 (131.341s/48.851s). This executes neither other four
  check bodies nor the8 VM examples. No public overlay interface was changed.
- Normal owning commit passed0/14.453s, all format/lint hooks passed; two message
  width warnings were resolved by a normal unpublished message-only amend
  passed0/13.420s with all hooks passed without warnings. Final source/tree
  parity1, empty index and foreign64 byte/stat parity; no hooks bypassed.
- Parent verified completed operation groups empty, no signals. Earlier optional
  watcher-preflight failure was zero-operation evidence, not a test failure.

No owning VM has run on this unit. After final review/finding disposition, only
`./test-runner.sh test system/switch-to-configuration` supplies the new lifecycle
proof. Stop unexpected actual local Linux compilation under the established
verification rule. No CI wait or live retained-cluster action is requested.

## Independent assignment

Risk HIGH: host startup/activation and mixed-generation rollback/persistent
storage behavior. All four lanes apply: general, architecture/repetition,
scope/proportionality, risk/compatibility. Read the canonical
mandatory-change-review skill and ALL four references, workspace/OS instructions
and applicable procedures. Retained reviewer0 is independent read_only,
gpt-6.1-sol/xhigh; saved settings govern, no overrides or nested reviewers.
Inspect complete committed source/history directly and report findings by
severity/originating lane, explicit whole-history/migration conclusion,
compatibility/consumer assessment and remaining proof limits. Do not run tests,
Nix/builds/network/DB/VM/process/live operations or read private packets/logs or
credentials. Source review gives no operational/integration acceptance.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-23-storage-redesign/.
