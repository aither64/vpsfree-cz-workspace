# Managed CI verification

Owner: retained `implementer2`, thread
`01a1a25e-a39b-7ad3-b5a3-d9afa94f9175`, saved
`gpt-6.1-sol/xhigh/workspace_write`, unchanged. Session identity was verified
with `dev-session current` in the tracking directory and the trusted developer
binding to `/home/aither/workspace/ai/vpsfree.cz`; both environment identity
variables were absent. Live roster and package execution access were checked.

## Scope and current disposition

Exact reviewed source: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, independently
confirmed in the feature worktree. Observe existing vpsfreecz/vpsadminos runs
`41695511680` (generic CI) and `41695651867` (image workflow) only. No new
tests, application edits, commits, merges, deployments, CI mutations, team
changes or session lifecycle actions are authorized to this package owner.

Local four-image tests, focused Ruby/Nix checks, RSpec and RuboCop are already
recorded as passed at this source. CI remains pending. The known livepatch
fixture failures retain failed/not-passed disposition; exact baseline recipe
identity and diagnosis limits are in [ci-failure-diagnosis.md](ci-failure-diagnosis.md).
No kernel/checksum fix is part of this package.

## Reporting and observer transfer

Authenticated readiness report used `report_to_lead` from this member's own
context, message ID `de35f0f2-1c26-4c6d-b9c3-a716d91b4d12`. Actual tool receipt:

```json
{"turnId":"01a1a31e-3d7a-7412-8ff5-00269633d3fe","clientUserMessageId":"de35f0f2-1c26-4c6d-b9c3-a716d91b4d12","steered":true}
```

Receipt follow-up message `9541c337-027e-4dd3-b76d-09890cba54ac` returned the
same lead turn with `steered: true`. The lead acknowledged delivery and explicitly
released the dependency: old `/root/ci_wait` ended, both observer handles
exited 130, no matching `gh run watch` remained, and no CI workflow changed.

Replacement utility policy resolves from catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
installed package `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`:
`gpt-6-luna/low`, operation lifetime, maximum concurrent 1, package
`full_access` (`danger-full-access`, approval `never`). Matching native config
is `share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`,
identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`.

The utility reports raw evidence to this active owner; it never claims a team
member reporting identity. This owner interprets the evidence and uses
authenticated `report_to_lead` for managed delivery.

Initial replacement `/root/ci_managed_watch` returned incomplete during shell
setup, before usable observation. One JSON file and one watch log were empty;
an independent exact-command process check found no matching watcher. No CI
mutation occurred. Escalation message `790ead25-6068-4caa-9968-39e4755d14f7`
returned lead turn `01a1a31e-3d7a-7412-8ff5-00269633d3fe`, `steered: true`.
The parent corrected command construction to separate native command handles
without shell background operators. Fresh `/root/ci_managed_observe` owns the
replacement observation. Both exact observers were independently verified alive
with `ps` after launch at 22:56:19/22:56:23 local time on November 3:

| Run | Native handle | PID | Full watch log |
| --- | --- | --- | --- |
| `41695511680` | `33773` | `2868129` | `ci-managed-generic-watch.log` |
| `41695651867` | `74195` | `2876309` | `ci-managed-image-watch.log` |

Both commands are `gh run watch <run> --repo vpsfreecz/vpsadminos --interval 30
--exit-status`. Launch used fresh context, explicit `gpt-6-luna/low` overrides
and inherited full access; utility also checked the matching native policy.
Initial raw JSON files `ci-managed-41695511680-initial.json` and
`ci-managed-41695651867-initial.json` were independently read to assert exact
head. They report generic suite job `126191147285` in progress, plain Intel
`126191147653` queued and image test `126192300407` queued.

Managed ownership message `e9fbc2d6-c851-4fc2-823f-2aa5d29e3b6b` returned:

```json
{"turnId":"01a1a31e-3d7a-7412-8ff5-00269633d3fe","clientUserMessageId":"e9fbc2d6-c851-4fc2-823f-2aa5d29e3b6b","steered":true}
```

This retained member stays active while the utility owns both native handles;
the owner does not duplicate its CI polling.

## Existing local evidence

[Verified image tests](verified-image-tests-result.md) records batch exit 0 at
the exact head, total 2716.16 seconds, with normal runner source lifetime and
the scoped 8 GiB resource module. CentOS Stream 9/10 passed in 1299.36/1300.69
seconds; Rocky 9/10 passed in 1391.30/1415.45 seconds. This establishes all four
local cases; it does not establish CI image selection or CI case completion.

[Duration checkpoint](ci-duration-checkpoint.md) records the generic test-step
start at 2026-11-03 20:42:44 UTC, native 350-minute bound at
2026-11-04 02:32:44 UTC, and 360-minute job bound at 02:42:40 UTC. Historical
failed-suite durations of 2h18m–4h10m do not prove a current stall or success.
Queued image/Intel jobs have no completion ETA established by these limits.

## Initial CI job inventory

The initial raw snapshot contains these generic jobs at the exact head. A run
summary status of `queued` coexists with the active suite; individual job states
are retained rather than treating the run summary as proof that all work is idle.

| Job | Name | Initial result |
| --- | --- | --- |
| `126124855016` | OS/cache build | success |
| `126191147285` | Run test suite | in progress |
| `126191147517` | Livepatch amd-low-memory-v5 | failure |
| `126191147559` | Livepatch amd-scale-aged-v6 | failure |
| `126191147584` | Livepatch amd | failure |
| `126191147641` | Livepatch amd-fresh | failure |
| `126191147643` | Livepatch amd-low-memory-v6 | failure |
| `126191147653` | Livepatch intel | queued |
| `126191147695` | Livepatch intel-representative-v5 | failure |
| `126191147777` | Livepatch amd-scale-aged-v5 | failure |
| `126191147819` | Livepatch intel-representative-v6 | failure |

Image workflow OS/cache job `126125355812` and detection job `126191399031`
passed; test job `126192300407` was queued. Detection log was captured through
the terminal job API (`gh api --allow-escape-sequences .../actions/jobs/126191399031/logs`)
at [ci-managed-job-126191399031.log](ci-managed-job-126191399031.log).
The ordinary `gh run view --job --log` interface refused while its workflow
remained active; the API needed the explicit raw escape-output flag. No test
or CI retry was performed.

Raw lines 597–600 list exactly the four changed `build.sh` files; line 613 at
20:41:42 UTC states:

```text
Detected images: centos-10-stream,centos-9-stream,rocky-10,rocky-9
```

This proves all four intended images were selected. Actual per-case CI
execution and results still need the test job log/artifact confirmation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
