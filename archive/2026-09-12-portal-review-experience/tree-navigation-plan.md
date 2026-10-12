# File tree and parent-commit navigation

Approved 2026-09-12; implement in the current initiative and deploy to aitherdev.
Baseline: runtime820277e, providerde83e9c, organizationee9c55b and workspace082c4c9,
deployed profile30. Initial initiative tracking is already committed.

## UI

Build native nested directory disclosures from comparison paths, initially all
expanded. Directories precede files, alphabetically per directory. Keep collapsed
state within an open comparison; direct/history navigation expands the selected
file's ancestors. New comparison/reload resets expansion. Collapse affects only
the navigator, preserving lazy content/editor bounds. Show basename and full-path
tooltip; support root files, deep paths and file/directory replacement.

Tree statuses use colored A/M/D/R/C/T with accessible full labels; headers keep
full labels. Color additions green and deletions red at every stats location,
retaining signs and neutral file/binary counts. Add shared copy icons next to
names in tree and file headers, outside links. Copy displayed repository-relative
path without quoting/newline (destination for renames; old path for deletions).

Replace View diff with a left-arrow link immediately before the full-file name,
labelled Back to diff. Preserve exact comparison, selected file and layout; clear
version and line. Parent hashes link to standard commit pages, all parents for
merges. Each commit uses first-parent diff; root says No parent and its empty tree
is not a commit link. Parent navigation preserves review/layout and clears file,
view/version/line selections. Support new tabs/reloads/history and repeated
navigation before the feature base.

## API and compatibility

Expose additive parents array. Commit detail accepts only commit objects reachable
from the saved immutable review head, including base/ancestors. Keep feature
history range unchanged, validate SHA and session/repository scope, reject unrelated
commits. No Git fetch/object retention, new endpoints, URL schema, persisted format
or dependency. Old package ignores new JSON; old-range ancestor links report
unavailable after rollback until rollforward. No migration or coordinated system
update. Deployment pins update runtime -> organization -> site user package.

## Verification and delivery

Focused native Git and handler tests for base/root/merge/unrelated/missing commits,
frozen head after branch movement and service restart; browser checks for tree,
keyboard, history, clipboard, stats, statuses, arrow and parent links, long/Unicode
paths, mobile, CSP and resource bounds. Quick tests and committed changes precede
mandatory adaptive xhigh review. Then package acceptance, CI and normal feature
user-profile deployment. Preserve all unmerged branches and open session; no
integration, archive or delete. Root applies user-facing writing skill before
commits and retains useful evidence plus stable portal link in handoff.
