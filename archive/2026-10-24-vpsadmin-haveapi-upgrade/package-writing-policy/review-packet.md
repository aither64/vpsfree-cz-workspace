# Shared writing policy: final committed review packet

Source complete and quick checks passed; independent final review pending.
Lead owns reviewer assignment and session state. No long checks or publication
have run for this package.

- Session: `2026-10-24-vpsadmin-haveapi-upgrade`; E2 saved Sol/xhigh,
  ready `workspace_write`; identity/current matched, ambient markers both absent.
- Canonical repository: `git@github.com:vpsfreecz/dev-workspace.git`
  (local project `vpsfree-dev-workspace`). Fresh SSH default is `master`.
- Registration: `vpsfree-dev-workspace-writing-policy`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-writing-policy`.
- Branch: `2026-10-24-vpsadmin-haveapi-upgrade-writing-policy`.
- Exact base: `767dfd587e346168e1443e65ccdb67ce748f3fe3` (fresh SSH master confirmed before creation).
- Exact head: `d4355518d945ef2e7d5fc2fdb45d6eab8226fa4c`; working tree/index clean.
- Plan/state: `../plan.md`, `../state.md`; brief is final design.md section
  “2026-10-30: optional API versions in KB and shared writing guidance”.

The user selected this repository as authoritative. The sole edit adds concise
version guidance to the existing factual workflow in
`skills/vpsfree-user-facing-writing/SKILL.md`, then reconciles technical-content
protection with requested factual updates. Existing routing covers KB and
vpsAdmin documentation. Versions may remain for demonstrated requirements or an
established process that keeps them current; the reason or maintained owning
reference is required. The lead directly accepted the final wording, including
the maintenance-process allowance, before commit.

No duplicated procedure, generalized framework, historical rewrite, new tests,
client/API source, pins, schemas, generated output or installed skills changed.
The workspace policy branch and product/KB work remain under their other owners.
This branch changes future editorial decisions only; it requires no runtime
package switch, rebuild, deployment, mixed-version transition or rollback action.
The policy source can be read directly without installation.

## Complete history and migration inventory

The complete base-to-head series contains one focused commit:

```text
d4355518d945ef2e7d5fc2fdb45d6eab8226fa4c writing: omit unnecessary documentation versions
```

One file, ten insertions. No superseded approach, fixup, obsolete compatibility
path, repeated dependency/channel/input update stream or consolidation remains.
**NO MIGRATIONS**: no schema/persisted-state change, migration file, or migration
merge/release/deployment/external-use lineage is introduced by this branch.

## Quick verification and commit

- `nix shell --inputs-from . nixpkgs#ruby --command ruby test/skill_policy_test.rb`:
  5 runs, 72 assertions, zero failures/errors/skips; seed19034, 0.026425s, exit0.
  The locked-input shell handle99865 completed. This successful check preceded
  only the lead's final maintenance-process wording addition; per lead direction
  its evidence is retained without an unrelated test repeat.
- Final frontmatter is unchanged; workflow numbering1–5 is intact; all three
  existing local Markdown/skill references resolve; no fence/whitespace drift.
- Final `git diff --check` and staged whitespace/single-file scope checks passed.
- No hook framework is declared; actual common hooks contain only inactive
  `.sample` files, and `core.hooksPath` is unset. Ordinary `git commit -F`
  completed0 without bypass flags or added framework.
- No long flake/package/native/client/browser checks were started. Existing CI
  configuration remains unchanged. No active command/effect remains.

## Independent review request

Proposed overall risk: low, localized reversible documentation guidance only.
Use retained `reviewer0` (Sol/xhigh/read_only) through the lead, no overrides;
general lane only under the mandatory-change-review skill. Read repo AGENTS,
this packet, the final skill, existing tests/README and the relevant design brief.
Independently assess exact final wording against user intent, necessity/default
verification, established-maintenance exception, preservation boundaries,
authoritative ownership, complete history and explicit no-migration conclusion.
This packet is evidence for review, not a completed review or merge approval.

## Complete final diff

```diff
diff --git a/skills/vpsfree-user-facing-writing/SKILL.md b/skills/vpsfree-user-facing-writing/SKILL.md
index ea8c960..bc51297 100644
--- a/skills/vpsfree-user-facing-writing/SKILL.md
+++ b/skills/vpsfree-user-facing-writing/SKILL.md
@@ -18,6 +18,13 @@ vpsFree technical documentation.
 ## Workflow
 
 1. Establish the supported behavior and factual claims before editing style.
+   Prefer versionless prose, install commands, links, and examples when the
+   actual client or protocol permits. Verify defaults before omitting version
+   selectors. Keep an exact version only for a demonstrated compatibility,
+   protocol, migration, recovery, or reproducibility requirement, or when an
+   established update process keeps it current. State the reason or link to
+   maintained guidance from the owning component. A URL, argument, or other
+   machine-significant value is not itself an exemption.
 2. Inventory every fact, command, value, link, identifier, and warning that must
    survive.
 3. Rewrite the prose in embedded mode. Keep the draft, self-audit, and comparison
@@ -73,6 +80,9 @@ requires a change:
 - IP addresses, ports, paths, hashes, versions, names, and URLs;
 - table structure and list syntax that affects rendering.
 
+This protection does not prevent removing optional versions in requested factual
+updates, following the workflow above.
+
 Visible labels and explanatory prose may change. In localized code samples,
 translate human-readable comments but preserve shebangs, tool directives,
 commands, identifiers, and configuration values.
```

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
