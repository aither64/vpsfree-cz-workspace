# C0311 committed successor: affected final review packet

Status at submission: complete source, normal two-commit history and quick checks
passed. Lead subsequently accepted reviewer0 all-four-lane affected final review
with no findings, including whole-branch history and no migrations, at this exact
range. The released postreview operation is recorded separately; this packet
retains its original quick-proof scope. No browser or SDK campaign is included.
The subsequent required tests/build/Nix passes and released own-ref publication
are recorded in the [final postreview handoff](postreview-results.md).

Session `2026-10-24-vpsadmin-haveapi-upgrade`; lead owns tracking/review/release.
Accepted brief: `design.md`, “2026-10-27: authorized 0.31.1 adoption gates”, plus
lead's explicit acceptance of fresh main911 and seven-path reconciliation.
Canonical SSH: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
Registered checkout: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-0311`.
Branch: `dev/vpsadmin-haveapi-0311`, unpublished.

## Exact complete range and provenance

Actual implementation/review base: `9113caa0915b2908373ecd616f8f752e779ed4c9`.
Head: **`e468ca48406bde1bd99cc42a05e1832fb42162f4`**.
Tree: `13db539707ae88c8635e194ca04f3e36c6e3d76a`.
Fresh main still equals911; tracked checkout is clean.

Exactly two logical feature commits:

1. `ea842820d8696a726e3fc408c32e32827ff612b7`: consolidated final exact
   npm0.31.1 registry dependency/lock/provenance/normal Nix hash and the retained
   data-driven source guards. No intermediate 0.30/0.31.0 pin commit.
2. `e468ca48406bde1bd99cc42a05e1832fb42162f4`: carried actual AsyncClient
   production adapter, R2 uncertainty and OPTIONS corrections, compatible
   upstream overlap reconciliation, and directly affected technical docs.

Original author name/email/date are preserved for both mapped source commits;
the committer uses the contributor's normal saved identity. Normal message-file
commits, no declared/active hook bypass and no identity/configuration change.
See [commit preflight](commit-preflight.json) and both commit logs.

[Complete series](commit-series.txt), [final diff](final.diff),
[range-diff](old-new-range-diff.txt), [mapping](content-mapping.json),
[diffstat](final-diffstat.txt), [all changed paths](changed-paths.txt).
Whole feature: 74 paths, 1491 insertions/615 deletions. This is carried adoption
with 0.31.1 metadata/docs, not a new adapter implementation. Old reviewed range
was `5a2d2bdc3ad7a827038f877d75959916528db844..baf00acc31d34ab37720643c5833b4476a341f3b`.
Its dependency4d040 maps to ea842; productionbaf maps to e468.

There are no other repeated input streams, obsolete implementations, fixups or
new migrations. **No migrations**: no DB/schema, persisted-state/format, session,
wire or node protocol change is introduced by this feature. None of its
migrations was merged, released, deployed or externally consumed because none
exists. Supported live f10 and published baf remain exact retained refs; neither
is an ancestor of the consolidated successor or claimed literally merged.
Their rollout/test provenance stays in the original records.

## Release and fresh-main reconciliation

[Source reconciliation](source-reconciliation.md) records the fresh-main
movement, initial empty shell sequencing error, lead's disposition and normal
fast-forward to911. The registration's initial5a is retained as historical fact.
There was no feature edit/commit at the stale base. Fresh main adds119 paths,
including product changes and BFF security pins; all112 paths outside the carried
scope are byte-identical to911. Seven overlaps preserve current main's entries,
requirements, BFF hash, type coverage, structural ledger and dataset assertions.
Only WORK_LOG and PACKAGING had textual conflicts. The new dataset-filter test
uses the existing controlled-XHR helper instead of its fetch stub; no assertion
or production policy change. [Preservation proof](upstream-preservation.json).

The carried transport/public/error/auth/R2/OPTIONS/expiry seam is byte-identical
to baf ([empty seam diff](carried-runtime-equivalence.diff)). The rest of the
application/BFF/browser source is not claimed equivalent to baf. Current BFF
manifest/lock/hash and flake inputs equal911. The old seven f10/main overlaps
remain included in the carried production source.

Actual `haveapi-client@0.31.1` bytes match registrySHA1/SHA512 and all53 packed
files match released source `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`.
SLSA source/ref/workflow/subject/invocation fields agree with release run
40592240342 attempt1. [Artifact proof](artifact-proof.json),
[statement](slsa-statement.json), [packed hashes](packed-source-files.json),
[release comparison](release-comparison.json). Locally computed archiveSHA256:
`08383df15f590e319d0140c7fda6c096b04a8237ca316e609424bf7745e31d54`.
Registry integrity:
`sha512-W3pgK2807qLVr3Yr1yQ+illlvcNasVDM7Dr/zxUuMUK7a0lHEkkxhdUeICGkWXb9Smy9FPIY5UcQCn6JlXEtag==`.
No provenance cryptographic signature-verification claim.

Relative to0.31.0, the JS implementation diff is only Client.Version. Actual
distributed bundle equals previous bytes after version substitution; all bundled
declarations and async implementation are unchanged. Only packed package.json
and bundle change. This proves the generic runtime boundary, not server-side
documentation latency or SDK compatibility. No generated SDK adoption; SDK0.1.1
and example runtime0.30.2 remain an independent supported pair.

Root lock differs from baf only in root/client entries. XHR1.8.0 and unrelated
resolutions remain equal. New normal npmDepsHash:
`sha256-1b+5uUE4OHl47aOHSxV3Ea1VYk14soGFk48beqmmlkM=`.
Current main BFF hash remains
`sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=`.
No custom fetcher/archive dependency, transport rewrite or server workaround.

## Actual quick verification

Supported Nix shell Node24.21.0/npm11.19.0; own root and BFF installs. A0 holds
the sole watcher slot; lead-authorized visible parent fallback used CPU60–63,
nice5, Nix maxjobs1/cores2 and retained every command handle through completion.
No competing watcher, generic timeout or foreign-process signal.

- Setup PASS0/48.353s: rootci409, BFFci89; root and current BFF production audits
  both zero vulnerabilities; normal prefetch/new hash; six source-guard cases.
  [Command](setup-command.json), [log](setup.log), [exit](setup.exit),
  [installed/lock proof](installed-lock-proof.json). Six existing optional-WASI
  missing-resolved warnings remain in the ordinary prefetch log.
- Focused10 actual-package/API files **159 cases PASS**, including real-library
  auth/public/error/abort, nodes/VPS, R2 contradictory401/403/422/shared guards,
  current merged dataset filters and IP-address wrapper boundary.
- **57 current BFF cases PASS**, **five OPTIONS fixture cases PASS**.
- Complete **ci:quick PASS**, including installed declarations, scoped lint and
  format, product/docs/structural audits and root/tooling/E2E/BFF types.
  Coverage82 adopted/192 deferred; current inventory257 routes/64 API modules.
  Combined [command](quick-command.json), [log](quick.log), [exit](quick.exit),
  [elapsed](quick.elapsed):127.414s.
- Final technical prose/runtime check PASS: actual Client.Version0.31.1,
  docs149/requirements76 and diff checks. [Log](final-docs-runtime.log).
- Exact committed Gitless Nix-filtered source guard PASS,15 required files;
  [log](filtered-source-guard.log), [identity](filtered-source-identity.json).
  Rooted source `/nix/store/6p46phpszswrwq6029rmj1gyyi7ynm44-source`, NAR
  `sha256-v8sM+hBV76YE1COTvEorTg0OUSvWd4OkPzi2006mPmw=`.

The first staging command rejected a path already deleted from the index; no
commit or source mutation occurred. Addressable paths were staged normally,
the existing deletion retained, and the two functional commits completed.
[Reconciliation](staging-reconciliation.json). No tests were repeated for this
index-only correction.

## Review scope, docs and remaining limits

Whole carried branch remains high risk because it contains auth renewal and
mutation admission. Lead coordinates retained reviewer0 with saved Sol/xhigh/
read_only settings and affected lanes: general/history, architecture/repetition,
scope/proportionality, risk/compatibility. Prior complete C31 review is retained
context; request an explicit whole-series/consolidation/no-migrations conclusion
for this range and focused inspection of release metadata and seven reconciled
paths. No automatic source-review exemption is assumed.

Current HAVEAPI_CLIENT/PACKAGING and dated0311/index/historical links describe
the selected dependency, artifact evidence, failure contracts and rollback.
No member-facing prose changed; owner applied the documentation skill directly.
No UI strings, fixture assertions/timeouts or configuration policy changed.

Earlier C31 unit/build/browser results are reused only within their proven
unchanged source/artifact scope. There is no blanket current119-path baseline
or BFF/package result. Prior browser3/6+5/6 failures and separate paired f10/baf
expiry passes stay separate; lead accepted that bounded disposition without
claiming synthetic6/6, an exact cause or a preexisting failure. Old mobile60/62
is historical and does not certify the newer transaction UI.

After affected review and lead release: required new exact-head normal build
and frontend/BFF/provenance/source/package-content outputs, with complete input
graphs and owned roots. Repo guidance calls for unit/build verification; source
reuse must stay explicit because fresh main changes product/BFF inputs. No long
batch is launched by this packet, and no automatic62/browser/SDK/base campaign
is proposed. Later real TLS/BFF/OAuth acceptance belongs to lead/E3's authorized
cluster gate; actual server performance belongs to A0.

[Protected remote/worktree proof](protected-after.json),
[fresh remote boundaries](final-remote-boundaries.txt),
[tested hashes](tested-file-hashes.json). Publishedbaf, LIVEf10, PR74 alias/head,
PR63 and defaults remain unchanged. New0311ref is unpublished. No force, PR
update, merge, deploy, provider/runtime/lifecycle or source-path swap. The
[PR74 exact plan](pr74-publication-plan.md) is still a separate approval gate.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
