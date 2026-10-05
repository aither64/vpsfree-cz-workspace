# Final configuration pin review packet

## Outcome and authorization

Pin the reviewed/published API revision through channel `vpsadmin`, role
`vpsadmin`, owned input `vpsadminServices`. Preserve unrelated nodes, follows and
pins, retain the full generated changelog, and keep one coherent input update.
Read [plan](plan.md), [state](state.md), [design](design.md),
[configuration report](configuration-result.md) and [rollout](rollout.md).

User authorizes both master integrations after exact final API Specs success.
Integration CI is unawaited. Deployment and rollback execution belong to the
user. No session cleanup is authorized; leave it open.

## Final complete history and migrations

Configuration worktree `worktrees/2026-10-03-newadmin-exception/vpsfree-cz-configuration`,
branch `2026-10-03-newadmin-exception`:

- Base: `7e32833aca1cb65902b50f61eb76dd1022691591`.
- Final head: `074b62fe4ca99bcb6e0b2cd186e43f039c666b36`.
- Complete series: one generated commit, `inputs: set vpsadminServices to f9beb46e`.
- [Actual final diff](configuration-final.diff): flake.lock only, 3 additions/3 removals.

The obsolete unapplied af8 pin was dropped with the prepared guarded clean
rebase onto the unchanged baseline, then regenerated through the owning channel
for published f9. No intermediate baseline was published. The old remote
feature checkpoint dd5 remains until final review/build and publication using
an exact force-with-lease. Historical e96/dd5 review/build evidence is preserved
in records. No repeated input updates or fixup residue remain in final history.

No migrations in configuration or the full referenced API delta; no schema,
seed or persisted-format changes, transitional migrations or new versions with
release/deployment/external-use provenance to establish.

Final API head is `f9beb46e5206864bca9d37672e1419cf03661467`, base 148ef0ea.
Its complete two-commit series and all four affected lanes passed independent
review with no findings. Runtime code/specs are unchanged from af8. Full old pin
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff` to f9 contains 18 commits/18 paths:
16 supported merged dependency updates, the auth fix and the timeout policy.
The generated configuration message retains all 18 subjects in exact Git order.
No consolidation of supported merged API history is appropriate.

## Quick evidence and owner/consumers

Lead executed the member-prepared sequence in the declared cached config shell:
clean/ref guards; drop the unapplied prior pin; then
`confctl inputs channel set --commit --no-editor vpsadmin vpsadmin f9beb46e5206864bca9d37672e1419cf03661467`.
Generator exit0, Nixfmt/applicable mandatory precommit and commit-msg hooks
passed; the standard long generated-line advisory is preserved under the
explicit exception. No handwritten lock edit or hook bypass.

Recursive JSON comparison retains all 64 nodes and changes only
`vpsadminServices.locked.{rev,lastModified,narHash}`. New timestamp1791058129,
hash `sha256-Byg9MDryCoLlSmHwignOBjkafajU0rSRHSVsNGXq0ow=` and exact f9 revision.
Root mappings, follows, other pins and API target definitions are identical.
Final diff check passes; tracked tree/index are clean. Implementer independently
validates these facts and exact generated history in the linked report.

flake.nix channel mapping remains the owner. Both API1/API2 select this channel;
common API imports derive source/modules/overlay through the existing input.
Production/Staging, nixpkgs/vpsAdminOS and WebUI source pins remain unchanged.
Pinned WebUI f123a7fb's refresh/session.json/bootstrap/current-user path was
independently inspected; [trace](pinned-webui-trace.md). All follow links remain.
Other channel consumers may take the source on separate builds/deployments;
this handoff scopes API1/API2. No coordinated fleet/WebUI update is required.

Public contracts, token formats and persisted state are unchanged. Mixed workers
are compatible; old workers may still raise until replaced. Rollback loads
unchanged state and restores the defect. There are no schema conversions.

## Required checkpoint and pending verification

High overall authentication/deployment risk. Reuse independent reviewer0's
saved gpt-6.1-sol/xhigh/read_only settings, no overrides or nested reviewers.
Affected lanes: GENERAL and RISK/COMPATIBILITY. Inspect the complete final series,
actual diff/JSON/message and exact source publication. Explicitly conclude
whether obsolete history remains and whether migration lineage is sound,
including no migrations. Prior unaffected architecture/scope/channel/consumer
and runtime reviews stand; do not repeat full unchanged implementation analysis.

Fresh exact-tree API1/API2 builds are pending. Previous dd5 generation 21-30-00
is historical evidence, not proof for this head. API Specs run 37151153953 at
exact f9 is pending and alone supplies the user's CI merge gate. This review
certifies committed metadata, not derivation builds or production activation.
No tests/build/push/merge/deploy/lifecycle action is assigned to the reviewer.
