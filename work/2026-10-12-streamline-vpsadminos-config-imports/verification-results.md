# Verification results

Source reviewed at `148832fb1cca24983328ef48697a9e1235ebc031`; final message-only
head `7e79afd4690ff5abac2554fd2a02ba8e8c97c0b1` (identical tree), initial base
`1150e37b1cc997b1728f2fda806a3433ef55b798`.

## Passed before independent final review

- All eight release keys, old aliases and original raw-file comparisons.
- Real guest nixpkgs24.11/25.11/26.05: exact, underscore and both stable selectors
  produce equivalent configurations/toplevels with stateVersion fixed at22.11.
- Guest library selection remains independent of vpsAdminOS's own26.05 input.
- Legacy latest-stable/unstable aliases retain their raw module behavior.
- Unknown old/future/malformed releases fail; separate error-text assertions pass.
- All four actual generated flakes/configurations/lock graphs evaluate.
- Copied single-file stable and unstable modules evaluate with matching inputs.
- Exact extracted KB UserData24.11 and Impermanence25.11 examples evaluate;
  impermanence early state mount resolves to `/persistent/var/lib/nixos`.
- Four generated-template checks rerun on the clean committed source head pass;
  generated lock revision names that feature commit, which contains new exports.
- Nix parser/formatter, shell syntax, source/candidate whitespace, documentation
  build, full declared Nixfmt/RuboCop hooks and hook-enabled commit checks pass.
- Six candidate/source checksums and schema-5 guarded manifest generation pass;
  all14Nix expressions parse and three bilingual example pairs match.

See `quick-module-eval-attempt-2.log`, `quick-{templates,standalone,negative,kb}-eval.*`,
`quick-hooks.*` and `final-template-eval.*` for exact output/status.
MkDocs gave one pre-existing navigation warning for an unrelated page. Commit
message TextWidth gave advisory72-column warnings, within the repository's80
limit. Exact source snapshots retain baseline trailing blank-line whitespace
because guard hashes require byte-for-byte production content; edited candidate
and manifest files pass whitespace checking.

## Corrected precommit fixture failures

Attempt1 stopped at getFlake rejecting fetchTree locator string context. Exact
source revision/NAR hash stayed pinned; clear only locator context after fetch
verification. Attempt2 passed the full module matrix, then found that a plain
path source had no rev/dirtyRev. Template evaluator now uses a local Git flake
reference, and the final committed-head check proves real revision provenance.
These are folded into the single owning feature commit. No kernel build was
observed during quick checks.

## Current runtime boundary

The published source `7e79afd4690ff5abac2554fd2a02ba8e8c97c0b1` passed all three
ordinary hosted image cases (25.11/26.05/unstable). Local ordinary 26.05 also
passed all 15 checks in 2,288.96 seconds, including the generated locked guest
flake, switch, network/DNS and restart. That local run used the documented
session-only host-metadata/empty test-config route, not the failing default
host-metadata route.

Hosted image run `38549964226` failed all three impermanence variants at
`fixture UID changed after restart`. Both switches and rebuild-stage checks
passed; restart/network/DNS/flake/machine-id passed before the UID assertion.
Later GID/payload/numeric-ownership checks were not reached and are not passing
evidence. Failures are retained in `ci-image-failure-artifacts/`. The unchanged
unstable path and unchanged raw compatibility modules support an independent
baseline ordering defect, but exact runtime map/mount state is missing.

The parent cancelled the local second impermanence case after receiving this
evidence. Its exit 1/SIGINT is cancelled/incomplete, not a product failure. No
local VM remains; two local unstable cases did not run. Full persistence
acceptance remains unmet. No integration, deployment, KB staging or publication
occurred. A scope question for the separate prerequisite fix is pending.

## Review remediation

Hook-enabled validation-message amendment passed; old/new source trees match.
KB companion static annotations, checker tests (10runs/22assertions) and source
contract validation passed. The full191-page checker fails on two unchanged
IP-address pages; untouched baseline contracts/source reproduce exactly those
missing counts. An independent216-discovery comparison finds only the same
four stale/unclassified baseline records and no candidate defect. Full corpus
pass is not claimed. All six page counts and guarded hashes/revisions/summaries
match. See kb-annotation-baseline-evidence.md/json and review-reconciliation.md.

Mandatory bin/check and all four rendered-template checks passed at final
amended source7e79afd46; strict120PNG inventory and repository baseline suites
are green. Source RSpec passed; CI/image workflows and companion Check pending.
Four fresh image cases begin only after final review/B1/I1 reconciliation.

## Runtime attempt 1

First26.05case failed beforeVMboot in host channel-registration evaluation:
system.vpsadminos.revision was null in the runner's store-path snapshot.
No guest runtime result is inferred. Source/code unchanged from baseline at
this boundary. Logs retained at image-attempt-1/. Next attempt will use
session-owned state directory; truthful hostrevision configuration is under
bounded investigation before any retry. No kernel build or VM activation occurred.

## Runtime attempt 3

Existing documented host metadata/empty testConfig route plus a short uniquely
owned state directory resolved earlier setup failures. Cached host kernel
6.12.109 booted, pool/network probes passed, and stable26.05 imagebuild started
with exact published OSCTL_IMAGE_VPSADMINOS_REV. The ordinary case subsequently
passed; remaining local cases were cancelled or not run, as recorded above.

## Diagnostic refinement

Implementer0's diagnostic-only delta is confined to the existing preservation
script: 49 additions/12 deletions. All five invariant reads and comparisons
retain failure, print expected/current state before aggregate failure, and
collect read-only maps/mount/activation evidence at initial rebuild, second
rebuild and restart. The earlier-sorting account, allocated identities and
original payload/ownership expectations remain unchanged.

Shell syntax, four nested Bash fragments, whitespace and eight isolated stub
cases passed. Declared hooks and hook-enabled amendment passed (exit 0):
`diagnostic-hooks.log/.status`, `diagnostic-commit.log/.status`. Committed head
`6d8c92b57151721701efce5578739a11678d03aa` received affected final review.
Both Important findings were corrected narrowly: actual specialfs invocation
and snippet boundaries appear in activation output, and the logical patch
records v2/history. Lead inspected retained syntax/filter fixture evidence and
the exact one-line delta. Hook-enabled amendment produced published v2
`4a40154539bf6dc73d391c30326af255b4dc15b2`; hooks and exact-lease push passed.
All four final generated-template/lock checks passed at that revision, exit 0
(`final-diagnostic-template-eval.log/.status`, fresh Luna/low, about 99 seconds).
No runtime pass is inferred from these diagnostic checks.

Publication automatically started image run `38562488356`, RSpec `38562488281`
and core CI `38562487990` at v2. Superseded v1 core run `38549964340` is confirmed
cancelled after verifying its head SHA. No current-head run was cancelled.
