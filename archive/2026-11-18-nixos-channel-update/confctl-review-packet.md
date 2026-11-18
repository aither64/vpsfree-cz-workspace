# Final confctl review packet

User accepted D4 and directed: design it first and then implement it. Current D5
is appended to design.md after the historic merged configuration pin work.

Expected behind/equal UPDATE is success/no-update; independent forward inputs
advance. Divergence/source/removal/equal-SHA metadata rejection stays exit3;
evidence/Nix errors stay1. Strict check-update still rejects rollback artifacts3.
No new flags, workflow workaround, solver/retries, dependency/pin changes,
release or deployment. Selected inputs use whole Nix candidates sequentially
from last accepted temporary reference, not hand-spliced graphs. Selected names
cannot drift. Final strict original-to-final check and snapshot precede one
atomic install/commit. Later hard failure installs nothing; existing post-install
hook failure leaves validated lock/hook effects. Conservative intertwined skip
is accepted; maximal update search is outside scope.

## Complete repository/history

Workspace /home/aither/workspace/ai/vpsfree.cz, session
2026-11-18-nixos-channel-update; worktree worktrees/<slug>/confctl.
Remote git@github.com:vpsfreecz/confctl.git; default master.
Base ff5e017780a35fb97b549db2a51b570193867c3b.
Head d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49.
Complete series: single head commit, inputs: skip behind revisions during guarded
updates. 14files,452insertions/79deletions. Source/CLI/tests/docs intentionally
one commit because they implement one public behavior contract. No obsolete
approaches/followups, repeated dependency/generated pin streams or migrations.
No migration release/deployment/external use. Worktree clean; lead inspected
complete series/stat/message and diff whitespace against owner report.

Source under lib/confctl: inputs/{forward_guard,guarded_update,updater}.rb;
cli/app.rb and cli/inputs/{update_result,root,channels,machines}.rb.
Tests: spec/inputs/{forward_guard,guarded_update}_spec.rb and
spec/confctl/cli/inputs_forward_only_spec.rb. No Nix/workflow changes.

## Quick evidence

Owner report and package-c-raw/quick-final.log: nix develop --command bundle exec
rspec spec/inputs/forward_guard_spec.rb spec/inputs/guarded_update_spec.rb
spec/inputs/commit_message_spec.rb spec/inputs/lock_graph_spec.rb
spec/confctl/cli/inputs_forward_only_spec.rb:128examples/0failures25.91s.
Changed Ruby RuboCop11files/no offenses; required Nixfmt/RuboCop hooks pass,
subject/period hooks pass, TextWidth advisory72column warnings, max<=80.
Man generation via bundle exec rake md2man:man and diff--check pass; generated
man output ignored. Full suite/full lint/CI remain after review. Earlier fixture
failures were repaired and superseded by final pass.

Coverage report to verify: all-behind exact bytes/index/HEAD/no commit;
equal/descendant; alias order/dedup; mixed skip/forward one rename/commit and
accepted-only summary; carry/discard temporary references; nested/shared
regression; selected-path drift; final strict baseline; later hard rejection,
evidence/Nix errors atomic; existing concurrent-writer/cache/interruption/hook
recovery retained; strict check-update3. Small actual Nix two-local-path fixture
tests reference/output plumbing without live upstream.

## Documentation/compatibility

Behavior/transaction/exit semantics → operators/reference+how-to → existing
README-linked docs/flake-inputs.md → source/regression evidence.
CLI reference/help → man/man8/confctl.8.md, cli/app.rb/shared update_result.rb.
Compatibility → CHANGELOG Unreleased. Execution evidence → package-c.md/session.
No docs moved or supported recovery retired. Lead applied writing skill directly
before commit; owner applied exact wording for mixed ahead+behind skips and
post-install hook-failure recovery exception.

No persisted schema/format or API protocol change. Old/new tools read same locks;
old binary restores behind-as-error behavior. Ancestry is history protection,
not detection of descendant reverts. Consumers: root/channel/machine commands
and both configurations' daily forward-only workflows in forward-only.md. Both
still pin this base until separately authorized confctl pin update.

## Assignment

High risk: public CLI exit behavior and atomic lock/index/commit recovery.
All lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Retained reviewer0 Sol/xhigh/read-only, independent of C;
no overrides/fallback. Read skill/all four references and actual complete
diff/series/tests/docs. Challenge scope before hardening. Explicit conclusions
on obsolete/repeated streams, no migrations, documentation placement/preservation.
No nested review/source edits/long tests. Return report_to_lead, lead saves report.
Implementer0 owns all fixes, lead acceptance/reconciliation. Confctl integration
not approved; earlier merge approval names only two configuration repositories.
