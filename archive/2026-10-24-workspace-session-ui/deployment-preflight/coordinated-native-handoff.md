# Coordinated native0.164 evidence preparation

Implementer2's bounded execution package under the final design's **Frozen
Codex0.164 compatibility amendment / New-native activation and recovery**.
Session/environment identity was verified. No live capture, candidate helper,
build, claim, activation, model/provider request or lifecycle action ran.

All historical scripts/captures remain unchanged. The previous checker
`compare.py` still hashes to
`303a4ef53f1bfaa8a9a62afc209bc1528fdf906c2949267e0c265238dffb0aec`,
and its preserved original remains
`75bea2e2c35f3bfc3ba9233a985157e49a48d1a309ac7c41299d4cf104616b35`.
Their same-native/PID success condition is not reused for this native upgrade.

## Explicit mode and evidence boundaries

New `coordinated_native.py` accepts only explicit `prepare-native-change` or
`post-native-change` modes. Preparation reports **native change / idle transition
required**, with `idle_verified: false` and `activation_authorized: false`.
It cannot claim a machine, establish idle state, stop a service or select a package.
The ordinary workspace-host switch owns idleness, shared-home/workspace admission,
ownership, package-transition refusal and forward recovery. This script reads no
foreign session state and invents no private idle proof.

The preparation compares the complete selected and candidate runtime/state JSON
with type preservation, including unknown fields; explicitly retains SQLite
schema/policy1 and archive3; preserves exact claim/repository/coordination/
integration contracts; and binds these frozen native identities:

- Codex0.164.0, llm-agents `ea188d2f072e0ec8d5b71245e228803672801a22`.
- Source `6aaac694803004a63c6f393d153c96d22521a6b9`, NAR
  `sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=`.
- Native SHA-256
  `d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`,
  previously realized by the parent's exact prerequisite at
  `/nix/store/16f481b2zzvyvr2ycw51sm51b3f0508f-codex-0.164.0`.

Final assembled application/system paths are pending. The script checks both
materialized native hashes and manifests, system public command and codex-ds
wrapper alignment, fresh candidate public registration and provider startup argv,
actual capacity0/reporting1/policy1 and retained registration-state identities.
It binds an exact expected new marker and complete new daemon argv. It does not
turn the old0.163 executable mismatch into equality or require later selected
state capabilities to exist in the historical launcher.

`coordinated-native-approval.example.json` is an intentionally unusable template,
not a new approval authority. The parent fills a fresh reviewed identity record
from final build/source/patch/graph receipts after the review/build gate. Supply
the exact candidate/system/native paths, runtime/configuration heads, approved
provider argv and codex-ds wrapper hash. Evidence paths must reference this
session's records or immutable store artifacts, with exact hashes. Source/patch
and full graph meaning remains the combined review's responsibility; the script
binds those reviewed bytes and verifies the actual source NAR/native hash rather
than regenerating builds or graphs. Preserve daemon-nix-store.patch and evidence
that conditional webpki-bump.patch is not applied. Ordinary extension/catalog/
machine/cluster/provider transition checks and final cross-consumer/source review
remain required; this native evidence mode does not replace them.

Raw approved identities, complete before capture, selected/launch/candidate
contracts, manifests, registration and startup facts are saved to a fresh `-raw.json`
sidecar before semantic assertions. The old immutable marker remains in that
record. Do not overwrite a failed receipt or use oldnz0/old9293 candidates.

## Pure quick checks

Command: `python3 -B coordinated_native_checks.py`. Six synthetic helper tests
with table variants passed, exit0 (see `coordinated-native-quick-checks.log`).
No real candidate or native helper is called by these tests.

Positive cases classify the upgrade as requiring an idle transition, bind a new
marker/startup, and accept a new process with exact approved identity, system/
wrapper alignment and retained conversations. Negative cases reject capability
loss/unknown differences, claim-contract changes, wrong binary/source/native
input, mixed0.163 manifest, same-native baseline, startup policy/capacity/provider/
reporting authority changes, wrapper mismatch, unchanged process identity,
wrong new marker/executable/argv and changed conversation identity.

The first synthetic positive post fixture retained old served-asset hashes and
failed. Only that fixture was corrected to describe the new served assets; the
production asset check was preserved. Python syntax and both historical checker
hashes passed. `coordinated-native.diff` and `coordinated-native-sha256.json`
provide the full new-file diff and hashes for combined independent review.

## Future watcher recipe, prepared only

After parent exact reviewed/built output signal, fill and review a new identity
record `coordinated-native-approved.json`. Both exact final system and application
must be rooted/copied/prepared before any shared-home idle cutover. This script
has no build or activation command. Parent launches a fresh verification watcher
for these uncertain-duration bounded reads, using unused receipt names:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/capture.py \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-native0164.json
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/coordinated_native.py \
  prepare-native-change /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/native0164-prepared.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/coordinated-native-approved.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-native0164.json
```

The result cannot authorize activation. Lead must obtain its own physical-machine
claim and ordinary idle cutover for every affected workspace, recheck after waits,
then use supported system dry-activation/switch and workspace profile switch.
Do not create a deliberate shared-home0.164/0.163 writer window, force a restart,
switch providers, bypass refusal or examine another session to manufacture idle.

After the parent reports supported activation complete, capture a fresh
`post-native0164.json` with the unchanged capture script and run:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/coordinated_native.py \
  post-native-change /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/native0164-post.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/coordinated-native-approved.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-native0164.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/native0164-prepared.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/post-native0164.json
```

Post proof requires new daemon PID/start identity (not a same-PID claim), exact
approved executable/hash/full argv and new marker/inventory, selected profile and
system publication/input heads, live public command and wrapper alignment,
retained roster/settings, authenticated health/aliases/thread identities, exact
served assets and new naming process/socket readiness. Actual naming inference,
terminal/provider functional agreement and the four interactive UI behaviors need
the separately assigned exact-binary canary/browser/operator evidence. A CLI
version or HTTP200 alone is not comprehensive native or UI acceptance.

If system succeeds but profile refuses or is uncertain, retain ownership and
reconcile the original command effects through ordinary forward recovery. Do not
run new system tools against the shared home as a partial-cutover probe. Preserve
state, WAL/journals, old/new roots and original0.163 provenance. Downgrade support
is not asserted. Lead owns reconnection, integrated-lineage proof and release.

This package is frozen after handoff pending combined review/results. No final
candidate/new-native preflight or rollout has been executed by implementer2.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
