---
lifecycle: archived
---

# HaveAPI 0.32 and generated vpsAdmin client releases

## Result

Released and verified HaveAPI **0.32.0**, vpsAdmin Go client **v0.1.0**, and
vpsAdmin TypeScript client **0.2.0**. All four changed source branches are
merged into their approved remote defaults. Clean public Go and TypeScript
consumer installs/checks passed. Rust remains **0.1.0**: all 686 generated
Rust/runtime files are byte-identical to its published release.

No remaining implementation, review, CI, publication, consumer check or resource
ownership. The session stays open; no archive/delete/stop or branch removal
was requested or performed. Only four disposable detached merge targets were
removed through ordinary Git worktree cleanup after verified integration;
feature worktrees and refs remain. No fleet/application deployment occurred.

## Phase checklist

- [x] Verify exact session identity and retained team/access/settings.
- [x] Design, initial plan/state checkpoint, scope and compatibility assessment.
- [x] Implement release metadata; regenerate Go, Rust and TypeScript.
- [x] Commit all deliverables; pass hooks/quick checks and independent reviews.
- [x] Resolve Go ImportantG1 through requested narrow compatibility documentation.
- [x] Pass exact-head longer checks, package validation and required CI.
- [x] Obtain explicit four-target integration/publication authorization.
- [x] Integrate approved defaults, push and prove exact final ancestry.
- [x] Publish HaveAPI across all maintained destinations and verify Packagist.
- [x] Publish Go v0.1.0 and TypeScript 0.2.0 after HaveAPI completion.
- [x] Verify actual public consumer downloads, hashes, imports/types and builds.
- [x] Release all merge claims, remove only temporary Git merge targets, retain
  feature refs/worktrees and leave the session open.

## Exact source and publication identities

All feature branches are `2026-10-30-haveapi-client-releases`; worktrees remain
under `worktrees/2026-10-30-haveapi-client-releases/`. Final comparison captures
and repository registrations are in runtime-maintained `portal.yml`.

| Repository / target | Exact final feature head | Publication |
| --- | --- | --- |
| haveapi / master | `0e7166a0f8f15827bfac051666a53bf449e999ec` | haveapi-0.32 and annotated v0.32.0 |
| vpsadmin-go-client / master | `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` | annotated v0.1.0 |
| vpsadmin-rust-client / main | `1ab58627a225589fefc983829de5c4cfee770b3b` | no new crate/version/tag |
| vpsadmin-typescript-client / main | `e5786f69b7c223c3bb5b1de99b7f97186eec368a` | annotated v0.2.0; npm 0.2.0 |
| vpsadmin / master, source only | `bcfa95eb136c50d25024f53a6b1af557d1173d56` | no source changes/release |

Fresh final-ref evidence proves every registered exact feature head is an
ancestor of its current remote default and every feature worktree is clean.
VpsAdmin default advanced to ac10a62f through dependency locks/generated Nix
metadata only; its API declarations are unchanged and selected bcfa remains
an ancestor. Frozen schema inputs were not silently refreshed or relabelled.
Raw evidence: integration/final-ref-checks.json.

Tag objects: HaveAPI v0.32.0 `e78e4b398819a82961cabb7c7ceea59c773c6a64`;
Go v0.1.0 `54a265db8d133cfebd58fb27a38dfdd5e5bba279`;
TS v0.2.0 `1b645b2190261268c566ed81c85543f4e51e6b55`.
Each peels to its exact integrated head above. No published tag moved.

## Authorization and integration

Initial `proceed` authorized implementation. After the concrete four-target
merge/publication question and TypeScript formatter/Go compatibility discussion,
user said **"that's ok. proceed."** Lead confirmed merges of haveapi/master,
Go/master, Rust/main and TypeScript/main plus HaveAPI0.32, Go0.1 and TS0.2
publication. This is the separate integration/publication authorization; no
lifecycle, unrelated feature or deployment authorization is inferred.

Each repository was prepared outside ownership and integrated fast-forward-only
with required hooks, normal SSH push and fresh remote proof under one short
claim. Claims were explicitly released and verified before CI/records/cleanup:

- HaveAPI: `5c252269-732c-423a-a252-0c229be4444e`.
- Go: `8e1f9dc9-8d0c-410b-a469-bb86b763129d`.
- Rust: `c493717c-de0f-4078-befc-d5107329e6cf`.
- TypeScript: `afeb4249-2913-4e0a-8cdd-cfbd81f8802e` (queued then granted;
  authoritative held status checked before mutation).

All target bases stayed unchanged, so no merge rebase was required. Go's narrow
G1 docs fix preserved generated source and its reviewed old/new ranges. TS's
provider rebind and final0.2 metadata range were independently reviewed.

## Independent review and decisions

Retained reviewer0, gpt-6.1-sol/xhigh/read_only, independently reviewed complete
committed histories/diffs, update streams and migration provenance. Saved
settings preserved; no fallback. All reports explicitly conclude no obsolete
history/repeated update streams and **no migrations**.

- HaveAPI high risk/all four lanes: [original review](haveapi-final-review-result.md)
  plus [CI follow-up](haveapi-ci-followup-review-result.md), no findings.
- Go high risk/all four lanes: [review and G1 remediation](go-final-review-result.md).
  ImportantG1 accepted/fixed through the requested narrow docs remedy: inherited
  Custom inputs are omitted by the generator; affected typed calls and the
  low-level complete-body request method are explicit. Lead inspected exact
  docs-only fix under narrow-fix rule. Source-breaking field/obsolete exported
  binding changes are documented. No unresolved finding.
- Rust medium risk/all four lanes: [final review](rust-final-review-result.md),
  no findings; 686 files independently equal base and actual published archive.
  Original divergent v0.1.0 source/recovery remains intact and is not described
  as literally merged into current main.
- TS: [original review](typescript-final-review-result.md),
  [provider-pin correspondence](typescript-final-correspondence-review-result.md),
  and [0.2 affected final review](typescript-0.2-final-review-result.md), no findings.
  User clarified that formatter changes qualify for the requested minor release;
  the initial semantic-only no-release decision is historical/superseded. All
  674 generated files equal the exact formatter transformation of0.1.1, with
  unchanged API/public types/runtime. Peer runtime stays exactly0.30.2.

Architect0 owns [design](design.md); lead owns [plan](plan.md), acceptance, prose,
records and approved operations. Implementer0 owns HaveAPI/Go, implementer1
schema/consumer checks, implementer2 Rust, implementer3 TypeScript. Fresh pinned
Luna/low utilities launched/monitored long or uncertain checks. Lead directly
applied the required writing skills to all release/README/development prose.

## Release verification

[HaveAPI release proof](release-verification.md): tagged run
[41056909572](https://github.com/vpsfreecz/haveapi/actions/runs/41056909572), source0e7166,
new artifact12977097967, manifestSHA256
`0fa2c61cc13a9b80f67f5d18eb7a23681851fe9e869c760040fe8a2cf1dfdfc8`.
All11payloads, ten dependency graphs and SDK source/runtime/formatter/lock inputs
match accepted source. Lead approved environment24722193856, deployment7438557678.
Publish job124068866573 succeeded12:51:21Z. All five RubyGems, npm tarball/browser
bundle, both PyPI files and public GitHub12assets match original tagged files.
No build-only artifact substituted, rebuild or accepted-upload retry occurred.

PHP master/v0.32.0 commit `d0d51d09ada7beb863d2cd726ca446504312579a`, tag object
`7c56769028abc9ea3f32f0e9003bdb69399c4055`; exact HaveAPI-Source0e7166. Full36file
blob/executable-mode tree matches retained PHP tar, treec5ea7301b278b43be7a67d14cb9225082295c6d5.
Packagist0.32.0 indexes the same commit. No uncertain/partial destination remains.

[TS release proof](typescript-release-verification.md): tagged run
[41059048868](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41059048868),
sourcee5786f69, original artifact12978397388. Lead approved environment25494232596,
deployment7438799627; publish job124074200061 succeeded. Public npm0.2 verified
13:05:31Z, exact public tarball byte-identical to approved tagged archive,
SHA256`36e699738830303fe8e1d76d102eacda025653dc75c07ce88d65a134c6ff3e3b`;
SHA512/SHA1 and source/tag/runtime/source-pin proof match. OIDC provenance public.
Initial public404 was processing delay; no reupload/retry/retag. Existing-account
restricted-tag creation bypass was server-reported; no rule configuration changed.

Preparation/check details: [HaveAPI](haveapi-preparation.md), [Go](go-preparation.md),
[Rust](rust-preparation.md), [TypeScript](typescript-preparation.md). These retain
exact quick/CI versions, base/head history, locks and artifact IDs. Final provider
full suite and packaged/extracted generator smokes passed. Rust exact-head CI
41051018591 passed default/blocking, MSRV1.95, docs/package and frozen generation;
local package-list gate passed697paths without changing Cargo.lock. No duplicate
real-server tests were needed for byte-identical Rust runtime.

## Actual published consumer checks

[Complete evidence](published-consumers.md); both batches ran once in clean owned
consumer caches without source replacements, private exemptions or API calls.

- Go public proxy/SumDB v0.1.0: Origin hash134a9e69/refv0.1.0 and all687downloaded
  files equal approved commit. modverify and representative constructor/language/
  header/VPS consumer build passed with Go1.26.8. ModuleSum
  `h1:lk18YreP1ygPjeVxchcsYVlyAPbKjxV4GJqYi8emlUM=`; GoModSum
  `h1:n7aZvL8Z1XGeKF6lDkdmsfGdBOh8SiKxl07FXjpGygw=`. Go1.16.15 floor
  compilation also passed during preparation. Binary was not executed.
- Public npm0.2.0 install with scripts disabled: registry integrity, downloaded
  bytes, installed lock and original tag receipt match; actual peer0.30.2 and
  source pin0e7166 verified. TS6.0.3 strict NodeNext/ES2022 typecheck plus actual
  ESM imports/facade construction passed, no authentication/actions/API requests.
  Source commit is proved by tagged receipt and byte equality, not an invented
  registry gitHead (registry does not provide one). Final batch exit0/~25.9s.

## Inputs, recovery and retention

[Schema evidence](schema-preparation.md):14 safety/snapshot specs and repeat
isolated full-fixture exports pass. TS canonical schema
`476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`, all six
plugins,151/519 application resources/actions. Go/Rust public capture hash
`70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`,151/519
application plus1/5auth. Profiles remain distinct. Capture truthfully records
f0465630; final generation/publication uses independently equivalent0e7166.
Old/new ranges, source/formatter/lock equivalence and original artifacts retained.

Initial Ruby3.2.0/Ubuntu26 CI provisioning failure was fixed with two reviewed
latest3.2patch selectors, preserving declared floor and effective inputs. Native
coordination CLI/project Ruby gem conflict failed before acquisition and was
resolved only at the subprocess environment boundary; see reusable
[lesson](../../notes/cross-project/2026-10-30-project-ruby-env-native-session-cli.md).
A TS quick-check watcher repeated a successful command while attempting log
repair; interrupted duplicate reconciled without source change, actual first
success retained and independent final tag CI passed. No uncertainty remains.

Feature refs/worktrees and raw accepted artifacts/receipts remain. Raw logs and
supporting archives are ignored/disposable; public release assets and compact
Markdown receipts retain durable identities. Ordinary temporary merge targets
removed after resource release; no session lifecycle helper invoked. No machine
reservation, deployment, cluster, pending worker or review/approval remains.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
