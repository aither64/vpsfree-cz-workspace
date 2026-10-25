# Library lockfile removal: independent final review

**No Blocking, Important or Advisory findings.** General, architecture/repetition, scope/proportionality and risk/compatibility lanes pass for the committed deliverable. Full affected build/package acceptance remains a post-review gate.

## Binding and scope

Verified `dev-session current` against trusted session `2026-10-22-haveapi-release`, workspace `/home/aither/workspace/ai/vpsfree.cz`. Both identity environment variables are absent without conflict. Live roster revision34 confirms independent retained reviewer0, ready/review-purpose, actual saved/assigned **gpt-6.1-sol / xhigh / read_only**. No overrides, fallback, nested agents or substantive authorship.

Thread `01a16406-faaa-7cd0-bde3-c20802c18a72`; project `01a16406-fa76-7532-9ee4-a890352500df`.

Repository vpsfreecz/haveapi; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-library-lockfiles`; branch `2026-10-24-haveapi-library-lockfiles`.

Complete reviewed range **`7ac977a26080d45d44b6608aafad2cadd2ec7f81..1103a3a14b1dc6dec17fc4859df80220a54f111d`**, final tree **`32a09190e05a89f6312e07f20a9e4585335e468c`**. Head/tree match; source/index are clean.

Read mandatory-change-review, Shared Reviewer Instructions and all four full lane references; owning AGENTS and changed development/releases procedures; the complete lead/owner packets, accepted removal design, actual complete commit/diff, relevant build/CI/hook/package consumers, tests and docs. Reused unchanged applicable workspace procedures already read in this context. HIGH classification is appropriate for prepared input and retained-artifact verification spanning build/restoration/publication.

## Four-lane assessment

**General: actual removal follows the library/application policy.** The only three deletions are JS package-lock.json, Python uv.lock and Rust-generator Gemfile.lock. They are ignored local inputs. Private runtime Cargo.lock, highlighter package-lock.json and flake.lock remain tracked and byte-identical. Package manifests/constraints are unchanged.

Fresh preparation now uses native npm install, uv sync and ordinary Rust-component bundle install. Python CI prepares before its existing locked checks/integration, and caches from the tracked pyproject. Shared Ruby-server CI prepares JS with install rather than requiring a tracked npm lock. Existing JS CI already uses install; highlighter ci and Cargo --locked remain. PythonChecks still runs the same locked Ruff checks; only its now-untracked uv.lock trigger was removed. Ruff version validation remains intact.

**Architecture/repetition: source preflight and prepared inputs have distinct owners.** `utils/release/artifacts.rb:74` keeps authored version/dependency/changelog/clean/tag checks independent of absent local library locks. `check_inputs` at108 requires the three local inputs, preserves both npm identity/version checks and the existing Rust local identity/dependency checks. Python's native locked consumers continue to validate its resolution; this method does not claim a new complete Python dependency parser.

Makefile release-check/version, build.sh and write_manifest all route through check_inputs. Native resolution remains with package managers; there is no parallel resolver or new registry machinery. The nine-path catalog is shared by manifest writing and restoration validation.

**Risk/compatibility: original release inputs survive tools-only restoration.** `Artifacts#verify` validates the source/version/run/file-set/checksums, requires the exact nine nonempty retained lock texts and passes the original Rust lock explicitly into package inspection. It never needs a newly resolved checkout lock for this path. `inspect_rust` checks the original packaged lock bytes against that explicit evidence while retaining exact source payload, file-set, executable and Fiddle requirement checks.

The gemspec unconditionally includes Gemfile.lock as a required package file. It can be loaded before preparation, but ordinary RubyGems packaging fails without the file. This supports cold Bundler preparation/restored inspection without silently omitting provenance. Generator ownership still hashes its local/packaged lock; its format, generator/template/runtime algorithms and API are unchanged. Fiddle's test now accepts the actual prepared compatible version while requiring activation equality and a nondefault gem, retaining the lower-bound negative.

The source/version disposable test copies the actual three prepared locks and invokes real make version. It checks full Python parsed records/top-level metadata, exact Rust expected substitutions, npm external bytes/records and unchanged source/root/tool inputs. Cold-source and cold-restoration cases exercise the changed boundary; malformed/missing/conflicting evidence negatives retain refusal. The cold-restoration unit isolates real Rust package inspection while stubbing other package inspection; it is not a full restored release bundle campaign.

Library consumers retain manifest dependency ranges. Fresh compatible graphs can differ between independent builds, explicitly documented. No source-commit-only reproducibility is claimed. Existing downstream ff876 remains pinned to its exact090a source/input boundary; no downstream repin/regeneration or generated API change occurs here. Published/tagged source and accepted artifact bytes stay historical and use their original helpers. Publisher/RegistryQuery and upload/retry rules are byte-identical.

**Scope/proportionality: one coordinated removal is justified.** Preparation, validation relocation and packaging/restoration changes are required to avoid breaking fresh checkouts and retained-artifact recovery when deleting these locks. Supporting workflow, test and documentation edits belong to that same policy implementation. No unrelated dependency upgrade, bot policy, generation ban, new ownership format or fallback was added.

Docs place local preparation, retained provenance, fresh-resolution limits and generated-library/application distinctions in owning contributor/release/generation guidance. They distinguish a build's prepared lock from an installed consumer's complete execution bundle. Current docs do not claim tests or publication happened merely because commands are documented.

## Complete history, streams and migration conclusion

Independently verified the exact merge base and sole parent are7ac977a2. The complete range contains exactly one commit, `1103a3a14b1dc6dec17fc4859df80220a54f111d`, message “build: keep library dependency lockfiles local”. All24 paths match the packet. Its full message explains the library/application choice, preparation and retained artifact evidence. Maximum message width77 complies with repository80; normal hook72-column warnings remain qualified.

The one-purpose commit is coherent. **No obsolete iteration, superseded approach, fixup-only step or transitional compatibility path remains.** There are **no repeated dependency/channel/input/generated update streams**: this removes tracked library resolutions once, without adding replacement pins or regenerating outputs. No consolidation exception is needed. Earlier instruction commit7ac and supported090a/default history remain outside this rewrite.

**Migration inventory/conclusion: no migrations.** No DB/schema, seed, persisted-format, protocol/API-version or public-name conversion is introduced. Lock tracking changes build-input acquisition/provenance, not application stored state. There is no transitional migration version with merge/release/deployment/external-use provenance to retain.

## Evidence and remaining gates

Reviewer performed static read-only checks, not tests:

- Reconstructed actual complete binary/full-index diff: **ae326d5898c7303163462f9f7f531d43da282e2e9c9ae1d4c3b05f33f0f0e9eb**, identical to source.diff.
- Verified all changed live blobs equal committed blobs, exact head/tree/parent/single-commit scope and clean status.
- Independently confirmed three library deletions, unchanged three application/toolchain locks, unchanged JS/Python manifests, Rust generator/template/runtime trees and publication/registry code.
- Inspected retained owner command/raw results: release-check exit0/.862s; release-test exit0/16.915s,187 Ruby examples/0 plus6 Python tests/0; focused Rust dependency/package4/0. Normal PythonChecks/I18n/RuboCop and message hooks pass, with recorded72-column warnings. Original fixture-shadow failure, style finding, signature refusal and normal signing results are retained; no source oracle or hook bypass is introduced.

One ancillary read-only Git command accidentally used the tracking CWD and emitted workspace status/path output; it was discarded and repeated in the exact reviewed worktree. No mutation or unrelated source/log-content inspection resulted. This report relies on the corrected exact-worktree proof.

Remaining: one affected final-candidate build/test/package/smoke campaign with the actual newly prepared resolutions, full manifest's nine real lock texts, installed npm/Python and packaged Rust behavior, and real tools-only restoration verification. The manifest unit case uses actual three library locks and fixture text for six other locks; it is not evidence of an assembled release's nine real locks. Prior91 or67 artifacts/results cannot supply freshness for the changed resolution contract. Reuse prior compiler/MSRV checks only with exact relevant input proof; do not relax the historical fixed4dc0 comparator. Patch backport/versioning needs its own exact provenance/metadata checks before final readiness.

No tests/setup/build/compiler/listener/network/CI/integration or source/index/config/cache/session-file edits were performed. Reviewer is command-free. Lead owns report persistence/reconciliation, subsequent authorized routing and required gates. Review itself grants no integration/publication/deployment/lifecycle authority; session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
