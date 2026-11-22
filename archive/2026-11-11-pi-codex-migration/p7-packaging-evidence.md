# P7 packaging continuation

Owner: implementer0. **Committed source boundary accepted**, 2026-11-12.
Commit `563f6be3ae0498c4b4e9d5fffe0c8844f4555e75` over
`11888bcb6e37eaffe1cc0f3c99b92b4ccdf34e11` owns exactly ten files,
313 insertions / 16 deletions. Exact committed hashes equal the final manifest;
index empty and owned paths clean at immediate window closure. Peer edits were
preserved. Normal file-message commit, no hook bypass, push or history rewrite.

The source packages the coherent Pi SDK/Node worker, fixed manifests and H0
exports/checks, optional immutable provider configuration and matching final C
dependency. Null catalog remains disabled; configured install invokes the actual
committed read-only validator. Native Codex/catalog, strict legacy package
metadata, portal contracts and runtime/auth path separation are preserved.

Accepted scoped proofs: current five-module worker/retained closure and
null/source producer assertions (50.938 s), real final-C goModules/hash/pin
proofs (2.792 s matching build), Nix parse/workflow filter/syntax/whitespace and
lead prose pass. Full configured application install, H0 VM/full integration
and subsequent changed P3 worker/app verification remain later whole-series
post-review gates. This is no installed-runtime, branch-wide CI or merge claim.

Initial source was D `67e08f2f…`, following accepted P1-F `ee0c8663…`.
P7-C's earlier accepted dependency evidence remains in
[p7-c-evidence.md](p7-c-evidence.md). The C pin stream through `46fd1886…`
must fold into the final logical dependency update before review, preserving
buildable intermediate heads. No migration or deployed state boundary was
introduced by P7. Lead owns consolidation, final review and publication;
implementer0 retains packaging review fixes and reports capacity available.

The package adds immutable Pi/Node/worker composition and separate H0/worker
feature manifests, exports the existing host module and focused checks, and
keeps the host VM outside fast CI. Native Codex inputs/catalog and existing
strict `package.json` remain unchanged. Source does not establish installed
launch, inference or rollout readiness.

## Source and lock provenance

`flake.nix` selects Pi main revision
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc` from `pi-runtime/upstream.json`, using
its coherent upstream package and upstream-pinned `nodejs_22`. P0's matching
tested outputs were Pi `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`
and Node `/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`;
P7 actual output/derivation evidence is recorded below. Version `1.5.2` names pinned
main and does not assert tag equivalence.

The incidental lock addition occurred during concurrent P3/P5 failed
`nix develop` calls against the initial incomplete graph. Exact first-writer
attribution is unproved. Neither writer intentionally changed dependencies;
P7 preserved and reviewed the resulting graph. The semantic check against
committed D `67e08f2f…` proves that only `pi`, `nixpkgs_3` and
`nixpkgs-darwin-x64` were added, plus the root Pi input. All old nodes remain
byte-equivalent as JSON values, including C/native inputs. Pi's Linux/Darwin
nixpkgs nodes equal its exact upstream lock. No `follows` substitutes D's Node
for the upstream SDK runtime.

The helper install/symlink hunk transferred from P2 at committed `67e08f2f…`
is preserved. P3 owns the sole production manifest parser and its negative/path
fixtures; packaging does not introduce a second parser. P3's real four-module
protocol-1 worker closure is used. Production source filtering excludes
`*.test.mjs` and retains module-relative files.

P3 subsequently committed core/worker/parser at
`daa780d1781df025aa918970310f4fb0f5f66a83`. At that boundary, `main.go` has no
`pi-runtime` dispatch and `portal/cmd/workspace-portal/pi_runtime.go` is absent.
The fixed H0 manifest's application entrypoint therefore remains a concrete
P3 integration dependency; P7 does not claim working H0 application capability
or substitute a stub. Worker-only package checks remain independent. P3 opened
its document hunk and lead confirmed the window; completed writing-pass and
ownership-transfer details are recorded below.

Subsequent P3 full source commit
`a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b` adds the real handler and final
five-module core (`worker`, `protocol`, `session`, `accounts`, `package`). The
generic production filter retains that added module. P3 reports its five Node
tests and actual SDK/Go fixture passed; the initial immutable package proof below
does not cover those later changes. P2 main registration remains a separate
source/commit prerequisite for application/H0 command acceptance.

## Checks to date

- `nix-instantiate --parse` passed for `flake.nix`, `nix/pi-worker.nix`,
  `nix/tests/pi-worker.nix` and `nix/workspace-portal.nix`.
- Exact Pi-only/upstream-lock semantic assertion passed; whitespace checks pass.
- Via cached D shell `/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`,
  the Python block extracted from the actual new check exercised the workflow's
  actual jq filter: only `package` and `pi-worker` remain in its seven-name
  fixture. The host list contains its prior two targets and `pi-runtime-host`
  once, with its original condition unchanged. Embedded JavaScript syntax passed.
- Official action-ref verification found checkout `v7.0.1` current at
  `3d3c42e5aac5ba805825da76410c181273ba90b1`. Install-Nix latest patch is
  `v31.11.5` (`3dc140bfc76c49fbd4dd958429132e3746bcb086`); prior `v31.11.2`
  was `448cde739abec1eaf0646249e3d25bb8d9bc7702`. Official comparison changes
  only installer/its CI, no action input contract. All four existing installer
  refs now select the compatible latest patch; checkout is unchanged.

The single fresh-watcher evaluation packet is
`/tmp/2026-11-11-pi-codex-migration-p7-coherence-packet.json`, targeting actual
source through an explicit `path:` flake with no lock writes. It records source
hashes and requested frozen source/Pi roots, app/worker/check derivations and
check/module exports. Fresh installed-catalog standalone Luna/low returned
**PASS, exit 0, 25.7 s**. Source hashes were unchanged and all owned sessions
terminal (root watcher 88415 / driver tool 17938). No build or lock write ran.
Raw log: `/tmp/2026-11-11-pi-codex-migration-p7-coherence.log`; result/policy:
`/tmp/2026-11-11-pi-codex-migration-p7-coherence-watch/`.

| Evaluated input/output | Exact root |
| --- | --- |
| Frozen source (authoritative, not a whole-HEAD claim) | `/nix/store/z1ajm8n0khkiysxid26s4zrbjxqblxrd-source` |
| Pi source at a22 | `/nix/store/w03p2sl10qld4fyqdjr5w3dk1lr13lwg-source` |
| Worker derivation | `/nix/store/p5ivq2vmj13s36snllvxajigi0xc282k-dev-workspace-pi-worker.drv` |
| Worker check derivation | `/nix/store/zgwgj0lh5djr5b9nw5rbzkpjay8md5jj-dev-workspace-pi-worker-contract.drv` |
| App derivation (evaluation only) | `/nix/store/iv80lsx0dcrns0mvgm2nxwx63fdhbn6g-dev-workspace-0.2.0.drv` |

The expected Pi module and worker/focused Ruby/host check exports were present.
The recorded base label `67e08f2f…` predates P3; only the actual frozen source
graph establishes evaluated contents. Later approved reporting/ref changes
require the new build packet, not reuse of these derivations as final evidence.
At that evaluation the new files were untracked, so ordinary Git-flake commands
omitted them and peers retained cached tools. The P7 commit now tracks them.

The updated source also passes parsing, actual workflow-filter/host-condition
assertion and embedded JS syntax. The production module check now recurses into
P5's inert reporting module; the offline contract includes its fake callback
test. No tool registration or communication readiness follows from packaging.
The new single-build packet is
`/tmp/2026-11-11-pi-codex-migration-p7-worker-check-packet.json`; it freezes the
packaging, upstream descriptor, four worker modules and reporting module/test
hashes. Requested output GC link is
`/tmp/2026-11-11-pi-codex-migration-p7-worker-check`. Its fresh watcher stopped
in preflight with exit 70 because live P3 `session.mjs` legitimately advanced
from expected `3c128629…` to `933c7ec6…`. **No Nix argv, test, build, output
link or model operation ran.** Result/report:
`/tmp/2026-11-11-pi-codex-migration-p7-worker-build-watch/`; root watcher 44831
and driver are terminal. This is an incomplete preflight, not a test failure.

The replacement uses an immutable snapshot rather than live source prechecks.
P3 selected exact tested worker commit `daa780d…` for this preliminary check,
explicitly excluding later account/cwd/paging/supervisor changes and production
session initialization. Committed core hashes are `2614f5ba…` for `session.mjs`
and `f8deb741…` for `protocol.mjs`; earlier live hashes do not identify that commit.

Snapshot construction uses archive base
`fc02306ab8e66f85fdae06519b1c907dc1728120` (including committed P3/P5/P6), six
exact P7 packaging overlays, the four positively checked worker blobs from
`daa780d…`, and reporting blobs from
`7584b9077b84c4a7e40d6c8da13f9571d40c9126`. Every other archived regular file
was compared to the base. No live Node source was changed or frozen.

- Immutable source: `/nix/store/ainnj3jk53sq6s9zbic5g6kykby3501w-source`.
- Source NAR: `sha256-1XlcfUxNj+2s+rUK1PZ2algNLw5UIm73T6+qeDq4B3Y=`.
- Retained source GC root:
  `/tmp/2026-11-11-pi-codex-migration-p7-worker-snapshot/source-root`.
- Exact replacement packet (source hashes, NAR, driver hash, readonly metadata
  argv and single worker-only build argv):
  `/tmp/2026-11-11-pi-codex-migration-p7-worker-snapshot/packet.json`.
- Requested log/output link:
  `/tmp/2026-11-11-pi-codex-migration-p7-worker-snapshot-check{.log,}`.

That driver returned raw exit 0 in 19.635 s, but receipt inspection **rejected
the claimed check pass**: `outputs.json` contains only the source store path,
the out-link points to source, and the computed worker output does not exist.
The store-path installable selected source rather than realizing the check.
Readonly evaluation had computed derivation strings without instantiating them.
This is metadata/source realization evidence only; no passing worker test is
claimed. Correction report: `6edcc913-52b0-4f90-b476-8753bbfbeb2c`.

The unchanged immutable snapshot is now selected through the explicit expression
`(builtins.getFlake "path:/nix/store/ainnj3jk53sq6s9zbic5g6kykby3501w-source").checks.x86_64-linux.pi-worker`.
New packet `/tmp/2026-11-11-pi-codex-migration-p7-worker-realize-packet.json`
requires a fresh watcher and positive output-link/derivation, real manifest and
Node/Pi closure assertions. It does not repeat a previously executed worker test;
that test never ran. It now **PASSes, exit 0, 23.233 s**: actual check derivation
`/nix/store/537r2iklcin0m877chxm8459hrdapimq-dev-workspace-pi-worker-contract.drv`
produced `/nix/store/2g7pabzpi4n0j3ickhiwkd7401vambzg-dev-workspace-pi-worker-contract`.
The output link positively matches that path and differs from source. Real worker
`/nix/store/5nifk90ggprxdxlmy2632pvzy9yaqqnb-dev-workspace-pi-worker` has the exact
manifest and references the expected Node/Pi roots. Golden manifests, packaged
SDK/version-pipe/private-state/shared-fake-auth assertions and all three inert
reporting tests passed. No model or real-account input was used.

Raw result: `/tmp/2026-11-11-pi-codex-migration-p7-worker-realized-result.json`;
log/output GC link: `/tmp/2026-11-11-pi-codex-migration-p7-worker-realized-check{.log,}`;
watcher report: `/tmp/2026-11-11-pi-codex-migration-p7-expr-worker-watch/report.txt`.
Watcher 57583 and all owned commands are terminal. Parent inspected raw JSON,
log, real out-link and installed manifest before accepting the pass. Old
source-only packet/log/out-link remain rejected evidence. Scope stays limited
to the exact committed worker snapshot; later source remains separate.

Subsequent explicit rooting of worker `5nifk90…` failed because that output was
then unavailable; cause is unproven. Premature retention report
`792e5db1-144b-42ef-b9ab-1b2f7549e17f` was retracted by
`1dfda731-33fa-497a-9596-30d5a5125455`. The successful observed-time check remains
valid, but no worker GC-root success is claimed. Lead directed no obsolete
baseline rebuild. The next current-worker check now creates a directory output
with `$out/worker` pointing to the immutable worker, so its result link retains
the runtime closure at realization. That artifact change awaits its current-input
check; no application or authority behavior changes.

Canonical SSH fetch verified consolidated C head
`a2b58b5e8d5c59cb448453e113b5dd48b20c3477`, tree
`18dca609c3847283f615982236d6f2e65f789bf0`, on the same-session remote feature
ref. Lead confirmed exact CI run `43210515235`, attempt 1, success and released
final C preparation. The isolated source at
`/tmp/2026-11-11-pi-codex-migration-p7-final-c/source` now selects
`v0.0.0-20261112113545-a2b58b5e8d5c`. Repository pin checker/fixture passed in
1.055 s; semantic assertions show only the C version/two sums and C lock node
changed. Pi/native/all other lock nodes are preserved.

Nix generated the final C lock node with source NAR
`sha256-SQqd4G/R9zpZXMo0sIVJSm4MgJvQgcBILa5aCy+JJkE=`. Immutable vendor input:
`/nix/store/vpznvcx80x59qiqh0jxmjbzk2z55ldlw-source`, NAR
`sha256-wxPurPytvRYe38yiGsdSnfnzVIm+JjaM1SW8/8eaAM8=`, retained by
`/tmp/2026-11-11-pi-codex-migration-p7-final-c/source-root`.
Fresh hash packet `/tmp/2026-11-11-pi-codex-migration-p7-final-c/hash-packet.json`
captured the recursive derivation graph and built only `goModules` with a
deliberate fake output hash. It returned the expected mismatch, exit 1 / 24.322 s,
actual SRI `sha256-AQkAmLM+haFVh4AA0o5syMB8rFTnG0d0XrP/Rb9mJEY=`.
Graph SHA256: `ccad69f34ea67bc3077537ffbf9880f146392f37bce9c212b535f36f140415b4`.

The matching graph, with actual vendorHash in source, was realized using an
explicit `getFlake` expression. Known-warm inline check passed, exit 0 / 2.792 s:

| Actual input/output | Exact identity |
| --- | --- |
| Source | `/nix/store/1dfzhh16b61mqhgd5mgbjzkkkk4vjg2w-source` |
| Source NAR | `sha256-2ZAv1EFpxO2175AycM3OX9d7wkYXG/QHBEW9rjockWs=` |
| goModules derivation | `/nix/store/d8i0mqppxb2z4i1mnk4ndkvbqm12ysz3-dev-workspace-0.2.0-go-modules.drv` |
| Actual output directory | `/nix/store/jlrwjx2h7bdji5ydp71ivsj0768cb67h-dev-workspace-0.2.0-go-modules` |
| Retained output link | `/tmp/2026-11-11-pi-codex-migration-p7-final-c/go-modules` |

Independent `nix hash path` on the actual directory matched the selected SRI;
its `modules.txt` names final a2 and contains no f9 version. Repository pin
checker/fixtures passed again against that exact source. Raw matching receipts,
actual-verified.json and logs are under `p7-final-c/`.

All five live pin files were guarded against concurrent changes, then replaced
from that tested source in 0.002869 s. Their bytes were compared afterward;
scoped whitespace and index checks passed. The index stayed empty and no peer
overlays changed. Full source hashes are in `p7-final-c/live-apply.json`.
Final live C/Go/sums/vendor are coherent. This supersedes the f9 pin stream at
`46fd1886…`; lead still owns its history consolidation before final review.

Final live quick checks pass: four Nix parses, repository pin checker/fixtures,
actual workflow fast filter/unchanged host condition, embedded JS syntax and
scoped whitespace. No full application/native/VM build ran.

Lead released the catalog producer amendment. Optional `piProviderConfig ? null`
is forwarded unchanged through `lib.mkPackage`, checked for exact bounded outer
schema/catalog/default shape and serialized once. Non-null installs exact bytes
at `share/dev-workspace/pi-providers.json`, mode 0444, compares bytes and invokes
only `workspace-portal pi-providers validate --package-root "$out"`. Null omits
the file and invokes no validator. No generic catalog/default, flag, auth scan or
worker/H0/legacy manifest field was added. Parse and final C preservation checks
pass. The real validator dependency is now committed as recorded below;
configured full-application installation remains a post-review gate. P4 owns
strict nested decoding/raw digest/selection fixtures.

One new immutable current-worker packet includes this settled producer and
closure-retention correction, using archive base
`34043a605eb8144dc64c87ba03666330f0ebb0a9` plus the ten P7 overlays. All five
worker module bytes match committed P3 `a74ae62…`.
Source `/nix/store/w2mcxc9hy00bcsfjd5z7av9fg71kf5gz-source`, NAR
`sha256-2t3ZnUDSyKqoBHMiLvIj6pWk6w0TAyEKMn3DVw3Ox+I=`, is rooted at
`/tmp/2026-11-11-pi-codex-migration-p7-current-worker/source-root`.
Packet `/tmp/2026-11-11-pi-codex-migration-p7-current-worker/packet.json` first
checks null/source emission and invalid outer shapes through actual Nix package
functions, then builds the current worker-only check using an explicit expression.
The empty non-null envelope in the metadata assertion is emission-only and is
not represented as a valid catalog or built configured application. Driver
requires real check directory → worker reference, five installed module hashes,
Node/Pi references and recursive graph. The exact command **PASSed, exit 0 /
50.938 s**, including five reporting tests with zero failures and the actual
null/source-emission/outer-rejection assertions.

| Current-worker result | Exact identity |
| --- | --- |
| Check derivation | `/nix/store/masprjyfn69id3i789y7piywcypfc8r8-dev-workspace-pi-worker-contract.drv` |
| Actual retained check directory | `/nix/store/qwgc0ahjxd607v0azrirjghijfx6xykf-dev-workspace-pi-worker-contract` |
| Actual worker | `/nix/store/4lwv3am1wfg95l5gr5rxwphnrw5vpdwa-dev-workspace-pi-worker` |
| Graph SHA256 | `0a32d027c30029916d68ce24df4dd696d99546dabcbadbdfe3ad978a97ca0cae` |

Parent read raw `command-result.json`, `check.log`, real out-link, manifest and
store references: the check directory references its worker, which references
the exact Node/Pi roots. Five installed module hashes were checked by the driver.
All receipts and the retained `check` link are under
`/tmp/2026-11-11-pi-codex-migration-p7-current-worker/`.

This operation used registered managed watcher
`e1f3ef2d-8b12-4ad4-a477-176648c1e968`, installed package `9hr3…`, catalog
`f2d5…`, Luna/low/full_access. Its managed status was **INCOMPLETE** because
utility report delivery/status acknowledgement was unconfirmed. Lead separately
inspected the exact native utility rollout: source session 95510 joined exit 0,
all exec cells terminal, final uncertainty only report delivery. Command PASS
and incomplete managed-report status are distinct. Lead closed reconciliation
in `p7-current-worker/parent-reconciliation.json`: command-result SHA256
`9538cad5a486bd0e841f42f401277b4c085584501ae9a1948a9020413c315f9d`, seven
native exec calls matched terminal results, source 95510 exit 0 and exact-turn
task completion. Resolution `9fdb3a86-46be-4521-9d67-c583f0cbef69` was accepted
at 13:32:47; it clears only the external-effects/unsent-continuation fence.
The runtime incomplete outcome remains; no report rewrite, new command or
thread cleanup occurred. No duplicate build or status-driven rerun occurred.
Configured semantic
install and subsequent uncommitted P3-I source remain outside this proof.

The real configured validator dependency is committed at exact
`558e710232a59c55042a615ac83e5bdda2a9e390` over
`2ced04211af1b9fd22ab77ded1af69aaacb15aed`. Its owner reports focused main
tests 0.072 s and pure web tests 0.121 s passing, using actual P4 LoadInstalled/
Validate and production builtin/full-chain/default support without runtime/auth
construction. This is source/quick-check evidence, not configured application
installation or live factory readiness.

Final ten-file commit manifest is
`/tmp/2026-11-11-pi-codex-migration-p7-final-manifest.json`, observed at HEAD
`adfde64148b5dc715d972c5782dd60f1bcd49e6b` with the validator dependency proven
ancestor. Eight code/generated paths equal the passing w2mc snapshot byte for
byte. Final prose hashes are README
`8ede397e2ceb250bc5ae909f2f19b2c582ec601a85c85c07ea9d6d7c056311b3`
and portal guide
`7129b4a5606231e1fdd0652bce1199e4f03ef6e54c7c074d06ba1cdfaecc04bd`.
The paths are `.github/workflows/check.yml`, `README.md`,
`docs/workspace-portal.md`, `flake.nix`, `flake.lock`, `nix/pi-worker.nix`,
`nix/tests/pi-worker.nix`, `nix/workspace-portal.nix`, `portal/go.mod` and
`portal/go.sum`. P3-owned `docs/pi-runtime.md` is excluded. No declared hook
framework or active hook was found; no bypass occurred. The granted window
committed exactly those ten paths at `563f6be3…`; receipt
`/tmp/2026-11-11-pi-codex-migration-p7-commit-receipt.json` positively verifies
full parent/head, complete inventory, committed hashes and owned cleanliness.
The index was empty at closure and the lead accepted that source boundary.

Remaining initiative gates: lead-owned history consolidation/final review and
the affected final worker/app/configured/H0 verification. No further package
source or test work was assigned by this acceptance.
Lead completed the new catalog paragraph/README/portal-guide writing pass;
the live grammar correction is outside the frozen worker snapshot and requires
no unchanged worker rerun. No H0 VM/full integration/flake-check run,
activation, credentials/login, model call, lifecycle action or merge is claimed.

## Documentation window

Lead confirmed the exclusive packaging/operator hunk window in
`docs/pi-runtime.md`. An exact prefix comparison at handoff proved its first
three P3 behavior sections/core-unavailable paragraph unchanged. Lead completed
the direct writing pass and transferred the full file, including this operator
hunk, into P3 commit `a74ae62…`; P7 must not stage it separately.
Lead also updated P3 core prose for the actual implementation and explicit
successor/power-loss limitations. README and portal-guide links remain P7-owned.
The text distinguishes immutable manifests from explicit machine auth/host-state
configuration and package/source checks from installed runtime readiness.
No activation instructions were executed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
