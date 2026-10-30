# TypeScript SDK preparation

Current release decision: **prepare 0.2.0**. The user clarified that generated
formatting changes qualify under the original request. The earlier semantic-only
no-release decision below is historical and superseded. Existing 0.1.1 CI
artifacts remain evidence of their exact tested head; they are not 0.2.0
publication candidates. Runtime stays exactly 0.30.2. Bounded release metadata
and documentation correction is committed at
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`; quick checks and affected final
review passed with no findings. Exact feature head is SSH-published; final
0.2.0 package CI and downloaded archive verification passed. Lead integrated
the exact reviewed head and published tag v0.2.0. npm **0.2.0 is PUBLIC VERIFIED**
at 2026-10-30 13:05:31 UTC: public tarball matches original tag artifact
12978397388 byte-for-byte and both receipt digests. Git ownership remains with
the lead. See [publication verification](typescript-release-verification.md) and
[0.2.0 review packet](typescript-0.2-review-packet.md).

Owner: implementer3. Preflight date: 2026-10-30. This is candidate preparation;
integration, tagging and publication remain separately gated. Lead owns the
session plan/state/portal; architect0 owns the design.

## Repository and release baseline

- Identity: `dev-session current` and both environment bindings agree on
  `2026-10-30-haveapi-client-releases` in `/home/aither/workspace/ai/vpsfree.cz`.
  Live roster confirms implementer3 has workspace-write access.
- Canonical fetch/push remote:
  `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`.
- Authoritative SSH `ls-remote --symref` and subsequent fetch confirm default
  `main` at `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`. Annotated `v0.1.1`
  (`f4cb49ab54214d043d34716d30a43f14224d6ce2`) peels to the same commit.
  `git diff --stat v0.1.1 origin/main` is empty. No release/default divergence.
- Registered feature branch: `2026-10-30-haveapi-client-releases`.
  Worktree: `worktrees/2026-10-30-haveapi-client-releases/vpsadmin-typescript-client`.
  Initial base/head: `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`.
- No repository-local AGENTS.md or declared hook framework exists. No
  `core.hooksPath` is configured. Repository docs and workflow supply commands.
- npm read-only registry response lists `0.0.0-stage`, `0.1.0`, `0.1.1`, with
  `latest=0.1.1`; `0.2.0` is absent. Recheck version availability before release.
  Current package/lock version stays `0.1.1` pending semantic generated diff.
- Both peer and development `haveapi-client` dependencies are exactly `0.30.2`.
  Keep this runtime requirement while updating the generator.

## Actual published artifact

Fetched npm's public 0.1.1 archive in memory and verified its SHA512 integrity:

```text
sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==
SHA256 9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8
```

The archive's `tools/generator.json`, `src/generated/.haveapi-generated.json`,
`schema/schema.json`, `schema/provenance.json` and `schema/tooling.Gemfile.lock`
are byte-identical to `v0.1.1`. This binds the actual published generation/input
baseline; npm metadata does not supply `gitHead`. No archive was extracted into
the source tree or published.

## Read-only publisher checks

- GitHub `actions/variables/NPM_RELEASE_ENABLED` returns `true`.
- GitHub environment `release` has required reviewer `aither64` and a custom
  deployment policy allowing tag pattern `v*`.
- Published npm 0.1.1 includes an npm provenance attestation reference.
  These checks establish current configuration/history, not authorization to
  publish a new version or independent verification of the live npm publisher
  mapping. No publisher configuration was changed.

## Environment preparation

Fresh verification utility selected from pinned catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`:
`verification_watcher`, GPT-6 Luna/low, native identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`;
installed execution policy is full access with approvals disabled.

Locked Nix/npm dependency preparation passed at the initial base. It reported
Node 24.21.0, npm 11.19.0 and Ruby 3.4.11 and installed three packages without
package scripts. Details: [prep result](typescript-dependency-prep-result.md),
raw disposable [log](typescript-dependency-prep.log).

## Frozen inputs and release decision

Lead handed off clean HaveAPI candidate
`f0465630595b4fd120561337b3d1d7fa96cbe221`. Read-only verification confirmed
HEAD/cleanliness. `tools/generator-source.rb identity` using this SDK's pinned
Ruby and both candidate load paths reports:

- Generator SHA256:
  `947a98d704dca737f8bef2e1042f710e77396a0a793cb7233e8093887a713d6e`.
- Shared source: `haveapi-client` 0.32.0,
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
- Candidate root VERSION SHA256:
  `e0ccf7913110f807adecc59be43ce6fb334f82a8a7f70f70fbbba34bf1eeaaf2`.
- Packaged formatter config:
  `clients/typescript/lib/haveapi/typescript_client/prettier.json`, bytes `{}`
  with final newline, SHA256
  `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`.
- Candidate TypeScript component lock SHA256 (read-only evidence only):
  `d71a09b1d8d4ce19ce5678e9c32d0962cdbfd75aa08cf895a8c861351f7e84ab`.
  This SDK uses the existing stdlib-only source helper and does not use or install
  the component bundle. No mutation of HaveAPI source, bundles or refs occurred.

Accepted `schema-candidates/typescript-fixture-a` inputs were copied after
verifying lead-supplied SHA256s:

| Input | SHA256 |
| --- | --- |
| `schema.json` | `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794` |
| `provenance.json` | `7b477c6156c82ab483d686e1e0305ea2a40b82e0e24d50dc7653228b19556927` |
| `tooling.Gemfile.lock` | `b1d32a5ff5fb7e922c56ac6efadfa765ac4b2043cae90a54f0a71124b9b90019` |

Lead verified repeat export `-b` byte-equivalence for all three files, source
`bcfa95eb136c50d25024f53a6b1af557d1173d56`, all six plugins, API 7.0/protocol
2.0/mount `/`, 151 application resources, 519 actions and 8720 parameters. Schema
bytes exactly equal the existing committed and published release baseline.

Added development-only exact Prettier 3.9.10 with locked npm integrity
`sha512-skGHTH1Yb9QvaTC4hWnRTzEYtCpApF0UMBPz+t/0ZPzP8ihefo/btKd+QA7pUE0fEwA1SbS/NmhyEcstdXOIdA==`.
`tools/regenerate` now explicitly selects this repository's local npm binary;
it ignores an inherited `PRETTIER` without changing the existing source/input
refusals. The generator enforces its exact formatter version and uses its own
packaged configuration. An added focused source test checks that an unavailable
ambient formatter does not override local selection. Toolchain record, generator
pin and hashes are refreshed. No new Ruby bundle/tooling graph was needed.

**No release.** At unchanged package/lock version 0.1.1, generation and subsequent
`--check` passed from the exact candidate. Exhaustive comparison loaded every old
manifest-owned `.ts` file with `git show v0.1.1:src/generated/<file>`, formatted
its bytes with this installed Prettier 3.9.10 and the candidate's packaged config
(`parser: typescript`), and compared against current generated bytes. All **674**
files match exactly. All 674 raw files changed through formatting only. Inventory
is identical (zero added/removed files), and manifest coverage remains 151/519
application and 1/5 authentication resources/actions. Default equals release tag;
the public artifact's manifest/input correspondence is established above.
No generated API, public type or runtime semantics changed. The huge raw diff is
generated formatting and manifest hashes; no version bump, release changelog,
tag or npm publication is warranted. Lead accepted this provisional decision
pending final independent review.

Initial generation watcher invocation contained an accidental trailing argument
and exited on usage validation before output changes. The corrected fresh watcher
ran the exact two-command script [generation command](typescript-generation-command.sh)
successfully in about 27 seconds; [log](typescript-generation-fixed.log). This was
an invocation correction, not a product defect or retry-until-green.

Source-based preparation is permitted before HaveAPI publication under the
revised design. Final retained-package inspection/extracted generator smoke,
source/package correspondence and rebind to any changed final HaveAPI SHA remain
required. No migrations or persistent state are involved in this SDK package.

## Committed candidate and verification handoff

Final candidate: `55e03a0e0a57533f0572f6f4856af33035472408`, one commit over
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`:
`Refresh offline generation for HaveAPI 0.32`. Worktree/index clean; origin/main
was fetched immediately before commit and remains the recorded base. Captured
comparison binds this exact range. No repeated pin/input update stream or
obsolete branch history remains. Single commit keeps all hash-bound tooling,
inputs and generated output consistent; no intermediate release/consumer state
requires separate pins. **No migrations.**

Quick batch passed about 42.7 seconds via a fresh policy watcher: locked npm
install, shared-source/refusal and local-formatter regression (1/1), build,
typecheck, strict consumer typecheck, and unit/release tests (10/10). Exact
[commands](typescript-quick-command.sh) and [log](typescript-quick.log).
`git diff --check` passed. Lead's final focused doc prose is included.

Final diff: 684 files +57548/-19317. Generated portion: 675 files +57468/-19275;
remaining nine tooling/docs/input metadata files: +80/-42. Full
[final-review packet](typescript-review-packet.md) records scope, complete series,
compatibility and [proposed longer package batch](typescript-package-command.sh).
No package/long verification started before independent review. Feature push
starts the same longer package CI.

Lead reports reviewer0 final independent review of
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc..55e03a0e0a57533f0572f6f4856af33035472408`
completed with **no findings**. Reviewer independently reproduced all 674
formatter-equivalence comparisons and actual npm archive baseline proofs,
accepted no-release/version 0.1.1, and explicitly concluded no repeated update
streams and no migrations. Keep the original packet/range as reviewed evidence.

Package/CI gate is authorized after rebind, but **push and package batch are held**
pending a new exact HaveAPI SHA. Its initial candidate CI failed while obtaining
Ruby 3.2.0 on ubuntu-26.04 (builder 404), before RuboCop/i18n checks. Owner0 is
making the lead-approved two-workflow latest Ruby 3.2 patch selection; source,
runtime, formatter and lock inputs are expected unchanged. Await exact new SHA
and equivalence evidence, update only generator revision pin, rerun affected
source/regeneration checks, and amend the logical SDK commit. Retain reviewed
old/new ranges and obtain the lead's affected-lane correspondence decision;
the previous candidate's review does not automatically accept a new range.

Rebind now completed: SDK final head
`d14ee69953d0664b4b6d96d7b8f2a3ede4383d88`, same base and one logical commit.
Provider final source `0e7166a0f8f15827bfac051666a53bf449e999ec`; independently
verified exact two-line provider diff and unchanged identities/ten actual locks.
SDK old-to-new diff changes only the source revision pin; all non-pin tree bytes
and all other pin fields equal reviewed head. Fresh generation/`--check`/source
refusal batch passed exit 0 in about 41 seconds. Detailed exact ranges,
correspondence proof, watcher log limitation and pending gate are in
[metadata correspondence](typescript-metadata-correspondence.md). Push/package
CI remain held until affected-range acceptance. No version/runtime bump.

## Final review acceptance and feature publication

Lead reports reviewer0's final correspondence review of exact refreshed head
`d14ee69953d0664b4b6d96d7b8f2a3ede4383d88` completed with **no findings**.
Reviewer independently verified sole pin change, final provider two-line CI
change and all ten locks; accepted exact final single-commit history, no repeated
streams and no migrations. Original four-lane review and 674/674 formatter/npm
archive evidence remain retained. Lead authorized the next package/CI gate.

Pushed exact feature head over canonical SSH. Authoritative pre/post remote proof:

```text
2026-10-30-haveapi-client-releases d14ee69953d0664b4b6d96d7b8f2a3ede4383d88
main                            60a1b5d1b911c610bd993d93ae2b28d1932a0ccc
```

Default unchanged. HaveAPI's exact final candidate is publicly fetchable:
its remote session feature ref advertises
`0e7166a0f8f15827bfac051666a53bf449e999ec`, and an unauthenticated GitHub
commit API read returned HTTP 200 for that exact SHA.

Fresh standalone policy-selected Luna/low watcher now observes only this exact
SDK head's push-triggered workflow and collects its retained artifact/receipt.
Native delegation was unavailable in this turn; launched `codex exec` with
explicit `--sandbox danger-full-access --ask-for-approval never`, model/effort
and the matching utility's developer instructions. It may collect logs/artifacts
but cannot edit, retry, approve, dispatch, publish or deploy. Full launcher log:
[watcher log](typescript-ci-watcher.log); [brief](typescript-watch-ci.md).
Prefer existing CI's full archive/receipt/consumer validation over a duplicate
local package batch. No local package batch has run. This is build-only 0.1.1;
no default merge, release tag, publisher change or npm publication.

## Final SDK CI and retained package

Exact-head [workflow run 41050381700](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41050381700)
passed on push at `d14ee69953d0664b4b6d96d7b8f2a3ede4383d88`,
2026-10-30 11:45:36–11:46:15 UTC. Build job `124044660165` succeeded;
publish job skipped. Workflow used the publicly available exact HaveAPI pin,
locked install, offline `--check`, build, typecheck, strict consumer checks,
unit/release suite, archive packing, extracted-package consumer validation and
receipt creation. Log confirms “Packed ESM, strict types and executor consumer
passed.” Existing CI covers the required package gate; the proposed local
package batches were not run.

- Immutable artifact ID: **12974257515**.
- Name: `npm-package-d14ee69953d0664b4b6d96d7b8f2a3ede4383d88`.
- Artifact digest:
  `sha256:bf82fb43faac16c875d26b450d8a4d0c14fd89353fb8b583c43d2f63f302b9cd`.
- Retention expiry reported by GitHub: 2026-11-29 11:46:10 UTC.
- [Tarball](typescript-ci-41050381700/package/vpsadmin-typescript-client-0.1.1.tgz),
  [receipt](typescript-ci-41050381700/package/receipt.json),
  [run status](typescript-ci-41050381700/status.json),
  [artifact metadata](typescript-ci-41050381700/artifacts.json),
  [full CI log](typescript-ci-41050381700/run.log),
  [watcher result](typescript-ci-watcher-report.md).

Retained receipt binds build-only package `vpsadmin-typescript-client` 0.1.1 to
commit `d14ee69953d0664b4b6d96d7b8f2a3ede4383d88`, tag `null`, filename
`vpsadmin-typescript-client-0.1.1.tgz`:

```text
SHA256 8c05778cc71bdfae404c0650022239033b96f7002482a601347a71f58a8bdc13
sha512-7bnurZ4cGeMQ4QkpVqtSwP28tlSRqYr87EXNG5ARTb8kr0ah/ovhwfcZCTQ8y0mZv+x+kB4kc+cUIsMPZFxT2A==
```

Parent independently rehashed the downloaded tarball against both receipt
digests, verified exact package/head/tag/runtime/dev-formatter metadata and
HaveAPI pin `0e7166a0f8f15827bfac051666a53bf449e999ec`, and compared its
generator identity, generated ownership manifest and all three saved schema
inputs byte-for-byte to the clean reviewed source. All **674** owned generated
modules include both JavaScript and declarations. Verification read the archive
without extracting into source, rebuilding or repacking it.

Fresh final SSH proof still reports feature `d14ee699...` and unchanged main
`60a1b5d...`; source/index remain clean. SDK implementation, quick checks, final
independent review and package CI are complete. No release qualifies, so no tag
or npm publication is proposed. Integration requires separate user direction;
cross-package HaveAPI retained-package/extracted-smoke and final publication
correspondence remain in the lead's owning release gate. No active operation or
resource claim is held by this SDK package.

## 0.2.0 release-decision correction

The user clarified that formatting is a generated-source change qualifying for
the requested minor release. The earlier semantic-only threshold was too narrow.
Lead/architect updated plan/design; preserve the earlier decisions and receipts
above as historical evidence. The public runtime/API behavior remains unchanged.

Registry/tag availability recheck: npm latest 0.1.1, 0.2.0 absent; no remote
v0.2.0 tag. Package/lock now 0.2.0, no dependency graph changes. Refreshed only
bound package-lock SHA256 in generator metadata to
`da67cb3a5430a26f86b9df6b912d14e66214f1d8239fd1a35446bb6c61e62e15`.
All generated files/manifest, HaveAPI 0e7166a0 pin, schema/provenance/exporter
lock, formatter/runtime/source/toolchain inputs remain byte-identical to d14ee699.
No generation write was needed. Added lead-written changelog and approved
README install/stale-version guide corrections; historical bootstrap instructions
remain intact.

One separate conventional release-metadata commit:
`e5786f69b7c223c3bb5b1de99b7f97186eec368a Prepare version 0.2.0 for the generated formatting update`.
Complete base-to-head series is d14ee699 followed by e5786f69 over
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`. New delta seven files +14/-10;
full range 687 files +57561/-19326. No migrations, repeated obsolete version
stream or superseded source/dependency pin. Final comparison captured; clean tree.

Fresh policy watcher quick batch first execution passed exit 0 in **38.345s**:
locked npm install, exact-source `--check`, build, typecheck, consumer typecheck
and all ten tests. Separate requested output log was missing; watcher then
violated no-retry and interrupted a redundant execution during read-only check.
Parent reconciled no source changes or unfinished operations. Successful first
run and separate interrupted run are both retained in
[launcher log](typescript-release-quick-watcher.log); no further duplicate rerun.
`git diff --check` passed; commit inside pinned Nix environment with no declared
hook framework to install/bypass.

Full affected-review inventory, evidence and incident context:
[0.2.0 packet](typescript-0.2-review-packet.md). **Push held** for the retained
reviewer before auto package CI. A new exact-head 0.2.0 archive/receipt and
consumer validation are required after review; the old 0.1.1 build cannot serve
as publication candidate. Lead records/co-ordinates the user's explicit named
integration/publication approval; this package owner has performed no default,
tag, npm or publisher mutation.

## Final 0.2.0 review, package gate and integration handoff

Lead reports reviewer0's affected final review of
`e5786f69b7c223c3bb5b1de99b7f97186eec368a` passed with **no findings**.
Reviewer independently checked version fields, unchanged external graph/source
bytes, lockhash, complete two-commit history, no repeated streams and no
migrations; accepted the successful first quick run and reconciled watcher
incident. Original unchanged-code review remains retained.

Pushed exact final feature head over SSH. Remote proof reported feature
`e5786f69b7c223c3bb5b1de99b7f97186eec368a` and unchanged main
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`. No superseded active branch run
needed cancellation. Fresh full-access/never-approval Luna/low watcher monitored
only the exact-head push CI and retained its existing artifacts.

[Run 41055792607](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41055792607)
passed in 52 seconds; build passed in 48 seconds, publish skipped. Coverage:
exact publicly available HaveAPI 0e7166a0 checkout, locked install, offline
regeneration check, build, typecheck, strict consumer check, ten tests and
retained-archive extracted ESM/declarations/executor consumer validation. No
duplicate local package batch or provider CI was run.

- Immutable artifact ID: **12976497463**.
- Name: `npm-package-e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
- Digest: `sha256:3942467a18649138a5f78582691cebba9673dede218176495989dd0309c2a7f8`.
- Expiry: 2026-11-29 12:30:48 UTC.
- [0.2.0 tarball](typescript-ci-41055792607/artifact/vpsadmin-typescript-client-0.2.0.tgz),
  [receipt](typescript-ci-41055792607/artifact/receipt.json),
  [run metadata](typescript-ci-41055792607/run.json),
  [artifact metadata](typescript-ci-41055792607/artifacts.json),
  [full run log](typescript-ci-41055792607/run.log),
  [watcher result](typescript-0.2-ci-watcher-report.md).

Receipt: `vpsadmin-typescript-client` **0.2.0**, source
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`, tag `null`, filename
`vpsadmin-typescript-client-0.2.0.tgz`:

```text
SHA256 36e699738830303fe8e1d76d102eacda025653dc75c07ce88d65a134c6ff3e3b
sha512-EugXnu4GEEdEXuaCh62MwCWQ4D9LkgmBuTnpLaSZM13NgwPbQkAWDiOdaQmr8Xt2lYsE4HrPuNEVrJsYuGJKkw==
```

Parent independently verified both tarball digests, source/version/tag metadata,
the exact HaveAPI pin, runtime 0.30.2 and formatter 3.9.10, byte-equivalence of
archive generator/manifest/all three schema inputs to reviewed source, and all
674 generated JavaScript/declaration module pairs. The old 0.1.1 archive remains
historical evidence only. This completes the SDK package gate; lead owns final
tag/publication workflow correspondence and approved release operations.

Prepared outside claims after fresh fetch:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/vpsadmin-typescript-client-merge-target`.
Fresh **detached** HEAD at origin/main
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`; tree/index clean; base is ancestor
of reviewed exact feature e5786f69. Complete series exactly d14ee699 + e5786f69,
full diff 687 files +57561/-19326; diff check passes. Actual `core.hooksPath`
absent; common hooks directory
`/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-typescript-client.git/hooks`
contains no non-sample hook files. No AGENTS.md or hook framework declared at
target; no hook was disabled or bypassed. Pinned environment is unchanged.

**Git ownership handed back to lead** after target preparation. This owner makes
no further ref mutations without an assigned repair. Lead performs fresh target
checks, approved fast-forward merge/hooks, SSH default push and remote proof in
the separate short claim. No actual merge, default push, release tag, npm write,
publisher change or claim was performed by implementer3. No active watcher or
uncertain operation remains in this package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
