# Final affected native Job review

## Result

No Blocking, Important or Advisory source findings. Accept the native Job parser
correction and focused regressions at
`ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f`.

This clears the affected independent **source-content review** gate for the next
required native/package proof. It does not establish a passing native cleanup,
authorize publication/CI/deployment/integration, or permit session lifecycle
actions. Exact immutable source/input proof remains required for subsequent
builds and mechanical pins; restored source verification is recorded below.

## Identity, complete range and history

Same retained independent `reviewer0`, purpose `review`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, `gpt-6.1-sol` / `xhigh` /
`read_only`, ready in the verified live roster. No overrides, fallback, nested
reviewer or substantive authorship. Before accessing records, `dev-session
current` returned exact bound slug
`2026-11-02-session-temporary-service-cleanup`; both environment markers were
absent and the trusted exact workspace/session binding matched.

Applied mandatory-change-review general/history and risk/compatibility lanes,
reusing unaffected prior all-four-lane, UI and source-graph conclusions. The
larger feature remains High risk because it controls native processes and
destructive lifecycle ordering. This correction addresses one native display
contract, with no framework, optional hardening or scope expansion.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Complete final range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f`.
Tree: `e52d2aa3da60fcf2e5d563b7606c98e7ef844180`.
Independently verified clean source/index and complete logical series:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — service owner/lifecycle and this fix.
3. `ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f` — dependent portal/package integration.

Inspected complete inventory/scope and range-diff against accepted `7302f4dc`.
UI and dependent patches are equal; only two core paths change, 71 insertions/
three deletions. The production delta is five lines including its explanatory
comment. Complete branch: 49 files, 4,216 insertions/127 deletions.

The fixup `bb87e2e912010f7e64810ec972a4b525ce3b32a9` and final trees are exactly
equal. Session refs retain original `7302f4dc`, fixup and consolidated head;
original/fixup are outside final ancestry. **No obsolete approach, transitional
implementation or fixup commit remains in the final series.** The correction is
folded into its owner, with the established logical split preserved.

## Native interpretation and safety

Reviewed `libexec/workspace-session-services.rb:683-689` and adjacent snapshot,
observe, stop and stopped-proof code. Exactly a present empty value becomes
internal `'0'`: `values.key?('Job') && values['Job'] == ''`. Existing explicit
`Job=0` compatibility remains. Canonical positive decimal IDs are accepted as
known pending jobs, not as settled jobs. The formerly allowed whitespace suffix
is removed.

The distinction survives actual key/value decoding:

| Raw observation | Result |
| --- | --- |
| `Job=` | Known native no-job value, normalized to `'0'` |
| `Job=0` | Known explicit zero, unchanged |
| `Job=41` | Known pending job; cannot satisfy stopped proof |
| Missing Job line | Unknown; refusal |
| Bare `Job` without `=` | Malformed pair; refusal |
| `Job=null`, arbitrary text, spaces, leading/trailing whitespace, `01`, `41 pending` | Unknown/noncanonical; refusal |

There is no nil fallback, `to_s` conversion, stripping, inferred absence or
command-flag change in production. The test transport uses raw lines for the
malformed cases, rather than turning an absent property into a synthetic empty
value. Fixture default serialization now emits native `Job=` for loaded and
not-found states, so existing run/stop/retry tests exercise the real formatting.

`stopped_proof?` still requires internal zero before proceeding. Same-boot
retirement still requires a terminal/not-found unit, a recorded invocation and
empty expected recursive cgroup. Snapshot still validates loaded InvocationID,
unit description/properties, manager UID/placement, boot and expected cgroup.
`observe!` still refuses not-found launches and absent/zero/malformed invocation
IDs. The existing reboot boundary is unchanged. Empty Job alone proves neither
process shutdown nor settlement of an unobserved/uncertain launch.

Inspected regression coverage: malformed observations preserve registry/resource
identity and running phase, dispatch no stop, then succeed on exact empty-value
retry; explicit zero stays supported; positive pending jobs block retirement;
not-found plus positive or missing Job remains nonretired and dispatches neither
stop nor reset-failed. Invocation mismatch, residual descendants and uncertain
unobserved absence remain covered by unchanged focused tests. No authorization,
ownership, journal/receipt or file-removal rule is relaxed.

## Official formatter evidence and causal limits

Read `design.md`'s Native Job formatting clarification and the retained official
260.2 source at commit `f1d0952a125b96b7ab2f1ff29a87448ade8ac29b`:

- `src/core/dbus-unit.c:254-276,958`: Job type `(uo)`; no job returns `(0,"/")`.
- `src/systemctl/systemctl-show.c:1228-1240`: positive IDs print decimal; zero
  sends NULL to the value printer.
- `src/systemctl/systemctl.c:581-603`: explicit `--property` sets SHOW_EMPTY.
- `src/shared/bus-print-properties.c:27-40`: SHOW_EMPTY plus retained property
  names prints `Job=`. The actual command already has explicit properties and
  does not use `--value` for its unit snapshot.
- `systemctl-show.c:2368-2374`: missing requested properties produce only a debug
  notice, not an invented zero/empty property line.

Computed SHA256 anchors for those retained source files:

| Retained file | SHA256 |
| --- | --- |
| `src__core__dbus-unit.c` | `80e1b2328ab84338dab095a6496adbf1be5f47d0e7093b2089a347dbcded5a42` |
| `src__shared__bus-print-properties.c` | `44ed2103f071017606ec316c487bcd33c4e1673b65f1a28380f4b4771ce22d6c` |
| `src__systemctl__systemctl-show.c` | `1feb72b27c0907f71f9414b30da85ad6d249fca3299b854aed6f8b04f4db75f6` |
| `src__systemctl__systemctl.c` | `2784741133135e46e44944d4c59123a109be4add86b18ff7699f7a9f0d2a18c4` |

The architect records that pinned nixpkgs's patches do not alter these blocks
and the relevant 260.5 blocks are identical. This reviewer inspected the retained
260.2 chain and exact command; no live unit probe or new upstream fetch occurred.

Saved CI `41526190428` binds `7302f4dc`: fast/package and native creation passed,
archive failed, host skipped. The archive log shows systemd 260.2, successful
registered unit Starting/Started, then `service manager job state unavailable`
on the first registered launch. The preceding permission interruption belongs
to its deliberate recovery fixture, which progressed successfully.

**The failed raw Job value was not captured.** Official formatting plus the
fixture-only native-empty red reproduction establish a source-contract mismatch;
they do not constitute an observed native response body. Registered-service
cleanup has not passed natively in that run or at this new head. Successful old
UI recovery/creation is scoped to `7302`, not a new-head native result.

## Quick evidence, immutable source and remaining work

Read the retained red/focused/standalone/aggregate/final-smoke logs and verified
their receipt SHA256 values. Native-empty fixture against old parser reproduces
the exact error (one test/four assertions). Focused and final consolidated smoke
pass seven tests/118 assertions; standalone all-service passes 32/466 in 21.91 s;
aggregate plus original bad-root checks passes 34/478 in 22.38 s. Changed Ruby
syntax/whitespace receipts pass. These are component results, not native proof.

The saved final delta exactly equals the committed `7302..ee3` diff. Both changed
worktree files equal their committed blobs. Full nine-node lock graph equals the
receipt and is byte-unchanged from `7302`; lock SHA256:
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.

The receipt records source
`/nix/store/8ygzal9j12xj6x600ws7yrhgn1ijngx2-source`, NAR
`sha256-5mDdLgLQl/XPjIs9Ey5l2UDxWwVKR/VWpNCQwEvqsiw=`. The store path was initially
absent and the first read-only hashing attempt failed. The lead independently
confirmed its absence and assigned exact-head source restoration without source
changes. Once the path became readable, this reviewer independently compared
all 672 committed files, symlink targets and executable bits: no mismatch,
omission or extra source entry. Read-only NAR hashing then returned exactly the
recorded hash above; the source lock hash also matches. No cause for the earlier
absence is inferred. This closes the review's source-provenance limitation;
future build/pin receipts must still bind their actual inputs separately.

**No database migrations.** Local schema 1 remains directly introduced by the
original feature, with no new schema or supported predecessor-state boundary in
this correction. Ordinary journal/receipt/Store formats remain preserved.
**No repeated dependency/generated stream exists in the runtime series.**

Current workspace `d250081c`, configuration `4a9be5ba` and prepared application/
system artifacts remain held at `7302` scope. No future pin is reviewed here.
The previously assessed pure-mechanical review exception remains conditional on
actual installed verifier proof plus independent actual NAR/full managed graph,
source/range, retained accepted review, migration and consolidated-stream
evidence. Unproved scope or a substantive change requires affected review.

The next affected acceptance proof is the existing packaged native archive
lifecycle check at the new exact inputs, with required package/CI verification.
Earlier passes do not certify this changed production/Ruby-filter input. No
additional duplicate Ruby campaign is requested by this review. No tests,
builds, CI actions, source/Git mutations, lifecycle operations, claims or nested
agents were run. Only this report was written; prior reports remain unchanged.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
