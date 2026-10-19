# Automatic session slugs: review packet

Status: all intended functional changes committed, quick checks passed; requesting
independent final whole-branch review. Integration tests and deployment await
finding reconciliation. Coordination artifacts follow the normal tracking cadence.

## Outcome and boundary

New session accepts the initial prompt with no typed short name. Options
allows an explicit custom short name. Existing date prefix and 48-character
limit remain. Forks, plan-created sessions and CLI names retain explicit naming.
The accepted raw prompt appears on preparation progress immediately, with
server-owned status/retry and eventual canonical session navigation.

The user chose model naming with file/network action tools disabled and
questions rejected immediately. Pure clock remains because pinned Codex
0.160.0 cannot hide it or its async question tool. No zero-tool claim, model
upgrade, Codex patch or arbitrary public configuration surface is authorized.
Global serving-instance user policy is trusted. Existing operator procedures
pause naming between MCP changes; no administrator-race framework is required.
The local development operator is trusted under both repository AGENTS files;
remote browser input remains untrusted. Assess filesystem hardening within
that stated boundary.

## Owned components and actual consumers

codex-web owns the additive RunEphemeralTurn API: trusted empty canonical
private cwd and separate empty private instruction file, exact model/effort,
bounded UTF-8 input/schema/instructions and final output. The helper creates
one private connection and ephemeral thread/turn, with a fixed restriction
recipe, bounded config/model discovery, pre-admission private rejection sink,
exact generation/thread/turn checks and cleanup within the caller deadline.
It does not use normal persisted resume/send/history/ledger paths. A unique
early identity may authorize interruption only, never success/adoption.

The current new consumer is dev-workspace's private session naming adapter,
using gpt-6-luna/low and at most 8192 raw UTF-8 prompt bytes. Server construction
provides its trusted socket; browsers cannot choose sockets, models for naming,
working directories, files or public utility config. The preparation worker
owns the ten-second whole budget, two-call limit, deterministic fallback and
package-generation checks. Existing normal codex-web clients and the reference
HTTP/browser component continue their established transport behavior.

The extension consumes runtime through its exact flake input. The workspace
consumer assembles that extension with site/team policy and both cluster
providers. Deployment uses its user profile. vpsfree-cz-configuration was
inspected; no system configuration change is needed by the observed contract.

## Persistence, compatibility and provenance

No database migrations, SQL schemas or seeds. New isolated private preparation
format1 and compact identity mappings coexist with unchanged receipt1/2/3,
manifest/journal and upload catalog1 readers. Accepted upload scopes use existing
pending submission retention before a slug exists. Old collection retains
those files; old CLI cannot honor new reservations, so newer recovery refuses
conflicting destinations/owners instead of adopting or discarding them.

Freeze request-ID input and expanded team policy before naming. SameID/sameinput
replays before catalog/upload lookup; changed input conflicts. Never evict an
admitted identity to admit a new request:512unfinished/10000total capacity.
Save name base, then immutable final slug, predetermined receiptID and epoch;
receipt handoff requires exact identity/request/team/epoch. Shutdown pauses
naming rather than committing fallback. Generation checks survive lock waits.

Preserve published but unmerged deployed ancestry: runtime4ef298b3 (cluster
schema1/policy3) and extension's four exact commits through399c3302. Their
original SHAs must remain. Whole default-to-head history includes them;
deployed-to-head diffs isolate this initiative's feature. They are already
consumed behavior, not abandoned iterations. No other owner's refs/records
were changed. Preserve all unrelated nested locks and both cluster providers.

Unpublished backend follow-up prose was folded into its owning commit before
publication; the prior8c0d3fc never deployed/consumed. Runtime own patches were
rebased onto4ef without conflicts; range-diff all equals. Neither that rebase
nor deployment grants default-branch integration approval. Final inventory
must list exact final heads, complete series, final diffs, and explicit whole-
branch obsolete-history and migration conclusions.

## Documentation

Owning helper API/operating limits: codex-web/docs/reference.md.
Owning preparation/recovery/browser contracts: runtime/docs/session-preparations.md,
docs/workspace-portal.md, docs/codex-package.md and test/README.md; entry pointers
in README. Main-context coordinator applies the user-facing prose skill.
Exact rollout/recovery commands and package/canary evidence belong separately
in this initiative's rollout.md; reusable failed-environment lessons in notes.
Design and reports are durable initiative artifacts linked from portal.yml.

## Review and release gates

Overall risk: high (private persisted state, upload retention/ownership,
experimental protocol tool restrictions, generation transitions and rollout).
Required lanes in one independent assignment:general, architecture/repetition,
scope/proportionality, risk/compatibility. Retained reviewer0 is unused,
read_only,gpt-6.1-sol/xhigh; verify live roster/settings before assignment and
omit overrides. Read mandatory-change-review skill and all four lane references.
No nested reviewers. Review scope, safety and proportionality directly;
request missing evidence rather than treating this packet as a conclusion.

Complete exact heads, series and final diffs are in [branch-inventory.md](branch-inventory.md).
Backend/helper quick evidence is in state and backend/utility reports. Provider
normal packaged mock CI passed at ca0f3bc9. Details of final quick evidence follow.
Schema/corpus/mocks/tagged compilation prove no exact-binary isolation by
themselves. Filesystem crash-gap states are covered; exhaustive injected
fsync/write failure coverage has not been claimed and is a known review gap.

Only after all intended changes are committed, quick checks pass and findings
are resolved/reconciled: packaged checks, race regressions, real Playwright,
exact old-source fixture, and exact assembled-candidate Codex binary fixture.
The latter must inspect unchanged provider/model capability catalogs, actual
tool schemas/dispatch, instructions/hooks/MCP sentinels, question/clock paths,
response-loss cancellation of an active provider continuation and persistence.
Failure must block enablement; fallback is not a substitute for that proof.

Assess the architect's source-based host-migration applicability conclusion in
[design.md](design.md#host-migration-applicability-for-runtime-51dca869) against
the final incoming diff. It finds generic tree preservation with no namespace,
rewrite inventory, host paths or authority contract change, rather than relying
only on matching policy numbers. No new extension host-migration VM trigger
is proposed; normal packaged migration/host-path checks remain required.
Forward-only profile switches; recovery uses a newer package retaining required
readers and prior behavior, never an earlier generation or state deletion.
Canaries use idle synthetic prompts and retain their sessions/refs. No archive,
delete, stop or merge authorization.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/>


## Exact final heads and commit split

See the [complete branch inventory](branch-inventory.md) and linked complete
committed final diffs. All four worktrees/indexes are clean. Upstreams fetched;
defaults unchanged. Workspace final source is based on current shared master
b9c2ef2b, whose inherited coordination commits are inventoried separately from
this initiative's pin-only incoming diff.

- codex-web: `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`.
- dev-workspace: `edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1`.
- vpsfree-dev-workspace: `c8f9ba36bbb0b346d2165229690015193ca97ac0`.
- workspace: `421edddb5efd0bce6a36f8acedef1cf6082c75ef`.

The helper is one public capability with its transport boundary, restrictions,
unit/schema/binary fixture and documentation. Runtime commits separate upload
reservation, preparation/receipt/CLI persistence, private naming adapter,
dependency selection/installed corpus, and browser request recovery/progress.
Tests/docs support each owning unit. Extension and workspace each have one
exact consumer-pin commit, preserving unrelated closure nodes.

Before review, the two-line missing policy installation was folded into the
runtime dependency commit (07a98d0 becomes4307b29). The browser commit becomes
edcfc18 with equal patch; old51-to-newhead final diff is only those two Nix
lines. No deployed/published ancestor4ef or399-series commit was rewritten.
Temporary f1f1c39 fixup and old07/51 are superseded unapplied feature versions,
not supported migration steps. Existing earlier backend superseded iteration
was also folded before publication. Require an explicit whole-history conclusion
on remaining obsolete approaches, compatibility paths and migration lineage.

No database or namespace migration is introduced. Preparation format1 and
compact mappings are introduced directly; no migration from an abandoned
preparation schema. Existing receipt1/2/3, uploadcatalog1 and authority schema
remain supported. Inherited cluster policy2-to3 ancestor4ef is already deployed
and externally consumed by extension399/workspace installed profile. Extension
maintenance/storage commits are also already consumed. Preserve their exact
identities and paths. The new feature itself has not been deployed, released or
merged. Real-binary evidence is still pending. Final source differs from the
architect's51 assessment only in the installed policy resource and commit IDs;
private state/migration source is unchanged.

## Final quick evidence

Use linked state/reports for exact commands, logs, prior failures and fixes:

- Provider complete mock package passed7.777s after early-identity cleanup fix;
  runtime five adapter groups passed7.1s. Config schema validates55fixed policy
  restrictions plus literal MCP enabled; protocol corpus and fast seven-case
  tool-schema parser passed. Tagged fixture compilation intentionally ran0tests.
- Stable backend web/uploads/session suites passed; Ruby creation/fork and
  reservation checks passed. Crash-gap states covered; exhaustive fsync/write
  fault injection remains a test gap for review to assess.
- Final browser five nonzero Go selectors passed(package0.998s), including
  shipped-browser API harness and optional-name/identity/legacy assertions.
  All15pure Node preparation contracts passed, with real legacy-upload evidence
  and fresh/attempted lookup rejection. Six JS syntax checks passed. Ruby
  regression16runs223assertions passed1.368544s.
- Final extension authority contract/corpus selectors:2runs149assertions,
  0failures/errors/skips(3.873312s). The first source invocation omitted the
  selected contract env; it was corrected to match package environment.
- Workspace deployment contract:4runs19assertions, no failures/errors/skips
  (1.429183s). Runtime and complete workspace package derivations evaluate.
- Full exported runtime-contract JSON equals deployed4ef, not only its numbers.
  Whole lock-node comparisons changed exactly provider/runtime in extension,
  and extension/runtime/provider in workspace; all other nodes equal baselines.
- Runtime first normal CI at51 failed only installation missing policy JSON;
  parent inspected its failed log and corrected source. Existing validator
  passed on reconstructed installed layout0.81s; final runtime CI run37146585009
  atedcfc18 is being independently watched. Do not treat that CI as real-binary
  tool-isolation proof. Complete final package suites remain a post-review gate.

Reviewer selection: retained reviewer0, purpose review, independent/unused,
ready/read_only, saved gpt-6.1-sol/xhigh; assignment omits overrides. No fallback.
All four lanes apply at high risk. Read actual instructions/references and
inspect code rather than accept packet conclusions. Pay particular attention
to user-authorized tool boundary, source-relative policy packaging, cleanup
under lost replies, one-owner persistent handoff/attachments, immutable browser
recovery, explicit custom-name domain and proportionality under trusted-operator
policy (including instruction-file link-count validation). Findings should
identify concrete supported failure or maintenance scenarios.

Return ordered findings with severity/lane/path/line/commit/evidence, residual
risks and direct validation needed. Explicitly conclude whole-branch obsolete
history and migration lineage, including “no migrations” as applicable. This
read-only reviewer must report_to_lead; coordinator records review.md. No app
edits, checks launching binaries/browsers/VMs, mutations, nested reviewers,
deployment, merge or lifecycle action by reviewer.
