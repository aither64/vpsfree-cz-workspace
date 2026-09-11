# Mandatory change review packet v35

## Outcome and exact boundaries

Review the final split and cutover contract:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently consumes the same exact generic
runtime for its privileged host module. Generic repositories contain no
case-insensitive `vpsfree` or `aitherdev` naming. Concrete site data is supplied
by consumers, the final package exposes only generic namespaces, and one exact
workspace commit is retained solely as the reversible compatibility bridge.

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `086e3d867140ab090e507a194b7fdfc1cc43cc65` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `c93ae3f258b9cdd8c4209b84c21e28a2c2bda4bc` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `204d78ac9c65483fa677ca3e47cb8204547b055a` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `580edfc14f3324274dbcce46c9f7ee95a624fa77` |

All source changes are committed and pushed, all five project worktrees are
clean, and `git diff --check` passes. Exact pins:

```text
workspace@204d78a -> vpsfreecz/dev-workspace@c93ae3f
  -> aither64/dev-workspace@086e3d8
  -> aither64/codex-web@c3200c4

configuration@580edfc -> aither64/dev-workspace@086e3d8
```

Compatibility source:
`4c7a5abf285b595f073d8333a3dbec5162b36d76`. The final workspace flake neither
constructs nor exports the bridge.

## v34 findings and remediation

- Authority JSON validation now has exact generic-runtime type and domain
  parity: integer schema, actual strings for tmux session/identity and Codex
  version, complete field sets, full supported `SAFE_PART` slug spelling and
  the existing size, path, identity and metadata constraints. The migration
  check consumes the generic runtime's shared valid/invalid fixture corpus.
- Every ready authority is correlated with exactly one captured live tmux
  session before a journal is written or a keeper handoff begins. The check
  binds the workspace socket, stable session ID, session name/slug, workspace
  and slug environment, managed-session marker, optional tmux identity and the
  complete Codex triple/pane. The separately frozen tmux preflight proves those
  recorded values still match the live server on retries and reverse.
- The live migration test now models a genuinely consistent managed session.
  Regressions reject a wrong valid socket, nonexistent session ID, renamed
  session, workspace metadata, tmux identity and Codex thread without creating
  the journal or moving state. Numeric and boolean JSON types and uppercase,
  underscore and long supported slugs are covered.
- Site configuration has one authoritative public validation boundary at
  `mkPackage`. The private tools constructor consumes normalized data and keeps
  only its independent generic authority-policy assertion. Malformed-input
  checks exercise the validator used by the public constructor.
- The durable plan now matches the runbook: build both generations, quiesce
  terminal sessions and stop old non-tmux services, install compatibility,
  stop services activation restarted, prohibit reconnects and lifecycle
  commands, run both preflights, freeze inventory, migrate both scopes,
  activate host configuration, then switch the profile to final.

The previous Scope advisory about direct lock traversal remains an explicit
decision: deployment inputs must be direct immutable GitHub refs, and a
`follows`/indirect topology must fail the gate until its proof is deliberately
updated. The 135 predecessor commits remain intentionally retained for source
provenance; the four current initiative commits own the new organization
behavior and each relevant boundary is independently valid.

## Compatibility and deployment assumptions

This is an intentional quiesced namespace cutover; mixed old/new processes are
unsupported. The migration preserves paths, bytes, metadata, profile
generations, tmux session/window identities, authorities, manifests,
credentials and TLS material. Durable partial operations are retryable. The
exact compatibility generation remains available until live acceptance.

No schema-4 journal has ever been deployed, so there is no predecessor journal
to upgrade. Rollback is allowed only while the journaled workspace, tmux and
host inventories remain frozen, and both locked reverse preflights must pass
before either scope mutates.

The user authorized aitherdev deployment, transient Codex-session restarts and
resetting development cluster state. Configuration deployment must use its
feature worktree. Default-branch integration remains a separate authorization
boundary: the registered shared workspace root requires an explicitly
authorized fast-forward before the alias-free package can be authoritative.

## Commit and API boundaries

- `codex-web`: client/security contracts, protocol compatibility, standalone
  example and CI are split by owning behavior.
- Generic `dev-workspace`: extraction, namespaces/runtime, host module,
  activation, tests/docs and CI are functional commits.
- Organization `dev-workspace`: retained provenance precedes four initiative
  commits for extension ownership, complete private migration, CI and complete
  public site validation. Migration commit
  `09711be9b787a49343b150dd8448599e9aa73cfb` owns the helper, private packaging,
  runbook and all migration tests at first introduction.
- Workspace: policy, site data, dependency selection, source removal,
  immutable bridge, final namespace and deployment checker are separate.
- Configuration: manual channel declaration, untouched `confctl` lock-only
  commit, and two aitherdev configuration commits remain distinct.

## Quick verification

- Generic: workspace-host `74` runs / `457` assertions; dev-session `285` runs
  / `2,852` assertions; focused Go command packages pass.
- Organization migration: `41` runs / `678` assertions at the exact rewritten
  head. Organization no-build flake evaluation passes every output.
- Workspace deployment checker: `2` runs / `9` assertions, live
  cross-worktree contract passes at generic `086e3d8`, and no-build flake
  evaluation passes.
- Configuration no-build evaluation, formatting and hooks passed; generated
  `.bin`/`.bundle` helpers are absent.
- Codex-web exact-head Actions `34512598834` is green. Generic exact-head run
  `34542903217` and organization exact-head run `34549692881` are in progress.
  Superseded organization runs accepted cancellation.

Long full checks, the NixOS VM, exact compatibility/final builds, aitherdev
configuration build and live cutover remain deferred until this remediation
review is clean.

## Review disposition and risk

Overall risk is **High**: public cross-project contracts, persisted user/root
state, credentials/TLS, systemd/tmux topology, destructive migration, rollback
ordering and host deployment change.

GitHub selected the organization feature branch as that new repository's
default. The current token cannot change it (HTTP 403). Neutral `master` exists
and all consumers pin an immutable revision; repository administration must
correct the default before normal integration.

The v34 fixes affect the migration authority boundary, journal schema, live
tmux inventory, path-domain support, package validation and durable plan. Rerun
General, Architecture, Scope and Risk with `gpt-5.6-sol` at `xhigh`.

## Non-goals and decisions

- Do not support mixed old/new runtime processes.
- Do not upgrade a never-deployed journal.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols or deployed vpsAdminOS nodes.
