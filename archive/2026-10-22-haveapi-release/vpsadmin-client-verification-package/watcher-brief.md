# Downstream verification utility — prepared, execution not yet granted

Fresh single-operation watcher, pinned gpt-6-luna/low, native identity
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, catalog digest
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`.
Use current installed full_access policy: danger-full-access, approval never.
Read actual selected runtime utility config and verify launch policy/model/effort;
never infer readiness from this brief alone. This utility is not a team member.

Read these absolute guidance paths before execution:

- `/home/aither/.codex/skills/dev-session-monitor/SKILL.md`
- `/home/aither/workspace/ai/vpsfree.cz/AGENTS.md`
- `/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/sessions.md`
- `/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/git.md`
- `/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/verification.md`
- `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client/AGENTS.md`
- `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client/README.md`
- `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client/docs/development.md`

Thread-bound session slug is `2026-10-22-haveapi-release`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Run dev-session current and confirm both
environment values either match or are absent under the parent-provided exact
binding. Tested downstream HEAD must be
`ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree
`322fa86ba290b5936a327c21371c94f96f86b249`. Read-only HaveAPI source must remain
`090a188cb4ef3477324718627f4ae3415d1c0975` in the same session's haveapi-followups
worktree. Preserve all known caches and untracked outputs.

After the parent explicitly grants this exact reviewed operation, create a new
evidence directory at
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/vpsadmin-client-verification-ff876abe`.
Do not reuse an attempted directory or remove any existing artifacts. Set
`VPSADMIN_CLIENT_VERIFICATION_EVIDENCE` to that absolute directory.

Before invoking any script, write `utility-ready.json` there using the actual
verified identity and these expected fields:

```json
{
  "ready": true,
  "agent_identity": "actual fresh utility thread or task identity",
  "session": "2026-10-22-haveapi-release",
  "workspace": "/home/aither/workspace/ai/vpsfree.cz",
  "head": "ff876abe17e3301da62c1b6afbda055ec89db9d2",
  "model": "gpt-6-luna",
  "effort": "low",
  "catalog_digest": "840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa",
  "utility_identity": "dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12",
  "execution_access": "full_access",
  "sandbox_mode": "danger-full-access",
  "approval_policy": "never"
}
```

The script parses and checks this file as a hard gate. Report utility readiness
and the exact owned command handle to parent. Then run exactly once:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/vpsadmin-client-verification-package/run.sh
```

Use the workspace root as launcher cwd. Capture full outer stdout/stderr in the
evidence directory's `batch.log` and preserve the exact exit status separately
as `batch.exit`. The utility owns the actual tool handle and monitors it. Record
UTC start/end and monotonic elapsed time in `watcher-result.json` with model,
effort, actual execution policy, command, handle, result and any active process.

This operation uses the downstream pinned Nix environment and existing isolated
Ruby3.3 bundle under target, with BUNDLE_FROZEN=true. It performs no setup/install
or writing regeneration. The evaluated downstream shell's complete derivation
graph is retained; selected tool outputs are matched to native inputs and exact
output records in that graph. Separate retained Rust1.95 roots must contain the
explicit selected MSRV outputs. Tool binary hashes, verbose identities and NAR
identities are saved. A stale producer inferred from an unrelated derivation is
not acceptable evidence. The script handles both known Nix derivation JSON
representations without guessing missing fields.

The batch runs provenance and read-only regeneration checks; development async
and blocking all-target tests; docs; generated-name deny lint; package list and
package; then independent Rust1.95 async/blocking tests and the same lint. It uses
separate ignored target directories and retains the .crate, package list,
command logs/exits, source hashes and input graphs. It checks packed generated
source matches the committed tree. No `--ignored` real_vpsadmin tests, listeners,
production requests, credentials, registry writes, release workflows or Git/index
mutations are authorized. Compilation and ordinary Cargo dependency resolution
are expected verification effects. Do not run cargo login or publish.

On the first nonzero command or guard failure, stop and report raw evidence;
do not diagnose, edit, retry, resume, relax a guard or launch extra commands.
Do not install dependencies, alter source, rewrite locks, select another toolchain,
use allow-dirty, clean caches, deploy or spawn nested agents. Unexpected Linux
kernel builds must be stopped and escalated; expected Rust/native dependency
compilation continues without an invented quiet-output timeout. An unresolved
running operation remains utility-owned until parent directs otherwise.

Return compact raw results: passed/failed/incomplete, exact head/command/handle,
exit and elapsed time, full log/result/artifact paths, failed step and bounded
error excerpt, any still-running operation. Parent owns diagnosis and acceptance.
