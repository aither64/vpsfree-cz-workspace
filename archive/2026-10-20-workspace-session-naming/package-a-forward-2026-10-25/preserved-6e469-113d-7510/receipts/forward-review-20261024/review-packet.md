# Final forward-refresh review — 2026-10-24

This is the completed committed deliverable after focused checks, before lead-launched
long verification on refreshed inputs. All four source worktrees are clean and
published. Read this packet, inventory.json and semantic-checks.json in this
folder, plus the exact source/diffs/history and owning reports below. Original
reports remain historical assessments; do not infer refreshed readiness from them.

## Outcome and boundaries

User asked for meaningful automatic workspace session names, safe automatic retry,
and manual slug entry if automation ultimately fails. Final total deadline is30s,
starting before queue admission, covering native retries, at most two utility
calls,200ms cancelable backoff and cleanup; require1s inference+250ms cleanup after
backoff. Hold one of two operation slots throughout. Freeze provider/input/model/
effort/settings/schema. Native willRetry progress never starts a fresh call.
A fresh call needs classified transient failure, affirmative old execution
settlement and successful cleanup. Ultimate failure preserves accepted inputs/
uploads and stops before base/slug/handoff reservation. No heuristic/generic
fallback, provider/account switch, model/native upgrade or existing-session rename.

Implementation and aitherdev deployment through configuration are authorized.
Default-branch integration, reboot and session lifecycle actions are not.
The prior waiting machine claim was granted Oct24, then released UNUSED revision3
once the changed deployed baseline was proved; no activation happened. No machine
or repository claim is held. Follow plan.md/state.md/design.md (new Oct24 section).

## Why this refresh and what must be preserved

Installed package l9sc1... runtimeb3a6eb2/client11ec57d has newer failed-turn recovery,
retry controls, shared-write cancellation isolation, bounded runtime admission,
accepted plan/fork recovery, deletion/retirement recovery and native service limit.
Immutable source/locked-NAR proof is in design.md:9–194. Runtime contract advertises
turnRetryStateSchema=1 and turnRetrySessionPolicy=1. Old built lary candidate lacked
these and is stale; do not suggest selecting it or deleting retry state.

Preserve newer baseline code and state readers/writers. Naming adds no migrations
or persisted/wire schema. Old naming branch heads were never activated/deployed
by this initiative; same-initiative provisional pins/publications are preserved
as evidence, not supported external boundaries requiring obsolete history.
Actual selected workspace/system Git SHA remains unproved. Installed composition
flake/lock content matches the verified workspace baseline; do not turn this into
a guessed SHA or literal-merge claim. Native dependency, binary hash, naming/team
catalogs and extension remain unchanged; no provider/auth configuration edits.

## Exact completed sources and cleaned histories

Worktree root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming

| Repository | Effective base | Final head | Owned series |
| --- | --- | --- | --- |
| codex-web | 11ec57d2203fc735696fe75a837d47da55a5c6af | 6e469863a69c7d35941ca2e15de9514223b58f4f | one owning protocol/retry-proof patch |
| dev-workspace | b3a6eb2fc0b41cf0cb965bf4c39991815d9df734 | 556a6e51b141fa419d620ad0d4ccd629fd2be6f5 |29d64ff4 dependency first,024f4b0e naming,556a6e51 archive diagnostics |
| workspace | ceca96a4932a17512ab96c741f5396136747471a | c8709037fa5bd2920051e7ce690f037ed31b3078 | one composed runtime update |
| vpsfree-cz-configuration | 25258cd3f483f0116dbab35c7acf89b16eff4bbc | de4d60d95dee0934a266e1f2fe80a48eeade3475 | one generated channel update |

The inventory binds exact trees, full own/remote-default-to-head series, final
diffs and hashes, registered initial bases and canonical origins. Main independently
verified all clean heads, fresh SSH publication/default snapshots and semantic lock
deltas. Workspace inherited FOUR coordination/artifact ancestors above remoteaadb;
metadata/counts/bounded path samples only, never copy/read other-session record
contents. Preserve these ancestors; they are not authored naming fixups. Review
owned ceca→c870 content, and explicitly assess the inherited-vs-owned distinction.
Configuration current baseline includes inherited input/CI updates; owned delta
changes only runtime/client nodes. Generated changelog remains unmodified b3a6→556
with all three final B commits and the allowed TextWidth advisory.

A old4300 patch replays cleanly, range-diff '='; all four changed ephemeral Go files
are byte-identical. Newer client files remain baseline ancestry/unchanged. A docs/
protocol corpus additions coexist with baseline additions.
B original naming and archive diagnostic patches are exactly equivalent to their
new owning commits. Redundant old915 attention readiness fix was OMITTED semantically:
new baseline has a2s explicit-stage/diagnostic implementation, our old test had5s
and Promise.race. Do not call this literal patch equality. Retain upstream test
unchanged;90 critical baseline blobs, service limit and retry capabilities are exact.
No unused old fallback, fixup series, repeated dependency/channel streams or new
migration is intended. Independently conclude complete history/consolidation and
migration lineage, explicitly no migrations if confirmed. Prior incremental reviews
alone do not complete this gate.

## Ownership, interfaces and actual consumers

codex-web owns native notification identity/validation, execution settlement and
cleanup proof behind additive CanRetryEphemeralTurn(err) bool. RunEphemeralTurn
and errors.Is categories remain compatible. Runtime imports that exact client
and owns deadline/slot/provider/retry/manual policy. Workspace composes extension
and runtime; configuration channel dev-workspace/devWorkspace selects matching
host module. Discover actual consumers from imports/pins/wrappers as needed.
Preserve new shared-client cancellation/continuation semantics while assessing
original naming logic in its new context. Avoid speculative retry frameworks.

## Reports, docs and quick evidence

- package-a-forward-2026-10-24/{README.md,inventory.json,replay-proof.json,range-diff.txt,source.json}: one owning replay, independent three-way tree match; focused Ephemeral/CanceledWrite/AlreadyCanceledWrite/ContinueFailedTurn/Continuation PASS3.589s, protocol coverage exit0, formatting/diff checks. No native execution yet on new head.
- package-b-handoff.md and package-b-forward-{final-proof.json,final-history.txt,final-diff.txt,range-diff.txt,checked-tree.json}: checked/published treecd57256..., separate-index reconstruction exact; naming/preparation36.625s, admission/generation/actual disposable accepted-fork recovery5.963s, upstream attention71/71 PASS8.269s. Pin/module, advice/terminal handler, syntax/format/Nix and archive8-case privacy/bounds/original-error checks pass. Live overlay compile-only0.043s; no inference.
- package-c-forward-2026-10-24/{README.md,inventory.json,quick-checks.json,semantic-check.json,activation-recipe.md}: one pin each; normal hooks/Nixfmt/diff/deployment-contract/semantic checks pass. Last workspace rebase only inherited tracking metadata, owning range-diff '=' and checked flake/lock bytes exact. Declared Nix/Gem shell fixed old parser hook environment without bypass.
- Main independent inventory.json/semantic-checks.json/publication.json in THIS folder: all90 preserved B blobs and A ephemeral code independently checked; exact lock node sets/edges preserved. Changed nodes only client in B and client/runtime in both C consumers. Extension767dfd58/native/siblings/follows preserved.

Owning docs: A docs/reference.md; B docs/session-preparations.md,
docs/workspace-portal.md,docs/codex-package.md. Main applied the writing skill and
accepted original plain technical prose unchanged in the newer context. No product
UI labels changed. Newer recovery docs/sections are preserved. C needs no new
product prose for generated pins. Use current site operations codex-providers-aitherdev.md
and selected installed coordination/operations guide; obsolete old site guide stays removed.

## Verification artifacts and limits

Architect collection-probe-plan.md binds exact clean B556a6/treecd572. Three executable
prototypes unchanged from original; syntax/compile-only PASS19.669s. Source-compatible
actual Collector plus production HTTP202/reservation/durable handoff during sweep,
preparation/switch-effect exclusion. Effects at activation boundaries are inert;
this does NOT prove native conversation completion during that sweep or real activation.
New retry workers decline nil-Codex/RecoverSessions=false fixture. Stronger native/
browser usability is a separate packaged VM lane. Review coverage inventory limits.

verify-native.sh is HEAD/catalog-only rebound to A6e469; old script retained.
Actual running native binary SHA5e538... and catalog049042... unchanged. Runner has
not executed on refreshed head. verify-packages.py likewise changed only expected
client head; B exact head is an argument, results are per-head. Fresh long checks
follow review, using actual derivation/input receipts for reuse. Old all-six PASS
and native PASS are historical, not certification of the refreshed code/input graph.

Live smoke/discovery artifacts remain source-compatible and compile-only. They
use the deployed private child and production namePreparation/modelSessionNameWithRetry/
accessor, with explicit discovered provider; they bypass HTTP admission and the
normalSessionName provider-resolution wrapper. Do not overclaim their scope.
They create no registered session. Actual provider availability, useful PHP name
within30s, empty loaded threads/cleanup, portal health and ordinary conversation
identity continuity remain post-activation gates. No live discovery/inference yet.

Automatic A/B CI ran after publication. The timestamped ci-snapshot.json records A
passed; B archive passed, fast failed and creation still running. Implementer1 is
diagnosing the exact workspacecodex cancellation-test failure read-only; no rerun
or source change is authorized. These results do not establish runtime readiness. C has no feature-push workflows. No CI rerun/wait is part of this
review. Old fixture failures and their diagnosed corrections remain preserved;
archive diagnostics capture evidence and are not a claimed cure of the original stall.

## Independent assignment and expected report

Overall risk HIGH: protocol/ownership/cleanup, cross-project dependency and deployed
state capability/forward-only package transition preservation. Same eligible retained
reviewer0 uses saved gpt-6.1-sol/xhigh/read_only, no override or fallback. Apply all
four lanes: general, architecture/repetition, scope/proportionality, risk/compatibility;
read mandatory-change-review skill and every applicable lane reference in full.
Review directly; no nested agents/source writes/tests/builds/CI waits/claims/deploy/
lifecycle actions. Read repository guidance first. Use actual committed code/series
and original review.md/review-resolution.md/review-attention.md/review-archive-diagnostics.md
for exact prior boundaries; do not rubber-stamp prior source claims.

Report severity/lane with concrete paths/commits. Assess preservation/conflict handling,
complete final history/pin consolidation and no-migration/state lineage explicitly.
Record original accepted residual limits; no new feature work is requested. If clear,
say no findings and list pending exact-head native/package/VM/build/live gates.
Retained read-only instructions may prevent writing report files; return complete
report text for main to save verbatim in this folder/review.md. Deployment and final
integration authority remain separate; grant neither from code review.
