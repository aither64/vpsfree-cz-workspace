# Released post-review batch A1: services and exact packaged API

Owner implementer0. Lead explicitly released the exclusive watcher slot after
final independent source review and successful B3 performance/auth/locale/output
acceptance. R1 closure is the lead's separately recorded decision. This batch
covers only mandatory services-up plus load/source/assets verification from the
exact package selected by that VM system closure. No further API/browser/CI,
provider/pin, source/Git, deployment, integration or lifecycle action is allowed.

Released source:70a2ed54b98d0c2f359a9cc4484452a257a9807b, clean worktree/index.
Session/current/environment binding verified. Host preflight found KVM available,
64 CPUs, about55GiB available RAM,149GiB free disk and48GiB free /dev/shm. The
ordinary services test uses one8GiB/eight-vCPU service VM with its configured
mailer container, jobs1 and explicit16GiB memory/shm and eight-CPU runner caps.
Unique temporary state and ownership are in ownership.json.

Fresh standalone utility: gpt-6-luna/low,
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, pinned catalog
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa.
Launch explicitly selects danger-full-access/approval never. watcher-launch.json
and watcher.log retain exact invocation/runtime confirmation. Utility owns the
only batch handle; no duplicate or automatic retry. Parent-written script is
/tmp/vpsadmin-a-services-released.py and captures full per-command logs, exact
exit/timing/PIDs and status.json. Kernel-build detection interrupts only the
owned command and escalates for effect reconciliation; no local kernel rebuild
is implicitly authorized.

Unlike a standalone overlay probe, the package is selected from the actual test
machine toplevel closure. Test config, system/profile, actual API and wrapped
Ruby store paths, .drv identities, full recursive derivation graphs, immutable
flake source graph and exact effective/packaged locks will be retained. Ordinary
services-up proves actual application/docs/assets; the same package's wrapped
Ruby then proves Fiddle/four0.30.2 gem/adapters and shared documentation files.
The packaged context/Rust/version sources and both legacy distributions are
checked against the verified released artifacts. New source graph identities
are recorded truthfully even if a test package labels its revision as unknown.

## Actual result: services runner setup failed

Attempt 1 failed before Python started because the watcher changed the outer
redirection. Its original `watcher-*` and `launch-failure-reconciliation.json`
artifacts remain unchanged. Lead accepted that command-start failure and
explicitly released a fresh attempt with the exact literal command:

```text
python3 /tmp/vpsadmin-a-services-released.py
```

Attempt 2 acknowledged that literal/argv before executing it once, without outer
redirection. `attempt2-watcher-launch.json`, `attempt2-command-received.json`
and `attempt2-watcher.log` prove the fresh Luna/low utility and explicit access
policy. The watcher outer handle 45184 finished. Its CLI exit 0 means it returned
a report; the actual batch exit is **1**, recorded separately in `status.json`
and `attempt2-watcher-result.md`.

The batch ran 09:00:40–09:09:41 UTC on 2026-10-26 (540.695 seconds).
Flake source graph capture passed in 0.638 seconds. The ordinary `services-up`
command exited 1 after 539.992 seconds; its native runner reported failure after
302.67 seconds. The runner built its test configuration/system, but failed in
`before(:suite) { services.start }` before starting the services VM or executing
service assertions:

```text
OsVm::Shell#prepare: UNIXServer.new(socket_path)
too long unix socket path (120bytes given but 108bytes max) (ArgumentError)
```

The parent-selected unique temporary root was too long for the runner's hashed
socket suffix. This is a test-state pathname error. It establishes no failure
of HaveAPI, Fiddle or generated documentation. A later authorized attempt must
use a short uniquely owned temporary root and check the complete socket-path
budget first. No source, provider or dependency pin correction is indicated by
this failure. No automatic retry occurred.

## Evidence and operation reconciliation

- `native-test-runner.log`, `native-services-log.log`,
  `native-services-shell.log` and `native-test-result.txt` retain native evidence.
- `failed-test-config.json` and `failed-test-paths.json` preserve the actual test
  configuration, system/profile and known derivations. The system is
  `/nix/store/2war0njnsnki8srg4v3bwj9kpcl25v1z-nixos-system-vpsadmin-services-26.05pre-git`;
  its derivation is
  `/nix/store/340dsj1shc5h6q7qpwgqqra3s6havbzr-nixos-system-vpsadmin-services-26.05pre-git.drv`.
  The test config is
  `/nix/store/yg5zy73il8xbk13v67x8ljm5icza7dpz-os-test-vpsadmin-services-up.json`;
  its derivation is
  `/nix/store/vc12ywkckmlw352bkzkklrppbq5blc70-os-test-vpsadmin-services-up.json.drv`.
- `flake-source-graph.json` captures the immutable source/input graph, including
  consumer `/nix/store/lzyiiff48xxp4idhy4k6806kxmvxg2qw-source`, vpsAdminOS
  `/nix/store/zd7z6pw3pkk6099kjvjryqq5xxgblygw-source` and followed Nixpkgs
  `/nix/store/5b2ic4sxjc2lzgxk4hninyw22r5gv5qr-source`.
- `attempt2-reconciliation.json` proves recorded command PIDs are absent and no
  process argv, cwd or readable file descriptor references the owned temporary
  root. Native machine logs record `kill SIGNAL: NONE` and `destroy`; no guest
  remains. No parent cancellation was necessary.
- Native and outer logs show no unexpected local Linux kernel derivation build.
  Kernel paths observed were substituted or copied to the generated image.
- `source-before.json` equals `source-final.json`. A fresh final Git/hash check
  confirms exact head `70a2ed54b98d0c2f359a9cc4484452a257a9807b`, tree
  `f1cb0699d91ab11b461d94b1174bc43cf28f14ef`, clean worktree/index and unchanged
  effective API, packaged API, flake, Composer and JavaScript hashes.

The exclusive watcher slot was released to lead after effect reconciliation
(report `efbfad4c-6b07-49b5-83e2-7b1d6cf98f96`). Lead owns integration into the
shared current state. No repository/Git mutation, deployment, merge, session
lifecycle change or deletion of retained evidence occurred.

## Remaining verification

Services-up has **not passed**. Actual service startup, shared documentation,
Go/Rust examples and PHP/console assertions were not reached. The subsequent
same-closure API selection/build/load, Fiddle/libffi and four-gem version/source
checks, packaged assets and recursive derivation graphs also did not run.
These remain separate required gates. Other API/browser batches remain subject
to lead release; no all-suite or CI result is claimed. This execution evidence
needs no application documentation change.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
