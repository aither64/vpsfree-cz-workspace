# Instruction change handoff

The reviewed instruction changes are fast-forward merged and published:

- Workspace master08b3c6f3ee2713004b8f9d22125ebbb15cb0db33.
- vpsfree-dev-workspace master3e5dc4681b0343ec236c3f3dfc0d6f725577c376.

User approval: "ok, merge it" in this conversation on2026-10-09, covering both
master targets. Fresh remote proofs are in integration.json. No rebase, new
commit or patch change was needed. The lead verified the current complete series
against final review, including the workspace's initial tracking ancestor.

Local checks, independent general/scope/risk review and exact feature CI37980203900
pass; packaged flake and development-cluster checks passed. No post-merge CI wait,
per the user's instruction. The clean temporary integration target was removed;
feature branches/source worktrees and unrelated shared changes are preserved.
No remaining authorized work or blocker; lifecycle is complete, session stays open.

The instructions require consolidation of superseded dependency/channel updates,
independent conclusions and evidence for necessary retained boundaries, plus a
lead check before any approved merge. Required deployed behavior, migrations,
source refs and merged-history protections remain. Rollout records retain
execution provenance. Details: review.md, inventory.json and final diffs.

Canonical review skill source is merged. The installed Nix skill bundle is
unchanged; no package update, deployment or downstream pin change was performed.
