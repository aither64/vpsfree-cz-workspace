# B incident2 deliverable

Published final: `7b8c646974df72e0df3e576d10f09d79823ae004`.
Tested and committed tree: `9a409e0eb0003d1e3cefd6874d0cae028506d368`.
Source is clean and frozen for lead-owned affected final review.

Plan recovery and bounded HTTP runtime-lock waiting are separate behavior
commits, preceded by one final A `ac62eeeb9d8b` Go/Nix/vendor selection. The
original core, capability and runtime commits remain exact. The deployed ed2
retention patch is unchanged; ed2 itself is retained by ref and bundle and is
not a literal ancestor of the consolidated candidate. The preincident product
tree differs only in the five mechanical dependency-selection files. There
are no migrations or persisted-state/schema changes.

See `implementer1-incident2-final.json`, `final-history.json`,
`implementer1-incident2-quick-commands.json` and the linked logs and full/range
diffs. Focused checks and relevant races passed. Initial fixture failures are
retained and diagnosed; they were not accepted through a blind rerun.
The final normal matrix covers all corrected and new cases. No native, full
package, long integration, build or deployment was run by this owner.

CI run 39995040046 was in progress at the single post-push snapshot. All recent
superseded branch runs were complete. No CI wait, rerun or cancellation occurred.
Lead owns review, verification, downstream publication and operations.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
