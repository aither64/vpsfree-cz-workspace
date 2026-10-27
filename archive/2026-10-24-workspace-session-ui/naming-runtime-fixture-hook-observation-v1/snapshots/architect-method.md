## Naming fixture composed hooks: diagnostic boundary and conditional correction

Architect0, 2026-10-26. This amends only the compile-only fixture composition in
the naming acceptance design above. It is a design disposition for lead review,
not an execution or source-edit release. Current/session environment agree;
live roster revision32 retains architect0 as ready Astra/xhigh/workspace_write.
Session, documentation, verification, lifecycle and team guidance and the
documentation/monitor/review procedures were reread. No Nix, build, test, native,
provider, VM, Git or application-source operation was performed for this design.

### Evidence and unresolved observation

The frozen [owner3 diagnosis](naming-runtime-fixture-hook-diagnosis-v1/diagnosis.md)
has SHA256 `ff7d75c6810c8494dc635aeef64a996925b11ec9e3627379701af5f4582d16a1`;
its [evidence](naming-runtime-fixture-hook-diagnosis-v1/evidence.json) has SHA256
`957ffcfa48043f382a226d0f1137975a82585d63ecce9c09b9432076ad9ed01c`.
Both hashes, the four proposed packet files, exact cited store-source files and
five actual v3 attempt files were independently matched by file-only reads.
Outer67455 remains runner1; stage01 was Nix1 in7.010813s, with empty stdout and
the original inspector's line106 conjunction failure. Final identity/guards
passed and the recorded groups settled. This establishes neither hook's actual
value; it does not establish that postFixup was forced. No output identity,
availability, recursive graph or build result exists from that attempt.

At runtimec31 source5dg, `nix/tests/naming-runtime.nix:28–51` clears postInstall
and postFixup inside the replacement buildGoModule. Extension767 source lfmic,
`flake.nix:158–164`, wraps the runtime package in overrideAttrs and appends its
migration symlink to postInstall. Workspace0c source iqym adds its update skill
through an argument override and does not clear hooks. Retained test-root a5cc
`lib/customisation.nix:162–191` explicitly replays an attribute overlay around
argument re-entry. That supports the indicated ordering defect; it is not a
certificate of the uninspected package-root d58 implementation. The extension
hook is legitimate for the installed application, but it does not belong to a
fixture that only installs a compiled test binary. No product defect or actual
fixture build failure is inferred.

### Accepted diagnostic method, subject to separate lead release

The [observer](naming-runtime-fixture-hook-diagnosis-v1/observe-hooks.nix), SHA256
`cee59bb28010093c21359cf94b575f56e3863fa069aa39a7f8c57f3728ebb92a`, and
[proposal](naming-runtime-fixture-hook-diagnosis-v1/observation-proposal.json),
SHA256 `1b5067215ccb5f5128e136c823397481d40b1dbf7b627312ca60c15671484131`,
are suitable for the bounded observation. Owner3 prepares the successor envelope
only after lead accepts this method. A fresh parent-released watcher owns any
actual invocation; this amendment authorizes neither preparation by another
owner nor execution.

Retain the exact proposed argv array, selection-context SHA256
`cb5cb835d52c5f04513501f217e9958cb17d79bd750477ae11886b81d1134fab`, and final
binding SHA256 `80dd48cf8d10aab8cc0f563ac18a0855fb03e28c464f0d2a819358f9921b7b1d`.
Comparison with actual v3 confirms only argv indices4 and6 change: a separate
observer file and the applied function name, with the same binding path. The
proposed working directory changes to the observer directory; imports/binding
are absolute and the context's relative snapshots remain context-relative.
No original inspector, assertion, selected input or package override changes.
The context's identity, full-lock, provenance and constructor prerequisites
remain enforced; the observer does not execute the inspector's later policy
assertions and cannot stand in for their acceptance.

Modern eval retains --json/--file/--apply/--offline, IFD=false, substitute=false,
empty builders, max-jobs0, accept-flake-config=false and empty registry exactly
as proposed. Evaluation may write derivation metadata/caches; it is not a
read-only-store operation. Offline has the already accepted documented scope,
not a network-isolation guarantee. No output build, root operation, query,
source-selection change, retry or automatic continuation is part of this step.
Preserve the180s/16MiB limits, finite recorded-group settlement and unconditional
finalization guards from v3. Use new no-clobber results and actual tool/session,
source, binding and input pre/post guards, preserving original packets.

Accept an observation as usable diagnostic evidence only when all of these hold:

- Actual eval exits0; stdout is complete JSON with the exact observer schema,
  keys and diagnostic-only scope. No truncation, ignored-setting warning,
  unresolved group, source/tool drift or failed finalization is accepted.
- Workspace0c, extension767, runtimec31, test-root a5cc and package-root d58
  revisions match the binding/context. Known source paths match retained
  receipts; a newly reported nixpkgs source path is observed metadata only.
  Package and fixture sources both equal5dg. Names and derivation/output fields
  have their declared string types and store-path shapes. New derivation/output
  values are recorded, not guessed or called currently available.
- All four exposed package/fixture hooks and their four drvAttrs counterparts
  are recorded verbatim as string or null, with null retained as absence. Never
  coerce null to empty, trim away content, or treat the wrapper's attributes as
  sufficient evidence of the builder's effective hook values.

The specific correction below is confirmed only if exposed and drvAttrs values
agree, fixture postInstall is exactly the extension migration-symlink suffix
from the composed package hook (same observed tools path, no additional command),
and fixture postFixup is actually empty. Compare the full returned strings with
the cited source; retain their raw bytes. Product install/fixup hooks must remain
present and consistent with the source. A null, unexpected extra command,
postFixup content, mismatch between exposed/builder values, or different failure
requires a narrow follow-up disposition. A successful observation is never
compile-only, VM-policy or naming acceptance, even if both fixture hooks happen
to be empty.

### Conditional implementation boundary

If those observations confirm the outer append, owner3's smallest source change
is confined to runtime `nix/tests/naming-runtime.nix`: apply the two empty hooks
to the final composed fixture, after package.override returns:

```nix
fixture = (package.override {
  # Existing replacement buildGoModule, attributes and goModules override.
}).overrideAttrs {
  postInstall = "";
  postFixup = "";
};
```

Keep the existing inner clears and replacement builder. In particular, moving
buildTestBinaries into only an outer overrideAttrs would retain the application's
go-install build phase and is not this correction. Preserve exact package.go,
package.goModules, source, postPatch pin check, preBuild review assets, vendorHash,
tags, subPackages, doCheck=false and empty checkPhase. A short adjacent comment
should explain that extension overlays can reintroduce hooks after builder
re-entry. The package and extension product hooks remain unchanged. No new
helper/export, mock package, directory creation, conditional hook execution,
native invocation or production behavior change is needed.

The original inspector SHA256
`8e21b2457a343c819e1e6bba9c02b391c98555b60d5b3bdf0e8a4c1d918d1ff3` remains
immutable. A separately prepared successor must retain all its logical
assertions, including exact empty hooks, test-c compilation rather than install,
compiler/modules identity, manifest bindings and complete managed/real VM
policies. Only newly accepted immutable source/input/provenance bindings change.
Use the same diagnostic projection on that final selection to establish both
exposed and effective drvAttrs hooks are empty; do not weaken line106 or replace
the full inspector with that projection. No separate application documentation
change is needed: docs/codex-package.md already states the compile-only contract;
the nearby source comment records the composition rationale.

### Quick checks, review and final-input dependencies

After separate source release, owner3 reports the exact one-file diff, preserves
the frozen c31 tree/failed attempts, and runs the declared Nix syntax/format quick
checks appropriate to this delta. Commit all intended changes and give the
retained independent reviewer the affected general/architecture scope and the
fixture's compile-only safety boundary before long checks. This changes a
previously unassessed composition boundary, so it needs affected review; it is
not an evidence-only edit or a reason for an unrelated full review campaign.
Preserve protected runtime9634151/extension399c330 ancestry and a single final
implementation/input-update stream, with old/new history and equivalence proof.

The new fixture source changes the runtime source NAR and source-bound derivation
identities even if module payloads stay identical. Old c31/5dg vendor, source,
browser and consumer receipts stay historical; do not relabel them final.
Prepare one coherent successor source/derivation and affected vendor proof under
the existing exact-final method, retaining Fx only on actual module/hash/content
proof and without repeated hash discovery. Generic runtime vendor proof does not
establish equality to the workspace d58 package's compiler/modules. Bind the
fixture to the actual composed package, as the existing inspector requires.

Owner0/owner1's ordinary consumer update routes must select the same newly
published runtime, preserve extension767 and unrelated lock nodes/edges, and
produce new complete source/input/provenance receipts before final naming
evaluation. No speculative pin or source hash is part of this design. Reuse
unchanged Go/Ruby/browser/client/native scenario passes only with actual relevant
input identity proof and an explicit old/new mapping; full self-source equality
no longer holds. The hook-only change alone does not require repeating unchanged
client/native tests or creating a custom native binary.

Once the final selection is accepted, run the unchanged full inspector plus
effective-hook evidence, immediate metadata availability/identity checks and
separate recursive graph inspection before any newly released build. Previously
unrun assertions remain unrun until those commands actually succeed. Then use
the existing fixture/manifest/driver build and managed/real acceptance sequence;
building a fixture or driver is not test acceptance. Dedicated real-account
availability, UID1000/user manager/private counter/egress, prompt30s/two-slot
behavior and native stop/join requirements remain unchanged. Unexpected failure
stops its stage, preserves evidence and owned resources, and returns to lead;
no automatic retry, cleanup or acceptance fallback is introduced.

No database/on-disk schema, public API, protocol, runtime option, deployment or
rollback contract changes. Installed behavior and migration hooks are retained.
Deployment, default integration, claims and lifecycle operations remain outside
this disposition. The session remains open; lead owns state/checklist and release.
