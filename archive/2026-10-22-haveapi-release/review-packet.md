# Final committed-deliverable review

## Outcome, scope and acceptance

Prepare HaveAPI 0.30.0 with rewritten JavaScript clients, Python client and Rust
client generator. Include Rust in the existing shared-version release contract:
metadata/dependency locks, dependency setup, component tests, gem construction,
payload inspection, manifest provenance, isolated extracted-gem smoke,
registry preflight/upload/retry/final completion and truthful release docs.
Preserve the three fixes already released in v0.29.12 but absent from master.

No registry upload, tag, official release-branch creation, GitHub release
publication, default integration or production deployment is authorized here.
Do not expand into unrelated runtime redesign or downstream crate regeneration.

Session `2026-10-22-haveapi-release`, workspace `/home/aither/workspace/ai/vpsfree.cz`.
Plan, state, design, registry-readiness, metadata-preparation and
publication-preparation files are in this same directory. Full series/messages:
[final-series.txt](final-series.txt); full final diff: [final.diff](final.diff).

## Repository and complete committed inventory

- Repository `vpsfreecz/haveapi`, target `master` (no integration approval).
- Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Feature `2026-10-22-haveapi-release`.
- Base `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
- Current head `08345b2d5ede025972a3daec8b4a373efb51d711`; original reviewed candidate
  `09024e01251a1334780b73f14218266e94706192` differs only in final commit message.

Complete base-to-head series:

1. `70180e6fb290a59d49ce804bc3ac8417a3276f0a`: shared Rust release integration.
2. `c305117fc50274fc9b14e881dd0ba485f9542735`: released structured-example validation.
3. `19730572d3a15d7d031bc87cac02bfe415ade784`: released generated-example syntax.
4. `62cb54e4a6c32b65b9d127334b26f0d73765d433`: released nested PHP example values.
5. `db91afadea891520b08d5df47c8ea14fc1ba57bb`: publication specs/docs/Rust filters.
6. `67dd584d3d0a11b132a1f6e754137de675f48001`: independent PyPA v1.14.3 update.
7. `08345b2d5ede025972a3daec8b4a373efb51d711`: `Version 0.30.0`, coherent metadata/changelog.

Source fixups were folded into their owning commit, source dependency order
corrected and the fresh-checkout doc prerequisite folded into publication docs.
No obsolete fixup commits remain. Verify whole-branch history independently.
Fresh target/tree-equivalence receipt will be linked at assignment.

The three maintenance commits preserve supported released behavior. They map to
v0.29.12 commits 9b53aa87aec7a8d9c61eee2716e5520b3ecf743c,
fda2e33d32c249310812730b6b3096b99778918d and
f82ca890683d518496fdb57dc1c040589a0d585b; their original-source and maintenance
-x footers remain. Exact example-source files match released content; the flake
retains both root Rust tools and released Node/PHP server-shell additions.

No database migrations, schema changes or persisted-state conversions. One
shared-version update stream includes generated npm/Python/Rust locks; registry
dependency versions/checksums were preserved. One PyPA dependency update. No
intermediate pin or channel streams retained. Assess this conclusion explicitly.
Separate publication tests/docs, source tooling, released behavior preservation,
action dependency and version metadata are independently reviewable purposes.

## Risk, reviewer and lanes

High risk: non-atomic, irreversible multi-registry publication, OIDC identity,
first-publication ordering and exact retained-artifact/recovery contracts.
Review all lanes: General; Architecture and repetition; Scope and proportionality;
Risk and compatibility. Read the mandatory-change-review skill and every selected
reference. Reviewer0 is retained independent gpt-6.1-sol/xhigh, read-only; verify
saved identity/settings at assignment. No nested reviewers/agents.

## Owning contracts and consumers

`HaveAPI::Release::GEMS` owns gem names and order. Artifacts/manifests and
Publisher preflight/upload/completion consume it. Destinations are RubyGems
haveapi-client, haveapi, haveapi-go-client, haveapi-rust-client; npm haveapi-client;
PyPI haveapi-client; PHP mirror vpsfreecz/haveapi-client-php for Packagist
haveapi/client. Ruby client must publish before its dependent gems. No duplicate
Rust-specific publisher catalog or new registry credential was introduced.

Preserve retained artifact bytes/checksums and same-run reuse, all-destination
preflight-before-write, conflict refusal, no rebuild after approval and partial
failure recovery. Source/tag correction requires a new version. New root Rust
commands and component shell isolate Bundler state and exclude user gem cache.
The build reuses Makefile release-rust; smoke loads the extracted generator and
verifies offline generation/runtime copies without checkout generator fallback.

JS remains one package/bundle; Client === CallbackClient, AsyncClient opt-in.
Python 3.11+; generated Rust 1.95+/edition 2024 and exact configured formatter.
Generator embeds Rust runtime source; private Cargo harness is not published.
Generated clients have independent snapshots/versions and no HaveAPI crate
runtime dependency. Existing protocol 2 support remains; no downstream pin or
production deployment. Do not infer new clients are API-identical to Ruby.

## Documentation and quick evidence

Changed docs: CHANGELOG.md; doc/agent-instructions/development.md and releases.md;
clients/rust/docs/releasing.md. Lead applied required user-facing-writing skill
after factual acceptance. Source docs own repeatable operations/compatibility;
this directory owns temporary registry/release evidence. Reusable observed setup
failure is recorded in notes/haveapi/2026-10-22-rust-bundle-isolation.md.

Quick checks passed in declared Nix environments: 78 release-tool examples,
six Python artifact tests, 28 generator units, 19 launcher contracts, 12 focused
server examples; release-check includes Rust; required Overcommit/style/syntax.
Version regression verifies local-only shared-version lock updates and preserves
the ignored root lock. Setup checks exposed and corrected inherited Bundler lock
and user-cache leakage; no tracked metadata was damaged. Actual artifact smoke
and full build/suites run after final review. No long integration run yet.

Official action checks and PyPA security/compatibility evidence are in
publication-preparation.md. Workflow's two Rust path filters address a concrete
missing build-only trigger; PyPA v1.14.3 is SHA-pinned separately. Other actions
were verified current. Registry account configuration remains unverified.

## Related downstream source context

Read-only receipt vpsadmin-rust-client-readiness.md identifies existing
vpsfreecz/vpsadmin-rust-client/main 945af6a97717a7a6373507bbc9592d5cd53727c2,
actual crate vpsadmin-client 0.1.0. Its embedded runtime and source-pinned generator
mean no dependency on publishing HaveAPI 0.30. No downstream branch/code changed.
Exact-head CI 39739951412/39600821857 is green. Protected release environment is
absent; no tag/release/secret setup. Historic independent-review certification
was unavailable in permitted source evidence. This packet does not claim the
whole crate independently reviewed. Inspect its release contract as needed for
HaveAPI consumer/registry context, without substituting unrelated crate review.

Return findings by severity with paths/commits and explicit whole-series history,
repeated-stream and migration conclusions (including no migrations). Remain
read-only. Do not run publishing helpers or long integration/builds.

Lead pre-assignment inspection confirms HEAD is the exact packet head, tracked
working tree/index are clean, origin/master is the packet base, and pre-reorder
123364c and final 09024e0 tree objects are identical:
`3bd9df27413a1794bad5d8db27faca551cc3f79a`. Final head reordering changed history,
not the intended tree. Implementer final receipt/fresh-fetch proof will follow
without authorizing any source mutation during review.

Final implementer evidence is complete: [package0-receipt.md](package0-receipt.md)
with fresh SSH fetch and ls-remote proof, exact tree equality/range-diff,
configured hooks and final release-check passing, preserved released-source
comparison, full quick evidence and proposed post-review batch. No owned
command, watcher, Git or hook operation remains; authors yielded source/Git
ownership read-only for review. Known generated __pycache__ is not an intended
deliverable. Capture-comparison saved the exact range.

## User-requested final commit message amendment

The user explicitly requested exact final message `Version 0.30.0` during review.
Old head `09024e01251a1334780b73f14218266e94706192` became
`08345b2d5ede025972a3daec8b4a373efb51d711`. Same parent
`67dd584d3d0a11b132a1f6e754137de675f48001`; both trees
`3bd9df27413a1794bad5d8db27faca551cc3f79a`, empty old/new diff.
Lead independently verified current HEAD, parent, exact one-line message and tree.
All declared precommit/commit-message hooks passed; no source change/test rerun.
Final series file refreshed and comparison recaptured. Bind the completed review
to both ranges under this message-only equivalence; no source lane restart needed.
