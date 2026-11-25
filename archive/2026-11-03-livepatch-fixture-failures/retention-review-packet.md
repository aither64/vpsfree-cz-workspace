# Cache-retention committed review packet

Session: 2026-11-03-livepatch-fixture-failures. Repository vpsfreecz/vpsadminos,
worktree worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos.
Review owner reviewer0, retained Sol/xhigh/read_only, independent.

Review the new cache-retention behavior and fresh final branch inventory under
the applicable general, architecture, scope and risk/compatibility lanes.
Original complete final review remains final-review.md for dd188397..4fc0f375;
review-reconciliation.md records narrow R1/R2 fixes through efc5f8fe.
Do not repeat unaffected resolver/runtime implementation review; inspect any
interaction necessary for this new workflow behavior and the complete final
history/equivalence inventory. This is a committed-deliverable review before
new long CI, not a request for a rubber stamp or runtime qualification.

Exact ranges:
- Failed tested/published old head efc5f8fe87f7b0ddc09b5946047e1c231d23db67,
  base dd188397abe37d0bc33f4c5dfb3605206ce5e326.
- Retention fix before refresh 06d373facd86003a6c2d27604d553939f7ef3577,
  same old base; old efc -> 06d diff is ONLY .github/workflows/ci.yml, +11/-1.
- Fresh final base 742eb30cb1a8b6766c85e915d26b0400e38244b1; final head
  48f2983e3cf6b5b72a21c254f744ad8e7d62a123.
- Complete final series is ONE commit, tests/livepatch: qualify current module
  probe sites, 16 files +2157/-180. No migrations, no repeated pin/input/generated
  update streams or obsolete fixup commits. All backups retained locally.
- Incoming baseline is three openSUSE commits, seven files +27/-14; no feature
  path, fixture/kernel/lock overlap. Clean conflict-free rebase. A reports
  range-diff '=', equal stable patch ID eb6c27981a4cb0e38498f77fb4e5a92856cbc212,
  all16 feature blobs and original message equal between 06d and final48.
  Verify these independently. Baseline work is canonical source, not another
  session's files or transcript.

Requested outcome remains current normal producer qualification without fixed
v7 whole-file allowlisting or historical-only offsets. Exact predecessor/boot
integrity, nine finite semantic sites, recovery and matrix contracts remain.
No production recipe/kernel/Nixpkgs pins, server/config implementation, public
API, helper CLI or fleet update change. Conditional merge approval requires full
CI success and remains unsatisfied. No deployment or lifecycle action permitted.

New evidence/fix: ci-sites-retention-failure.md links full exact failed attempt,
raw logs, public narinfo receipts and read-only canonical cache helper source
revision f924aabd0a774d88d173419527215cf4b538168a. Build126191705303 passed and
copied both outputs; Intel126236869931 could not substitute captured sites
aiqijl... about61min later, before any VM/descriptor read. Sites narinfo404 while
normal producer200. Existing cache profile rooted only BUILD_OUT; sites are
outside that closure. Daily GC can collect unrooted output, but actual deletion
timing is NOT journal-proven. Assess fact/inference and smallest sound correction.

Only workflow changes: ordinary run/attempt-specific local candidateSites
outlink; conditional second existing push-ci-generation call using exact captured
LIVEPATCH_SITES_OUT and branch-livepatch-sites profile. Existing90day policy,
SSH copy, source/module/digest identity, toplevel profile and focused/ZTS skips
remain. The nearby source comment explains the lasting retention invariant;
no additional project-doc mechanism was necessary. Operations evidence belongs
in the linked session note, not product docs.

Quick checks on final refresh:19 actual-workflow identity/retention controls
pass (real Nix JSON/assertions/checksums, build/SSH stubbed), YAML/matrix/guard,
Bash/Nix parse, whitespace, declared cached Overcommit Nixfmt/RuboCop pass.
Original message and feature patch are equivalent; all message hooks passed on
06d before rebase. One IFD-disabled eval confirms unchanged qi47 producer/module
and aiqijl sites/asfl9 drv. No build or nine-minute ELF rerun needed for unchanged
module/SDK/parser inputs. Exact prior24 resolver controls,34 consumer specs,
all9 real-module selectors, helper build/49+19 CRC remain bounded evidence.

New exact CI must prove retained output availability on downstream runners and
all runtime witnesses/native/nine rows. Current failed run41714748110/attempt1
remains watched; no retry or replacement run launched yet. Do not treat static
controls as live cache/guest proof. Read plan.md, state.md, original reports,
package-a-result.md, ci-sites-retention-failure.md and relevant final source.
Return complete review through report_to_lead; stay read-only and do not write
source/session files, run long checks, fetch/push, retry/cancel CI or merge.
Include explicit final history, repeated-stream and no-migrations conclusions.
