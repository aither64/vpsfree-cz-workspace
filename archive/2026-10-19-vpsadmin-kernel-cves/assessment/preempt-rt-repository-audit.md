# vpsAdminOS PREEMPT_RT repository audit

The repository **did contain an RT-enabled optional kernel package**, but the
inspected history does not select it as the default or in a tracked machine
configuration. This is compatible with the operator's statement that RT was
never deployed. Repository history alone cannot prove deployment absence.

- On **23 August 2023**, commit `7c9ca632` added `6.1.46-rt13` with
  `features.preempt_rt = true`. The same file kept the default at ordinary
  `6.1.46`. [Exact package and default](https://github.com/vpsfreecz/vpsadminos/blob/7c9ca632802667efba5fc010360a9c84d0e696ae/os/packages/linux/availableKernels.nix#L4-L14).
- That feature selects `PREEMPT_RT = yes` and `PREEMPTION = yes`; when the
  feature is absent it defaults to false. Thus this was an actual selectable
  RT configuration, not merely a reference in a patch.
  [RT configuration](https://github.com/vpsfreecz/vpsadminos/blob/7c9ca632802667efba5fc010360a9c84d0e696ae/os/packages/linux/common-config.nix#L60-L63),
  [false default](https://github.com/vpsfreecz/vpsadminos/blob/7c9ca632802667efba5fc010360a9c84d0e696ae/os/packages/linux/common-config.nix#L26-L28).
- On **8 September 2023**, commit `972c8d49` removed the optional RT package
  while changing the non-RT default to `6.1.52`.
  [Removal diff](https://github.com/vpsfreecz/vpsadminos/commit/972c8d49b5a2ff6d0459c6147e0d382039a61450),
  [new default](https://github.com/vpsfreecz/vpsadminos/blob/972c8d49b5a2ff6d0459c6147e0d382039a61450/os/packages/linux/availableKernels.nix#L3-L13). The locally retained release
  tags `vpsAdminOS-release-23.06-8` and `-9` still contain that old optional
  catalog. Both resolve to the same catalog blob as the addition.
- At inspected local origin/staging `a26791178a929adb96d978c093f6a3c5be4b0f9d`, stable is
  `6.12.113` and unstable is `6.18.49`; neither catalog entry enables the RT
  feature. The optional helper remains, with a false default, and the non-RT
  path requests `PREEMPT_NONE`.
  [Current kernel versions](https://github.com/vpsfreecz/vpsadminos/blob/a26791178a929adb96d978c093f6a3c5be4b0f9d/os/packages/linux/available-kernels.nix#L4-L5),
  [default selection](https://github.com/vpsfreecz/vpsadminos/blob/a26791178a929adb96d978c093f6a3c5be4b0f9d/os/packages/linux/packages.nix#L89-L93),
  [feature default](https://github.com/vpsfreecz/vpsadminos/blob/a26791178a929adb96d978c093f6a3c5be4b0f9d/os/packages/linux/common-config.nix#L37),
  [conditional RT helper](https://github.com/vpsfreecz/vpsadminos/blob/a26791178a929adb96d978c093f6a3c5be4b0f9d/os/packages/linux/common-config.nix#L85-L88),
  [non-RT path](https://github.com/vpsfreecz/vpsadminos/blob/a26791178a929adb96d978c093f6a3c5be4b0f9d/os/packages/linux/common-config.nix#L862).

All source changes touching the primary RT terms were inspected. The only
configuration enablement/removal pair is the 2023 optional package above;
`2d9d79a5` later reformats the helper with nixfmt. Other matches occur in
cumulative Linux patch conditionals/comments and do not enable a configuration.
No `PREEMPT_RT_FULL` match or `linux_rt`/`linuxPackages_rt` selector was found.
`PREEMPT_DYNAMIC`, XFS realtime support and realtime monitoring terminology
are distinct from PREEMPT_RT and were not counted as RT enablement.

## Scope and reproducibility

Read-only scan on 2026-10-20T13:24:17.518258+00:00 of canonical `repos/vpsadminos.git`:
**3,524 refs, 11,645 reachable commits,
103,215 reachable objects and 35,637 unique
blobs (541,052,340 bytes)**. Ref coverage includes 148 local branches,
337 remote-tracking refs, 81 tags and retained backup/archive/coordination refs.
No other-session worktree was accessed. The repository is not shallow, has no
partial-clone/promisor setting, and the reachable-object scan reported **zero
missing objects**. The two roots are the OS history from 2016-06-03 and merged
image-scripts history from 2014-06-12. Local origin/staging's tip is dated
2026-10-20T11:59:25Z. The ref inventory was unchanged at the end.

`GIT_NO_LAZY_FETCH=1` and `GIT_OPTIONAL_LOCKS=0` were used. `rev-list --objects
--all --missing=print` fixed the reachable-object inventory; `cat-file --batch`
scanned each unique blob case-insensitively for RT symbols and the optional
package name, then common alternate RT selectors. 49 text blob versions matched
the primary terms. Full-history/root/merge-parent `git log -G` identified the
relevant differences; exact trees supplied configuration context and immutable
line links. All retained branch/tag trees are covered through their reachable
blob objects. No missing-object fetch, network access, Nix evaluation, build,
test, API request, source/ref/index change or advisory change was performed.

The JSON [coverage/results](preempt-rt-repository-audit.json) binds the full
[ref inventory](preempt-rt-audit-evidence/refs.txt),
[keyword history](preempt-rt-audit-evidence/keyword-history.txt),
[matching blobs/lines](preempt-rt-audit-evidence/blob-scan.json), and alternate
selector scan with hashes. This proves coverage of locally available reachable
history, not deleted/unavailable remote refs. Compressed NARs were inspected as
raw stored blobs, not unpacked configuration evidence. External kernel/nixpkgs
inputs, downstream deployment configuration and fleet boot history are outside
this repository-only task.

The appropriate conclusion is: **RT was offered as an optional package for a
short period in 2023; no tracked default/use selection was found. Whether it ever
ran on a node requires deployment evidence, not this repository search.** The
confirmed operator statement remains the separate evidence for never deploying
RT; this finding does not silently revise any draft.
