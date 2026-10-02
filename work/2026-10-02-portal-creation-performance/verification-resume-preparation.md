# Seeded verification continuation preparation

Historical pre-registration preparation and review provenance. The watched
continuation using `57c28957` subsequently registered successfully, preserved
the original failure in `seeded-continuation/`, and launched the real App
Server. It stopped at the prototype's incorrect comparison of a native process
executable with the selected public shell launcher. The claim remains; this
pre-registration command must not be reused. Current correction and prepared
follow-on: [verification-started-preparation.md](verification-started-preparation.md).
No application, version, pin or settings changes were made.

Executed script SHA256 (preserved provenance):
`57c28957b019ddba36cebf2ae650c30bd1a9fcc2468be7077da4e9544c367b28`.

Earlier checked script SHA256 (retained provenance):
`d31623c6cd4ee3f0a3ae5f7de387c8727efeefecee1db303dc9151802612f481`.

The first continuation launch of that earlier script exited 1 before its claim
or any fixture write. The parent inspected `seeded-acceptance.log` and found
`cannot exclude an owned process from the private fixture`: unrelated same-UID
systemd PID 4239 and sd-pam PID 4242 had unreadable cwd. The unchanged original
`result.json` still describes the earlier registration failure; it is not the
current launch diagnostic. No continuation directory was created.

The requested direct remediation removes only the all-`/proc` same-UID scan.
The stopped sequence recorded only the seed subprocess; normal runtime launch
was not reached. The proof is absence of that exact recorded PID (including
refusal of a reused/ambiguous PID), absence of fixture Unix sockets, and the
unchanged strict inventory that excludes registration/runtime/creation records.
Unrelated process cwd permissions are outside this specific fixture boundary.
There is no general recovery, PID inference or permissions workaround.

The selected loader requires exactly `developmentClusterProviders`,
`displayLabel`, `hostLabel`, `portal`, `schema` and `sshHost`
(`dev-workspace/libexec/workspace-host:1279`). The actual retained diagnostic
has the `error:` prefix. The new fixture satisfies that contract without
relaxing the loader. The original private fixture was untouched at that
preparation checkpoint; the later authorized run applied the correction.

The continuation accepts only `/tmp/pcp-oct02-a` and candidate
`/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0`.
It checks the exact incomplete registration failure, empty results/no warm-up,
unchanged Full preset/version/settings, private ownership/auth metadata,
absent recorded seed PID, no fixture sockets/registration/runtime/creation
records, and every
persisted seed's identity/source/cwd/version/padding. The observed empty,
unlocked transition lock is retained. Before any replacement, a single-use
claim preserves the original result, registration stderr and invalid fixture.
Any repeated or interrupted continuation refuses. No recovery/reset framework
or material design deviation was required.

Focused verification at `57c28957`, before the watched continuation:

- 56 checks passed: 41 continuation guards, 9 synthetic-rollout cases, 4
  mocked main-path cases and 2 in-memory preservation/interruption cases.
  Recorded live/reused and invalid seed PIDs still refuse; private Unix sockets
  still refuse. A regression case forbids global process enumeration and cwd
  reads while supplying an unrelated unreadable-cwd condition. Strict layout,
  ownership, history/settings/identity and single-use preservation checks pass
  their existing cases. No credential reads, fixture writes, actual subprocess,
  model/history RPCs or integration activity occurred.
- AST/compile and whitespace/Markdown checks passed. Comparison against the
  retained earlier script proves that only `require_no_seeded_services` changed
  among functions/classes. Main sequencing, all other guards, durable evidence
  preservation, timing/model/progress/fault/no-tool assertions and helper
  interfaces remain unchanged. Current focused check source is
  `/tmp/portal-resume-focused.py`; the prior check source is preserved at
  `/tmp/portal-resume-focused-before-process-fix.py`.

Earlier verification at `d31623c6` (not rerun as live integration):

- AST/compile, `--help`, whitespace and Markdown checks passed.
- Read-only preflight passed against all 3,379 private rollouts: 208,256,155
  bytes, each containing the exact original 16 KiB injected padding. It took
  9.32 seconds, launched no subprocess and wrote no evidence. The original
  seed process PID is absent. Auth was inspected only through file metadata.
- 50 focused checks passed: 35 continuation guards, 9 synthetic-rollout cases,
  4 mocked main-path cases and 2 in-memory preservation/interruption cases.
  These covered wrong candidate/root/settings/auth, result/history mismatch,
  runtime/registration/prior-claim records, ownership/modes, held locks,
  live/ambiguous processes/sockets, model/tool activity, changed preset/version,
  backup-before-replacement ordering, no credential copying/reseeding, and
  repeated/interrupted claims. They wrote no filesystem fixtures and launched
  no real subprocess/model/integration activity. Focused test source remains
  outside Git; its preserved prior version is named above.
- AST comparison against the prior reviewed script showed only `main` and the
  diagnostic-log option in `run` changed among existing functions/classes.
  The common registration-through-acceptance sequence is identical. All
  helpers for seeding, no-tool detection, creation gates, model timing,
  progress, faults and process retention are unchanged.

The exact candidate store directory disappeared during earlier preparation.
The parent has now restored and privately rooted the unchanged workspace
`461bedfb` output; the host build passed. Runtime `8ae46f9`, SDK
`4c170393`, extension `4f817322` and configuration `4123d883` remain the supplied
heads. The harness refuses an absent package and accepts no substitute. Keep
the parent's GC-root link outside the exact evidence directory: unexpected
entries there are intentionally refused.

Historical command, already consumed by the watched continuation; do not repeat:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-creation.py \
  --candidate /nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0 \
  --auth-json /tmp/pcp-oct02-a/codex/auth.json \
  --evidence-root /tmp/pcp-oct02-a \
  --resume-seeded
```

The watcher must use the prepared tool environment and keep every timing,
model, progress and fault gate enabled. Failure retains all evidence and
services for parent diagnosis. This preparation performed no application
edits, model/history RPCs, integration, builds, deployment, commits or lifecycle
actions. The session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
