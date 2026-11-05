# I7: existing builder deletion/reset semantics

2026-11-05, implementer0; prior packages accepted, capacity confirmed.
Session/current and both environment bindings match; unchanged workspace
guidance reused, repository AGENTS reread. Canonical bare vpsadminos source
`2951a632c4254a44747a8da326e3dde897eaa0e2`; all refs below are at that SHA.
Only this evidence file written. No commands affecting containers, runtime,
Git state or session lifecycle were executed. Recreation uses prior I4.

## Exact selector

For an idle, coordinator-owned builder in its owned single-pool worker:
`osctl-image ct del --type builder --force <CTID>`.

`osctl-image/lib/osctl/image/cli/app.rb:154-163` declares `[ctid...]`, type
`builder|test|instance`, and `--force`/`-f`. `cli/containers.rb:46-50` filters
managed CTs by exact type and exact `ct[:id]`, not builder NAME or glob.
Obtain/check the actual CTID first with `ct ls` (default fields include pool,
id/type/distribution/version, `:7-13,25`). Passing the builder name usually
matches nothing; the method has no explicit unmatched-ID error. With no ID,
`--type builder` selects **all** managed builders; with neither selector it
selects all tagged managed CTs (`:48-50,67-72`). Do not use either broad form
for a targeted reset. The deletion call does not forward the displayed pool
(`:60-61`), so this recommendation assumes the owned single-pool worker.

## Deletes and stops; does not recreate or exclude active builds

Without CLI `--force`, it lists selected CTs and asks for literal `y`
(`containers.rb:52-58`). This flag only skips that prompt: the client always
submits `ct_delete force: true, prune: false`
(`osctl-image/lib/osctl/image/osctld_client.rb:217-219`).
`osctld/lib/osctld/commands/container/delete.rb:24-39` stops the CT, uses kill
for a running forced deletion, and refuses failed recovery cleanup. It then
removes mounts/config/registration and trashes the dataset (`:49-68,115-121`);
immediate trash pruning occurs only if requested (`:108`).

There is no CLI idle check, build-owner reservation or active-user exclusion
in this path. The daemon's container manipulation block does not establish
that no image build uses the builder. Coordinator ownership/draining must
ensure no active or queued use before deletion; do not treat confirmation or
daemon locks as a safe reset protocol. Failed/uncertain cleanup is not success.

Deletion itself never recreates. Next `Builder::UseOrCreate` creates/setup
when its deterministic CTID is absent (`operations/builder/use_or_create.rb`
`:22-31`; `builder.rb:35-38`, established in I4). A present builder is reused.

## What survives and proposal limit

The command deletes the builder CT, not exported archive/cache directories,
verified results, repository payloads/index, other CTs or separately allocated
image work datasets. Their lifetime is separate (I4, `operations/image/build.rb`
`:67-83,230-268`). Successful deletion therefore preserves completed verified
outputs; no global cache purge belongs to builder reset. Distinguish diagnosed
builder corruption from ordinary image failure. If ownership/draining or
cleanup is uncertain, replace only that worker and use a bounded explicit
retry; this is a proposed coordinator contract, not existing CLI behavior.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
