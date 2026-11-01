# React HaveAPI 0.32.0 — committed final review packet

User approved the finish plan; lead released E3's complete React package.
Scope: adopt the actual published JS0.32.0 archive, preserve the adapter unless
compatibility requires a correction, and consolidate the dependency stream.
Authority: design.md finish-plan React section6560 and finish-plan.md.
No SDK/generator, new security campaign, unrelated audit fix, live login,
deployment, PR rewrite, registry change or default integration.

## Exact source and complete history

Repository: `repos/vpsadmin-webui.git`, canonical SSH vpsfreecz/vpsadmin-webui.
Only active review alias `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-031`,
registered branch `dev/vpsadmin-haveapi-031`.

- Fresh base: `40653dffed4561dd6086716fd506a7223d3631d7`.
- Final dependency: `2ee0167a46f6a6d8d0c25e7f6c5632e517e275a0`.
- Final adapter/head: `163ad4e09a1b77f788e65a8345d69c74c8475723`.
- Final tree: `3f41d39d0d21c2c7231a4b62ce14662f7765ceb4`.
- Prior reviewed/published candidate: `02e58932cef3b667ff68401ff93e4e43bc2a3ce5`.

[Complete series](series.txt), [full77-path diff](final.diff),
[exact nine-path delta from02e](change-from-02e.diff),
[old/new range comparison](range-diff.txt), [history inventory](history.json).
Original dependency and adapter authors/dates are preserved. One final0.32
update replaces the unmerged0.31.2 dependency selection; no intermediate pin,
merge commit or fixup stream. Adapter implementation, tests, BFF, scripts,
E2E fixtures and Node/flake inputs are byte-identical to reviewed02e.
The two logical commits retain dependency versus adapter ownership. Owning
provenance/packaging docs and the dated technical work log reflect the selection.
Old release work logs remain explicitly historical, including the02e record.

NO MIGRATIONS in the owned delta: src/lib/api/migrations.test.ts is a VPS action
fixture. No database/schema/persisted format or wire protocol change. Upstream
history is retained intact; no assertion that upstream has no migrations.
Rollback uses matching prior frontend/BFF artifacts, retaining BFF credentials
and session storage. No coordinated node/API upgrade is required.

## Actual artifact and compatibility

Approved archive: `package-032/vpsadmin/archives/haveapi-client-npm.tgz`, SHA256
`144cf17ada3b4578c8a3d81c87d183c94bd72d98e83934475c019b8bfd8b2efc`.
Registry SHA512 integrity and parsed SLSA subject digest match those actual bytes.
Release source `0e7166a0f8f15827bfac051666a53bf449e999ec`, refs/tags/v0.32.0,
workflow41056909572/attempt1. No cryptographic signature-verification claim.
[Metadata](npm-metadata.json), [parsed statement](npm-provenance-statement.json),
[provenance record](provenance-final.json), [used declarations](used-declaration.diff).
Actual published dist differs from checked-in tag dist; compatibility never uses
a reconstructed tag bundle or Ruby release identity.

The used RequestSpec/AsyncClient.request/AsyncError surfaces retain the adapter
contract. Runtime owns transport/serialization/validation; WebUI retains live
per-request credentials, isolated public/auth clients, bounded read renewal,
abort/timeout/error mapping and uncertain-mutation non-replay. No compatibility
source correction was needed. Owning interfaces remain haveapiRequestClient.ts
and haveapi.ts; real consumers are existing domain adapters/public calls/mutation
guards. Requirements007/011/012/046/059/068 remain unchanged.

Normal declared-shell lock-only npm update changed only root selector and the
HaveAPI package node; XMLHttpRequest1.8.0 and every unrelated lock node are exact.
[Semantic lock proof](lock-semantic-diff.json). Normal prefetch produced
`sha256-ujVCNq8qjDfRlfeyu4jv9v+6q5H2u/ozQ/f+rRPoAmQ=`;
[command/result](npm-deps-hash.result.json), same six bundled WASI warnings
retained in npm-deps-hash.stderr.log. No custom fetch/archive dependency path.

Owning docs: docs/design/HAVEAPI_CLIENT.md and PACKAGING.md,
docs/work-log/2026-10-31-haveapi-0320.md, WORK_LOG.md. The old current-main entry
is labelled its original02e scope. No user-facing UI text or visual behavior
was changed, so localization/screenshot work was not introduced.

## Quick acceptance and preservation

[Original quick command](quick.sh), [result](quick.result.json),
[stdout](quick.stdout.log), [stderr](quick.stderr.log): exit0,86.956s.
Locked Node24.21.0/npm11.19.0; source guard +6cases, normal npmci, all53installed
package files exactly equal the approved archive, real AsyncClient/AsyncError
exports, root typecheck,9focused files/123PASS, docs audit257routes/64modules/
160documents/76requirements, frontend Nix parse. Auth/renewal/public/errors,
invalid/contradictory receipts, timeout/abort and mutation-no-replay use the actual
installed package via existing controlled XHR fixtures, not a library mock.
[Installed53-file archive binding](installed-artifact-binding.json).

The existing Gitless export holds exact2488 tracked blobs/modes/links and the
new lock. [Identity](identity.json), [tracked inventory](tracked-source-inventory.json).
Normal npmci did not touch retained checkout node_modules. No artificial
Nix max-jobs/cores/taskset; native watcher interface remains unavailable and the
previously disclosed documented parent-monitor fallback was used. The normal
prefetch/source evaluation is quick dependency preparation, not a full app build.

All19972 private descriptors, directory inode51554956, terminal952323/PTY323,
canonical live2e32/inode51692404 remain exact. Both oldbaf and old02e have explicit
recovery refs; current-main02e and original live0312 refs are retained. Fresh
SSH main406/own03102e/protected PR74old5dd/PR63b63 were read, not mutated.
[Baseline](baseline.json), [fresh remote proof](remote-before.txt),
[final preservation/effects](effects.json). All owned handles consumed; no active
operation. Source/Git writer RELEASED for review. No publication or registry change.
The previous19 dev-only advisories remain outside scope: their dependency nodes
are among the proved unchanged entries; no new audit claim or remediation campaign.

## Requested review and next boundary

HIGH risk because an actual protocol/authentication client artifact changes.
Request affected final general, architecture/repetition, scope/proportionality,
risk/compatibility review with explicit whole-base-to-head history, single update
stream and NO MIGRATIONS conclusion. Prior reviewer0 at02e was all4/HIGH,
NO FINDINGS; reuse its saved Sol/xhigh/read_only settings without overrides.
Lead assigns retained independent review; this packet is not self-approval.

Review accepted by lead: reviewer0 native01a19317-f44d-7250-9d07-7a133f93103a,
all4/HIGH NO FINDINGS, whole history/one stream/NO MIGRATIONS. Released postreview
full unit1929/build/fiveNix outputs now PASS on this exact reviewed tree. The
released recovery-first/explicit-old02e-lease own031 publication and independent
SSH/public comparison are complete. [Final receipt](receipt.md) and
[effects](postreview/attempt-1/effects.json). No old runtime result is relabelled;
protected PR74/63 remain unchanged. Application default integration,
production deployment and lifecycle remain separately unapproved.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/).
