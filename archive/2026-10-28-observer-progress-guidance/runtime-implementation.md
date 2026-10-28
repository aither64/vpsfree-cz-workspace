# Generic runtime implementation package

Implementer1 owns the generic dev-workspace edits and Git operations. Source,
focused checks and SSH publication are complete. Independent final review,
longer checks and deployment remain with the lead. No default integration or
session lifecycle action was performed.

## Exact branch and history

- Repository: `git@github.com:aither64/dev-workspace.git`.
- Worktree: `worktrees/2026-10-28-observer-progress-guidance/dev-workspace`.
- Branch: `2026-10-28-observer-progress-guidance`.
- Base: `d5d2b39b13a6875a26b218ffaf7b589b9d71a1fb`.
- Published head: `4a002f52c3b55099540aa99708d5fcf29f7b2456`.
- Complete series: one commit, `4a002f52c3b55099540aa99708d5fcf29f7b2456`,
  `progress: assess evidence within the current phase`.
- SSH `ls-remote` verified that exact feature head and unchanged remote master
  at the base. Worktree is clean. `capture-comparison` saved the exact range.

Final diffstat:

```text
 docs/dev-sessions.md                             |  43 +++++--
 portal/internal/progressobserver/instructions.go |   4 +-
 portal/internal/web/progress_evidence.go         |   2 +-
 portal/internal/web/progress_evidence_test.go    | 152 +++++++++++++++++------
 portal/internal/web/progress_observer.go         |   8 +-
 5 files changed, 156 insertions(+), 53 deletions(-)
```

No superseded approaches, fixup commits, repeated dependency/pin streams,
migrations, generated dependencies or transitional state changes exist in this
range. There is no migration release/deployment/consumer lineage to preserve.
Older exact stock hashes and `PendingV2Instructions` remain supported recovery
paths. The independent reviewer still owns the whole-branch history and migration
conclusion.

## Result and compatibility

Stock instructions match the architect's shared text exactly: 1,798 UTF-8 bytes,
SHA-256 `c7593c1d8dc796b2ae1abed89c56b55232e7b26db7ac309331e616f853aceb82`.
Exact preceding stock hash
`5703253227dfeff529a053bcc32501eb9ff58fb468f23690b1035d425e53684c`
is recognized alongside both older hashes. Custom near-matches remain custom;
the new stock does not refresh repeatedly.

The scheduled v3 prompt assesses phase and milestone evidence, accepts useful
design learning, preserves contextual checkpoints and anti-stall signals, and
requires evidence of stable contracts and independence before splitting work or
deferring authentication. The source map names optional design.md. Matching-key
resolution can correct a mistaken stall premise without code delivery.

New lead notices use the lead's final writing-skill pass verbatim. Dynamic
arguments and `Progress response <key>: <decision and reason>` are unchanged.
Stored notices, pending v2/v3 messages and options, submission IDs, native
thread identity, model/effort, custom policy, idle gates and manual deferral retain
their existing paths. No scheduler, schema, protocol, lifecycle, native injection
or recovery implementation changed.

`docs/dev-sessions.md` owns the lasting behavior explanation; its existing entry
point remains valid. No rollout instructions were mixed into feature docs.
There were no material deviations from the architect's brief.

## Verification

The fresh operation-only watcher used retained catalog digest
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`,
`utilities.verification_watcher` GPT-6 Luna/low and its matching native utility
identity `dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`, with full access
and approval policy never. It ran:

```sh
nix develop . --command bash -c 'cd portal && go test -mod=readonly ./internal/progressobserver ./internal/web ./internal/workspacecodex -run TestProgress -count=1 -v'
```

Result: exit 0 in 30 seconds; all selected tests passed in all three packages.
Full output: `/tmp/observer-progress-runtime-quick-20261028.log` (disposable).
The implemented source was tested before commit; only gofmt and documentation
reflow followed. The six-member source-map prompt measured 3,484 bytes against
the unchanged 4,096-byte bound. Tests cover current/older stock refresh, custom
retention, idle/manual work, original pending v2/v3 request options, and matching
design evidence through normal concern/result/notice handling. Existing wrong-key,
acknowledgment, missing-evidence and native same-thread/manual-retry coverage passed.

Nix-environment gofmt verification and `git diff --check` passed. No hook framework
is declared in this repository and no active hooks were found; the commit ran
through its Nix environment without bypasses. Stock equality with design.md and
the instruction byte count were independently checked after commit.

Automatically triggered GitHub CI was in progress when handed off:
[run 40660885906](https://github.com/aither64/dev-workspace/actions/runs/40660885906),
exact head `4a002f52c3b55099540aa99708d5fcf29f7b2456`. No CI wait or manual long
integration run was started before final review.

After final review, the architect recommends one existing packaged-suite batch,
`nix flake check --print-build-logs`, using a fresh watcher, then the composed
workspace/configuration checks owned by the lead. Stop that batch at its recorded
result or an established escalation; no additional framework or unrelated
investigation is needed for this package.

Remaining limits: tests verify guidance delivery and compatibility, not model
judgment quality. Independent review must assess meaning across all three prompt
surfaces. No candidate package, host deployment, live observer refresh or machine
ownership was exercised by implementer1.

The lead and implementer0 were notified of the exact published dependency head.
Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-observer-progress-guidance/
