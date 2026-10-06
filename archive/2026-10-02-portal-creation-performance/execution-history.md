# Historical implementation and verification checkpoints

These notes preserve earlier execution checkpoints, including superseded heads,
prepared operations and unresolved statements at their original time.
[state.md](state.md) is the authority for current status. Curated review,
measurement, observation and rollout records provide final evidence.

## Identity and ownership

This parent had no environment or trusted existing session binding;
`dev-session current` reported none. It created this separate owned initiative.
Initial substantive tracking commit `8762bd33` preceded source/external mutation.
Root thread `01a0fd0b-f0bf-77f2-814b-f1f2af67a094` is idle for parent coordination.
Retained members: architect0 Astra/xhigh/workspace_write; implementer0
6.1-sol/xhigh/workspace_write; reviewer0 6.1-sol/xhigh/read_only.
Live saved identities/settings are checked before assignments.
Catalog digest: `4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17`.
Fresh utility watchers use catalog Luna/low/operation, maximum one at a time.
Shared master/index/unrelated files, other sessions, branches and staging are
preserved. No migrations or persisted format changes were introduced.

## Exact branch inventory

All feature branches: `2026-10-02-portal-creation-performance`. All registered
worktrees: `worktrees/2026-10-02-portal-creation-performance/<project>`.

| Project | Final feature head | Verification |
| --- | --- | --- |
| codex-web | 4c170393a96ed0a6ac2e43488d073f6fcab36132 | Four review lanes clear; CI37024785401 passed |
| dev-workspace | 924c0ec28c41dd8b56aaf17f2212b302ca614899 | Four correction review lanes clear; CI37063660861 passed |
| vpsfree-dev-workspace | 8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 | Corrected pin review clear; CI37064115624 passed |
| workspace | 1b670e0329c80b5ed266f6edb92ac2096134677c | Corrected pin review, package build and flake checks passed |
| vpsfree-cz-configuration | 3d26ec396ceb935a233bdda3079618821d099b3e | Corrected pin review, host build and dry-activate passed |

All five feature branches are published over SSH. Comparisons captured for all
exact heads. SDK has one capability commit. Runtime has three commits: SDK pins
`dfda7b8`, locked freshness/recovery `4262bb2`, and receipt progress `924c0ec`.
Each consumer has one pin commit. No obsolete approach, unused compatibility
path, follow-up fix or migration remains. Whole-branch histories and no-migration
conclusions are in the review results. Workspace cleanly rebased onto shared
master `508064ed`; intervening changes were unrelated coordination records.
Final narrow correction and pin consolidation: [remediation.md](remediation.md).

Configuration channel `dev-workspace`, role `devWorkspace`, updated with confctl
`--commit`; installed Overcommit passed. Its generated changelog received an
intentional correction to the final consolidated target. Parent proved only
intended generic/SDK lock nodes changed, plus extension in workspace. Both
consumers select exact runtime `924c0ec` and SDK `4c170393`. Codex0.160.0,
llm-agents, providers, Full catalog and host paths are unchanged. Deployment
checker passed canonical portal identity and exact generic lock metadata.
The application remains a user-profile package, with no system application pin.

## Verification evidence

SDK focused wire/default/filter/corpus/generated0.160 schema checks passed in7s;
full exact-head CI37024785401 passed. An initial Nix attempt stopped before tests
because GOFLAGS selected absent vendor data; explicit `-mod=readonly` resolved
it. Lesson: notes/codex-web/2026-10-02-nix-develop-go-module-mode.md.

Corrected runtime focused checks passed in51s: selected Go creation/recovery/
progress/fork packages,60 Ruby tests/624 assertions, syntax and diff. The first
attempt failed after151s because a fork fixture did not answer the existing SDK
source-idle `thread/turns/list` RPC. Implementer corrected the fixture preserving
source validation. All21 checked source checksums matched after commit split.
Final full runtime CI37036484407 passed at `8ae46f9`; final extension
CI37036675532 passed at `4f817322` (13m2s). Earlier full CI runs remain historical
evidence. No host VM module logic changed.

Independent reviewer0 actual native context confirmed6.1-sol/xhigh/read_only.
SDK and runtime each passed all four lanes with no Blocking/Important findings.
An Advisory on the prototype no-tool guard was corrected by the architect;
parent inspected selected0.160 ResponseItem contract, AST/hash and29 focused
in-memory assertions. Prototype SHA256:
`85f0dca8a3b39bbeb0e53b1dcb4973bd31927a22643999bfde01751fad3ff30f`.
Extension and final consuming-pin general/risk supplements found no findings and
confirmed clean whole history/no migrations. See review-sdk-result.md,
review-runtime-result.md, review-extension-pin-result.md and
review-final-pins-result.md.

The first packaged batch passed flake checks/build, then browser acceptance
failed with12 null querySelector errors. Parent traced missing pending/queue
status markup in the interactive plan fixture to unchanged production catch
handlers. Implementer added the two exact template paragraphs; strict page-error,
progress and elapsed assertions remain. Fresh browser verification passed in8s.
Parent directly inspected this test-only correction under mandatory review
step9; unaffected lanes did not need reruns. [remediation.md](remediation.md)
records the exact fixture hash, history consolidation and final pin proof.

Fresh `final_acceptance` Luna/low owns one related batch: exact-head generic/
extension CI plus final consuming package/browser/history/fault/host build.
Both CIs and final package/browser checks passed. Isolated seeding completed
3,379 active/0 archived genuine rollouts,208,256,155 bytes in2,109.264s.
The batch exited1 because its schema2 workspace fixture omitted required
sshHost. No timing samples, faults, private runtime launch or host build ran.
Parent inspected the strict supported loader and assigned architect0 a narrow
prototype correction/guarded continuation, preserving failure evidence and
acceptance gates. No parent duplicate polling. Full private logs/status and artifact
metadata stay under ~/.local/state/dev-workspaces/verification/
2026-10-02-portal-creation-performance/; synthetic runtime evidence is under
/tmp/pcp-oct02-a. No credential/history content is copied into tracking.

Final consuming candidate:
`/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0`.
Parent read completed build metadata once and proved its Codex executable equals
installed9g8's executable, and its Full catalog digest/settings match the
retained site catalog with3 members. Private live-canary preset prepared.
No timing, activation or canary result is claimed yet.

Independent aitherdev build first stopped at confctl confirmation EOF, exit1,
before building. Parent inspected the exact single-machine target and local
help: build supports --yes, while --no-interactive is deployment-specific.
Fresh host_build_confirmed Luna/low owns the authorized corrected
`nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev` at exact4123.
Both attempts retain separate private log/status files. No activation.

## Documentation and next actions

SDK docs/reference.md and runtime docs/dev-sessions.md/workspace-portal.md own
optional index behavior, locked freshness, complete retry scans and progress
semantics. Parent applied the user-facing writing skill directly. Session
[design.md](design.md), implementation-sdk.md and implementation-runtime.md
record accepted design and implementation evidence. Individual ordered deployment
and recovery are in [rollout.md](rollout.md). Real-package verification brief and
prototype are [verification-prototype.md](verification-prototype.md) and
[verify-creation.py](verify-creation.py).

Baseline:103.546s acceptance-to-ready;98.212s filesystem discovery versus4–7ms
indexed discovery. Fresh new/approved-plan/fork paths skip discovery only under
existing creation/slug locks. Every retry adoption or replacement retains a
complete scan. Final normal proof and upload binding still authorize ready;
progress cannot do so.

Inspect the corrected prototype and continuation proof, run a fresh watched
five-sample/fault/build batch, then dry-activate the owned
aitherdev configuration and inspect before host switch. Use the installed
workspace-host to select the same consuming application package from its user
profile. Pre-activation snapshots retain36 active root IDs and the owned Full
roster. App Server, portal, router and tmux services were active at snapshot.
Respect lifecycle journals, generation and idle refusals. Recover software with
a newer forward revert generation. Retain all canaries/private services and
branches; no cleanup or lifecycle retirement was authorized.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/

Corrected aitherdev build passed exit0 in108s at exact4123d883. Confctl built
generation2026-10-02--19-44-24; no local kernel build. Fresh watcher completed
and retained full host-build-confirmed.log/status. No activation has run.

Architect prepared exact pre-registration --resume-seeded continuation, with
required sshHost:"" fixture, single-use claim/preserved failure evidence and
unchanged timing/model/progress/fault gates. Read-only actual3379-history
preflight passed in9.32s;50 focused guard/history/main/preservation checks
passed. Prototype SHA256d31623c6cd4ee3f0a3ae5f7de387c8727efeefecee1db303dc9151802612f481.
See verification-resume-preparation.md. Same retained reviewer0 assigned a real
new four-lane turn scoped to this new private continuation design; application
heads remain clean/unchanged. No timing or activation result yet.

Parent confirmed unrooted candidate0klh7 disappeared. Fresh candidate_retention_build
re-realized unchanged workspace461bedfb with --out-link candidate-root; exit0
in about4m10s, exact output0klh7 restored/rooted. Build phases passed including
348 Ruby runs/3662 assertions,0 failures/errors,12 skips. Private log/JSON/status
preserved. Candidate-root outside exact /tmp evidence remains a GC root.

Retained reviewer0 four-lane seeded continuation review completed without
findings at artifactd31623c6; actual turn context confirmed6.1-sol/xhigh/read_only.
Report: review-seeded-continuation-result.md. Fresh seeded_creation_acceptance
Luna/low owns exactly one guarded continuation via prepared script; full private
seeded-acceptance.log/status. Original failures remain preserved; all five
samples/fault gates enabled. No activation or timing result yet.

First guarded wrapper exited1 before claiming or changing private fixture,
with `cannot exclude an owned process from the private fixture`. Parent
inspected current log; unchanged old result still reports initial register
failure and is not this attempt’s cause. Global /proc scan encountered
unreadable cwd of same-UID user systemd4239/sd-pam4242. No continuation claim
or runtime was created. Architect0 assigned narrow deletion of unrelated
process enumeration, retaining exact seed PID/socket/strict private-record
proof and all acceptance gates. Direct reduced-scope remediation to be
inspected under mandatory review step9; no application changes.

Narrow process-guard correction inspected directly: only
require_no_seeded_services changed, deleting global same-UID /proc enumeration.
Exact recorded seed PID/socket/strict inventory proof and all acceptance
helpers/gates remain. Architect56 focused checks/AST passed; current SHA256
57c28957b019ddba36cebf2ae650c30bd1a9fcc2468be7077da4e9544c367b28.
Parent actual read-only preflight passed9.447s/3379 histories/no writes.
Fresh seeded_creation_corrected utility owns the same corrected acceptance
operation; full private seeded-acceptance-corrected.log/status, no initial
claim existed. Review step9 direct reduced-scope verification needs no
unaffected lane rerun. No application head or activation changed.

Corrected guarded run reached real private register/profile/config/normal
workspace-host run-codex, then exited1 at an incorrect prototype executable
assertion before tmux/portal/warmup/measurements. Parent inspected actual
processes.json: app-server PID1687746 started18:14:22.525450Z, real native
entrypoint a29lfsrd.../libexec/codex/bin/codex. Selected public command is
the same package’s bin/codex shell launcher. Its supported layoutVersion1
manifest declares native entrypoint bin/codex; runtime package is correct.
Current result records this cause; original register failure is durably
preserved under seeded-continuation. Registry/profile/config/genuine markers
and live App Server retained, zero model goals/sessions created.

Architect0 assigned a bounded native-manifest identity correction and thin
one-time pre-portal follow-on driver reusing original setup/acceptance functions.
No App Server relaunch, old claim clearing, application changes, settings
changes or gate relaxation. New follow-on design receives affected-lane
independent review before fresh watched execution. Host/application activation
remain pending real timing/fault evidence.

Parent captured exact retained App Server PID1687746 kernelStartTicks1027257437,
boot ID/native executable/cwd/cmdline digest/socket inode and setup-file digests
in private benchmark-started-proof.json outside the fixture. Executable matches
selected a29 package manifest; cwd equals original spawn root /tmp/pcp-oct02-a.
Architect tool namespace cannot inspect host /proc; driver must validate the
parent-supplied proof during host execution rather than guess ownership.

Parent read-only preflight refused before claim or mutation because the harness
expected a direct socket at the advertised App Server path. Parent initially
misinterpreted its mode/type and proposed a proxy explanation; direct host
inspection and exact Codex0.160 upstream transport source disproved that
explanation. The normal advertised path is a symlink to the protected daemon
socket. Its resolved target retains the original saved inode/dev/UID/mode0600,
and original PID1687746 owns its listening kernel socket. The original process
proof had captured stat() of the target; the driver used lstat() of the alias.
No alias or backend replacement occurred. Architect0 is correcting that exact
continuation guard using both retained target proof and a new private alias
metadata proof; no private fixture, process, claim or original proof is changed.
See the selected release source:
https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server-transport/src/transport/unix_socket.rs.
All application heads and acceptance gates remain unchanged. Parent actual
preflight and affected-lane independent review remain prerequisites to the
single watched continuation.

Corrected started driver721de6f0 and main4a483d39 passed AST/compile and actual
read-only aitherdev SSH preflight in10.447s: all3379 rollouts, exact retained
PID/native identity and both original-target and alias/listener proofs passed.
No claim or private mutation occurred. Retained reviewer0 assigned real new
four-lane affected-design turn; saved6.1-sol/xhigh/read_only reverified. Packet:
review-started-continuation.md. Main acceptance helpers/extracted blocks and
all five project heads remain unchanged. Prepared one-use watched command
selects these exact hashes, candidate GC root and runtime8ae before execution.

Started-continuation four-lane review completed with no Blocking/Important/
Advisory findings at main4a483d39/driver721de6f0. Parent verified actual native
reviewturn01a0fe00-6b9a-75a0-be6e-7821a32f8a1b as6.1-sol/xhigh/read-only and
preserved the full public report in review-started-continuation-result.md.
Architect77 focused checks and actual3379-history preflight passed. New fresh
Luna/low utility owns one exact host continuation, retaining current command
log/status separately from prior setup failures. Timing/fault gates unchanged;
no outcome or activation is claimed before its result.

First started-acceptance wrapper exited1 in0.73s before Nix/driver execution:
its head guard called git outside the declared shell, absent from sudo PATH.
Parent inspected the current log and proved result hash unchanged/no
started-continuation claim. Original log/status retained. Parent moved head/
artifact checks into runtime Nix shell in a new private environment wrapper;
source prototype hashes and all review/acceptance gates are unchanged. Fresh
Luna/low operation will own the corrected wrapper with separate evidence.

Corrected environment wrapper entered Nix and the reviewed driver, claimed
started-continuation and launched genuine private tmux1798536/portal1798541
with retained App Server1687746. Warmup ready at19:17:01.9965352Z, accepted
19:16:54.765656829Z (7.230879s). Root01a0fe0c-52c2-76e1-98bf-f11e1455623a;
Full three member IDs/settings preserved. Model first assistant19:17:06.347Z,
completed19:17:06.396Z. Current result incomplete because wait_model counted
event_msg.user_message (zero in selected rollout). Parent read-only own-root
metadata proved canonicalresponse_item userinput_text GOALcount1, taskstarted1/
completed1 and no tool calls. Two other input_text parts are normal AGENTS and
environment context. This is a harness counter defect, no duplicate submission.

Parent assigned architect0 canonical0.160 counter correction plus smallest
one-time after-warmup continuation with shared unchanged five-sample/fault tail.
No goal resubmission, servicesrestart, reseed, claimclearing or auth read/copy.
All original claims/failure evidence retained. Parent captured private
benchmark-warmup-proof.json (SHA42c582ce94c42d27454cd65ae11094b822a657ffc8acac9ca0f39566a9ae36a9),
only actual process/socket/file metadata and ready receipt/roster/manifest hashes.
Direct counter remediation uses focused inspection; new follow-on/extraction
receives affected independent review before fresh watched execution. All five
application heads remain unchanged.

Parent inspected saved warmup progress metadata once after watcher completion.
All16 begin/finish frames were present: prepare80ms, conversation497ms,
terminal474ms, member architect798ms/implementer845ms/reviewer1513ms,
prompt1469ms and final evidence8ms. Live receipt polling observed individual
stages before ready. This confirms useful progress and a cheap fresh conversation
on this retained warmup; it does not substitute for five measured samples/faults.

Canonical counter actual read-only warm-up model/receipt/roster/progress check
passed: GOALcount1, no tools, completedturn,16frames. Firstassistant11.581344s
afteracceptance/4.350465s afterready. No resubmission or new request. Whole
after-warmup preflight caught inherited preportal config digest (normalTUI
screen_reader_detection_done) then overly broad socket-path uniqueness
(accepted client streams share listener pathname). Parent supplied exact current
noncredential config hash and proved original FD30/kernel355192150 LISTEN plus
ordinary connectedstreams. Architect narrows these bounded prototype guards;
all original process/alias/target proofs, failures and claims remain unchanged.
Actual full-driver preflight and affected independent review remain pending.

Parent deployment preflight found the previously built host output missing from
the Nix store. Its generation metadata and exact derivation remain recorded.
A fresh utility will re-realise the same derivation with a private GC root; no
source or pin change, host activation or new generation selection is involved.
The application candidate root remains valid. Removal cause is unconfirmed.

Exact derivation re-realisation exited1 in22s because that derivation was also
absent from the Nix store. Parent preserved host-retain.log/status and selected
a normal exact-head confctl rebuild followed by retention of the original
toplevel output. No activation occurred; no unexpected kernel build started.

Fresh host rebuild/retention passed in99s, exit0, producing the same generation
2026-10-02--19-44-24 and toplevel jpv50m4a7p47jhmzb99ybl478aa3r1s7.
Parent verified its private host-candidate-root resolves to that exact existing
output. Both application and host candidates are now retained; no activation.

Completed warm-up continuation review: reviewer0 actual new turn
01a0fe2c-090a-73b1-a59a-81766896775a, saved6.1-sol/xhigh/read_only,
all four affected lanes/high risk, no findings or fallback. Full public report
and actual final/settings evidence: review-warmup-continuation-result.md.
No unaffected application branch review rerun or unexecuted outcome certified.

Watcher milestone: all five measured creations completed their readiness and
model gates. Reported ready values rounded to milliseconds: 6.121, 6.401,
6.333, 6.501 and 6.428 seconds. Approximate median6.401/max6.501 meet
accepted thresholds. Both faults remain running; parent has not accepted the
whole result or activated either package. Exact metadata will follow completion.

## Measured result and diagnosed recovery failure

Continuation ran once, wrapper exit1 in90s. All five measured creations completed:
6.1212148666, 6.4013488293, 6.3327300549, 6.5007338524, 6.4283411503 seconds.
Median6.4013488293/max6.5007338524 pass. First-assistant offsets after acceptance:
11.7624390, 11.3165598, 10.6208901, 11.3227859, 10.8633192 seconds.
Every sample has one canonical initial request, completed model and no tools.

Lost-response helper1892775 created root01a0fe38-b8e0-76c1-b8f0-fd84783964a5,
then withheld its successful JSON from Ruby as designed. Receipt
 a4ad299484ab1972eb099a9b08793976cc442dc0ce8bae6fa768bba282e37634
failed attempt1. Retry2 ran loaded/index and complete filesystem discovery
(11.2 seconds), then failed exact RPC -32600/no-rollout error. No additional
retry, state reset or activation occurred. The member fault did not run.
Current result remains incomplete; five-sample timing evidence is retained.
Architect0 new actual turn01a0fe3b-4fce-7e92-b8ab-fe3e1434feb4 owns design.

Architect selected-source trace corrected the parent initial hypothesis: the
error arises from thread/resume, which requires a persisted rollout even for a
loaded root. Thread/read handles missing-rollout separately. No SDK predicate
change has been made or assigned. Preserve strict disappearance proof and live
identity; design examines first-turn policy instead. The earlier suspected
error-classification mismatch is superseded, not an accepted implementation.

Parent accepted recovery-design.md. Implementer0 actual turn
01a0fe49-8c6f-7be0-822c-d33c19d3a53b owns bounded runtime source/tests/docs
and consolidation into the existing unmerged core commit. SDK stays unchanged.
Architect0 has a new prototype task to assess the configured @portal_command
Go-provider interface for mixed old-consumer/new-provider fault verification
while the existing private profile/generation and all runtime identities stay
unchanged. No such boundary or driver is accepted/executed yet; no profile
switch, bypass, retry or fixture mutation is authorized by its preparation.

Committed runtime correction head924c0ec28c41dd8b56aaf17f2212b302ca614899,
core4262bb2 and unchanged SDK-pin dfda7b8; progress patch remains equivalent.
Five owned files only, final tree equals the checked snapshot and worktreeclean.
Ruby47 runs/558 assertions passed in10.39s, four tmux environment skips. Member
Go sockets were blocked by setsockopt permissions; parent actualhost Nix focused
protocol check passed exit0, package0.278s/0.076s. Parent main-context writing
pass confirmed settled docs before commit. No source SDK/pin/protocol/schema
change. Consumer branches still pin8ae until publication; prior CI does not
certify924. Complete source inventory/review: review-loaded-root-correction.md.

Loaded-root whole-branch review completed at924c0ec: actual reviewer0 turn
01a0fe5b-e7ec-7830-a92b-4a172c0247c1, saved6.1-sol/xhigh/read_only,
all four lanes/high risk, no findings/fallback/overrides. Complete series,
no-obsolete-history and no-migration conclusions preserved in
review-loaded-root-correction-result.md, including MCP fixture clarification.

## Corrected consumer publication and preflight

Extension8f8d8ec, workspaced74680d and configuration3d26ec3 published with exact
old-head force leases; unrelated refs preserved. Workspace lock changed only
extension/runtime nodes from its previous pin. Config's two generated updates
were folded into one owning input commit; final tree equals generateda88eb21.
Its intentional changelog correction names the original40838aa2→final924c0ec
range. Active Overcommit passed. Rebase base40289e3 contains unrelated default
host updates; earlier reviewed pin patch remained equivalent. Final deployment
contract passed. Review packet: [review-corrected-pins.md](review-corrected-pins.md).

Actual host old-provider observation was read-only and returned exact-root
thread-not-loaded, exit1. That is uncertainty, not replacement proof. Original
fault/root/journal and consumed claims remain untouched. Architect0's metadata
observer and continuation design are pending. The prepared fault driver has not
claimed or run; original five samples remain original8ae46f9 provenance.

Corrected pin review completed at final workspace1b670e03/base58df04cf: no findings, coherent locks, clean full series, no obsolete history or migrations. Actual reviewer0 context6.1-sol/xhigh/read_only verified. [review-corrected-pins-result.md](review-corrected-pins-result.md) preserves full public final. Fresh Luna watcher corrected_consuming_builds owns final application/checks, host build/roots and exact extension CI37064115624; no activation launched.

Actual pinnedSDK root probe completed read-only: loaded-list targetfalse; read and turns APIs return exact-target thread-not-loaded. No live-root/idle/materialization proof now. [root-observation.md](root-observation.md) records exact source/result and preserves uncertainty. Old prepared fault driver stays unexecuted; architect0 prepares fresh exact cases, no old retry/replacement or sample replay.

Corrected application xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2 built/rooted; all consuming flake checks passed. ProviderSHAac2bf71e98d1bafb4357bbf0bb7b7d1140f0bb4a1a903147cff67790284e9c4c; Codex/runtime-contract/catalog byte equality confirmed. Aggregate corrected-builds exit1 was host retention only. Parent corrected watcher report: candidate identity JSON/root DO exist and are printed in full log. Git author diagnostic did not cause test failure.

Host Nix output4wa4aiamhn1cm63j7gsaiqdqfn0f9ign built, but confctl GC-root creation used Etc.getloginroot under rootSSH (actualuid1000/loginuid0), causing permission refusal. Normal local tool shell uid/loginuid1000 supplies aither login; fresh watcher will rerun only host step there with explicit preflight. Source/pins unchanged; no product workaround, root-directory change or loginuid override. Original failed log/generation preserved. Lesson: notes/confctl/2026-10-02-ssh-login-identity-gcroot.md.

Host build passed69s in correct local login. Its wrapper exit1 came from parent retention glob counting current symlink as a duplicate generation. Parent corrected finite directory selection and retained the already-built exact output without another build. Generation2026-10-02--23-26-29; toplevel4wa4aiamhn1cm63j7gsaiqdqfn0f9ign; corrected-host-identity.json/root confirmed. Both final candidates retained; no activation. Exact extension CI37064115624 success verified.

Host dry-activate exactgen2026-10-02--23-26-29 returned0 (parenthandle44206 and status). Observer reported incomplete because noninteractive log lacked service/health detail. Parent directly checked confctl activation/raise/controlflow and accepts command success; no additional health or real activation claimed. Faults, host switch/profile switch/canary remain.

Actual host metadata-only fresh-fault preflight passed at21:45UTC. Exact hashes match new brief: mainafd95a7d, driver1a4ffad2, tests34cf3982; final providerxl9/ac2bf71e, original process/socket/profile/records intact. Seven in-memory groups passed. Reviewer0 assigned real fresh turn for all four affected prototype lanes, saved6.1-sol/xhigh/read_only; source/application reviews unaffected. [review-corrected-faults.md](review-corrected-faults.md). No claim/RPC/fault execution yet.
