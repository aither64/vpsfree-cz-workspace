# Follow-up final review: global exclusions

Reuse original review-packet.md, review-report.md and all four mandatory lanes.
Same independent reviewer /root/final_review (gpt-6-astra/xhigh); remain read-only,
no nested delegation. No long checks/deployment have started.

Blocking finding fixed: newly admitted untracked reads query only the effective
core.excludesFile value with the operator's system/global configuration, then
pass that setting into the existing isolated Git repository reader. Fixed Git
flags, inherited-GIT-env stripping, timeouts, concurrency and output bounds
remain in force. Missing setting preserves standard default excludes; unexpected
configuration failures reject the read. Repository/object operations do not load
system/global config. The added regression verifies project/shared/tracking
HTTP 404 for a globally excluded fixture, and preserves index/publication HTTP
200 for the same paths. The final focused suite passed in 3.744s after rebasing
onto current runtime master, plus gofmt/diff checks. Source docs describe policy.

The required correction changes the Git execution boundary; reassess applicable
architecture/risk/general/scope concerns, then explicitly conclude final whole-
branch history, repeated-input consolidation and migration lineage. Prior
unrelated conclusions may be retained. Runtime correction folded into the one
behavior commit. Workspace pin amended/rebased; configuration pin regenerated
through confctl from current upstream in an owned detached scratch, then the
old pin series was replaced via interactive rebase with that one generated commit.
Nothing has been merged/released/deployed. No migrations. Each branch has one
final logical commit; no superseded pin streams remain. Both consumers select
runtime c1c620f91a04a70d599d208953b412a466981999. The upstream archive work advanced
runtime/configuration/workspace masters during this task; feature branches now
include those supported baselines. Workspace conflicts resolved by taking current
master inputs and regenerating only the nested runtime lock with nix flake update.
Source-only prior behavior unaffected; no manual generated-lock editing.

Preserve original report and save follow-up findings/conclusions separately as
review-followup-report.md under the session tracking directory.

dev-workspace: base 9e66eb84c204cd83fcd2a891a0d052c1e32a77de; head c1c620f91a04a70d599d208953b412a466981999
c1c620f91a04a70d599d208953b412a466981999 portal: open non-ignored untracked file links
docs/workspace-portal.md                           |  40 ++++--
 portal/internal/repository/review.go               |  11 +-
 portal/internal/repository/source.go               |  90 ++++++++++---
 portal/internal/web/source_files.go                |  25 ++--
 portal/internal/web/source_files_browser_test.cjs  |   2 +-
 portal/internal/web/source_files_test.go           | 139 ++++++++++++++++++++-
 portal/internal/web/static/source-file.js          |   4 +-
 portal/internal/web/workspace_source_files_test.go |  18 ++-
 8 files changed, 275 insertions(+), 54 deletions(-)

workspace: base a243ff2bfbabdb8bf23cc010adf2b692e77ba644; head 2b60e845de29aef76f3b31690f00e74bc0b2f614
2b60e845de29aef76f3b31690f00e74bc0b2f614 inputs: select portal untracked-file support
flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)

vpsfree-cz-configuration: base a4847bd6bbf2a62c107cff30b47452a60548a33e; head cf1271132140ca69776c6b24efce7891a531c736
cf1271132140ca69776c6b24efce7891a531c736 inputs: set devWorkspace to c1c620f9
flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
