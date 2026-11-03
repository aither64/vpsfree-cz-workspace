# Configuration whole-branch history packet

Scope is only the independent history, consolidation and migration conclusion.
The actual generated-only lock diff qualifies for the mechanical-content review
exemption; no redundant substantive content review is requested.

## Requested result and exact range

The user requested staging and os-staging channel updates after verified
vpsadminos integration. The accepted design addendum begins at `design.md:155`.
The lead later relayed explicit user approval for configuration/master
integration; see [integration preparation](configuration-integration-preparation.md).
Deployment remains outside the request.

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Target: `master`
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsfree-cz-configuration`
- Feature branch: `2026-11-03-fedora-45-image-build`
- Base: `c4107822060e9e34b24a83950d618c9f28a7722b`
- Head: `e3ac35780cc909764a3bb059b4d9dfa23cf60867`
- Publication: feature push succeeded over SSH with hooks active; fresh
  `ls-remote` confirmed the exact head and unchanged configuration master.
  Portal comparison captured the exact base/head. Worktree remains clean.
- Entire series: one commit, `e3ac35780cc909764a3bb059b4d9dfa23cf60867`
- Final diff: `flake.lock` only, six additions/six removals in the
  `vpsadminosStaging` and `vpsadminosOsStaging` locked identities.

Both move from `b45b27b4330a08d85f413999e4bf66ba4503eee1` to the exact
reviewed/tested/remotely integrated vpsadminos/staging head
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`. The generated commit message/changelog
is preserved unchanged and includes all eleven imported upstream commits.
No handwritten application/configuration behavior changed.

## History and migration inventory

One logical vpsadminos update stream covers the two requested channels and their
existing follows consumers. No intermediate update commit, repeated pin,
superseded approach, follow-up fix, or unused compatibility path exists on the
configuration branch. No consolidation is needed. No configuration feature
commit was merged, released, deployed, or externally consumed; only feature
publication is authorized. There are no migrations in the configuration range.

The complete upstream source range is
`b45b27b4330a08d85f413999e4bf66ba4503eee1..dd188397abe37d0bc33f4c5dfb3605206ce5e326`:
eleven commits, 17 changed files, 158 additions/27 removals. Ancestry is proven
by `git merge-base --is-ancestor`. The exact commit inventory and rationale are
in [configuration execution](configuration-update.md#imported-upstream-range-prepared-inventory).
The range contains Fedora 45, Ruby package dependency updates, nixpkgs lock
updates, a CI Ruby patch-selection update, and the OOM killer queued-miss fix.
No database, on-disk, or protocol migration exists in that range. Its nixpkgs
lock changes are overridden by the unchanged configuration follows edges.
No deployment compatibility is claimed from the image verification alone.

## Evidence

- Generated mutation: newer daily-workflow confctl CLI with
  `inputs channel update --forward-only --commit '{staging,os-staging}' vpsadminos`.
- Hooks: pre-commit and commit-msg passed. Generated message width warnings
  retained under the repository/workspace exception. No bypass.
- Quick checks: JSON validity, `git diff --check`, otherwise clean checkout.
- Complete semantic lock check: 158 paths, all 62 follows edges preserved;
  only two raw selected nodes and six effective paths changed; 152 other paths
  unchanged. `configuration-lock-graph-result.json` records exact hashes.
- Baseline/final committed lock exports and hashes are recorded in
  `configuration-update.md`; both artifacts live outside the checkout.
- Complete CLI guard/channel/selected metadata verification batch passed at
  exact `e3ac3578`, all three exits 0, elapsed 54s. See
  [result](config-final-checks-result.md) and raw `config-final-checks.log`.
  The complete-graph guard reported exactly the six expected effective paths.
  Channel listing preserved staging nixpkgs `718f670e` and vpsadmin `ff730be4`;
  both vpsadminos roles resolve to `dd188397`.
- Selected metadata evaluation passed: staging node1 uses `vpsadminosStaging`;
  machines/build uses `vpsadminosOsStaging`; both revisions are exact
  `dd188397abe37d0bc33f4c5dfb3605206ce5e326`. The dev-shell banner was removed
  from `config-inputs-info.json` for valid JSON, with raw output preserved in
  the combined log. No operation was rerun. Committed final lock equality and
  exact JSON input/revision assertions passed after extraction.
- GitHub Actions listing for exact feature head returned no runs; only
  scheduled/manual daily-update exists, so no feature-push CI was expected.

Documentation placement: checked repository AGENTS, README, current daily-update
workflow and flake channel definitions. Routine generated updates require no
project documentation commit. The individual update's evidence and future
deployment limits belong in the session execution record. Recovery for this
undeployed package is reverting its generated lock update; no live state changed.
