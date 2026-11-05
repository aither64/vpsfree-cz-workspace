# Final affected deletion-preflight review

## Findings and disposition

No new Blocking, Important or Advisory source findings in the assigned general
and risk/compatibility lanes. Accept the committed four-line fresh-deletion
preflight and focused fixture correction at
`60a2438f8217bb91cbd527c2d84a47ed46244952`.

This clears the affected independent source-content review gate. It does not
certify historical absence of effects from the first ambient CLI invocation,
close that evidence limitation, certify package/native success, or grant
publication, deployment, integration or lifecycle permission. The incident and
remaining verification limits below must remain explicit in later readiness
records.

## Identity, exact scope and settings

Same independent retained `reviewer0`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, purpose `review`,
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh live roster revision 27 confirmed
ready state and these saved settings. No override, fallback, nested reviewer or
substantive authorship.

Before accessing records, `dev-session current` returned exactly
`2026-11-02-session-temporary-service-cleanup`. Both environment markers matched
that slug and `/home/aither/workspace/ai/vpsfree.cz`, also matching the trusted
thread binding. Read mandatory-change-review in full and the general/risk
references; consulted applicable runtime/workspace instructions and lifecycle,
documentation and verification procedures. Read the released packet section,
receipt/diff and both final architect sections, then traced actual source,
retained incident evidence and focused results directly. Risk remains **High**
because deletion ordering and fixture access to a native runtime are affected.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Complete final range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..60a2438f8217bb91cbd527c2d84a47ed46244952`.
Final tree: `7c0d27a9abba6263d905c612c9fd4c57c7d53cd0`.
Immediate correction range:
`ad0770a8ce6bb3b70645dc196386106a049072e8..60a2438f8217bb91cbd527c2d84a47ed46244952`;
four paths, 135 insertions/14 deletions. Published predecessor:
`5f7b13fd32f85ac0f502b42642578b19bbefc67e`.

This is an affected final review of committed, focused-green work. Unaffected
four-lane machine/service/capacity conclusions and the direct M1/test-wiring
closures are reused under the skill's narrow-fix policy. This correction restores
an existing refusal contract; no new machine-identity or UI policy is reviewed.
Prior reports remain unchanged.

## Validation order and recovery

Inspected `libexec/dev-session:2494-2508` and its existing helpers. New lines
2499-2502 execute within the creation and exclusive slug locks, after failed-
creation context and conflicting-journal checks, before coordinator idle/capacity
admission. They test strict presence of the **ordinary** deletion journal rather
than an access token that might identify only a services prelude.

`path_exists?:8436-8440` uses lstat and rescues only ENOENT. Present malformed or
symlink journals remain present and retain the strict loader's refusal; they do
not become fresh deletions. `validate_removal_tracking!:6220-6235` requires exactly
one active/archive root, checks it without creating tracking, and returns its
actual location. The existing recovery-location validator at 6526-6537 derives
and reads locations, including the existing cluster cleanup-paths inventory. It
does not stop services, reset a cluster or publish removal state.

This restores the intended DevSession class/message for invalid fresh recovery
locations before M1's strict coordinator read can fail with ENOTDIR. It leaves
M1's ENOENT-only rule intact. A valid location still reaches that strict reader;
the EIO control asserts code 5, typed cause, retained ledger bytes and no removal
publication or recovery directory.

The insertion does not move the earlier ordinary loader in
`failed_creation_start_context`, or the later capacity/loader, retirement-identity,
`prepare_removal!` publication or validation calls. Existing-journal retries bypass
the fresh preflight, including after tracking moved into private recovery. Exact
operation identity, saved force matching and its existing force upgrade remain
at `prepare_removal!:6605` onward. Journal/prelude conflict handling, saved phases,
coordinator binding, service cleanup and eventual file-removal order are unchanged.
Normal command-entry lock/journal-directory setup already precedes the boundary;
acceptance does not mean zero filesystem setup before refusal.

Inspected the unchanged two original error/message regressions, archived-root
control, services-prelude-only control and adjacent retained-journal/tracking-move,
operation/force and lifecycle controls. The archived and prelude-only tests put
tripwires at coordinator admission/publication and assert preserved bytes and no
new recovery data. The retained retry path is preserved rather than forced to
rediscover absent ordinary tracking. No new format or recovery policy is needed.

## Repaired confirmation fixture

Reviewed `test/dev_session/deletion_lifecycle_test.rb:201` onward and the existing
CLI runner/runner_for seam. Both CLI instances now receive explicit fixture-only
environment hashes, without ENV.to_h, and use the injected runner with NullTmux
and disposable state. The runner's portal command is absolute Ruby plus a
controlled local script, and its socket is an absent path below the temporary
workspace. Assertions verify the selected command/socket before invocation.

The script recognizes only exact known retirement and uploads-removal argv and
aborts on any other command. Its retirement branch requires the ordinary journal
at thread_retiring while tracking still exists; uploads cleanup requires tracking
already preserved. A negative answer records no calls and retains tracking.
A positive answer requires exactly the two expected fake calls, removes only
fixture tracking and leaves the absent socket absent. CLI failure assertions now
include retained local stderr. The script delegates to no installed portal or
native client. No environment framework, fence bypass or production guard
relaxation was added.

The positive case exercises the retirement call/order through a stub; an XDG-only
environment that merely skipped retirement would not prove that boundary. The
new fixture does not certify real retirement, native cleanup, or effects of
earlier executions. Existing native-order/recovery tests keep their separate role.

## Incident: evidence and unresolved limits

The initial selected batch reports 111 tests/1,214 assertions and one confirmation
failure. It inherited ambient runtime configuration, but the exact helper argv
and CLI stderr were captured without retention. **Its precise guard branch and
historical native effects are not proved.** Neither a later reproduction nor
current conversation continuity establishes that it made no native call or had
no effect on another thread.

The separately retained diagnostic is stronger evidence for **that second
invocation only**. Its argv identifies installed package
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`, disposable
cwd/workspace/state, inherited live socket, no explicit thread ID and no force.
The recorded error is `find session conversation: submission fence exists
without its migration journal` and process exit 1.

Independently read its retained runtime source
`/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source` and installed codex-web source.
Recomputed client/submission_database/submission_migration SHA256 values; all
match the architect's exact d3a anchors. `main.go:55-86` selects a disposable
socket-hashed JSON/SQLite path while retaining the socket-adjacent legacy path.
Thread command constructs its client and defers Close. The constructor does not
connect. `workspacecodex/client.go:584-600` calls ThreadOperationAttempt before
discovery; codex client.go:3363-3371 enters the submission transaction. Database
initialization runs before the operation callback, and migration.go:115-191
returns the recorded fence error before import or target discovery.

Thus the recorded second invocation reaches no native connection/initialization,
target selection, operation recording, interrupt, retirement, archive or
continuation. This does **not** establish zero filesystem interaction: database
initialization can create disposable SQLite/schema/WAL state; predecessor locking
can open/create and flock the live-adjacent legacy .lock, then read its fence.
Historical lock preexistence is unknown. No fence/ledger rewrite or import is
reached on that branch. Source unwinding closes predecessor descriptors and the
failed database; the client is deferred closed, and recorded process termination
leaves no held process locks. No retained disposable database specimen exists to
prove its exact writes.

The incident is documented honestly and the committed fixture removes the
observed ambient access path. I found no remaining source defect requiring a
broader subsystem or live audit through this review. Historical first-run
no-effects certification remains unavailable; source acceptance does not convert
that unknown into a clean operational receipt. No live status, native request,
fence inspection, lock cleanup or replay was performed or requested here.

## Affected history, migrations and inputs

Independently inventoried the complete final five-commit series:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/Team UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — service owner/lifecycle.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent integration/fixture.
4. `1517c8b6c34746fdc756fdb327939fa480b7b468` — capacity and its verification.
5. `60a2438f8217bb91cbd527c2d84a47ed46244952` — machine claims and this correction.

First three commits are exact/range-diff equal. Fourth differs from 8230 only by
the three accepted Automation-navigation test clicks. The product JS/API and
assertions remain unchanged. Fifth incorporates the four-path correction into
the owner of the strict-state interaction. Independently verified that retained
fixup `47348755c50378dc9dd5d6fcee8a268634a4d38b` and final head have the exact
tested tree above, and that the saved core diff equals the committed delta.
Earlier published/reviewed/fixup refs and failed-CI evidence remain retained.
**No obsolete fixup, abandoned approach or transitional implementation remains
in the final five-commit history.** Unaffected M1 and fixture-registration/content
closures remain as recorded; this review does not repeat the machine design.

**No database migrations.** This correction changes no schema, API, capability,
force/permission contract or saved recovery policy. Direct feature introductions
of retry/claim schema 2, supported production schema-1 predecessors, local service
schema 1 and legacy journal/payload formats retain the previous provenance and
forward-reader conclusions. No transitional migration was introduced by these
fixes. **No repeated dependency/generated input stream exists in this runtime
series**; flake lock and full nine-node graph including root equal c218 and the
previous reviewed inputs.

Extension f8da/workspace48b and existing downstream pins remain unchanged by this
follow-up. Their earlier content conclusions are reused; stale selections and
historical artifacts still do not certify this final runtime. Actual final pin
consolidation, source/NAR/full-graph equivalence and readiness certification remain
required. No hypothetical future pin or deployment is accepted here.

## Source and verification evidence

Independently hashed readable source
`/nix/store/cb4jkgajyfa4iq27b5h4xkd2bwiysq7r-source`:
`sha256-Rgak4IV7sAUBG7LNN55sJlhPIjjnY5tgJZH88DgeO/A=`.
All 679 Git entries matched clean final worktree and immutable source contents,
symlink targets and executable modes, without extra/missing source entries.
Lock SHA256 is
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`;
actual metadata graph matches the lock. The active ordinary review root remains
untouched.

Read the causal red and final focused logs and independently matched receipt
hashes, including the actual launcher log. The final frozen/tested tree matches
the committed tree: 111 selected/executed/unique cases, 1,221 assertions plus
two M1 cases/67 assertions, no failures/errors/skips; four Ruby syntax checks
and diff check pass. Recorded batch time is 63.79 s. Earlier focused six cases/52
assertions pass. The initial failed batch and separate diagnostic remain retained
as failures, with their distinct evidence limits.

Previously accepted backend four-variant/32-manifest and corrected activity
desktop/mobile evidence remain scoped to their actual inputs. They are not a
blanket final package/native pass. Current 5f7 CI failed before either VM. Exact
new runtime package/native/archive/creation and remaining composition/deployment
verification are outstanding. Extension CI on its declared older runtime graph
does not certify this runtime. No deployed or installed usability success follows
from the source checks.

This reviewer ran no tests, builds, live/native probes, cleanup, publication,
claims, CI or lifecycle operations. No application, Git, store, prior report or
source root was mutated. Only this permitted review report was written. The
source gate is accepted within these limits; lead owns subsequent check selection,
incident disposition and operational authorization.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
