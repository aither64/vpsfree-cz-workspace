# Rendered Go acceptance preparation

Preparation only. Tested final head/tree: **UNSET** until the combined package
is committed, quick checks pass, final independent review is accepted, and lead
releases one long batch. Owner1 orchestrates the environment/utility; owner0 owns
Git. No checks, generation, compilation, listener, installation or network probe
ran during this preparation. The four yielded Go source hashes remain unchanged.

## Source blocker to finish before commit/review

Source inspection found two stale legacy profile call sites in
`clients/go/spec/documentation_acceptance.rb`: `check_environment!` and
`prepare_sdk` read `for_version('7')` after `mount`, without completing finalization.
New profiles publish only at successful finalization. Lead granted a narrow
Go-harness-only correction and proportional pure environment regression; owner0
confirmed the legacy-only `finalize(nil)` seam and released the source window.
The two calls and a real environment-preflight call at the start of the existing
build checker are authored. The first quick preflight stopped before app load
because its declared Git binary was absent; that failure is retained in
`client-example-profiles-go-quick/environment-02*`. Owner1 restored/rooted the
same exact declared tools; subsequent actual environment preflight and mounted
DSL checker passed (`environment-03`, `profile-03`), with clean added style and
syntax. No compiler/listener/generation ran. The shared implementation does not use the
server when all registrations already contain prepared legacy profiles. No automatic profile may use this nil-server path.
The old runner SHA before correction is
`c6a9521990dfe7d4b07b46097ec99588f4529d008789ed7f66973e82cf6e3453`.
Current runner SHA is c62cdc3ba0bf8ea8c6a6c847001ec1739013779a39ceec0caf322dbaa6147cd6;
build checker SHA is 6cc2a5699b491aa126896f6d513356f3d6db602eaadd0659d0b3110ca5d5774c.
The completed six-path source/quick yield is in
`client-example-profiles-go-receipt.md/json`; final compiled acceptance stays gated.
Do not launch acceptance with this old runner or an unreviewed successor.

## Command and environment

From the exact registered root
`worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles`:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py go-acceptance -- bundle _4.0.23_ exec ruby clients/go/spec/documentation_acceptance.rb
```

The same command with `--check-environment` is the pure preflight, after the
lifecycle correction. Later use a passive session observer around the actual
runner only if accepted as below. The product runner remains the test oracle.
The existing native build-plan control is `documentation_build_check.rb`; it is
not the compiled acceptance and may invoke Go's dry-run planner/Git. The pure
wire controls are `documentation_wire_check.rb`; they are constructed requests,
not executed Go traffic. Do not replace the actual acceptance with either.

Use the accepted prepared wrapper, SHA
`eb20cb767cf6e056050e6cf580e6c4b06fdfe70518821753ef9a4d3ac030c963`, and its
validated go-acceptance environment. It uses own root `.gems`, own Go `.gems`,
selected Ruby default directory, dedicated frozen Gemfile/config/cache and exact
declared tool PATH; inherited component Ruby/Bundler variables are cleared.
Accepted Ruby is 3.4.11, Bundler 4.0.23, Go toolchain 1.26.9. Exact binaries,
realpaths, hashes, versions and Nix derivation/input graph must be captured at
execution; prior readiness alone is not final tested-input proof. If tools are
missing or a download/install is requested, stop; no automatic setup fallback.
The dedicated ignored lock SHA is
`9854dbae73d4b299a255042bdb562f4ab56475c950ba0076cdf708e3d4b883c0`, the accepted
checksum-only completion from 17738ce7 with all 55 payloads proven. Preserve all
other root/server/Go-unit/Rust lock hashes and source/catalog inputs.

Before the granted batch, select new absent/owned session-only Go cache and temp
paths. Set `GOCACHE`, `GOMODCACHE` and `GOPATH` to those own paths; never borrow an
old writable cache. The helper itself sets `GOWORK=off`, `GOPROXY=off`,
`GOSUMDB=off`, `GOTOOLCHAIN=local` on every command. Keep those restrictions and
record inherited Go flags/toolchain settings; require no unexpected GOFLAGS or
GOENV overrides. Build uses the real command
`go build -buildvcs=false -o TMP/bin ./cmd/...`, local `replace` only. No registry
or toolchain download is needed. Keep fixture loopback traffic functional; do
not dump proxy environment or credentials. Setting `PYTHONDONTWRITEBYTECODE=1`
is already part of the wrapper.

## Actual execution, ownership and stop behavior

The runner owns one in-process `WEBrick::HTTPServer`, bind `127.0.0.1`, port `0`
(ephemeral; actual chosen port is in server config). It mounts the actual fixture
`serve` method at `/`, starts one Ruby thread, and owns its shutdown/join in the
run method's ensure. There is no child HaveAPI Ruby server process and no fixed
4567 port. WEBrick constructs the bound listener before starting its thread; the
runner has no separate HTTP readiness probe or polling loop. Do not invent a
readiness check or retry. Passive evidence can record the actual listener/port,
server-thread status and Ruby PID without adding a request.

It creates one native temporary directory, generates the SDK from its saved
fixture JSON, uses that same JSON as the legacy documentation profile, renders
16 programs, runs actual gofmt, builds all programs once, then executes/verifies
them in table order. SDK/module/canonical names come from the real generator;
program source is the real renderer output. The three authenticated call cases
compose real auth/action renderings through the existing compose helper.

`Open3.capture3` owns each synchronous gofmt/build/program child; a nonzero child
status or any verifier exception immediately aborts remaining cases. The runner
has no retry, upload or polling. Its ensure shuts down and joins the server;
native mktmpdir disposal is part of the existing helper. On a failure retain raw
outputs and observed exact child identity/state; reconcile only owned processes,
with no broad kill or new cleanup policy. No generic quiet timeout is warranted.
A watcher owns one accepted related batch/handle and returns first failure; it
must not diagnose, repair, retry or launch another watcher.

## Cases and actual verifier claims

| Cases | Existing assertions |
| --- | --- |
| init/basic/token/oauth2 | No fixture request. These configure existing credentials; no token-login exchange. |
| object | Mounted/versioned nested path; exact input body preserves nil/false/zero and `_meta:{}`; output contains 123. |
| empty/omitted | Exact `widget:{}` body; no metadata envelope. |
| list/fail/association | Expected mounted path and supplied output substring (1/2, failure text, nested id9). |
| query | Exact parsed full query hash: name empty, boolean `0`, integer `0`; controlled raw query in diagnostic. |
| operation | Initial route then exact action-state55 route; no extra requests. |
| basic_call/token_call/oauth2_call | Same exact object body plus expected auth header value; no extra request. |
| hostile | Exact escaped hostile string body with empty metadata envelope; expected output. |

All non-init cases reject extra fixture requests. The verifier does not assert
HTTP method, every output byte, absence of unrelated auth headers or every
operation progress/cancel behavior; do not overstate those claims. No equality or
validator relaxation is proposed. This acceptance proves the generated fixture
SDK/real rendered programs against a controlled WEBrick responder, not a real
HaveAPI endpoint/authorization/login implementation. The separate current-DSL
pure checker proves adapter registration/filtering and canonical model fidelity.
Neither proves compatibility with an external installed vpsAdmin SDK.

## Evidence and passive observer proposal

The helper captures child stdout/stderr internally but on success returns only
stdout; it prints only the final 16-program total. Its temporary generated tree
is normally disposed. Raw top-level output alone therefore cannot preserve
successful compiler diagnostics, per-case status or generated source inventory.

Proposed minimal SESSION-only observer, subject to lead acceptance before use:
load the unchanged actual runner, prepend transparent wrappers around its actual
`prepare_sdk(dir)`, `prepare_programs(dir)`, `verify`, and `Open3.capture3`; call
`GoDocumentationAcceptance.run!` once. Every wrapper invokes `super` with exactly
the original args/options/block/environment and returns the same value or
re-raises the same exception; no test substitution, source replacement, added
request or alternative verifier. Capture allowlisted argv/cwd, actual returned
stdout/stderr/status/PID, timing, exact started/completed cases, bound port and
server-thread terminal status. Do not log full environment or arbitrary auth
headers. Fixture sample secrets are deterministic; avoid generic HTTP logging.

Copy/hash only the owned generated SDK/description/consumer tree before native
tempdir disposal, at actual generation/render boundaries and after actual gofmt/
build; retain raw rendered and compiled/formatted source distinctly. Capture
partial trees in ensure on first failure. Record generated binaries' hashes
(and bytes if the accepted evidence package requests them), go.mod/description,
all file modes/bytes/hashes, raw outputs and errors. Evidence failure must fail
the operation and must never swallow an original test failure or claim PASS.
Native fixture/tempdir lifetime stays with the actual helper. Observer source,
launch payload and environment must be hashed before the watcher runs.

Require before/after exact committed HEAD/tree/full intended-source inventory,
clean index/nonignored state and lock/dist proofs. Bind accepted final review to
the exact executed source and retain any subsequent input equivalence proof.
A fresh session-policy Luna/low utility owns the one separately granted long
operation using actual parent-verified identity/readiness; owner1 coordinates
the slot. This plan launches no utility and supplies no verification claim.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)

## Prepared observer payload

The accepted proposal is now authored as the session-only
`client-example-profiles-go-observer.rb`, SHA-256
`8d83a20b31634acbf271f3ff1aaf9469a4ff43b5eebc19490cdd510dbb8e4629`.
It has not been loaded or executed. The separately granted syntax-only
check passed exit0; source-inspected signatures match the unchanged actual
helper. See `client-example-profiles-go-observer-syntax/source-inspection.md`. Owner1 has the path for exact
future payload hashing. The future command shape, only after final committed
review and the separate batch grant, is:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py go-acceptance -- bundle _4.0.23_ exec ruby /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-go-observer.rb --root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles --evidence NEW_ABSOLUTE_SESSION_EVIDENCE_PATH
```

This shape must use owner1's then-current validated rooted-tool environment,
not the original stale standalone PATH. The outer batch owns exact source/review/
cache/tool/input guards and final evidence acceptance. The observer does not
supply those proofs and adds no extra fixture requests or test assertions.
