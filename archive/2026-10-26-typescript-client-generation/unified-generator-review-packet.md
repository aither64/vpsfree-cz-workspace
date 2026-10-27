# Final affected review packet — unified generators and TypeScript examples

Status: final committed deliverable, quick checks pass; ready for mandatory independent final review. No advisory/early review requested.

## User outcome and boundaries

Implement the accepted plan: all three Go/Rust/TypeScript generators can fetch/save a schema and generate offline; generic user READMEs show capture before generation; vpsAdmin-specific steps live in its client README. Root README distinguishes dynamic JS/TS discovery client (`clients/js`) and TypeScript saved-schema generator. Add generated-TypeScript Ruby server examples like Go/Rust. User explicitly selected public/Basic/existing-token capture. No describe/inspection command requested.

No production API calls, new transport/runtime, token login/renewal/OAuth, Go ownership framework, schema/DB export repeat, release/version bump, source registry/factory settings, default integration, deployment or lifecycle action. Package stays private. Shared format1 source bytes and application operations remain fixed.

## Repositories and history

Verified session `2026-10-26-typescript-client-generation`, workspace `/home/aither/workspace/ai/vpsfree.cz`, own worktrees under `worktrees/<slug>`. Sources committed and quick checks required before assignment.

HaveAPI base/master `029f79b31cec93167f07e43e571c36b5f42d5b80`, final head `e6d4f797fc92090fff265585196970e6b017003f`, tree `fb854bfe0b0fdd00cedec7ecb7e56de38e8e2efd`:
1. `23fb16ec7c693ada6c04528e102fa64538c408b9` — shared schema/capture and Rust facade/source closure.
2. `6a532e4a25947e4f065a77e50dc312146c21dd07` — common Go/Rust CLI and generic guides, preserves supported legacy Go invocation.
3. `4916b44ae030788a53c0514d05642ff97540116a` — complete modular TypeScript generator with common facade/CLI/deps/digest and root entry/docs.
4. `e6d4f797fc92090fff265585196970e6b017003f` — generator-owned TS Documentation adapter plus optional server profile/renderer, fixtures/docs/registration.

Earlier reviewed range `029f79b..fae5508aca9def6b1388d298aab898b0b9ce832c` comprised parser `e40e0595` + emitter/docs `fae5508a`. Those unmerged original commits are consolidated into the complete TS generator; final series directly introduces final shared-schema/module design. Old publication refs/reviews are retained as provenance, not obsolete feature history. `before-unified` retains fae5508a and `before-consolidation` retains exact complete pre-rebase tree at e99891f6. No supported release/deployment/external-consumer state requires intermediates. Capture helpers and server bridge are separate reviewable functional boundaries; adapter+server profile together make one usable documentation feature. Tests/docs/build hunks follow their owner. Lead independently checked all854 tracked modes/bytes/symlinks against approved source; only approved harness puts->$stdout.puts lint correction differs, independently reversed in memory to verify original hash. Final tree equals preconsolidation tree. Ordinary hooks ran each final4. Full diff76files4976+/496-, current affected fae..final54paths.

Downstream vpsadmin-typescript-client base genuine emptyroot `6c67b3c6e10e4096f6717345026371a89691f62a`; final head `50a9602cbc30ca0c18ace092ad9750439e9cf82a`, tree `301d22460ac3810d7cfda951898163db1c1f3022`. One coherent initial package commit, no scaffold/flat predecessor/pin update stream. Previous published7bc0f83 remains evidence. Driver now explicitly selects both verified Ruby+TS library paths, validates actual loaded features/source location, dirty/untracked shared inputs and exact shared identity, plus source-refusal tests. Lead independently compared committed tree inventories: all674 generated TS mode/blob entries and protected schema/provenance/exporter lock/package/npm/flake/srcindex inputs are identical; parsed manifest differs only at generator_source_sha256. Final schema/provenance/locks and all674 generated TS modules are byte-identical. Compared with published7bc0f83, exactly six paths change (151+/15-): service README, tools/regenerate, newtools/generator-source.rb, newtest/regeneration/sources.test.mjs, tools/generator.json, and generatedownershipmanifest. Manifest dictionary differs only at generator_source_sha256; newmanifestSHA256 `8f42cf24dc661c90799c0da89b8a00e719c09b0fe61ee2eb374f5e120edc7a09`. Provider/source/driver identities are honest final inputs, not manual relabeling.

Unchanged vpsAdmin base `898e2881e8230d24fb06baee1c58737ae55e0009`, head `7456c7eaae11cee0c76a984b1386a94656510f88`, prior review retained. Existing integration run40330622527 finished success at exacthead. No new exporter/DB work.

No migrations or new persisted state in any final feature range. Generated action names migrate/migration_plan do not constitute migrations. No feature migration merged/released/deployed/externally consumed boundary. Review must explicitly assess COMPLETE 4/1/1 history, repeated update consolidation and migration lineage.

## Public and shared contracts

Shared owner `clients/ruby/lib/haveapi/schema{.rb,/**}` (`HaveAPI::Schema`) stdlib offline loader + lazy HTTP, Ruby>=3.0. Shared Snapshot format1 sevenkeys/canonical bytes/strong contextual endpoint checks; Rust/TS Snapshot facades preserve helpers/native errors. Rust saved-load endpoint strengthening is documented intentional behavior; relative manifest segment helper remains supported after focused fix.

Common CLI: fetch URL --api-version V --profile LABEL --output FILE; mutually exclusive basic-user/basic-password-env or token-env, no credentials in saved output/diagnostic exception chains. Existing token only, anonymous discovery and token request at same exact mounted versionURL, validates advertised header, no redirects/retries/token actions. Atomic save preserves existing output on failure. All3 generate --schema/--api-version/--output offline. Rust config/Go module/package/Rust+TScheck remain language-specific. Go old URL+destination/default-version/rawBasic supported; new saved description uses existing symbol-key model/emitter.

Shared identity haveapi-client0.30.0 SHA256 `caf98b1e2e9a17f26eaae012fbb56808429f47083aac02d08305cd264aee5cc6`; TS generator digest `646b996c90cd1fffead13badadcc4ae1520e95c9fd4191c9ca352e9de48d8bcf`; VERSION bytes `42659901f3c792eb230cf32b2c844ae738cd6d53dd84c1b7eb434e969b472ec2` unchanged. Real saved schema3.6MB oldTS/oldRust/shared load+capture canonical bytes identical SHA256 `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`.

TS profile: typescript package_name + optional package_version/snapshot_path/generator_version, public createClient root (already reexported by own client), rendered label TypeScript(generated)/idtypescript-generated. Existing dynamic tabs unchanged. Full frozen private mount-time IR uses server StructuralSchema stripping ALL defaults; authorized request Context/sample controls render. Stale/unsupported sample limitation, optional dependency startup validation/atomic failure, no render-time files/generation/network/compiler. Publicruntime0.30.2 executes versionedbase, Basic/existingtoken; no generated auth endpoints or retry/completion policy. Ownership source/package boundary unchanged.

## Verification and documentation

Quick checks: commoncore20/0 + actualRubyTokenheaderpolicy; TS45/0 including eight actualrenderedstrictsnippets; Go68/0 actualCLI/directemitterbyteparity with go_fmt/no-discovery; Rust151/0 after diagnosed safe_segments fix; selected releasecontract11/0; serverfocused43/0; generateddoctarget18/0. Scoped24file + coreRuby3.0 + adapter/server lint allgreen, normalhooks eachfinal4. ComponentGo68/0 reconfirmed freshpolicyLuna43s with actualdeclared json3.1.0. Prior failures/dependency races were diagnosed and corrected, no blindCIrerun.

Complete downstream construction PASS38s via freshLuna: regenerate+--check, new exact-source/dirty-version/untracked/preload refusal test1/0, build, strict typecheck and consumer typecheck, four local client tests. No operation active, no repeated unchanged checks. Allworktrees/indexes clean, ordinary hooks/commit messages passed; no sourcewrites currently authorized during review.

Directleadwritingpass: all3genericREADMEs/rootREADME, development guide, clients/typescript/docs/documentation.md, serverdoc/client-examples.md+visibleviewparagraph, downstreamREADME acquisition/driverparagraph. Commands/local links/fixtures checked. Genericdocs no vpsAdmin instructions; serviceREADME contains actual exportercommands without execution. Existing full modular-source review preserved in modular-output-review.md and readme-review.md for unaffected original parser/emitter/exporter. Source emitter/templates/IR/naming unchanged vs fae5508a.

Long postreview tests NOT launched: realCapture/FetchCommand root+mounted loopback Public/Basic/token/failurepreservation; actualrendered14snippets22requests using published0.30.2 root+mounted auth/requests/errors; real extracted Ruby+Rust gems consumer; extracted npm archive consumer. No production/DB/rebenchmark. FinalbranchCI comes after publication, prior CI only certifies its exactheads.

## Requested independent review

High risk (authenticated capture, reusable schema/generated APIs, authorization-sensitive examples and output ownership). Retained reviewer0: gpt-6.1-sol/xhigh/read_only, independent of implementation; settings unchanged, no fallback. Read mandatory-change-review SKILL and allfour references (general, architecture/repetition, scope/proportionality, risk/compatibility), applicable workspace/repo instructions. Review committed finaldeliverable directly; no source/record edits, tests/builds/CI/fetch/push or nested agents. General review includes user-facing documentation and complete branch history; assess shared provider/actual consumers/pins/source closure. Report findings by severity and explicit wholehistory/repeatedstreams/migration conclusions; source review cannot certify deferredruntime/archive checks. Keep bounded affected review; unaffected earlier conclusions may be retained when inputs proven unchanged. Lead persists verbatim report as unified-generator-review.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
