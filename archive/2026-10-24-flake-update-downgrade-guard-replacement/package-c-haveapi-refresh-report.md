# HaveAPI target-guidance refresh

The local feature is now `74f1cef68946fe4d6a6bc0a25c626df18c7232cf`, directly
based on fresh master `7ac977a26080d45d44b6608aafad2cadd2ec7f81`. The narrow independent final review passed without findings, retaining prior
specialist conclusions. The exact refreshed head is now published over SSH by
force-with-exact-baec-lease; default7ac remains unchanged and source is clean.
The original baec publication/range remains preserved as provenance.
[Full final source/publication/CI/effects receipt](package-c-haveapi-refresh-final-receipt.json)
binds this current state. No other repository source, pin or verification was changed.

Master added only three AGENTS.md lines documenting library/application
lockfile policy. The feature does not add or change library lockfiles. Fresh
repository guidance was read. The old reviewed range
`67fcd34ba506264a5c7ee2e8e18a88d221c6f469..baec8e58e11a4868a6c713e70d406709bb94c152`
is preserved by backup ref refs/backup/2026-10-24-flake-update-downgrade-guard-replacement/before-haveapi-guidance-refresh
and exact old/new series/diffs in review-haveapi-refresh/.

The rebase had no conflicts or material edits. New-base feature patch bytes and
stable patch ID equal the original; range-diff reports baec8e58 = 74f1cef6. Full
recursive modes/types/blob comparison independently proves the new tree is the
old feature tree with only the fresh target's AGENTS.md blob. All other source,
tests, helper/workflow/docs, hook configuration, flake/dev environment and lock
bytes are identical. The single R pin remains
5436d3d7c36d3d5174eab3c44e3578830749d3db. There is one coherent adoption commit,
the same three feature paths, no duplicate update stream and no migrations.

[Complete local inventory](package-c-haveapi-refresh-inventory.json) binds all
ranges, hashes, paths and equivalence evidence. Nine focused fixtures passed in
the declared Nix shell, including YAML/inline shell syntax, shared resolver and
rejection/error/publication stops. Helper Bash syntax and diffcheck passed.
Ordinary rebase/commit hooks passed HaveapiI18n and commit-message checks; the
unchanged message retains its allowed >72/<=80-column warnings. Raw logs are
package-c-haveapi-refresh-rebase.log and package-c-haveapi-refresh-quick.log.
Actionlint evidence applies to the exact unchanged workflow blob; no action ref
was selected or edited during this refresh.

The prior real HaveAPI pattern/CI remain exact old-source historical evidence.
After the narrow gate and publication, only one fresh HaveAPI real nonpublishing
pattern is needed to bind the new full-source identity. The new driver and
manifest are frozen at:

- package-c-haveapi-refresh-post-review.py:
  c0ff46d07593482468e148a1ea0588e1806475a1cfcd22859535147fa72911ca.
- package-c-haveapi-refresh-verification-manifest.json:
  5484745a91c545dc4ebde972e0c7745db44a5f3e92e0004c1cc2121a19c56f39.

The manifest includes only HaveAPI plus unchanged R provider, the new complete
tree and explicit AGENTS hash; workflow blocks, lock graph and provider are
identical to the original frozen R manifest. Static AST/JSON/source-tree/file/
blob/Bash/no-publication preflight passed. New uncreated root:
/tmp/flake-update-guard-haveapi-refresh-1. No runtime or auth command was run.
The completed narrow review is frozen at SHA-256
3e07ec8ebeed1dd69ed9e5988501527cf143ef1920dcb7439bfaad334dc3e25e. The
private-auth noarg launcher is now frozen at SHA-256
e6ebdf72289ff2eb5967400522f9238dd3458a208da34e1096a34026b973a3fb.
[Exact runtime brief](package-c-haveapi-refresh-verification-brief.md) binds the
review, source, driver, manifest and freshroot. The
future watcher receives only that executable path and captures the full
aggregate log; it must perform no auth/token/config/environment reads itself.
Root owns launch after current TF3; no other pattern/provider/race/VM repeat is
requested by this refresh.

The later force-with-exact-lease publication must freshly confirm master7ac and
featurebaec. A source-equivalent rebase push changes only AGENTS.md compared with
the currently published tree; Ruby CI's push path filters exclude that file, so
no fresh exact-head run may be triggered. Record that honestly in one bounded
post-push snapshot; no dispatch or old-head CI relabeling. No merge/default,
deployment, claims or lifecycle action is authorized by this feature refresh.

Publication evidence: first push was refused by Overcommit signature verification
without any remote mutation. Hook configuration and both custom hook files
were verified byte-identical to the reviewed source, then ordinary overcommit
--sign repaired signature setup; a fresh target/lease check and second declared-
shell push passed. No hook bypass or source change occurred. Original failed
and successful receipts/logs remain separate. Final comparison captured base7ac
and head74f. One bounded new-head CI observation found actual Ruby RSpec
40109905180 completed successfully on74f; the earlier possible no-run condition
did not occur. No cancellation, dispatch, wait or rerun was performed.
