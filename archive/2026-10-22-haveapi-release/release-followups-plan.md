# Post-0.30.0 development follow-ups

The user requested fixes for PyPI/RubyGems publication confirmation and the full
original tagged build output (job `120072628557`, run `39849807897`), including
`rimraf@2.7.1`, `inflight@1.0.6`, `glob@7.2.3` deprecations and Rollup's rewritten
top-level `this` in TypeScript output. The user explicitly requires these changes
to stay in a development branch, with no further release without approval.

First finish the already authorized 0.30.0 recovery using its original immutable
tag/artifact. Investigation/design may proceed independently; application edits
start after that release is resolved. Do not move or amend a released commit.

Planned branch `2026-10-22-haveapi-release-followups`, based on integrated master
`b64fb25bea8d8222fb3263b99956c0b61438a859` unless a freshly verified master has
advanced. A separate registered HaveAPI worktree keeps original release artifacts
and refs intact. No new version, default integration, release branch/tag or
publication is authorized for this follow-up.

| Owner | Expected result | Acceptance / dependency |
| --- | --- | --- |
| architect0 | Full build-output diagnosis and bounded package design | release-followups-design.md + link from design.md; actual dependency/warning origins and publication evidence; no source edits |
| implementer0 | Serialized new development worktree/Git setup and later commits | Separate registered branch, declared hooks, exact-path commits, original release tree/artifacts untouched; after lead grant |
| assigned implementer | Registry confirmation fixes | Bounded transient handling/diagnostics, strict hashes/identity/conflict behavior and original-artifact recovery preserved; after design acceptance and release resolution |
| assigned implementer | JS dependency/code-generation warning fixes | Resolve actual warnings without blanket suppression; preserve public browser/Node/types/runtime compatibility; after design acceptance and release resolution |
| lead | User-facing prose, scope acceptance and coordination | Explain changes/results and retain explicit no-release boundary |
| reviewer0 | Independent committed final review | Complete base-to-head history/final diff/migrations and applicable lanes after quick checks; before long acceptance |
| fresh utility | Longer verification and CI observation | Exact development head, no publication/retries/approval authority |

Read owning repository instructions before edits. Preserve known supported paths,
keep authored/generated/dependency purposes reviewable, consolidate fixups before
final review and state no migrations when the inventory is empty. Use an explicit
compatibility assessment; do not hide the warnings with broad log filtering or
weaken publication conflict checks. Full commands/logs belong in session evidence;
lasting behavior/recovery guidance stays in the repository documentation.
