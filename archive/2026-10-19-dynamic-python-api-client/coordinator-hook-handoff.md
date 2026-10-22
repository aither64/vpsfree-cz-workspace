# Coordinator issue: Overcommit trust across merge-preparation revisions

Investigate and fix the generic `dev-workspace` merge coordinator. This handoff
covers the coordinator defect only, not the initiating project's implementation,
merge operation or session recovery.

## Later runtime flow

The selected runtime now provides repository/machine resource claims. Sessions
acquire ownership and execute their own ordinary Git/environment/hook commands;
the coordinator no longer creates new automatic checkouts for new work. Follow
`workspace-host coordination guide` from the currently selected package. The
failure below describes the retained executor path, not the new claim workflow.

## Defect

Merge preparation checks out a feature revision and then creates a historical
target worktree. Both linked worktrees share a common Git config. When their
Overcommit configurations differ, preparation cannot reliably finish:

1. The feature checkout hook requires trust for the feature configuration.
2. Historical target creation invokes its checkout hook, which requires a
   different configuration signature.
3. Signing the historical configuration replaces the feature signature.
4. Retry repeats the feature checkout and creates a fresh UUID target, so the
   already completed work cannot be resumed and the signature failures alternate.

Observed blocking message:

```text
Signature of configuration file has changed!
Run `overcommit --sign` once you've verified the configuration changes.
```

Ordinary signing and normal checkout-hook validation succeeded independently for
both clean revisions. The defect is the preparation sequence and shared trust
state, not a signing failure. It occurs before merge job submission.

## Confirmed constraints

Installed Overcommit 0.73.0 forces `git config --local` for configuration and
plugin signature reads/writes. It maintains one configuration signature rather
than a multi-version trust store.

Inspected sources:

- `lib/overcommit/configuration.rb:234,327`.
- `lib/overcommit/hook_signer.rb:70,105`.
- `lib/overcommit/configuration_loader.rb:55`: fixed repository `.overcommit.yml`
  plus optional `.overcommit-local.yml`; no alternate configuration CLI option.

Git 2.54 explicit local scope does not consult `config.worktree`; conditional
includes are disabled without `--includes`. Read-only probes confirmed these
limitations. `GIT_CONFIG` file override conflicts with forced `--local` (exit129).
A local configuration overlay does not pin the complete configuration and plugin
contents across revisions. Repeatedly alternating normal signatures cannot solve
preparation that restarts both stages.

## Runtime locations

Repository: `git@github.com:aither64/dev-workspace.git`.

Observed installed package:
`/nix/store/1i1g6rp8ind51qqayzpww7cn1xp1k1gq-dev-workspace-0.2.0`.
Recheck the selected package in the new session; these are investigation identities,
not instructions to modify an installed store path.

Primary source: `libexec/workspace-coordination-execution.rb`:

- `retain_commit`: installed line203 repeats the feature checkout.
- `prepare_merge`: installed line291 allocates a fresh target; line313 checks it out.
- Prepared hook environment handling and merge worker preflight.

Inspect the preparation entry point/retry caller to preserve a stable preparation
identity. Change `libexec/workspace-coordination.rb` validation only if new bound
metadata requires it. Relevant owning docs are the coordination and recovery
guides. The observed package lacked the `integration.md` referenced by its guides;
record that separately rather than inventing a recovery interface.

## Proposed direction, not an implemented fix

Make preparation resumable by exact stage with a stable target checkout:

- Preserve successful feature checkout/hook verification.
- Preserve successful historical checkout/hook verification.
- Stop at explicit operator trust checkpoints when required.
- Require final feature configuration/plugin trust before admitting mutation,
  without replaying the completed historical checkout afterward.
- Run ordinary required checkout, merge and push hooks; explicitly verify their
  failure behavior rather than assuming a successful Git exit proves every hook ran.

Bind checkpoints to owner/incarnation, repository/common Git directory, exact
feature and target baseline, clean trees, evidence and prepared hook environment.
Changed identities/content invalidate affected stages. Coordinate shared trust
access so another checkout cannot silently invalidate mutation preflight.

Do not disable signatures, bypass hooks, auto-sign unreviewed configuration,
manufacture trust hashes, edit operation ledgers or integrate through direct Git
around the coordinator. A new multi-version trust adapter is a larger alternative,
not an incidental workaround to implement alongside staged recovery.

## Verification and compatibility

Use disposable fixture repositories, independent of any existing blocked operation.
Reproduce differing old/new Overcommit configurations with signatures enabled.
Prove feature hook → historical hook → final feature trust → merge/push hooks.

Check interruption/retry after each stage, stable target reuse, preservation of
successful stages, retry of failed stages and absence of default-ref mutation
before complete preparation. Reject altered configuration/plugin bytes, baseline,
owner, evidence, environment, dirty trees, malformed checkpoints and stale trust
before mutation. Cover ordinary hook failures and unchanged-hook repositories.

Preserve existing completed snapshots/jobs and uncertain-effect recovery. Prefer
bounded additive preparation metadata; require explicit compatibility/capability
handling if older runtimes could misread partial preparation. Retain payloads needed
for recovery and follow forward package-selection recovery rules.

Implement in the new session's own worktree with its own verified identity and
normal project guidance. Run quick checks, independent review and focused integration
before selecting a new runtime package. Changes to shared runtime selection and
its default branch require the applicable explicit authorization. Existing sessions'
records, worktrees, trust configuration and paused operations are outside this
handoff's execution scope.
