# Extension machine metadata resolver

Lead released one bounded publication-feedback read after runtime CI diagnosis.
Exact Check41689335044/headf8da remained in_progress, conclusion null; flake job
126103462975 was running `nix flake check --print-build-logs`. Setup, checkout and
Nix installation passed; devcluster-check was pending. This is a status snapshot,
not successful extension acceptance. Evidence is `extension-f8da-ci-snapshot.json`
and `extension-f8da-ci-jobs.json`. No logs were retrieved while it was running,
and no polling, watcher, retry, local campaign or source change followed.

## Feature publication

Lead released independent source-only publication after final review and the
accepted corrected-runtime rebind. Exact reviewed
`f8da821e3c76e26e73aa9d89a712eab0e0faa319` is now published at
`refs/heads/2026-11-02-session-temporary-service-cleanup` on
`git@github.com:vpsfreecz/dev-workspace.git`. Fresh SSH fetch/ls-remote proved the
feature absent and default HEAD/master exacte4e before ordinary new-branch push.
Fresh post-push refs prove feature exactf8da and default unchangede4e.
The checkout/index stayed clean; no lease rewrite, rebase, source edit or other
ref mutation was needed. Reviewed one-commit series, source NARU5y, full34node graph
and lockb2282 remain unchanged. The source NAR was independently rehashed.

Exact Check push run [41689335044](https://github.com/vpsfreecz/dev-workspace/actions/runs/41689335044),
attempt1, was in_progress at one discovery snapshot. No superseded active run for
this feature existed, so nothing was canceled. B passed the exact run to lead and
A, who own verification coordination; no CI logs, watcher, polling or wait ran
here. One bounded run-detail lookup captured the workflow ID/path. Evidence:
[publication receipt](extension-f8da-publication-receipt.json),
[initial run snapshot](extension-f8da-publication-runs.json), and
[workflow/run identity](extension-f8da-publication-workflow.json).

All publication effects are reconciled and the Git lane returned clean. This is
feature publication only: no PR/default integration, downstream pins, local long
extension checks, build, claim, deployment or session lifecycle action. Runtime
acceptance remains the prerequisite for later extension contract/package work and
final pin/artifact preparation. The source-package receipt below is historical
pre-publication evidence and retains its original scope.

The independent extension package is committed locally and its Git lane returned.
No owned operation remains. No publication, downstream pins, build, full flake or
native tests, machine claim, deployment or session lifecycle action occurred.
Lead owns final intended-composition review and later publication choreography.

## Committed scope and source

- Repository/worktree: `vpsfree-dev-workspace`, this session's registered feature
  checkout under `worktrees/2026-11-02-session-temporary-service-cleanup/`.
- Fresh SSH default and selected extension base:
  `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`.
- One final commit: `f8da821e3c76e26e73aa9d89a712eab0e0faa319`.
- Tree: `0dee92a5a0971f250db89520c5d101b5b16bc008`.
- Source: `/nix/store/y01y2bs4mar8zq9s72npz3lrmlsjvasa-source`.
- Actual source NAR: `sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=`.

All 112 committed source entries match the Nix source, including bytes, symlinks
and executable bits. The source is retained by session-local indirect root
`extension-machine-resolver-retained-source`. Complete source metadata and proof:
[metadata](extension-machine-resolver-source-metadata.json),
[proof](extension-machine-resolver-proof.json).

Full `e4e..f8da` diff: four owned paths, 247 insertions and 11 deletions:
`lib/workspace_confctl_adapter.rb`, `flake.nix`,
`test/workspace_confctl_adapter_test.rb`, `docs/workspace-confctl.md`.
The complete staged and committed diffs were inspected. Commit used pinned Nix
tools and a temporary message file. No hook framework or active hooks are declared;
none were bypassed. Checkout/index were clean at lane return. Foreign refs,
worktrees and bare local master remained untouched.

The entire 34-node lock graph, all fields/edges and lock bytes equal the base.
Lock SHA256: `b2282ff7b51986f792cdfe5207c928699a085684c2183e539c434e55341a07bb`.
No migrations, dependency updates, old-state rewrite or external consumption
boundary changes. The existing confctl pin remains sufficient; its source was not
changed. No obsolete extension fixup or intermediate pin commit remains.

## Supported boundary

Frozen protocol-1 `resolve-machine` accepts exactly schema, operation, selector,
and source path/revision. It verifies the exact Git commit and uses a narrow
offline `confctl.machines` projection with IFD and lock updates disabled. It
returns only schema, exact name and sharedLockId. Missing labels yield null;
present-null, empty or malformed labels refuse. Names/labels require valid UTF-8,
1–256 bytes, no control characters and no leading/trailing whitespace. Source
paths and interpolation-shaped selectors are encoded safely for Nix.

The runtime owns canonical identities, claim keys and display. The resolver
does not call MachineList, build/copy, inspect, SSH or target/native probes, nor
does it create deployment artifacts/log directories. Existing operations and
artifact/recovery formats remain unchanged. Optional machineIdentityConfig is
forwarded only when nonnull. Lead supplied the final owning-document writing pass;
its claims were checked against the final code before commit.

## Quick evidence

Pinned environment selection used `nix shell --offline --max-jobs 0 --impure
--expr` with the extension's pinned Nixpkgs Ruby/Git/Nix. The test command was:

```sh
WORKSPACE_COORDINATION_COMMAND=/nix/store/9019d7wm0c40q59vrnlf1clwp7q00xrd-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/lib/workspace-coordination-command.rb \
WORKSPACE_CONFCTL_LOCAL_EVAL=1 ruby test/workspace_confctl_adapter_test.rb
```

Final result: 10 tests, 89 assertions, zero failures/errors/skips in 2.527900s.
This includes all four existing deployment/recovery fixture tests. New cases
exercise strict fields/duplicates/bounds, UTF-8 and whitespace, exact source
revision/selector, output overflow and rejection without artifact creation.

Actual disposable Nix evaluation uses a canonical bare Git repository with an
escaped source path. It resolves the earlier committed metadata despite changed
HEAD, returns Unicode/shared/literal-interpolation names, refuses missing or
malformed targets/labels, and proves IFD is disabled. Unselected private metadata,
packages and machinesJson throw if evaluated; resolution succeeds without forcing
them. The local evaluation case is explicitly opt-in outside a build sandbox;
it ran with no skip here. Package-sandbox tests retain the remaining pure fixtures.

Ruby syntax for adapter, test and entrypoint; Nix flake parse; whitespace: pass.
Actual old-provider evaluation with explicit null policy returns `dev-workspace`;
a constructor-boundary evaluation passes a supplied schema-1 policy unchanged.
The latter is pass-through proof, not final runtime/extension/workspace composition
acceptance. That exact composition follows the separately released workspace
package and local provider overrides, before publication and final generated pins.

An initial test load found that pinned Minitest has no optional mock module.
The tests now use direct method substitution/restoration in the existing fixture,
requiring no new dependency. All final checks above pass. No broad check campaign
or long operation was launched.

Next: lead coordinates complete intended source, mandatory review of exact local
composition, publication and final pin certification. No published SHA was guessed
and the consuming workspace was not edited by this package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
