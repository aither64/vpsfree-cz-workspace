# Runtime package review evidence

Owner: implementer1. Current milestone: source/quick preparation complete at
`71654e18c5558c6b8b5cb3f33bfedced7fab727d`; exact artifacts restored and rooted;
bounded diagnostic complete with an incomplete resume control and full teardown.
Codex 0.167 acceptance/deployment is blocked on intentional provider admission
incompatibility. User choice pending: authorized native compatibility patch/rebuild
or retain installed 0.165. No further probe, materialization, inference, patch or
build is running/authorized during that wait. Retain R ownership for the response
and review findings. No integration, activation or session lifecycle action occurred.

## Final source and complete history

- Repository: `git@github.com:aither64/dev-workspace.git`.
- Branch: `2026-11-08-codex-version-update`.
- Worktree: `worktrees/2026-11-08-codex-version-update/dev-workspace`.
- Base: `32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6`, still current fetched
  `origin/master` at publication.
- Final head: `71654e18c5558c6b8b5cb3f33bfedced7fab727d`, clean, SSH-published
  and independently verified with `git ls-remote` by implementer and lead.
- Sole commit: `codex: update packaged runtime and naming to 0.167.0`.
- Entire series/final diff: base..head above, 14 files, 57 insertions and
  56 deletions. No intermediate runtime pin commits or fixups remain.
- Final fetched source: `/nix/store/hl0gh74z1yyy30xw6wac2l319vqcawkb-source`;
  narHash `sha256-f5FD3Si1aOYE+qIeyv0gqw56E9IetR4NWDBmpDQa8MU=`.

Changed paths: `flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum`,
`nix/workspace-portal.nix`, `nix/tests/session-creation.nix`,
`portal/cmd/workspace-portal/{naming_runtime.go,naming_runtime_test.go,
naming_runtime_integration_test.go,maintenance_native_integration_test.go,
monitor_native_integration_test.go,session_communication_native_integration_test.go}`,
`docs/codex-package.md` and `docs/session-preparations.md`.

Scope: frozen Codex selection, matching final codex-web Nix/Go/vendor pins,
exact 0.167 host/child naming prerequisites, current actual-native fixture
provenance and supported-version docs. Old 0.165/0.166 and wrong-version naming
startup are rejected before any bundled execution. Canonical catalog bytes,
materialized assembly, protected fixture ancestors, local-only child launch,
existing deadline/cancellation, ordinary-daemon continuity and forward recovery
contracts remain intact. Historical unrelated fixtures remain unchanged.

**History/migrations:** one logical dependency stream with only final W
successor selected. The earlier W `7e3143b` pin/vendor discovery existed only
in the uncommitted worktree and logs; final code/checksums contain none of it.
No schema, migrations, persisted-state format or migration guards were added.
No version in this branch was deployed, released or externally consumed before
publication. C/S consume the final published head. Independent whole-branch
history/migration conclusion remains the reviewer's gate.

## Exact input, binary and catalog graph

- llm-agents: `d960982d3b05c294f3cf98cab3e23798548a0ced`, narHash
  `sha256-h0CHJMm9bCObkUg2VU1B/QCFWC28eg7YMylnlrTKG2U=`.
- codex-web: corrected accepted `f78eae3415d20b98503f11e9fe251e3111bfe4da`;
  source `/nix/store/2y2a7df1yv9aadbb10ykwibx465wb17g-source`; narHash
  `sha256-1QVZzEjeu/cjlcTlGTQyMGIuuPqKZ1YsXtOJV59ZROM=`.
- Go pseudo-version: `v0.0.0-20261108230351-f78eae3415d2`; Sum
  `h1:aMt3t21u+m0Yf6mHc/O9RG9deTtAuyEZMyZqPlc5f7U=`; GoModSum
  `h1:z4to20c2m2G4k2YusCQCw3g7z1g63EugO4dmjTgo+dM=`.
- Vendor hash: `sha256-jUWhtHeiuyvh4Rzf/0KePGFrG72pNimtH6GBKJhRVkk=`.
- Semantic scoped lock diff: codex-web, llm-agents and llm-agents' own
  flake-parts/nixpkgs nodes only. Root inputs, root nixpkgs and unrelated nodes
  unchanged. `go mod tidy` removed superseded codex-web checksums.
- Codex 0.167.0 output: `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0`.
- Derivation: `/nix/store/9rxjqb3nzbf4b9s0bj3h4yl8igm105is-codex-0.167.0.drv`.
- Native: output plus `/libexec/codex/bin/codex`; SHA-256
  `13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10`.
  Isolated private-home `--version` reports `codex-cli 0.167.0`.
- Fetched source: `/nix/store/j9bhifsiqjhxknbzmx46884jnr1lffrc-source/codex-rs`.
- Explicit reconstructed prepared-source receipt:
  `/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs`. It incorporates
  derivation daemon-nix-store.patch, store/output substitutions, chatgpt
  recursion limit and Cargo preBuild settings. This is a reconstructed receipt,
  not fetched source or an independently built-source output. Config/catalog
  bytes remain identical to fetched source.
- Config schema SHA-256:
  `66ed795352d32f2464778acd2e332b7fafe644246d540cdceec4663c56cfbc16`.
- Full 0.165/0.167 catalog: 539696 bytes; SHA-256
  `1384625c0b6b3e67d3c60da29becea2b017f2c283fc1e2d05b8edafb4698eb10`.
- Canonical Luna: unchanged 62680 bytes; SHA-256
  `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
- Evaluated assembly: `/nix/store/7n09p85h6ax3nx4nvkjydlk67s1inm1k-codex-package-0.167.0`;
  derivation `/nix/store/06bnk8f7w91p47siklhxg2sni74fj9gn-codex-package-0.167.0.drv`.
- Evaluated generic package: `/nix/store/96fn4gsrbj9q8ldajmjx66qi920zdhsp-dev-workspace-0.2.0`;
  final exact remote-source derivation
  `/nix/store/kzkw39jk9gkp2ml7x7r6xkh10i8bm0i3-dev-workspace-0.2.0.drv`.

The upstream output still symlinks rg/bwrap outside its runtime root, so keep
mkCodexPackage. Actual deployed daemon identity must be checked independently
of CLI/assembly identity. System and workspace assembly closures can differ.

## Executed preparation and quick verification

Fresh watchers resolved installed full-access Luna/low policy from package
`/nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d` and its
matching native utility TOML. No watcher left a running tool session.

- Exact cached native/source retrieval: `nix copy --from https://cache.numtide.com`
  with the two frozen roots; exit 0 in 7.84 seconds,
  `/tmp/codex-0167-realization-1.log`. No Rust compilation.
- Independent naming/source quick batch: exit 0, about 48 seconds,
  `/tmp/codex-r-0167-source-quick.log`. Go naming tests and tagged compile;
  local workspace protocol corpus; Ruby provenance/compatible-client checks
  (2 tests/5 assertions) and native private-preflight selector
  (1 test/114 assertions), no failures/errors/skips.
- Final corrected-W vendor discovery: uniquely named fake-hash derivation
  `/nix/store/ivld0kd4xqyg9np2g6r1wb9wa2s97fm4-codex-0167-vendor-discovery-f78eae3415d2.drv`;
  expected exit 1 hash mismatch in 16 seconds, actual final digest above,
  `/tmp/codex-r-0167-vendor-final-discovery.log`.
- Final proof plus focused quick batch: exit 0 in 55 seconds,
  `/tmp/codex-r-0167-final-proof-quick.log`. Fresh proof output was absent
  before build, and log shows the derivation actually built:
  `/nix/store/ga92ypjflph129cvnf3kf2i9v5ahwiqx-codex-0167-vendor-proof-f78eae3415d2.drv`;
  output `/nix/store/mx719bvia39xhmyy4d2kci4xv804m9fs-codex-0167-vendor-proof-f78eae3415d2`.
  `nix hash path` independently matches the final vendorHash.

Final commands: `nix build --impure --no-link --print-build-logs --file
/tmp/codex-r-0167-vendor-proof.nix .`, then repository `nix develop` running
pin-consistency checker and its positive/negative corpus, `go -C portal mod
verify`, focused naming Go selectors, compile-only tagged
`live_switch_integration,naming_runtime_integration`, local
`workspace_protocol_contract.py` against shared exact-native
`codex-native-0167/schemas`, Node syntax and `git diff --check`. No native
fixture execution occurred. No declared hook framework exists in this repo;
ordinary Git hooks were preserved and not bypassed.

Documentation: owning package/preparation guides now state the exact 0.167
contract while preserving strict 0.163 and prior prompted boundaries. Version
selectors are needed by executable preflight and maintained update guidance.
Logging retention checked against selected native source. Prose reviewed with
the writing/Humanizer skills; recovery and tool-effect limitations preserved.

## Remaining review, CI and long verification

Exact-head CI: [Check 42534510998](https://github.com/aither64/dev-workspace/actions/runs/42534510998),
attempt 1, head `71654e18c5558c6b8b5cb3f33bfedced7fab727d`, running.
Obsolete c92d539 run 42533810335 finished cancelled after the successor
publication/cancellation request. Archive/creation package dependencies had
already failed in fixup; fast was cancelled, host skipped. Logs were inspected:
checkPhase passed, the builder exited just after the native version probe,
consistent with the known stale equality in that source. Logs do not print the
failing shell assertion. The successor derives the correct expected version.
No old-run retry. Log: `/tmp/codex-r-0167-ci-watch-failures.log`; old watcher
accounted for all tool sessions, none left running.
No workflow dispatched or retried by this package.

Combined final review precedes local package/native/VM builds and executions.
Existing auto-triggered CI is observed independently. Required post-review
checks include packaged contracts/full applicable suite and the accepted
managed naming VM fixture. No deployment/readiness claim is made here.

Harness: [runtime-naming-vm.nix](runtime-naming-vm.nix), parse passed. It selects
the final reviewed composed workspace with exact runtime/provider/extension/
workspace heads; uses final package vendorHash and pin-check postPatch; and
freezes manifest hashes from exact package/source/test binary bytes. Native SHA,
prepared-source identity, protected ancestors and all fixture resource guards
remain enforced. It explicitly retains prepared source with `builtins.storePath`
and `additionalPaths`, then checks guest-readable config/catalog files. Ancestor
constants are checked in the frozen manifest, without guest `.git`; independently
prove final Git ancestry while preparing heads. UID1000 and systemd user cgroup
own the disposable guest units. Loopback synthetic providers are permitted,
the fixed denied-canary counter rejects its port, and other developer egress is
rejected. Only the read-only counter helper has narrow sudo permission.
No live Codex homes, sockets, registries or authorities are mounted or selected.

Post-review invocation, with actual final reviewed values:

```sh
nix build --impure --no-link --print-build-logs \
  --file work/2026-11-08-codex-version-update/runtime-naming-vm.nix \
  --argstr workspaceRef 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/workspace?rev=3f813d5862c1a29d8dd34bd78863b5dfba38767a' \
  --argstr headsFile /home/aither/workspace/ai/vpsfree.cz/work/2026-11-08-codex-version-update/runtime-heads.json
```

Final harness head binding: workspace `3f813d5862c1a29d8dd34bd78863b5dfba38767a`,
runtime `71654e18c5558c6b8b5cb3f33bfedced7fab727d`, provider
`f78eae3415d20b98503f11e9fe251e3111bfe4da`, extension
`f8da821e3c76e26e73aa9d89a712eab0e0faa319`. S supplied the refreshed published
workspace head after its semantic and joint checker passed. Store these four
values as the named heads-file keys before the post-review invocation.

Before build, capture evaluated VM/fixture/manifest derivations, full input graph,
prepared-source inclusion, guest kernel output/cache availability and dry run.
Guest `test -r` supplies executed source readability proof. Stop unexpected local
kernel compilation and investigate. Existing test outer limit is 300 seconds;
expected risk is VM/build prerequisites and native behavior. Required selectors:
`TestManagedNamingRuntimeIntegration` and `TestNativeNamingRuntimeHTTPFailure`.
Failure logs copy before assertion. No VM/native run or kernel-cache claim yet.

Trust boundary: local host operator is trusted; remote HTTP/MCP/client inputs
retain existing authority checks. This package adds no operator-hardening scope.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-codex-version-update/

## Narrow package-assertion correction

S inspected the committed package before any local build and found the old
0.165 literal in `nix/workspace-portal.nix` postFixup. Focused checks had missed
that packaged assertion. The accepted correction derives only that assertion's
expected CLI text from selected `codex.version`; evaluated postFixup now expects
exactly `codex-cli 0.167.0`. Equality, explicit naming 0.167 guards and historical
negative fixtures remain unchanged. Generated postFixup passed `bash -n` in the
repository Nix environment, current Nix/native assertions were inspected, and
`git diff --check` passed. No package/native integration build was run.

Successor delta against historical c92d539 is one changed assertion line. The
sole owning update was amended and SSH-published with an exact-old-head
force-with-lease. Final Nix/Go lock/module/pin-check files were byte-verified
against the successful dependency receipts above; dependency identities, module
set and vendorHash are unchanged. The final vendor proof remains valid within
that unchanged scope, while the generic package derivation changes with source.
C/S were notified to consolidate their undeployed pins before combined review.

## Prepared retained R execution gate

`runtime-heads.json` contains the exact four heads above. It is a prepared
verification input, not an execution receipt. During review no harness evaluation
or build is authorized, and no reviewed source/harness edit is performed.

After explicit review release, R will use one fresh watcher for a bounded
preflight/evidence batch before deciding whether the VM can build:

1. Evaluate the exact invocation's `drvPath`, capture its recursive derivation
   graph with `nix derivation show --recursive VM_DRV`, and capture
   `nix-store --query --requisites VM_DRV`. Confirm exact source, package,
   fixture, manifest and reconstructed prepared-source dependencies.
2. Identify guest kernel derivation/output from that graph. Check its store
   availability and `nix path-info --store https://cache.nixos.org KERNEL_OUTPUT`,
   then inspect the exact harness build `--dry-run`. A missing kernel substitute
   stops launch for diagnosis; no unexpected local kernel compilation.
3. Verify protected ancestor relationships from the recorded bare refs; the guest
   retains frozen manifest constants and requires no `.git` data. The harness
   checks config/catalog readability before executing tests in guest-only state.
4. Record whether composed output/driver prerequisites already have S-owned
   successful derivation receipts. Do not launch a second full composed-package
   build. The harness dependency points at the same final S package, allowing
   exact store reuse.

The actual post-review build command is the fully bound invocation above.
Existing VM test timeout is 300 seconds (outer driver command 360 seconds);
first materialization cost is separate and depends on cache/build prerequisites.
Run only after preflight, using a fresh watcher with kernel escalation policy.
No live services, homes, sockets, authority or registry are selected.

Additional retained R checks are the `codex-package` assembly contract and
required current native runtime selectors (monitor operation, bounded pause and
communication) with exact selected native and final S managed package. Native
state-upgrade and prompted utility protocol checks remain W-owned. Full generic
package or composed builds already proven by identical derivation/input receipts
will be reused within scope, while CI observation stays lead-owned. The exact
release batch and available receipts determine which remaining commands need
execution; this preparation claims no check executed.

## Exact artifact recovery and GC roots during review

Reviewer and lead found the unrooted native/fetched/prepared paths collected.
Historical successful quick/proof results above remain historical evidence;
artifact availability is separately established here. No application source or
reviewed harness changed.

Recovery command: `bash /tmp/codex-r-0167-recovery.sh`, containing the original
exact `nix copy --from https://cache.numtide.com` with native22139ip and fetched
sourcej9bh roots, followed immediately by `nix-store --realise EXACT_PATH
--add-root SESSION_ROOT` for each. Exit 0 in 3.86 seconds;
`/tmp/codex-r-0167-recovery.log`. Cached native NAR hash still
`sha256-O2aF3vo39LJj+tY6dhFFbd/mQp1dip6UCOolQ+RJOcc=`. No compilation.
Native delegation was unavailable in this turn; bounded direct monitoring used.

The original prepared working copy
`/tmp/codex-0167-prepared-47wvj0l0/codex-rs` survived. Its previously recorded
prepare_install.rs, chatgpt/src/lib.rs, Cargo.toml, config and catalog hashes
matched; `nix-store --add` reproduced exactly
`/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs`, then it was rooted.
No arbitrary replacement source was used. Native/config/catalog hashes match
the exact receipts above, and fetched/prepared config/catalog bytes are equal.

All roots below are absolute children of
`/home/aither/workspace/ai/vpsfree.cz/work/2026-11-08-codex-version-update/gc-roots/`:

| Root | Exact target |
| --- | --- |
| `native` | `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0` |
| `fetched-source` | `/nix/store/j9bhifsiqjhxknbzmx46884jnr1lffrc-source` |
| `prepared-source` | `/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs` |
| `llm-source` | `/nix/store/ib6qj3vlq8fjja2bm5dl2b2sk3nyv8ww-source` |
| `runtime-source` | `/nix/store/hl0gh74z1yyy30xw6wac2l319vqcawkb-source` |
| `provider-source` | `/nix/store/2y2a7df1yv9aadbb10ykwibx465wb17g-source` |

`nix-store --check-validity` and `--query --roots` confirmed every target and
registration. W/reviewer received direct readiness messages. W owns disjoint
old-native/tool roots; no duplicated retrieval. Preserve roots through remaining
verification/recovery obligations. No root/state cleanup is authorized here.

Historical vendor proofmx719 and normal vendorwhyx outputs were also collected.
The normal output is unavailable from cache.numtide; no vendor rebuild was
performed during review. Original successful fresh-proof logs/hash remain
truthful historical results, not a claim of currently readable output. No tagged
managed VM fixture binary was previously built. Root any newly materialized
required fixture/proof outputs immediately in their later authorized operation.
No native suite, version probe, activation or lifecycle action was run.

## Exact CI alternate-provider compatibility failure

Completed creation job `128895731073` in run `42534510998` fails during the
first explicit alternate-provider creation, after primary and automatic cases
succeeded. The earliest actionable log is line 5063 in
`ci-runtime-42534510998-creation.log`: native initialization `thread/resume`
returns RPC -32600, “This chat uses alternate, but your current provider is
primary. Switch to alternate to continue.” Selected-form evidence confirms
alternate/gpt-5.5/high. This is an explicit native refusal, not a browser timeout
or the incidental pattern warning.

Exact 0.167 source `app-server/src/config_manager.rs` `load_for_resume` computes
current provider before applying saved/request overrides and rejects different
saved/requested providers. Loaded resume also calls
`check_thread_model_provider_for_input`; turn/queue/goal input paths use the same
check. The 0.165 official source lacks these guards. Runtime provider resolution
supplies selected session ModelProvider but ordinarily uses the shared default
provider server; a request override alone does not satisfy the new native
current-provider rule. Architect and lead received this consequential supported
compatibility boundary; no source fix or blind retry is proposed.

Previously proposed smallest faithful check (subsequently released and executed below): exact rooted 0.167 stock
App Server in private disposable state, two synthetic provider definitions with
default primary, initialize/start alternate/resume alternate plus same-provider
primary control. Capture explicit native responses without browser/VM or model
inference. The released probe outcome is recorded below; no rerun occurred. No live provider
configuration, credentials, home, socket or authority is used.

Architect confirmation: request config/modelProvider overrides cannot change
the current-provider check; native latest-config reload excludes request
overrides. Per-cwd projection cannot preserve provider switching because resume
requires both saved and requested provider equal current. Global configuration
writes would invalidate concurrent explicit sessions. No safe fixture-only
correction is available inside this brief. Acceptance/deployment of 0.167 is
blocked pending the lead's compatibility decision. A compiled native mismatch
policy patch, routing redesign or history rewrite requires expanded design/scope
authority; none is implemented. The released minimal private no-inference diagnostic is complete with the
incomplete-control limitation recorded below; no expensive rerun is launched.

## Released no-inference provider probe: incomplete control

Lead released one bounded private stock-native diagnostic. Exact script
`/tmp/codex-r-0167-provider-probe.py` used rooted native SHA
`13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10`,
prepared-source/config identity above and private state
`/tmp/codex-0167-provider-probe-5somsz35`. Native startup/initialize and primary
and alternate thread/start succeeded, echoing selected provider and gpt-5.5/high.
However, primary resume control and each alternate resume variant (explicit
modelProvider, config-only provider, both) returned `no rollout found for thread
id ...` before reaching current-provider admission. Untouched no-inference
threads were not materialized. Therefore this diagnostic is **incomplete** for
the provider-mismatch claim, despite confirming binary identity and startup.

No synthetic HTTP request or model POST occurred. Native PID3129318 exited0;
reader/server threads joined; process-group scan found no remaining PIDs.
Elapsed1.574s. The script's result is incomplete (intended exit1); the shell
logging wrapper's final `cat` returned0, which is not a passing probe result.
Artifacts: `runtime-provider-probe/result.json`, `frames.json`, `stderr.log`;
wrapper output `/tmp/codex-r-0167-provider-probe.log`. Native delegation was
unavailable, so the short operation was directly monitored visibly.

No retry, inference, seeded/rewritten history, source change or bypass followed.
A materialized synthetic rollout or supported no-inference materialization API
is needed for a faithful resume control. That additional preparation is not
authorized by this single-run/no-history-change release. Existing exact CI
native mismatch plus native source/intentional tests remain the direct evidence
for R2; the incomplete probe adds no provider acceptance proof. Architect
received the limitation explicitly. No supported workaround is established.

Final diagnostic checkpoint accepted by lead: no additional probe or
materialization is needed. Exact CI native mismatch and intentional selected
source guard establish R2. Wrapper exit0 remains explicitly distinct from the
incomplete diagnostic result. Effects are limited to private synthetic files,
joined process/thread teardown and six explicit session GC roots. Required native
/source receipts remain the exact restored identities above; no root cleanup.
Optional diagnosis has stopped while the user decides scope.
