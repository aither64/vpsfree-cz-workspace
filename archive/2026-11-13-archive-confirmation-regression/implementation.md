# Package G: provider helper proof inputs

Implementation and focused CI fixture correction ready for affected review,
2026-11-15. Owner implementer0; lead owns acceptance, review, later verification,
integration and deployment.

## Exact range and publication

- Repository: `git@github.com:aither64/dev-workspace.git`.
- Registered clean feature worktree:
  `worktrees/2026-11-13-archive-confirmation-regression/dev-workspace`.
- Branch: `2026-11-13-archive-confirmation-regression`.
- Fresh fetched base: `458c7857b942fb592607c83af7b5287a6c93ea96`.
- Final committed/pushed head: `9241a342a6ef4ca69148594e98cce7ddcfb459a6`.
- Complete two-commit series:
  `e96284d1a0484a01888a6d7166fcbd5f68855659`
  (`provider: preserve native utility proof inputs`), then
  `9241a342a6ef4ca69148594e98cce7ddcfb459a6`
  (`test: allow setup time in continuation timeout fixture`). The independently
  reviewed original provider commit is retained unchanged.
- SSH push completed; `git ls-remote` verified the exact feature head.
  Worktree/index are clean. The diagnostic `dev-workspace-e` checkout remains
  untouched and is outside the product worktree/build source.
- Dependency inputs unchanged: codex-web
  `91a17d00a737d59a91b5e7bb420aa89e7ec52d93`, llm-agents
  `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`. No changes to `flake.nix`,
  `flake.lock`, `portal/go.mod` or `portal/go.sum`, and no native/Codex runtime
  change. Downstream pin work uses the lead-released final G head after review.

## Delivered change

Five files, 220 insertions and 13 deletions:

| File | Change |
| --- | --- |
| `portal/cmd/workspace-portal/codex_provider.go` | Extract the existing raw SDK composition into a small factory used by the CLI and tests; explicitly supply the `vscode` source list. Preserve disabled implicit resume, submission paths, instruction preservation and absence of routing/watch/question-answer composition. |
| `libexec/workspace-provider-sessions.rb` | Launch scoped helpers through `capture_env!(codex_environment(entry), ...)`, deriving native homes from registered workspace identity. |
| `portal/cmd/workspace-portal/codex_provider_inventory_test.go` | Exercise actual scoped inventory with the production client factory, a disposable retained monitor, metadata-only fake RPC and exact synthetic bootstrap provenance. Include independent missing-source/missing-home controls and wrong source/origin/CWD/ephemeral/history/bootstrap cases. Reject unplanned RPCs; tolerate an unrelated loaded identity within scoped inventory. |
| `test/workspace_host/provider_sessions_test.rb` | Call the actual scoped Ruby helper through a temporary executable subprocess. Verify all native-home variables derive from registration with absent and conflicting parent/host variables; retain scope arguments. No whole-helper override is used by this regression. |
| `portal/cmd/workspace-portal/maintenance_continuation_timeout_test.go` | Correct the pre-existing first-attempt fixture budget from 300 ms to 3 s, including setup/handshake, with the original assertions and production timeouts unchanged. See CI diagnosis below. |

The sufficient architect brief is [Package G in design.md](design.md). No design
deviation, broad constructor change, RetryStore change, diagnostic subsystem or
Archive behavior change was introduced. Fixtures contain only synthetic data.

## Quick verification

All checks used the repository Nix environment with unchanged pinned inputs:

```sh
nix develop --no-write-lock-file --command bash -c \
  'cd portal && go test -mod=readonly ./cmd/workspace-portal -run "TestProvider|TestScopedProvider" -count=1'
nix develop --no-write-lock-file --command ruby \
  test/workspace_host/provider_sessions_test.rb
git diff --check
```

- Focused Go provider/scoped checks: PASS, 1.648 s, tool session 16344 exited 0.
- Ruby: 12 runs, 80 assertions, no failures/errors/skips, 1.373 s;
  tool session 42034 exited 0.
- Go files formatted with the Nix shell's gofmt; staged/final diff checks passed.
- No declared hook framework or active repository hook was present; the ordinary
  Git commit ran without bypass flags. Commit message came from a temporary file.
- Push/remote verification tool session 16741 exited 0. Every owned command ended;
  no native daemon, session service, machine claim or uncertain effect remains.

No long/native integration, package build/check, live provider retry or deployment
was run. These remain after committed-deliverable independent review. The planned
longer check is disposable native idle/working scoped preparation extended with a
valid retained monitor and the real Ruby launch environment; stop at preparation.

## Compatibility, history and documentation

No persisted state/schema, native protocol, journal, provider selection, identity,
permission policy or recovery contract changes. A rollback reads the same state
but restores the two validation refusals. No coordinated node update is needed
for this application fix.

The complete base-to-head series contains two distinct logical changes: the
provider input repair and an independently pre-existing test-fixture correction
required by CI. Per lead decision these remain separate; the latter is not an
obsolete product fixup. No transitional compatibility path, migration,
dependency/pin update or consolidation stream exists. No migration was merged,
released, deployed or externally consumed; there are no migrations in this
package. The original provider range received independent review; lead owns
affected-lane review of the new test-only commit and refreshed final history.

Documentation placement: the nearby factory comment preserves the consequential
raw-client/no-routing invariant. `docs/codex-providers.md`, especially Native
transition and State and package compatibility, already describes the restored
validation and recovery behavior and needs no product prose change. Current
execution/review/deployment evidence belongs here, not in reusable project docs.
No sensitive incident identifiers or metadata are included in the product diff
or this packet.

Next dependency: lead invokes affected independent review for the new test commit
and final range, then owns required CI and separately authorized
integration/deployment.
No lifecycle closure or cleanup is requested.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/>.

## CI follow-up diagnosis

Required Check fast job `132770485616`, run `43700542294`, attempt 1 failed
at `TestMaintenanceCancellationContinuationTimeoutRetriesOriginalIdentity`.
Public log retained at
`/tmp/2026-11-13-archive-confirmation-regression-builds/ci-fast-job.log:1911–1912`
and `:1974–1975` (raw ANSI sibling retained by lead).
Both packaged executions timed out during HTTP/WebSocket handshake before the
fixture reached the deliberately unanswered `thread/resume`. The test's 300 ms
child deadline includes store/identity/recovery work and a freshly constructed
client, so setup competes with the intended bounded native wait. The test is
unchanged from the recorded feature base (introduced by `1b5cebfecceb204ecf5670f5532715fb74f7a1a8`).

The exact unchanged test passed once in the local Nix shell, 0.781 s,
tool session 45271 exit 0. That scoped result does not overturn the CI failure.
No broad CI/test rerun was used as diagnosis. Architect0 recommends a narrowly
scoped first-attempt fixture cap of 3 s, below its 5 s fake-server read timeout
and 10 s parent deadline. Preserve every reached/deadline/parent-live/uncertain
identity/deduplication assertion; no maintenance production seam or deadline
change is needed. Lead accepted this exact test-only correction and required it
as a separate focused commit. The provider commit remains unchanged. The
`reached` request flag, `DeadlineExceeded`, live parent, unsettled/submitting
continuation, stable ID, retry settlement and exactly-one-send assertions all
remain intact. No production maintenance source or timeout changed.

Focused corrected verification:

```sh
nix develop --no-write-lock-file --command bash -c \
  'cd portal && go test -mod=readonly ./cmd/workspace-portal -run "^TestMaintenance(CancellationContinuationTimeoutRetriesOriginalIdentity|CallerDeadlineWinsNativePauseCap|NativePauseCapDerivesBoundedDeadline|SharedAllowanceDoesNotRenewAcrossCalls)$" -count=1'
```

PASS, 3.572 s, tool session 53315 exit 0. Final diff check passed. Separate
commit and SSH push/remote proof completed, tool session 22808 exit 0;
worktree/index clean. No extra long test, build or deployment was launched by
implementer0.

After publication, inspected exact superseded run `43700542294`:
`headSha=e96284d1a0484a01888a6d7166fcbd5f68855659`, `status=in_progress`.
`gh run cancel 43700542294 --repo aither64/dev-workspace` accepted the request,
tool session 58681 exit 0. The immediate status read still showed
`in_progress`; cancellation completion belongs to the lead's existing runtime
observer and is not claimed here. No workflow for final head `9241a342...` was
canceled. Existing fast-failure and passed archive evidence remain preserved.
Every owned local command ended; no unfinished command effect or resource claim
is held.
