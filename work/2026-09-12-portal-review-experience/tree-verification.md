# File tree and parent-navigation verification

## Implementation and review

The extension provides native expanded directory trees, compact accessible file
statuses, colored line counts, repository-relative path copy controls, an explicit
full-file back arrow, and parent links to standard commit pages. Parent details
may cross the feature base but remain ancestors of the frozen review head. Feature
history, first-parent diffs, existing URLs and private state formats remain intact.

Native backend 4e714b7; parent UI 9490e1e; final runtime 41c6d75. General and architecture
reviews found no issues. Scope's one Important finding was fixed: parent links
omit the default view parameter and clear file/view/version/line. The fix was
folded into its owning commit and all 21 browser checks passed. Risk review found no Blocking or Important issue; its extreme-path-depth
Advisory is accepted and documented. Package verification and deployment passed;
live browser acceptance passed. See tree-review-reconciliation.md.

## Quick checks

- Full runtime Go suite passed, including repository 7.722s and web 27.742s.
- Focused parent/durable checks after final native simplification passed 0.630s/
  1.147s. Review-related repository/web race tests passed 6.125s/6.939s.
- Chromium component acceptance passed 21 checks on final UI, combining actual
  pinned CodeMirror/Shiki and shared copy controls with bounded fixture APIs.
  Coverage includes keyboard disclosures, collapse/history reveal, Unicode/deep
  paths, file/directory collision, statuses/count colors, exact path copying,
  full-file arrows, parent/root/merge links, immutable links/anchors, responsive
  layout, no CSP/page errors and 8-file editor retention. Root inspected desktop
  and mobile screenshots. No 5,000-file DOM stress test was performed.
- Parent-page commit was checked separately before the tree UI in a detached
  worktree, which was removed cleanly afterward.
- Workspace deployment-contract checks passed 3 runs/14 assertions, zero skips.
- Committed range whitespace checks and JS parsing passed. All tools came from
  the respective pinned Nix inputs. Browser launch first used the Chromium store
  directory instead of bin/chromium; correcting the executable path resolved that
  harness error without any product change.

## Compatibility and delivery

The parents array is additive; older clients ignore it. Commit links before the
feature base are unavailable under the old package and work again after
rollforward. Canonical/private formats are unchanged, so no migration, live
rollback exercise, system configuration update or coordinated node update is
needed. No new dependency, Git fetch/object retention, API route or URL key.

Normal workspace-host switch installed profile 31 from the exact workspace
feature package after all required reviews were reconciled. The package is
`/nix/store/4zjl93s2i42zzdbfv4jv1b8s0000b8wd-dev-workspace-0.2.0`. Router, portal,
Codex and tmux services are active. Codex remains 0.154.0; profile 30 retains
the previous package 8a2c8nb. The switch passed ordinary generation, cluster/runtime
and protocol checks without forced interruption or a system-configuration change. No feature integration, archive, delete or branch removal is authorized.

## CI and final acceptance

Original runtime cbe617d passed CI 34710527917; original e2aa14b organization passed
CI 34710592527, including flake and devcluster. Final rewritten heads have new
runs, both successful: runtime 34711167462 on 41c6d75 and organization 34711209482
on 6c98b36, including flake and devcluster checks. All superseded runs were
complete and none needed cancellation. Exact links are in tree-ci-results.json.

## Exact package acceptance

The final site package passes its full Go checks (repository 10.278s, web 32.932s),
session suite 296 runs/2,979 assertions with 12 existing skips, and host suite 73
runs/438 assertions with 3 existing skips. There are zero failures/errors. The
check phase took 2 minutes 13 seconds. The site workspace flake check also passes
its 3 deployment-contract tests/14 assertions. Generic and organization flake
checks are covered by their exact feature-head CI runs; they were not needlessly
repeated locally. No local kernel build was started.

## Live browser acceptance

The first live acceptance run passed all 16 checks in 139.141 seconds against the
installed profile 31, observing the exact runtime head 41c6d75. It exercised
expanded trees, keyboard collapse, preserved collapse during layout changes,
history revealing selected paths, accessible colored status letters and counts,
native clipboard copying from tree/header, and retained syntax highlighting.
Before/unified and After/split full-file links loaded directly; the back arrow
returned to each frozen diff and cleared the source version and line.

Control-click opened a parent in a separate tab with its full standard commit
page. Reload and Back/Forward worked, and ancestor navigation crossed the saved
comparison base. The 390px layout retained read-only editors without document
horizontal overflow. No page errors or CSP violations occurred. Root inspected
all four retained desktop, full-file, parent and mobile screenshots.

Strict TLS/authentication was tested separately and passed; the browser context
ignored certificate errors. The live run did not change Git refs or conversation
state. Merge/root and remaining status edge cases are covered by component/Go
fixtures. Results, frozen URLs and screenshots are in artifacts/tree/; the
reproducible harness is tree-live-browser.cjs. Temporary build links, logs,
component screenshots and message files were removed after recording results.
The installed package, registered worktrees and all branches remain retained.
