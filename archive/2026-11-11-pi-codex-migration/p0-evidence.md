# EXEC-P0: supported Pi worker probe

Implementer1, 2026-11-12. P0 and its bounded tagged-custom-input follow-up are
committed and quick checks pass; ready for lead acceptance. Architect0 accepted
standalone SDK workers as the production candidate after inspecting the finite
API evidence. No existing portal, libexec, flake or host configuration was edited.

## Exact source and dependency identity

- D base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- P0 commit: `ab9ce9234fe2b1f80367b7bb1836a81925b2a034`, branch
  `2026-11-11-pi-codex-migration`, canonical remote
  `git@github.com:aither64/dev-workspace.git`.
- Follow-up commit: `0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`, immediately after
  peer P2 head `063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c`. No peer history was
  amended or rewritten.
- Pi source: `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`; source store path
  `/nix/store/w03p2sl10qld4fyqdjr5w3dk1lr13lwg-source`.
- Built package: `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`.
- Deriver: `/nix/store/vv0rmmd9fh7n2p2axr127kpk8hmvgsrl-pi-1.5.2.drv`;
  output NAR hash `sha256-BLExHGk7KE4VkNPGC91H9+kTzEPyfWt/orlbfaTJP3w=`.
- SDK workers and stock RPC use the package's Node 22.23.2:
  `/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`.
  The D Nix environment's test harness/namespace fixture uses Node 24.19.0.
- Pi model catalog revision:
  `sha256-4cbd75daee429216860f6e5b7e13b4ddb12b495f6947061e5777edd27ce0b4f1`.

The fresh native watcher completed the pinned upstream Nix build successfully
in 163.4 seconds, per the lead's watcher result. No member launched a duplicate
build. [Build log](p0-pi-package-build.log) and [derivation graph](p0-pi-derivation.json)
retain the dependency evidence. Pi's own source, npm lock, installer lock and
model catalog pin were used, without patching source or installing ambient npm
dependencies. SHA-256 of the source input files:

| File | SHA-256 |
| --- | --- |
| `flake.lock` | `81a0975f37e2ad795d0980a4c06ee010391aa476aa36a4b39eff0ef5cd0f543d` |
| `package-lock.json` | `99fb5fd69694b6879de2f8b5062648f86f1001c76648db08042705517737ffd4` |
| `packages/coding-agent/install-lock/package-lock.json` | `57e3b475e52f630cf903f73b0d2a02c405875af61ce4a845f481dcc798f58005` |
| `nix/model-catalog.json` | `6b4c957eb83bdf6faac9909f259d7fac47d14fb31c1c1dd21f121d784061ad76` |

## Checks and outcomes

The final API quick check passed in 17.497 seconds using the pinned package's
Node directly while P7's separate flake/Go edit was incomplete:

```sh
env \
  PI_PROBE_PACKAGE=/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2 \
  /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node \
  --test test/pi_runtime/probe.test.mjs
```

The [final API log](p0-api-probe.log) records one passing finite fixture and no
failures, cancellations or skips. Before the tagged cases, the original
published-head check passed in 11.84 seconds:

```text
finite SDK/RPC fixture: private workers, canonical auth, history and honest Unknown
tests 1; pass 1; fail 0; cancelled 0; skipped 0
fixture duration 10149.287426 ms; process duration 11836.803902 ms
```

The [custom-message failure log](p0-custom-message-unavailable.log) preserves the
temporary dependency ENOENT between the successful batches. The final check
covers four standalone SDK workers, two fake sessions
with one lead/member pair each, private native history/settings and shared
canonical authentication. One fake expired grant refreshes once under native
locking; canonical file replacement becomes visible across processes. Manual
stream/history/provider/model/default changes and abort pass. Settings persisted
explicitly stay local to one worker. Stock RPC plus the first-party extension
also passes manual stream/history/model/abort, auth alias replacement and native
session reopening. Both use offline fake providers; no cloud credential, real
account or paid model call occurred.

SDK crash points after completed work/before reply and after tool effect/before
result preserve history without resending. Stock RPC drops the native prompt
response and reopens after process death. Native history has no transport UUID.
The ordinary-prompt checks expose Unknown outcomes; they do not establish
native deduplicated admission. The fixture does not implement a production
durable Unknown receipt
store or claim a host outbox proves Pi acceptance. Arbitrary tools gain no
exactly-once guarantee. A positive fixture refusal before the native call is the
tested NotSubmitted case. Queue/fallback/team automation remains unreleased.

The lead then requested a six-active-minute falsification of one public
composition seam: `sendCustomMessage` with custom type and immutable host
submission ID/digest in details, `triggerTurn`, and public history reads. Source
shows a precise fresh-session gap: `SessionManager._hasConversation()` at
lines 1158-1177 counts only user/assistant roles, so `_persist()` at 1180 skips
initial custom-only input. This is not a global impossibility conclusion for
existing-session tagged input. The finite follow-up tests both fresh and
established sessions at the model-call boundary, with no raw JSONL writes,
private hooks, synthetic user prelude or duplicated user input.

The exact Pi package disappeared after the original successful check; initial
follow-up attempts failed before cases executed with ENOENT for `bin/pi`.
Cause is unverified. A fresh lead-owned watcher restored the exact output in
142.717 seconds and retained it through `p0-pi-package-root`; all watcher/driver
sessions finished, per the lead's receipt. See [rooted build log](p0-pi-package-rooted-build.log).
No member duplicate build or alternate package was used.

The restored-package custom results are decisive: the fresh tag is in memory
but absent on disk at inference and process death loses it; an existing
persisted conversation has the exact tag through independent public
`SessionManager.open().getEntries()` before inference and after restart.
This is conditional native acceptance evidence, not execution completion or
fresh-session coverage. Architect0 accepted that result. Native UUID absence
alone is not an impossibility argument. The separate proposed ordinary-input
host witness was not researched or tested by this follow-up.

All eight owned files passed staged `git diff --check`; all probe `.mjs` files
passed `node --check` from D's Nix shell. No hook framework is declared in D,
`core.hooksPath` is unset, and its canonical hook directory contains no
non-sample hooks. No hooks were bypassed. Commit used a temporary message file
and `git commit -F`; the first used the repository's Nix environment, while
the follow-up used normal Git with the same unchanged hook configuration.
Follow-up Node syntax checks used the exact pinned package's Node executable.

## Rootless launch result

Exact finite command, run from D's worktree:

```sh
nix develop --command node test/pi_runtime/containment.mjs .
```

[Containment receipt](p0-containment.json) retains each generated systemd argv,
invocation ID, UID/GID maps, observed namespace/cgroup, child identities and tool
status. The owned units were:

- `pi-p0-564e74e8-fc67-4551-bd80-44874a7f6c9c.service`, mount namespace
  `4026533850`;
- `pi-p0-f26e934d-9228-413f-aeec-a9b7f27da1eb.service`, mount namespace
  `4026533852`.

Both simultaneous services returned SUCCESS. Their children inherited the exact
owning namespace and cgroup. Repository access and local Nix daemon ping worked;
daemon execution is not contained/accounted by that ping. Disk-backed `/tmp`
and `/var/tmp` markers survived exit. Restart/rebind was not tested.

The rootless launch route failed required tool semantics: supplementary host
groups `[1,100,989]` became visible as `[65534,100,65534]`, and the exact host
sudo wrapper failed its root/setuid check inside the namespace. Host baseline
reached password authentication; no password or privileged action was attempted.
Lead/architect0 accepted this as a Launch gate blocker and allocated separate H0
design. No further rootless variant or unisolated fallback was attempted.

An initial sequential comparison incorrectly compared namespace inodes after
unit exit; inode reuse invalidated that assertion. It was corrected to
simultaneous services. A first sudo observation used the Nix shell's unwrapped
binary; the final fixture uses the exact host wrapper and records its baseline.
These fixture corrections explain why earlier attempts are not launch evidence.

All API fixture children were joined, including intentionally killed workers;
owned temporary API homes were removed only afterward. Both finite systemd
commands returned; a later unit query found no `pi-p0-*` units. Collection is
not independent cgroup-empty verification. Completed scratch from the initial
failed assertion was removed by its exact known path after this reconciliation.
No tool session or command remains running or uncertain.

## Gate decision and next dependency

| Gate | Result |
| --- | --- |
| Pilot adapter APIs | Passed for fake supported SDK/RPC composition; SDK selected by architect0. Usable Pilot-ready still requires H0, production caller/authority/Unknown-hold/capability wiring and review. |
| Automation-ready | Not established for the tested ordinary prompt/RPC path. Existing tagged custom input gives conditional acceptance evidence; fresh input and complete host receipt/reconciliation remain separate gates. Do not release dependent automated dispatch based on this fixture. |
| Launch-ready | Blocked for rootless route; H0 is a separately owned dependency. |

Changed scope is exactly `pi-runtime/{README.md,upstream.json}` and six files in
`test/pi_runtime/`. P0 ranges are D base through `ab9ce923` and peer P2 head
`063c4a4b` through `0af8ac84`. The complete shared branch also includes the peer's
P2 delivery, which this P0 result does not assess. No P0 schemas, migrations,
deployed/released state, legacy
conversion, maintained Pi fork, production worker wiring or lifecycle action.
Later branch additions still require whole-branch review under the lead's
workflow. No default-branch merge or deployment was performed or authorized.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>
