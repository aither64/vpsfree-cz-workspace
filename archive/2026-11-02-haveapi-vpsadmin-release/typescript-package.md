# TypeScript client package

## Current status

Package D complete: exact reviewed commit
`d354491537f8b654b4d2c33a705cad84474f95d6` integrated into remote main and
published as npm `vpsadmin-typescript-client@0.3.0` through original tag workflow
41538988296 attempt1. Independent review accepted all four lanes/history/no
migrations without findings. All assigned local checks and exact-feature CI pass.
Original immutable artifact13184014717 was verified, then eligible protected
approval was submitted. Registry downloaded tarball is byte-identical to the
approved original, and registry SLSA statement payload binds its digest to the
exact source/tag/release.yml/original attempt.

Annotated v0.3.0 object5a51d6b108da9e57b10494bdf089b61a270b167b peels to exact
remote main/source d354491537f8b654b4d2c33a705cad84474f95d6. Fresh SSH proof retained.
A master5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 equals both exports. Source stays
clean; no post-review edits, retry/repack/tag move, claims or deployment. No
remaining D task or active utility. Lead notified final proof to unblock E.

See [publication receipt](typescript-release.md),
[registry proof](typescript-registry-verification.json),
[final checks](typescript-final-checks-result.md), and
[review packet](typescript-review-packet.md). Earlier checkpoints below are
historical preparation evidence.

API7.0/protocol2/full-fixture/all six plugins,151application resources/519actions/
8720parameters and separate1auth/5actions preserved. Canonical schema bytes equal
baseline, but actual generated code changes established conditional0.3.0. Fixed
toolchain and exact npm runtime0.32.0 pair are preserved. One final coupled SDK
commit, no obsolete history/repeated streams/migrations.

Input digests:
- Schema476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794.
- Provenance d51cfb24217fb381f66c1a0eb46168c637fea7ec988beb7e54b2d9a679ad81b6.
- Exporter lock62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c.

Isolated exact-source clone: `worktrees/<slug>/haveapi-ts-tools`, detached at
1ef9b204ba45bb261d3334be5c555cc1856b713b (tag v0.32.2 object
7f8f656ca7655bafaf2cf5e7095573806085a442). Independent Git/hooks metadata and
canonical SSH origin; clean, no HaveAPI source edits, feature branch or claim.
Lead owns source-input registration treatment. Generator source SHA256
c21f17af40295bdd633f846ef9099bfb3d7a3c52aa1b581a802b5c42d7b426e7;
VERSION SHA25676c46a6bd29921677707362fa740e3f171f82a3091d69cc97cd8c7dccdcc1d10;
shared Ruby-client source0.32.2 SHA256
d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439.
Supported npm runtime is exact0.32.0, different from Ruby source identity.
Npm peer/dev/lock agree; fixed toolchain retained. Registry integrity matches
lead receipt and [setup result](typescript-npm-setup-result.md).

675 manifest-owned sources (prior674), only new file descriptions.ts; no removed
owned file or exported declaration. Final diff687files,29934insertions/11443deletions,
principally generated output; handwritten adapter/generator wrapper/toolchain
unchanged. Tests cover SDK-exposed describe/help/options, typed metadata, input
error vs transport identity, namespace projection/raw envelopes and real published
AsyncClient loopback calls. Exact-runtime tarball check passed.

## Initial preparation evidence

Preparation complete; application edits, generator execution, project commits,
publication and longer checks await the architect's design and lead release.
No repository or machine claim has been acquired.

- Owner: implementer3, retained settings unchanged.
- Verified session: `2026-11-02-haveapi-vpsadmin-release`; `dev-session current`
  and both `DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE` match the trusted binding.
- Repository: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`.
- Fresh fetched target: `origin/main` at
  `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
- Branch: `2026-11-02-haveapi-vpsadmin-release`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin-typescript-client`.
- Created and registered with `dev-session worktree add ... --base origin/main
  --no-fetch` after fetching origin. Portal initial base matches the SHA above.
- Final preparation `git status --porcelain` and `git diff --exit-code` are clean.

## Guidance and tooling inspected

Read the workspace AGENTS routing, sessions, lifecycle, Git, commits,
verification and documentation procedures, plus dev-session-documentation and
dev-session-handoff skills. No repository-local AGENTS.md exists at the fetched
target. Read README.md, docs/development.md, docs/releasing.md, flake.nix,
flake.lock, package.json, tools/generator.json, tools/toolchain.json and the
release workflow.

The repository declares no hook framework, no hook setup script and no
core.hooksPath. Its canonical hooks directory contains only Git sample hooks;
there are no declared hooks to install. No hook was bypassed.

The pinned environment evaluates offline and `nix develop --offline --command
sh -eu -c 'node --version; npm --version; ruby --version'` succeeds:

- Node.js 24.21.0.
- npm 11.19.0.
- Ruby 3.4.11.

The four declared tool outputs were already valid in the store. Shell evaluation
identified `/nix/store/zg6r62wlcam422gh5grfv65nv38045dh-nix-shell.drv`;
the ordinary shell output was initially unrealized, and dry-run preparation
reported only that trivial shell derivation. Shell activation then completed in
under one second. No npm dependency installation, build or test ran.

## Facts for the forthcoming design package

The current package version is 0.2.0. Both peer and development dependencies
pin haveapi-client 0.30.2, while tools/generator.json records shared-source
identity haveapi-client 0.32.0. The assigned successor must use exact
haveapi-client 0.32.0 and released HaveAPI source
`1ef9b204ba45bb261d3334be5c555cc1856b713b`.

The current generator revision is
`0e7166a0f8f15827bfac051666a53bf449e999ec`. Generation is offline from committed
full-fixture schema/provenance/tooling inputs. The docs require a clean exact
HaveAPI checkout, source/tooling hashes and the repository's Prettier 3.9.10.
The recorded fixture has 151 application resources, 519 application actions,
and separately retained authentication coverage. No generator checkout has been
created or mutated during this preparation.

The release workflow validates and retains an immutable tarball and receipt;
tag publication requires source on main, matching version, enabled npm release
variable and protected release-environment approval. No release prerequisite or
registry availability is claimed by this preparation.

Next: accept the final architect-owned package and lead release, consume the
updated API schema, prepare an isolated exact HaveAPI generator checkout,
update the supported runtime pair, regenerate and evaluate the conditional
minor release under the specified checks. Any uncertain checks later use a fresh
Luna/low monitor under dev-session-monitor. No integration, deployment or CI wait
is authorized by this preparation assignment.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/

## Generation and verification checkpoint

Repeated export gate accepted: receipt identifies two independent clean-source
exports at A head `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`; all three files
compare byte-for-byte and hashes were recomputed locally.

Exact-source generation and deterministic `--check` passed in 40 seconds under
a fresh Luna/low watcher; see [generation result](typescript-generation-result.md).
The output retains identical application/auth coverage. Manifest inventory grows
from 674 to 675 owned source files only by adding `descriptions.ts`; no owned file
or previously exported declaration was removed. Real generated code changes
establish the conditional minor-release gate. Fresh remote tags and npm versions
show latest 0.2.0; 0.3.0 is selected. Final main-agent prose was applied.

Initial local check batch: clean npm install, build, source typecheck and strict
consumer typecheck passed. npm tests had 12/13 pass: the new actual-runtime test
incorrectly expected unnamespaced GET keys instead of the declared `network`
input namespace. Corrected the expectation to `network[enabled]` and
`network[limit]`; implementation/runtime behavior was correct. Tarball check had
not run because the batch stopped at this failure. Full log:
`typescript-checks-initial.log`. This batch was inadvertently launched directly;
the already-owned nontransferable handle was collected to completion without
relaunch overlap. Follow-up checks use a fresh policy watcher.

## Feature publication and review handoff

SSH feature push succeeded. Fresh ls-remote proves feature head
`d354491537f8b654b4d2c33a705cad84474f95d6`; main remains
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`. No rebase required after fresh fetch.
Full committed diff includes676 generated paths (675 owned TS sources plus
manifest),29697 generated insertions/11398 deletions;11 remaining input/package/
prose/test/checker paths. Final complete series is the single commit above.
Independent review requested through lead; no readiness/integration approval
inferred. No utility/check process remains running, no delayed test batch.

## Read-only release prerequisites

A equality gate confirmed by lead and independent fresh SSH query: vpsAdmin
master is5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5, exactly the exported source;
no A rebase. Lead reports services-up34/34pass and released A ownership.
D independent reviewer0 all-four-lane final review is assigned, not yet accepted.
D source remains clean atd354491537f8b654b4d2c33a705cad84474f95d6; main still
 e5786f69b7c223c3bb5b1de99b7f97186eec368a. No0.3.0tag exists; npm latest remains0.2.0.

Read-only GitHub checks: NPM_RELEASE_ENABLED=true. Release environment required
reviewer aither64, tag-only policy v*. Active Release tag creation ruleset25982494
covers refs/tags/v*, repository-admin bypass actor. No settings changed. Existing
npm ownership and trusted publishing are operational prerequisites; OIDC authority
cannot be proven by npm whoami, and no credentials were inspected. Package stable
version/name/lock/private:false/license/repository identity already pass existing
preflight tests. Actual preflight's on-main gate remains for exact integrated D.

Feature validation run41537316829 succeeded without a CI wait. Immutable artifact
13184393526, npm-package-d354491537f8b654b4d2c33a705cad84474f95d6,332621bytes,
was retained at typescript-feature-artifact. Downloaded receipt and archive match
source/version; tools/release.mjs verify passed under pinned Nix. Feature receipt:
SHA25657236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610,
integrity sha512-jZKO+c9azQqwXYLMp+yCl54pqhjyGDVr6rxOzq2rjusEBQ8Xm5dCdc8a2iHV5buUq8hc6835tmF5wjlP8/HJ/A==,
tag null. This is validation evidence, not the tag publication artifact.

After the lead's exact integrated D signal: fresh main/head/version/tag check,
annotated matching v0.3.0 SSH tag push triggers release.yml; record run and its
immutable artifact ID. Build validates and retains one tarball+receipt, then the
protected publish job downloads that exact ID and publishes through OIDC.
Manual dispatch is build-only. Download/retain original tag artifact and compare
registry integrity after publication. Before any uncertain retry, inspect original
run and registry; retry only failed publish with original artifact. Never move
tag, repack, rebuild tag run or replace a published version. No tag push,
publication, workflow dispatch or protected approval performed at this checkpoint.

## Integrated and publication released

Final review accepted by lead, all four lanes/history/no migrations/no findings.
Lead integrated exactd354491537f8b654b4d2c33a705cad84474f95d6 and released D claim.
Fresh own checks prove main equality and A export-source equality. Annotated tag
v0.3.0 SSH-pushed; original tag run41538988296 attempt1 underway. See
[publication receipt](typescript-release.md) for tag, workflow and immutable
artifact/registry verification. No code changes or new review needed.

## Concrete publication artifact approved

Original tag build41538988296/attempt1 passed; original artifact13184014717
retained/verified against exact tag/source/version receipt. Eligible protected
release approval submitted after verification, deployment7505242931. Separate
fresh Luna/low ts_publish now monitors terminal result; earlier build watcher
finished. No rebuild/repack/tag move or retry. Final registry/downloaded tarball
verification follows terminal success. Full details in typescript-release.md.
