# Superseded operational checkpoints

Current status is authoritative in [state.md](state.md). The following preserves
discovery, failures, recovery and intermediate rollout provenance.

# 2026-10-16-update-codex

## Status

Codex 0.163.0 is deployed in both aitherdev and the workspace profile. Native,
package, CI, state compatibility, naming, portal and terminal checks passed.
All three coordinator jobs so far succeeded. Current system is icx8yqs5 at
configuration 9721c331; application is a335n75h, native assembly jrsm1rzx.
Final provider acceptance found and is correcting a shared-login restriction.
Configuration aed7d507 is published and under focused independent review.
Local ChatGPT authentication was restored from retained private backups after
the canary's native guard removed it; local login status passes. No provider
request has yet been sent by these failed DeepSeek attempts.

- [x] Discovery, layered skills, implementation, quick checks and publication.
- [x] Independent full-branch review; native/package/VM/state/naming/CI checks.
- [x] System and workspace activation, followed by strict-profile schema correction.
- [x] Authentication incident containment and synthetic preservation check.
- [ ] Focused authentication review and isolated real provider canary.
- [ ] Exact final system rebuild/activation and live acceptance.
- [ ] Handoff; retain active lifecycle, branches and reservation pending merge approval.

## Next actions

Finish focused review at aed7d507, run the private-home provider canary, build
that exact configuration and deploy through the same retained reservation.
Confirm deployed profile loading preserves shared authentication, services,
conversation and terminal continuity, plus retained recovery roots.
No default-branch integration or reboot is authorized.

## Documentation

Approved plan is in plan.md and the technical/verification brief in design.md.
The four repository-owned skills and package/operations guides are committed.
Exact rollout evidence remains session-owned.

## Repositories

Planned: codex-web, dev-workspace, vpsfree-cz-configuration and workspace.

## Commands run

- dev-session current: no existing session or inherited environment binding.
- dev-session start update-codex --no-codex --no-attach --json: created this slug.
- Exact environment identity/current matches 2026-10-16-update-codex and this root.
- team list: refuses because shell-only startup has no lead Codex thread.
- normal start: requests a goal file for noninteractive creation; no thread created.

## Results

Planning found stable Codex 0.163.0 and llm-agents e85b99217baf13a38fc887b31338b1833f1159c0.
Runtime and system currently select 0.160.0-related sources. Naming gates and model
catalog hashes need updating. New source schema declares every existing fixed
utility restriction. New llm-agents changes native daemon installation to an
immutable Nix-store target and still supplies linked helper resources.

## Open questions

No user decisions pending. Native compatibility and deployment admission remain
to be verified.

## Cleanup

No project edits, builds or deployments yet. Preserve all unrelated shared files.
Do not archive, delete, stop sessions, remove branches or prune retained roots.

## Setup lessons

Shell-only sessions cannot become managed while their shell authority is present.
Initial ordinary tracking requires plan.md, state.md and portal.yml committed.
The initial plan commit omitted the manifest; a separate setup registration commit
was necessary after shared master advanced, preserving concurrent work. A stop of
this newly created empty shell closed its tmux runtime but then reported an empty
recovery identity; normal start subsequently succeeded. No unrelated session was
interrupted. Native startup took about two minutes and recovered its terminal after
an App Server disconnect. Configuration post-checkout hooks required its pinned
bundle; the failed add had already registered the worktree. Installed and signed
Overcommit through its Nix shell, with frozen dependencies under this session.

Candidate Codex and dependency setup were monitored with fresh Luna/low utilities;
logs and status artifacts are retained here. The candidate package was substituted
from the upstream cache; no Rust or kernel compilation was needed.

## Quick verification

- Candidate-generated experimental App Server schema: complete codex-web request
  corpus compatible. All 55 fixed policy restrictions and literal MCP enabled
  validate against exact 0.163.0 config source.
- Catalog refresh is idempotent. Existing semantic Luna derivation tests pass
  after updating the full-source byte-length assertion (472072 bytes).
- Browser contracts: 64 passed. Focused ephemeral Go tests pass (2.2 seconds).
- Full Go suite failed in an unchanged socket fixture: its Nix-shell TMPDIR plus
  long test name/suffix exceeded Unix socket address length. Re-run with TMPDIR=/tmp
  inside the same Nix environment; no protocol or feature behavior is implicated.
- Skill validator needs PyYAML. Use a Nix python3.withPackages environment rather
  than the ambient Python or nix shell with the library alone.

- Full codex-web Go suite passes with short TMPDIR. All four skills validate.
- Runtime local protocol contract passes against 0.163.0. Naming unit tests pass
  with DEV_WORKSPACES_CODEX_PROVIDERS pointing at a nonexistent session-owned
  path; otherwise unchanged fixtures read the real host provider catalog and
  reject their intentionally absent runtime identity. This is local test isolation,
  not a production provider change. Vendor dependency preparation passed with the
  existing hash.
- codex-web published head: 8851f1c35e9424b1240705cb73d09d387d9276f0.
- Configuration skills commit and exact llm-agents channel update committed with
  its declared Overcommit hooks. No application or system activation yet.

## Final review checkpoint

All intended project changes are committed and quick checks pass. Exact branch
heads and complete series are in review-heads.json and the review packet. Risk is
high; general, architecture, scope and risk lanes apply. Roster is null, so the
installed default lead_reviewed review-purpose role selects standalone
GPT-6 Astra/xhigh. Source branches have not been merged or deployed.

The workspace instruction discovery budget required shortening only the new route;
the correction was folded into its owning unmerged commit. Initial live system
Codex is 0.162.1; application Codex is 0.160.0. The prepared target is 0.163.0.

## Review remediation

Astra/xhigh standalone /root/final_review reviewed all four complete branches in
review-report.md. No obsolete history, repeated pin streams or application
migrations. Blocking B1 was the stale catalog byte length; corrected to 62680,
with matching SHA-256 checked directly. The same fixture now binds the selected
0.163.0 source path. Runtime skill names byte-length/source prerequisites.
These narrow corrections stay within the reviewed design; no new review lane
is needed. Fixes are folded into their owning commits; consumer pins are
regenerated through confctl and scoped Nix updates, one update per stream.
Long native checks will use a fresh catalog Luna/low verification utility.

## Clean CI dependency correction

Latest runtime CI 38918415585 failed its fixed-output vendor derivation. The
old hash was incorrectly retained after a local cached output had hidden the
changed Go module metadata. CI computed
sha256-WGrWBDAXKKrtkq9+ZBHgP3eWsH1F507JNP8aJ8iIltc= for the selected codex-web
pseudo-version. Corrected the generated dependency hash in the owning upgrade
commit. This is a mechanical dependency remediation; full clean package build
must verify it. The failed run log is ci-vendor-failure.log. No blind rerun.

## Native gate passed

Final cweb a0561fa has a reviewed fixture adaptation for 0.163.0: base instructions
are the first developer input message, rather than a top-level request field.
Six focused shape tests pass. Same independent reviewer /root/final_review,
Astra/xhigh, accepted the affected general/risk lanes in followup-review-report.md.
A redundant CLI review was started while message delivery appeared opaque; it was
stopped once the retained reviewer returned, before any acceptance decision.
The original review still covers unaffected lanes and consolidated histories.

Fresh Luna/low native_checks_retry completed native-retry.log/status with exit 0:
packaged cweb checks, namespace ownership, GPT-5.5 and Luna protocol/isolation suites.
Source is realized and rooted by native-source. No native safety restrictions were
relaxed. New final vendor hash q/VR3ZgKqOjRCVpSjMSQcOS6/mUptbFyEqh6mp7Ht34=
comes from the selected Go module tree and awaits clean package verification.
All consumer pins now select runtime 24588400; exact heads are final-heads.json.

## Final repeatability cleanup

After the clean-CI dependency finding, the runtime skill now explicitly requires
go mod tidy, the final Nix vendorHash and a fresh dependency derivation. Removed
superseded codex-web checksums. These are narrow procedure/generated-content
corrections within the reviewed upgrade. The running package batch remains bound
to 24588400/d9dd1934/2d7306f8; final refreshed heads require exact builds before
activation. Preserve their separate receipts rather than relabeling old evidence.

Final runtime skill validates after its vendor/tidy clarification. All 55 fixed
utility restrictions and literal MCP enabled revalidate against the now-realized
exact 0.163.0 core/config.schema.json. No policy changes. Full local package/VM
batch remains running under /root/package_checks, with no activation submitted.

## Disposable VM runner correction

Standard runtime and workspace flake checks and workspace package build passed
before the custom naming VM. Its provenance seed accidentally retained Nix
string context for package.drvPath, pulling 4109 build-input/source paths
(38.5 GiB) into the guest. Parent cancelled only owned Nix build PID 983995
after validating its exact argv. The batch stops before state/config probes.
Discarded string context for this provenance-only .drv name in both session
VM expressions; the fixture checks its syntax, and never opens the derivation.
Actual output/source/binary resources remain strongly retained and hashed.
No application source change or host activation. Resume from the custom VM
and remaining probes with a fresh watcher if the interface is available.

The utility report misidentified the interrupted phase as aitherdev. Actual
/proc argv and the empty managed-naming-build.json prove it was the custom
managed-naming VM; the state probes and configuration build had not started.
The interruption was a deliberate parent cancellation of that exact owned Nix
process to fix the closure bug, not a new user cancellation.
The watcher interface became unavailable; declared visible parent monitoring
fallback under dev-session-monitor. Continue the remaining authorized checks
without restarting the completed native suites.

Final runtime package, native assembly and workspace flake checks/build passed.
The corrected custom VM driver then failed its own Ruff lint for an unused
shlex import, before boot. Removed only that temporary wrapper import. Resume
remaining-checks.sh from VM onward; no application fix or broad rerun.

Custom VM booted, then both native naming tests failed at their first bounded
root nft counter command (fixture line 274). Its stderr is intentionally hidden.
Add a session-wrapper preflight that reports only synthetic counter output or
root-command error before fixtures; do not alter assertions or permissions
without identifying the prerequisite failure. Latest upstream default heads are
unchanged and ancestors of all four final feature branches.

Counter preflight identified sudo requiring a password: the VM whitelist used
the Nix-store command path while the fixture invokes /run/current-system/sw/bin.
Changed only this disposable VM sudo rule to the exact invoked counter path;
NOPASSWD remains scoped to this one read-only helper. Preflight remains enabled.

## Release checks passed

Final naming VM passed TestManagedNamingRuntimeIntegration (70 s) and
TestNativeNamingRuntimeHTTPFailure (8 s), including ordinary continuity, two
slots/one child, missing home, child loss and managed TERM/KILL.
Both 0.160.0 and 0.162.1 disposable saved-thread startup, 0.163.0 read/resume/turn/
fork, and old-reader-after-upgrade checks passed (state-compatibility.json).
No migration/SQLx/SQLite errors were found in synthetic stderr; deliberate local
HTTP fallback produced WebSocket protocol diagnostics, not state failures.
Real final-package Luna/low naming returned codex-upgrades in 2704 ms, below
ten seconds (naming-canary.json). All final runtime CI is green (38920925512).
The live thread probe initially assumed workspace-root cwd, but its actual
unchanged owning-session cwd is the tracking directory. Exact ID and one saved
turn were present. Corrected only this session-probe expectation to the verified
tracking cwd, preserving identity and nonempty history assertions.
System build from exact configuration 107255f8 is now running.

Live owning-session read passed with exact ID, tracking cwd and one saved turn
(retained-thread-before.json). The first confctl build stopped at its ordinary
interactive confirmation (EOF); no build or deployment effect. Use its documented
noninteractive flag for the already authorized exact-target build.

## Coordinator preparation

System build passed at clean configuration 107255f8; configuration-info embeds
that exact revision. Target i2908m46dzh334smk0i81d4wn6z6y421, application a335n75h.
Both system/workspace native assemblies report 0.163.0, SHA-256 5e538cfe...,
materialized resources and original immutable native closure retained.
Release evidence is frozen in release-evidence.json. Do not mutate its referenced
artifacts after snapshot preparation. All four comparisons are captured at their
final heads; fresh default refs remain unchanged ancestors. No activation yet.
Machine preparation runs inside the configuration Nix shell with its frozen
bundle available for ordinary retained-checkout hooks. Selected adapter is
6ca7nm0qjwp59p637fz8agvj79ka2dgy; inspect the retained environment against this
current catalog rather than copying a historical helper path.

## Postactivation acceptance and DeepSeek correction

Machine job c99ecbc3-7376-4b55-b7b8-3f1edb4abaaa and dependent profile job
587f4fa9-f4df-4bf2-ab4d-42d0664f8edf both succeeded. System/profile point at
i2908m46; application is a335n75h and actual managed native is jrsm1rzx,
0.163.0, SHA-256 5e538cfe... . Reservation 0c72d37a-dcdd-44bc-bd4a-bc9f9a462505
remains deployed_review for owner c7fbd286-e060-419b-b538-6675336ab1ce.
Original release-evidence.json and its referenced files remain immutable.

The pending Codex marker cleared through the ordinary scheduled service at
18:14:50 local; no manual deletion, restart or lifecycle bypass was used.
check-live.py initially assumed codex-ds was a system-path command. It is installed
by Home Manager under ~/.nix-profile/bin; its wrapper selects the exact system
assembly wz4w6709. Corrected this session-only assertion. Full live evidence is
live-acceptance.json, with strict help alone explicitly insufficient for config
loading. The retained exact thread grew from one to four saved turns after the
switch; real Luna/low naming returned a valid title in 3444 ms.

The one real provider canary attempt failed before any request: strict loading
rejects preferred_auth_method. The selected schema also rejects
model_supports_reasoning_summaries; both settings are obsolete. Removed them in
configuration 9721c331, retaining forced_login_method=api and existing catalog
supports_reasoning_summaries=true. Corrected the operations guide and skill to
use a real strict ephemeral request, because --help short-circuits config
loading. Quick strict App Server startup with the rendered managed profile as
an isolated base config passed, without copied authentication or model requests
(deepseek-profile-source-check.json). Early diagnostic attempts found debug
prompt-input does not support strict-config; that approach was discarded before
commit. No new application protocol, state, provider or authentication contract.
The configuration commit passes declared hooks; Nixfmt and diff checks pass.

## Strict-profile follow-up review passed

Standalone native reviewer 01a14588-e373-7c11-a6cc-752943095379 used catalog
Astra/xhigh/read-only (deepseek-review-identity.json), replacing the retained
reviewer only because native follow-up dispatch was unavailable. All four
applicable lanes and the complete four-commit configuration branch passed with
no findings (deepseek-review-report.md). No repeated pin streams or migrations.
The actual 0.163.0 reasoning-summary capability is
supports_reasoning_summary_parameter, defaulting true in native ModelInfo;
the catalog's legacy supports_reasoning_summaries field is not the authority.
Removal of the two invalid profile keys preserves supported behavior.
Exact source 9721c331 is rebuilding; old release evidence stays frozen.

## Corrected system activation submitted

Exact configuration 9721c331 rebuilt to icx8yqs5; Codex remains 0.163.0 and
all dependency inputs/application/native outputs are unchanged. Fresh snapshot
be7d097a seals deepseek-release-evidence.json and the new exact build.
Preparation used the selected a335 package/catalog; its confctl adapter is
39n6n34l and retained environment f7zlrnwa. An initial lead assertion incorrectly
expected the predecessor 6ca7nm0q helper. Reading the actual selected catalog
resolved the inspection without rerunning preparation or modifying the snapshot.
The environment embeds the correct 39n6 helper. Nix shell startup text was
separated from JSON; original response is deepseek-machine-preparation.raw.

Approval d3a89773 records the existing actual user deployment instruction for
this exact snapshot, narrowed to system switch. Job ca886f70-c791-4d3b-a63d-8f3a059c3744,
attempt d6ce8e2d-f32e-47f9-a1c6-19bb2ca2d58e, is running under the original
reservation and depends on the successful first profile job. No new reservation,
merge approval, reboot or application switch was introduced.

## Shared-login incident and containment

The corrected-system job ca886f70 succeeded; both live links select icx8yqs5,
configuration 9721c331. Its strict canary then reached native login enforcement
and failed before any provider request. forced_login_method=api checks shared
OpenAI authentication, even for a custom DeepSeek provider, and removed the
local ChatGPT auth.json. The exact native path logs out locally without token
revocation. Parent restored the private file from two identical retained operator
backups; local login status passes (local-login-recovery.json). No credential
bytes were output or copied into session records. This check should have been
isolated first.

Configuration aed7d507 removes only this unrelated OpenAI-login restriction.
The DeepSeek provider still authenticates with DEEPSEEK_API_KEY. A disposable
synthetic-auth before/after check proves that the old profile deletes synthetic
auth and the corrected strict exec preserves its exact bytes, then stops at an
empty prompt before any model request (deepseek-login-preservation.json).
Nixfmt, diff, declared hooks and skill validation pass; source is published.
This authentication fix is independent of the earlier invalid-schema cleanup;
there are no repeated pins or migrations. Focused general/risk review is running.
Previous native reviewer resume refused because its ephemeral run retained no
rollout; exact failure is preserved. A fresh catalog Astra/xhigh read-only native
review replaces that unavailable identity, with persistent rollout this time.
Subsequent provider probes use an isolated Codex home and no copied ChatGPT login.

## Authentication review and real provider check passed

Standalone reviewer 01a14598-96f1-7e92-9212-eb4912342792 verified catalog
Astra/xhigh/read-only and accepted affected general/risk lanes at full final
configuration aed7d5071e24793d7bd811af11ccfa80e6f049d6. The report explicitly
supersedes the earlier forced-API-login conclusion. Complete five-commit history
is sound: invalid-schema cleanup and login-preservation are separate corrections,
each dependency pin stream changes once, and there are no migrations.
(deepseek-login-review-report.md and identity receipt).

The real strict isolated-home DeepSeek canary passed: deepseek-v4-pro returned
CODEX_UPDATE_OK in 2.47 seconds, with no tool calls, copied production login or
shared-auth change (deepseek-canary.json). The wrapper/key/model/endpoint/native
assembly are the deployed identities; semantic profile hash binds the final
source. Exact aed7d507 system build is running; then prepare a fresh snapshot and
activate under the same reservation. Actual deployed-profile empty-prompt loading
will verify shared-auth preservation without spending another model request.

## Final activation submitted

Exact final configuration aed7d507 built to lr6b9x40 (login-system-build-receipt.json).
Fresh reviewed snapshot 33676b8b binds immutable login-release-evidence.json,
including real provider success and final five-commit configuration history.
The prepared artifact matches the exact build, input identities and current
installed 39n6n34l adapter in f7zlrnwa environment. Final machine job
02558206-3690-414d-8e55-06b2362fb903, attempt
5c5c1563-76a9-4a27-a467-8eb1fc124a7e, is running under the original reservation,
depending on the successful prior machine job. Existing user deployment direction
is recorded for the new exact snapshot; no merge, reboot, profile switch or
reservation release was authorized or attempted.
