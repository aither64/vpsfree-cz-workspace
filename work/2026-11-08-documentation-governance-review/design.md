# Documentation governance: findings and implementation brief

Status: approved implementation scope; D2 release brief, 2026-11-09.
Design owner: architect0. D1 findings below remain the investigation baseline.
The lead's D2 assignment records the user's authorization, "ok, implement it",
after acceptance of the proposal and explicit directory/file structure. This
authorizes P1–P3 and documentation of optional editor-package pilot conventions.
It does not authorize a new role, catalog/runtime changes, package deployment,
integration or session lifecycle actions. Architect0 edits this design only;
implementation owners and release conditions are recorded below.

## Recommendation

Keep documentation with the implementer who understands the behavior, make the
README an entry point, and give independent review seven concrete placement and
fidelity questions. Adopt an explicit directory convention with mappings for
existing repositories. Pilot an optional documentation editor for substantial
reorganizations or multiple audiences; do not add a permanent default writer or
another mandatory review stage.

The existing rules already require placement, completeness, supported upgrade
guidance, and independent documentation review. The additions should make those
rules easier to apply, rather than repeat them in more places.

## Evidence and limits

Identity was checked with `dev-session current`; both environment variables match
the trusted binding to `2026-11-08-documentation-governance-review` and
`/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster identifies
architect0 as Astra/xhigh, design purpose, workspace_write. No peers were used.

These are observed local remote-tracking snapshots, read with `git show` from
canonical bare repositories. They were not refreshed over the network and are
not a claim about today's live remote tips. Bare repository `HEAD` differs and
omits some named examples; it must not be confused with the observed default
remote-tracking ref.

| ID | Repository/ref | Exact inspected head |
| --- | --- | --- |
| O | vpsadminos, `refs/remotes/origin/staging` | `4bfed8ba8ddfec49e5a3909df5ede733ea762c99` |
| C | vpsfree-cz-configuration, `refs/remotes/origin/master` | `1072f89f932ad570fb6d14007387d230549ccd14` |
| G | generic dev-workspace, `refs/remotes/origin/master` | `32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6` |
| S | vpsFree dev-workspace extension, `refs/remotes/origin/master` | `f8da821e3c76e26e73aa9d89a712eab0e0faa319` |
| W | coordination workspace, inspected `HEAD` | `527362b66eb903819ccb13ebb1e62495887195ca` |
| F | confctl, revision linked from O README | `822c0e35dbe2549111912f539116b4225dfd3035` |

The installed documentation skill matches G byte-for-byte. The installed review
skill, general-review reference, and site writing skill match S byte-for-byte.
Workspace procedures and the two project AGENTS files were read. Evidence is
limited to current guidance, the named README material and relevant linked docs,
and a small role-support check. No historical author/reviewer audit, application
verification, package build, or production inspection was performed. Therefore
this identifies present structural gaps, not why a particular past review missed
something or whether every documented operational fact is currently deployed.

### What the rules already say, and what remains weak

1. **Placement is already required.** G
   `skills/dev-session-documentation/SKILL.md:66–104` distinguishes behavior,
   reusable operations, supported upgrades, and individual rollouts. W
   `docs/agent-instructions/documentation.md:27–65` applies it locally. S
   `skills/mandatory-change-review/references/general-review.md:80–97` explicitly
   checks placement as well as completeness. Mixing one rollout's state into
   feature reference is contrary to existing policy, not an authorized category.
2. **README scope is unspecified.** G skill `:21–25` asks for README or index
   links, while `:94–96` defers to existing layouts. Neither establishes what a
   root README is for or when topic details should move out. “Smallest useful
   update” plus an easy README append can plausibly encourage accumulation;
   that is an inference, not proven historical causation. The repository rules
   O `AGENTS.md:6,70` and C `AGENTS.md:53–59` also give no README content contract.
3. **Review asks for paths but not an explicit routing conclusion.** S review
   skill `:164–168` requests changed/checked docs and separate rollout links;
   the general lane can reject bad placement. There is no short required answer
   identifying the audience, applicability and support lifetime of moved
   material. Stronger evidence can fit the existing packet/report without a new
   reviewer or form system.
4. **Operational titles do not establish lifetime.** C
   `docs/operations/aitherdev-disk-retention.md:94–104` combines rollout wording
   with lasting deletion/rollback limits. C `docs/operations/mx2.md:70–76`
   describes a CentOS-to-NixOS transition and queue obligations that may remain
   necessary after one rollout. Their current support boundary is not stated.
   Removing all “deployment” text would lose required recovery knowledge.
5. **Existing ownership is sensible.** W `docs/agent-teams.md:108–115` assigns
   technical documentation and evidence to implementers, packet completeness to
   the lead, and independent review to a read-only reviewer. S review skill
   `:41–51` excludes substantive authors from reviewing their own change. S
   `skills/vpsfree-user-facing-writing/SKILL.md:19–39` requires facts first,
   factual-drift comparison, and the rewrite by the context-owning agent.

## Approved directory and README contract

Use the following convention for new material; existing well-defined subsystem
homes are explicit equivalents. Create directories only when they have content.
No per-page front matter, fixed document bundle, or wholesale move is required.

```text
project/
  README.md                         purpose, basic start, grouped docs links
  docs/
    index.md or README.md            existing renderer's index; choose one
    reference/<topic>.md             supported behavior, constraints, rationale
    how-to/<task>.md                 user/developer tasks with the product
    operations/<service-or-task>.md  maintained operator/maintainer runbooks
      upgrades/<from>-to-<to>.md     supported transitions, including rollback
  # Existing equivalents retained:
  # vpsadminos: docs/os/, docs/osctld/, docs/user-guide/, docs/containers/
  # configuration: configs/<component>/README.md for local config reference

coordination-workspace/
  work/<slug>/{plan,state,design}.md  intent, current evidence, proposals
  work/<slug>/rollout.md             one rollout's exact steps/results/recovery
  archive/<slug>/...                 retained records after authorized archival
  notes/<project>/<dated-topic>.md   reusable workspace development lessons

deployment-repository/              only if its local policy permits records
  docs/deployments/YYYY-MM-DD-<topic>.md  one historical execution, not a runbook
```

The configuration repository expressly prohibits deployment receipts and
`docs/operations/releases/` (C `AGENTS.md:53–59`). For that repository use session
records, never the optional `docs/deployments/` destination. This local rule
overrides the generic allowance for dated deployment records. Raw logs and
generated output remain disposable artifacts under existing retention policy.

The root README contains purpose, intended users, major components, basic
requirements/start commands, and grouped navigation. A brief prerequisite or
warning needed to use the basic start safely stays beside it. Specialist test
profiles, CI implementation details, operational sequences, migration plans and
execution evidence go to their named destinations. Short descriptive links are
good navigation; they are not pollution merely because their destination is ops.
There is no arbitrary line limit.

Reference explains what the supported system does and why. How-to explains a
user/developer task. Operations explains how maintainers administer a deployed
service or development infrastructure, with prerequisites, expected results and
failure handling. A runbook may include concise local configuration facts needed
to operate safely; link to fuller authoritative reference instead of duplicating
it. Application transaction rollback remains behavior; reverting deployed
software remains operations. Classify mixed paragraphs by meaning, not by title.

Use stable topic/task filenames for maintained docs; use dates only for execution
records. Scope upgrade filenames/headings to actual source/target releases or
state boundaries, not invented version numbers. Keep a supported upgrade until
the owning maintainer explicitly retires the path with evidence covering old
state, backup restore and rollback. Unknown retirement evidence means retain and
mark applicability unresolved. A completed rollout alone does not end support.
Historical records stay historical rather than being updated into current advice.

This clarifies rather than contradicts G skill `:94–96`: a default routing
convention and explicit existing mappings do not mandate a file per category.
Add that clarification to the canonical generic skill; keep the
specific repository mapping and C receipt prohibition in local guidance.

## Concrete placement for the requested examples

| Observed material | Approved home and README treatment | Preservation requirements |
| --- | --- | --- |
| O `README.md:62–78`, Explicit ZFS Full Suite | Move the commands to an `Explicit ZFS full suite` subsection of existing `docs/os/testing.md`, beside running tests (`:203–253`); root README links to Testing, optionally mentioning explicit long ZFS runs in that link. | Preserve explicit opt-in, exclusion from default `-t ci`, profiles, unique run IDs and state isolation. Verify examples against the runner during implementation. `mkdocs.yml:48` already exposes Testing. |
| O `README.md:143–157`, Automated flake updates | New `docs/operations/flake-updates.md`; one Maintainer operations link in README and a navigation entry in `mkdocs.yml`. | Keep repository workflow details, final-lock baseline check, ordinary push, fresh baseline on target movement, and cache behavior. Keep F `docs/flake-inputs.md:153–288` authoritative for shared guard semantics; do not copy its contract. Preserve pinned link initially; changing its version policy needs compatibility evidence. |
| C `README.md:74–86`, three separate headings | Replace with one Documentation section grouping Configuration and Operations links. Link `configs/vpsadmin/api/README.md` directly and a new `docs/operations/README.md` containing the Mail, Aitherdev and API OAuth entries. | Maintain discoverability; do not remove short links as though they were embedded runbooks. Add navigation to the existing docs renderer only if that site exposes these operator docs. |
| C `configs/vpsadmin/api/README.md:24–166`, abuse parser details | Retain file overview at `configs/vpsadmin/api/README.md`; move substantial parser behavior to `configs/vpsadmin/api/abuse-notices.md`. Move operator checks/reprocessing steps to `docs/operations/vpsadmin-abuse-notices.md`, with reciprocal links. | Provider matching, historical assignment, disclosure, partial success, lack of retry/deduplication, mail deletion and irreversible notifications remain reference facts. The runbook repeats a short safety prerequisite and links them; do not bury those guarantees in a rollout record. |
| C API README `:3–4` → `docs/operations/vpsadmin-documentation-oauth.md` | Keep the existing site runbook and link from operations index. Its first-setup vs ordinary-upgrade distinction (`:19–29,257–270`) is a useful positive example. | Preserve client/key reuse, coupled package/hook compatibility (`:13–17`), log-protection ordering, credential handling and rollback (`:300–319`). “Generate once” is still maintained setup, not proof of one historical rollout. |
| C `docs/operations/mx2.md:3–68` | Keep service policy, isolated-check scope, recurring deployment prerequisites and diagnosis in the existing runbook. | Keep real-network verification limits, ACME gating, absent milter, opportunistic TLS and backscatter limitation explicit. Fixture details are reusable verification guidance, not execution evidence. |
| C mx2 `:70–76` | Extract transition-specific steps into `docs/operations/upgrades/mx2-centos-to-nixos.md`; retain queue paths and ongoing recovery cautions in `mx2.md`, linking the transition. | Preserve both queues, drain/recovery obligations and no unverified queue-copy assumptions. State source/target and supported recovery applicability. Do not retire without owner evidence; exact one-run progress stays in its owning session. |
| C `docs/operations/aitherdev-disk-retention.md:3–92,101–104` | Keep maintained policy, inspect/apply, ownership rules and irreversible-deletion recovery in place. Rename final section to Maintenance and recovery. | The user-profile runtime remains the coordination-policy authority (`:78–92`). Keep deletion limits, holds, uncertainty and manual-store-removal prohibition. |
| C Aitherdev `:9–11,94–99,106–113` | Separate initial declarative adoption prerequisites from routine verification. Where still supported, place initial transition in `docs/operations/upgrades/aitherdev-declarative-cleanup.md` and link it. Describe archive compaction as a separately invoked maintenance procedure, linking its owner. | Do not label these as executed history without evidence. Retain legacy executable backup handling and archiveRecoveryPolicy 3 prerequisite until supported transition/recovery ends. Particular activation results belong in session rollout records. |

Moves must preserve old anchors or leave short forwarding links where callers
may depend on them. Do not generate links to private session records as the only
home for public supported behavior. This mapping is a content plan, not a claim
that the operational examples have been executed or verified here.

## Seven independent-review acceptance questions

Use the existing general lane and packet, not a new review stage. For affected
documentation, the reviewer answers these with paths/sections and any exception:

1. Can a reader reach the explanation from the README/index, and does the README
   stay within the entry-point contract?
2. Does each changed passage have the right audience, owner and home: reference,
   how-to, reusable operations, supported upgrade, or individual execution?
3. Would current reference still make sense after this initiative is finished,
   without branch status or private session context?
4. Do commands, behavior, examples and stated verification agree with the final
   source and evidence, distinguishing prepared, tested and deployed claims?
5. Have moves preserved every consequential prerequisite, failure/partial-success
   condition, compatibility restriction, data-loss warning and recovery step?
6. Are upgrade applicability and retirement conditions explicit where relevant,
   including old persisted state, restoration and rollback; is unknown evidence
   disclosed rather than treated as retirement permission?
7. Is there one authoritative explanation per contract, with working links and
   anchors, and do prose edits preserve factual meaning and required writing rules?

The implementer's packet needs only a compact inventory: changed topic → reader
and class → authoritative path/link → evidence or unresolved applicability.
Existing packet paths and checks can carry it. The reviewer records a placement
and preservation conclusion, naming exceptions, rather than only “docs checked.”
No-update cases retain the existing short justification. Apply existing
severities by consequence: a lost queue-recovery instruction can block delivery;
a harmless heading preference is advisory. Do not require universal front matter,
generated inventories, extra reviewers, or review of routine session findings.

## Dedicated editor versus reviewer

| Responsibility | Owner and timing |
| --- | --- |
| Technical truth, rationale and command semantics | Implementer throughout implementation; architect resolves consequential design and applicability questions. |
| Reader/routing choices and docs package boundaries | Design owner in the implementation brief; lead accepts scope and ownership. |
| Optional structural/editorial work | A context-equipped implementer/editor on assigned documentation files once contracts are settled; it reports proposed factual changes rather than inventing them. |
| User-facing final rewrite | Context-owning main agent/lead applies the site writing skill directly after facts settle and before commit; a specialist can advise or audit. |
| Independent adequacy and fidelity judgment | Existing independent reviewer after intended changes are committed and quick checks pass. The editor cannot independently review its own contribution. |

An editor is useful for a substantial docs reorganization, a feature spanning
several reader groups, sustained bilingual work requiring editorial expertise,
or repeated placement failures despite the checklist. It is unnecessary for a
short correct paragraph, routine pin update, or every session. Benefits are
focused navigation and consistency work; costs are another context transfer,
file ownership coordination, lead factual acceptance, and possible serial delay.
The largest risk is fluent wording that dilutes failure or compatibility meaning.
Supply the editor with the settled brief, exact source, technical-owner contacts
and a protected fact/command inventory; require a factual diff check.

The runtime already supports named specializations. W `docs/agent-teams.md:3–28`
and `config/agent-teams.nix:46–68` separate role identifier, behavior, purpose and
instructions. G `portal/internal/teamruntime/runtime.go:208–228` accepts a custom
identifier with known behavior/purpose, nonempty retained instructions, and
compatible access. G `portal/internal/web/creation_test.go:173–190` explicitly
tests a custom `scribe` role. An editing `editor` role can therefore use existing
implementer/implementation behavior and workspace_write; an advisory specialist
can use general/read_only. No new `documentation` purpose or runtime subsystem
is needed. A role configured as review would be eligible for ordinary review
selection and must not simultaneously become the author.

This is source-supported capability, not a live new-role launch test. No default
editor is in the inspected site lineup. Adding a selectable role would require
an approved catalog change and normal package delivery; adding/reconfiguring a
retained member requires explicit user direction. Existing saved settings and
capacity limits stay intact. Prefer a bounded documentation package to an
existing implementer first. Any later specialist must receive sufficient task
context; it does not displace main-agent writing requirements.

## D2 implementation release

Identity and the live same-session roster were rechecked on 2026-11-09.
Architect0 retains Astra/xhigh and workspace_write. Implementer0 through
implementer3 retain Sol/xhigh, implementation purpose and workspace_write.
Applicable workspace procedures and installed documentation/review skills are
unchanged from the copies read for D1. Their unchanged guidance is reused.

The relevant contracts are settled: the directory tree, existing-layout
equivalents, README boundary, seven review questions, supported-recovery
preservation, factual ownership and editor limitations above. P1 is split into
disjoint source packages P1a and P1b. P2 and P3 can proceed independently of P1's
source edits: this design supplies their agreed contract. Unknown historical
retirement evidence does not block rearranging docs while retaining the path;
it prohibits retiring supported instructions or asserting that support ended.

The lead accepts these release boundaries and creates/registers worktrees
serially before dispatch, avoiding shared manifest races. Each implementer reads
this final convention and its repository's AGENTS/procedures, refreshes its own
source baseline and reports material differences before changing the accepted
scope. D1 SHAs are evidence snapshots, not required implementation bases.
All implementation edits and commits use session feature branches/worktrees,
including workspace guidance. Shared-master tracking is lead-owned. Architect0
does not create worktrees, edit implementation files or allocate peers.

| Package / owner | Exclusive implementation files | Acceptance and checks |
| --- | --- | --- |
| P1a — implementer0 | Generic dev-workspace: `skills/dev-session-documentation/SKILL.md`, `docs/dev-sessions.md` Documentation during development section. Workspace: `docs/agent-instructions/documentation.md`, `docs/agent-teams.md`. | Document the concrete tree and README contract, existing-layout equivalence, supported-upgrade lifetime and local receipt prohibition. Keep generic placement authoritative; site mappings and optional editor-package conventions remain local. Preserve context-owner/main-agent writing, independent review and lifecycle rules. Check cross-document consistency, relative links/anchors, Markdown and repository-required hooks/docs checks. |
| P1b — implementer1 | vpsfree-dev-workspace: `skills/mandatory-change-review/SKILL.md`, `skills/mandatory-change-review/references/general-review.md`. | Add compact placement/fidelity inventory to the existing packet and seven acceptance questions plus explicit placement/preservation conclusion to the general lane. Preserve reviewer independence, review timing, adaptive lanes/severities, narrow-fix policy, whole-branch history and migration checks, and planning/evidence exemption. No extra review gate or required metadata system. Check links and consistency against the accepted design and P1a destinations; run applicable Markdown/hooks checks. |
| P2 — implementer2 | vpsadminos: `README.md`, `docs/os/testing.md`, new `docs/operations/flake-updates.md`, `mkdocs.yml`. | Apply the two O mappings above, preserving commands, explicit ZFS opt-in/profiles/isolation, guard/cache/publication semantics, pinned shared-contract link and old entry points. Inspect the current runner/workflow for factual equivalence. Check moved-content inventory, links/anchors, navigation and the repository's docs build. Do not run the ZFS suite solely for relocating text. |
| P3 — implementer3 | vpsfree-cz-configuration: `README.md`, `configs/vpsadmin/api/README.md`, new `configs/vpsadmin/api/abuse-notices.md`, new `docs/operations/README.md`, new `docs/operations/vpsadmin-abuse-notices.md`, existing `docs/operations/mx2.md` and `docs/operations/aitherdev-disk-retention.md`, and transition pages `docs/operations/upgrades/mx2-centos-to-nixos.md` and `docs/operations/upgrades/aitherdev-declarative-cleanup.md` where the mapped transition content warrants them. | Apply all C mappings above; preserve factual contracts, discoverability and recovery. Keep the linked OAuth runbook unchanged, checking its new index link. Retain transition requirements when retirement evidence is absent and state their scope honestly. Do not introduce deployment receipts. Check before/after fact/command inventory, links/anchors and existing docs rendering where applicable. No production commands or configuration builds solely for text relocation. |

These are complete packages through documentation, quick checks, commits,
publication and review fixes under ordinary repository procedures. Additional
renderer/navigation files beyond the named boundaries need lead coordination;
do not expand into a broad historical cleanup. No runtime, catalog, executable,
configuration-input or unrelated documentation changes are in scope.

All four owners may ask architect0 routine technical questions directly using
the existing same-session peer transport, their actual sender address and new
stable message IDs; retry uncertain delivery with identical IDs/text/options.
Implementer0 and implementer1 are peers for authoring/review wording alignment;
implementer2 and implementer3 may clarify concrete routing with them or architect0.
Each keeps its named files. Consequential design changes, overlapping ownership,
new scope and approval-bound actions go through the lead. Lead owns plan/state,
portal, worktree/branch registration, final packet completeness, acceptance and
user-facing synthesis; architect0 owns design and technical clarification only.

Each completion report includes exact base/head and published branch, changed
paths, compact topic → audience/class → authoritative home inventory,
before/after preservation evidence, commands/results, remaining gaps and
whole-branch history/migration provenance (expected: no migrations). The lead
applies the required main-agent user-facing writing pass after technical facts
settle and before committing affected user-facing prose; owners coordinate that
pass rather than substituting a context-poor editor. Implementation readiness
requires the seven questions to be answerable and all required quick checks to
pass, not just moving text successfully.

Final independent review follows intended commits and quick checks, before any
necessary long checks. Longer docs builds use the ordinary watcher and review
ordering when applicable. No new tests merely restating wording are needed.
Keep logical repository changes separately reviewable. Feature publication and
review do not authorize default-branch integration.

Optional editor-package pilot conventions are part of P1a's team guidance only:
use an existing implementer for an explicitly scoped docs package when the
triggers above justify it; preserve technical-owner and main-agent responsibilities.
Lead may evaluate placement rework, factual corrections and coordination cost
from ordinary evidence. This work does not launch a separate pilot, add a
persistent/selectable role, change the roster/catalog or introduce telemetry.

No data schema, API, generated client, protocol or executable behavior changes
are proposed. Documentation paths/anchors and procedural meaning are the
compatibility surface. Preserve supported mixed-version and rollback contracts
through moves. If approved changes prove misleading, revert the documentation
commit or repair links; never infer operational rollback or cleanup permission.
Generic installed skill changes require a later, separately authorized package
rollout before they reach installed users. Package deployment is outside this
implementation release; completion reports must distinguish prepared source
from installed policy. Workspace text applies when read, while retained member
prompts do not automatically refresh (W `docs/agent-teams.md:228–237`). Do not
change this session's roster or lifecycle as part of delivery.

Settled and sufficient for release: user-authorized scope, routing/mappings,
review requirements, preservation invariants and the four exclusive owners.
Remaining before dispatch: lead worktree preparation and package acceptance.
Source freshening, factual/link checks and committed delivery belong to each
implementation owner. No further architect investigation blocks these packages;
legacy-transition uncertainty is handled by preservation, not unsupported
retirement. Integration, deployment and lifecycle actions remain outside scope.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-documentation-governance-review/
