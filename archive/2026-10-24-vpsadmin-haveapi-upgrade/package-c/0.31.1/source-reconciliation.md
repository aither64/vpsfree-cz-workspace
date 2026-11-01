# C0311 source and baseline reconciliation

The released generic npm package is verified independently of the server-side
TypeScript documentation fix. [Artifact proof](artifact-proof.json),
[packed/source hashes](packed-source-files.json),
[release comparison](release-comparison.json) and
[implementation diff](js-runtime-source.diff) bind the actual 0.31.1 archive to
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, tag v0.31.1, release run
40592240342/attempt 1. Registry SHA1/SHA512 match actual bytes; locally computed
SHA256 is `08383df15f590e319d0140c7fda6c096b04a8237ca316e609424bf7745e31d54`.
The SLSA artifact subject, source, ref, workflow and invocation fields agree;
no cryptographic signature-verification claim is made. All 53 packed files
equal tagged source. Compared with 0.31.0, only package.json and the bundle
change; the bundle is byte-identical after version-string substitution, and
all bundled declarations and async implementation remain unchanged.

Fresh canonical WebUI main advanced from 5a2d2bdc to
`9113caa0915b2908373ecd616f8f752e779ed4c9` while the successor was being prepared.
The initial assertion caught the movement. A sequencing mistake then created
the new empty registered shell at 5a; no source edits or commits occurred there.
The effects were reconciled and reported before any carry or dependency setup.
Lead accepted fresh 911 as the implementation/review base and explicitly
released ordinary preparation. The clean empty own branch was fast-forwarded
with `git merge --ff-only`, without reset, force or changes to other checkouts.
Its registration's initial 5a remains factual; final review uses actual base911.

Own worktree: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-0311`.
Own branch: `dev/vpsadmin-haveapi-0311`. [Fresh-target delta](fresh-target-delta.json)
and [complete upstream history](upstream-main-history.txt) preserve the movement.
No old branch, ref, worktree, live configuration or cluster was changed.

The baseline adds 119 paths, including BFF security pins, product and test work.
These are upstream baseline content, not additional authored upgrade scope.
All 112 paths outside the carried change are byte-identical to 911. Seven
overlaps are reconciled as recorded in [preservation proof](upstream-preservation.json):

- WORK_LOG: retain both complete sets of entries and add the dated 0.31.1 entry.
- PACKAGING: use the new frontend hash and preserve current main's BFF hash
  `sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=`.
- REQUIREMENTS: preserve current main's product/security criteria and add only
  the carried production-client pointers.
- E2E type coverage and tsconfig: retain current adopted files and add the
  carried strict public-overview fixture; retain all other deferred hashes.
- Structural ledger: retain current main's product ledger changes and the
  carried removal of the obsolete haveapi.ts size exception.
- datasets.test: retain the new exact NAS/backup-filter test and all assertions;
  route its fetch stub through the existing controlled-XHR helper so the real
  installed client is exercised, matching the other carried wrapper tests.

Only WORK_LOG and PACKAGING had textual conflicts. No adapter policy, fixture
timeout, browser configuration, UI strings or production behavior was redesigned.
R2 contradictory-receipt classification, mutation guards, OPTIONS correction,
transport/public/error/auth source and expiry fixture remain equal to baf.
Current main's BFF manifest, lock, Nix hash and flake inputs remain unchanged.

Root manifest/lock select exact 0.31.1. Compared with the predecessor, the only
root lock entries changed are the root pin and haveapi-client; XHR1.8.0 and all
unrelated resolutions remain equal. The new normal dependency hash is
`sha256-1b+5uUE4OHl47aOHSxV3Ea1VYk14soGFk48beqmmlkM=`. The independent
successor root/BFF installations, both zero-vulnerability production audits and
six source-guard cases passed. [Installed/lock proof](installed-lock-proof.json)
and [setup log](setup.log) retain actual package identity and results.

Earlier 0.31.0 evidence is reused only for the proven unchanged carried
implementation and fixture contracts. No blanket current-BFF/product, build or
browser result is inferred. The earlier 3/6 and 5/6 runs remain failures, with
separate f10/baf sole desktop expiry passes and accepted bounded disposition.
There is no synthetic 6/6 or exact-cause/preexisting claim. The old 60/62 mobile
expansion disposition is historical, not proof of the newer transaction UI.
New exact-head artifacts and required affected checks follow final review.
No migration or persisted/wire contract change is introduced by this package.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
