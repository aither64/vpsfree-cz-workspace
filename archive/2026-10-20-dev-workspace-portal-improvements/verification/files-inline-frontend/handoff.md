# Files frontend handoff

Normal commit `fc9c944afee16627f3f28e94ed73b8fa3e039368`, parent
`b0f3f2ea6140a7c8a107f93a7a894cad7e320f5c`; clean B/index, not pushed.
Implementer2 has returned B source/Git/index ownership to the lead.

The 13-path frontend boundary and exact candidate blobs/tree are retained in
`commit-proof.json`, `candidate-blobs.json`, `candidate.patch` and
`precommit-tree.txt`. No backend/CLI/docs/pins or unrelated files changed.
Source and standalone use the accepted shared `renderSourceFileContent` export.
The UI implements inline tree/content selection, native modified anchors,
read-only Raw/Preview, exact original-text Copy, real download, race retirement,
hide/resume, lazy/manual listing, independent scrolling and mobile stacking.
Existing app cache consumers are56, affected styles22, source module3;
unrelated attention/notification cache refs are unchanged.

`quick-final.log`: repository-Nix syntax/format/whitespace PASS;
source renderer plus read-cycle suites18/18; three focused Go wrappers PASS
(SourceFileBrowserContracts, ShippedBrowserClientMatchesSessionAPI,
AutomaticArchivalPageIsSeparateFromIndex), 1.179s. The first quick uncovered
history extraction missing the new Files lifecycle names; the lead approved
ONLY pauseFiles/resumeFiles VM stubs in read_cycle_browser_test.cjs. Assertions,
budgets and product lifecycle behavior were not weakened. The original log
retains that resolved failure. User-facing strings received the lead's direct
English pass before commit.

No browser was launched, and no runtime acceptance is claimed. Parent owns
committed final affected review and the existing bounded Files browser segment:

```sh
PORTAL_BROWSER_TEST=1 go test -mod=readonly ./internal/web \
  -run '^TestQuestionBrowser$/^portal_improvements_browser_test.cjs$' -count=1 -v
```

No more native50 attempts. Backend imp0 and guidance imp3 own their corresponding
source/documentation changes; lead owns combined records/history/publication,
review, final pin closure and any authorized deployment. No new project prose
is needed in this frontend-only package. No Git operation remains assigned to
implementer2 after this handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
