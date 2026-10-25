# Release follow-ups: confirmation and build diagnostics

Status: frozen execution brief for lead assignment, 2026-10-22. Architect0 owns
this design; application changes require the lead's per-package grant. This is
future development, not a change to the completed 0.30.0 publication. Use the
separate `2026-10-22-haveapi-release-followups` branch/worktree registered as
`haveapi-followups`, based on freshly verified master
`b64fb25bea8d8222fb3263b99956c0b61438a859`. Preserve that release commit, `v0.30.0`,
the original run/artifact/draft-to-public release lineage and all package bytes.
No version bump, new release, tag, default integration or registry mutation is
authorized by this brief. Original-release recovery and final destination
verification remain lead-owned, separate operations.

## Evidence and scope

The complete official job log is retained as
[release-followups-build-job120072628557.log](release-followups-build-job120072628557.log)
(run 39849807897, build job 120072628557, 3,201 lines). The maintained-package
step succeeded; these warnings did not prevent npm publication. The publication
helper stopped before reaching npm because its ordered RubyGems confirmation
guard failed. The sequence remains Python, client/server/Go/Rust gems, npm, PHP,
then final GitHub completion; changing order would not fix confirmation.

| Observation | Cause/status | Owning change |
| --- | --- | --- |
| npm deprecated rimraf 2.7.1, inflight 1.0.6, glob 7.2.3 (log 1375–1377) | Confirmed lock chain: gulp-jsdoc3 3.0.0 → tmp 0.1.0 → rimraf 2.7.1 → glob 7.2.3 → inflight 1.0.6. Top-level glob 13 from Mocha is a different chain. | Replace the obsolete documentation wrapper, package J1. |
| Rollup top-level `this` rewritten, three builds | Confirmed TypeScript ES5 helper probes such as `(this && this.__awaiter)` in emitted ESM, across seven async files; not an authored reliance on ESM `this`. | Imported, bundled helpers, J1. |
| Five circular import diagnostics per build | Real runtime edges in callback invocation and async resource objects, not all removable with type-only imports. | Bounded module-graph correction, J2. |
| `fiddle/import` will not be a Ruby 4 default gem | Actual unconditional require in Rust generator; used by atomic `renameat2` replacement. Missing explicit runtime dependency. | Rust gem dependency/lock, R1. |
| Rust `authentication__token__token` / `project__task` module/method non_snake_case | Intentional generated component-boundary separator; IR and public accessors use these names. | Precisely scoped generated lint attributes, R1; preserve names. |
| Runner useradd UID above SYS_UID_MAX; empty Git fixture clones | Nix runner account setup and deliberately empty release-test repositories, respectively. Informational, not a package defect. | Retain visible; do not edit upstream installer policy or suppress stderr. |

The npm log contains deprecation/security wording, not a completed audit finding:
installation used `--no-audit --no-fund`. The obsolete chain is development/doc
tooling, not bundled client transport. Remove its cause; do not claim an exploit
was proved, apply blanket overrides or run an unrelated dependency upgrade.

Publication evidence:

- [Attempt 1 diagnosis](release-publication-failure-diagnosis.md): PyPA received
  200 for wheel/sdist at 20:39:51/52 UTC. The immediate helper completeness read
  failed at 20:39:54. Its original response was not retained; 404 versus a valid
  partial file list is unknown. Later official metadata matched both original
  SHA-256 values. A specific PyPI cache mechanism is inferred, not established.
- [Attempt 2 diagnosis](release-gem-confirmation-diagnosis.md): Rust gem upload
  succeeded at 20:46:33; twelve five-second confirmation polls exhausted at
  20:47:34. Exact responses during that minute were not logged.
- [Independent visibility controls](release-rust-metadata-visibility.md): at
  20:49:46 the canonical Rust version endpoint returned a negative cache HIT,
  Age 398, predating upload. At 20:52:22 canonical metadata, official v1/index
  and one downloaded payload all matched the original Rust gem. Unique-query
  v2 also matched. This proves a cached negative observation after upload, not
  that a request no-cache header caused recovery or a particular backend fault.
- Source/run/artifact: b64fb25bea8d8222fb3263b99956c0b61438a859 /
  39849807897 / 12455689943. Original manifest SHA-256:
  `f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`.
  Lead reports attempt 3 succeeded and the release has 11 assets; final
  destination verification has a separate owner. No new probes were made here.

## P1: registry observation contract — implementer2

Exclusive files: `utils/release/publish.rb`; new
`utils/release/registry_query.rb`; new
`utils/release/spec/registry_query_spec.rb`; existing
`utils/release/spec/publish_spec.rb` and `release_spec.rb` where current one-read
expectations change; `doc/agent-instructions/releases.md` recovery/confirmation
paragraphs. No workflow/action changes are needed for this design. If source
evidence later requires one, route its exact purpose through lead first.

Lead additionally assigned P1 `utils/release/artifacts.rb` and `rust_smoke.rb`
for R1 packaging acceptance only: inspect the retained gem's runtime fiddle
requirement against R1's declared gemspec contract, activate that requirement in
the isolated smoke and reject default-gem fallback. Coordinate the exact
requirement with implementer3; retain existing source/runtime checks. This does
not expand installation, network, environment, workflow, registry or version
scope. P1 owns these shared files; R1 supplies its requirement and fixtures.

1. Keep artifact/source verification, all-destination preflight, registry order,
   PyPA ownership of Python credentials/uploads, PHP guards, OIDC and final draft
   completion boundaries. A successful upload means accepted bytes, not yet
   publicly confirmed metadata. The helper must never rebuild, overwrite,
   retry a conflicting upload or turn a digest mismatch into a wait.
2. Separate read transport from package validation. `RegistryQuery` accepts only
   the helper's constructed HTTPS metadata URLs on `rubygems.org`, `pypi.org`
   and `registry.npmjs.org`, with no userinfo; no redirects, credentials, cookies
   or upload-token propagation. Return a small response containing parsed JSON
   (or missing), HTTP status and an allowlisted diagnostic header map. Malformed
   successful JSON/schema is an error, not absence. Existing callers can retain
   `gem_present?`, `npm_present?`, `pypi_files` wrappers.
   Preserve the previous Net::HTTP environment-proxy behavior: use its normal
   `:ENV` default rather than disabling proxies with a third `nil` argument.
   The old helper honored configured proxies and no concrete requirement
   justifies removing that compatibility. Do not inspect/log proxy environment
   values or copy publishing credentials into metadata request headers. Normal
   operator-configured proxy authentication remains Net::HTTP's responsibility;
   registry HTTPS validation, fixed endpoint guards and redirect refusal remain.
3. Successful metadata always passes existing strict checks. Add explicit gem
   `name`, `version` and `platform == 'ruby'` checks as well as exact SHA-256
   (the observed v2 schema supplies those fields). PyPI requires exact project
   and version, expected nonduplicate filenames and every matching SHA-256;
   unexpected files fail. npm retains exact identity and retained tarball
   SHA-512 integrity. Never accept a latest-version endpoint or package name
   alone. A missing checksum is malformed/conflicting evidence, not success.
4. Requests carry `Cache-Control: no-cache`. On canonical missing or valid
   incomplete metadata, make at most one additional GET to the **same exact
   version endpoint** with a fresh nonsecret `haveapi_confirmation=<random hex>`
   query. Validate the full response identically. Do not append credentials,
   use third-party mirrors, purge caches or accept an unchecked download as
   confirmation. Canonical success needs no second request. Any identity/hash
   conflict stops before alternate reads. This cache-distinct read is a
   protocol-safe mitigation, not a guarantee of origin freshness; finite expiry
   still reports uncertainty. Keep v1/direct-download controls diagnostic-only.
5. Preflight: missing is a normal result only after the canonical/fresh pair;
   transport failures never become missing. Allow up to 60 seconds for transient
   read failures, then fail before writes. Do not impose a ten-minute wait on a
   genuinely new unpublished version. Partial PyPI metadata is validated before
   staging only the missing **original** files as today.
6. Post-upload Python completeness and each gem/npm confirmation use a
   **600-second monotonic deadline**, polling immediately, then after 2, 4, 8,
   15 and at most 30 seconds. Final all-destination validation uses one shared
   600-second deadline, not an unbounded nested wait for each item. Missing or
   valid partial metadata may be retried here. Retry HTTP 408/429/500/502/503/504,
   connect/read timeout, temporary connection failure/reset and temporary DNS
   failure only. 401/403, other permanent statuses, redirects, TLS validation
   failures and schema/identity/digest errors fail immediately.
7. Treat valid Retry-After seconds or HTTP date for 429/503 as a minimum delay:
   `delay = max(normal_backoff_for_round, parsed_retry_after_or_zero)`. A zero
   value or past date must not remove the normal positive backoff. Invalid
   values use normal backoff; a valid delay above 30 seconds is honored when it
   fits (30 seconds caps normal backoff, not the server's requested minimum).
   Keep the deadline absolute: if the resulting delay cannot fit, finish as unconfirmed
   rather than retrying earlier. Invalid Retry-After uses the bounded backoff.
   Never sleep after the last permitted attempt. Bound each HTTP attempt by
   remaining time (including connect/read/body), not just each socket read;
   no request or sleep starts once the deadline expires. Inject clock/sleeper
   and transport in tests so no test waits for propagation or uses a registry.
8. Diagnostic lines identify phase, registry/package/version, attempt, elapsed
   time, HTTP outcome, missing filenames and allowlisted `Age`, `Date`,
   `Cache-Control`, `X-Cache`, `Retry-After`. Sanitize/control-limit values;
   never print bodies, auth headers, all environment values or signed URLs.
   Deadline errors say whether upload succeeded but confirmation is pending and
   which later destinations were not attempted. Retain tag/run/manifest links.

No new mutable publication journal or workflow credential path is required.
The retry loop encloses **GET confirmation only**, never `gem push`, `npm
publish` or the PyPA action. An upload failure of uncertain effect stops for
diagnosis. A workflow rerun remains an explicit operator recovery decision:
first establish that every logged successful upload is publicly visible with
the original identity/hash, then rerun using the original tagged workflow and
artifacts. Cache-distinct 404s cannot prove that an earlier upload failed. Do
not recommend immediate blind reruns or use `skip-existing`; a conflict stops.
Verified existing versions are skipped; only verified missing destinations/files
receive one ordinary upload. These future helpers cannot retrofit v0.30.0's
tagged workflow. No old source/artifact replacement is part of this package.

P1 acceptance: deterministic fake-clock/transport tests cover canonical404 →
fresh200, both404 until success/expiry, partial Python files → complete, matching
existing skip, all four gems, no npm before Rust confirmation, missing/wrong
name/version/platform/digest, duplicate/unexpected Python files, no redirect or
credential leakage, Retry-After/deadline accounting, transient versus terminal
failures, and original-only partial-file staging. Assert zero second upload
after accepted-but-unconfirmed, zero completion on any unconfirmed destination,
and fail-fast conflicts before any publish command. Replace old tests asserting
an immediate Python failure with this contract. Unit tests must not use real
sleep, registries, tokens, listeners or GitHub dispatch.
Use fake transport/clock controls for repeated 429/503 with Retry-After zero,
past/future dates, malformed values and above-backoff delays; assert positive
sleep, finite attempts and absolute-deadline refusal. A network-free transport
test also preserves Net::HTTP's environment-proxy selection and proves metadata
requests acquire no publishing Authorization/Cookie headers. Do not read live
proxy settings or create a proxy listener to test this compatibility choice.

P1 cache-regression clarification, explicitly accepted by lead on 2026-10-22:
preflight retains the union of individually validated
expected filenames/hashes observed during that invocation. Later 404 or a smaller
valid file list cannot erase known presence and schedule that file for upload.
Every response still fails immediately on identity, schema, duplicate/unexpected
file or digest conflict. Only files missing from the observed union are staged.
Post-upload and final success require one complete validated response, never
union-derived completeness. A complete preflight union only skips upload and
enters confirmation. Report regressing visibility; do not persist a new journal
or treat past presence as current availability. A withdrawn/deleted file expires
confirmation rather than triggering reupload. Publisher owns package validation
and this invocation-local known-file policy; RegistryQuery remains the minimal
transport abstraction. Safe diagnostics identify regressing visibility without
payload bodies. Focused fake controls cover canonical partial → fresh 404,
regressing/disjoint matching partials, transient responses, invocation reset,
conflicting hashes after matching evidence and union-complete preflight that
does not satisfy post-upload/final confirmation. No journal or new write/network
scope; this is an amendment to the existing P1 brief, with no further approval
required before the assigned implementation.

## J1: JS dependencies and ES5 helper emission — implementer1

Exclusive files: `clients/js/package.json`, `package-lock.json`, `tsconfig.json`,
`gulpfile.js`; new `clients/js/jsdoc.json`; new
`clients/js/test/compatibility/build_helpers.spec.cjs`; `clients/js/test/README.md`.
Lead-approved helper paths are `clients/js/jsdoc_aliases.js`,
`clients/js/test/compatibility/jsdoc_aliases.spec.cjs` and
`clients/js/rollup.config.js`. The Rollup configuration exports an `inputOptions`
factory shared by gulp and J2 graph tests; J1 owns it, with no warning filter or
context change. The alias helper owns the fixed Action heading/span mapping;
its dedicated test exercises actual maintained JSDoc output and navigation.
Own integration of any additional J2 test script into package.json; J2 does not
edit shared manifests. `build`, `dist`, `html_doc` and test emit stay generated.
The lead explicitly requires the cumulative eight JS dist outputs listed in
commit item 6 below to be committed separately after J1/J2 authored changes.
They are regenerated only, never hand-edited; other build artifacts stay out of
source history.

Official npm metadata read during this investigation reports JSDoc **4.0.5**,
tslib **2.8.1**, node-resolve **16.0.3**, Acorn **8.19.0**. Use exact devDependency
versions with regenerated lockfile; keep TS 5.9.3, existing runtime dependencies
and unrelated locked versions unchanged. Review the lock diff for unintended
churn. These versions support the repository Node 24 development environment.

- Remove gulp-jsdoc3 entirely; invoke the maintained JSDoc CLI via process.execPath
  and `require.resolve('jsdoc/jsdoc.js')` from `gulp doc`. Preserve inputs
  `build/**/*.js` and README, Markdown plugin, html_doc destination and nonzero
  failure propagation. Put equivalent options in jsdoc.json. Source inspection
  of the installed wrapper confirms it implicitly selects ink-docstrap. Switch
  deliberately to JSDoc's maintained default template and remove that obsolete
  template dependency too; generated documentation appearance may change.
  Preserve API content, navigation and existing documented page/anchor links,
  with representative checks for Client/Action/resource pages, not only an
  empty index. Do not retain tmp or the old wrapper for visual parity.
  The documented `HaveAPI.Client.Action.html#invoke__anchor` link must continue
  working if the new template emits `#invoke`. A fixed gulp post-doc step may
  add an inert legacy anchor beside the canonical heading. Preserve both IDs;
  require exactly one canonical target, reject conflicting aliases and make
  processing idempotent. Use fixed local page/ID mappings, not arbitrary
  schema-driven HTML rewriting. Test the actual generated page/link and a
  missing-target failure; keep all HTML generated and propagate build errors.
- Set TypeScript `importHelpers: true`; bundle the resolved tslib ESM through
  node-resolve. Keep target ES5, ESNext intermediate modules, the existing UMD
  shell, factory-local translations, `strict: false` payload behavior and
  CommonJS/AMD/browser-global exports. tslib is a build dependency because its
  used helpers are bundled and declarations must not require a runtime tslib
  import. Inspect the packed result to prove this. Preserve applicable bundled
  third-party license notice. Do not change Rollup `context` or filter warnings.
- Parse the final bundle with Acorn ecmaVersion5; choose the tslib ES5-compatible
  ESM entry (not modern helper module wrappers leaking const/arrows) and confirm
  no standalone runtime `require('tslib')` or AMD dependency. Check polluted
  global `__assign`, `__awaiter`, `__generator`, `__extends` values are never used.
  Existing callbacks still load with Promise/AbortController/globalThis absent;
  async operation retains its documented Promise/modern-runtime requirements.
- Public main/types entries, `Client === CallbackClient`, AsyncClient exports,
  generic/error types and deep declaration paths stay compatible. ES5 syntax
  does not promise an ES5-only async platform. No source TS helper edits and no
  hand edits to emitted helpers/bundle/declarations.

J1 acceptance: clean locked install has no three obsolete dependency versions;
build emits no THIS_IS_UNDEFINED warning; helper behavior and loader/declaration
tests pass. Do not hide other warnings while J2/R1 are pending. JSDoc generates
real API pages and reports errors visibly. A bundled isolated npm consumer works
without checkout or devDependency access, including strict TS compilation.

## J2: actual circular imports — implementer0

Exclusive source files: `clients/js/src/haveapi/client.ts`; new
`clients/js/src/haveapi/client_invocation.ts`; entry `clients/js/src/haveapi.ts`;
`clients/js/src/haveapi/async/{resource,resource_instance,resource_list}.ts`; new
`clients/js/src/haveapi/async/resource_model.ts`; new
`clients/js/test/compatibility/module_graph.spec.cjs`. Coordinate the single
gulpfile/package wiring change through J1, not concurrent edits. Existing
behavior tests may gain focused assertions only after their J1 ownership is
clear. This is a dependency-graph fix, not an API/resource refactor.

- Callback cycle root is client.ts's runtime Action import for two
  `Action.waitForCompletion` calls. Move only `Client.prototype.directInvoke`
  and `Client.prototype.invoke` implementations, with their docs, into
  client_invocation.ts, importing Client and Action there. Keep interfaces/type
  imports in client.ts and load the method-installing module from the existing
  main entry before exports are usable. This removes client → Action, including
  longer Action → Parameters → ResourceInstance → Client cycles, without
  replacing dynamic `Action.waitForCompletion` lookup with a different object.
  Preserve existing constructor/provider registration and callback/global quirks.
- Async resource.ts constructs/recognizes instances and lists while both classes
  call its resource helpers; these are real runtime edges. Consolidate exactly
  this strongly connected group into resource_model.ts. Keep existing three
  module paths as explicit re-export facades for their **existing** names/types.
  Preserve named class identity, private fields, function bodies, `instanceof`,
  nonthenability, attribute snapshot semantics, list iteration and materializing
  responses. Do not introduce runtime dependency injection, constructor setters,
  duck-typing brands, dynamic imports or new public factory APIs merely to break
  the cycle. Type-only dependencies remain type-only; no top-level instance
  construction is added. Private declaration files may change organization but
  existing consumer imports must resolve and typecheck.
- A Rollup API test observes warnings and fails on CIRCULAR_DEPENDENCY and
  THIS_IS_UNDEFINED; it must not filter them from normal builds. Use actual built
  modules after J1 configuration. Verify runtime and type export parity through
  entrypoint and retained declaration facades. Module initialization must work
  for CJS, AMD, global, strict wrappers and isolated async test emit.

J2 acceptance additionally exercises callback completion (including patched
Action.waitForCompletion), Resource-valued async parameters, local association
references versus immutable request snapshots, save/accepted-unbound behavior,
list identity/iteration and unknown-resource errors. Existing tests supply most
coverage; add only missing regression cases. No timing/auth/path/protocol change.

## R1: Rust generator warnings — implementer3

Exclusive files: `clients/rust/haveapi-rust-client.gemspec`, component
`Gemfile.lock`; `clients/rust/template/resources.rs.erb` and `resource.rs.erb`;
`clients/rust/spec/unit/generator_spec.rb` plus dedicated dependency assertions;
`clients/rust/spec/integration/run.rb` only if a focused lint-acceptance mode is
needed; `clients/rust/docs/releasing.md` for lasting packaging requirements.
No runtime/generated consumer source, route/naming algorithm or Cargo dependency
upgrade. Shared release artifact-spec changes, if needed, go through P1.

- Declare fiddle as a **runtime gem dependency** in the gemspec, because loading
  Generator requires it and atomic exchange uses Fiddle::Importer/Function.
  Resolve and lock a Ruby >=3.2-compatible maintained version in this component
  bundle; retain exact chosen version and upstream metadata in the implementation
  receipt. No ambient `gem install`, vendoring, optional rescue or replacement of
  the atomic filesystem operation. The current isolated client-rust shell already
  installs this locked bundle. Broaden Nix inputs only if a concrete build failure
  shows a missing native build prerequisite; route that through lead first.
  This prerequisite is now demonstrated: implementer3 reports fiddle 1.1.8
  extconf cannot find libffi through pkg-config or `ffi.h`/`ffi/ffi.h` in the
  declared isolated shell. Lead approved implementer0 as sole `flake.nix` editor
  to add libffi to both the client-rust and top-level release shells. The chosen
  gem requirement is `~> 1.1`, `>= 1.1.8`, locked to 1.1.8 with its official
  checksum; no unrelated dependency update or atomic algorithm change. Supply
  native headers/libraries through Nix, not ambient installation. Acceptance
  must prove the clean isolated dependency build and retained-gem activation.
  Setup remains serialized behind the active J1 utility. The reported shellHook
  setup failure exited 7, affected only the new worktree's `.gems`, and left no
  active process or released/shared-source effect; owner evidence retains the
  incident details. This report is not a successful setup or compile receipt.
- Keep the documented double-underscore component boundary and all method/module
  spellings. Add `#[allow(non_snake_case)]` only to affected generated module
  declarations and Client accessor methods, with the naming-contract rationale.
  Avoid crate-wide allow(warnings), blanket RUSTFLAGS and suppressing runtime or
  handwritten diagnostics. For module declarations, the narrow allowance may
  apply within that generated module; keep generated field/action naming tests
  and do not present it as a handwritten-code lint exception. No renaming or
  dropping disambiguation to appease the style lint.
- Unit fixtures assert exact existing names/routes remain, attributes occur
  only for identifiers requiring the double-underscore exception, ordinary
  names remain unchanged, and generator ownership/check/determinism still work.
  Package smoke must install declared fiddle through the retained gem dependency,
  not rely on the Ruby default gem. Generated source bytes/provenance digest may
  change after regeneration; existing generated clients remain functional.

R1 acceptance: no Ruby default-gem warning when loading the installed generator;
generated nested fixtures compile with `-D non_snake_case` at supported Rust1.95
and development toolchain (same pin evidence acceptable only with its recorded
limits). No new lint suppression outside the generated owning items and no public
identifier, schema, route, MSRV, crate-name or atomic replacement behavior change.

## Execution, review and checks

The concrete cumulative post-review command sequence and exact compiler
selection are in [release-followups-verification-plan.md](release-followups-verification-plan.md).
It supersedes duplicated long-command suggestions below; no command has been
executed by the architect.

Lead confirms the new worktree/baseline and grants P1/J1/J2/R1 independently.
Implementer0 retains all shared Git/index/hook serialization. P1 and R1 can
proceed independently. J1 and J2 edit disjoint files but coordinate Rollup test
wiring; full JS green depends on both. No owner edits release source or original
dist. Technical project docs accompany owning code; lead owns user-facing prose.

Lead explicitly accepted the normal environment-proxy behavior and
`max(normal_backoff, Retry-After minimum)` clarifications after reading the
updated design. The positive-union preflight clarification remains accepted.

Suggested dependency-safe logical commit sequence (implementer0 serializes Git;
these are boundaries, not authorization for new work):

1. **Rust runtime dependency and build prerequisites.** Rust gemspec and its
   complete consistent lock update; `flake.nix` libffi additions to both owning
   shells; P1's `artifacts.rb`/`rust_smoke.rb` retained-dependency checks and their
   focused specs; runtime-dependency packaging documentation. Keep the declared
   requirement, native build input and isolated activation acceptance together.
   No naming templates or registry confirmation changes in this commit.
2. **Rust generated-name lint handling.** The two templates, naming-specific
   generator/compile-harness checks and naming rationale. Preserve every public
   identifier and route. This change is independently reviewable from Fiddle
   and carries no dependency/lock/native-input edits.
3. **JavaScript build and documentation tooling.** J1 package/lock changes,
   tsconfig imported helpers, gulp/shared Rollup options, maintained JSDoc config
   and alias helper, helper/alias/ES5 compatibility checks and test documentation.
   Keep this one coherent tooling dependency update; do not split the final
   lockfile into incoherent dependency fragments. Existing cycle diagnostics
   remain visible at this intermediate boundary.
4. **JavaScript circular-module correction.** J2 callback invocation extraction,
   async resource implementation/re-export facades, entrypoint wiring and graph/
   runtime compatibility tests. This follows J1 because graph checks consume its
   shared Rollup options. Include any J1-owned final test-wiring hunk that depends
   on these new files here, so no earlier commit references absent test modules.
5. **Registry confirmation and recovery.** New RegistryQuery, Publisher changes,
   fake-clock/transport/positive-evidence tests and release-guide confirmation
   prose. Includes the accepted proxy/backoff/preflight-union behavior. Exclude
   Rust retained-dependency acceptance already committed in item 1.
6. **Cumulative generated JavaScript distribution.** Regenerate from the final
   J1/J2 sources with their committed lock, then commit exactly these eight
   outputs separately, with no hand edits: `clients/js/dist/haveapi-client.js`,
   `clients/js/dist/types/haveapi.d.ts`,
   `clients/js/dist/types/haveapi/client.d.ts`,
   `clients/js/dist/types/haveapi/client_invocation.d.ts`,
   `clients/js/dist/types/haveapi/async/resource.d.ts`,
   `clients/js/dist/types/haveapi/async/resource_instance.d.ts`,
   `clients/js/dist/types/haveapi/async/resource_list.d.ts`,
   `clients/js/dist/types/haveapi/async/resource_model.d.ts`.
   The new client_invocation/resource_model declaration paths are generated
   outputs even if ignored before explicit staging; retain their public facades.
   Any different generated file set needs reconciliation, not a broad directory
   add that could sweep in unrelated artifacts.

P1 and R1 may touch different hunks of release specs/docs: owners identify which
belong to item 1 versus item 5 before implementer0 stages them. Likewise separate
dependency and naming test hunks for items 1/2; do not stage a whole mixed file
merely for convenience. If a test requires a later file, move that test and its
minimal wiring to the later dependent commit rather than weakening the test.
Preserve other owners' work without global stash/reset. Hooks remain mandatory.
Use concise area-prefixed subjects and explain purpose/compatibility in bodies;
keep test receipts in session records. No follow-up `Version 0.30.0` commit or
version bump: that message belongs to immutable released history. Inventory and
review the complete final six-part series, not just its last commit, before
long acceptance. Exact boundaries may be combined only where concrete file/test
dependencies require it; keep runtime Fiddle and generated-name lint separate.

Known short checks, after authorized implementation and locked setup:

- P1: root tools-only Nix shell, `make release-check`, `make release-test`;
  focused fake-clock registry specs and Ruby syntax/RuboCop for changed helpers.
- J1/J2: client-js shell, `npm run typecheck`, `npm run build`,
  `npm run test:compatibility`, `npm run test:async`, `npm run test:resources`,
  `npm run test:types`; new focused tests must not require a server. A build
  needed by unit tests is a quick local check, not the full release build.
- R1: root/component declared shell, `make test-rust-unit`; owning Ruby checks
  and offline template/naming/dependency specs. No full Cargo acceptance yet.

Commit all intended code/docs/lock changes with normal hooks. Inventory the
complete new branch series, exact base/head and final diff; no migrations.
Independent mandatory final review covers registry security/recovery/partial
publication, deadline tests, loader/helper compatibility, runtime graph and Rust
package/naming boundaries. Close findings and pass relevant quick checks before
long acceptance. Earlier 0.30.0 review does not cover these changes.

After review, a fresh policy watcher runs the authorized long batch from the
exact final branch head: clean `make release-deps`, `gulp doc`, full JS/server
contract suite; `make release`, `make test`; retained-artifact `smoke-npm`, Rust
gem smoke, Python package smoke and artifact verification per the release guide.
Include isolated CJS/AMD/browser/strict bundle and strict installed declaration
consumers, ES5 parser, exact Rust generated-name lint compile, and packaged fiddle
dependency activation. Capture full logs and assert named warnings absent,
reporting remaining diagnostics rather than hiding them. No TestPyPI/RubyGems/npm
upload or release dispatch is needed to prove polling correctness; fake HTTP
responses are authoritative for transient/control paths. A later build-only CI
run may validate runner differences on the new development branch, never tags.

## Compatibility and recovery

No DB, persistent application state, protocol, API-version, deployment, PHP mirror
or generated SDK naming migration. Old/new clients interoperate as before. JS
keeps its browser/Node formats and declared ES5 syntax, with existing async
runtime requirements. JSDoc uses a newer default renderer but must preserve
documented API content and destination. Rust consumers do not need regeneration;
future generator use requires its explicitly declared dependency and produces
the same public names with scoped style attributes. Regeneration changes owned
source hashes normally; do not rewrite published generated crates.

Release-tool runtime may wait up to ten minutes per post-upload destination;
this is deliberate bounded observability, not repeated publication. Account,
schema and content errors remain immediate. Rollback of these development
changes needs no state conversion. Registry writes are irreversible and are
outside this follow-up; the existing original-tag/original-artifact recovery
procedure remains in force. No test, build, install, listener, credential read,
source edit or Git mutation was performed for this design. Public npm metadata
was read to select exact tool versions; PyPI/RubyGems visibility evidence was
reused from its assigned owners, with no duplicate package-visibility probes.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
