# Final repository instruction review packet

Session:2026-10-19-vpsadmin-kernel-cves (verified exact thread/env ownership).
Repository:security-advisories; owned worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories`.
Target/default:`origin/2026-07-13-security-advisory-automation`, notmaster.
Base:`ea6247687fd02417f87e1e5593fecd8b9055925d`.
Final head/quick checks will be appended before assignment.

## Requested outcome

User requested a reusable selection process in repository instructions/skills,
including high-threat CVEs even if vpsAdminOS was not vulnerable so members can
see evidence-backed non-applicability. Research selection remains separate
from later user-approved dossier/draft creation. No drafts have been authorized.

Acceptance:canonical `docs/cve-selection.md`, mandatory AGENTS routing and README
entry point; reproducible inclusive graph/fix/CNA enumeration, exact prior-report
and accessible private-draft dedup, later assignments/corrections/rejections,
formal score separate from threat and member relevance, positive scoped negative
evidence vs unknown, runtime/history/roles and partial coverage, prior claims and
policy/proposal revisions, explicit selection/draft/publication/email boundaries.
Must preserve existing `docs/evidence.md` conservatism, supported evaluator states,
coherent snapshots and publication guards. No new evaluator enums/schema.

Scope:only AGENTS.md,README.md,docs/cve-selection.md. No implementation, schemas,
dossiers, evaluations, API/service writes, exploits, deployments or workflow edits.
A new skill framework was rejected as unnecessary:existing repo instructions
can route to one canonical document. Research artifacts under work/ are context,
not deliverables in this branch. Lead applied context-owning factual prose check.

## History/migration inventory

Intended split:one logical docs/instruction commit. Three files implement one
canonical method and its mandatory/documentation entry points. Full base-to-head
series and final diff will accompany assignment. No prior branch iterations or
obsolete approaches; no dependency/channel/generated-artifact update streams.
No migrations, persisted-state/API/protocol/configuration/runtime changes, no
release or deployment consumption. No supported path removed. No integration
or deployment is authorized; retain branch.

## Review settings and lanes

Risk:High for security assessment instructions and approval/evidence claims;
changes are documentation only and reversible, but bad guidance can produce
false not-affected claims or unauthorized writes.
Retained reviewer0:independent saved review-purpose gpt-6.1-sol/xhigh/read-only.
Use exact saved settings, no model/effort overrides.
Lanes:general,scope/proportionality,risk/compatibility. Read mandatory-change-review
skill and each lane reference. No architecture lane: no implementation logic,
new framework, interface or component abstraction changes.

Assess full committed branch yourself; explicitly conclude on whole history,
no migrations and no repeated update streams. Check scope/proportionality,
evidence contract consistency and phase/approval semantics. Do not review the
research candidate list as a final dossier assessment; no early research review
requested. No source edits, nested reviewers, merges or publication.

Return Blocking/Important/Advisory findings or clear no-findings conclusion with
residual limits. A requested narrow fix will be delegated to its implementer;
lead accepts focused fixes under skill without automatic full rerun.

## Verified final committed range and checks

Head:`69027fd51efc5c7eb0a4711947b4f9d08190940e` (lead rev-parse verified).
Complete series:one commit `docs: define kernel CVE selection before advisory drafting`.
Final diff:AGENTS.md,README.md,docs/cve-selection.md only,238 insertions/2 deletions.
No migrations, repeated update streams, generated artifacts or obsolete history.
Worktree clean. No push/integration yet. Read complete diff with:
`git diff ea6247687fd02417f87e1e5593fecd8b9055925d..69027fd51efc5c7eb0a4711947b4f9d08190940e`.

Implementer evidence:normal Nix bundle/hook installation passed;
`nix develop --command bundle exec overcommit --run` RuboCop and all precommit
hooks passed; normal hooked Nix git commit passed. Body TextWidth advisory2lines
>72 but all<=80 required. Eight local Markdown links/newlines/whitespace and
base-to-head `git diff --check` passed. No new tests or full Ruby suite for the
pure instruction/documentation change; no runtime behavior affected.
