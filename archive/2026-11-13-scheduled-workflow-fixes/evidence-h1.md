# H1: KB firewall listener readiness and diagnostics

Owner: implementer0. Lead released H1 after B1 implementation acceptance and
capacity confirmation. Architect confirmed the implementation matches the
[sufficient brief](design.md); no design deviation or added gate.

**Delivery accepted and exact final head integrated into remote master by lead;
full master runtime is lead-monitored and pending.** Final head
`cb7825245ea786fb0f51c469d1a7dc5c6a1ececc` implements the released Fedora-only
persistent-mode amendment. The fresh changed-source scenario passed all unit,
listener and original policy assertions before/after restart. Original review
and failed runtime remain bound to `2cfbde6`; successful successor evidence is
recorded separately below. Lead owns full master CI; implementer0 retains
future failure-diagnosis ownership if needed.

## Source boundary

- Repository: `vpsfreecz/vpsfree-kb-contracts`.
- Branch: `2026-11-13-scheduled-workflow-fixes`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-kb-contracts`.
- Base: `f97785c2c265172a4c78893e0673034fde56e4dd`.
- Sole source: `tests/suite/kb/firewall.nix`; final diff 50 insertions,
  8 deletions.
- Shared helper requires each local listening port 22, 80, 81 and 443 from
  one `ss -H -lnt` snapshot per readiness probe. Port 81 remains live so denial
  checks test firewall policy against a real service.
- Setup and restart use the same existing runner wait primitive, with one
  120-second readiness deadline. Setup uses `set -eu` so failed service commands
  fail promptly. No policy retries, arbitrary sleeps or timeout increases.
- Readiness failure collects local `ss -lntp`, socket-service status limited
  to 10 journal lines per matching service, and 80 journal lines, with a separate
  30-second diagnostic command bound. It rethrows the original readiness error
  even if diagnostic collection fails.
- External IPv4/IPv6 allow/deny, ICMP, established-connection, public-zone and
  restart assertions are unchanged. Unit definitions, executable fixture files,
  source-page hashes and all five test-variant scenarios are unchanged.
- No KB prose, production KB writes, real service changes, configuration pins,
  schemas, persistent formats or migrations. No dependency/pin update streams.
  Test-only compatibility; reverting the source commit restores earlier behavior.

## Quick evidence

- `nix-instantiate --parse tests/suite/kb/firewall.nix`: pass.
- Evaluated the actual test definition's common/firewalld Ruby through its
  Nix `make-test` adapter with the pinned flake's lib and fixture inputs, without
  constructing or booting a VM; output `/tmp/scheduled-workflow-fixes-h1/firewalld.rb`.
- `ruby -c /tmp/scheduled-workflow-fixes-h1/firewalld.rb`: pass.
- Disposable `/tmp/scheduled-workflow-fixes-h1/check-helper.rb` loads that
  generated Ruby and executes the real helper's shell probe with stub sockets.
  It proves partial 22/443 fails, complete 22/80/81/443 passes, missing 81 or
  similarly named wrong ports fails, deadline stays 120, all three diagnostics
  are requested with a 30-second bound, diagnostic failure preserves the exact
  original exception, and setup service failure stops before readiness.
- Byte comparisons against base confirm all external/established assertions,
  unit definitions and variant scenarios remain unchanged.
- `git diff --check`: pass.

Pinned Nix format and full repository source checks passed in fresh native
utility `/root/h1_static_watcher`:

```sh
nix shell github:NixOS/nixpkgs/0bb7ec54c8483066ec9d7720e780a5caa71f8612#nixfmt -c nixfmt --check tests/suite/kb/firewall.nix
nix develop --profile /tmp/scheduled-workflow-fixes-h1/dev-shell -c bash /tmp/scheduled-workflow-fixes-h1/static.sh
```

The static script runs generated Ruby syntax/helper checks, then
`bin/check --allow-missing`. No runtime integration is part of that batch.
Format command exit 0 in 55.831 seconds; development-shell/static command exit 0
in 496.767 seconds. The repository inventory validates 60 concepts, 120 variants,
66 Czech references, 61 English references and 120 PNGs. Its Ruby suites pass.
The retained-socket diagnostic in the log is expected negative-fixture output:
`tools/test-machine.rb` and `tools/test-runtime.rb` explicitly assert that refusal;
the associated suite ends with 34 runs, 1,244 assertions, 0 failures/errors.
No unexpected local kernel build occurred and no watcher-owned process remains.
Policy is the installed verification utility `gpt-6-luna` / low / full_access,
package `/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, matching
native utility `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`
(danger-full-access, never approvals). Raw evidence is disposable under
`/tmp/scheduled-workflow-fixes-h1/`, main log `static.log` and result `static.result`.

Pinned input graph (unchanged): vpsAdmin
`942c6eaed41331f823d8e0f670ed239e2b308440`, vpsAdminOS
`6bdf458fd9105379860234ff33d352e55844f08f`, runtime nixpkgs
`5dfba6236110080a54247d6460bc2ff5dda939cc`, tooling nixpkgs
`0bb7ec54c8483066ec9d7720e780a5caa71f8612`.

Unchanged `flake.lock` SHA-256:
`7cea2341634af13a005b83ac6a77122154f297a1ced62eaeccd902de791d1f69`.
No hook framework is declared by the repository; inspected the ordinary hook
directory and found no executable non-sample hooks. No hooks were bypassed.

## Original reviewed committed range

Complete series (one source commit):

```text
f97785c2c265172a4c78893e0673034fde56e4dd  origin/master base
2cfbde649769509e2628600535e3023d872f1735  tests: wait for all firewall fixture listeners
```

Committed with `nix develop /tmp/scheduled-workflow-fixes-h1/dev-shell -c git commit -F /tmp/scheduled-workflow-fixes-h1/commit-message`.
Saved pinned environment: `/nix/store/yqi33c9312swbggnmmsbazd5xbwaf756-nix-shell-env`.
Fresh `git fetch origin` followed by saved-profile `git rebase origin/master`
reported the branch up to date. Final range `git diff --check` passes and the
worktree/index are clean. Portal comparison captured at that exact range.

Complete diff is reproducible with `git diff f97785c2c265172a4c78893e0673034fde56e4dd..2cfbde649769509e2628600535e3023d872f1735 -- tests/suite/kb/firewall.nix`.
Disposable copy `/tmp/scheduled-workflow-fixes-h1/final.diff`, SHA-256
`cf58dd9b8b15f3fb11dcfb90571fc44641f175d2a1acf09feb6d921a1e883b20`.
Final diffstat: one file, 36 insertions, 8 deletions. No obsolete approaches,
follow-up commits, migrations or dependency/pin update streams exist in this
branch. The complete source-only range is available locally for final review.
No feature push has occurred, per lead's explicit review-first direction.

## Remaining acceptance

Lead completed independent final review of the exact local range and released
the following command at `2cfbde649769509e2628600535e3023d872f1735`:

```sh
nix develop /tmp/scheduled-workflow-fixes-h1/dev-shell -c ./test-runner.sh test --fresh --state-dir /tmp/scheduled-workflow-fixes-h1/runtime-state 'kb/firewall#firewalld'
```

Fresh utility `/root/h1_firewalld_runtime_watcher` ran this sole actual
scenario, using the freshly rechecked installed utility policy recorded above.
Main output `runtime.log`, exact completion receipt `runtime.result` and
runner-native state/logs `runtime-state/` beneath the same temporary evidence
directory. Firewall source SHA-256:
`c957e44d979872494f2a137bb395f2e936ecf5648c5678bf869cae02447af0c6`.
Retain source/input identity, resolved Fedora image,
before/after restart socket evidence and final result. A residual failure needs
its new socket/service evidence interpreted before changing scope or claiming
resolution. Do not increase timeouts or rerun an unchanged failure. Then perform
fresh target fetch/rebase, publish the feature and capture its comparison.

### First actual attempt: failed, retained and diagnosed

Exit 1 in 531.235 seconds. Native runner result `unexpected_failure`.
Exact test JSON `/nix/store/1hfdrndqpi1cry1qgsyll1492xm993vg-os-test-kb-firewall.json`,
derivation `/nix/store/910289sv859dyxsaahygw74a2jrv0xw5-os-test-kb-firewall.json.drv`.
Native logs under
`/tmp/scheduled-workflow-fixes-h1/runtime-state/os-test-kb__firewall-3b3255f7/`:
`test-runner.log`, `machine-shell.log`, `machine-console.log`, `machine-log.log`,
`machine-fs-vmSharedDir.log`, `test-result.txt`.

The run used system
`/nix/store/5wg0lsy11p9ayzz5zd8j5r4b5yh3fav7-vpsadminos-system-vpsadminos-26.05pre-git`,
kernel `/nix/store/mad7zijkfkvvmp58512idxgjn5ar2mv4-linux-6.12.95/bzImage`,
initrd `/nix/store/i82yxl5ljjkjsgmsbvcj67r6h0lnlfzc-initrd/initrd`,
squashfs `/nix/store/1n4xw0y12ll73ksq0r9330axf2bmfz4a-squashfs.img`,
QEMU `/nix/store/w4i3scdab4y1vp6wlkymx19gjgm80pka-qemu-host-cpu-only-for-vm-tests-10.2.4`
and virtiofsd `/nix/store/5k8lzdmn4xybrsw876ijv7mnrbmah4rq-virtiofsd-1.13.3`.
No local kernel build occurred.

Retained shell-log evidence:

| Stage / lines | Listeners and result |
| --- | --- |
| Initial service setup, 322–330 | `systemctl enable --now sshd.service` succeeds; only the three socat enablement symlinks are newly created |
| Initial readiness, 333–349 | IPv4/IPv6 port 22 and ports 80, 81, 443 all present |
| Initial policy, before restart at 16:00:22 CET | All six external allowed-port checks pass; IPv4/IPv6 port 81 denial checks fail as expected; existing/zone checks pass |
| Restart, 16:00:22–16:00:31 CET | Container restart succeeds; sshd stops cleanly, key-generation conditions are already satisfied |
| Post-restart timeout diagnostics, 1139–1272 | Only 80, 81, 443 listen; no sshd.service start attempt appears after boot; keygen target and generated AF_UNIX SSH socket are active |

Wildcard `systemctl status 'ssh*'` did not retain unloaded/inactive sshd state;
literal `UnitFileState`/drop-in information is therefore an evidence gap,
not an inferred disabled/failed status. Host-key and bind failures are not
shown. The TCP service is distinct from systemd's generated local AF_UNIX
socket. Architect verified exact official Fedora RPM
`openssh-server-10.5p1-1.fc45.x86_64`: vendor service has
`WantedBy=multi-user.target`, no alternative target or condition.

The native runner stopped/deleted its test container and powered off the guest
with status 0. Watcher reconciled runner PIDs 2310780/2330234, VM 2377102 and
virtiofsd 2374887 as exited; no test-owned effects remain running. No retry,
feature push, merge target preparation or new VM was performed after failure.

### Read-only image contract investigation

Runtime DNF output identifies Fedora 45,
`openssh-server-10.5p1-1.fc45.x86_64`, `firewalld-2.5.2-1.fc45.noarch`, and
`socat-1.8.1.3-1.fc45`. The exact imported image build/hash was not printed by
the run. The published default image index maps `fedora/latest` to 45; its
archive was last modified before this run, making association strong but still
an inference rather than a captured import checksum.

Read-only archive:
`https://images.vpsadminos.org/v1/vpsadminos/minimal/x86_64/fedora/45/image-archive.tar`.
Last-Modified `2026-11-07T07:54:36Z`, size 262716416 bytes,
ETag `"6aeed93c-fa8bc00"` enforced with `If-Match` during retrieval;
SHA-256 `b63c150090d0c594d2348a272bb493e9e7fb644bb81a19b4142210742cce46c4`.
Outer metadata exported_at `1794037392`; config identifies Fedora 45.
Files were decoded without installation or execution. Findings saved in
`/tmp/scheduled-workflow-fixes-h1/fedora45-image-units.json`:

- Persistent `etc/systemd/system/multi-user.target.wants/sshd.service` points
  to `/usr/lib/systemd/system/sshd.service`.
- Persistent `etc/systemd/system/sockets.target.wants/sshd.socket` points
  to `/usr/lib/systemd/system/sshd.socket`.
- `sshd.socket` has `Conflicts=sshd.service`, `ListenStream=22`, `Accept=yes`.
- Service uses ordinary `WantedBy=multi-user.target`; no SSH service drop-in or
  override was found in the archive.

Thus ordinary service enablement leaves an already-enabled conflicting socket
for reboot. This is a concrete image activation-graph defect matching the
observed missing TCP activation; exact boot job arbitration was not retained.
Architect/lead accepted the sufficient fixture-mode amendment below. No service
start after restart, sleeps or wait growth conceal persistence.

### Persistent SSH mode amendment: committed for review

Lead explicitly accepted/released the architect's recorded amendment. Current
whole-branch range is:

```text
f97785c2c265172a4c78893e0673034fde56e4dd  unchanged remote master base
cb7825245ea786fb0f51c469d1a7dc5c6a1ececc  tests: persist complete firewall fixture listeners
```

Consolidated the unmerged, unpublished original source commit with
`git commit --amend -F /tmp/scheduled-workflow-fixes-h1/amended-commit-message`
in the pinned shell, preserving ordinary hooks (none declared/active). Fresh
fetch/rebase reported the branch up to date. Worktree/index clean; comparison
captured at the new range. No remote/default history was rewritten.
No migrations, dependency/pin streams or obsolete intermediate commits.

The original reviewed/failed range remains explicitly
`f97785c2c265172a4c78893e0673034fde56e4dd..2cfbde649769509e2628600535e3023d872f1735`.
This is a substantive successor, not patch-equivalent evidence reuse: it adds
Fedora persistent activation selection and assertions. Original diff is retained
as `reviewed-readiness-only.diff`; full new diff `amended-final.diff`, exact
old-to-new diff `activation-amendment.diff`, under the temporary evidence root.
Full new diffstat: one file, 50 insertions, 8 deletions. Old-to-new delta:
15 insertions, 1 deletion.
Full new diff SHA-256
`27e16d7414c610c311d6c6d3a7f7417e17353c9fb83aa43b7bf79c46d20ccc87`;
old-to-new diff SHA-256
`5e58f7e03b9eb5cfc63a465299d99d4aa5f648122fc6b235d232c5c45a339e01`;
current firewall source SHA-256
`b55a74bd32b9ae5dcac9ac735b55bcfea610fdc3b135aefe083c08439d8e1ff8`.

Fedora setup alone disables/stops `sshd.socket` before the existing service
enable/start. A local literal check records named `Id`, `UnitFileState` and
`ActiveState`, then requires service enabled/active and socket disabled/inactive
both before exercise and after restart. Failure diagnostics name both units
explicitly. No start/repair action follows restart. Other distributions and all
shared readiness/timeouts, units and firewall assertions remain unchanged.

Amendment quick checks passed:

- Nix parse and pinned `nixfmt --check`.
- Actual generated amended Ruby syntax.
- Existing actual readiness probe against amended source, including diagnostic
  failure/original exception preservation.
- Actual firewalld example control-flow probe: socket disable precedes service
  enable, either setup failure stops progression, mode checked before exercise
  and after restart, no post-restart start command.
- Actual mode-check shell accepts enabled/active service + disabled/inactive
  socket and rejects each of the four wrong states independently. An initial
  temporary probe-shell case-pattern typo was corrected before this passed;
  that typo was not in project source.
- Pinned `nix eval .#testsMeta.x86_64-linux --json`,
  `ruby tools/check-page-contract.rb --tests-meta ...` (4 pages, 8 variants,
  12 tests, 21 executable samples) and `ruby tools/check-managed-page-sources.rb`.
- Byte comparisons prove unchanged external/established/ICMP assertion methods,
  shared setup/restart helpers, unit definitions and non-Fedora scenarios.
- Final complete-range `git diff --check`.

Reused the successful full static batch only for its unchanged capture/runtime
helper/tool/fixture/contract inputs. The sole changed Nix test source was reparsed,
reformatted, regenerated into Ruby, helper/control-flow exercised, and included
in fresh metadata/page contract validation. No integration result was reused.

Lead completed focused general+risk final review of the new full range and
old-to-new amendment, without findings. Exactly one fresh changed-source run
was then launched through fresh utility `/root/h1_amended_runtime_watcher`:

```sh
nix develop /tmp/scheduled-workflow-fixes-h1/dev-shell -c ./test-runner.sh test --fresh --state-dir /tmp/scheduled-workflow-fixes-h1/runtime-amended-state 'kb/firewall#firewalld'
```

This is the changed-source acceptance explicitly released by the lead, not a
retry of the failed unchanged test. Fresh utility policy rechecked against the
same selected package/catalog recorded above. Logs/receipt are
`runtime-amended.log` and `runtime-amended.result`; runner artifacts remain in
`runtime-amended-state/`, all under the same temporary H1 evidence root.
Source/lock hashes match the current reviewed range. A read-only preflight
`If-Match` HEAD request for the published Fedora archive confirms its prior ETag;
headers retained as `amended-image-before.headers`. Actual imported-checksum
association limits from the failed run remain explicit.

### Changed-source runtime: passed

The one released amended run exited 0 after 400 wrapper seconds; native script
370.23 seconds, sole example 158.13 seconds, result `expected_success`. No
unexpected local kernel build. Actual tested script is byte-identical to the
quick-checked generated Ruby, SHA-256
`530faeede406583247035bbab57a5dc6f89605b77648883bb09d1e8b5ce744c4`.
Exact native test JSON
`/nix/store/w3a7v42bkjjhqmq2yf1ngi3jnqd2nlag-os-test-kb-firewall.json`, derivation
`/nix/store/rdgvg1h9vya1ys6qgq4gq1yygpbb2r8z-os-test-kb-firewall.json.drv`.
Its system/kernel/initrd/squashfs/QEMU/virtiofsd paths equal the full machine
identity already recorded for the first run; source script differs exactly as
reviewed. Full unchanged input graph remains bound by flake.lock and its hash.

Native machine-shell receipt:

| Stage (2026-11-13 CET) | Service / socket | Listener and policy evidence |
| --- | --- | --- |
| 16:30:23–16:30:29, before exercise | `sshd.service` enabled+active; `sshd.socket` disabled+inactive | TCP 22 on IPv4/IPv6; 80/81/443 present |
| 16:31:03, initial policy | mode unchanged | six IPv4/IPv6 allowed probes succeed; both port81 denials fail as expected; original ICMP/established/zone assertions pass |
| 16:31:08 restart | no post-restart start/repair command | native restart succeeds |
| 16:31:17–16:31:23, after restart | service enabled+active; socket disabled+inactive | TCP 22 on IPv4/IPv6; 80/81/443 present |
| 16:31:30–16:31:35, persistent policy | mode remains correct | all original dual-stack allow/deny, ICMP and zone checks pass |

DNF/runtime identify Fedora 45 x86_64 and firewalld 2.5.2-1.fc45.noarch.
Read-only published archive `If-Match` HEAD requests before/after the run keep
the prior ETag, size and Nov7 modification date. This preserves the precise
published artifact receipt while retaining the native import-checksum gap;
the test itself did not print an archive SHA. The failed boot's exact job
arbitration is still not asserted. The new runtime independently proves the
supported fixture now persists its selected mode and passes the policy tests.

Native artifacts live beneath `runtime-amended-state/os-test-kb__firewall-3b3255f7/`:
`test-runner.log`, `test-result.txt`, `machine-shell.log`, `machine-console.log`,
`machine-log.log`, `machine-fs-vmSharedDir.log` and retained guest disk.
Runner container stop/delete and guest poweroff all exited 0. Watcher joined
the command and reported no surviving runner/QEMU/virtiofsd processes. No
unresolved operation effects remain.
Native machine-shell log SHA-256:
`06c303a0456285e2f9872aef6c3626ddfc0510ce239980670eb7b69ff90b4ca0`.

### Publication and lead merge-target handoff

After runtime pass, fresh `git fetch origin` and pinned-shell
`git rebase origin/master` were unchanged. Complete range diff-check passed;
feature worktree/index clean. Ordinary SSH push published
`2026-11-13-scheduled-workflow-fixes` at
`cb7825245ea786fb0f51c469d1a7dc5c6a1ececc`; fresh `git ls-remote` proves that
feature head and remote master still
`f97785c2c265172a4c78893e0673034fde56e4dd`. Master is an ancestor of the feature.
Final comparison captured; no default-branch mutation, PR or merge by implementer.

Per explicit lead direction, cancelled only
[Managed page runtime 43453670047 attempt1](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/43453670047)
after matching repository, workflow ID336079991, push event, exact feature
branch and current head. Final authoritative state: `completed/cancelled`.
Job131982108233 cancelled during Check repository; Prepare test state and Run
tests skipped; Cleanup test state succeeded. Other branches/default runs and
the independent Check workflow were untouched.
Feature Check run43453670102 attempt1 was still in progress when handed to the
lead; it was not awaited or represented as passed. Lead owns the integrated
master workflow acceptance. Remote refs were freshly verified at
`2026-11-13T15:34:50Z`.

Prepared detached target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/vpsfree-kb-contracts`.
HEAD `f97785c2c265172a4c78893e0673034fde56e4dd`, clean worktree/index, detached;
no declared hook framework and no executable non-sample hooks. No hook bypass
or repository claim was taken by implementer0 during preparation.

### Lead integration receipt

Lead accepted H1 delivery and reports fast-forward-only integration of the
exact final head `cb7825245ea786fb0f51c469d1a7dc5c6a1ececc` into remote master,
from `f97785c2c265172a4c78893e0673034fde56e4dd`, with fresh remote proof and a
clean target. Lead merge claim `07b183fb-c6ec-4a16-bee3-2a421a2eecfe` was held
15:35:57–15:36:36 UTC, then explicitly released and verified; no unresolved
effects were reported. This integration preserves the exact reviewed/tested
final head, not merely an equivalent successor. The earlier failed `2cfbde6`
is historical evidence and is not claimed to be an ancestor literally merged.

The master push automatically launched full
[Managed page runtime 43454286948 attempt1](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/43454286948)
at the same final head. Lead is reusing that actual master run because its
command runs the full suite, rather than dispatching a duplicate. Root watcher
owns monitoring. This receipt does not claim that pending master run passed.
No default/other run cancellation, extra check, source edit, target mutation or
lifecycle action was performed by implementer0 for this reconciliation.

Publication triggers the repository's broad Managed page runtime workflow on
`tests/**`. Lead explicitly directed deferring publication until review and
focused acceptance, then cancelling only that automatic run matching this exact
repository/feature branch/current head. No workflow edits or skip-CI markers.
Lead owns the user-approved integration and complete integrated-master workflow.
Do not cancel other branches or default-branch runs.

State/plan remain lead-owned. Implementer has no default-branch mutation, PR,
merge, deployment or production KB operation. No full feature-branch runtime
campaign will be launched for this readiness repair.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
