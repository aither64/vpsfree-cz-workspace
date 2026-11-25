# Shared incident escalation KB source review packet

Final mechanical pin stream is committed and SSH-published. Source verification
uses an explicitly accepted pin-only baseline exception: original full check
FAILED, targeted diagnostic PASS, exact unexecuted suffix PASS. This is not a
full bin/check pass. Separate reviewer0 source/history assessment and fresh
capacity admission remain before any runtime or capture.

## Exact final range and publication

Repository git@github.com:vpsfreecz/vpsfree-kb-contracts.git; branch
2026-10-30-oomd-abuse-policy. Owned canonical worktree at
worktrees/2026-10-30-oomd-abuse-policy/vpsfree-kb-contracts.

- Base ce2c8cd9358c3636e5d39343e595df813a0b197f.
- Final head7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d.
- Final tree9ffcfb0aac68b7785c1344ff8b5423127bffab12 exactly equals tested stage.
- Complete series: one commit, Pin shared incident escalation for VPS list captures.
- Exactly5files8insertions/8deletions. No migrations.
- Old1119bcdcf7db00a9bd91e84490d7a8de37c3575e/tree
  651f1834f002bde1200118761a6725e1f3865678 preserved under
  refs/backup/2026-10-30-oomd-abuse-policy/pre-shared-escalation-kb.
- One app pin stream folded into owner commit. No obsolete intermediate pins or
  runtime code edits. No old pin used by any KB guest/runtime/capture, no supported
  external consumer, release or deployment. Original197 and1119 checks/reviews
  remain separately scoped historical evidence.
- Fresh SSH fetch/default unchanged, no rebase needed. Explicit1119force-with-lease
  push exited0; independent ls-remote proves exact7bdee28 feature and unchanged
  masterce2. Clean worktree; comparison saved exact base/head. Normal amend from
  temporary message file; no declared hook framework/core.hooksPath or bypass.

[Full final diff](kb-shared-source-evidence/final-source.diff),
[old/new range-diff](kb-shared-source-evidence/range-diff.txt),
[complete receipt](kb-shared-source-evidence/source-pin-receipt.json),
[SSH proof](kb-shared-source-evidence/remote-after.txt).

## Input graph and impact

The required five files are flake.nix, generated flake.lock, captures.json,
contract/navigation.yml and contract/pages.yml. They select app
f60d41a453b1703e42de4341285bdc6ba339aff0/tree
f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c, independently proven over SSH after
owner0 publication. App default remains ac10a62f1cb0fc890378ae83cdf18dd0e29f049a.
App narHash sha256-ohmg6N/icH7V8B1t6tMETDkJk1l09bHM2LgWmv69lP8=.

Full old1119→final and basece2→final graph comparisons prove only vpsadmin
locked/original revision and locked narHash/lastModified changed. All input edges
and every other node, including explicit OS6bdf458fd9105379860234ff33d352e55844f08f,
are unchanged. No blind fingerprint refresh.
[Full graph](kb-shared-source-evidence/full-graph.json),
[graph comparison](kb-shared-source-evidence/graph-comparison.json),
[base comparison](kb-shared-source-evidence/base-to-staged-graph-proof.json).

Inherited app939159f2→ac10a62f1 changes only webui composer.lock/php-packages.nix.
Featureac10→f60 adds escaped localized incident type label/ratios in lists. The
incident details append after unchanged base table, outside h1+firsttablecrop.
Only getting-started/vps-list and restore-backups/playground-vps-list, eachcs/en,
require later refresh:4PNGs. Existing zero-incident fixtures expose0/5+0/10.
No new scenario, semantic-ID, fixture, page prose or PNG change.
[Impact assessment](kb-shared-source-evidence/impact-assessment.json).

## Exact verification and exception

Original nix develop -c bin/check --allow-missing ran on tree9ff/appf60 and FAILED
exit1 after~64s. Earlier101runs/1263assertions and19runs/150assertions passed.
RunnerSessionTest34runs/1238assertions had1failure at test-machine.rb:1728 comparing
retained child metadata after successful shutdown. Full utility log was not
redirected; it is incomplete. Native failure JSON/runner logs were recovered
without replay and preserved. They show stopped/complete/gone/claims0, unchanged
three listeners, and only the Ruby stand-in VM argv changed to[]. Companion
unknown-pidfile case preserved its entry/refused handoff as required. Relevant
source hashes match basece2/old1119/staged9ff. No unsafe stop effect observed.

One authorized exact targeted test PASS nativeexit0,14.01s,1run57assertions; this
does not erase failure or prove invocation fixed. Architect/lead explicitly
accepted PIN-ONLY baseline exception in kb-source-check-disposition.md; no runtime
change/assertion weakening permitted.

Exact unexecuted suffix PASS nativeexit0,386.1135s in same pinned shell/tree,
from ruby -c tools/test-node-ssh.rb through bin/validate --allow-missing. Original
argument parser and tests_meta regenerated exactly. Full redirected log/native
argv/result preserved. All semantic contracts and final existing inventory valid:
60concepts120variants66CSrefs61ENrefs120PNGs. No successful prefix/machine-suite
rerun. Necessary source tools restored~296.5MiBunpacked plus smallwrappers; no
image/kernel/realguest. No command remains live.

[Failure/result](kb-shared-source-evidence/source-check-result.json),
[native event](kb-shared-source-evidence/original-native-failure/),
[source hashes](kb-shared-source-evidence/failed-test-source-identity.json),
[targeted log](kb-shared-source-evidence/targeted-check.log),
[suffix input](kb-shared-source-evidence/suffix-input.json),
[suffix result](kb-shared-source-evidence/suffix-check-result.json),
[suffix full log](kb-shared-source-evidence/suffix-check.log).

## Review request and remaining gates

Retained reviewer0 saved Sol/xhigh should independently assess the committed
mechanical five-pin scope, exact graph, baseline exception and complete one-stream
history/no-migration conclusion. Content is mechanical, but history assessment
is required. No broader runtime fix is part of this package. Lead assigns review.

Automatic source Check will be observed separately. Any own exact automatic
managed runtime still queued/no steps will be cancelled under standing hold;
running effects must be reported before action. No manual runtime dispatch.

After separate sourcegate and fresh supported capacity coordinated with owner0:
full screenshots topology/native source+guest closure attestation,4PNGs in one
private output, strict exported validation, visual review, separate generated
media/provenance commit retaining generator revision, exact-final strict hosted
Check. Strict hosted gate is not waived by baseline exception. No production KB
write, merge, deployment or lifecycle action.

Checked project docs AGENTS/README, docs/webui-change-workflow.md and runtime
contract/clusterREADME. No product prose change is useful for mechanical pins.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/


Hosted status at publication: ordinary source Check41187229857 in progress,
observed by fresh Luna/low utility (parenthandle83317). Automatic Managed page
runtime41187229710 already in progress at source-check step, before test-state
preparation/runtime; no queued-only cancellation taken. Lead notified for exact
running-run disposition, full observed jobs retained.
[Mechanical equivalence](kb-shared-source-evidence/mechanical-equivalence.json)
proves each non-lock file changes only its one old→final application revision;
generated lock comparison covers all nodes/edges. This is mechanical equivalence,
not literal patch equality.

Lead disposition: exact automatic Managed page runtime41187229710 may continue
normally through its native guarded capacity. No cancel/dispatch/retry. This
mechanical five-pin content does not change runtime/test code; appf60 was cleared.
Separate committed pin/history+baseline-exception review is assigned immediately
and must finish before this owner's capture prep/runtime admission. Hosted test
coverage does not replace the four required PNG captures. Source Check is
untouched; source/managed terminal outcomes remain pending and will be reported
for actual scope. No local capture admission follows from this CI disposition.

Reviewer0 committed pin/history assessment cleared with no findings and accepted
the explicit pin-only baseline exception. Lead records kb-shared-source-review.
Hosted ordinary source Check41187229857 completed success on exact7bdee285, watch
exit0/377.6s. This separate full remote result does not change the original local
FAILED record. Fresh exact Managed watcher now owns run41187229710 under lead's
normal-continuation decision (actual parenthandle22007). No local admission.
Read-only capacity proposal: kb-capacity-evidence/admission-plan.md and JSON.

## Subsequent bounded runtime execution blocker

Leadreleasedcapacitypackageafterreview/sourceCI. Genericpackagesbuilt; managedCI
completed success. Actualpublicstart once returned0/ready, but periodictracker
EACCES at/procchildexe left knownobservationgap. Nofixtures/capturesattempted.
Authorizedguardedstoponce returned1after900.30s; all4QEMUexit0/all29recordedPIDs
absent, but nativecomplete=false/phasestopping/readyfalse/exactclaim+controlsocket
retained. No release/reset/cleanup/force/sourceedit. Runtimecaptureheldpending
userchoiceofseparatereviewedrepairboundary; pin/template milestonesremainvalid.
[Terminal effects](kb-capacity-evidence/public-stop-terminal-effects.json).
