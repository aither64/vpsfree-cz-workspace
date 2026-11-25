# Bounded legacy KB capture package

Preparation only. Final combined vpsAdmin source head is pending; no source-pin
edit, capture build, runtime start, KB mutation or deployment performed.

## Ownership and source boundary

- Owner: implementer3, also retaining notification-template review-fix ownership.
- Dedicated repository/worktree: `vpsfree-kb-contracts` at
  `worktrees/2026-10-30-oomd-abuse-policy/vpsfree-kb-contracts`.
- Feature branch: `2026-10-30-oomd-abuse-policy`.
- Initial/current base: `ce2c8cd9358c3636e5d39343e595df813a0b197f`.
- Current KB vpsAdmin pin: `939159f27b5d627930281d5fac0c0aa9ba53bfc7`.
- Application feature base: `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`.
- Inherited WebUI drift `939159f2..ac10a62f1` final diff contains only
  `webui/composer.lock` and `webui/php-packages.nix`; no PHP declarations,
  landmarks or gettext catalog changed in this range. Final source checks must
  still verify the effective pin. Feature drift assessed separately.
- Fixed scope from architect and legacy owner: `getting-started/vps-list` and
  `restore-backups/playground-vps-list`, Czech and English, four PNGs total.
  Base VPS zero-incident fixtures should render 0/5 and 0/10. No new OOM scenario.
- `getting-started/vps-details` uses h1 and first table only; the new OOM section
  follows that table, outside crop. Recheck final combined source before capture.
- Relevant pages: CS `informace:novacci`, EN `information:new_members`, and CS
  `navody:vps:obnova_webu_zo_zalohy`. English playground screenshot has no current
  source-page binding but remains required by the bilingual concept contract.
- Read full repo AGENTS, README, canonical WebUI workflow, cluster README/runtime
  contract and workspace procedures. No managed-page expansion or production
  publication. Lead owns any actual member-facing candidate prose.

## Private runtime preparation

Explicit owned config: `kb-capture-private/config.json` (0600). Private state,
output, logs and short temporary directories are beneath `kb-capture-private/`
(0700); all excluded by workspace ignore rules. Config contains generated
synthetic passwords; never print or commit it.

Full `screenshots` topology: services 4096 MiB, node1 4096 MiB, node2 4096 MiB,
backuper1 2048 MiB; services root 12288 MiB; each node tank sparse 320 GiB.
No reduced `ip-inventory` profile. Synthetic example.test users/domains and
existing documentation-range address pools preserved. Added explicit test-admin
level99 namespace1/8; member namespaces9/8 and17/8. DNS guests disabled, gateway
resolver selected. Runtime generates its own private CA/SSH trust.

Candidate dedicated bridge addresses: services172.16.106.181, node1 .182,
node2 .183, backuper1 .184; br0/gateway172.16.106.1. Initial four ping probes had
no replies. This is not reservation proof. Native resource registry/probe checks
must pass afresh at owned start; no foreign reservation contents accessed or
changed.

Host observation on preparation: KVM readable/writable; br0 up at
172.16.106.40/24; qemu-bridge-helper setuid and /etc/qemu/bridge.conf allows br0.
RAM available57,234,411,520 B (~53.3GiB), shared memory free35,265,597,440 B
(~32.8GiB),64CPUs.14GiB guests require separately assessed positive browser/runtime
margins. Refresh immediately before action.

Disk risk: state/store/tmp share /dev/vda1, free51,335,053,312 B (~47.8GiB),95%
used.12GiB services image +12GiB writable root eventual extent +16GiB documented
base reserve leaves~7.8GiB before three sparse-tank growth, closure downloads,
construction scratch/import overlap and retained-host obligations. Sparse960GiB
logical capacity is not current physical allocation and does not certify fit.
Exact final-input closure/cache/kernel and physical growth assessment is pending.
No capacity admission has passed; do not start/build until supported admission
passes. No foreign cleanup, lower fixture or runtime redesign is authorized.

## Preparatory provenance

`kb-capture-private/source-preparation.json` retains the clean KB base/tree,
complete locked-input graph, ten source/contract/scenario digests and private
configuration digest. It explicitly marks the final application head pending
and is not runtime, reservation or capacity proof. Final reviewed source and
native source/artifact receipts must supersede this preparatory inventory.
The generic `tools/capture-export.rb` is specifically bound to the reduced
ip-inventory qualification; it is not the carryback list for these four PNGs.
Use the normal output-root artifact contract for accepted selected media and
exclude private state/credentials/transcripts.

## Shortest supported next route

1. Receive final combined published vpsAdmin SHA from backend/lead. Confirm legacy
   file/crop map and distinguish base drift. Pin exact SHA in flake.nix+lock,
   captures.json, contract/navigation.yml and contract/pages.yml; update lock with
   `nix flake update vpsadmin`, inspect semantic graph for unrelated changes.
2. Run pinned-shell source `bin/check` (allow-missing only for pending media),
   interpret any control drift individually; no broad fingerprint refresh.
   Commit source changes and publish. Lead coordinates independent source review.
3. Assess reviewed final inputs, exact closure/cache/kernel and actual capacity;
   stop affected capture if evidence cannot establish supported admission. No
   runtime mutation before review/capacity. Keep owning private config unchanged.
4. After review/admission, fresh Luna/low utility launches full dedicated runtime
   with explicit config/state, bridge mode. Capture each of two checkpoints for
   cs/en into one private output. Native readiness/source/closure attestation and
   leases remain authoritative. Failures retain native evidence/ownership.
5. Update candidate inventory then strict exported validation and bin/check with
   explicit output root. Visual-review all four PNGs/crops/fonts/counts/locales.
   Copy only accepted PNGs/inventory/provenance to repository; preserve generating
   revision. Commit mechanical media separately, publish and manually dispatch
   strict hosted Check on exact final committed head; verify checkout+strict step.
6. Report branch/history/migration/verification evidence to lead. Any later KB
   release needs its separate guarded candidate/staging/production approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.

## Exact source-pin plan pending lead release

Application final-review candidate resolved locally as
`51297de1a05fee60aaba8a31e443abf95675396c`. This is not publication proof or
permission to advance. Final app review is active; no KB pin, push, build or
capture may run until the lead supplies the review outcome and publication
release. If the application changes, replace this candidate with the final
approved published exact head.

After release, from the owned KB worktree:

1. Verify the exact published application feature SHA with `git ls-remote` over
   SSH and confirm the supplied SHA matches the reviewed final revision. Fetch
   KB origin and verify current master/base before starting changes. Keep branch
   history linear under the normal Git procedure.
2. Replace the exact old SHA
   `939159f27b5d627930281d5fac0c0aa9ba53bfc7` with that released SHA in four
   source files only: `flake.nix`, top-level `captures.json.vpsadmin_commit`,
   `contract/navigation.yml.vpsadmin_revision` and
   `contract/pages.yml.revisions.vpsadmin`. Assert each target has exactly one
   old-value occurrence; preserve source formatting.
3. Run `nix flake update vpsadmin` in the KB root, through a fresh required
   verification utility if duration is uncertain. Let Nix own `flake.lock`.
   Inspect the semantic before/after graph: intended vpsAdmin revision/hash;
   unchanged explicit vpsAdminOS override and other direct pins; explain any
   necessary transitive graph changes. No broad lock refresh.
4. Stage only those five files so Git-filtered Nix source includes intended
   changes. Run the pinned-shell `nix develop -c bin/check --allow-missing` as
   the source batch, through a fresh utility. The flag applies only to pending
   media and does not waive semantic/runtime source checks. Inspect every drift
   by control/label/route/context, separate inherited packaging drift from the
   OOM feature range and report any blocked result. No blind fingerprints.
5. Confirm the final source diff is the exact five-pin change or a separately
   justified minimal contract correction. Record source checks and full input
   identities. Commit with a temporary commit-message file and required hooks,
   fetch/rebase safely, publish the feature branch and record remote head.
   Commit source package before capture; no runtime build may sneak into this
   source/check phase.
6. Give reviewer0, through the lead, the committed complete KB base-to-head series,
   pin/lock diff, no-migrations inventory, source checks, two-concept/four-PNG
   crop map and capacity gap. Wait for the separate independent KB source review.
7. Only after that review and supported exact-input capacity admission may the
   dedicated full-topology runtime/capture batch start. Native provenance must
   bind the committed KB generator revision. Media acceptance and hosted strict
   exact-final-head Check remain later distinct gates.

Current action boundary: command/check plan prepared only. The KB worktree
remains clean at `ce2c8cd9358c3636e5d39343e595df813a0b197f`.

## Corrected app source release pending SSH proof

The lead cleared corrected app candidate
`5a59ead40a283f74d211c7afde4d4d69aab28785` and released publication to backend
owner0. This supersedes candidate51297de1 in the prepared plan. Waiting for that
owner's actual SSH remote publication proof before any KB pin updates. The
source-only package is then authorized; runtime/capture still require separate
reviewer0 committed-source review and supported capacity admission.

Fresh preparation measurement:49,923,178,496B free on shared root/store/tmp,
44,328,979 free inodes. This is an observation, not admission. Exact reviewed
input/cache assessment remains pending. No claims or machine reservation.

## Released source pin implementation

Backend owner0 supplied SSH proof for final reviewed
`5a59ead40a283f74d211c7afde4d4d69aab28785`, tree
`55ba156994507edd4ebe334adadffd9767f73814`, with master unchangedac10a62f1.
Independent SSH ls-remote matched both refs. Fresh KB fetch/rebase was no-op.
The five intended pin files are staged, tree
`7f28bc0eb9063b0f9fb674a5fb8f7fd9d6a00c2e`. No fingerprints changed.

Nix lock update passed13seconds through a fresh Luna/low utility. Comparison of
all lock nodes and input edges confirms only vpsAdmin locked/original identity
changed, to narHash`sha256-NSETbm2yBSjs4nzC+NUl9L/awqvmAHBXglrUzZpFSW8=`.
Explicit OS6bdf458f and all other nodes/edges unchanged. Pin/lock diffs and
complete graph receipt are under `kb-source-evidence/`.

Source-shell dependency plan is296.5MiB unpacked+5small Ruby/shell derivations,
with no guest-image/kernel derivations. Source checks use pinned shell and
`bin/check --allow-missing`; media is later. Backend owner0 acknowledged bounded
source allocation and has no heavy local runtime/build allocation. All later
heavy local admission must remain coordinated with him. No runtime admission,
claim, guest build or capture has occurred.

## Source delivery checkpoint

Source package published at197b3544546a793d3d489c951e4b06bb9c3038f5, exact checked
tree7f28bc0eb9063b0f9fb674a5fb8f7fd9d6a00c2e, one5file8+/8-commit abovece2c8cd.
Source checker passed exit0, no fingerprint drift. Clean worktree; SSH remote
proof verified. [Full review packet](kb-source-review-packet.md) contains complete
range, graph, migration-none conclusion, impact map and all source check evidence.
Awaiting lead-coordinated reviewer0 separate committed-source assessment. No
runtime/capture/admission from this source milestone.

## Automatic managed runtime deferred

Lead explicitly directed queued own exact-head automatic run41118003110 to be
cancelled before independent source review. Pre-action status was queued at
head197b3544546a793d3d489c951e4b06bb9c3038f5, job124277139468, no steps run.
Cancellation request succeeded; job reached cancelled with no executed steps.
This defers long runtime validation and is not a failed source/functional check.
Evidence:kb-source-evidence/managed-runtime-{before,after}.json.
Source Check41118003005 remains running/observed and was not cancelled. No
workflow configuration changed, no other run touched, no local capture started.
A fresh exact-head managed-runtime dispatch requires lead selection after source
clearance; it has not been requested.

## Source review clearance and final-pin dependency

Lead reports reviewer0 cleared KB197b354 mechanical pin/history scope with no
findings. Retain that exact original review/range and source-check evidence.
Backend hosted foundation found generic stock-mail branding in two built-in EN
fallback bodies; backend owner0 is applying a text-only correction. Site
notification head e8c2c3d and API/UI/schema contracts remain unchanged. The final
app SHA will change; do not pin interim heads, build/start captures or dispatch
managed runtime. Wait final corrected published app SHA+remote proof.

No supported runtime consumed197b354. Fold the final update into the single
owning unmerged pin stream, preserve reviewed old/new range/input equivalence
and no-migrations evidence, then apply lead's relevant review/check gate. Existing
Check197 result is scoped only to that exact source. Backend29other foundation
failures remain under diagnosis; no readiness claim from this package.

Read-only capacity guidance inspection: portable runtime supports an explicit
private state/output root, but the documented real qualification requires a
private disk-backed campaign root. No documented tmpfs-backed VM/image qualification
or combined file+guest-RAM proof was found. No tmpfs alternative is assumed and
no alternate mount/profile/cleanup framework introduced. Later full topology
admission must use supported existing filesystems and exact source/cache/physical
measurements, coordinated with owner0's current image build. No heavy allocation
or claim by this package.

## Shared capacity coordination checkpoint

Backend owner0 reports its staged old-head two-image build completed exit0 in
461seconds, with no running scenario/VM left by that build. Shared root free
37,009,141,760B (~34.5GiB) at its observation. Exact image measurements receipt
pending from owner0. Old images may supply cache inputs only; they do not prove
final KB source/closures or admission. This package still holds no allocation
claim, creates no guests, and waits corrected final app head. All future heavy
admission remains coordinated with owner0/lead and actual fresh disk/RAM/shm
measurements. No support inference from build success or cache presence.

## Hosted source Check197 completed

Run41118003005 passed at exact head197b3544546a793d3d489c951e4b06bb9c3038f5.
Fresh utility completed watch exit0 in9m20s and no handle remains. Its job
checkout/source step succeeded; strict step was correctly skipped. Full status,
steps and log remain kb-source-evidence/ci-source-status.json and ci-source.log.
This is source-phase evidence only for197; it does not certify a later final
pin or regenerated media. Managed runtime remains deferred/cancelled, no capture.

## Final authoritative source refresh pending proof

Lead cleared final app4d72e3e754fd47b598de1e54e05b3c5d26c62200. Waiting owner0's
actual SSH publication proof before pins. Original197 source review/check packet
preserved separately as kb-source-review-packet-197b354.md and original evidence
unchanged. No supported runtime consumed197.

Read-only old5a→final4d diff is exactly two generic core EN fallback bodies plus
testDBstartup OFF flag and tests/README docs; no WebUI source changes. Final app
tree588e65a8a13e3da69483cbf4c44cdfac84694a9e. FourPNG crop map remains applicable,
subject to final-source checks. Fresh shared-root observation48,058,322,944B free,
not admission; owner0 final-input allocations remain coordinated. No KBheavyrun.

## Final pin source check active

Actual SSH publication proof from owner0 and independent check matched finalapp
4d72e3e754fd47b598de1e54e05b3c5d26c62200/defaultac10a62f1. Fivepinrefresh staged,
tree651f1834f002bde1200118761a6725e1f3865678; graph comparison only vpsadmin identity
changed, narHashsha256-UMUwSBHp6HqMYC4ucoDAvOiuQEJesYhqgGWVK9HPc1g=, all other
nodes/edges/OS override unchanged. Evidence kb-final-source-evidence/ retains
full graph and197→finaldiff; original197packet/checks retained separately.

Fresh standalone Luna/low utility launched exact full `nix develop -c bin/check
--allow-missing` against this staged source; parenthandle91800, source-watcher.log,
source-check.log and finalsource-watcher-result.md. Prior197success is not reused
as proof. Only after exactbatch success fold into owning single unconsumed pin
commit, publish explicit old-head lease, preserve old/new range proof. No runtime
or capture; owner0finalimageallocations coordinated and KBheavyheld.

## Authorized owned-temp cleanup

Lead conveyed explicit user cleanup request while keeping useful final source
checker alive. Exact known owned artifacts inventoried: no KB guest images,
prepared runtime result roots or actual guest data exist. Removed seven unused
small temp files plus empty completed first-source-shell scratch after checking
no active cwd/fd/TMPDIR reference and matching renderer/helper evidence copies.
Allocated blocks reclaimed32,768B. Receipt:kb-final-source-evidence/owned-temp-cleanup.json.
Current source-check scratch /tmp/nix-shell.ugRi2i, currentbrief, neededcommitmessage,
privateconfig, finalinputs and all source/check/review evidence preserved. No
peer state, worktrees, lifecycle cleanup, directstore deletion or globalGC.
No substantial own reclaim opportunity; shared GC remains lead-owned.

## Final source publication checkpoint

Final head1119bcdcf7db00a9bd91e84490d7a8de37c3575e selects final app4d72e3e7,
tree651f1834f002bde1200118761a6725e1f3865678. Full exact-input source check passed
559.474seconds, final commit tree matches tested tree. One final five-file pin
commit abovece2c8cd, SSH lease publication/proof, clean worktree and comparison
captured. [Final source packet](kb-final-source-review-packet.md) preserves old197
review/check/graph and final range equivalence, no migrations. Long KB work remains
held by lead; no runtime or capacity admission inferred.

Final source Check41122715625 is observed by a fresh Luna/low standalone utility,
parent exec handle87142, with ci-source.log/ci-source-status.json and
ci-watcher-result.md under kb-final-source-evidence/. No preparation/build/runtime
was launched. Exact managed-runtime41122715604 cancellation is confirmed final,
no executed steps. Final post-check owned cleanup totals49,152B; evidence retained.

## Pre-rework source CI complete and supersession boundary

Source Check41122715625 passed at exact1119bcdcf7db00a9bd91e84490d7a8de37c3575e,
watcherexit0/6m45s, no livehandle. Full status/log and result remain under
kb-final-source-evidence/. User subsequently approved shared per-type incident
escalation rework. This passing result is preserved for old1119source only; no
future generic-engine source/media acceptance is inferred. KB1119pins remain
unchanged until coherent final reviewed/published backend source; no interim
pin refreshes or heavy capture work. Original source/history receipts retained.

## Shared-escalation legacy impact confirmation

Legacy owner1 reports source complete and quick checks passed, pending owner0's
coherent combined commit. Two-concept/fourPNG map unchanged:
getting-started/vps-list and restore-backups/playground-vps-list, cs/en. The list
column now uses the API-localized registered type label, escaped by the WebUI:
VPS memory-pressure incidents / Incidenty přetížení paměti VPS. Existing zero
fixtures0/5+0/10 remain sufficient. No extra scenario.

Generic detail section and type row remain after unchanged first/base table,
outside existingh1+first-tablecrop. Existing semantic documentation IDs
vps.oom-summary/details/settings are retained for unchanged user intent despite
PHP/formaction incident_policy renaming. Verify final combined published diff,
not interim worktree, before pin/capture. No KBsource/pin/deps/build/runtime edits
made on this report; mandatoryaffectedreview+capacityrelease remain prerequisites.

## Lead capacity observation, no admission

Lead reports freshdf126GiBfree/87%used, materially improved by external host
activity beyond this package's measured49,152Bowned-temp cleanup. Do not attribute
that capacity change to this package or treat it as admission. No immediate extra
inventory/preparation requested. KBpin/prep/build/runtime/capture remain held until
final backend source/publish/review and actual exact-input budget, coordinated
with owner0's sequential allocations. Re-measure only at that concrete gate.
