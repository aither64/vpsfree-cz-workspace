# Sensitive session archive exclusion fix

Architect: architect0. Design accepted by lead for workspace-only implementation
on 2026-10-31. No application edits, target-session changes or archive retry were
performed during investigation.

## Cause and evidence

The archive worker failed before publishing a lifecycle journal because the
workspace's `.gitignore` overrides the sensitive session's local Git exclusions.
The runtime's refusal is correct.

- The authorized target's retained portal receipt reports `state: failed`,
  `phase: starting`, and finish time `2026-10-30T17:50:45Z`. Its worker error is
  `Git exclusion is overridden for sensitive records`. The original worker used
  `/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`.
- Read-only inventory found no target archive journal or cleanup sidecar.
  The retained worker journal confirms the same error. No target conversation,
  team or tracking contents were inspected or copied.
- Workspace commit `4579b97f13708afe94e64cb51a030bcaf665ae74` added the compact
  tracking rules. `!/work/**/` re-includes the session root, and the Markdown
  and portal exceptions re-include its records. Repository `.gitignore` rules
  have higher precedence than `.git/info/exclude`.
- Read-only `git check-ignore -v` identified those workspace negations as the
  winning rules. Existing local root exclusions are present, and a targeted
  index query returned no tracked target paths. The currently installed runtime
  still checks real Git exclusion results in
  `libexec/workspace-sensitive-sessions.rb:ensure_sensitive_exclusions!`.
- Two disposable Git prototypes reproduced the failure with synthetic content.
  The proposed rules passed for both tracking roots, before directories exist
  and after creation: all sensitive paths stayed ignored; ordinary direct and
  nested Markdown/manifests stayed visible; raw files stayed ignored; `git add
  -A` staged only ordinary files. Adding an explicit sensitive-root negation
  made the root visible again, preserving the runtime's genuine refusal.

## Scope, interfaces and implementation boundary

One package for implementer0, in this initiative's dedicated workspace worktree:

1. `.gitignore`: apply retention rules below each immediate session directory,
   rather than matching that directory itself. Use this shape for both `work`
   and `archive`:

   ```gitignore
   /work/*/**
   !/work/*/**/
   !/work/*/**/*.md
   !/work/*/**/portal.yml
   ```

   Keep the existing repository/worktree/cluster rules. Add a short comment
   explaining that the session-root boundary preserves private exclusions.
2. `test/storage_retention_test.rb`: add focused Git behavior regression tests
   loading the repository's actual `.gitignore` into a disposable Git repository.
   Use a separate small fixture from the compactor fixture where practical;
   these tests need Git, not a live runtime or private sensitivity records.
   Name the new tests with `tracking_ignore` for the focused command below.
3. `docs/operations/workspace-storage-retention.md`: add a short explanation of
   the session-root exclusion boundary and why broad directory negations must
   not be restored. No new procedure or document is needed.

No generic runtime, extension, configuration, input pin, package-generation,
portal, API or CLI changes. No target repair. Lead owns integration and tracking.
There is no second independent implementation package for this narrow fix.

## Invariants and acceptance criteria

- Both `work/<slug>/` and `archive/<slug>/` can be excluded by existing private
  `.git/info/exclude` entries. Root and descendants stay ignored, including
  direct/nested Markdown and `portal.yml`, raw data and absent future paths.
- Ordinary session Markdown and `portal.yml` at direct and nested paths stay
  eligible for Git tracking. Ordinary raw artifacts remain ignored.
- A synthetic `git add -A` proves that sensitive records never enter the index
  while ordinary intended records do. Include both tracking roots.
- The old rules fail the new regression; the fixed rules pass. Assertions check
  Git behavior, not an exact source-text copy of the patterns.
- An explicit higher-precedence `!/work/<sensitive-slug>/` override still causes
  the same root probe used by the runtime to return nonzero. Cover the analogous
  archive root too. Do not bypass or weaken runtime exclusion checks.
- Unrelated ignore rules and unrelated shared index/worktree changes survive.

## Compatibility, persistence and recovery

This changes repository-local Git selection only. Existing exclusion entries,
sensitivity records, manifests, operation journals, Git heads and runtime
ownership retain their formats and identities. Old and new runtime generations
use the corrected rules without coordinated updates. No database, protocol,
generated configuration, vpsAdminOS node or persisted-state migration is needed.

The failed target operation is still pre-journal and retains its original portal
receipt. This fix neither retries it nor grants lifecycle permission. After
integration, the lead may assess authorized read-only readiness. Any eventual
archive retry remains the ordinary retained receipt flow, under separate exact
session authorization. Do not clear receipts, rewrite exclusions or alter the
target to make a test pass.

Reverting the ignore-rule change restores the defect; it does not corrupt or
transform state. Correct forward if regression occurs. Preserve private
exclusions and all retained recovery data. Rollback cannot undo accidental Git
publication, so synthetic `git add` coverage is a required privacy check.

## Verification and delivery

Quick commands from the feature worktree:

```sh
nix develop --command ruby -c test/storage_retention_test.rb
nix develop --command ruby test/storage_retention_test.rb --name '/tracking_ignore/'
git diff --check
```

The focused tests must be self-contained and not call the existing compactor
fixture requiring `DEV_WORKSPACE_RUNTIME_SOURCE`. Run checks in the declared Nix
environment. Delegate environment realization if it becomes a long build.

After all intended changes are committed and quick checks pass, obtain the
mandatory independent final review of the complete workspace branch and its
history, including the explicit conclusion that there are no migrations.

Then run the existing packaged check, which supplies the pinned runtime source
for the full storage-retention test file:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.storage-retention
```

Use the required verification watcher for this uncertain-duration Nix check.
Stop if it unexpectedly expands to local kernel work or fails; inspect before
retrying. No broad runtime lifecycle VM campaign is required because no runtime
behavior changes. Synthetic fixtures provide the destructive/staging coverage;
never use the reported target as a test fixture.

The lead integrates the approved workspace branch into shared `master` under
the repository claim and tracking-lock rules. This updates the live Git policy
directly. No aitherdev system deployment, user-profile switch or configuration
pin update is necessary. After integration, read-only `git check-ignore` queries
can verify actual target root/known record-path exclusion without opening its
contents or changing it. The current fix session stays open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-vpsadminos-archive-fix/>
