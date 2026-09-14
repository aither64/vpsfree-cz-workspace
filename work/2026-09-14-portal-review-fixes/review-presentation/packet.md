# Portal presentation follow-up review

Initiative: 2026-09-14-portal-review-fixes. Plan/state: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-portal-review-fixes/plan.md and state.md.
All project worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/<name>.

## Requested behavior and boundaries

User approved three focused follow-ups to previously deployed portal fixes:
1. Sticky file headings in Unified, Split and full-file views. Compact long
   paths while preserving full path access, counts/collapse/links. Linked lines
   remain visible below the header; each header belongs to its own section.
2. Automatically use the existing 58px icon sidebar only while a repository
   comparison is visible. Return to 250px on overview/other tabs. Keep narrow
   screen behavior and file tree. Maintain accessible navigation/actions and
   Codex limits popover. No fullscreen toggle or saved preference.
3. Replace raw archival paragraph with labelled policy/rule/scan date/conditional
   Not before, readable blockers and a closed Technical details disclosure. The
   merged tier is conditional, not proof branches are merged. Preserve full
   diagnostic output in the disclosure and last successful settings on read
   failure. Keep existing Keep open behavior/help.

No Git projection, Codex provider/protocol, persistence, server API, worker
archival decisions, fingerprint, retention or schema changes are intended.
No integration into default branches, archive/delete or configuration-repo work.
Deploy from the existing workspace feature via user profile and leave session open.

## Revisions and commit split

Review this follow-up delta against the deployed baseline:
- dev-workspace: b837f0d974a98857daef7e4cc09d8f3039a059a0 -> 774db1205a0cd653b687cec34e788eabd6a9f1c1
- vpsfree-dev-workspace: f6050a4d661be7c923518e0b962a4372ebad7f50 -> 109e9ded49d9b336a25f44ebfdbe19e5ed598b90
- workspace: 1c3f3e156cad0f84090ec1934acbb867eb723345 -> a24742ab2e999cabafe81926a4271af436546b19
  Workspace has also rebased onto shared master d926aa2; its intervening tracking
  commit is pre-existing coordination, not follow-up implementation. Compare
  flake.nix/flake.lock for package-pin scope.
- codex-web remains 882c88ccfbebfb646fb2cafbe9bc6790141b2d13, unchanged.

Runtime has three focused follow-up commits: sticky headings plus browser
coverage, compact sidebar plus browser fixture, archival presentation plus
projection and browser coverage. Downstream pin updates are consolidated into
existing unmerged pin commits; their deployed previous heads remain review bases.
Earlier task implementation has completed reviews in ../review and was deployed.

## Ownership and compatibility

The generic dev-workspace runtime owns app.js shell/settings, repository-review.js
and its optional internal mount callback, styles and templates. The only mount
consumer is app.js plus the repository acceptance fixture. CodeMirror remains
owned by portal/review-ui and its existing display contract is unchanged.
Codex limits markup is shared by session and index templates; compact behavior
must preserve both consumers. Archival CLI owns policy/state and returns its
existing status payload; browser adaptation intentionally preserves stored raw
blockers to avoid changing inactivity fingerprints.

Organization extension consumes the exact runtime pin via lib.mkPackage;
workspace consumes the organization pin and supplies site configuration. Provider
pin stays unchanged. Browser assets/templates are packaged together. Existing
open documents keep their own loaded code; reload to adopt changes. No new state
is written beyond the existing user-requested hold operation. Older package can
load the same state; previous user profile is retained for rollback. Shared Codex
0.154.0/App Server remains running. Trust local operator for host administration;
retain all remote request validation, origin and lifecycle target checks.

## Verification and risk

Quick checks passed: nix shell --inputs-from . nixpkgs#go nixpkgs#gcc
nixpkgs#nodejs -c bash -c 'cd portal && go test ./internal/web' (32.128s),
node --check for changed JS, git diff --check; workspace package evaluates.
Browser acceptance is written but will run after review. Planned checks:
repository fixtures in Chromium/Firefox (sticky transitions, all-view anchors,
long paths, original +116/-6), real template browser scenarios for sidebar and
settings, packaged checks, CI and deployed read-only smoke/screenshots.

Overall risk: Medium, bounded compatible browser work crossing internal shell
and renderer boundaries with downstream package pins. No host migration or
state/API change. Lanes: General, Architecture, Scope, Risk (deployment/pins).
All reviewers: gpt-6-astra / xhigh. Review the committed delta and history directly.
Do not spawn nested reviewers. Write your report in this directory as <lane>.md.

## Final verification addendum

Final runtime: 63cbc32173f73da313e4f11c9c2214884f6161d5.
Final organization pin: 3f602aef0662b23eef9f7aa2f4c5a76e20e943bd.
Final workspace pin: c986868b94ef67c9ecf9a65b814f1f18793dadee.
The final tree folds direct review/browser corrections into the three owning
presentation commits; the previously deployed lifecycle fixture's coalesced
focus stimulus is a separate test-only commit. Compared with reviewed 774db12:
preserve failed hold-save diagnostics through read-back; keep keyboard tab focus
by updating the same history/hash route without native fragment focusing; avoid
same-tab duplicate history; improve browser fixture inputs and named subtests.
No external contracts, state formats or accepted scope changed. No lane rerun
was required for these bounded corrections. Original reviews remain exact at
their recorded heads, with decisions and final checks in state.md.

Both engines pass the repository and real-template presentation acceptance.
Final focused web suite: 33.639s; template presentation suite: 15.277s.
Runtime packaged/host VM checks and final workspace deployment contract pass.


Post-deployment mobile acceptance correction: runtime cdcaafa → 227bcfc changes
three CSS declarations and extends the existing mobile browser assertion. The
control cannot shrink/wrap; the heading gets its own mobile row, with the
directory hidden there while tooltip, accessible name and copy retain the path.
This corrects the already assessed compact mobile heading behavior without
adding a design, abstraction, contract or state change. Chromium/Firefox
acceptance and the real-template overlay smoke pass; the coordinator inspected
the final mobile screenshot. No lane rerun under workflow steps 9–10. Downstream
pins: organization 08d691c and workspace d53014f; provider unchanged.
