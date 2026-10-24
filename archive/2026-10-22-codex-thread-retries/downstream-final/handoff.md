# Final downstream runtime selection

W `2f340789f3e07c5a019cd92a95a8ffaa7b201ec7` and C
`2a59f1ee9857dc97f12990981ebcabfd08341d79` are clean and SSH-published.
Both select B `c79af9736c04f6e7cd9c6b2197913d101896544c` and A
`5743f94c2fbd01b65438847d2e2bab0f01df32ae`. Extension 767dfd58,
native 0.163.0, every other input node, edge and follows path are preserved
relative their fresh defaults. C also preserves the upstream Gemfile changes.

See [final.json](final.json) for exact heads/trees/ranges, source refs, verified
bundles, complete diffs and graphs, check results and prospective build selectors.
[graph-proof.json](graph-proof.json) binds the full lock comparison.
Each branch has one final pin commit; there are no downstream migrations.
Deployed predecessors are retained nonancestors, not claimed literally merged
or equivalent to the new substantive runtime successor.

Quick checks and matching deployment contract pass. The initial W command's
formatter lookup failed after both Ruby suites passed; the exact C-pinned
formatter check passed separately. C's rebase hook needed the newly inherited
parser gem; ordinary pinned-shell setup and checkout passed before the generated
commit, with all normal commit hooks enabled. One post-push CI inventory returned
no runs for either branch; no CI wait occurred.

Lead/retained reviewer owns whole-branch history and migration assessment.
Lead/watchers own remaining final source review, longer checks, exact builds,
copy, activation and verified deployment. Integration needs its separate approval.
No lead state/design files, B/A source, live resources or session lifecycle changed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

Reviewer evidence supplement: [formatter-final.json](formatter-final.json) records
the exact C-Nix formatter command, exit 0 and raw stdout/stderr, with unchanged
W/C heads, trees, flake blobs and SHA-256 before and after.
[workspace-preliminary-to-final.json](workspace-preliminary-to-final.json) proves
preliminary 41b27287 and published 2f340789 have identical trees and parents.
The local amend only removed a premature reviewed-status claim from the message;
the publication log records only final 2f340789 replacing deployed 3d613a16.
W/C pins remain at c79af973 pending the lead's next exact final B release.
