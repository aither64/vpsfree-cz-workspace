# Provider correction and normal dependency: owner0 final inventory

Prepared for combined final review, 2026-10-20. Source publication, full
integration and deployment are not claimed. Lead owns final combined history
assessment, review, publication and integration decisions. Owner1 owns the
uncommitted production WebUI transport/tests/docs and its next commit. No
session lifecycle or shared runtime action belongs to this package.

## HaveAPI provider

- Base: `c58704a08451a231fdf6c6123437133422af46dc`.
- Final head: `f94e65e35166a0bf8048a27c9d57c7d36957d65b`.
- Tree: `2f2879b95f4fba789d8a9d52ca914b8876438dae`.
- Parent of the new correction: `19c20c90cc957d4225ece50a92e190855f252710`.
- Latest owner observation: clean tree/index at the final head. Not pushed.
- Author and committer of the new commit: Jakub Skokan
  <jakub.skokan@havefun.cz>.

The complete six-commit series is in `haveapi-series.txt`:

1. `991101f2`: callback compatibility fixture.
2. `0d2111e5`: callback TypeScript migration and its generated bundle/types.
3. `8f8e5766`: independent async client, shared core and generated outputs.
4. `f3fcd33f`: TypeScript source workflow guidance.
5. `19c20c90`: additive CallbackClient value/type alias.
6. `f94e65e3`: nested wire-error compatibility correction.

`haveapi-final.diff` covers the complete base-to-head diff;
`haveapi-correction.diff` isolates the final correction. The new commit touches
13 paths, 105 additions/31 deletions, including coherent generated output. Only
the async decoder's error-map validation changes at runtime. The callback
runtime remains unchanged. `Envelope<T, Errors = ValidationErrors>` preserves
the callback default, while async receipts and errors use exported recursive
`ApiErrors`. Local `ValidationErrors` stays flat.

The rationale is the actual server forwarding contract: `Action#error!` accepts
custom errors and the output formatter recursively localizes their maps/arrays.
Stock validation remains flat; no claim of a stock nested VPS error producer is
made. Nested string-array leaves remain authoritative API rejections at HTTP
200 and 422. Scalar/non-string leaves and malformed metadata remain protocol
failures.

Verification before commit:

- Actual prior bundle with new regressions: expected failure, nested 200/422
  replies classified as protocol instead of API; exit 1.
- Strict source typecheck, ordinary gulp build and both generated-declaration
  consumer configurations: PASS.
- Callback compatibility: 26/26 PASS; actual async bundle suite: 39/39 PASS,
  including 13 core cases and prior save/receipt/validator regressions.
- `git diff --check`: PASS. Normal top-level Nix commit and all declared hooks:
  PASS. Reviewed unchanged Overcommit configuration was signed normally after
  stale-signature refusal. An unpublished message-only amendment wrapped text
  to satisfy the hook; final tree is unchanged. Ambient Ruby missing-extension
  warnings remain in logs; they are not claimed absent.
- Lead's direct prose pass accepted `clients/js/doc-async-client.md` unchanged.

There are **no migrations** in the complete series: none were merged, released,
deployed or externally consumed. There are no dependency/channel/pin updates or
repeated dependency streams. Generated bundle/declaration outputs remain with
their source boundaries; the latest correction updates only its affected
outputs. Earlier reviewed heads, ranges and tar identities remain historical.
The reviewer must assess the final six-commit history and retained boundaries.

## Official archive

One new archive was produced from clean committed `f94e65e3` using normal
HaveAPI `nix develop .#client-js`, `npm ci`, gulp build, clean generated-byte
comparison and `npm pack --json`. Node 24.21.0, npm 11.19.0 and TypeScript 5.9.3
were used. The tracked client lock hash remained
`1c7f66cccadc6abf9474d3403db38ce524aa49d3352efb19596aa86ffeaaaec6`.

- Vendor file: `vendor/haveapi-client-f94e65e35166a0bf8048a27c9d57c7d36957d65b.tgz`.
- Bytes: 55,702; 51 regular packed files, including 44 declarations and MIT
  `LICENSE.txt` with the original copyright notice.
- SHA-256: `41c3c3f16577dd7c8849f11615e3111302513af65a1e5640c9b121f772fb9975`.
- npm integrity:
  `sha512-aMx3ofhbRmF0JjfzUdgV3k4Oh1G/4U37uvmKvDLtX9J/5A/yy8a1GALHK6v54wJY0fU9mW2pX9kkfqBlMZOmJw==`.

Every packed file was compared with its committed `clients/js` blob: all 51
matched. No source/build/node_modules tree was packed. No `gitHead` is present;
the recorded clean build and byte reconciliation establish the source claim.
`archive-provenance.json` supplies the full file inventory and toolchain. The
archive was copied unchanged into WebUI; no intermediate vendor archive exists.
Prior `19c`/`23cad716` and older package/browser proofs keep their original
identities and are not fresh executions of this provider correction.

## WebUI dependency boundary

- Parent: `5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
- Dependency commit: `3b2eed453f385ee37d07c7339edcce8fc28ffd31`.
- Committed tree: `3e32a1871a217457fae11202e0da47e196b63a0e`.
- Author and committer: Jakub Skokan <jakub.skokan@havefun.cz>.
- Exact 22 owned paths: `dependency-paths.txt`; full delta: `dependency.diff`.
- Index empty after commit; owner1's unstaged files were preserved. No WebUI
  publication or rebase occurred. Do not describe the combined worktree as clean
  while owner1's production package is in progress.

The commit contains root manifest/lock, vendor archive/provenance/license
explanation, the standard frontend Nix hook, existing source checker/tests,
package documentation and removal of the dedicated pilot app/runner/script.
It includes no owner1 production source, test setup, ordinary E2E, API contract,
requirements, work-log or generated inventory changes.

Normal pinned npm lock installation and clean `npm ci` passed. The actual
installed AsyncClient import passed. All 482 previous non-root lock entries kept
their versions, resolved URLs and integrity; the only additions are the exact
HaveAPI archive and registry `xmlhttprequest@1.8.0` with locked integrity.
`lock-delta.json` records that guard. A package's `latest` manifest constraint
does not float through this lock.

The pinned `prefetch-npm-deps` rejected the relative tarball as
`file:///vendor/...: invalid format`. The sole watcher stopped on that first
failure; no retry or filtered-lock/cache workaround was used. Architect and lead
accepted the documented Nixpkgs `importNpmLock` alternative with its matching
`npmConfigHook` and one `packageSourceOverrides` mapping to the committed tar.
Only the frontend aggregate hash was removed. BFF hash, flake pins, source
filter, Node version, provenance and output boundaries remain unchanged. Standard
build-private metadata points at Nix store sources; the hook restores original
manifest/lock before the build.

Six source-checker tests passed, including Gitless source, changed/missing
archive and locked-integrity mismatch. Nix syntax and quick evaluation passed.
After staging the owned source files, the evaluated filtered source contained
the vendor archive and provenance:

- Frontend derivation:
  `/nix/store/7zz0g420q3fn9m1hzkjcy17g90fyrm86-vpsadmin-webui-frontend-1.0.0.drv`.
- Dependency metadata derivation:
  `/nix/store/yj02cj4ap2fx6ylzsd23i038vg393h88-vpsadmin-webui-1.0.0-sources.drv`.
- Source: `/nix/store/va46y2i77ybfz35hz935z16jynnz20bk-source`.

These are dirty-worktree preparation identities, **not** final committed build
outputs or a successful Nix frontend build. Full application tests/build,
frontend/source/package Nix builds and ordinary browser workflows remain pending
combined committed-deliverable review. No second watcher or eager build ran.

Normal Nix commit succeeded without bypass. This repository declares no hook
framework and had no active non-sample Git hooks. Lead applied the direct prose
and fact pass to the vendor guide/manifest, `HAVEAPI_CLIENT.md` and `PACKAGING.md`;
the final mechanical changes export `OUT` for reproduction and remove obsolete
prefetch-warning history from the current guide.

There are **no migrations** in this dependency package. Its archive, root lock
and Nix mechanism form one final dependency adoption stream. The complete WebUI
feature history also contains earlier pilot commits and a now-superseded runner.
This inventory does **not** claim that history consolidation is unnecessary;
lead and reviewer must assess the complete combined range after owner1 commits.

## Raw evidence and remaining gates

Raw evidence root:
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/nested-errors/`.

- `baseline.log/.exit`, `quick.log/.exit`, `async.log/.exit`.
- `commit-final-clean.log/.exit`: final normal provider hook run.
- `package/operation.log/.exit`, `npm-pack.json`, `receipt.json`.
- `dependency-setup/lock.log/.exit`, `ci.log/.exit`, `lock-delta.json`,
  `prefetch.stderr/.stdout`, `source-quick.log/.exit`, `final-quick.log/.exit`,
  `staged-paths.txt`, `commit.log/.exit`, `receipt.json`.
- Watcher operation transcript/exit:
  `/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/evidence/dependency-setup.*`.

Next: owner1 completes its committed production package and quick checks; lead
accepts the combined inventory and final review. Later authorized verification
must build the actual normal frontend and run ordinary workflows. The provider
source must be published before dependency readiness is claimed. No source push,
default merge, registry release, deployment, runtime rollout or lifecycle action
was performed in this package.
