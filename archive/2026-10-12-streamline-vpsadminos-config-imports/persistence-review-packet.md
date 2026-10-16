# Final cause-driven persistence correction review

Committed correction head `809799be12da1d35eacd180dd936579ab55e5bbe`, tree
`22fc767a89d06537a57e6786bb1d1e71df0a4d41`. Clean source worktree. Reuse retained
reviewer0, Sol/xhigh/read_only. Read mandatory review
skill and all four lanes. High risk: guest activation and persisted identity.

User outcome: fix the discovered defect within this initiative and establish
the cause, without an unexplained workaround. Exact source/allocator, generated
activation order and all-three-variant v2 runtime evidence establish allocation
against transient `/var/lib/nixos` before late binding of intact saved maps.
Original UID/GID 995:993 became 996:996 while maps and numeric payload ownership
remained 995:993. Live switches passed because their bind was already mounted.
See `impermanence-root-cause.md`, `implementer-ci-v2-causal-evidence/` and
`ci-v2-image-failure-artifacts/`. Prior proposal is historical/superseded.

Workspace `/home/aither/workspace/ai/vpsfree.cz`, slug
`2026-10-12-streamline-vpsadminos-config-imports`. Source worktree
`worktrees/<slug>/vpsadminos`, initial base
`1150e37b1cc997b1728f2fda806a3433ef55b798`, feature v2
`4a40154539bf6dc73d391c30326af255b4dc15b2`. Baseline fix must be a separate
logical commit after this feature. No migrations, public pin changes, repeated
dependency streams or obsolete shipping history. Prior published/tested heads
are retained by exact backup refs; no merge, release, production deployment or
external guest adoption has occurred. Disposable CI is recorded separately.

New scope: four current self-contained raw files (25.11, 26.05, latest stable,
unstable), focused activation/shell tests wired into the existing quick runner,
minimal existing selector-stub backend fields, and owning guide. Latest stable
and 26.05 stay byte-identical. Independent baseline defect belongs to this
second commit; do not demand folding into selector v2. The full two-commit
history/diff must be reconciled with the original final branch review. Unchanged
KB companion `2d11b2cc8445a695e7862af18ca0a70598afb38b` and six guarded candidates
retain prior review/narrow-fix evidence. No KB edit/publication in this fix.

Accepted design: native legacy-only step for existing promoted directory binds
at `/var/lib/nixos` and `/var/log`, with upstream specialfs before it and users
after it. Move only these binds out of boot.specialFileSystems; retain systemd
units, configured sources/options and other mounts. Existing utils.fsBefore and
lib.toposort order the selected subset. Actual cross-phase edges, cycles and
duplicate definitions fail explicitly. No option type/apply/module replacement,
full mount-script replay, account backend forcing or ID/ownership repair.

Before mkdir, require source below an available non-root backing mount; root
comparison uses mount IDs. Shipped images host-bind `/persistent` before guest
init. Custom root-backed sources intentionally fail with an actionable error;
do not claim universal backward compatibility. Preserve all existing metadata;
create only missing directories. Verify matching live source before changes,
avoid stacking/overwriting mounts, retain matching remount options and verify
mountpoint/inode equality after operation. Explicit parent-shell exit prevents
legacy allocation after failure; NixOS ERR recording alone is insufficient.
Ordinary and sysusers/userborn retain previous behavior and no new identity
guarantees. Dry activation performs no added mount work.

Data formats stay unchanged; no host coordination is required. This prevents
new drift in healthy guests, but does not repair damaged guests. Existing live
IDs can override the still-correct saved map on a later rebuild. Guide explains
preserving IDs/maps/data before recovery and rollback's reintroduced ordering
risk. Main agent applied the user-facing writing skill to guide/error prose.

Complete branch series is exactly two logical commits above `1150e37b`:

1. `4a40154539bf6dc73d391c30326af255b4dc15b2` — selector feature v2, already
   reviewed/reconciled with prescribed narrow diagnostic corrections.
2. `809799be12da1d35eacd180dd936579ab55e5bbe` — independent baseline correction.

Complete final diff: `vpsadminos-persistence-final.diff` (19 paths, 1615 additions,
189 deletions). New owner delta: `vpsadminos-persistence-fix.diff` (9 paths,
944 additions/165 deletions). No fixup/WIP/superseded source stream or migrations.
No production input/lock churn. All old retained 22.11–25.05 raw files, root
assertion, host/kernel/daemon code and original image preservation assertions
remain unchanged by the baseline fix.

Quick requirements: full release/alias/caller-lib/stateVersion/negative matrix,
four generated templates, copied standalone routes, real 25.11/26.05/unstable
activation/dry/backend/topology checks, exact prior-v2 ordinary/alternative
script equality, and eleven cases using the actual evaluated shell snippet.
Missing storage, failed bind, wrong live mount and failed lookup must prevent
allocator marker; custom existing metadata/payload must remain unchanged.
All these quick checks passed. First batch passed selectors/templates/standalone
then failed only at missing lib.findFirstIndex in the new test; helper corrected
before the commit. Focused rerun passed every actual-release bool, eleven actual
generated-snippet shell cases, negative errors, exact KB consumer evaluation,
hooks and docs. Logs/statuses: `persistence-quick-eval.*`,
`persistence-remaining-eval.*`, `persistence-eval-rerun.json`,
`persistence-kb-eval.*`, `persistence-quick-{hooks,docs}.*`. Hook-enabled commit
also passed (`persistence-commit.*`). Body lines meet 80-column limit; 72-column
hook messages are advisory. Final committed-head template proof passed all four
at 809799be (`persistence-final-template.*`, exit 0). Runtime follows
review; no failed check is represented as a passing result.

No corrected runtime pass yet. Required long cases are ordinary/impermanence
26.05 and explicit unstable on final reviewed/published head, retaining the
dynamic earlier-sorting account and all original five expectations. Nominal
25.11 image still uses stable builder; no historical runtime claim from its name.
Real 25.11 quick evaluation remains distinct. No production rollout approved.

Requested report: inspect all new source/tests/guide and reconcile the complete
two-commit series with the original final review. Cover general, architecture,
scope and risk lanes, including the intentional root-mount source/topology
failure boundaries and standalone duplication contract. Explicit whole-branch
history/repeated-stream/no-migrations conclusions are required. Do not repeat
unchanged KB/selector analysis without a new defect. Remain read-only, no nested
agents, source edit, Nix/runtime retry, publication or lifecycle action. Verify
exact session/live roster/saved settings before work. Findings and verification
limits must distinguish static/generated/stub evidence from actual new-head
mount/boot proof, which remains pending.
