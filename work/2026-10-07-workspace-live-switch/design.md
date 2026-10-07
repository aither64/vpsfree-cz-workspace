# Design and verification brief

The lead owns this design and the application edits. It implements the accepted
plan; substantial deviations return through the lead's account. Review scope is
high risk because this changes host package transitions and mixed generations.
The local operator is trusted; concurrency, state integrity, session identity,
remote-client authorization and forward recovery remain the boundaries.

## Transition decision

Resolve candidate Codex through the candidate package's bundled path, or the
existing explicit executable override. Compare canonical native executable,
launch policy, complete argv and native capacity from immutable runtime markers.
Catalog digest and package provenance are validated but do not require restart.
No version-string-only matching and no synthetic rewritten launch record.

Both selected predecessor and candidate publish livePackageSwitchPolicy 1 before
preserving running services. A predecessor without that contract takes one idle
restart cutover, including when the native tuple is unchanged. Recheck policy
and launch compatibility during candidate activation/reconciliation. Unknown
markers or launch mismatch take the conservative restart path.

Use the same decision throughout switch and reconciliation. The switch retains
the exclusive transition lock, lifecycle/creation preflight, cluster adoption,
authority compatibility, retention roots and pending forward retry evidence.
The live path does not quiesce, respawn or sync managed terminal clients.

## Member reporting and catalog

Pass the exact configured host-profile path through team CLI/browser services
into member MCP bindings. The report helper invokes profile/bin/dev-session for
each report, without resolving that path permanently to a package. Its fixed
workspace, slug, sender, lead and member identity checks and stable report IDs
stay intact. Custom profiles must work. The first idle restart retires old
helper processes; later member-turn policy binds the new helper. Retained
rosters keep model, effort, access and instruction snapshots; new selections
validate against the installed catalog. No roster migration or automatic edits.

## Interfaces and compatibility

Add an internal host-profile argument to team commands/bindings and an additive
runtime contract capability. Keep registration/pending payload schemas and
existing digest provenance intact. New runtime understands old markers and
requires conservative restart where launch/policy evidence is unavailable.
Forward-only package selection and recovery remain unchanged. Preserve old GC
roots; no DB migrations, daemon wire changes or coordinated fleet upgrades.

## Acceptance and checks

Focused Ruby tests cover busy live switch, same catalog and changed catalog,
native executable/argv/capacity/policy mismatch, absent/malformed markers,
unsupported bootstrap, custom profile, failed activation and forward retry.
Go tests cover report binding/stable dispatcher across generations and preserved
roster/catalog selection. Keep hook validation in the declared Nix environment.

After all code/docs/pins are committed and quick checks pass, independent review
covers general, architecture/repetition, scope/proportionality and risk/
compatibility lanes and complete base-to-head history with no migrations.
Then packaged checks and an isolated exact-binary fixture preserve running lead
and member across portal reconnect, queued work, pending questions/approvals and
exactly-once reporting. Deployment separately proves host/application identities
and a second live compatible switch. Do not mutate unrelated live sessions for
verification or interrupt threads to force the initial cutover.
