# Separate runtime update decision

HaveAPI merge was explicitly approved; WebUI PR74 must remain open.
HaveAPI19c20c9 is rebased/reviewed/published with allfiveCIworkflows green.
No merge job was admitted: selectedcoordinatorRuby3.4 is forced inside
HaveAPIdeclaredRuby3.3shell and cannot load its nativegems.

Prepared correction: dev-workspace dce4784fe0069b061dd76cdf689e2099b4b0e66d,
base09a407953026514ae84be81dab9442fd74b6a362, tree5dc33558cc877c26573b9489aab13eb2e4c1ac89.
Onlyproductionchange selects `ruby` from entered repository Nix `PATH`; tests
exerciseactualselection plusmissingdependencies/environmentrestoration, docs
explainmatchingnativeABI. No command/state/schema/ledger or approvalgateschange.
All four final review lanes accepted the correction with no findings. The old
code fails the interpreter-selection regression; the corrected code passes four
focused tests with 30 assertions. The packaged coordinator suite passed all
54 tests across both exported shards with complete unique coverage and no skips.
The first isolated proof stopped before Nix because the harness assumed the
ignored generated Gemfile.lock was archived. A setup-only correction now copies
and hashes the matching retained lock and private gems; one fresh operation
is authorized. A second setup stopped before validation because Nix inferred
an ancestor Git directory; the proof now uses an explicit path: source reference.
No ABI result is claimed from either failed setup.
Neither result is a deployed-runtime claim.

The runtime fix is a separate component. Adoption requires the normal composed
workspace runtime pin, applicable configuration channel and package-composition
checks at the then-current baseline. Runtime/profile activation needs separate
user approval and the catalog queue. The foreign aitherdev reservation must be
preserved; any approved rollout waits for its owner. There is no direct
activation bypass. Integrating the new dev-workspace fix into its default branch
also needs approval naming that repository.
No merge/deploy permission inferred from sourcefixreview or HaveAPIapproval.
This document describes a sourcecorrection awaiting testedresult/rolloutscope,
not a readyinstallationartifact or submittedjob.

Once legitimately correctedruntime selected, refreshHaveAPI target/source
baselines and prepare/approve/submit exact supportedfast-forwardmerge. Keep
WebUIopen, no tag/npmrelease/defaulttransport/deployment/sessionlifecycle.

Correction feature published normally at
https://github.com/aither64/dev-workspace/tree/2026-10-19-haveapi-async-client
with exacthead dce4784, unchanged master09a4079, no force/default integration.

A later watcher preflight stopped before running the path-qualified command
because it checked the generic user profile instead of the workspace profile.
Read-only exact-path verification confirmed no actual generation change; the
next fresh brief names the workspace profile explicitly. No ABI receipt exists
from that unexecuted attempt.

## Final verification

The isolated real environment proof passed in a fresh snapshot, exact command
exit0 in about27seconds. HaveAPI19c and correctiondce were pinned. The actual
repository shell selected Ruby3.3.10/API3.3.0 while hostcoordinator is3.4.9/API3.4.0;
Bundler4.0.23, Overcommit0.73 and json/racc/prism/bigdecimal loaded. All588
committed files,5 original native libraries and original/copied generatedlock
remain unchanged. This is environment evidence, not an admitted coordinator job
or runtime deployment. All54 coordinator tests and finalreview are accepted.

Next user decision: whether to integrate the reviewed correction into
dev-workspace/master and authorize corresponding normal shared-runtime rollout
preparation/activation, keeping WebUIopen, so approvedHaveAPImerge can continue.
No rollout artifact or newpins/configintegration has been prepared or authorized
yet; recheck the then-current composition and foreignreservation before rollout.
