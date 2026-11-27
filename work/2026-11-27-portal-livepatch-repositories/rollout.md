# Aitherdev rollout completed

System activation, application activation, live acceptance and all three approved
master integrations completed on 2026-11-27. No reboot or native Codex restart
occurred. All claims are released. The session was not archived or deleted.

## Exact delivered composition

- Runtime: `066691a37851742bbc47179c32b0077b0b0a016f`.
- Preserved deployed extension: `39470c642bace7a09d25194aea30100575c5efe2`.
- Configuration: `0a2ed34c91c7019e89d6d04195f9da31677b1fc4`.
- Workspace source deployed: `56b9e263dffd4e2591be41be0a7b97af68b734da`.
- Workspace final merged head: `71c5e5fcfdfb9bb1b1fbc38e5a6a17643e77379d`.

The deployed workspace range `db6ea35f2..56b9e263d` and final range
`eaa302627..71c5e5fcf` have identical ordered patches (`git range-diff`: two `=`
entries). The new baseline contains unrelated tracking commits. The application
derivation stayed exactly
`/nix/store/mm10c4a31w437j7ixi55xw6v104fkyy8-dev-workspace-0.2.0.drv`.
Build evidence therefore applies to the final composition. The old deployed SHA
is not literally an ancestor of master; its patch-equivalent successor is merged.

Live system and system profile:
`/nix/store/favk592yk1n5fr3v6ihsr2qsi9p7qxgq-nixos-system-aitherdev-26.05.20261122.0dc498b`.
Selected application:
`/nix/store/0b87p0xy0acfs2kn7m20isa196my848p-dev-workspace-0.2.0`.
Passing composition outputs:
`/nix/store/iclrcrlc25b0rcjqx6fpgjj8n0wyzxm5-dev-workspace-deployment-contract-tests`
and
`/nix/store/47yfwqpghdy4h0ldglafj8zgszv9qmy3-workspace-cluster-provider-composition-tests`.

## Activation and recovery evidence

Builds and independent review finished before activation. The configuration's
existing provider/Pi operations guides, installed coordination guides and site
machine-retention policy applied; the formerly referenced
workspace-coordination-aitherdev.md does not exist in current configuration.

A prior settled deployment reservation was released through supported CLI under
transition exclusion, preserving its original evidence. This was necessary
administrative recovery under standing site authority; its sensitive source
material remains only in ignored local evidence. Our exact schema-2 aitherdev
claim was verified against configuration `0a2ed34c`.

Dry activation reported dbus-broker reload and Home Manager restart. The command
`confctl deploy --yes --no-reboot --generation 2026-11-27--16-43-19
cz.vpsfree/machines/aitherdev switch` completed with exit 0 and both systemd and
firewall health checks passing, retaining confctl's auto-rollback protection.

System activation initially waited for user default.target: reconciliation wanted
the exclusive transition lock while housekeeping readers held it. Temporarily
stopping auto-archive/reconcile timers, services/path and coordinator allowed the
ordinary activation to finish. Application activation restored the recurring
units. No GC or native session was stopped.

The first two application switches refused before profile selection due to an
archived Pi session's incomplete earlier administrative recovery. Its retained
journal referenced an unloaded, unpersisted mapping that had been moved aside;
the archive capture also omitted that mapping's exact identity fields. Under
exclusive transition/session/team/runtime locks, restored the original mapping
byte-for-byte and reconciled only Conversation, Settings, HistoryRef and Generation
from retained evidence. Preserved archived status, reservations, stop/drain proof,
original lifecycle backup and conflict journal. No worker or input was replayed,
and no completion or integration proof was fabricated. Both Go preflight and the
installed Ruby compatibility reader then passed. Restricted recovery details and
hash receipts remain local beside the original recovery evidence.

The third ordinary profile switch selected the exact tested candidate and exited
0. Fresh observers accounted for all activation sessions. Portal healthz returned
200. Codex PID `3338117` was unchanged; portal PID `2039996`, router `2039883` and
coordinator `2040003` were active. Verified actual units
workspace-codex@vpsfree-cz.service and workspace-portal@vpsfree-cz.service.
Auto-archive timer and reconcile timer/path were restored and active.

No unfinished mutation or recovery remained. Claim
`19a7b50b-01f4-4719-8e5b-e05fd0b80906` was released at 2026-11-27T16:26:01Z
under site policy, before outstanding UI acceptance and integration.

## Live acceptance and integration

Applied all 13 exact ancestor bases through `dev-session worktree review-base`.
The resumable script checked registration, branch, head and ancestry and recorded
previous values. One concurrent session-lock refusal succeeded on retry. Source
refs, lifecycle manifests and old durable comparisons were unchanged. See
[review-bases.md](review-bases.md) and local review-base-application.json.

The browser exercised the deployed frontend/API through the portal Unix socket,
forwarding GETs and blocking mutations. Old saved pair remained identical. Core
history showed 13 commits and 9 files; refresh, branch comparison, rendered source,
individual commit and saved-URL reopening passed. A vpsAdminOS card loaded
independently. Final browser process exited 0 with no page errors. Initial harness
failures were its default five-second assertion and obsolete Monaco selector;
corrected checks assert the actual CodeMirror source content. Screenshots and
live-browser-report.json remain disposable local evidence.

Each repository was integrated with a fresh short claim, unchanged target check,
ordinary fast-forward merge, normal SSH push and exact remote equality proof.
Configuration's Overcommit hooks remained active inside its Nix shell. Shared
workspace integration also held the tracking lock and preserved all unrelated
working-tree changes. Claims were released immediately after proof; temporary
merge checkouts were then removed. See [state.md](state.md) for final SHAs.

Recovery remains forward through the supported workspace-host transition command;
do not erase journals or blindly select an older profile. Clearing an explicit
review base restores automatic comparison without modifying Git history. No
software rollback or base clearing was needed in this rollout.
