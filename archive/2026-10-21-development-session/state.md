---
lifecycle: archived
---

# PHP mitigation status

Phase: merged; ready for user build and deployment.

## Phase checklist

- [x] Verify exact session identity and retained Full-team roster/access.
- [x] Record substantive plan and owner backlog.
- [x] Architect completes PHP/advisory inventory and design brief.
- [x] Implementers complete configuration changes and quick checks.
- [x] All intended changes committed; whole-branch inventory prepared.
- [x] Independent final review passed; user directed merge before system build completion.
- [x] Publish reviewed feature branch and hand off exact machine command.
- [x] Default-branch integration explicitly directed and verified.
- [x] User reports all eight machines deployed.
- [ ] Inspect actual deployed/built INI and administrative FPM settings.

## Current owners and next actions

Merged to remote configuration/master at38e7c837893695999e588a73f5d2a0088b8257b1.
Three commits:823ffe9 native exact release-26.05 stable pin;01213695 exact revert
of workaround;38e7c837 standalone Foto shutdown. User explicitly approved merge.
PHP source selected8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f (PR576865 merge).
All ten configured FPM/session runtimes evaluate8.4.27; Foto noFPM/legacy runtime,
server503, data/accounts preserved. Independent final review/all4lanes passed.
No builds/deployment by agents; user owns next pull/build/deploy. Site shutdown
and patched workers take effect on that later activation, not by Git merge.

### Follow-up phase checklist

- [x] Reverify session/roster/access and updated procedures.
- [x] Exact release-26.05 source SHA containing PR576865 pinned natively.
- [x] Workaround exactly reverted; Foto shutdown separate commit.
- [x] Ten fixed runtime evaluations/noFoto proof, hooks and quick checks pass.
- [x] Final independent review/history check passed without findings.
- [x] User-approved FF merge and exact remote proof; merge claim released.
- [ ] User build/deployment, intentionally outside agent scope.

## Coordination and evidence

Identity: `dev-session current` = `2026-10-21-development-session`; both environment
markers match the trusted thread binding and workspace path. Retained architect
and implementers are ready with saved workspace_write; reviewer is read_only.
Read required workspace routes and installed workspace-host coordination guide.
Shared workspace has substantial unrelated changes; preserve all of them.
Initial workspace resource claim refused because tracking-only workspace is not
registered as a feature repository. Use the required shared tracking flock for
this checkpoint; acquire configuration repository claim after its registration.

## Documentation

Design and implementation comments will capture mitigation scope. Individual
rollout and check evidence belong here, not configuration repository test reports.

## Repositories

vpsfree-cz-configuration: branch `2026-10-21-development-session`, worktree
`worktrees/2026-10-21-development-session/vpsfree-cz-configuration`, registered
initial base `86e19685313270d88e4db30038c056ce4b807abd`.
Implementer0 holds repository claim `6be8fc81-9164-489e-a607-8f21376cbde6`.
Release after Git effects are verified and no operation remains running.

## Setup checkpoint

Initial plan/state committed as da085022. Worktree creation reached base
86e19685313270d88e4db30038c056ce4b807abd but ambient checkout hook lacked pinned
gems; implementer0 owns recovery through the repository Nix shell. No hook bypass.
Plan/state are built-in portal artifacts (explicit artifact add correctly refuses).

## Runtime coverage checkpoint

Architect preliminary PHP hosts: int.blog, int.kb, int.utils, int.web,
int.webui1, int.webui2, int.webui-dev and aitherdev. Implementer1 independently
validated confctl brace-selector semantics and build+switch deploy behavior.
The candidate selector was corrected to eight hosts: int.vpsadmin-webui1 is
JS-only; an external qr.php image reference does not install PHP. Final
effective-value evaluation remains pending. Foto uses
independent PHP 5.6 and WordPress maintenance uses embedded PHP, requiring
explicit package-level coverage. Repository hooks now pass under pinned Nix
shell; no bypass. Vendor confirms critical issues but has not published enough
technical detail to independently verify mitigation effectiveness.

Implementer1 prepared php-runtime-coverage.md and validated pinned live confctl
selector syntax, exact eight-host output, deploy flags and generation semantics.
`--generation current`/numeric offset is supported; `latest` is not. Lead
accepted a session-local evaluator exposing actual pinned confctl evalConfigFor
for evidence rather than recreating configuration composition.
Watcher policy resolved from matching retained/installed catalog
ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376:
utilities.verification_watcher = gpt-6-luna/low; native utility
`dw_91978c240a6a43c2168b5be643cb58668a0bdf42d703ed0e`, execution full_access,
explicit danger-full-access/approval never. Launch only for required long check
when final review has passed.

## Accepted design

Architect design.md accepted: four source boundaries (FPM pool module, NixOS
module list, nested kb-staging import, narrow default php buildEnv overlay).
Overlay scope is justified by actual aitherdev/Composer/wp-cli CLI consumers;
FPM administrative setting covers independently sourced foto/DokuWiki packages.
No PHP source override or all-version override authorized. Implementer0 owns
four source files and one coherent commit; implementer1 owns effective runtime
and exact-selector evidence. No active source/Git overlap. Vendor source links
and mitigation uncertainty are in design.md. Intentionally stopped staging
container must stay stopped.

## Latest user scope correction

User said "let's not waste time with CLI". Lead stated focus on web-request
PHP/FPM. Implementer0 removed exact owned overlay/index change and notified
implementer1 to drop CLI work. Final deliverable is three FPM configuration
paths; aitherdev remains for staging FPM. Architect reconciling design.
Implementer1 stopped a legacy Foto identity evaluation that began import-from-
derivation source fetching; this is a verification limit, not a test failure.
Use bounded FPM option projections before review; defer uncached package
realization to post-review watcher build.

## Committed deliverable and final review

Final head 38687a8438a6e75b20a1924fb65d060a05217b06; single commit over registered
base 86e19685313270d88e4db30038c056ce4b807abd. Three paths, 21 insertions; no
migrations, repeated dependency streams, superseded commits or CLI overlay.
Quick formatting/parse/diff checks and normal commit hooks pass. Independent
11-pool effective settings evidence confirms Off/admin false. Full inventory
and final diff are in review-packet.md and configuration-final.diff.
Risk high (security/host behavior/rolling deployment). Reviewer0 retained
Sol/xhigh, read_only, all four lanes, no fallback. Long builds remain gated on
completed review. No deployment, merge or readiness claim yet.

## Publication and ownership evidence

Implementer0 completed normal pinned Nixfmt pre-commit and commit-msg hooks;
72-column recommendations were nonblocking and all commit lines obey required
80-column limit. `nixfmt --check`, `nix-instantiate --parse` on all three paths,
and staged/final base-to-head diff whitespace checks passed. Fresh origin/master
still 86e19685313270d88e4db30038c056ce4b807abd. SSH-published branch and verified
exact remote head 38687a8438a6e75b20a1924fb65d060a05217b06 with ls-remote.
Checkout clean, one commit ahead/zero behind; no push-triggered CI (only scheduled
or manual daily-update). Config claim 6be8fc81-9164-489e-a607-8f21376cbde6
explicitly released after no command remained running. No merge/deployment.

## User integration authorization and fast-track verification

User: "okay, fast-track verification, we can check it by building just one
 affected machine. then merge it". This authorizes integrating the affected
vpsfree-cz-configuration feature into its default master after checks. Lead
confirmed that repository/target to user. Verify only int.kb full system build
as representative machine after final independent review; retain existing
all-11-pool configuration evaluations. Stop optional runtime probes. Production
deployment remains unrequested; final handoff supplies exact eight-host command.
No workspace feature integration authorized or needed.

## Final independent implementation evidence

Implementer1 complete: php-runtime-coverage.md reconciled to FPM-only scope,
exact final head and snapshot /nix/store/2q5ar7wpdivcz06vvibqc8bc7k6rvnm2-source.
All 11 pools pass final directive/admin/raw-config/no-conflicting-key checks;
Apache PHP false and nested autoStart false. Metadata for 10 ordinary PHP 8.4.26
pools and shared etc/php.ini/lib/php.ini inspected. Foto package/ExecStart
metadata remains uninspected due uncached IFD; its effective option settings
pass. No optional runtime/request probe launched after fast-track instruction.
Actual HTTP/service runtime behavior awaits operator deployment. Coverage,
settings and runtime metadata artifacts registered in portal.

## Final review passed

Reviewer0 retained Sol/xhigh completed all four lanes at exact final head with
no findings. Full history/no repeated streams/no migrations explicitly accepted;
review.md preserves report and limitations. Independent snapshot comparison:
474 tracked blobs identical to exact committed head. Proceed with one int.kb
build per user fast-track direction, then approved master FF integration.

## Representative build invocation correction

First watcher attempt ran int.kb build once and stopped before build work at
confctl's confirmation prompt (EOF, exit 1). No configuration failure diagnosed.
Lead checked pinned command options: build has --yes switch. Fresh watcher
will run `nix develop -c confctl build --yes cz.vpsfree/containers/int.kb`.
Original log/result retained; no retry inside watcher. Build only, no deployment.

## Latest user direction: merge now

User: "merge it, I want to deploy it". Lead confirmed merge now and disclosed
standalone system build has not completed. Final review/all11 config checks
passed. No further long build launched. Deploy command builds before activation.
Integration package assigned to implementer0 for config/master only: fresh claim,
fetch/exact reviewed range check, comparison capture, normal-hook FF merge/SSH
push, exact remote verification and explicit release. No production activation.

## Final outcome

MERGED: remote master and retained feature branch both exactly
38687a8438a6e75b20a1924fb65d060a05217b06, SSH push and ls-remote verified by
implementer0. Fresh fetch base unchanged; final complete one-commit/three-path
diff matched independent review; no rebase/head change, obsolete history,
migrations or repeated streams. Comparison captured before integration. Normal
checkout/post-merge/pre-push hooks completed in pinned Nix environment, no bypass.
Integration claim 24889ff0-c3ce-4f82-9202-27f968603604 released revision 2;
no running operation. Clean detached integration worktree retained at
worktrees/2026-10-21-development-session/vpsfree-cz-configuration-integration
per urgency; feature worktree/refs retained. Session remains open; no lifecycle
action authorized or performed.

Reviewed and configuration-checked; no successful system build or deployment
claimed. User's latest direction superseded waiting for the single system build;
first attempt stopped at confirmation prompt. Deploy builds before activation.
Remaining operator action: update configuration checkout and run:

```sh
confctl deploy --one-by-one 'cz.vpsfree/{containers/int.{blog,kb,utils,web},vpsadmin/int.{webui-dev,webui1,webui2},machines/aitherdev}' switch
```

Eight machines/11 FPM pools; no PHP CLI change. Mitigation efficacy for the CVEs
unconfirmed by vendor technical disclosure. Actual worker/upload/session checks
remain operator post-deploy work. Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-development-session/

## Post-deployment verification request

User: "ok, all deployed. now you can check that the build contains the appropriate
php ini setting". Identity/ready roster reverified. Read-only verification of
actual deployed/store artifacts assigned to both implementers using existing
design. No new code/deliverable review needed for routine verification evidence.
Previous evaluation-only limitations must be distinguished from new artifact
proof. Production deployment itself remains user-reported until remote current
system identities are inspected. No claims required for these read-only checks.

## Actual artifact verification finding

Implementer1 reached aitherdev read-only: selected host system
/nix/store/vq63sg427gay6wb9w41ixnv6hza88izk-nixos-system-aitherdev-26.05.20261019.f3a73bc
references nested staging system
/nix/store/7psqfgnz602qlhg935fy5rbc6il8jqkw-nixos-system-kb-staging-26.05pre-git.
Both nested FPM units reference actual generated INI
/nix/store/6a856s7i2cgn3wkaaylm6l8nl9rasn7q-php.ini with no active Off assignment;
their actual generated FPM configs lack the administrative upload-progress flag.
Current selected nested build therefore lacks our module settings; scan-chain
check/current-vs-running distinction pending. Staging was already active; no
state changed. User informed; cannot claim rollout verified.

Other service hosts: direct IP/pinned FQDN SSH fail host-key verification; no
keys accepted or checking weakened. Exact-head evaluator-derived config output
paths are absent from this local store. User asked asynchronously where deployment
ran (machine/checkout path), while reachable staging investigation continues.
No new build, source, Git or deployment mutation performed.

## Final actual-build verification checkpoint

Both implementers completed read-only packages. Staging FAIL confirmed across
actual -c INI, -y FPM config, includes, wrapper scan INI and unit environment:
no active Off or admin flag in selected aitherdev nested build. No live worker
probe. Seven other machines UNVERIFIED: SSH host-key checks block access and
exact expected generated outputs absent locally. Full summary and linked
per-owner evidence: deployment-verification.md. User informed and asked where
(machine/checkout path) deployment ran. Remaining work depends on that provenance
or trusted artifact access. No source/build/deploy mutation, no held claims.

## User accepts private staging exception

User: "that's ok, aitherdev is not publically reachable". Record the absent
workaround in the selected aitherdev staging build as an accepted private-host
exception; do not pursue its deployment or change the running container.
Seven public service machines still lack actual-build verification. Remaining
blocker is deployment machine/checkout provenance or trusted artifact access;
previous request for that information remains unanswered. No source/deployment
changes or new tests required by this acceptance. Session remains open.

## New follow-up branch/provenance

Implementer0 refreshed clean session feature onto current origin/master
37a338b25192d9271ee211110800c2dc6a094a57, no unmerged commits yet and no rewrite
of prior merged history. Stable role maps nixos-stable/nixpkgs to nixpkgsStable,
current cd4ea8d57de16f4810bc5f14207bac45fbf19f67. Correct native exact-revision
setter verified; manual lock changes prohibited. Selected installed runtime now
uses short repository merge claims only; feature preparation/updates/hooks/
commits/pushes take no durable repository claim. No claims held.

Mechanical exact pin unblocked as bounded direct lead brief to implementer0 while
architect finishes substantive workaround-removal design: native setter for
8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f only, no open interface/design choice.
Source removal remains gated on design. Exact user-clarified release-26.05
head/PR merge and independent runtime evidence plan recorded; no builds.

## Accepted fixed-version brief

Lead accepted architect's current design.md / php-fixed-version-design.md.
Two commits: generated stable lock update; remove global module/imports and
retain exact Off/admin false only in existing Foto config. Expected ten stable
pools use PHP8.4.27. Vendor fixed floors are8.2.35/8.3.36/8.4.27/8.5.12;
CVE disclosure says upload-progress workaround incomplete, so Foto remains
unpatched with only partial precaution. No PHP/System build or deployment.

## Native selected-source pin complete

Commit823ffe9cd1bbbf6dd708f756211d4d0d55913bc6 native-generated pin; normal
hooks pass, generated message preserved. Actual lock diff only nixpkgsStable
locked revision/hash/timestamp; source selected8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f.
No transitive/original/channel-policy edits. Functional four-path patch applied:
remove global module/two imports; retain mkAfter Off/mkForce admin false on Foto.
Independent final runtime checks underway against new pin/source. No builds.

## Foto disablement scope change

User: "hm, so disable foto.vpsfree.cz temporarily if we can't update it. the
workaround isn't enough to fix the issues." Source-only disablement authorized,
no actual activation. Implementer0 stopped publication; obsolete functional
commit6cf8c9e2a67908874e343682c088ed190749529a was local/unpublished and will
be amended to final disablement. Native pin823ffe9c retained. Source brief
supersedes Foto-only partial workaround. No earlier merged history rewritten.

Architect current design now approved: Foto hostname retains domain/ACME/SSL
settings and uses server-level return503; root/locations/FPM/php56 fetch/import
and cleanup pool registration removed. Accounts/data remain; no deletion or
live activation. Ten fixed pools expected, no workaround remaining. Native pin
plus final functional commit only; obsolete unmerged Foto workaround removed
through normal owned amend. User-facing maintenance prose not introduced; nginx
standard response suffices. Full design.md current section supersedes historic
Foto-only plan in php-fixed-version-design.md.

## Latest commit split and integration authorization

User: "hurry it up. the workaround commit should be jsut reverted.
foto.vpsfree.cz disabled in a standalone commit"; then "merge it when done".
Final series THREE logical commits: native stable pin823ffe9; exact revert of
merged38687a original mitigation; standalone Foto shutdown. Implementer0 owns
unmerged history consolidation and verifies final tree equal55ed38c candidate.
Combined functional55ed38c was briefly feature-published, never merged; owned
force-with-lease rewrite allowed to honor explicit split. Preserve earlier
merged history. Mandatory final reviewer follows final commits/quick checks;
no review assigned prematurely. After pass user explicitly authorizes affected
vpsfree-cz-configuration/master FF merge+SSH push, no builds or deployment.
Independent eval passed final source: ten8.4.27 pools, noFoto or workaround,
nginx503/no root/locations and preserved accounts; final commit identity pending.

## Final three-commit deliverable ready for review

Head38e7c837893695999e588a73f5d2a0088b8257b1 over base37a338b25192d9271ee211110800c2dc6a094a57.
Three commits native823ffe9 / exact revert01213695 / standaloneFoto38e7c837.
Normal hooks and parse/format/range checks pass. Exact final tree8a42d008 equals
evaluated55ed38c tree. Ten patched8.4.27 pools; noFoto runtime/no workaround,
server503, accounts/data preserved. Full packet/diff/evidence ready. Feature
published exact head, clean detached target prepared and comparison captured;
no merge claim until review accepted. No migrations/repeated pin streams or
obsolete unmerged ancestry; previous already-merged history preserved.

## Final fixed-PHP review passed

Reviewer0 Sol/xhigh/read_only all4 lanes/no findings at exact38e7c837. Full
three-commit history, exact revert, one pin stream, no migrations accepted.
Independent473blob snapshot equality and tenpatched runtime evidence accepted.
No builds/probes; user owns. php-fixed-review.md preserves report. Implementer0
instructed execute approved prepared FF/SSHmasterpush under short merge claim,
verify exact remote head and release immediately. No deployment.

## Fixed-PHP final integration evidence

User "merge it when done" approved configuration/master, exact three-commit
scope. Implementer0 merged reviewed38e7c837 into unchanged target37a338b,
normal FF/hooks and SSH push passed, no rebase/source change. Exact remote
master and retained feature both38e7c837893695999e588a73f5d2a0088b8257b1;
lead independently read remote same exact head. Merge claim
c358cf9a-ee47-43cc-a7b0-9f8e069617b5 released immediately after remote proof,
no operation running. No builds/probes/deploy/data mutation/cleanup performed.
Feature refs/worktrees retained; session left open. Final review packet/report
and independent PHP/version/treebinding evidence registered in portal.
Next operator action: pull configuration/master, build and deploy complete
series together. Foto returns503 only after later activation; no live state
changed in this follow-up. Stable source8c259fc0 includes PHP8.4.27 fixes.
