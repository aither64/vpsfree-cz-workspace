# Go client preparation

Owner: implementer0. Source and Git changes are limited to this session's Go
client feature worktree. No tag, default-branch or publication writes authorized.

## Baseline and release decision

- Canonical repository: `git@github.com:vpsfreecz/vpsadmin-go-client.git`.
- Fresh SSH fetch and authoritative `git ls-remote --heads --tags origin` on
  2026-10-30 show **no remote tags**. All remote refs are branch heads.
- Default `master` / initial feature base:
  `73f164dd5eeebfc494705ae27981d30872fa88c3`.
- Registered feature branch: `2026-10-30-haveapi-client-releases`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/vpsadmin-go-client`.
- Source declares module `github.com/vpsfreecz/vpsadmin-go-client`, Go 1.16,
  generated API routes for 7.0. There is no authored package version or
  repository release workflow. No independent registry publication was claimed.
- Lead selected a first `v0.1.0` conditional on meaningful generated interface
  or runtime changes. This is the first proposed semantic tag, not a known
  next minor of an existing tag. No version bump precedes the comparison.

## Inputs and boundaries

- Exact HaveAPI candidate:
  `f0465630595b4fd120561337b3d1d7fa96cbe221`; clean source and resolved inputs
  recorded in [haveapi-preparation.md](haveapi-preparation.md).
- Public schema: lead-accepted capture from implementer1, API 7.0, profile
  `public-live-api-7.0`, captured 2026-10-30 11:20:08–11:20:12 UTC by public
  unauthenticated OPTIONS to `https://api.vpsfree.cz/v7.0/`. SHA-256:
  `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`;
  3,649,376 bytes, identical to the accepted Rust snapshot. Format 1 / protocol
  2.0 / mount `/`. Inventory: 151 application resources / 519 actions;
  separately one authentication resource / five actions. Public/plugin
  completeness remains limited to this capture.
- Effective bundle lock:
  `bb4b5eab29bef661b4b3b5cd64a26852eee795105d0a1d872a37623ffb70450d`;
  shared source:
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
  Ruby 3.4.11 / Bundler 4.0.23 / Go 1.26.10. Generation used `BUNDLE_FROZEN=true`
  and the unchanged owner-prepared component bundle. All 46 relevant Go
  executable/library/template/metadata and sibling shared-schema input hashes
  are retained in [generation-inputs.json](go-logs/generation-inputs.json).
- Generator owns all `client/**`. Preserve handwritten root `go.mod`, README
  and `shell.nix`. No manual edits to generated files.
- Generate twice into fresh candidate module directories with copied unchanged
  `go.mod`, using the prepared HaveAPI component bundle:

  ```sh
  BUNDLE_GEMFILE="$HAVEAPI_SOURCE/clients/go/Gemfile" bundle exec ruby \
    "$HAVEAPI_SOURCE/clients/go/bin/haveapi-go-client" generate \
    --schema /accepted/api-7.0.json --api-version 7.0 \
    --output /candidate/client --package client
  ```

  Omit `--module`; fresh output catches obsolete files because the Go emitter
  does not remove stale destinations. Review full filename and content deltas
  before replacing only owned generated files. Compare whitespace-insensitive
  payload as well as raw formatting and explain removed API elements.
- Bind maintained Go executable, library and templates plus sibling Ruby shared
  schema identity to final retained generator gems before release acceptance;
  keep this a bounded input-correspondence check with no new runtime framework.

## Generated comparison and compatibility

- Two fresh independent candidate generations produced identical file names
  and SHA-256 hashes. Old inventory: 648 files; new: 682; 84 added, 50 removed,
  475 changed. Full comparison: [inventory-comparison.json](go-logs/inventory-comparison.json).
  Installed output equals that frozen candidate; only `client/**` changed.
- Meaningful generated changes justify the lead-selected first `v0.1.0`:
  request language/header selection, translated client errors/validation,
  IP-release campaigns/requests, node kernel/eBPF/software state, password-change
  logs and WebUI settings. OAuth revocation uses captured
  `https://auth.vpsfree.cz/_auth/oauth2/revoke` rather than the previous
  `http://api.test/_auth/oauth2/revoke` fixture value. The existing trusted-origin
  controls still apply; generation adds no automatic trust exemption.
- Every removed file was already disconnected from the previous `Client`
  resource/action graph. The exported types/constructors remained callable
  directly, so their removal still requires release documentation for callers.
  Removed groups: `AuthToken`, `SessionToken`, `EnvironmentConfigChain`,
  `IntegrityCheck`/`IntegrityFact`/`IntegrityObject`, `IpTraffic`/`IpTrafficMonitor`,
  `VpsConfig`, `VpsOutageMount`/`VpsOutageWindow`; actions
  `ClusterAuthorizeMigrationKeys`, `UserTotpConfirm`/`Disable`/`Enable`.
  These are absent from the accepted contract; keeping stale generated files
  would falsely imply support. This observation does not assert when the server
  removed or replaced them. Their complete filename inventory and reachability
  check are in [removed-file-reachability.json](go-logs/removed-file-reachability.json).
- Surviving public structs have no field-type changes in the inspected model
  declarations. Source-level field changes remain: news-log create/update
  `Message` becomes `CsMessage`/`EnMessage`; node update drops `Cpus`,
  `TotalMemory`, `TotalSwap`; advisory node-status input/output `Note` becomes
  `CsNote`/`EnNote`, and outputs expose `Node *ActionNodeShowOutput` instead of
  `NodeId`/`NodeName`. Added fields include advisory content revisions, user time
  zones, network/OAuth controls and VPS replacement backup-preservation options.
  Full structural comparison: [public-struct-delta.json](go-logs/public-struct-delta.json).
- `NewValidationError` now accepts an optional `*Client` for language selection.
  Zero-argument calls remain valid; assignment to an exact
  `func() *ValidationError` function type needs a wrapper.
- No library/runtime dependency or `go.mod` change. API remains 7.0. Consumers
  of old pseudo-versions can keep their source pin while adapting public fields
  and obsolete types; rollback cannot undo already submitted API operations.
  No migrations, persistence changes, deployment or coordinated node update.

## Verification and status

Generation/formatting and `git diff --check` passed. Go compile/format quick gate
passed in 22 seconds through a fresh catalog-selected Luna/low watcher, using
repository `nix-shell`, Go 1.26.8: `gofmt -l client` was empty and `go test ./...`
passed (`[no test files]`). The tested generated file inventory matches both
the fresh candidate and final commit. Log: [compile-quick.log](go-logs/compile-quick.log).
The lead explicitly classified compile smoke as a quick gate.
There are no existing `*_test.go` files and no declared hook framework; native
Git hook files are only `.sample` templates. No bypass was used.

## Final feature series

Base: `73f164dd5eeebfc494705ae27981d30872fa88c3`.

1. `8a7483d535ac8caf86d318c89a773afde79c5ee2` — regenerate only `client/**`.
2. `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` — lead-approved `CHANGELOG.md`
   and README language/schema/compatibility prose.

Final diff: 611 files, 22,505 insertions, 13,488 deletions. The large delta is
generated bindings, including the 84 additions/50 removals. The only handwritten
changes are 66 documentation lines. No repeated dependency/pin streams, obsolete
implementation commits, migrations or transitional schema versions. All intended
changes committed, clean worktree. Root `go.mod` and `shell.nix` unchanged.
Feature branch published over SSH after fresh fetch; remote proof confirms
`134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` after the documented narrow review
fix below. Default remains the original base.
No repository CI workflows exist in this client; no integration tests were
started by the feature push.

Go 1.16 floor verified on final head with official `go1.16.15` Linux/amd64 archive
(go.dev metadata SHA-256
`77c782a633186d78c384f972fb113a43c24be0234c42fef22c2d8c4c4c8e7475`),
inside repository `nix-shell`, with `CGO_ENABLED=0`: `go test ./...` passed.
The official dynamic binary initially hit NixOS's generic loader refusal; an
explicit Nix glibc loader plus `NIX_LD` for child tools allowed the unmodified
archive to execute. No product failure or source workaround was needed.
Log: [Go 1.16 compile](go-logs/go1.16-floor/compile.log). This explicitly checks
both language syntax and the standard library floor; latest-toolchain compilation
alone was not used to claim minimum-version compatibility. `go.mod` stays 1.16.

HaveAPI has a bounded CI-only successor,
`0e7166a0f8f15827bfac051666a53bf449e999ec`. Generator/shared-schema/runtime and
all retained lock identities are identical to generation candidate `f0465630`;
see [HaveAPI evidence](haveapi-preparation.md). Preserve both revisions and
rebind final release-source evidence deliberately. No Go payload changed.

Final retained-package correspondence passed using exact-source HaveAPI release
run `41049401404`, artifact `12973953100`. Independently verified all manifest
payload checksums and all 46 recorded executable/library/template/metadata and
shared Ruby-schema input hashes against its retained gems. Actual final Go lock
is byte-identical to generation lock. Receipt:
[retained-package-correspondence.json](go-logs/retained-package-correspondence.json).
HaveAPI publication remains an ordered prerequisite to publishing this SDK;
artifact correspondence does not itself authorize either release.

Final fresh fetch/SSH proof confirms owned feature `134a9e69` and unchanged
remote default `73f164dd`; worktree clean. Package is ready, awaiting merge and
publication approvals. No live production API mutation has run.

## Independent review follow-up

Reviewer identified an Important inherited Go-emitter boundary: `Custom` inputs
have no generated field/setter or serialization entry. Newly exposed required
inputs affected are `IpReleaseCampaign.Create.addresses`,
`IpReleaseCampaign.Exempt.addresses`, `IpReleaseRequest.Keep.addresses`, and
`WebuiUserSetting.Set.value`. Existing captured operations also affected:
optional `SystemConfig.Update.value` and required
`Webauthn.Authentication.Finish.public_key_credential` /
`Webauthn.Registration.Finish.public_key_credential`.

The lead selected and accepted the bounded documentation remedy; no generated
patch or generator expansion. Existing `DoBodyRequest(method string, path string,
params interface{}, output interface{}) error` accepts the complete namespaced
JSON request map and authenticates/adds configured language. It bypasses typed
input validation; callers check its error and response envelope and read the
namespaced payload. It does not populate the generated convenience `Output`
field or itself reject an API failure/HTTP status. Following the full reviewer
report, installed the lead's final user-facing prose in README and CHANGELOG and
amended only the final documentation commit. Focused inspection and
`git diff --check` passed; no new behavior/design required a review rerun under
mandatory-change-review step 9.

Preserved reviewed range `73f164dd..2c4f55bb` and final range
`73f164dd..134a9e69` in [review-g1-remediation.json](go-logs/review-g1-remediation.json).
Generated source hashes remain identical, preserving existing compile, Go 1.16
and deterministic-generation results. Published amended owned feature branch
using force-with-lease with exact expected old head `2c4f55bb`; remote proof
confirms `134a9e69`. No CI workflows exist to cancel. Final comparison capture
initially refused because another native command held this session's writer;
retry succeeded with exact base `73f164dd5eeebfc494705ae27981d30872fa88c3` and
head `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`.

## Integration target preparation

At the lead's assigned preparation-only boundary, fresh fetch and SSH remote
proof retain default `73f164dd5eeebfc494705ae27981d30872fa88c3` and reviewed
feature `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`. Created fresh detached target
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/vpsadmin-go-client-merge-target`
at that default base. Complete two-commit feature series unchanged; both
worktrees clean; fast-forward ancestry proven. No declared or installed hook
framework, no dependencies beyond prepared Git needed for merge/push. Existing
compile checks remain valid; no suite rerun.

No merge, claim, default push, tag or publication performed. Lead now owns Git
mutations for both prepared repositories; implementer0 stops ref changes unless
assigned a repair. Exact target/base/head and history receipt:
[integration-target-preparation.json](haveapi-logs/integration-target-preparation.json).
