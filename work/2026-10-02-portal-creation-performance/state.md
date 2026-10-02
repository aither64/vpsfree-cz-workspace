---
lifecycle: active
---
# Portal creation performance state

Phase: implementation and pre-activation verification complete; application rollout blocked
until the unrelated active session becomes idle. The actual-history live portal
canary follows normal activation. Implementation, independent review, exact-head
CI, consuming builds, two real fault cases and aitherdev host activation passed.
The user authorized implementation and the accepted aitherdev rollout. All five
feature branches remain unmerged; default-branch integration requires explicit
direction. Archive, delete and session stop were not requested.

- [x] Retained Full team, design and implementation
- [x] Focused checks, independent complete-branch reviews and publication
- [x] Exact SDK/runtime/extension CI and consuming package/host builds
- [x] Real 3,379-thread fixture, warm-up and five normal creation measurements
- [x] Real lost-helper-response and partial-team retry acceptance
- [x] Exact-generation host dry-activate and switch, two health checks passed
- [ ] Workspace user-profile activation and retained-identity/service checks
- [ ] One actual-history Full-team live portal canary
- [x] Current documentation reconciled and deployment-blocker handoff prepared
- [ ] Explicit integration approval and every exact final head merged

The five normal Full-team creations at the original candidate reached ready in
6.121215, 6.401349, 6.332730, 6.500734 and 6.428341 seconds: median **6.401349**,
maximum **6.500734**. Each sent one goal, completed a model turn and used no tools.
These values belong to runtime `8ae46f9`/candidate `0klh7`; the final correction
changes recovery only. Final-package production latency remains the canary gate.
[Measurements](verification-measurements.md) preserve exact provenance.

## Identity and ownership

This parent initially had neither environment identity nor a trusted existing
session binding; `dev-session current` reported none. It created this separate
initiative. Initial substantive tracking commit `8762bd33` preceded source and
external mutations. Root: `01a0fd0b-f0bf-77f2-814b-f1f2af67a094`.
Retained architect0 uses Astra/xhigh/workspace_write, implementer0 uses
6.1-sol/xhigh/workspace_write, reviewer0 uses 6.1-sol/xhigh/read_only. Live saved
identity/settings are checked before each assignment. No roster was invented.
Catalog digest: `4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17`.
Fresh utility watchers use Luna/low/operation, maximum one at a time.

Shared master/index/unrelated records, other sessions and staging are preserved.
No archive, delete, service cleanup, branch deletion or cluster operation occurred.
There are no migrations or persisted-format changes.

## Final branch inventory

All branches: `2026-10-02-portal-creation-performance`.
Worktrees: `worktrees/2026-10-02-portal-creation-performance/<project>`.

| Project | Exact final head | Verification |
| --- | --- | --- |
| codex-web | 4c170393a96ed0a6ac2e43488d073f6fcab36132 | Four lanes clear; CI37024785401 passed |
| dev-workspace | 924c0ec28c41dd8b56aaf17f2212b302ca614899 | Four correction lanes clear; CI37063660861 passed |
| vpsfree-dev-workspace | 8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 | Pin review clear; CI37064115624 passed |
| workspace | 1b670e0329c80b5ed266f6edb92ac2096134677c | Pin review, package build and flake checks passed |
| vpsfree-cz-configuration | 3d26ec396ceb935a233bdda3079618821d099b3e | Pin review, host build, dry-activate and switch passed |

All heads are published over SSH, and comparisons are captured. SDK has one
capability commit. Runtime has three clean commits: SDK pins `dfda7b8`, locked
fresh creation/recovery `4262bb2`, progress `924c0ec`. Each consumer has one final
pin commit. Independent review confirmed no obsolete approach, follow-up fix,
unused compatibility path or migration in the complete series. Workspace
functional base is `58df04cf`; its rebase was patch-equivalent. Configuration
functional base is `40289e3b`. [Remediation](remediation.md) and
[corrected pin review](review-corrected-pins-result.md) preserve inventories.

Consumer locks select runtime `924c0ec` and SDK `4c170393`, with matching lock
metadata. Only intended nodes changed. Codex0.160.0, providers, catalog and host
paths remain unchanged. Confctl generated the configuration channel pin; hooks
passed and its changelog was deliberately corrected. The application is selected
from the user profile, without a system application pin.

## Verification and review

SDK wire/default/filter/corpus/selected-schema checks and full CI passed.
Runtime focused Go/Ruby recovery and progress checks passed; final full CI passed.
Consuming package build and flake checks passed, including Go/Ruby/package and
workspace contract/catalog checks. Strict browser verification passed after the
interactive plan fixture gained the two existing status paragraphs.

Independent retained reviewer0 used its actual saved 6.1-sol/xhigh/read_only
settings, without fallback or overrides. Overall risk is high because creation
recovery affects persistent ownership, cross-project protocol use and deployment.
SDK/runtime/correction/prototype reviews covered general, architecture, scope and
risk/compatibility. Mechanical consumer supplements covered general and risk.
Final application and pin reviews have no Blocking, Important or Advisory
findings. An earlier prototype no-tool advisory and narrow browser fixture fix
were resolved with focused inspection; affected follow-up designs received new
review turns. Unaffected lanes were not repeated.

Current source review: [SDK](review-sdk-result.md),
[runtime](review-runtime-result.md),
[loaded-root correction](review-loaded-root-correction-result.md),
[corrected pins](review-corrected-pins-result.md).
Fresh fault-driver preparation review cleared all four lanes at 21:57 UTC:
[report](review-corrected-faults-result.md). Frozen driver ran once through a
fresh Luna watcher, exit0, completing at 22:05 UTC. Lost-response retry retained
the exact new root; member interruption retained the root and architect0 ID,
with two unfinished members present before retry. Both retained receipt, frozen
Full policy and attempt2, one goal, completed model turn, no tools, detailed
progress and final evidence. [Fault results](verification-corrected-faults.md).

This was old-consumer/new-thread-create-provider verification, not full-package
activation. The original stranded root is now unavailable. SDK4c's read-only
probe found it absent from loaded enumeration, and exact-target read/turns/idle
checks returned thread-not-loaded. Those errors do not authorize replacement.
The old receipt/journal, original fault/result, earlier claims and five samples
remain unchanged; the old same-root continuation was never run.
[Observation](root-observation.md) and [accepted recovery design](recovery-design.md).
No repair of that unavailable old root is claimed.

## Deployment

Final application candidate:
`/nix/store/xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2-dev-workspace-0.2.0`.
Provider SHA256 `ac2bf71e98d1bafb4357bbf0bb7b7d1140f0bb4a1a903147cff67790284e9c4c`.
Its Codex launcher/native, runtime contract and catalog match the retained old
candidate. Private corrected-candidate-root retains it; original candidate-root
continues retaining0klh7.

Host generation `2026-10-02--23-26-29`, toplevel:
`/nix/store/4wa4aiamhn1cm63j7gsaiqdqfn0f9ign-nixos-system-aitherdev-26.05.20261001.4feb8eb`.
Private corrected-host-candidate-root retains it; old host-candidate-root remains.
Parent initiated exact-generation confctl dry-activate then switch in the normal
local aither Nix shell. Both exited0. Switch reported systemd and firewall health
checks passed (2/0), and parent verified `/run/current-system` equals this output.
A fresh Luna observer owned the long switch wait. No unexpected kernel build.

Parent initiated installed `workspace-host switch --source` using the exact
workspace worktree. Fresh `profile_switch_observation` reported exit1: the normal
idle gate refused storage-redesign's active turn. Parent confirmed current
activity through read-only `thread observe`; no interruption or bypass follows.
Old package9g8 remains selected, and the supported switch restored prior quiesced
terminals. Preserve the failed log/status and pending update; retry through the
ordinary installed switch once all sessions are idle. Post-activation/canary remain
pending.
Pre-activation snapshots preserve36 production root IDs and owned3 members'
identities/settings. [Rollout](rollout.md) records ordering and software recovery.

Fresh read-only watcher observed the blocking root from 22:12:18 through
22:22:32 UTC; every observation remained active, with successful RPCs and no
errors. Its bounded window ended incomplete, without interruption or cancellation.
No watcher or deployment command remains running. User scheduling preference was
requested asynchronously; absent a reply, no new interruption or bypass is inferred.

Final blocked-rollout retention/health check passed: all36 prior root IDs and
owned3 member identities/settings remained exact; all four workspace user
services and nginx were active. The new host remained selected and the old
application9g8 remained selected. Private blocked-rollout-retention.json records
this check; it is not final-package activation or canary evidence.

Earlier host-build wrappers failed on SSH inherited login identity and a duplicate
current-symlink inventory, after the actual Nix output built. Parent diagnosed
both and retained the exact built output; failure logs remain. No root-directory
permissions, loginuid, contract or product guard was changed. Lessons are in
notes/confctl/2026-10-02-ssh-login-identity-gcroot.md. Earlier absent old Nix
outputs were reproduced normally and rooted; disappearance cause is unknown.

## Documentation and next action

Owning SDK `docs/reference.md` and runtime `docs/dev-sessions.md` and
`docs/workspace-portal.md` describe optional index-only listing, locked freshness,
complete retry scans, frozen live-root policy and bounded progress semantics.
Parent applied the user-facing writing skill directly after settling the facts.
Session [design](design.md), implementation records and
[rollout](rollout.md) retain individual design and deployment evidence.
[Historical checkpoints](execution-history.md) preserve superseded commands,
failures and preparation states; this file governs current status.
Private logs/status/identity snapshots are under the initiative's verification
directory in ~/.local/state/dev-workspaces; synthetic evidence remains in
/tmp/pcp-oct02-a. Credentials and rollout payloads never enter tracking.

Next: obtain normal idle proof, retry the ordinary profile switch with a new
retained log/status, verify package, services and retained identities, then run
the single actual-history Full-team canary. Keep generation/activity/journal
refusals intact. Post-activation and live-canary wrappers remain unexecuted, with
absent status/destination claims. Retain all branches and this active session.
After the live canary passes, hand off readiness awaiting explicit integration
approval; do not infer that approval from implementation or deployment.

Session URL: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>
