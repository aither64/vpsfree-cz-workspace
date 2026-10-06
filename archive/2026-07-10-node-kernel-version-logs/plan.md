# 2026-07-10-node-kernel-version-logs

## Goal

Provide an operator-facing tool which uses the central logs on `int.log` to:

- show the booted kernel timeline for every vpsAdminOS node, with timestamps;
- collapse consecutive boots of the same kernel by default so kernel changes
  stand out, while retaining an option to show every observed boot;
- answer, for a requested minimum kernel version, when each node entered its
  current uninterrupted period at or above that version;
- distinguish an exact transition from incomplete or retention-bounded
  evidence instead of inventing a date;
- produce machine-readable output suitable for security-advisory notes.

The first iteration deliberately concerns booted kernel versions only. Kernel
livepatch and eBPF LSM program state require a separate evidence source and
policy model.

## Affected repositories

- `vpsfree-cz-configuration`
  - primary implementation repository;
  - configure `int.log` to retain a small boot-event index;
  - package the server-side index/backfill helper;
  - add the operator command as a configuration-local `ConfCtl::UserScript`
    under `scripts/`, following the existing `runtime_kernels.rb` pattern;
  - provide the one-time retained-log backfill operation and tests.
- `vpsadminos`
  - source/reference repository for the existing boot markers and the stable
    booted-system paths used by an optional live cross-check;
  - no vpsAdminOS change is required for the first iteration;
  - an additive structured boot marker can be considered later without making
    the central tool depend on a coordinated node rollout.

No vpsAdmin change is needed: deployment or configured-generation history is
not proof that a node actually booted the kernel.

The `confctl` repository is explicitly not affected. `confctl` remains a
generic deployment tool; this workspace-specific functionality uses its
existing user-script extension point from `vpsfree-cz-configuration`.

## Approach

### Evidence available today

vpsAdminOS has always made the kernel's standard early-boot line available to
rsyslog through `imklog`:

```text
kernel Linux version 6.12.79 (...) #1-vpsAdminOS ...
```

Since vpsAdminOS commit `316aa5b9b114aaace48e6ff233c77b6fa6a46d1a`
from 2025-06-17, it also writes an explicit post-boot marker to `/dev/kmsg`:

```text
kernel vpsAdminOS 25.11.git.a4bc7a3 with kernel 6.12.79
```

Both forms are present in the sampled `int.log` files with RFC3339 timestamps
and full cluster hostnames. The standard `Linux version` record is therefore
the backward-compatible source; the explicit marker additionally supplies the
vpsAdminOS build ID. The two records for one boot arrive milliseconds apart.
Some input is duplicated, so records must be normalized and deduplicated.

The central node log tree currently contains 3,317 files and about 217 GiB.
Repeatedly scanning it for every advisory query would create unnecessary I/O.
The configured node-log retention is 180 daily rotations, although the sampled
`stg/node2` directory currently starts on 2026-04-03. Query output must report
the actual evidence boundary.

### Recommended design

1. Add a dedicated rsyslog action to the existing `remote-file` ruleset on
   `int.log`. For hostnames below `cz.vpsfree/nodes/`, retain only recognized
   kernel boot messages in a tiny append-only line index using the same
   RFC3339 syslog file format as the raw logs. This lets the backfill copy
   retained records byte-for-byte and keeps one parser authoritative. Keep
   this security evidence indefinitely in one intentionally unrotated file;
   machine-readable JSON is produced at the user-command boundary.
2. Add an explicit, idempotent backfill command. It scans the retained raw
   `log*` files once at low CPU/I/O priority, recognizes both historical
   formats, sorts exact records, and atomically writes a separate plain-text
   backfill index. Keeping live and backfill files separate avoids replacing a
   file which rsyslog has open. Repeated scans merge previous backfill records
   so expired raw rotations cannot erase evidence. Live capture records its own
   start boundary; for backfilled nodes the oldest observed boot is the history
   boundary. Queries parse, merge, and semantically deduplicate the sources.
   The helper is deliberately designed for a trusted root-operated central log
   server. Test/maintenance path overrides are not treated as an adversarial
   security boundary; with the production defaults, raw logs are passed only
   to recursive `grep`.
3. Add `scripts/kernel_boots.rb` in `vpsfree-cz-configuration` as a registered
   `ConfCtl::UserScript`. It owns parsing, machine selection, query semantics,
   table and JSON formatting, and invokes the capture/backfill helper deployed
   on `int.log` through `ConfCtl::MachineControl`. No command or library is
   added to the `confctl` repository. Proposed configuration-local interface:

   ```text
   confctl kernel-boots list [machine-pattern] [--all-boots] [--json]
   confctl kernel-boots version-since VERSION [machine-pattern] [--json]
   confctl kernel-boots backfill
   ```

   The default machine set is the currently configured, non-carried
   vpsAdminOS nodes. A separate option can include retired nodes still present
   in the index. The server-side helper is an implementation detail installed
   only on `int.log`; operators normally use the user-script commands above.
   Timeline and version queries retrieve the backfill and live indexes through
   one read-only snapshot helper invocation.
4. Coalesce the standard and explicit markers for the same node/kernel within
   a short boot window. Prefer the explicit marker's OS build metadata, but do
   not silently discard a disagreement between the two marker types.
5. In the timeline, collapse only *consecutive* equal kernel versions by
   default. A sequence `6.12.81 -> 6.12.79 -> 6.12.81` must retain all three
   transitions because it shows a rollback and subsequent fix. `--all-boots`
   shows same-kernel reboots after marker-pair deduplication.
6. For `version-since VERSION`, compare numeric kernel components and walk
   backwards from the latest state. Report the beginning of the current
   uninterrupted `>= VERSION` interval, not the first time the node ever ran
   that version or newer. This makes a later rollback visible.
7. Optionally live-check configured nodes when answering `version-since`:
   obtain the boot time from `/proc/stat` and the immutable booted kernel module
   directory below `/run/booted-system/kernel-modules/lib/modules`. This does
   not depend on `uname`, which livepatch or eBPF code can alter. The live check
   detects a missing latest log record and can identify a current boot older
   than central retention. It does not reconstruct missing historical boots.
   The first implementation includes this check by default for threshold
   queries, with an opt-out for offline or central-log-only operation.

Suggested table fields are `NODE`, `BOOTED_AT`, `KERNEL`, `VPSADMINOS`, and
`EVIDENCE`. The version-period view uses explicit `at-or-above`, `below`,
`conflict`, and `unknown` states and includes `VERSION_SINCE`,
`PREVIOUS_KERNEL`, and `HISTORY_SINCE`. A requested live check which fails must
make the current status `unknown`; operators can explicitly choose
`--no-live-check` to accept central-log-only evidence. Vulnerability assessment
is one possible use of this generic version history, not part of its data
model or vocabulary.

### Alternatives considered

- Scan all raw logs for every command. This needs the fewest configuration
  changes, but each query would scan roughly 200 GiB for active nodes and gets
  slower as retention fills. It is suitable only as the one-time backfill.
- Maintain SQLite with per-file inode/offset cursors. This gives rich queries
  and incremental recovery, but adds state-management and corruption/rebuild
  complexity which is unnecessary for a few boot records per node per year.
  A line index plus a reproducible backfill is simpler and auditable.
- Infer history from deployed generations, channel pins, or vpsAdmin events.
  These show intent, not the kernel that successfully booted, and cannot be the
  authority for security-advisory dates.
- Change only the vpsAdminOS boot message. A structured marker would improve
  future metadata but cannot recover older events and would delay complete
  coverage until every node updates. It should remain an optional additive
  follow-up.

## Compatibility and deployment

- The raw central-log layout and existing 180-day rotation remain unchanged.
- Existing machine logs are read-only inputs with the production paths. The
  backfill's only operation on them is recursive `grep`; all temporary and
  persistent output is written below the dedicated state directory. The helper
  trusts its root operator and does not defend test/maintenance path overrides
  against deliberately constructed filesystem aliases.
- The new index is additive persistent state containing only boot metadata. An
  old configuration can ignore it after rollback; a rebuilt index can always
  be produced from whatever raw logs are still retained.
- Deploy the `int.log` rsyslog capture and query package first, then run the
  backfill. This closes the live-capture gap before the expensive historical
  scan begins. Backfill must not run as part of activation.
- No node update or coordinated all-node vpsAdminOS deployment is required.
  Old and new nodes produce at least one recognized marker.
- A later structured vpsAdminOS marker must be additive and the central parser
  must continue recognizing both existing formats during mixed-version
  operation.
- There are no database schemas, vpsAdmin APIs, generated clients, protocols,
  or Terraform contracts to migrate.
- No `confctl` release, dependency update, or coordinated `confctl` rollout is
  required. Existing installations load the new command from the configuration
  repository's standard user-script directory.
- Log timestamps are evidence of when rsyslog ingested the early boot record;
  they are expected to be close to boot time but depend on the node clock.
  Current live checks can compare them with kernel `btime`.
- The compact live index is intentionally unrotated because it contains only
  recognized boot events and is expected to remain very small. Backfill history
  is semantically deduplicated and preserved across repeated scans.
- Central syslog is operational evidence, not cryptographically authenticated
  per node. Permitted senders supply the stored hostname and program name, so a
  compromised node or another permitted sender can forge historical records.
  The live SSH check corroborates current state but not historical timestamps;
  this trust boundary must remain visible in operator documentation.
- A simple numeric `>= VERSION` rule is intentionally limited. Advisories with
  fixes independently backported to several stable branches will eventually
  need a policy consisting of multiple per-branch minimum versions rather
  than one global threshold.

## Testing plan

- Unit-test parsing of both observed marker forms, RFC3339 offsets, malformed
  input, duplicated records, marker pairs, and explicit/standard conflicts.
- Unit-test timeline reduction for consecutive equal kernels, same-version
  reboots, upgrades, downgrades, and rollback/re-fix sequences.
- Unit-test numeric version comparison (including differently sized numeric
  components) and `at-or-above`, `below`, unknown, and retention-bounded
  output.
- Test the backfill against fixture log directories, including recognized and
  unrelated messages, repeated runs, raw-input preservation, and empty input.
- Test table and JSON output deterministically.
- Test `scripts/kernel_boots.rb` registration, machine selection, argument
  handling, and its interaction with a stubbed `int.log` helper response.
- Build/evaluate the `int.log` configuration and validate the generated
  rsyslog configuration.
- Run the repository's Overcommit hooks in `nix develop` before committing.
- After committed quick checks pass, run the mandatory standalone change
  review before the longer `confctl build` integration check.
- Build `cz.vpsfree/containers/prg/int.log`; before any deployment, dry-activate
  it and verify that a synthetic fixture or subsequent real boot produces one
  indexed logical event without changing ordinary remote logging.
