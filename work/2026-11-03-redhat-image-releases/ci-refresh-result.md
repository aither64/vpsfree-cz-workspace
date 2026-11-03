# Refreshed publication and CI verification

Current phase: refreshed feature published; fresh exact-head CI discovery and
observation delegated. No result at the old head is claimed at this head.

- Refreshed head: `54b4313404cea35b58ebb9df951ae75e27c44971`.
- Tree: `5c03648e084e907957b37263846bc5763abdac1f`.
- Reviewed base: `742eb30cb1a8b6766c85e915d26b0400e38244b1`, target `staging`.
- SSH repository: `git@github.com:vpsfreecz/vpsadminos.git`.
- Owner: retained `implementer2`, thread
  `01a1a25e-a39b-7ad3-b5a3-d9afa94f9175`, saved
  `gpt-6.1-sol/xhigh/workspace_write`, unchanged; package `full_access`.

Session binding/current and live same-session roster were freshly verified.
Both environment identity variables were absent; trusted developer binding to
this exact session/workspace was used. [Refresh mapping and checks](refresh-result.md)
retain the old/new ranges, six byte-identical patches and source/input limits.
Lead accepted reviewer0's refreshed four-lane no-findings/history/no-migration
conclusion before publication. No source edit was made by this package owner.

## Publication and Git authority release

Fresh `git ls-remote --refs origin` proved feature
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52` and staging `742eb30` before the
push. Both branches were fetched; local head/tree matched the reviewed refresh,
with clean worktree/index. Hook signature verification was `1`, no bypass.

Publication through the prepared `nix develop --profile .../refresh-hook-shell`
used this exact Git operation:

```sh
git push --force-with-lease=refs/heads/2026-11-03-redhat-image-releases:1a637e9eac4311adba2b08d60dfa7a17d07bcb52 origin 54b4313404cea35b58ebb9df951ae75e27c44971:refs/heads/2026-11-03-redhat-image-releases
```

Exit status 0; [full publication log](ci-refresh-publication.log). Fresh remote
proof showed feature `54b43134` and staging unchanged `742eb30`; local index
and worktree remained clean. No default-branch push or merge claim occurred.
Exclusive feature Git/index writer authority was promptly released in managed
message `1d0ed226-8585-4d69-a98b-2418c5f033ba`, receipt:

```json
{"turnId":"01a1a3bd-b39d-7263-ba7e-1b8aeb45ea90","clientUserMessageId":"1d0ed226-8585-4d69-a98b-2418c5f033ba","steered":true}
```

This owner retains only the refreshed CI package. Old watched runs were already
terminal; no superseded run cancellation was needed or performed.

## Fresh CI operation

Fresh-context operation utility `/root/ci_refresh_watch` was launched with
explicit `gpt-6-luna/low`, retaining parent settings. Current installed package:
`/nix/store/hyjxg06wbz3z7jm62338a3s3s18hn66w-dev-workspace-0.2.0`.
Pinned/installed catalog digest:
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Matching native utility config:
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`,
identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`;
execution `danger-full-access`, approval `never`, one operation, maximum one.
The utility stays outside the roster and cannot use member reporting identity.

It owns exact-head push-run discovery, conditionally launching only a missing
qualifying workflow, then native 30-second watches and raw evidence collection.
An automatic image run qualifies if actual detector evidence covers all four
Red Hat cases; additional openSUSE cases are preserved separately. A pending
detector is not grounds for duplicate dispatch. No CI retry/cancellation,
source edit, diagnosis, merge, deployment or lifecycle action is assigned.
Automatic push runs were discovered and independently asserted to match exact
head `54b43134` from their raw JSON. No workflow was dispatched.

| Workflow | Run | Native handle | PID | Initial state |
| --- | --- | --- | --- | --- |
| Generic CI | `41741634771` | `7050` | `913471` | OS/cache job `126284299199` queued |
| Images | `41741634791` | `79291` | `913599` | OS/cache job `126284298737` queued |

Both process commands were independently verified: `gh run watch <run> --repo
vpsfreecz/vpsadminos --interval 30 --exit-status`. Complete logs are
`ci-refresh-41741634771-watch.log` and `ci-refresh-41741634791-watch.log`.
Raw discovery is `ci-refresh-runs-initial.json`; each full run snapshot is
`ci-refresh-<run>-initial.json`. Detector selection/results remain pending.
Automatic RSpec run `41741634539` was running and RuboCop `41741634674`
already passed at this head in the discovery snapshot; no unsupported dispatch
was needed. Final evidence is still required for pending jobs.

Managed readiness message `a584d4ea-a31e-461c-980a-3b9e8908e31d` returned:

```json
{"turnId":"01a1a3bd-b39d-7263-ba7e-1b8aeb45ea90","clientUserMessageId":"a584d4ea-a31e-461c-980a-3b9e8908e31d","steered":true}
```

Old [CI evidence](ci-managed-result.md) remains scoped to `1a637e9e`: core
109 passes and four native 24 GiB image passes. Fresh full generic-suite and
four-case native image results are required here. Old RSpec/RuboCop successes
also remain old-head evidence; current Overcommit/Nixfmt/RuboCop passed in the
reviewed refresh package. No unsupported workflow dispatch is invented.

Known nine livepatch fixture failures retain failed/not-passed disposition:
same `vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`
as [baseline diagnosis](ci-failure-diagnosis.md). Actual candidate checksum/read
failure is still unobserved; no kernel/fixture/hash repair is in scope.

The owner remains active for utility outcomes and sends substantive results
through its own authenticated `report_to_lead`. Lead owns verification
acceptance and the standing approved staging integration. Session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
