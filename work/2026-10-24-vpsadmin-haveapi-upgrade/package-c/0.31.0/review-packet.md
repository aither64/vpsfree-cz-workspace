# C4: React HaveAPI 0.31.0 successor review

Status: source complete, committed, quick checks passed; ready for lead-assigned
independent final review. No long unit/build/package/browser campaign or
publication has run for this successor. The user-authorized cluster follow-up
belongs to lead/architect/E3 and does not change this source boundary.

Session: `2026-10-24-vpsadmin-haveapi-upgrade`. Lead owns plan/state and review
assignment. [Design C4](../../design.md#c4-independent-react-successor-implementer1).
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

## Exact source and complete history

Canonical SSH: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
Registered worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-031`.
Branch: `dev/vpsadmin-haveapi-031` (unpublished).
Fresh target/base: `5a2d2bdc3ad7a827038f877d75959916528db844`; main remains this exact target.
Head: `baf00acc31d34ab37720643c5833b4476a341f3b`; tree: `2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`.

The complete base-to-head series is exactly two logical commits:

1. `4d040e0357e405761432075a23783b4d0d779432`: direct exact npm0.31.0 registry adoption,
   lock/provenance/normal Nix hash and retained data-driven source guards.
2. `baf00acc31d34ab37720643c5833b4476a341f3b`: reviewed production AsyncClient adapter,
   R2 mutation uncertainty and OPTIONS fixture correction carried from f10,
   with directly affected current technical docs and dated work-log updates.

Both original author names/emails/dates are preserved; committer uses the saved
contributor identity. Normal Git commits used message files, checked identity,
no hook bypass. No declared hook framework, configured core.hooksPath or active
non-sample hooks were found. No Git identity/hook configuration was changed.

[Full history](commit-series.txt), [complete final diff](final.diff),
[old/new range-diff](old-new-range-diff.txt), [content mapping](content-mapping.json),
[delta from f10](predecessor-to-successor.diff). Whole branch: 73 changed files,
1426 insertions/614 deletions; this is the carried unmerged adoption, not new
0.31 implementation growth. Delta from f10 is only ten metadata/technical-doc
paths. `src/`, BFF, E2E, scripts, E2E config and Vitest setup are byte-identical
to f10 ([empty runtime diff](runtime-equivalence.diff)). This preserves current
main's seven previously reconciled product overlaps and all R2/OPTIONS fixes.

The previous dependency commit02b45 maps to4d040; f10 maps tobaf00. Superseded
0.30 pins are not retained as intermediate commits in this new series. There
are no other repeated dependency/input streams, obsolete designs or fixup
commits. Source guards remain with the dependency they enforce; adapter,
fixtures/tests and docs remain one production-boundary commit.

No migrations: no DB/schema, persisted-format, wire, BFF session or node
protocol change. No new migration was merged, released, deployed or consumed.
The live f10 software is a supported consumed predecessor, kept on its exact
original branch/worktree/ref; it is not an ancestor of this consolidated series
and is not claimed literally merged. Its production code is proved equal above.
No live source/configuration/lock, current cluster, provider/F or other project
was changed. Existing f10/877/014/757 refs and PR74/PR63 remain preserved.

## Release compatibility and artifact proof

Exact generic runtime: `haveapi-client@0.31.0`; protocol2.0 unchanged. Source:
`c9124da141adc258fbbaf67d4ec19ee3f8580849`, tagv0.31.0, release workflow
40554625752/attempt1. [Registry metadata](npm-metadata.json),
[SLSA payload](slsa-statement.json), [original attestations](npm-attestations.json),
[53 packed/source matches](packed-source-files.json),
[packed-file delta](packed-file-delta.json), [implementation diff](js-runtime-source.diff).

Archive SHA256: `1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3`.
SHA512 integrity: `sha512-KdEEu7jMFWFTHBVWtSSjZoB6WA68BDSE68IMW8LXUverfcg8V1tzptBcgu+IUOwOcqayq9OaPxJX676Cir+S0g==`.
Registry digests and SLSA subject/source/ref/workflow/invocation fields match.
All53 packed files equal the tracked clients/js files. This is artifact/source
and provenance-field evidence; no new cryptographic signature-verification claim.
The only implementation-source delta is Client.Version; async source and all
bundled declarations are unchanged. Packed changes are the bundle, package.json
and two READMEs; dist-byte identity was checked separately, not assumed.

Installed actual Client.Version=0.31.0 and the installed bundled declarations
pass checks. Only root dependency and HaveAPI lock entry changed; XHR1.8.0,
all unrelated resolutions, BFF lock/hash and flake inputs remain unchanged.
Normal frontend npmDepsHash:
`sha256-G2LFBs0USqvIXPDiGyra2uXGHxsr557BUrh7Fft0roo=`.
No local tarball/custom fetcher, SDK adoption, adapter rewrite, UI copy or server
change. Generated SDK0.1.1/example runtime0.30.2 is A/B documentation scope;
React continues its independently supported generic runtime0.31.0.

## Quick evidence and scope

Used supported `nix develop`, locked Node24.21.0/npm11.19.0 and independent
`npm ci` in the successor. A0 owns the sole utility slot; lead explicitly
released visible parent fallback. Each owned command completed/reconciled with
full logs/status, taskset62-63/nice10/Nix maxjobs1 cores2; no extra watcher.
Normal owned toolchain profile and filtered-source root are retained.

- Installed dependency/lock agreement: only root pin/client entry changed;
  source/provenance agreement and packed comparison passed as above.
- Six existing source-guard cases PASS, including substituted artifacts,
  floating/missing transport, excluded paths and symlinks. [Log](setup-confirmation.log),
  [exit](setup-confirmation.exit). Prefetch confirmed the same normal hash;
  six preexisting bundled optional-WASI URL warnings retained.
- Eight actual-package fixture files, 123 cases PASS: request transport,
  auth/language, public isolation, malformed/errors/aborts, VPS receipts,
  R2 contradictory401/403/422 uncertainty and shared no-duplicate guards.
- Complete required `ci:quick` PASS: scoped lint/format, docs/inventory,
  structural/product audits, root/tooling/E2E-core/BFF-core types. E2E type
  coverage72checked/195deferred, unchanged. [Log](quick.log), [exit](quick.exit),
  [elapsed](quick.elapsed) (141s). No full unit/build/browser run is included.
- After verification prose was finalized, docs audit PASS (137 docs,
  75 requirements, 257 routes/64 modules) and installed runtime version PASS.
  [Final docs/runtime log](final-docs-runtime.log).
- Actual committed Nix-filtered Gitless source guard PASS,15 required files,
  [log](filtered-source-guard.log), [exit](filtered-source-guard.exit),
  [source identity](filtered-source-identity.json). Rooted source
  `/nix/store/z283lwwdi70gdqbfdclkm34kgp0zvgyq-source`, NAR
  `sha256-aRkO/aTZzx3NmVDkr45L+UyroUlUeVgUrl8AcvYiSWM=`.
- Diff whitespace, exact two-commit inventory, unchanged runtime trees and clean
  final worktree checked. Fresh read-only [remote boundaries](final-remote-boundaries.txt)
  show main5a, published/livef10, PR74alias/head5dd; successor absent remotely.

Setup exception retained in [original log](setup.log)/[exit](setup.exit): all npm
operations and prefetch produced results, but bash-u exited1 on host-generated
/etc/bash_logout's unset guards. No host change or repeated installation was
made. The bounded confirmation used bash-ec, source guards and cached prefetch,
then passed. The attestation metadata helper initially looked forsha256; the
published subject issha512 and was compared to the actual SHA512 correctly.
Neither was a library/source failure or an uninvestigated test retry.

## Review and remaining gates

Whole-branch risk: high (carried auth renewal, receipt/mutation admission and
hosted package boundary). Suggested lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Lead assigns retained reviewer0 with
saved Sol/xhigh/read_only settings; no new review has yet been performed.
Prior f10 review and 0.30 receipts are historical context, not 0.31 acceptance.

After committed independent review: affected required unit/build/Nix frontend,
BFF, provenance/source/package-content checks at this exact successor with normal
owned roots; a bounded existing auth/browser smoke if relevant. Matching new
frontend/BFF provenance is required even though BFF source/dependencies are
unchanged. Do not repeat the old full API/VM/platform campaign or all62 browser
cases by default. The two proven preexisting mobile transaction-expansion
failures remain accepted residuals in old60/62 proof; no clean-browser claim,
layout fix, live OAuth/member mutations or cluster action is included here.

Technical docs only: current HAVEAPI_CLIENT/PACKAGING, dated031 entry/index and
historical predecessor links. No member-facing copy changed; owner applied the
documentation skill directly. No user-writing approval gate is introduced.

Own-branch publication and PR74 decisions remain with lead. See the concrete
[pending protected-ref plan](pr74-publication-plan.md). No push, PR edit/new PR,
force, default integration, deployment, lifecycle action or cleanup was performed.
