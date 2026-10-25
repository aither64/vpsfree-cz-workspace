# Package B execution evidence

Status: independently reviewed functional implementation preserved unchanged;
final corrected dependency refresh committed, quick-checked and published.
Native/packaged verification and deployment remain under the lead's coordination.
No merge authority is implied. The lead owns shared plan/state, review decisions,
and deployment coordination.

Current acceptance blocker: fast job `119971119612` in Check `39820766257`
failed a pre-existing notification browser fixture before its deferred
registration callback became ready. Evidence and the narrow test-only proposal
are in `package-b-current-fast-diagnosis.md`; source/refs remain frozen pending
lead release. No CI rerun or duplicate local verification was launched.

- Repository: `dev-workspace`, SSH `git@github.com:aither64/dev-workspace.git`.
- Worktree: `worktrees/2026-10-20-workspace-session-naming/dev-workspace`.
- Branch: `2026-10-20-workspace-session-naming`; worktree clean.
- Exact initial/current upstream base:
  `bf6d4b0c49600c15e17fe71248807ef43424e932`.
- Tracking prerequisite: workspace `7e66fed3f5160242b56a44aa2a254f2553fa5f36`.
- Exact published final head:
  `4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`.
- SSH remote proof matches `origin/2026-10-20-workspace-session-naming`.
- Exact checked/final tree: `c4e3e4ff05983abdc8051c292b06e9b2ba14db7d`.
- No migrations, persisted-format changes, default-branch integration,
  deployment or lifecycle actions.

## Complete final history and provenance

1. `9d741a1682020d17ffe9cc4bb6c30254575afc58`
   `deps: update codex-web for safe ephemeral naming retries`.
   Go module/checksums, flake source/lock and vendor hash select exactly
   `4300c40b6406161afc74c124c40155f28a557032`.
2. `4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`
   `portal: retry session naming before requesting a manual name`.
   Application behavior, focused/native/browser fixtures and owning docs,
   including the corrected labelled retry-advice fixture and failure diagnostics.

Exactly one dependency-first update stream and one functional commit remain.
Local fixups and provisional selections were consolidated into those owners.
Complete series: `package-b-final-history.txt`; complete final diff:
`package-b-final.diff`. The saved portal comparison binds the exact base/head.
**No migrations** exist in this branch.

Local intermediate `eb28f371`/`0a8e0e7` were reordered before publication and
were never merged, deployed, released or externally consumed. Provisional
published B heads `268f2e87` and `d9ea3925` selected intermediate A
`b81f8058` and `ee119a01` within this same initiative. No deployment or known
supported external compatibility boundary requires retaining those pins.
The A late-error fix and subsequent native-fixture advice correction were folded
into its single owning commit; B's refreshes and fixture fixups were folded into
the two final commits. No obsolete pin or broken dependency ordering remains.

The independent review input was B
`ae0399b31746bc14ea2fcbe3185f36d8e4b04885`, selecting A `96077b62`.
Its exact evidence is preserved in `package-b-reviewed-ae0399/` with a SHA-256
manifest, original patches, history and checks. Review found only A's buffered
post-terminal error ordering defect. A's narrow fix was published provisionally
as `f722adab`; B's corresponding pin stayed uncommitted and unpublished when
native verification exposed an A-only fixture override of the reserved built-in
provider. Its passing 33.110s quick check is explicitly provisional in
`package-b-f722-focused-result.json`. A `4300c40b` removes that fixture override
and retains built-in retry defaults. Actual native acceptance remains separate.

Final B differs from reviewed B in exactly five dependency files: `flake.nix`,
`flake.lock`, `portal/go.mod`, `portal/go.sum`, and `nix/workspace-portal.nix`.
The functional commit patch is byte-identical; `package-b-final-range-diff.txt`
marks it `=`. The dependency delta exactly matches the checked delta, and the
checked/final tree is identical. `package-b-refresh-proof.json` binds both
ranges, hashes, checks and publication. There are exactly two final commits,
no repeated pins, no migrations and no deployed or known supported external
boundary requiring an intermediate pin. All intermediate consumption was
provisional within this same initiative. SSH publication used an explicit
old-`ae0399` lease; the remote default still equals the recorded base.

Production application source, product docs and the browser acceptance helper
are byte-identical to prior `d9ea3925`. Changes after that head are the final
client pin/hash plus the two owning fixture files: `test/creation_model.py` and
`nix/tests/session-creation.nix`. Final consolidation preserved the exact checked
tree. No production policy/API/model/catalog change was added for the fixture.

## Implemented behavior and documentation

One 30-second context starts before queue admission. Two workspace operation
slots remain held through native inference, at most one fresh utility call,
200 ms cancelable backoff and cleanup. Provider resolution happens once; input,
model, effort, instructions and schema stay fixed. Retry requires the public
`codex.CanRetryEphemeralTurn` proof and at least one second inference plus
250 ms cleanup after backoff; context/time are rechecked after waiting.

Generic failure names and the attachment-only placeholder are removed.
Failure leaves base/slug/handoff empty and reuses existing retry/manual controls.
Accepted request/provider/settings/uploads and receipt identity stay unchanged.
Historical saved bases, slugs and `attachment_only` records remain readable.
No UI strings or browser product code changed.

Owning docs: `docs/session-preparations.md`, `docs/workspace-portal.md`, and
`docs/codex-package.md`. Lead applied the context-owned writing/English pass
and approved those exact edits; they have not changed afterward.

## Final quick verification

All checks used the repository Nix environment and exact published A pin,
without a module replacement.

- Focused Go command: `go -C portal test -mod=readonly ./internal/web
  -run 'TestSession(Naming|Name|Preparation(AutomaticRetry|Naming|ProductionNaming|AttachmentOnly|CustomName|Name|ConcurrentName|Shutdown|SavedBase))'
  -count=1 -timeout=50s`: **pass, 32.796s**.
- Actual Python HTTP handler check: `python3
  work/<slug>/package-b-fixture-check.py`: pass. Executes the real handler in
  disposable memory/scratch, with no listener or native inference; proves exact
  nested one-second advice only in labelled progress mode, advice-free terminal
  output, counter decrement and compact diagnostic flags.
- Live overlay compile/list-only: `go -C portal test -mod=readonly
  -overlay=work/<slug>/package-b-live-naming-overlay.json ./internal/web
  -list '^TestDeployedSessionNamingSmoke$' -timeout=10s`: pass, 0.048s.
  No live discovery or inference was executed.
- Final focused and overlay checks ran separately and passed. An earlier
  reviewed-head combined 55s wrapper expired after its Go stage passed; the
  separately repeated overlay/parse checks passed. That older wrapper is
  preserved in the reviewed checkpoint and is not the final check command.
- Exact pin check passed for `v0.0.0-20261022170834-4300c40b6406`.
- Only the `codex-web` flake-lock node moved; no sibling input changed.
- Final vendor hash: `sha256-tv5Wa3sIDf6Fd4J+fXzmDR9AMXpdCeFFkhVesCXI4uQ=`.
  Generated by Nix-shell `go mod vendor` plus `nix hash path`. The same recipe
  previously reproduced the baseline's exact
  `sha256-ABmwKlrjiXjFrrtplRaw2fmMDlv/gxWfufEMA0vjXNQ=` hash.
- Go formatting, Node syntax, Python/embedded VM Python AST, Nix parse and
  `git diff --check`: pass. Application code did not change after earlier checks.
- Commits/rebases used ordinary Nix-environment Git with no hook bypass. No hook
  framework is declared by this repository.

Prior development runs (temporary same-session A replacement, then provisional
published pins) passed in 32.424s, 33.545s and 32.860s. They are superseded by the
final exact-pin result. Temporary module replacement/vendor trees were removed
following evidence capture; no source replacement remains.

## Failed CI evidence and fixture correction

Original log: `package-b-provisional-ci-failed.log`, run `39810261469` on B268.
Fast/package+focused and archive jobs passed. Creation VM failed at the first
native-positive naming case, logging `duration_ms=512 outcome=utility_error
category=server` and showing manual controls before reservation. The run's
artifacts API returned an empty list; exact request counts/native error frames
were not downloadable. The original failed log is retained. The subsequent provisional d9 run
`39812327908` failed at the same native-positive scenario with
`duration_ms=470 outcome=utility_error category=server`; its original log is
`package-b-second-provisional-ci-failed.log`. Both used the advice-free positive
fixture before the final correction.

Architect traced pinned native behavior: overload without structured server
retry advice is terminal before the stream retry loop, regardless of the retry
ceiling. Both A/B positive fixtures omitted that advice. Two terminal failures
exhausting the two fresh calls explains the short failure but remains an
inference because exact old wire counts were unavailable. A's late-error fix
alone did not establish a correction for this fixture.

The final native-progress case emits exactly
`response.error.headers = {"retry-after":"1"}` beside the overload code/message.
The marker is removed before terminal/fresh/persistent cases, which remain
advice-free. Per-response overload/advice modes and remaining counters are now
summarized on VM failure. This is test-only; production policy is unchanged.
Native confirmation still requires the post-review watcher, including owned
retry progress, same-turn success/no early interrupt, and settled fresh recovery.

Coverage inventory: `package-b-coverage-inventory.md` identifies exact existing
collection/preparation/package-generation tests and their package/shard commands.
They are outside the final naming-only quick selector. It explicitly flags the
absence of a packaged real collector-sweep + usable native session scenario.
Architect's `collection-probe-plan.md` prepares a disposable session-only
collector + custom-name portal acceptance/reservation/handoff check; the lead
accepted that limited proof scope. It does not prove a usable native conversation.

## CI snapshot and remaining verification

- Current exact head Check run: `39820766257`, in progress at the nonwaiting
  post-publication snapshot:
  https://github.com/aither64/dev-workspace/actions/runs/39820766257
- Reviewed B `ae0399` run `39814914672` completed/success; its earlier snapshot
  is retained in the reviewed evidence. This is not final-pin acceptance.
- Superseded B268 run `39810261469` and Bd9 run `39812327908` completed/failure.
- No superseded queued/in-progress run remained to cancel. No CI wait, rerun or
  manual workflow trigger was performed. Query evidence: `package-b-ci-status.json`;
  cancellation inventory: `package-b-cancelled-ci.json`.

After its review/fix inspection, the lead launches the required fresh watcher:

```
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation
```

Run from this dev-workspace worktree with Nix/KVM. The package supplies Chromium,
authentication and disposable state; no host environment override is needed.
A's exact native protocol fixture supplies explicit RPC retry/turn/interrupt
proof; B's VM covers production naming admission, automatic/manual workflow,
accepted inputs/files/settings and reservation. Neither fixture code nor these
quick checks are executed native acceptance evidence.

The prepared live model recipe is `package-b-live-naming-smoke.md`, with
compile-only overlay verification above. Its read-only discovery was corrected
for registered identity `vpsfree-cz` and all-OS-thread child enumeration, then
passed against the current predeployment runtime without inference. Diagnosis:
`package-b-live-discovery-diagnosis.md`; snapshot:
`package-b-predeploy-discovery.json`. The model probe calls existing helper code
against the deployed portal-owned backend using disposable scratch, without a
registered test session or new product API. Actual model execution remains the
lead/watcher's post-activation step under machine ownership.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
