# HaveAPI latest-master interaction review

User directs merging HaveAPI client into master and keeping WebUI PR74 open.
No WebUI integration or new feature/release/deploy scope. Only HaveAPI feature
needs latest-base integration; original independently reviewed range is
c14e7d3158b91c134c2817b489cd29772fc09f82..f5320eae05cbf8256a40cb04358be876ea7bde75.
See callback-name-review-packet.md, bridge-review-packet.md, original full review
ledger, design.md, current inventory and owner premerge final report.

Upstream changed to c58704a08451a231fdf6c6123437133422af46dc via two release
draft query/preparation fixes (52664813+c58704a0). Three upstream paths:
doc/agent-instructions/releases.md, utils/release/publish.rb and
utils/release/spec/release_spec.rb. Feature migration earlier touches release
source-path spec, so inspect combined interaction. No broader design change.

Owner0 authorized clean equivalent rebase only, no manual conflict resolution.
Final exact head, complete series, range-diff, ordered stable patch IDs, tree
reconstruction and quick checks supplied in final report and owner lineage.
All intended source changes must be committed and clean, quick checks green.
This packet does not claim installed certified_equivalent: selected coordinator
autocertification refuses substantive upstream changes, so applicable independent
review is needed. Stable patchIDs alone are not tree/build proof.

Review affected general, architecture/repetition and risk/compatibility lanes
including release-spec interaction, full final series/diff/migration and update
stream conclusions. Scope addition none; reuse original scope conclusions unless
new evidence triggers scope lane. Original high-risk client behavior retains its
review; do not rerun unrelated full investigation. Saved independent reviewer0
gpt-6.1-sol/xhigh/read_only without overrides. Read required local/review routes
and selected references. No source edits/nestedagents/longtests/push/merge/release
or lifecycle actions.

Acceptance: ordered feature changes and messages preserved; upstream fixes retained
without changing intended client export/transport/global/auth/resource behavior,
generated JS/declarations match reviewed package, no new deps/pins/migrations or
obsolete history, current quick coverage addresses interaction. Explicitly conclude
whether original user merge approval remains applicable under patch-equivalent
rebase rule. Final current-head feature CI must pass before root submits supported
coordinator fast-forward merge to master. No automatic npm publication/tag.
WebUI PR74 remains open at5dd2333b; no source or metadata action.

Owner final range c58704a0..19c20c90cc957d4225ece50a92e190855f252710;
clean tree0ef10a638118397c07f537b6a33159ec2ee21fe1. Lead independently
read lineage/verification/rangediff and verified clients/js tree equality and
5equal range-diff pairs. Quicks allgreen as final ownerreport.

Lead additionally ran git merge-tree --write-tree --merge-base=c14e7d3
c58704a0 f5320eae: exact resulting tree0ef10a638118397c07f537b6a33159ec2ee21fe1
equals rebased19c20c9 tree. This independently reconstructs upstream+reviewed
feature, beyond stable patch ID comparison.
