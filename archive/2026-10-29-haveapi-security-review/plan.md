# 2026-10-29-haveapi-security-review

## Goal

Perform an independent defensive security regression review of the HaveAPI
changeset requested by this workspace's owner. User specifically authorizes this
new workspace session using their Codex subscription and Daybreak Blue, xhigh.
Use provider openai (Codex subscription), model gpt-daybreak-blue-latest/xhigh;
verify actual configured/native identity and report any mismatch before analysis.
Work in solo mode; do the independent reasoning yourself, no added team members
or nested auditors. Use the haveapi-security-audit skill, read its full SKILL.md
and applicable workspace/repository instructions. Verify your own session current
and thread binding before session-owned work. Leave this session open.

Repository git@github.com:vpsfreecz/haveapi.git, canonical bare clone
/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git. Audit exact published head
ae46cf27a9afb6558d386c293cec7231dd6c423d,
tree27dcf148f9b03867a3dfc65a29c76e77a87682ec, comparison base
f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0. Full five-commit changeset:51073383
core documentation redesign,78ab264a optional documentation OAuth,2f6c18a8
performance contracts,1b264e25 example formatting,ae46cf27 formatting instructions.
Prior reviews/checks/development deployment do not replace this independent
security review. Focus on introduced regressions and related unchanged code
needed to understand the boundary; distinguish pre-existing behavior.

The user later expanded reporting to every confirmed security bug found within
this reviewed boundary, not only regressions. Pre-existing findings therefore
receive the same evidence and remediation treatment, while remaining explicitly
classified against the comparison base.

Prepare your own isolated same-session worktree from exact head, ordinary hooks
and declared Nix/Ruby environment; keep initial plan/state and review scope under
your own session. Do not read another session's records, worktree, roster,
transcripts or private state. Source objects are available from the shared bare
repository. No cross-session communication permission is granted by this brief;
report your progress/findings in your own conversation and portal. The initiating
session2026-10-27-api-documentation-redesign remains separate; no access/merge/
deployment authority is transferred. The user can read your session directly.

Review changed server documentation dispatch/rendering and OAuth/session code,
related authorization/description filtering and per-request identity cleanup,
HTML/JS/sample-data escaping and cache isolation, parser/error handling and
client-example literal correctness. Follow the skill's evidence requirements.
Use only synthetic local fixtures and existing local regression helpers. Keep
all audit artifacts under your checkout vulnerabilities/, with one directory
and reproducible local regression example/report for each confirmed finding.
Do not modify existing repository files or apply fixes, commit/publish findings,
run external/live/devcluster requests, access credentials, merge/rebase/deploy,
or perform session lifecycle cleanup. Do not claim a vulnerability from source
suspicion alone; locally validate material findings under the skill. Preserve
unconfirmed leads internally and state coverage limits honestly. No broad
unrelated subsystem audit or new framework/dependency project.

Give meaningful progress as boundaries are assessed; do not impose an arbitrary
short time budget. At completion provide severity-ordered confirmed findings
with exact source lines, prerequisites/impact, local reproduction command/result,
introduced/pre-existing classification and proposed remediation without applying
it. Or state no confirmed security regressions, identifying concrete coverage and
limits. Record exact audited range, model/provider/effort, clean tracked source
and reconciled owned check processes. Findings/evidence are audit records, not
new application deliverables requiring an automatic nested review. Default merge,
release/production/deployment and lifecycle actions are outside scope.

## Corrected-head re-audit addendum

After the initial report, the owning implementation session published corrected
head `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b` (tree
`30efb19e02a756036771767745a9858fe968f95b`) with direct parent
`ae46cf27a9afb6558d386c293cec7231dd6c423d`. This session will independently
re-audit that exact head using a second isolated same-session worktree. The
bounded delta comprises the Ruby CLI and curl example renderers, their new shell
regression spec, and the client-example documentation.

Re-run the four original VULN-01/VULN-02 exploit cases against the corrected
head, inspect the complete direct-parent delta for escaping or semantic
regressions, and locally assess the adjacent unchanged
`clients/ruby/lib/haveapi/cli/example_formatter.rb` copy/run boundary. Report a
third finding only if synthetic local execution demonstrates material impact.
Preserve every original restriction: solo reasoning, no peer worktree/records,
no source fixes, no live/credentialed target, no publication/integration/
deployment/lifecycle action, and one evidence directory per newly confirmed
finding.

## Second corrected-head re-audit addendum

The owning implementation session subsequently published exact head
`aee093cd3387c261570067e58b7f1e16029e3619` (tree
`295f884f0b2a8257883e82197fad3d8821c251ca`), direct parent
`a3f522e509faaf9da34d9e87c7f7e9246c76bd6c`, two commits above previously
audited `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b`. This pass independently
reviews the eight-path VULN-03/VULN-04 correction, reruns all prior synthetic
PoCs, and verifies exact request argv/JSON, hostile response visibility and
shell inertness, and the retained whole-block Copy contract. It keeps the same
solo, read-only, local-fixture, no-live-target and no-lifecycle boundaries.

## Affected repositories

- `haveapi` only, from the canonical bare repository at
  `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`.
- Audit comparison: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0..ae46cf27a9afb6558d386c293cec7231dd6c423d`.
- Expected audited head tree: `27dcf148f9b03867a3dfc65a29c76e77a87682ec`.
- No application source changes, fixes, publication, integration, deployment,
  or cross-session access are authorized.

## Approach

1. Verify the current session binding and native provider/model/effort before
   reading source.
2. Record this session's scope, then create a registered isolated worktree at
   the exact published head without fetching, rebasing, or reading another
   session's checkout.
3. Read repository-local instructions and establish the declared Nix/Ruby test
   environment and ordinary hooks without changing tracked source.
4. Inventory the complete five-commit range and inspect changed documentation
   dispatch/rendering, OAuth/session handling, authorization/description
   filtering, request identity cleanup, HTML/JavaScript/sample escaping and
   cache isolation, parser/error handling, and generated client examples.
5. Trace each material lead across the necessary unchanged boundary. Compare
   head behavior with the base to classify introduced versus pre-existing
   behavior.
6. Validate any material lead locally with synthetic fixtures or existing
   regression helpers. A confirmed finding must have its own
   `vulnerabilities/VULN-XX/` directory containing a reproducible example and
   `report.md` in the audit-skill format. Unconfirmed leads are not findings.
7. Reconcile owned test processes, tracked-source cleanliness, exact audited
   revisions, coverage, limits, and final severity-ordered conclusions in this
   session's state and handoff.

## Decisions

- Solo review: no team members, nested auditors, cross-session communication,
  or access to the initiating session's records/worktree.
- Use only repository-local, synthetic requests and fixtures. No external,
  live, credentialed, or devcluster requests.
- Findings and PoCs are uncommitted audit artifacts. Existing repository files
  are read-only, and remediation is proposed rather than applied.
- Source suspicion is insufficient: only locally reproduced security impact is
  reported as a confirmed finding.
- The audit covers the supplied range and related unchanged code needed to
  establish the affected trust boundary. Per the user's follow-up, confirmed
  pre-existing bugs found there are reportable; this remains neither a broad
  subsystem nor a dependency audit.

## Compatibility and deployment

- Review-only work has no runtime compatibility or deployment effect.
- The comparison explicitly considers mixed request identities, documentation
  visibility, caching, generated examples, and old/new behavior at the exact
  base and head. No configuration or persisted-state mutation is authorized.
- Recovery consists of stopping any owned local check process and retaining the
  isolated worktree and uncommitted audit artifacts; the session remains open.

## Documentation

- Session intent and decisions: this plan and `design.md`.
- Current progress, commands, results, limits, and cleanup evidence: `state.md`.
- Confirmed issue evidence only: one directory per issue below the HaveAPI
  worktree's `vulnerabilities/` directory.
- No project documentation change is useful because this is a read-only audit.

## Testing plan

- Quick integrity checks: verify exact commit, tree, ancestry, five-commit
  series, tracked cleanliness, repository hook declaration, and available
  Nix/Ruby entry points.
- Targeted regression checks: use existing local helpers and narrowly scoped
  RSpec/standalone synthetic fixtures for dispatch/auth/filtering/escaping/cache/
  parsing/client-literal leads.
- For any confirmed flaw, run the exact reproduction from the Ruby server
  component as specified by the audit skill and capture the important result in
  its `report.md`.
- Stop when the requested changed boundaries have been traced and every material
  lead has either reproducible security impact or a documented internal
  disposition. Do not add unrelated full-suite or external verification.
- Corrected-head phase: first run the four original finding examples unchanged,
  then the repository's focused shell/example specs and only the directly
  relevant renderer/documentation checks. Exercise the adjacent CLI-help
  formatter with a fake local executable and hostile literals before deciding
  whether it is a finding.
