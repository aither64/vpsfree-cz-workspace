# C/config machine-retention source checkpoint

Lead-approved policy prose is committed and SSH-published. This checkpoint is
source-only; final runtime and confctl channels remain deferred until final B.
Both exact old deployed heads remain available under the named safety refs in
*-baseline.json, plus original patch/series receipts. Default refs are unchanged.

Workspace base 5276ad798d3dcf2c714f2336b0a50636bab900ae;
source checkpoint c1d9f68e233af1f1630cd1362a2cc86370d94d60.
Configuration base 38e7c837893695999e588a73f5d2a0088b8257b1;
source checkpoint bcb3fa5a9194368645f89787978b5c8fb613bf42.

Range-diffs retain all three original C patches and the original configuration
pin patch exactly, plus one focused source policy commit in each repository.
New baseline additions are preserved; rebase had no conflicts. No migrations or
lifecycle implementation, schemas, claim APIs, receipt schemas or saved role
settings changed. No intermediate B/A pins or channel updates were generated.
The existing sole runtime pin remains deployed f8f2938/A852; final composition
will amend/consolidate that stream after B, preserving source groups. Current
source checkpoints are not the final composed deployment graph.

Workspace policy changes AGENTS.md and the routed Git/deployment/lifecycle/
coordination docs. It keeps short approved merge claims and independent feature
work, and requires every deployed physical machine's integration lineage, actual
user acceptance and explicit machine release direction. It records source,
system/profile, alias, ancestry and migration evidence; missing gates keep the
machine held. Legacy automatic lifecycle release is implementation behavior,
not permission. Configuration changes only its reusable aitherdev coordination
operations guide and links the generic #machine-retention anchor. That anchor
will be supplied by the later serialized B policy source package before final
composition. Per-rollout revisions/evidence stay in this initiative.

Final AGENTS size is 15882 bytes, 502 bytes below the unchanged 16384 assertion.
The final paragraph applies the lead's exact hook-setup and physical-machine
release wording. Existing instruction/routing suite: 9 runs, 166 assertions,
0 failures/errors/skips, 0.071814s. workspace-source-quick.json and logs retain
exact argv/workdir. Affected local document links and contradiction scan passed;
whole-range and staged diff whitespace checks passed. No unrelated instructions
or assertions were relaxed.

Configuration environment/hook evidence: `nix develop --command bundle check`
reported all Gemfile dependencies satisfied. Rebase executed in the declared Nix
shell with ordinary hooks and no bypass. `nix develop --command git commit -F
/tmp/portal-config-machine-policy.commit` passed pre-commit Nixfmt and commit-msg
SingleLineSubject/TrailingPeriod/TextWidth. TextWidth produced nonfatal >72-column
warnings on body lines; all lines comply with the repository's <=80 requirement.
Working trees are clean. Both feature publications used exact old-head leases;
remote proofs are retained. Quick `gh run list` metadata reads returned [] for
both branches, so no superseded queued/running workflow needed cancellation.
No CI wait, long/full/browser checks, repository claims, machine operations,
default integration, deployment or lifecycle actions occurred. The lead's held
machine claim remains untouched.

Source checkpoint complete; implementer1 is ready for an explicit serialized B
notifications/runtime-policy handoff. B remains exclusively implementer0 until
that handoff. Parent retains independent review and all long utility work.
