# Implementation evidence

Implementer0, 2026-10-29. Assigned serial execution package from the accepted
[design](design.md). No default integration, deployment or lifecycle action.
Lead owns state/plan and final independent review. This file owns detailed
implementation commands and evidence; raw logs below are disposable.

## Identity and actual bases

`dev-session current` returned `2026-10-28-plan-mode-waiting-marker`.
Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE matched the thread binding:
`/home/aither/workspace/ai/vpsfree.cz`. Both canonical origins were checked and
fetched over SSH before registration:

- `git@github.com:aither64/codex-web.git`:
  `f6f4a187509b3bebfc81585c535be856eaab0d04` (`origin/master`).
- `git@github.com:aither64/dev-workspace.git`:
  `cc0d452a0653a112c8a013492c1734d9554bb909` (`origin/master`).

Registered each with `dev-session worktree add <slug> <project> --as-is
--base origin/master --no-fetch`. Branch in each repository is
`2026-10-28-plan-mode-waiting-marker`, under canonical
`worktrees/2026-10-28-plan-mode-waiting-marker/<project>`.
Substantive initial tracking was already committed at workspace `1085b570d`.

## Result and compatibility

Reused the bounded ActivityRecorder Requests map. Only native item/method
identities were added to its existing schema-1 checkpoint request shape.
`ActivitySnapshot.BlockingRequests` projects supported, complete, current-turn
identities using the same durable connected observation as timing. No response
authority or question text is exported. The portal consumes these identities
and retains the exact attentionDigest(thread, turn, item, method) key.
No separate registry, native RPC or production browser implementation changed.

No database migrations, persistent schema version changes, seeds or state
rewrites. Schema-1 JSON readers ignore additive identity fields; new readers
accept their absence, retain totals and omit identities until fresh observation.
Read behavior checked against activity_store.go `readActivityCheckpoint`, which
uses ordinary json.Unmarshal, schema/thread/turn validation and the existing
256 KiB bound. Old writers can omit the fields without changing timing totals.
Connected current observation is not restored from checkpoint state. Existing
128-request bound remains. Old portal source stays compatible with the library;
new portal source requires the exact pinned library. No Codex release change,
coordinated fleet update, runtime activation or deployment was performed.

## Coverage and quick verification

New boundary regression in codex-web uses its real ObserverOnly client against
the existing Unix WebSocket fixture. It receives a blocking Plan question with
isBlocking omitted, observes identity in ReadActivity, has empty Prompts and
writes only expected read/subscription frames. Projection coverage includes
explicit optional input, approvals, duplicate observation, second question,
resolution, terminal metadata, incomplete identity, unknown state/scope and
reconnect. Storage coverage decodes through predecessor request fields and back
to schema 1 while checking totals and absence of private request content.
Existing timing/terminal/bounds tests remain in the selected batch.

Portal regression uses an observer with no Prompts method, projects through
observeAttention/reduceAttention and verifies the attention API input event,
unchanged key, duplicate suppression, second-question identity, approval kind,
stale/foreign/malformed snapshots and resolution. Existing notification test no
longer manufactures answerable prompts. Existing browser harness covers `?`,
focused acknowledgement and reservations; its added resolution assertion retains
`R`. No production title or acknowledgement implementation changed.

Toolchains came from each flake's exact pinned nixpkgs:

- codex-web: `/nix/store/bx7ivhrfvs5263ryip99zkc1v0x853i2-source`.
- dev-workspace: `/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source`.

Fresh watchers use retained catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
utility `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`,
`gpt-6-luna` / low, full-access execution. Installed matching utility TOML
specifies danger-full-access and never approval. Each watcher owns one batch;
none edits source, diagnoses, retries, deploys or grants acceptance.

1. `codex_quick_check`: pinned `nix shell <codex-nixpkgs>#go -c go test
   ./codex -run 'Test(Activity|Observer)'` failed before tests because cgo could
   not find gcc. [Log](logs/codex-quick-1.log). No process remained. Corrected
   the environment once by adding the same pinned nixpkgs gcc.
2. Fresh `codex_quick_check_2`: `nix shell
   /nix/store/bx7ivhrfvs5263ryip99zkc1v0x853i2-source#go
   /nix/store/bx7ivhrfvs5263ryip99zkc1v0x853i2-source#gcc -c go test ./codex
   -run 'Test(Activity|Observer)'` passed (exit 0), 11s elapsed; package 3.192s.
   [Log](logs/codex-quick-2.log). Tested f6f4a187 plus the implementation later
   committed unchanged at 9d337b70987fdf1dd42a5d8efff31f755a122550.
3. Inline known quick browser check from portal/: `nix shell
   /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#nodejs -c node --test
   internal/web/attention_browser_test.cjs` passed 75/75, exit 0, 7.957s.
   Includes final two-line resolution regression. Full output retained in tool
   execution; compact summary here. No browser production file changed.

4. Fresh `portal_quick_check` batch: from portal/, `nix shell
   /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#go
   /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#gcc -c go test
   -mod=readonly ./internal/web -run 'Test(Attention|Notifications)'` passed
   exit 0, 19s elapsed; package 0.588s. [Log](logs/portal-quick-1.log).
   Tested final Go source, generated module pins and browser test diff; later
   vendorHash correction does not affect focused Go or browser source.
   The same watcher ran dependency-only zero-hash discovery on
   `/nix/store/b2rpm7smbn7fzrs4dmp1pxg8mc6bdca7-dev-workspace-0.2.0-go-modules.drv`,
   which completed with expected mismatch exit 1 in 15s. It printed the actual
   hash above; [log](logs/vendor-hash-discovery.log). This was deliberate hash
   discovery, not a test failure. No package or integration suite was run.
5. Inline declared exact-pin check, final dependency inputs: `nix shell
   /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#bash
   /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source#jq -c bash
   nix/check-codex-web-pin.sh portal/go.mod
   v0.0.0-20261029173332-9d337b70987f jq` passed exit 0. Semantic lock
   comparison confirms only the codex-web lock node changed.

6. Fresh standalone CLI `vendor-watcher` (native ID
   `01a188be-4bea-7941-a10a-eb172d7509b5`): `nix build --no-link
   --print-out-paths
   /nix/store/mxvfp26s261x63fbzcx05w8fmzvc2n76-dev-workspace-0.2.0-go-modules.drv^out
   --print-build-logs` passed exit 0 in 0.2s, producing the exact output below.
   [Build log](logs/vendor-hash-verification.log),
   [watcher result](logs/vendor-watcher-result.md),
   [launch transcript](logs/vendor-watcher-transcript.log). Launched fresh
   through `codex --ask-for-approval never exec --sandbox danger-full-access
   --model gpt-6-luna -c 'model_reasoning_effort="low"'` with the matching
   installed utility instructions. Launch banner confirms approval never,
   danger-full-access and low effort. No running operation remains.

Go formatting used pinned gofmt on changed Go files; git diff --check passes.
Neither repository declares a hook framework or core.hooksPath. Canonical hook
directories contain only inactive sample files; no hooks were bypassed. Commits
use focused area: action subjects and temporary message files with git commit -F.

## Publications and dependency stream

codex-web was fetched again, unchanged origin/master, committed then rebased
(no-op) before SSH publication. Exact feature head remote-verified with
`git ls-remote origin refs/heads/2026-10-28-plan-mode-waiting-marker`:
`9d337b70987fdf1dd42a5d8efff31f755a122550`.

Downstream exact dependency update is one stream: codex-web library/source for
portal attention. flake.nix and generated flake.lock select
`9d337b70987fdf1dd42a5d8efff31f755a122550`; `nix flake update codex-web`
changed only that lock node. Locked NAR hash:
`sha256-IGseAWlpopeTARLDeSI5NcWG6QiXBCrmbN6OjqnYw6c=`.
`go get github.com/aither64/codex-web@9d337b70987fdf1dd42a5d8efff31f755a122550`
selects `v0.0.0-20261029173332-9d337b70987f`. Removed only predecessor codex-web
checksum lines after generation; unrelated modules and inputs retained.
The old vendorHash no longer matches. An intentional zero-hash dependency
build discovered `sha256-2f7iuoBO4KsjNKQH4iAOtjWwKuNC9O4H+YfLPtAZy0E=`;
replaced predecessor `sha256-2aYEuOcFTjdecQu/GEP2i2sLlYi5eMnDxpKb2nyU7Mw=`.
Final verification succeeded, exit 0. Exact dependency derivation:
`/nix/store/mxvfp26s261x63fbzcx05w8fmzvc2n76-dev-workspace-0.2.0-go-modules.drv`.
Output: `/nix/store/8m2rrmwr5bcnkw1daii6wb08d3af381b-dev-workspace-0.2.0-go-modules`.
Source: `/nix/store/wdh3nqarvakn0aqs3q4zw479v3lgjr2s-source`.
The complete recursive derivation/source/input graph is retained in
[go-modules-input-graph.json](logs/go-modules-input-graph.json).
Re-evaluation after committing the final downstream source returns the exact
same derivation, establishing that the dependency result applies to that head.

Downstream head `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3` published over SSH
and remote-verified with git ls-remote. Fresh fetch immediately before commit
confirmed unchanged cc0d452a origin/master; rebase was a no-op.
Both worktrees are clean. Captured portal comparisons at these final heads with
`dev-session worktree capture-comparison <slug> <project> --as-is`.

## Whole-branch inventory for independent review

codex-web range:
`f6f4a187509b3bebfc81585c535be856eaab0d04..9d337b70987fdf1dd42a5d8efff31f755a122550`.
One commit: `9d337b7 activity: expose passive blocking request identities`.
Full final diffstat:

```text
 codex/activity.go              |  72 ++++++++++++++-----------
 codex/activity_recording.go    |   3 +-
 codex/activity_snapshot.go     |  27 +++++++++-
 codex/activity_storage_test.go |  48 +++++++++++++++++
 codex/activity_test.go         | 118 +++++++++++++++++++++++++++++++++++++++++
 docs/reference.md              |  17 +++++-
 6 files changed, 252 insertions(+), 33 deletions(-)
```

No obsolete iteration commits, superseded dependency pins, migrations or
transitional migration paths. No feature commit has been merged, released,
deployed or externally consumed as a supported release. Publishing the branch
provides the exact downstream dependency, not release or integration evidence.
dev-workspace range:
`cc0d452a0653a112c8a013492c1734d9554bb909..5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`.
One commit: `5f4f1c1c portal: use passive request identities for attention`.
Full final diffstat:

```text
 docs/browser-notifications.md                  | 10 +++-
 flake.lock                                     |  8 +--
 flake.nix                                      |  2 +-
 nix/workspace-portal.nix                       |  2 +-
 portal/go.mod                                  |  2 +-
 portal/go.sum                                  |  4 +-
 portal/internal/web/attention.go               | 17 ++----
 portal/internal/web/attention_browser_test.cjs |  2 +
 portal/internal/web/attention_test.go          | 80 ++++++++++++++++++++++++++
 portal/internal/web/notifications_test.go      | 17 ++----
 10 files changed, 109 insertions(+), 35 deletions(-)
```

There is one final dependency stream, with no intermediate pin commits or
migration history. The two logical cross-repository commits contain the complete
implementation, focused coverage and owning documentation. Final diffs pass
`git diff --check origin/master..HEAD`. Existing declared hooks are absent in
both repositories (only sample files); no hook bypass was used. Lead directly
applied the user-facing writing skill to browser-notifications.md; implementer
only normalized the requested line wrap afterwards.

Independent reviewer must assess full cleaned series and final diffs, including
an explicit no-migrations/history conclusion. No independent review performed
by implementer; no readiness or integration approval implied.

Lead will run post-review `nix flake check --print-build-logs` in both worktrees
and applicable branch CI through fresh watchers. Implementer did not launch
these long suites or CI waits.

## Diagnostic-only successor after repeated local acceptance failure

The later narrow test-diagnostic commit is `08f3dbb92bc8585929edee85a824d44dfb3b0846`,
published separately after functional runtime target 5f4f1c1c. It does not change
production behavior or dependency pins. The [diagnostic review packet](archive-diagnostic-review-packet.md)
contains final full branch history, quick checks, KVM evidence, minimal recipe
and exact input-graph proof for new diagnostics against the reviewed 5f runtime.
No long VM run by implementer; independent affected-lane review remains with lead.
