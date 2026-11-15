# Scoped preparation reproduction

Package E, implementer0, 2026-11-15. Isolated diagnosis only; no project fix,
commit, real-session access, provider switch or session lifecycle action.
Lead owns acceptance and plan/state; architect0 owns design.md.

## Identity and exact inputs

`dev-session current`, both DEV_SESSION identity variables and the trusted
thread binding match `2026-11-13-archive-confirmation-regression` in
`/home/aither/workspace/ai/vpsfree.cz`. Retained roster: implementer0,
workspace_write, GPT-6.1 Sol/xhigh.

- Source: `git@github.com:aither64/dev-workspace.git`, exact base/head
  `22351ed4207c47bf5ff3d975e7ab3d1f9fb73c92`.
- Own registered branch: `2026-11-13-archive-confirmation-regression-e`;
  worktree: `worktrees/2026-11-13-archive-confirmation-regression/dev-workspace-e`.
- Installed helper:
  `/nix/store/q85i6cmv3qkmif3k23nn3qvzsh779f7b-dev-workspace-0.2.0/bin/workspace-portal`;
  immutable source `/nix/store/q0dlf4srzzd1vm4bv35197cji10d3x4x-source`.
- Exact native executable:
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
- codex-web: `91a17d00a737d59a91b5e7bb420aa89e7ec52d93`.

## Fixture and effects

Inspected the original `provider_scoped_integration_test.go` harness in full.
Its `TestNativeScopedProviderSwitch` includes native archive/unarchive and full
switch/continuation; it was not run. A separate untracked diagnostic fixture
`portal/cmd/workspace-portal/provider_prepare_diagnosis_test.go` uses its native
startup, synthetic loopback backend and private metadata conventions, but calls
only the installed `codex-provider scoped-prepare` for two separate scopes:
idle and working. It preserves raw helper stdout/stderr privately and records
only ID/source/CWD/path/model/effort/status, settings-read result, progress and
whether the original turn remains active.

All fixture state is confined to `/tmp/provider-prepare-e-20261115` (0700),
including synthetic HOME, CODEX_HOME, XDG_STATE_HOME, authority, package metadata,
manifest, native socket and histories. The model backend uses loopback and a
synthetic credential string; no provider catalog or real credentials are read.
The daemon is killed and joined by fixture cleanup. The test context is 45 s;
Go test has a 60 s timeout. The entire wrapper is launched through a registered
session service so backend and native descendants remain in its cgroup.

Executed registered command:

```sh
dev-session service run 2026-11-13-archive-confirmation-regression --as-is \
  --name provider-prepare-e --id eca2ed83-ad55-4546-bbb6-0b219469bfed \
  --cwd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-archive-confirmation-regression/dev-workspace-e \
  --json -- /run/current-system/sw/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-archive-confirmation-regression/dev-workspace-e/run-provider-diagnosis.sh
```

The wrapper enters the repository Nix shell, formats the owned fixture, and runs:

```sh
go test -mod=readonly -tags provider_prepare_diagnosis \
  -run '^TestProviderPrepareDiagnosis$' -v ./cmd/workspace-portal -count=1 -timeout=60s
```

Raw private artifacts: `check.log`, `native.log`, per-scope `.stdout`/`.stderr`,
`result.json`; authoritative wrapper completion is `exit-status` in that temp
directory. Lead received exact command/effects to arrange a fresh watcher before
execution. Lead registered monitor `a43ecfe9-42bd-40b9-984e-43bc112e0f4c`,
validated frozen Luna/low/full_access policy and actual utility thread/turn
receipt. The watcher owns command/status/log observation; implementer0 does not
duplicate polling. The fixture has no project implementation or commits,
migration or published/deployed lineage.

## Result and interpretation

Monitor `a43ecfe9-42bd-40b9-984e-43bc112e0f4c` reported terminal success;
authoritative `exit-status` is 0 and Go reports PASS in 1.208 s (fixture 1.15 s).
Watcher tool session 69196 exited 0 with no reported unfinished effects. Lead
independently verified service `eca2ed83-ad55-4546-bbb6-0b219469bfed` had
authoritative state `exited`, error null, observed 08:59:32 UTC. Its retained
phase field still said `running`; the observed state establishes exit. No
service stop, cleanup or session lifecycle action was taken.

| Observed field | Idle | Working |
| --- | --- | --- |
| Helper exit / stderr | 0 / empty | 0 / empty |
| Direct `ReadThreadSettings` | success | success |
| Native metadata model / effort | `gpt-5.5` / `low` | `gpt-5.5` / `low` |
| Source / CWD / rollout path | `vscode` / exact / materialized | `vscode` / exact / materialized |
| Native metadata status | `active`, empty activeFlags | `active`, empty activeFlags |
| Snapshot intent `active` | false | true |
| Original turn active after preparation | false | true |
| Last progress stage | `capturing-settings`, no failure reason | `capturing-settings`, no failure reason |

The snapshot intent proves the working scope really had an in-progress turn;
the metadata status `active` describes a loaded native thread and alone does
not distinguish idle from working. Both snapshots contain exactly one retained
thread. The helper accepts the client's `thread/read excludeTurns:true` request
shape on this native version. No underlying error exists to sanitize in this
successful run.

This rules out ordinary active-turn preparation as the failure trigger in the
exact current native/helper/codex-web combination with freshly materialized
single-root histories and an unmanaged package fixture. It does not prove the
real operation's retained metadata, managed catalog/team state, ownership,
private files or historical execution generation. Do not prescribe idleness as
the fix. No broad fixture rerun is needed without a concrete difference.

Post-gofmt fixture SHA256:
`6526d2678cff932d9c644227afbef9780899debaa81be5a1efc5d77ecd56f30e`.
Wrapper SHA256:
`dcffeefe0f37c97eb1c0a0e05d5b801f20f61d549e59fb8eb717ac576a5eec93`.
Raw result SHA256:
`e333407cadaf26d504320c68efab3febaff4ff4bb620b78fc796707dddbfa2e4`.

## Next discriminant and read-only probe

Architect0 owns comparing the exact failed operation's native metadata with the
successful fixture, using only thread IDs/socket from the narrowly filtered
shared operation record. Implementer0 has not accessed the real target.

Prepared an untracked disposable probe at
`portal/cmd/provider-metadata-diagnosis/main.go` in the same own worktree. The
cached build in the repository Nix shell succeeded with exit 0; tool session
69331 was joined. Exact executable:
`/tmp/provider-prepare-e-20261115/provider-metadata-readonly`.

```sh
/tmp/provider-prepare-e-20261115/provider-metadata-readonly \
  --socket "$operation_socket" --thread "$operation_root"
```

Only operation-bound values may be supplied by architect0; repeat `--thread`
only for additional explicitly permitted IDs. The source was sent for inspection
before invocation. It uses a direct WebSocket connection and a single outgoing
send path that rejects any method except `initialize`, `initialized`, and
`thread/read` with exactly `threadId` and `includeTurns:false`. Reads are bound
to the exact supplied ID set. It does not use automatic-resume client wrappers,
install watches, read turns/pages, reply to native prompts, cancel, write
settings or run preparation. A global 10-second context bounds the read.
Output contains only requested ID/readState and the allowed native metadata
ID/source/CWD/path/model/effort/status/projectId, or a numeric native error code
and fixed error category. Full response/error messages are never printed.

Probe source SHA256:
`d6ad116a083bf5b28f2761b45485f1fdbd9ce0fca561c6e1abd5faa21ec4f98e`.
Executable SHA256:
`e5fe04705c6d9133e295f83962957967b7d8e50f704d9f1f894b76a5f4ecc120`.

Architect0's exact-native schema inspection establishes that `Thread.model` is
optional/nullable, not absent from the 0.165.0 protocol: null is permitted when
unavailable. Therefore neither protocol removal nor activity is a cause until
the operation-specific response proves it.

Stable session URL:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/>.

## Package F: read-only preparation diagnosis

The scoped helper bypasses the ordinary workspace client constructor and loses
two inputs required to validate retained native utilities. These are source
defects in the exact package already identified above, independent of thread
activity. The isolated fixture in package E had no retained utility, so it did
not exercise this path.

1. `portal/cmd/workspace-portal/codex_provider.go:93–99` constructs the SDK
   client without `ThreadSourceKinds`. SDK `NewWithOptions` at
   `codex/client.go:959` retains an empty slice; it supplies no default.
   `headlessThreadMaterialized` at `codex/headless.go:34–38` requires the thread
   source to be in that list, using `threadSource` at `codex/client.go:5936–5938`.
   An empty list rejects the expected `vscode` source and returns the exact
   fixed error **`headless Codex thread has the wrong identity`**. The normal
   workspace constructor sets `ThreadSourceKinds` to `[]string{"vscode"}` at
   `portal/internal/workspacecodex/client.go:61`.
2. The scoped Ruby launch uses `capture!` and does not supply the existing
   `codex_environment(entry)`, unlike the ordinary provider helper. The worker
   environment lacks `DEV_WORKSPACE_CODEX_HOME`; the raw client's `CodexHome`
   is therefore empty. After source validation is corrected, native archive
   proof fails with the exact fixed error **`archive proof requires a retained
   thread, canonical directory and Codex home`** at
   `portal/internal/workspacecodex/archive_proof.go:78–85`. The canonical-home
   value supplied by the existing environment helper is the required input.

Both failures arise during `buildProviderInventoryScope` while progress still
says `locking-sessions`: utility inventory calls `monitoroperation.Lifecycle.State`,
whose order is project metadata, thread metadata, automated bootstrap provenance,
then archive-state proof. The initial failure is the source-list omission; the
missing home is the next blocker. Neither requires the thread to become idle.

The smallest proposed remedy is to supply the explicit application source list
to the existing raw SDK construction and launch scoped helpers with the existing
Codex environment helper. Preserve the raw client's no-watch/no-routing behavior;
do not replace it wholesale with a client that adds ordinary mutation behavior.
Architect0 owns the design; no functional fix has been made.

### Exact bounded comparisons

Reused the original installed-source validators, including the automated native
bootstrap-identity validator. Only the allowed source list and the local
`CodexHome` input changed between the following reader instances:

| Reader inputs | Project metadata | Thread metadata | Bootstrap provenance | Archive-state proof |
| --- | --- | --- | --- | --- |
| Original empty source list, empty home | pass | pass | wrong-identity error | not reached |
| Empty source list, canonical home only | pass | pass | same wrong-identity error | not reached |
| `vscode` source only, empty home | pass | pass | pass | missing canonical-home error |
| `vscode` source and canonical home | pass | pass | pass | pass, `ArchiveActive` |

The bounded local authority, pending-lifecycle, retained-root/readiness, catalog,
roster and target-filtered inventory checks passed before these comparisons.
The SDK was an observer with implicit resume disabled. No runtime/store lock,
retry cancellation, native activation, prepare, close, archive, provider switch,
routing change or state write was performed. The automated validator returned
only fixed success/error categories; no provenance or conversation content was
printed or copied. Incident-specific metadata and exact identifiers remain in
private, untracked artifacts; they are deliberately omitted here.

Temporary diagnostic source, under the registered `dev-workspace-e` worktree:

- `portal/cmd/workspace-portal/provider_preparation_readonly_test.go`
- `portal/internal/monitoroperation/preparation_diagnostic.go`

The second file reuses existing strict record readers and the original Inventory
body, substituting passive, target-filtered snapshots for methods that would
otherwise create/acquire lock files. Original application files are untouched.
These temporary sources are untracked and have not been committed.

Both runs used the repository Nix shell and this focused command from `portal/`:

```sh
PROVIDER_PREPARATION_READONLY=exact-target-confirmed \
  go test -mod=readonly -tags provider_prepare_diagnosis \
  -run '^TestProviderPreparationReadonly$' -v ./cmd/workspace-portal \
  -count=1 -timeout=30s
```

The RPC context was 10 seconds. Initial original/home-only comparison: diagnostic
exit 1, 0.389 s, joined tool session `37540`; this is the expected recorded
validator failure. Source-only/source-plus-home comparison: exit 0, PASS in
0.398 s, joined tool session `88894`. Both commands exited; no operation-owned
process or uncertain effect remains. No new daemon or service was launched.

Private local logs:
[initial comparison](/tmp/provider-prepare-e-20261115/target-readonly.log) and
[causal comparison](/tmp/provider-prepare-e-20261115/target-source-comparison.log).
They remain outside tracked/portal evidence and must not be copied into ordinary
session records. Source and log SHA256 values:

| Artifact | SHA256 |
| --- | --- |
| Final temporary test | `73ce0aa2011dbc64054e2539c415617e72a808b34858ed7bb1cb7180b57f59a3` |
| Passive inventory adapter | `d82e038dac327b307879ac70c198cd1bcd89d94239cfcbf49c0ea74766f9c38d` |
| Initial comparison log | `8539a7451aafa167be3ae9cdc809a69d74cb808191f082e097f40aca833ad9d0` |
| Causal comparison log | `23efd45e450763c04fd050705b876a9fe376aa6014cab1a43e6bbc0a17abdc2f` |

This establishes the first real failing gate and the succeeding gate with only
the proposed input corrections. It is not a full provider switch, review,
deployment or proof that every later retained utility/member would pass. No
broader run is needed to establish this cause. Head remains
`22351ed4207c47bf5ff3d975e7ab3d1f9fb73c92`; there are no new commits,
migrations, publication, integration or deployment effects.
