# Independent final review

No Blocking or Important findings. No application change is requested by this
review. The reviewed task changes may proceed to the planned longer verification.
This is review evidence, not integration or deployment approval and not a claim
that the feature is deployed or ready for use.

## Identity and scope

Reviewed on 2026-10-28 by retained `reviewer0`, thread
`01a182d1-b79b-7060-a7dc-f20d38733788`, saved `gpt-6.1-sol` / `xhigh`, purpose
`review`, access `read_only`. The same-session roster confirms those settings;
no override or fallback was used. `dev-session current` from this tracking
directory printed `2026-10-28-files-tab-limit-diagnosis`; both session environment
variables were absent, consistent with the trusted thread binding. Review was
independent and direct, without nested reviewers or peer communication.

Applied the mandatory review skill's general, architecture/repetition,
scope/proportionality and risk/compatibility lanes. Overall risk remains high:
the new confined HTTP filesystem interface, paired browser assets, deployment
selection and inherited persisted communication/reporting policies need review
together. Read applicable workspace procedures, each affected repository's
AGENTS, the packet, own plan/design/state and delivery/check receipts, relevant
implementation, tests and documentation.

The user selected collapsed lazy directories and alphabetical pages, then
authorized implementation. The task delta is one runtime commit, 14 files,
+1,140/-92, plus two small selection commits. The scanner, continuation format,
bounded browser queue and tests serve that supported behavior. They introduce
no recursive fallback, cache service, database, cleanup subsystem or unrelated
native upgrade. The inherited six runtime commits account for the larger full
diff; they are a deployed compatibility dependency, not additional Files work.
Recorded diagnosis, inventory, committed implementation and matched pins are
concrete delivered milestones. Available timestamps do not establish total
active working time, so this review makes no unsupported elapsed-time claim.

## Exact reviewed history and consolidation

Runtime repository: `git@github.com:aither64/dev-workspace.git`, target `master`.
Reviewed the complete linear series and final diff from
`4a002f52c3b55099540aa99708d5fcf29f7b2456` to
`617235fce02ac7095d258c73575bb8a64696b6d1`:

1. `cc106266345ebe5e3332561c7143947bc1415b69`: communication grants and delivery.
2. `e9153e614e44766d0f0efd6721b34b7bf2f4c14a`: transcript communication presentation.
3. `d0a9c5f6dc38220bed45d0d7ef631768ad538203`: recovered-send retry proof.
4. `fd9128a1c2dd81202c9b09b76e640e816f020524`: durable pending-send drops.
5. `f9d8e4fe7d0dddab7d323e14f1019b12552a15fa`: settings categories.
6. `f199947c4c0d2c5d96f4f663053ff5a592946ef4`: durable communication projection.
7. `617235fce02ac7095d258c73575bb8a64696b6d1`: lazy Files browsing.

The remote base is the merge base; `f199947c` is an ancestor of the final head.
Independently compared all 45 files changed by the inherited range with selected
immutable runtime source `/nix/store/m7nsrybwhd1x0iwqpxsz79ywgqi5v1c5-source`:
all matched byte for byte. The selected package and complete input/source
receipts remain in [rollout-preparation.md](rollout-preparation.md). No prior
review or integration approval is assumed. The inherited commits have distinct
behavioral purposes; the durable projection complements the earlier native
transcript presentation. No obsolete runtime approach, task fixup or transitional
implementation remains. Preserve the deployed predecessor lineage intact.

Workspace repository: reviewed the complete task diff
`668291226733ffdb18fe94588078994af02a8594..388d27e3be1e57178558f0171850c02926135c99`,
one runtime-selection commit. Independently inventoried the full 11-commit range
from remote `6e131813ed455b2335a9287be760877d3242fd9d`; it matches the receipt.
Its preceding ten commits are already shared-master tracking, KB candidates and
notes. Their private record content was not opened or claimed as substantively
reviewed here. The feature integration delta against current shared master is
only `flake.nix` and `flake.lock` (+5/-5).

Configuration repository: reviewed the complete one-commit range
`2d6837f0b9582bbd812ecccf6cd59b5685029e0a..f6f8a2f746302328e45217c15529b8c82e3a40f2`.
Its generated confctl message retains the full runtime changelog; the diff is
only the intended `devWorkspace` lock selection (+3/-3).

There are exactly two task pin streams: the workspace nested runtime input and
configuration's channel-owned runtime input. Each contains one final update;
there are no superseded intermediate pins to consolidate. Runtime has no
dependency-update stream. No obsolete task history remains in the reviewed
ranges. Independent semantic lock comparison found only `dev-workspace` and
`devWorkspace` changed respectively, with unchanged edges, all other nodes and
lock metadata preserved. Both select the exact final runtime and narHash
`sha256-ZYW7q9Q1TetTecOhzNop8U5UExuVUmFQQhb3KvPWdr8=`. Native/runtime dependency
selection files are unchanged throughout the complete runtime range.

Read-only SSH `ls-remote` during this review confirmed all three published
feature heads above and remote defaults at the stated runtime, workspace and
configuration bases. This is review-time evidence; integration needs a fresh
target check under its normal procedure.

## Correctness, architecture and compatibility

The generic runtime owns the interface. The workspace composes it through the
existing extension input; configuration consumes its host module and Codex
package helper through the existing confctl mapping. Inspected the actual
workspace flake, deployment-contract checker and aitherdev consumers. Selection
does not move the application into the system profile or alter native Codex.

`tracking_directory.go:160` validates the canonical relative path, reuses
`openConfined` and the authorized work/archive root, checks entry types with
nofollow stat, and reads only immediate children. A 201-entry max-heap and exact
JSON-size accounting implement the specified ordering and bounds. The cursor
is a position bound to scope/generation, not authorization. Before/after and
reopen checks detect ordinary concurrent changes. The repository adapter
(`source.go:121`) shares four reader slots and includes slot waiting in its
deadline. The route (`source_files.go:294`) rejects malformed parameters and
maps changed generations to 409 without partial success. Preview/download
confinement and the old recursive endpoint remain intact.

The browser Files block (`app.js:3726` onward) uses per-directory generations
and a two-request queue, retains open nodes, removes queued subtree reads and
rejects late cancelled results. Refresh replaces page one without inferring
selection absence from a partial listing. Selected content uses its independent
read fence and clears stale actions on confirmed unavailability. Old browsers
retain the old endpoint; new browsers report unsupported/invalid responses
without recursively falling back. All three app asset references advance
together. The API and browser responsibilities are localized; no additional
abstraction or optional hardening is needed for this supported boundary.

The inherited communication code binds grants to exact identities, durably saves
submission identity/options before sending, reconciles uncertain outcomes,
checks normal execution/provider holds, and serializes revocation against
admitted sends. Store admission reserves completion/revocation capacity.
MCP lead resolution and member reporting remain distinct. Transcript projection
does not become authorization, native pagination or send acknowledgement.
Pending-send drops retain delivery identities and copy lineage; storage failure
holds dispatch. Inspected the related service/native, MCP, browser and package
registration/recovery tests rather than relying on predecessor review.

**Migration inventory: no database migrations** in any reviewed range. The
Files commit and both pin deltas add no persisted format. The whole runtime
range is not persistence-neutral: it adds private schema-1 communication state,
changes reporting policy 1 to 2, adds communication policy 1 and persists browser
drop markers in the existing attempt format. The package capability guard and
upgrade documentation preserve the communication boundary; older browser
behavior for drop markers is explicitly documented. No unapplied intermediate
schema migration, stale-schema guard or transitional migration remains.
Keep this deployed state and recover forward with compatible packages.

Runtime feature documentation is discoverable from the README/portal guide and
matches the Files implementation. Communication upgrade guidance covers its
reporting-registration boundary and ordered host/application selection. The
existing configuration operations guide covers the matching channel, host-first
activation when needed, user-profile application and forward recovery. Individual
revision/build/rollout evidence stays in this session, with no unnecessary new
operations document for a routine pin update.

## Verification limits and next action

Inspected the recorded passing focused session, repository, web/API/browser,
Node and hook checks. Reviewed regression coverage for 5,001-child paging,
byte-shortened pages, escaping, confinement, work/archive changes, mutation,
descriptor/slot cleanup, cancellation, selection and old API behavior. Reviewer
ran read-only history/diff/whitespace and source/lock comparisons, not another
test suite. No long verification was launched.

Remaining evidence: full Go suite, runtime/composed/deployment-contract packages,
aitherdev build, exact-head CI and the prepared native Chromium smoke. The
current Node Files fixture emulates DOM behavior; the prepared smoke uses real
details controls but controlled request promises. Neither alone proves the full
deployed portal, real HTTP aborts or live host/profile continuity. Preserve those
limits in the verification/deployment receipt. A very large single immediate
directory can still time out; that is the documented bounded-scan tradeoff, not
a reason to add a cache or broaden this fix.

Next: lead launches the prepared verification batch through its watcher. Fix
any resulting defect within the accepted boundary; apply the mandatory skill's
narrow-fix rule rather than automatically commissioning another full review.
Integration still requires explicit named repository/target approval, including
the inherited runtime lineage if absent from remote master. Actual activation
requires its separate authorization and machine ownership. Leave this session
open; this report authorizes no lifecycle action.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>
