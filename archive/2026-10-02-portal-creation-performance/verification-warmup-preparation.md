# Completed warm-up continuation preparation

Prepared for parent inspection, affected-lane independent review and one fresh
watcher run. All five measured samples and both fault cases remain pending.
The retained warm-up is not a sample. This preparation performed no integration,
model/history RPC, runtime launch, private fixture write, claim or cleanup.

Exact SHA256:

- `verify-creation.py`:
  `f5abd7988804dc5502016fb3e9aedd169109e295fb9bc55f47285a7d7460145f`
- `verify-warmup-creation.py`:
  `d45a474c5ef69dde3038474398bb2a4bf90e10dcb6956bdc9df6d6fbbb691b47`
- Shared `verify-started-creation.py` identity helpers:
  `86228a7a44e44bfeb323f0df261490a901566188d64336935fb9e59550d47f57`

## Diagnosed failure and selected contract

The parent's watched run passed the earlier process/socket proof, claimed
`started-continuation/`, launched tmux/portal and created only the Full-team
warm-up. Its ready artifact records **7.230879068 seconds**, ready at
`2026-10-02T19:17:01.9965352Z`, root
`01a0fe0c-52c2-76e1-98bf-f11e1455623a` and the exact three retained members.
The parent observed first assistant output at `19:17:06.347Z`, completion at
`19:17:06.396Z`, one started/completed turn and no tool activity. The result
remains incomplete, with zero samples and no `warmup` entry, because the old
counter expected `event_msg.user_message` and found zero.

Selected [Codex 0.160 ResponseItem and content metadata](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/protocol/src/models.rs#L890-L966)
persist canonical message content with aligned `content_item_kinds`. Metadata-only
inspection of this fixture confirmed a context item classified
`agents_md.instructions` / `environments.environment_context`, then a separate
`user.text` part containing the exact 186-character GOAL. The selected
[AGENTS context source](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/core/src/context/user_instructions.rs)
identifies that context classification and its enclosing markers.

`initial_goal_parts` counts canonical `user.text` parts only, requires exact
GOAL equality and rejects unknown/missing/misaligned classifications or non-text
input. Only the two known context classifications with their full enclosing
markers are accepted as context. A `user_message` event, if present, must echo
the exact GOAL but does not increment the count. Completion still requires
exactly one canonical GOAL, an assistant response and `task_complete`. The
selected call/output suffix guard and timeout are unchanged. There is no
fallback to event-only counting, permissive `>=1` count or arbitrary user text.

## Exact continuation boundary

`verify-warmup-creation.py` is a separate one-use driver for `/tmp/pcp-oct02-a`
and candidate
`/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0` only.
It accepts the exact counter failure with zero samples/no recorded warm-up and
preserves the original seeded and started claims. No generic resume CLI,
registration, seeding, runtime restart or warm-up goal submission is added.

The parent's owned mode-0600 metadata proof is
`/home/aither/.local/state/dev-workspaces/verification/2026-10-02-portal-creation-performance/benchmark-warmup-proof.json`,
SHA256 `42c582ce94c42d27454cd65ae11094b822a657ffc8acac9ca0f39566a9ae36a9`.
It pins the original process/alias proof hashes, candidate/config/result/preset,
three recorded processes, registry/registration/inventory, ready artifact,
receipt, roster and portal manifest. All three proof files remain unchanged.

The driver verifies only recorded App Server 1687746, tmux 1798536 and portal
1798541 against boot/start/executable/cwd/command digests, and the three exact
socket identities. It reuses the original App Server alias/target/listener
checks. No global process scan or inferred ownership is used. Exact private
root/profile/auth metadata, layouts, original claims and nonsecret record
hashes must match. Other session/creation evidence or a prior
`warmup-continuation/` refuses. Credentials are checked by metadata only.

The first parent read-only preflight of this new driver refused before claim
because normal CLI resume had added `tui.screen_reader_detection_done = true`
to private `codex/config.toml`. Inspection confirmed the only top-level keys
are `cli_auth_credentials_store = "file"` and `tui`. The driver now pins the
exact current hash
`5e6aaa3ba5d51ab835aa9803bf04706bd55f1e6d53e6410d659bf6053e8a0b75`;
the preserved original config remains pinned at
`4a6d91cf2bed4ef5ac8ed28723e0074689259534722f855cbb8f690fa7ed069a`.
No configuration was edited and no broader hash exception was added. That
refused driver was `432e88e3d0f96d407e0e62e7b6494ff41a6630e7f4af272fdbe3594421e08841`.

The parent's next read-only preflight reached the inherited listener guard and
refused because it counted all same-path `/proc/net/unix` rows. Normal connected
portal/terminal clients add accepted stream rows (flags `00000000`, type `0001`,
state `03`) beside the original listener. The shared helper now selects only
the recorded kernel inode 355192150, still requiring FD 30 and exactly one row
with flags `00010000`, type `0001`, state `01` and the exact resolved path.
Duplicate recorded-inode rows, wrong FD/kernel/path/flags/state or a missing
listener refuse. Original process/alias proofs and target identity are unchanged.
Only this row selection changed from shared-driver SHA
`721de6f01de6762bc639d4b09275c8dac96f5c9c0e8b7906d6ed651167f9022c`.

The third parent preflight passed those guards and found that normal warm-up
creation had allocated its worktree group and creation journal. Driver
`b512c7d82276ae328801ff58d9bd0ce4d84bf64dbe416b46822c6c70c24697a9`
incorrectly still required an empty `workspace/worktrees`. Metadata inspection
confirmed the exact owned mode-0700 empty group `2026-10-02-creation-warmup`
and owned mode-0700 `.locks` directory. Its only entry is the owned mode-0600
regular 4,163-byte `2026-10-02-creation-warmup.creation.json`, SHA256
`da2324cab28eae16f6bd97af531c91f8b3cbd5523195f8490247f112538d7e51`.
The driver now requires those exact contents and pins/preserves that journal
with the other noncredential records. Other groups or lock/group contents
refuse. No journal plaintext was output; no private record was changed.

Before any claim, the retained warm-up passes `ready_evidence`, exact saved
root/member/receipt/timing identities, corrected `wait_model` and shared
`progress_evidence`. The original 3,379 seed rollouts/208,256,155 bytes/16 KiB
padding remain required, with exactly the warm-up's four thread rollouts added.
No model request is sent to recompute this evidence. Process and record checks
repeat immediately before the new exclusive claim.

`warmup-continuation/` is never cleared or reused. It preserves and fsyncs the
current failure, ready artifact, pinned records/events and all three proofs
before replacing `result.json`. Existing claims/logs/history remain untouched.
A partial claim or later failure retains all evidence/services and requires
parent diagnosis; there is no reset, retry or cleanup path.

## Shared gates and focused checks

`finish_creation_samples` owns the unchanged five sequential measured creations,
all-sample median <10 seconds and maximum <15 seconds, both original helper
faults, representative-history gate and final result handling. Fresh setup
calls it after its warm-up; this driver calls it after validating the retained
warm-up. `progress_evidence` extracts the existing stage/phase checks so both
paths use identical validation. No timing sample is discarded or replaced.

81 focused checks passed in `/tmp/portal-warmup-focused.py`:

- 25 model cases: canonical exact-one goal, absent/duplicate/changed goal,
  context classifications, event echo, unsupported input and all selected
  call/output variants, missing assistant/completion and timeout.
- 4 progress and 13 retained warm-up cases: required stages/member completion,
  visible detailed phase, exact receipt/roster/timing identity and model failure.
- 14 process/socket and 12 record/layout cases, including the exact current/
  preserved configuration pair, changed-setting refusals and the retained
  worktree/journal layout. Other group, group-content or lock-content entries
  and changed journal bytes refuse.
- 5 driver-ordering and 2 preservation/interruption cases: no runtime restart,
  warm-up resubmission or write before validation/claim; claims stay single-use.
- 3 sample-tail cases: all five values and both faults remain; maximum 15 or
  median 10 yields incomplete. These are synthetic values, not performance data.
- 3 AST checks: the five-sample/fault tail is identical, progress checks are
  identical after the local variable extraction, and only `wait_model`, `create`
  and `finish_creation_verification` changed among existing main helpers.

An additional 44 checks passed in `/tmp/portal-listener-focused.py`: 8 selected
manifest cases and 36 original process/alias/listener cases, including one
recorded LISTEN row plus two ordinary accepted stream rows. All replaced
alias/target, foreign owner, changed process, FD and listener refusals remain.
The warm-up suite passed again against the corrected shared helper and exact
retained worktree layout.

All runtime observations in these checks were mocked. No real subprocess,
model/history RPC or private write occurred. Tests read the parent metadata
proofs, never auth. Preparation also inspected noncredential TOML and rollout
structure/classification metadata without printing prompt or assistant content.
AST/compile and whitespace checks passed. Main's prior hash was
`4a483d39a5a5d9b93bbbf9f2eef0a901cef749ca1a0e10ad6e9de3aefe846605`;
earlier review/preflight provenance remains in
[verification-started-preparation.md](verification-started-preparation.md).

## Prepared command

After parent actual read-only preflight and affected-lane independent review,
use one fresh operation-only watcher in the parent's actual aitherdev SSH,
`sudo -H -u aither`, runtime Nix environment:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-warmup-creation.py
```

Do not rerun either earlier continuation. The parent owns host observation,
review, execution and acceptance. Warm-up readiness and focused checks do not
establish the five-sample performance gate or successful fault recovery.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
