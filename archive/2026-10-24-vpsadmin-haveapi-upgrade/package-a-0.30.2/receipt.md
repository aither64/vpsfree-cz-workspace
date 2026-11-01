# Package A3: HaveAPI 0.30.2 dependency refresh

Status: locally checked and committed. Package A is
`44393c352fbd5e9247850ed8490f369999553d62`; branch head after unchanged B replay
is `47946f8c0731ee464f079d955c67b768ec895411`. Worktree/index clean at handoff.
Git ownership/B3 freeze released to the lead. No active or uncertain operation.
Whole-deliverable review and post-review integration checks remain lead-owned.

Owner implementer0; session `2026-10-24-vpsadmin-haveapi-upgrade`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Current/environment identity verified.
Accepted architect brief: design.md 2026-10-26 Package A3. Initial source head
`57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`, original base
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`. The original twenty Package A
paths remain the boundary; native libffi/pkg-config shell/CI prerequisites are
retained. B-owned profiles, SDK/API identities and original authorship are
preserved. No provider patch, publication, deployment or lifecycle action.

## Retained history and source ownership

The clean pre-refresh exact head is retained in local session-owned branch
`2026-10-24-vpsadmin-haveapi-upgrade-pre-0.30.2-2026-10-26`.
Old base/head diff and complete history are saved as old-branch.diff and
old-history.txt; old-b.diff preserves the final registry-based B patch. Existing
0.30.1 review and R2 evidence remain unmodified. No remote ref is changed.

The superseded unpublished dependency stream will be consolidated into the
final 0.30.2 Package A commit, with B replayed unchanged and its author retained.
Exact old/new ranges and patch-equivalence proof follow after rewrite.

## Release provenance and compatibility

Architect-owned release bytes/metadata reside in ../release-0.30.2/. Before
extraction, all four Ruby artifact SHA256 values were rechecked against registry
metadata and the npm tarball against its SHA512 integrity. Both browser bundles
come from its dist/haveapi-client.js and match canonical source
`321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8` byte-for-byte. The saved registry SLSA
statement binds that commit/tag/workflow, run 40238928168 attempt1. Integrity and
statement inspection are recorded without claiming signature verification.
Detailed hashes are in artifact-verification.json and the architect release
receipt. PHP archive integrity is generated from its exact Packagist source ref,
which has no registry-provided archive checksum.

Ruby client/Go generator/JS/PHP 0.30.1-to-0.30.2 source changes are version-only;
server context derivation and Rust documentation lookup include the upstream R1
performance remedy. Protocol remains2.0 and API7.0/SDK0.1-series identities stay
unchanged. Server and optional generator gems move together to preserve loaded
version validation. No database migration, persistent-format or node coordination
change is intended. Rollback restores source, locks/gemsets and bundled clients
as one set; a server rollback reintroduces the prior R1 cost.

## Verification scope and documentation

Use plain scoped rake in the root Nix shell, never bundle-exec rake or the broken
local HaveAPI updater. Use ordinary Git hooks from a fresh root shell without
outer Bundler activation. Prior setup lessons: ../package-a/receipt.md and
notes/vpsadmin/2026-10-24-haveapi-adoption-dependency-setup.md.

A fresh pinned gpt-6-luna/low utility owns each uncertain setup/generation batch.
Only known quick version/hash/metadata/require, callback/PHP and mount checks run
here. Full API specs, GET/performance, services-up and package builds await final
committed-deliverable independent review under lead ownership. Adoption alone
does not close R1. Package B owns lasting API behavior documentation; this
mechanical dependency refresh needs no additional feature documentation beyond
updated declarations/generated artifacts and this current verification receipt.

## Completed focused evidence before commit

- Scoped plain-rake generation plus actual API load passed (53seconds), with
  four HaveAPI gems0.30.2 and libffi3.8.0. Recorded loaded source paths are in
  generation.log. Every packaged file from all four digest-verified Ruby gems
  matches the installed API files:211 server,65 client,55 Go and29 Rust.
  installed-source-match.json also binds the loaded context/Rust documentation
  sources to SHA256. No installed-gem patch or hidden override is used.
- Version comparison against the retained old head found only intended HaveAPI
  updates, no unrelated transitive upgrades. All121 API,29 client and33
  download-mounter lock entries agree with their generated gemset versions.
  Every HaveAPI Nix source hash matches the registry SHA256; see
  initial-resolver-changes.json and metadata-consistency.json.
- Both0.30.2 browser bundles pass syntax plus the exact upstream callback suite
  (12cases each,24 total), including callback-era runtime without Promise or
  AbortController. See js-callback.log and retained callback.spec.cjs.
- Targeted Composer generation/PHP load passed, changing only haveapi/client
  0.30.1 to0.30.2 at exact source a02dd2506209f54ea782fbd949243207bf9f93bc.
  Composer2nix changed only its archive identity/hash.13 focused tests passed
  355assertions with the same existing pagination nullable-argument deprecation.
  The utility omitted its requested separate log despite naming it in the
  report; php-generation.log was reconstructed from the complete retained
  php-watcher.log transcript without rerunning. Exit0 and23seconds are in the
  original transcript/report.
- Scoped Nix formatting, four Ruby declaration lint checks and whitespace pass.
  All tracked HaveAPI references are inventoried; no0.30.1 remains in assigned
  Ruby/generated/browser runtime files. Historical B docs remain B2-owned.

The bounded existing documentation_profile mount/init tests remain separate
from any full page GET or R1 performance acceptance. Final state follows after
normal hooks/history consolidation.

The existing two documentation_profile examples passed under all plugins:
2examples,0failures,47seconds. This mounts the real consumer/profile and checks
both Rust init renderers without a full page GET. The watcher retained a
truncated intermediate chunk from verbose database setup; final completion,
selected example result and exit0 are present. mount-quick.log identifies this
capture limit; no successful full-suite or full-raw-log claim is made.

Before rewrite, all five B files match the old committed head byte-for-byte.
The17-path refresh delta and expected hashes of all25 feature files were saved.
The only test-created PHP cache directory was removed; dependency caches remain
available for B2. Old notes/review records and the preserved source ref remain.

PHP integrity cross-check: generated php-packages.nix source hash decodes to
`fcf2453bbfa1dd8ebe8861124151100cf422e355a9319eea84f7fb9f3a3864b2`, exactly the
architect-downloaded archive at the Packagist source ref. php-integrity.json
records both Nix and SHA256 representations. No unrelated PHP package changed.

At the commit/rewrite preparation checkpoint, no command or watcher remains
active. The lead was sent the API readiness report early and the complete quick
result. Normal hook/rebase execution waits only for confirming that the other
worktree writer is paused, under the lead's serialization contract.

## History rewrite execution

The original A3 assignment explicitly retained sole A Git/index ownership and
made B2 a future dependent writer. Repeated status reports found no B changes;
all five B files matched the old head. After a reasonable chance for the lead
to change that serialization, execution proceeded under that existing gate,
without starting or consuming another writer's work.

The scoped restore of the saved seventeen owned paths changed the intended
files, then ambient post-checkout Overcommit rejected its effective configuration
signature. The subsequent normal root Nix rebase reached the intended original
A edit stop. Both effects were reconciled immediately: clean tree, exact HEAD
ff44d95e, normal rebase state, no unknown or abandoned command. No hook was
bypassed. The saved exact A delta was applied at that stop and only its paths
staged for a normal root Nix amend. Future checkout/restore operations should
also use the repository Nix environment because they can invoke Overcommit.

## Exact final history, migration conclusion and handoff

Old reviewed/source range:
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`.
New Package A/B range:
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..47946f8c0731ee464f079d955c67b768ec895411`.

| Final commit | Scope | Old disposition |
| --- | --- | --- |
| `44393c352fbd5e9247850ed8490f369999553d62` | Original20 Package A dependency/native-prerequisite paths, final0.30.2 | Replaces unpublished `ff44d95ebe9794341185ba5c78250e130dde80fd`; obsolete0.30.1 pin stream consolidated |
| `47946f8c0731ee464f079d955c67b768ec895411` | Unchanged five-file registry-based Package B | Replays `57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`, exact patch and original author/date/message retained |

The lead confirmed B3's explicit no-write/no-command freeze before the amend
completed. All normal pre-commit hooks passed: MigrationSpecs, Nixfmt,
VpsadminWebuiI18n, RuboCop and VpsadminApiI18n. All commit-message hooks passed
without warnings. Rebase continued normally to the session feature branch.
No repository-wide reset, stash, hook bypass or foreign/default ref mutation.

Proofs: all25 final feature-file hashes equal the pre-rewrite expected files;
old-head-to-new-head diff is byte-identical to the saved seventeen-path A delta;
B's full binary patch is byte-identical, and B author/date/message are identical.
The index/worktree are clean, original twenty A paths retained, no extra feature
paths. See [history-proof.json](history-proof.json),
[range-diff.txt](range-diff.txt), [final-history.txt](final-history.txt),
[final-a.diff](final-a.diff) and [final-branch.diff](final-branch.diff).
The retained pre0.30.2 local ref still points to the exact old head. Earlier
review receipts remain historical; no reviewed-equivalence claim is made for
new released server/Rust source identities. Independent final review remains
required after B3/current documentation is complete.

Migration conclusion: **none** in the entire base-to-head series. No migration,
schema, seed or persisted-format change was merged/released/deployed/externally
consumed as part of this feature. Superseded dependency pins have no supported
consumer or state boundary requiring separate commits. Registry artifacts being
published upstream are provenance, not evidence that these vpsAdmin feature
commits were deployed or integrated. No push/merge/deployment was performed.

At release there is no setup/test/hook/rebase process running and no unresolved
command effect. Lead may hand the worktree to B3 for its owning documentation
paragraph and bounded quick evidence, preserving the final A commit. B3 may
amend B only under that assignment. R1 consumer performance/authorization/
locale/ownership proof, full/core API checks, services-up/packaged adapter loads,
SDK compile gaps and other selected long checks remain explicitly outstanding
after independent committed-deliverable review. This handoff does not call the
whole branch ready for use and does not close R1 or change R2 historical evidence.

Stable session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
