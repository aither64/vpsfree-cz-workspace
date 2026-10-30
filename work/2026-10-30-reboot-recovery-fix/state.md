---
lifecycle: active
---

Phase: fix deployed, verified and integrated; OOMD continuation awaits approval.

- [x] Reproduce the provider-filter failure and implement the compatible fix.
- [x] Commit and publish all changes; pass quick checks and independent review.
- [x] Pass application/system builds, reboot VM and exact-head CI.
- [x] Deploy system and application; verify portal, Codex and tmux continuity.
- [x] Merge all four exact feature heads into their remote master branches.
- [x] Resume and continue HaveAPI upgrade and Linux CVE review.
- [x] Release all repository and machine claims; remove temporary merge checkouts.
- [ ] Obtain explicit archival direction for OOMD's twelve completed helpers,
      then recheck, archive only those helpers and continue OOMD normally.

The first two requested sessions both report recovery state `active` and
`executionHeld: false`. Native lead turns are positively `inProgress`:
HaveAPI `01a18f0a-c5ad-7b81-bf77-0e4ae3243e90` (started 23:00:10 UTC), Linux CVE
`01a18f0a-fbaa-7a52-b045-dd864e13e99d` (started 23:00:24 UTC), 2026-10-30.
The parent roots, team settings and saved work were preserved. Ordinary resume
restored terminals; portal Continue used the retained request IDs.

OOMD's eight retained subjects verify, but twelve completed standalone exec
helpers in its exact tracking CWD are outside the retained set. The existing
unknown-identity guard still refuses. [Exact archival proposal](oomd-helper-recovery.md)
records their IDs and read-only preflight. The async approval question is still
unanswered; no helpers or session have been archived. Do not weaken the guard.
The initiative stays active solely for this requested continuation.

## Cause and implementation

Native `thread/list` defaults to the server's model provider. Retained threads
belong to `codex-lb`; the ordinary saved query returned zero rows while
`modelProviders: []` returned the expected eight. Loaded discovery previously
masked the omission, but is empty after reboot. This was neither lost history
nor corrupt submission evidence.

codex-web exposes an optional provider filter; nil preserves the native default
and a non-nil empty slice selects all providers. dev-workspace uses all providers
for exact retained discovery while preserving root, member, project, CWD,
pagination, submission and unknown-thread checks. No native version, schema,
journal or receipt changes. Application recovery remains forward-only.

## Final revisions and integration

All source worktrees are under `worktrees/2026-10-30-reboot-recovery-fix/` and all
feature branches retain the same dated name. Each exact head was pushed over SSH
to its approved remote `master`, with fresh remote equality proof under a short
repository claim. The complete final series and diffs were rechecked against
[review](review.md); no rebase, obsolete stream, consolidation or migration remains.

| Repository | Integrated feature head |
| --- | --- |
| codex-web | d3a29bee90ef00a08816920408c596152339a637 |
| dev-workspace | f05f50eed6dbfa2794502653176f0bbbbf20f1fa |
| workspace | 1deb88301418722ed1aebeaa2bebafd9b2e007d8 |
| vpsfree-cz-configuration | f9a6996153daec9e20a3feb58e05981b5907ef7b |

User authorization: “Find the root cause and implement a fix. aitherdev can be
deployed using vpsfree-cz-configuration. Once verified, you can merge it.”
Concrete target set is the four masters above. Follow-ups explicitly authorize
continuing HaveAPI upgrade, Linux CVE review and OOMD abuse policy.

## Verification and deployment

[Quick checks](quick-checks.md) cover provider wire encoding, cold discovery,
pagination, unknown-thread rejection and the negative removal experiment.
Independent final review by `/root/final_review`, gpt-6.1-sol/xhigh, found no
issues in all four whole-branch histories. This threadless maintenance initiative
has no retained reviewer, so the installed delegated catalog fallback was used.
The generated-schema corpus does not explicitly exercise the new option; focused
wire tests and live native queries cover the unchanged selected Codex version.

[Verification results](verification-result.md): composed package, reboot VM,
aitherdev build and runtime CI 41137347714 passed. Library CI 41137125628 passed.
The VM's intermediate polling AssertionErrors and fixture model-refresh 403s
were inspected; they are not final test failures (see rollout.md).

[Executed rollout](rollout.md) records exact generations and recovery evidence.
System and persistent system profile both resolve to
`/nix/store/n1j80kcr11sj01v8l594flc7jmir048a-nixos-system-aitherdev-26.05.20261026.718f670`.
Application profile resolves to
`/nix/store/rxn2q52znanqmvjwkdilfj24yrg95jpq-dev-workspace-0.2.0` (generation 215).
System dry activation, no-reboot switch and two health checks passed with normal
auto-rollback. All five portal/router/coordinator/Codex/tmux services are active;
Codex PID 1906 and tmux PID 1917 are unchanged from before deployment.
Machine claim `2ab59c0b-617e-4b9b-b741-ef3925a063d4` was released after verified
complete deployed lineage integration. Every repository claim is also released.

## Ownership and documentation

No DEV_SESSION identity existed and `dev-session current` found no session.
This conversation created a separate threadless initiative with
`start --no-attach --no-codex`; no team was invented. Source worktrees and feature
refs remain. Only the three clean temporary merge checkouts were removed.
Unrelated shared tracking/index changes were preserved. No lifecycle cleanup is
authorized by this handoff.

Lasting behavior is documented in codex-web `docs/reference.md` and dev-workspace
`docs/workspace-portal.md`; operational evidence stays here. Reusable diagnosis:
`notes/dev-workspace/2026-10-30-retained-discovery-provider-filter.md`.
Configuration hooks ran in its Nix environment; initial checkout's ambient-gem
failure was repaired in place without bypassing hooks. The Go checks use the
runtime development shell so the C compiler is available.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-reboot-recovery-fix/
