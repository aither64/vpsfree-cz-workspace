# Disk cleanup inspection, 2026-10-30

Architect read-only findings at approximately 20:24 UTC. User requested unused
temporary/test-image cleanup. Lead owns global collection; implementer0 owns
settling its build and old image references; implementer3 owns its unused KB
temporary data. This note records inspection, not completed cleanup.

## Identity and authority

`dev-session current` and both environment identity variables matched
`2026-10-30-oomd-abuse-policy` in `/home/aither/workspace/ai/vpsfree.cz`.
Read workspace sessions, lifecycle, verification, documentation and storage
retention guidance, the documentation/handoff skills, the selected runtime's
complete coordination guide, and configuration repository
`docs/operations/aitherdev-disk-retention.md` from `origin/master`.

Selected runtime: `/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`.
Coordination catalog digest:
`sha256:f0188e28ef09cea1410c21f723a77ad2bc1e133d6f6e258af26eed0e058bfce7`.

## Measurements and native preservation evidence

All measured paths share `/dev/vda1`. Initial `df -B1 /` showed 96% use and
46,800,138,240 available bytes. Latest read showed 46,181,154,816 available
bytes (43.01 GiB), 955,855,466,496 used, 1,055,740,375,040 total. Concurrent
machine activity means these reads are not a cleanup comparison. Inodes were
33% used.

Commands inspected metadata through supported collection, without manually
reading peer worktrees, records or recovery contents:

```sh
workspace-host coordination gc --dry-run --json --sizes
workspace-host coordination gc --dry-run --json --sizes --expire-unused
sudo -n nix-store-cleanup --dry-run --verbose
```

The default preview completed with `retry=false`, offering two notification root
links. First explicit-expiration preview took 27.0 s and returned `retry=true`
after ledger activity. One fresh retry took 27.6 s, exited 0, and returned
`retry=false`: **three root unlink actions, zero checkout actions, zero removals,
234 preparation records and 158 preserved entries**.

| Final preservation reason | Entries | Allocated payload bytes |
| --- | ---: | ---: |
| Unknown or unfinished integration | 2 | 5,399,244,800 |
| Required by live work or preparation | 18 | 12,555,628,544 |
| Required by live work (roots) | 135 | Not reported |
| Profile generation required by live work | 3 | Not reported |

The measured payload total is **16.72 GiB protected**, not reclaimable space.
The three eligible links under `~/.local/state/dev-workspaces/coordination/roots/`
have these basenames:

- `9e2458aa-f382-4a8b-9c27-0d5d818bf268-fdedc8996975-notification`
- `bb0dd8a7-303a-45c1-bc98-4ca0f2a942a3-fdedc8996975-notification`
- `bbd9a7da-4138-418a-b962-05972b67a7bd-fdedc8996975-notification`

Links becoming idle explains the extra candidate. Removing these links alone
reclaims negligible space; Nix closure reclaim is unknown until ordinary GC.
Preparation count is an inventory count, not 234 collectible payloads.

Invoking host preview through `sudo -n` refused with
`sudo: a password is required`. This is an authentication failure for that
invocation, not a requirement that preview run as root. No privileged preview
completed, and no profile/test-root removal or privilege expansion occurred.

Follow-up public-script/help inspection verified that
`~/bin/nix-store-cleanup --dry-run` supports unprivileged preview; only `--apply`
requires root. This helper can remove whole recognized retired test trees,
including guest disks, separately from ordinary store GC. Eligibility begins
with registered `/tmp/**/os-test-*/config.json` symlink roots. An inaccessible
process cwd/fd conservatively preserves candidate test trees; other scan errors
can print `INCOMPLETE SCAN` even when dry-run exits 0. An unprivileged zero count
cannot establish that no retired test data is reclaimable. Only `--help` and
the installed public script were read in this follow-up; no new preview or
temporary-directory scan was run. Actual host `--apply` remains unavailable
without sudo credentials. Lead will consider an unprivileged preview only if
ordinary Nix GC leaves insufficient capacity; none is being run while GC proceeds.

## Shortest supported next action

Lead will coordinate `workspace-host coordination gc --apply --json
--expire-unused` after owner0 settles its build; collector must continue to
preserve its native live/recovery holds. Owner0 then runs ordinary Nix GC after
accounting for its own image/build references. Compare `df -B1 /` before/after
the actual cleanup. Lead records applied actions and measured reclaimed bytes.

Do not manually remove protected payloads, store paths, profile history or roots
based on age. Recognized host test directories require terminal results, seven
inactive days, available native locks, no process references and no `.keep`;
ad hoc directories require explicit owner retirement. No session lifecycle,
archive compaction, claim, source deletion or cleanup application was performed
by the architect. No further inventory is needed for this package.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

## Execution receipts (lead)

Owner0 stopped its exact final-image Nix client2405219 with native SIGINT; native exit1/156s and absence were verified, no guest had launched. Its `/tmp/oom4d.GPsawj` directory was empty and removed. Old5a JSON/root-image outputs were already absent and had no explicit roots; final image outputs were not realized. The disposable manual DB root was absent; completed automatic DB helpers had pruned their roots. Reproducible ignored Bundler caches removed:154,230,784 allocated bytes, plus three obsolete tiny scripts and the empty directory. Compact script evidence and source remain. No final image is being retained solely as a cache during the cleanup hold.

Owner3 removed known inactive shell/temp files only after reference checks; cumulative49,152 allocated bytes. Final source checker completed and its final checked source tree was committed/published as1119bcd; useful compact evidence and private configuration remain. No KB guest images exist. Its automatic managed runtime was cancelled while queued with no executed steps, preserving the heavy-allocation hold.

Lead ran `workspace-host coordination gc --apply --json --expire-unused`: native exit0, retry=false, actions=[], removed=[],158 preserved rows. Result: `coordinator-cleanup-result.json`. The previously previewed three idle notification links were no longer offered by the applying collector; no checkout/root deletion is attributed to this apply. Native protection of live/recovery payloads remains.

Ordinary `nix-store --gc` completed through a fresh retained-policy Luna/low utility: native exit0,315s, **1,000 store paths deleted /2.3GiB freed** (native rounded figure). Before/after available root/tmp/store filesystem bytes:45,346,455,552 ->48,477,487,104, delta+3,131,031,552; concurrent machine activity means the df delta is not all attributed to GC. Final free45.15GiB. Full native `nix-gc.log`, exit/elapsed and before/after receipts preserved by owner0; no operation remains. No manual store path, root or profile-generation deletion.

Owner2 completed final exact ignored React dependency/build/browser cleanup:321,429,504 allocated bytes (306.539MiB), including frontend/BFF node_modules, dist, redundant browser report assets and three own obsolete helpers. Retained6,234,112B original failure traces, Markdown diagnoses and all final PNG/docs/log/JSON/patch receipts; hashes match and source b67c7917/treece3b38c9 unchanged/clean. Only completed own-package processes were in scope; unreadable foreign processes did not authorize touching their data or require privileged scanning for these privately owned ignored caches. Immediate df gain321,167,360B, final free48,649,687,040B (~45.3GiB),96% use, with concurrent machine writes. Receipt: react-verification/cleanup-receipt.json and react-cleanup.md.

Cleanup complete: native Nix2.3GiB plus475,709,440 allocated bytes (~454MiB) own caches/temp data. All cleanup/build commands exited, no guests launched, no source changes, no session lifecycle operation. Heavy allocations remain held; future verification must reassess capacity rather than immediately recreate these caches/images.
