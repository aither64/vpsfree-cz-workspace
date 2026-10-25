# Exact-head feature CI preparation — disabled

Assignment a99c205e. Session binding and live roster34 verified; implementer3
retains Sol/xhigh/workspace_write. This is a command package, not execution.
All gates in `execution.disabled.json` are false and all future IDs are unset.
No source, Git, ref, network, native, cache or CI command was run for this prep.
The original e370 source and original review remain untouched. Remediation
9eec3256 must finish after reviewer0's terminal yield; preserve this preparation
and bind a fresh execution record to the resulting accepted head/tree.

## Parent push, after accepted review and concrete lead execution grant

Use the SDK's unchanged `nix develop --command git` and Python tools. Record
full argv/cwd/exit/stdout/stderr and UTC times in a new session evidence directory.
Verify binding, exact accepted HEAD/tree/branch, canonical bare/common directory,
SSH origin, empty index, clean tracked files and no nonignored untracked files.
Compare the new accepted source receipt and unchanged schema, generator.toml,
Cargo.toml, flake.lock and existing ignored local Cargo lock hashes. No HaveAPI
replay, setup or cache mutation is needed for pushing or reading provider data.

From the exact SDK root, future normal commands are:

```sh
nix develop --command git fetch --no-tags origin refs/heads/main:refs/remotes/origin/main
nix develop --command git ls-remote --symref origin HEAD refs/heads/main refs/heads/2026-10-24-vpsadmin-rust-client-0.1.0
# Assert remote HEAD is main at accepted base ff876abe and the new feature is absent.
# Any drift or preexisting feature ref stops for diagnosis, with effects recorded.
nix develop --command git push --porcelain origin HEAD:refs/heads/2026-10-24-vpsadmin-rust-client-0.1.0
nix develop --command git ls-remote origin refs/heads/2026-10-24-vpsadmin-rust-client-0.1.0
```

Require the post-push feature ref to equal the exact accepted final head. No force,
rebase, main push, tag, dispatch or repository claim is part of this operation.
If the push outcome is uncertain, reconcile that exact ref before any further
operation; do not retry automatically.

## One fresh observer operation

Fresh native watcher: gpt-6-luna/low, explicit `--sandbox danger-full-access
--ask-for-approval never`, matching native utility identity and retained catalog.
Parent remains Sol/xhigh. Use a NEW evidence directory and fresh context; verify
actual persisted turn_context model/effort/sandbox/approval before opening a
hash-bound payload gate. No readiness/thread/run identity exists yet.

Use the existing provider client, whose last retained path is
`/nix/store/skimcry4q6bcafjf4mc2g0gcyd7im0ij-gh-2.102.0/bin/gh`, without inspecting
credentials. Check its actual availability/identity at execution, never install
or silently substitute it in this prep. Native source tools stay SDK-owned.
The observer alone discovers/polls the automatic push run. Official GETs are:

```text
repos/vpsfreecz/vpsadmin-rust-client/actions/workflows/ci.yml/runs?branch=2026-10-24-vpsadmin-rust-client-0.1.0&event=push&head_sha=FINAL_HEAD&per_page=100
repos/vpsfreecz/vpsadmin-rust-client/actions/runs/RUN_ID
repos/vpsfreecz/vpsadmin-rust-client/actions/runs/RUN_ID/attempts/1/jobs?per_page=100
repos/vpsfreecz/vpsadmin-rust-client/actions/runs/RUN_ID/attempts/1/logs
repos/vpsfreecz/vpsadmin-rust-client/actions/runs/RUN_ID/artifacts?per_page=100
repos/vpsfreecz/vpsadmin-rust-client/actions/artifacts/ARTIFACT_ID/zip
```

Invoke `gh api ENDPOINT`; paginate JSON lists with `--paginate --slurp`. Bind
exact repository, final head, branch, push event, ci.yml path/workflow ID and
attempt1; discovery requires exactly one matching new run. Never select a moving
latest run. Poll at interruptible 45-second boundaries with bounded output.
No generic silence timeout. On first actual failed job/run, retain available
raw failed-job logs/status and list any still-active remote jobs, then return
for parent diagnosis. No retry/rerun/cancel/dispatch/source repair by the utility.

On success require the exact expected jobs: dependencies, client(async),
client(blocking), msrv and regeneration. Check actual job/step names against the
accepted final workflow, allowing only its intended conditional package skip in
async. Retain full original attempt logs ZIP and complete jobs/status JSON.
Do not invent provider step outputs, actual tool paths or aggregate test counts.
Provider omissions are recorded as UNKNOWN, not inferred from success.

## Bounded artifact preservation and local inspection

Download only the original, nonexpired artifacts named
`cargo-lock-RUN_ID-1` and `verified-package-RUN_ID-1`, by exact IDs from that run's
artifact listing. Require one of each. Preserve API metadata, original ZIP,
local SHA-256 and byte size, provider digest when supplied. Compare a supplied
provider SHA-256 to original downloaded bytes; if absent, label it UNKNOWN.
No registry request, installation, execution of archives or replacement output.

Use Python stdlib `zipfile`/`tarfile`, not broad extraction. Before reading members
reject absolute/parent/backslash/NUL names, duplicates, symlinks, special members
and unexpected shapes. Bound the two artifact archives to 64MiB compressed and
256MiB expanded/5000 members; the expected lock/package are much smaller. Write
retained regular files only into a NEW evidence subdirectory with exclusive
creation. Stop with original bytes retained on a mismatch or limit violation.

For the lock artifact, require exactly Cargo.lock + identity.json. Verify raw
lock SHA equals JSON lock_sha256 and exact final head/run/attempt identity.
Bind its artifact ID, ZIP digest, raw lock digest and job ownership; no API job
output field is assumed. Preserve both files.

For verified-package, require exactly the native `.crate` and package-list.txt
in the actual upload layout (currently package/vpsadmin-client-0.1.0.crate and
package-list.txt under their common target ancestor). Check list membership
against the native archive inventory. Inspect original archive bytes without
executing them: name/version0.1.0, normalized and original Cargo manifests,
no HaveAPI/path/Git dependencies, Cargo.lock presence, VCS exact final head/root
path and absent/false dirty flag; compare all packaged Rust sources to accepted
source and record eight runtime hashes. Retain packaged Cargo.toml,
Cargo.toml.orig, Cargo.lock and VCS hashes, archive SHA/size, and artifact ID.
The packaged Cargo lock can be normalized by native Cargo: record its actual
hash separately from the shared CI input; do not demand invented byte equality.

These are feature-CI verification artifacts, not dry-run or actual publication
archives. Release workflow later runs its own required verification/resolution;
never substitute this feature lock/artifact for that separate run. No real-server
campaign is needed while the saved schema and all Rust/runtime bytes remain equal.

Return one compact terminal report with exact run/attempt/head, phase results,
logs/artifact identities and any active remote/local ownership. Parent assesses
coverage/UNKNOWNs and owns diagnosis. Source fixes follow the accepted narrow
review route. No publication, settings, credentials, tag or main effects here.

The future launcher uses this exact policy shape, with only a new evidence path
and final bound brief supplied after the lead grant (not executable now):

```text
/run/current-system/sw/bin/codex --ask-for-approval never --sandbox danger-full-access -c model_reasoning_effort="low" -c developer_instructions="Run only the assigned verification operation, retain its result, and do not edit application source, diagnose failures, retry, approve, or deploy." exec --model gpt-6-luna --cd /home/aither/workspace/ai/vpsfree.cz --json --output-last-message NEW_EVIDENCE/watcher-final.md -
```

Retained catalog: `/nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`,
file SHA4355a431ee50c57b3d9c4c7163c44b9e65397b9e8dd845f0e1c9f07366401a23,
utility model/effort gpt-6-luna/low/max1; selected installed execution_access is
full_access. Matching native TOML is `agent-teams/utilities/verification_watcher-low.toml`
under that same share directory, SHA05bb61262da9020ca471cb0b345240a44e4a452dab4877d685075c7e960b49d9.
These are policy facts, not a claim of future actual watcher readiness.
