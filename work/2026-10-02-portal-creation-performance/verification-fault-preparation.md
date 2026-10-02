# Corrected-provider fault continuation preparation

**Held:** the parent's subsequent old-provider `thread observe` returned
`thread not loaded` for the original root. Do not execute the prepared fault
driver or claim it. [recovery-design.md](recovery-design.md) records the required
method-specific observer evidence and conditional fresh-case alternatives.
The source hashes and earlier preparation below remain historical provenance.

Prepared only. The parent accepted the application correction in
[recovery-design.md](recovery-design.md); the implementer owns that edit. This
prototype uses the existing configured Go-helper boundary to test an old Ruby
consumer with the corrected `thread create` provider. It does not switch the
profile, change a generation token, relaunch services or bypass a package-switch
refusal. Both fault completions and the full-package live canary remain pending.

The five original measurements remain at candidate
`/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0`, runtime
`8ae46f9`: median 6.401348829269409s, maximum 6.500733852386475s. They are not
measurements of the new provider/package. The warm-up and all five successful
goal/model checks are retained, not repeated.

## Supported composition boundary

Source inspection of the old consumer and matching runtime confirms:

- `libexec/dev-session` accepts the configured portal command, and
  `create_portal_thread` builds `thread create` with the complete runtime,
  authority, cwd/socket/command, model, effort and frozen lead instructions.
  `CLI#run` still holds the shared transition lock and invokes
  `validate_host_generation!` against the original profile and token.
- `portal/cmd/workspace-portal/main.go:threadCommand` parses those public flags
  and calls `workspacecodex.Client` directly. Its `create` entry has no
  package-root, profile-token or package-generation selection. The original
  `--portal-command` argument remains the original adapter; its value and the
  resulting MCP/environment configuration are not rewritten to the new binary.
- `nix/workspace-portal.nix` installs the compiled Go command at
  `bin/workspace-portal`; Ruby is separately installed/wrapped under `libexec`.
  The retained provider was confirmed to be an ELF executable. A new provider
  must also be canonical, executable, inside a Nix store package and match the
  explicit SHA256. Its package must select the same assembled Codex launcher
  and byte-identical `share/workspace-portal/runtime-contract.json`.

This is a bounded use of the existing test adapter, not a new production
recovery interface. There is no `--from-candidate`, private lifecycle executor,
registry rewrite or substituted profile evidence. The unchanged public flags,
stdout JSON and progress frame contract still need parent source review against
the exact corrected head. Contract-file equality supplements that review; it
does not prove every CLI flag by itself.

The only new main-harness dispatch is `rootRecoveryProvider: {path, sha256}`.
It applies only to `thread create` for `2026-10-02-creation-root-loss` and
`2026-10-02-creation-member-loss`. All other commands use the original provider,
including team initialization and its existing member-progress fault. The
adapter forwards argv unchanged and records only provider path/hash and an
argv digest in the existing private event file. It does not log instructions
or credentials. The old Ruby invocation, inherited lock FDs, environment,
profile, registration, live portal, App Server and tmux remain unchanged.

## Files and exact prepared source

| File | SHA256 |
| --- | --- |
| `verify-creation.py` | `85fbcfb7823fb03215a441355a8823e7a3ed6e10b124e82d0d1c504389eacda4` |
| `verify-fault-creation.py` | `6a9ea19a49d8e61c88ca6b8e0b24085dae7fba7fdd5d7aef57d84839f25048c4` |
| `verification-fault-records.json` | `260a13f810d5ab3213ce392613ea14c694e217de43ee0df905963d5334d9a36c` |
| `test-fault-prototype.py` | `72aee4672bd13fc8ecb0e68c6b7da6cbb3bd222cff1f0fd278c4a82488c9e7be` |

The unchanged imported started/warm-up helpers remain at
`86228a7a44e44bfeb323f0df261490a901566188d64336935fb9e59550d47f57` and
`d45a474c5ef69dde3038474398bb2a4bf90e10dcb6956bdc9df6d6fbbb691b47`.
The previous reviewed main SHA
`f5abd7988804dc5502016fb3e9aedd169109e295fb9bc55f47285a7d7460145f`
remains historical provenance. Earlier preparation files and consumed claims
are retained.

`verify-creation.py` gains the finite selector and provider-dispatch evidence.
Its original post-ready acceptance tail is extracted to `complete_creation`,
called by both ordinary `create` and this root-fault retry. AST comparison
before writing proved that tail identical, and all 29 other existing functions
unchanged. Fresh main, five-sample loop, member fault, canonical goal counting,
no-tool assertion, model timeout, final receipt/roster and progress checks keep
their existing behavior.

The metadata packet pins 86 finite current noncredential records, 64 files in
the three consumed claims, 11 current directory inventories and all imported
prototype sources. This includes original result/error, attempt-2 receipt,
disarmed fault, no-root/goal-unattempted manifest, journal, configuration,
registration, preset, sample artifacts and event records. It contains hashes
and relative paths only, not credential or rollout data. Current samples and
history metadata were checked read-only: 3,379 retained seed files totaling
208,256,155 bytes, plus the 24 warm-up/sample root/member rollouts. Preflight
does not reread rollout payloads. Its successful-model evidence is the pinned
earlier result, not a new model observation.

## Read-only parent preflight and prepared command

The exact corrected candidate path and compiled binary hash are intentionally
required arguments. The parent supplies and freezes them after build and source
review. Do not execute the placeholder command. In the same aitherdev SSH,
`sudo -H -u aither`, runtime-Nix context used for prior host checks:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-fault-creation.py \
  --provider-package /nix/store/REPLACE-WITH-EXACT-REVIEWED-CORRECTED-PACKAGE \
  --provider-sha256 REPLACE-WITH-REVIEWED-COMPILED-GO-BINARY-SHA256 \
  --preflight
```

This path performs no RPC, subprocess launch, claim or write. It validates the
original process/socket proof ancestry and exact retained App Server 1687746,
tmux 1798536 and portal 1798541 identities with the unchanged shared helpers.
It checks the original profile identity, owned 0700 root, record ownership and
hashes, owned 0600 auth metadata only, exact fixture inventory, absent member
fault/claim, attempt-2 failure, unchanged preset/settings and all five timings.
It neither enumerates unrelated processes nor adds physical ancestor checks.

Immediately before execution the parent must additionally verify the exact
original root `01a0fe38-b8e0-76c1-b8f0-fd84783964a5` is still loaded, idle and
unmaterialized at its recorded cwd/source using the existing selected App Server
read interfaces. Same process plus absent rollout is not proof of live root
ownership; this metadata-only driver does not make that inference. Missing
host visibility, missing live-root evidence or any changed record requires
diagnosis before a claim. No replacement root is accepted by the fault check.

After that preflight, affected-lane independent review and parent authorization,
a fresh watcher runs the same frozen command **without `--preflight`**, once.
The fixed member-fault date must still be 2026-10-02 UTC; crossing midnight
refuses for parent diagnosis rather than selecting another slug silently.

## Exact execution and acceptance

1. Recheck records and services; exclusively create `fault-continuation/`.
   Copy and fsync the current pinned records and all three parent host proofs,
   then fsync directories before any config/result write. The original claims
   remain in place and are pinned; no auth, rollout or production history is
   copied. An interrupted claim is retained and prevents repetition.
2. Add only the finite provider field to the retained benchmark config. Keep
   its original package, Ruby args, profile/token and all other fields. The
   result retains the old candidate, warm-up, all five sample/model records and
   timings, adding separate provider identity and compatibility-test provenance.
3. POST the ordinary creation retry for receipt
   `a4ad299484ab1972eb099a9b08793976cc442dc0ce8bae6fa768bba282e37634`, expected
   attempt 2; require the same receipt/slug and accepted attempt 3. Observe normal
   ready evidence and require the exact original root. Invoke the shared final
   checks: Full roster/settings, canonical GOAL exactly once, assistant/model
   completion, no tools, detailed progress and completed stages. Require one
   actual corrected-provider dispatch for this root. Record retry latency
   separately from original acceptance-to-ready; neither enters the five timings.
4. Persist that root result, then invoke the unchanged
   `create(..., "creation-member-loss", 180, "member-progress")` once. Its original
   fault must leave at least one ready and one unfinished member, then retry the
   same receipt. Keep the same root and every earlier ready member ID, sequential
   initialization, exact-goal/model/no-tool/final-stage checks and inconclusive
   missed-boundary refusal. Require two corrected `thread create` dispatches
   (fresh call and retry); the team fault itself still uses the old provider.
5. Require both fault results and unchanged retained sample/warm-up data.
   A passing result is explicitly tagged `old-consumer/new-thread-create-provider
   faults`, with full-package canary still required. Failure preserves evidence,
   selected provider field, claim and services; it does not retry or clean up.

The driver never directly submits the GOAL. Normal runtime may submit the
previously unattempted fault root's initial goal once; no warm-up/sample goal is
submitted again. It never calls `finish_creation_samples`, creates another root
fault or repeats seeding/registration. Unknown RPCs remain runtime refusals.

## Prepared verification evidence and limits

`python3 -B test-fault-prototype.py` passed six focused in-memory groups (including
subcases): AST preservation, exact provider scope/ELF/hash, changed record and
prior-claim refusal, dropped/reordered/changed sample refusal, receipt 2→3 and
same-root/shared-tail checks, and preflight/preservation/execution/failure order.
Runtime, subprocess and write boundaries were mocked to refuse accidental use.
Local current-record/layout/history-metadata validation also passed with only
host process verification and candidate inspection explicitly mocked. It read
no credential or rollout payload and made no private write. Actual host and
corrected-package preflight are still pending.

This preparation does not establish full-package activation compatibility,
new-package latency or completed fault acceptance. Parent owns corrected-source
review, exact package/hash freeze, actual host/root preflight, independent
prototype review, watcher execution, pins, deployment and the final canary.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>
