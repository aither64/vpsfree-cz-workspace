# Final review: background document title notifications

## User scope and acceptance

User reported Codex waiting badge without title marker, requested investigation,
then a plan to fix and deploy aitherdev through vpsfree-cz-configuration, merge
and release after verification, and finally said "Implement the plan."
Accepted correction restores existing five-second attention-only polling while
hidden. Preserve unread ✓/native-blocking ? semantics, focused-only ack/presence,
hidden heavy-read pause, generation/identity/pagehide fences and no new protocol.
No Codex upgrade, server/store/schema migration, push infrastructure or session
lifecycle change is in scope. Release means exact aitherdev claim.

Workspace: /home/aither/workspace/ai/vpsfree.cz
Slug: 2026-10-26-document-title-notifications
Tracking: work/2026-10-26-document-title-notifications/{plan,state,design,rollout}.md
Worktrees: worktrees/2026-10-26-document-title-notifications/{dev-workspace,workspace,vpsfree-cz-configuration}

## Review assignment

Selected retained reviewer0, gpt-6.1-sol/xhigh, read-only, independent of authors.
Overall risk: high for composed host/profile rollout, deployment ordering and
mixed loaded assets; browser correction itself is bounded and compatible.
Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and all lane
references: general-review.md, architecture-review.md, scope-review.md and
risk-review.md. Perform review directly without subagents. Verify same-session
identity and saved settings first. Read workspace procedures and repo guidance.
No edits, tests/builds, deployment, merge or claims during review.

Review the complete base-to-head histories/final diffs, not only final commit.
Explicitly conclude history consolidation, repeated pin stream disposition,
migration inventory/provenance (no migrations), compatibility and scope.
Investigate findings within the supported operator trust boundary: local host
operator trusted; remote clients untrusted. Record concrete file/line evidence,
severity and lane. Do not add speculative infrastructure or test campaigns.

## Intended commits and ownership

Runtime: one focused browser correction commit with its matching tests/docs and
asset version; no obsolete branch approaches or repeated pin updates.
Workspace: one exact runtime input-selection update, composed lock generated.
Configuration: one generated channel update preserving confctl message/hooks.
Pins are separate consumer updates. No functional extension/codex-web changes.
No database migrations or persisted format changes anywhere; none was released,
deployed or externally consumed by this initiative before review.

Runtime owns title policy and its unchanged attention HTTP consumer. Workspace
composes the application through the existing extension; configuration selects
the matching generic host module via devWorkspace channel. Inspect actual
consumer locks and source graph. Extension and frozen system/runtime llm-agents
pins remain unchanged; system/profile Codex are intentionally distinct.

## Quick evidence

Runtime published ef85bd0ae50714dbce51ba5807c0234875212a53 over
7e6d7c9cdb3388ab7abc720c034c15c21afbd686, clean worktree.
Node attention suite 75/75 (8.5 s), changed JS syntax checks and targeted Go
Firefox fixture journal/readiness checks passed through repository Nix shell.
Nix package derivation evaluation and git diff --check passed. Precommit drvPath
is not final artifact proof. No declared runtime hook framework; no bypass.

Lead directly applied vpsfree-user-facing-writing/humanizer-en to the final
notification paragraph and Firefox procedure clarification before commit.
Behavior docs remain runtime-owned; this rollout evidence remains session-owned.

Long package/VM/native browser checks have not started before final review.
Deployment requires matching lock contract, built exact closures, machine claim,
host activation then user-profile switch. Integration approval covers all three
master targets; no repository claim during review/tests. See rollout.md for exact
aliases, predecessors and preparation; no deployment has occurred.

## Final ranges and consumer checks



### dev-workspace

Base `7e6d7c9cdb3388ab7abc720c034c15c21afbd686`; head `ef85bd0ae50714dbce51ba5807c0234875212a53`; target `refs/heads/master`.

```text
ef85bd0ae50714dbce51ba5807c0234875212a53 portal: refresh attention titles in background tabs
```

```text
 docs/browser-notifications.md                   |   6 +
 docs/workspace-portal.md                        |  11 +-
 portal/internal/web/attention_browser_test.cjs  | 153 +++++++++++++++++++-----
 portal/internal/web/firefox_tabs_acceptance.cjs |  60 +++++++---
 portal/internal/web/firefox_tabs_test.go        |  31 +++++
 portal/internal/web/static/session-attention.js |  13 +-
 portal/internal/web/templates/session.html      |   2 +-
 7 files changed, 218 insertions(+), 58 deletions(-)
```

Complete final diff: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-document-title-notifications/dev-workspace-final.diff`.

### workspace

Base `978a2f280185f3ae114c2db13130f13e6976b159`; head `6521561ff57caf84b7ddfa62eee59c7c47d62590`; target `refs/heads/master`.

```text
6521561ff57caf84b7ddfa62eee59c7c47d62590 inputs: select background title attention correction
```

```text
 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)
```

Complete final diff: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-document-title-notifications/workspace-final.diff`.

### vpsfree-cz-configuration

Base `880a6253f8d6cc1368e633f936b174792e86bff7`; head `c6fa188bfe10bf8acbe728ce8197b77e46705975`; target `refs/heads/master`.

```text
c6fa188bfe10bf8acbe728ce8197b77e46705975 inputs: set devWorkspace to ef85bd0a
```

```text
 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

Complete final diff: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-document-title-notifications/vpsfree-cz-configuration-final.diff`.

Consumer quick gate passed: deployment contract on final locks; Ruby contract
suite 4 tests/19 assertions; semantic graph node sets/edges and every sibling
node unchanged. Only runtime node differs in each lock, both selecting ef85bd0
and narHash sha256-yPBaMwSpf1354Q/qiZcgJq/C3EMxsuqtNZ69qYH45PI=.
Config Overcommit Nixfmt/RuboCop and generated message hooks passed. Workspace
Nixfmt check passed from pinned config shell; no workspace hook framework.
Clean worktrees, canonical SSH pushes and exact feature remote heads verified.
No long checks or deployments performed by this session.

Workspace was rebased from c00fa4b3..3b5050c81 onto local shared master
978a2f280. Final new range 978a2f280..6521561ff. Range-diff is one '=' patch;
base additions are four tracking-only commits under work/archive. Filtered
package source, flake blobs and candidate drv unchanged. Reviewer must explicitly
assess this equivalence, inherited tracking disposition and complete final
series (origin/master c00fa4b3 through final workspace head where relevant).
Old unpublished-to-default feature head was replaced using bound force-with-lease;
no old head was deployed. No superseded workspace workflows existed.

All three heads are now frozen for review. Store final report at
work/2026-10-26-document-title-notifications/final-review.md and report to lead.
