# 2026-08-09-kb-kvm-review

## Repositories

- `vpsadmin-kb-captures`
  - branch: `2026-08-09-kb-kvm-review`
  - worktree:
    `worktrees/2026-08-09-kb-kvm-review/vpsadmin-kb-captures`
  - base: `origin/master` at `f54352d`
- `vpsadminos`
  - branch: `2026-08-09-kb-kvm-review`
  - worktree: `worktrees/2026-08-09-kb-kvm-review/vpsadminos`
  - base: `origin/staging` at `579737ac9`
- Reference repositories: `repos/vpsadmin.git` and `repos/vpsadminos.git`.

## Status

- The KVM article includes the requested backup-link correction, realistic
  storage screenshot, and production-shaped guest networking. The
  capture-local immutable-source wrapper is in place; the shared vpsAdminOS
  test framework and pin remain unchanged. The final networking defects found
  by the maintained test are committed and have passed quick verification;
  fresh review, a maintained rerun, exact GitHub Actions, and restaging remain.
  Production remains untouched.
- The isolated capture-repository worktree has been created.
- Runtime-test, contract, CI, and bilingual KB sources are implemented in two
  reviewable commits: `1d1cffc` and `0cbfa2e`.
- Mandatory fresh-context review completed with blocking findings. All listed
  fixes are implemented, and the same reviewer approved the final two-commit
  result with no remaining findings before VM integration tests.
- The original candidates were staged for review. Production remains untouched.

## 2026-08-10 storage and networking extension

- Commit `a27124b Point KVM snapshot references at backup documentation`
  changes the dataset-snapshot link from exports to the Czech and English
  backup pages. Targeted runtime-contract and diff checks passed.
- Commit `b7633ce Give the KVM storage example realistic headroom` changes the
  documentation and dedicated capture fixture to a 120 GiB allocation split
  between a 20 GiB root dataset and 100 GiB `vm-images` subdataset, with an
  80 GiB first guest disk leaving 20 GiB free. The runtime storage scenario
  uses the same ratio at test scale and asserts at least 20 percent logical
  headroom. The shared `data` fixture remains unchanged.
- A bridge-mode `screenshots` devcluster successfully created and mounted the
  dedicated `vm-images` dataset, but node1 stopped answering on its bridge
  before Playwright reached the dataset page. Stopping the initiative's own
  cluster then exposed an exhausted shared filesystem. Only this initiative's
  stopped 13 GiB generated cluster state was reset; no other session data and
  no production or staging content was changed. Shared capacity subsequently
  recovered to 255 GiB free.
- Networking implementation in progress documents and tests three permanent
  production-shaped paths: a public VPS `/32` with libvirt NAT and persistent
  TCP/UDP port forwarding; a public `/32` routed via the VPS private `/32` and
  onward to a libvirt domain; and an IPv6 `/128` routed from the VPS `/64`
  without NAT. The outer VPS veth is explicitly kept out of libvirt bridges.
- The new `kb/kvm#networking` RSpec scenario builds a deterministic KVM guest
  appliance in Nix, exercises the exact article scripts, and checks inbound
  HTTP/SSH/UDP, outbound source addresses, route-via state, and idempotent hook
  reconciliation. The test-only appliance is not exposed in user
  documentation.
- Quick verification of the in-progress networking tree passed Nix parsing,
  Bash parsing, ShellCheck for all changed samples, runtime-contract validation
  with five scripts and five samples, tagged test inventory evaluation, the
  generated test-JSON build, generated networking-script Ruby syntax, and
  inspection of the built 27 MiB kernel/initrd appliance. The initrd contains
  BusyBox, Dropbear, and the complete compressed virtio dependency chain.
- Commit `757c8ff Document production-shaped KVM guest networking` adds the
  bilingual NAT and routed-network guide, reusable scripts, runtime contract,
  and permanent `kb/kvm#networking` RSpec scenario. Commit `db75d2c Capture
  realistic KVM image-storage headroom` records the regenerated Czech and
  English dataset screenshots. Commit `62568a3 Refresh routed-network
  navigation discovery` classifies the two new annotated vpsAdmin navigation
  paragraphs in the independent inventory.
- A fresh bridge-mode `single` devcluster captured both language variants from
  the dedicated `kvm-storage` fixture. The resulting Czech image is 821x361
  with SHA-256
  `5addfc72ce42d8a69bc8ce57ae10bb3da5f8089d1759152ecfe0dacf6352eeb1`;
  the English image is 813x308 with SHA-256
  `5b319b10e335f91d9bd1fc21500dcea7af56a35d85be682397004c84f4563de2`.
  Both show the 20 GiB root and 100 GiB `vm-images` subdataset mounted at
  `/srv/libvirt/images`. The capture wrapper twice remained in its event loop
  after writing a successful result and closing Chromium; only the completed
  wrapper was interrupted. Both images were validated and visually inspected,
  and the cluster stopped cleanly.
- Coordination commit `172df09 Guard updates of existing KB media` extends
  `bin/kb-contract-build` with explicit `policy: update` media objects guarded
  by the exact production SHA-256. Create remains the default and rejects a
  source hash. Its tests pass with 18 runs/97 assertions, and the staging-tool
  suite passes with 23 runs/71 assertions.
- Read-only production media fetches recorded the existing Czech screenshot
  SHA-256
  `2bb7e5d12c91cc812145ee9f1a50cc20e3f08a2ff08a2c3349637dd5e1562e2a`
  and English screenshot SHA-256
  `5f77a96899cd100f51c75f3d0f1060f0d9a4f4a37fba8528c0cfa2908b6c0c9d`.
  The rebuilt release manifests each contain one guarded page replacement and
  one guarded media update. Candidate pages are byte-identical to the contract
  sources, and complete-corpus annotation discovery passes with 69 bindings
  and 9 exceptions.
- Final quick verification before mandatory review passed the complete
  `nix develop --command bin/check`, a build of the `kb/kvm` test derivation,
  candidate/source annotation validation, both coordination unit suites, and
  `git diff --check`. The capture worktree is clean at `62568a3`; coordination
  `master` is clean for the two intended tooling paths at `172df09` and is one
  commit ahead of `origin/master`.
- Mandatory fresh-context review found three important lifecycle gaps and no
  blocking or advisory findings. Storage, bilingual parity, snapshot links,
  route-via semantics, IPv6 delegation, iptables chain scoping, guest
  isolation, screenshot checksums, and both release manifests were otherwise
  accepted. The findings were:
  - production media hashes were checked only during promotion, so staging
    could review a stale production baseline;
  - redefining an already-active routed libvirt network changed only persistent
    XML and could silently leave old live routes;
  - the test invoked the NAT hook directly without proving libvirt's automatic
    `network.d` stop/start lifecycle.
- Coordination commit `2d83746 Reject production media drift before KB
  staging` checks create/update media against production before any staging
  mutation and tolerates candidate content only during approval-gated
  promotion retries. The regression suite now includes production drift while
  staging remains unchanged and passes with 24 runs/77 assertions; the
  candidate-builder suite remains green at 18 runs/97 assertions.
- The first combined network-lifecycle correction was rewritten before push
  after focused review required independently reviewable commits. Commit
  `81802fd Reject active routed-network redefinition` refuses to redefine an
  active routed network and prints the safe domain/network stop-and-rerun
  procedure. It forces `LC_ALL=C` for stable `virsh` output. The maintained
  test proves changed inputs are rejected without changing inactive XML,
  applies and verifies them after a deliberate stop, restores the real routes,
  and restarts the guest.
- Commit `e5fdd34 Exercise libvirt NAT hook lifecycle` separately stops the NAT
  guest and default network, verifies automatic hook cleanup, starts the
  network, verifies automatic rule restoration, restarts the guest, and checks
  traffic before the existing direct idempotent reload coverage.
- Quick verification after these fixes passed the complete capture `bin/check`
  suite, the `kb/kvm` derivation build, both coordination unit suites, Bash/Ruby
  syntax, and whitespace checks. Candidates and one-page/one-media manifests
  were rebuilt; both candidate articles are byte-identical to contract sources
  and complete-corpus navigation validation still passes with 69 bindings and
  9 exceptions.
- Focused re-review accepted the automatic libvirt hook fix, but required the
  split above, locale-independent active detection, proof that refusal leaves
  persistent XML unchanged, and direct media retry coverage. Coordination
  commit `448925c Cover retry semantics for guarded KB media` now proves that
  staging rejects candidate production media for both create/update policies
  and that approval-gated promotion retries accept both forms after a partial
  save. The coordination suites pass with 26 runs/91 assertions and 18 runs/97
  assertions. A final focused review of `81802fd`, `e5fdd34`, and `448925c`
  was required before VM integration.
- A third standalone reviewer with fresh context approved `81802fd`,
  `e5fdd34`, and `448925c` with no blocking, important, or advisory findings.
  It confirmed locale-stable refusal before `net-define`, unchanged persistent
  XML coverage, changed-route application/restoration, automatic libvirt hook
  cleanup/restoration with recovered traffic, focused commit boundaries, and
  create/update staging and promotion-retry semantics. The reviewer ran only
  the short unit suites and explicitly approved proceeding to the maintained
  VM integration test.
- The first post-review maintained run exposed a separate test-runner source
  safety defect before VM execution. The stopped screenshot cluster had a
  sparse 320 GiB node image and 12 GiB service image under ignored
  `.devcluster`. The pinned resolver treated the absolute worktree as a path
  flake and streamed about 333 GiB of logical content into fully allocated Nix
  store source `/nix/store/b6s4mpnhfbq6vr58h0xqm1464lc8vyyb-source`.
  Free space fell from roughly 178 GiB to 124 GiB. The run was stopped as soon
  as the source copy was confirmed; no VM example completed and the result is
  invalid as acceptance evidence.
- Only this initiative's stopped generated devcluster state was reset. The
  copied source, wrapper, and derivation had no live GC roots and were removed
  through Nix garbage collection. Free space recovered to roughly 499 GiB.
- A new vpsAdminOS worktree now changes
  `test-runner/nix/resolve-repository-source.nix` to use a `git+file` flake for
  any checkout with `.git`, retaining the old path fallback for non-Git source
  trees. A permanent RSpec fixture creates a linked Git worktree with ignored
  `.devcluster/disk.img` and asserts the immutable Nix source excludes it.
  Focused specs pass with 7 examples/0 failures. The initial command without
  `-Itest-runner/spec` and the next run without the local `libosctl/native`
  prerequisite failed before examples; the documented native build procedure
  was then used and the maintained focused command passed.
- The first fresh-context review found one Important compatibility defect:
  `repoRootString` entered the `git+file` URL without escaping, so otherwise
  valid checkout paths containing spaces or URL delimiters failed before
  source resolution. No other findings were reported, and no VM tests ran.
- The second fresh-context review confirmed the Git branch fix, but found the
  same Important path-URI issue in the retained non-Git fallback. The fallback
  now uses the escaped path as an explicit `path:` flake reference, and the
  existing immutable-source fixture runs from `plain #?%`. No other findings
  were reported, and no VM tests ran.
- Final vpsAdminOS commit `2b5145b13 Filter Git repository sources` passes
  filesystem inputs with `--argstr`, percent-encodes the Git file URI, and
  proves the complete pipeline from a linked worktree path containing a space
  plus `#`, `?`, and `%`. Dirty tracked content remains available while
  ignored and untracked files are excluded. The escaped `path:` fallback is
  covered with the same special characters. The focused spec passes with 7
  examples and the complete test-runner suite passes with 177 examples and no
  failures. Nixfmt, RuboCop, pre-commit hooks, and commit-message hooks passed.
  The branch was force-pushed; queued CI jobs for superseded commits were
  cancelled.
- Final capture commit `0ec5753 Use filtered vpsAdminOS test sources` pins the
  runtime contract, flake input, and all imported workflow actions to
  `2b5145b13`, and makes vpsAdmin follow the same explicit vpsAdminOS input.
  The complete `bin/check --allow-missing` suite, `actionlint`,
  `git diff --check`, the
  generated `kb/kvm` test declaration, and discovery of all five `kb-runtime`
  scripts passed.
- The real capture-repository resolver now creates a 4 MiB Nix source with a
  3.3 MiB apparent size. Store free space remained near 490 GiB throughout
  verification. A third standalone reviewer approved final ranges
  `579737ac9..2b5145b13` and `e5fdd34..0ec5753` with no Blocking, Important, or
  Advisory findings. It independently reran the focused resolver specs,
  runtime contract, exact pin/follow checks, and tagged listing; it also
  confirmed the 4 MiB source contains no `.devcluster` or `*.img` content. No
  VM tests ran during review, and the exact maintained suite is now approved.
- The first exact maintained run at capture head `0ec5753` completed in
  2,328.08 seconds. `storage`, `platform-defaults`, `nfs-locking`, and
  `libvirt` passed. `networking` failed before its examples because the helper
  treated `NetworkInterface#add_route`'s `fire2` result Array as the
  TransactionChain and called `chain.id`; the retained log is
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b/test-runner.log`.
- Pinned vpsAdmin API call sites and existing tests destructure the first
  result element. Capture commit `9cdb2ea Handle vpsAdmin route transaction
  tuples` applies `chain, = add_route(...)` to both routed IPv4 and IPv6
  helpers. Full capture quick checks and the generated `kb/kvm` test
  declaration pass. A standalone mandatory reviewer approved the commit with
  no findings after confirming `fire2` returns `[chain, ret]` and both helpers
  wait on the returned chain. A maintained networking rerun remains.
- Exact-head GitHub runtime run `31391339443` reproduced the same networking
  failure while the other four scripts passed. Its artifact
  `kb-kvm-test-logs-31391339443` was downloaded and inspected; both
  `services-shell.log` and `test-runner.log` contain the same `NoMethodError`
  at the pre-fix `chain.id`, so the CI failure has the same identified root
  cause rather than an unrelated runner failure.
- At the user's request, an additional independent design review is mapping
  every workspace consumer of the vpsAdminOS test framework, checking path and
  dirty-worktree assumptions, comparing source-filter designs, and proposing
  a wider vpsAdminOS/consumer verification matrix. The framework change will
  not be considered complete solely from the KB consumer run.
- The wider review found seven maintained external consumers and no observed
  current breakage, but identified a materially larger compatibility surface
  for a central source-filter contract: Git subflakes, submodules, untracked
  development inputs, and non-Git sources all require policy decisions and
  workspace-wide verification.
- The user identified that captures already enters through a Git flake. A
  focused independent follow-up found no blocker to exporting the capture
  flake's immutable `${self}` source as `TEST_RUNNER_REPO_ROOT` and recommended
  this narrower design. It preserves the shared vpsAdminOS framework contract;
  tests, metadata, and tracked extensions all resolve from the same source.
  Captures does not use the one caveat, absolute checkout-local
  `--test-config` paths; future uses should pass relative paths.
- Capture commit `e02a612 Use the immutable capture flake as the test source`
  wraps both `apps.test-runner` and `packages.test-runner`. The wrapper uses
  the original `837baf040` vpsAdminOS pin. Its source is 3.3 MiB apparent / 4.0
  MiB allocated and contains neither `.devcluster` nor `*.img`; the normal
  `./test-runner.sh` entry point lists all five `kb-runtime` scripts. The full
  `bin/check --allow-missing` suite and the generated `kb/kvm` derivation build
  pass. Route-tuple fix `cd973e2` follows as a separate commit after the
  history rewrite.
- The proposed vpsAdminOS source-filter branch is no longer consumed by this
  initiative and will not be merged. No all-consumer framework rollout or
  integration matrix is required for the capture-local fix.
- Mandatory fresh-context review approved exact capture range
  `e5fdd34..cd973e2` with no Blocking or Important findings. Its sole Advisory
  finding was the stale open-work entry below, now corrected. The reviewer
  independently confirmed the wrapper source size/content, unchanged
  `837baf040` pin, extension/test source behavior, route tuple contract, commit
  split, and quick checks. No VM test was run during review; the maintained
  networking rerun remains required.
- The first maintained run after the capture-local source redesign completed in
  2,336.97 seconds. `nfs-locking`, `storage`, `platform-defaults`, and
  `libvirt` passed. `networking` progressed past the corrected IPv4 route tuple
  and then failed while creating its IPv6 fixture: `Network` declares a stale
  `belongs_to :user`, but the pinned database has no `networks.user_id`, so
  assigning `user:` raised `ActiveModel::MissingAttributeError`. The complete
  retained log is
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b/test-runner.log`.
- Commit `22a02cb Match the routed IPv6 fixture to the network schema` removes
  only the invalid global-network owner assignment. The registered IPv6 prefix
  remains owned by `vps.user`, which is the persisted ownership boundary.
  Full `bin/check --allow-missing`, the generated `kb/kvm` derivation build,
  Nix parsing, and whitespace checks pass. A fresh mandatory review and the
  maintained networking rerun remain.
- A fresh mandatory review approved `cd973e2..22a02cb` with no Blocking,
  Important, or Advisory findings. It confirmed that the 2018 routable-subnet
  migration removed `networks.user_id`, current network seeds create global
  networks without owners, the `/64` `IpAddress` retains `vps.user` ownership,
  and the prefix/split/size values satisfy the pinned model. No VM test ran
  during review; `kb/kvm#networking --fresh` is approved as the final runtime
  proof.
- The reviewed `networking --fresh` rerun reached both route helpers: IPv4
  returned transaction chain 4 with `198.51.100.11` routed via private
  `10.106.0.10`, and IPv6 returned transaction chain 5 for
  `2001:db8:200::/64`. It then failed after 1,175.74 seconds when the
  private-only outer VPS fetched the test guest appliance from services at
  `172.16.106.53:18080`. The request reached the internal network, but services
  had return routes only for the public IPv4 test range and routed IPv6 range;
  `curl` timed out after 135 seconds. The first public-address VPS had fetched
  the same persistent Nginx asset successfully, ruling out a one-shot server.
- Commit `f8ae87a Route private test addresses through the vpsAdminOS node`
  adds the missing declarative services route for `10.106.0.0/24` via node1 at
  `172.16.106.41`. This models the production guarantee that private addresses
  work on the internal network. Full `bin/check --allow-missing`, the rebuilt
  services VM closure and generated `kb/kvm` derivation, and whitespace checks
  pass. A fresh mandatory review and maintained networking rerun remain.
- A fresh mandatory review approved `22a02cb..f8ae87a` with no Blocking,
  Important, or Advisory findings. It confirmed services-to-node route
  direction, declarative ownership beside the public-prefix route, unchanged
  Ganesha authorization, and that node MASQUERADE remains limited to private
  traffic leaving `eth0` while internal traffic on `eth1` retains its private
  source. No VM test ran during review; a fresh networking rerun is approved.
- The exact `f8ae87a` networking rerun completed after 2,133.14 seconds. Its
  capture-local source remained 3.3 MiB and store capacity stayed safe; the
  sparse test state used about 13--14 GiB while retaining a 333 GiB apparent
  size under `/tmp/os-test-runner`. The private-only VPS successfully fetched
  both guest assets through the added internal route, and its public `/32`
  route-via assertion passed.
- The same run exposed two later permanent-test defects. Both deterministic
  KVM appliances failed to answer because their initramfs opened
  `/dev/console` before mounting `devtmpfs`; with `set -e`, init could exit
  before loading virtio or configuring networking. The active routed-network
  guard also fell through to `net-define` and reported the existing UUID
  instead of refusing the active network. The retained log is
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b/test-runner.log`.
- Commit `f1db60e Mount devtmpfs before opening the guest console` fixes only
  the deterministic appliance boot order. Commit `878c659 Detect active
  libvirt networks by name` changes both documented scripts to consume the
  complete `virsh net-list --name` output rather than parsing localized
  `net-info` labels or using an early-closing quiet grep. Czech and English
  pages, sample hashes, and section fingerprints remain synchronized.
- Post-fix quick verification passed `nix develop --command bin/check
  --allow-missing`, Bash syntax and whitespace checks, and a complete rebuild
  of the `kb/kvm` test declaration including the corrected initramfs and
  services VM closure. Candidates are byte-identical to the contract pages;
  their new SHA-256 values are
  `6cc4a3887d7a443efea5bfeddbdb1a8e54be3a3f87e09501444e04b4a551c564`
  (Czech) and
  `d3a5d6e80b62993d99ed862943653d2ada102b69f838c18618bf100ed600c63b`
  (English). Release manifests were regenerated but not staged.
- Exact `f8ae87a` GitHub static run `31405605311` passed. Runtime run
  `31405605528` failed after all five scripts executed; its complete
  `kb-kvm-test-logs-31405605528` artifact was downloaded and inspected. The
  other four scripts passed, while networking reproduced the same unreachable
  NAT/routed appliances and active-network `net-define` error as the local
  run. The two post-fix commits therefore address the identified CI root causes
  rather than treating a rerun as acceptance evidence.
- Mandatory review of `f8ae87a..878c659` found no correctness or compatibility
  defect in either fix, but reported one Important permanent-diagnostic gap:
  the libvirt PTY console had no reader, so another early appliance failure
  would still be visible only as an external timeout. The reviewer withheld
  rerun approval until that gap was fixed.
- Commit `21fce40 Retain KVM guest boot diagnostics` sends each guest's serial
  console to a persistent per-domain libvirt log and makes the first NAT,
  routed-IPv4, and routed-IPv6 endpoint waits report bounded endpoint, domain,
  interface, route, firewall, console, and QEMU-log state on failure. A focused
  re-review found that one combined 8 KiB probe could let the final QEMU tail
  evict earlier evidence, so the unpushed commit was amended to keep each
  labeled section independently bounded. Full
  `bin/check --allow-missing`, the generated `kb/kvm` test build, and
  whitespace checks pass; `virt-xml-validate` also accepts the generated
  file-backed serial-console shape. Final focused re-review approved exact
  range `f8ae87a..21fce40` with no Blocking, Important, or Advisory findings
  and approved the maintained networking rerun. No VM test ran during review.
- The exact `21fce40` networking rerun reached all setup paths and used the new
  diagnostics. The NAT console showed `Initramfs unpacking failed: write
  error`, followed by missing `/proc` and a PID 1 panic: the 128 MiB guest had
  only about 59 MiB available after kernel reservations for a 41 MiB unpacked
  initramfs. Commit `8e413ed Give the KVM guest enough initramfs memory` raises
  the deterministic appliance to 256 MiB; both outer VPSes retain ample space
  within their 1 GiB test allocation.
- That run also proved the new active-network guard emits the documented
  refusal and leaves inactive XML unchanged. After the deliberate
  `net-destroy`, however, `virsh net-define` rejected XML for the same network
  name because it would generate a different UUID. Commit `745de40 Preserve
  the routed libvirt network identity` reads an existing network UUID and
  carries it into regenerated XML, allowing an inactive persistent network to
  be updated without an undefine gap. Fresh review required the lifecycle test
  to protect that design directly, so the unpushed commit was amended to assert
  the same valid UUID before the update, after changed routes, and after
  restoring the production-shaped routes.
- Full `bin/check --allow-missing`, Bash/whitespace checks, and the generated
  `kb/kvm` build pass for both follow-up commits. Candidates remain
  byte-identical to the contract pages; their SHA-256 values are now
  `6993ab4b41d3229fd1ad7934a2c345293b3efcf5ba0cf62d99f2e3ba74e7e121`
  (Czech) and
  `655cb1b61b66317dc17bc2920a33f27e6d0671ec5116d9151203b7a2b25f1c23`
  (English). Release manifests are rebuilt but not staged. Fresh mandatory
  review remains before another maintained run.
- Fresh mandatory review accepted the memory increase and UUID-preserving
  implementation, but withheld rerun approval because the lifecycle test
  asserted route changes without directly protecting identity continuity. The
  amended `745de40` now validates and compares the UUID at all three lifecycle
  points. Focused re-review approved exact final range `21fce40..745de40`
  with no Blocking, Important, or Advisory findings and approved the
  maintained networking rerun. No VM test ran during review.
- The exact `745de40` networking run proved the capture-local source boundary
  in the live runner: `TEST_RUNNER_REPO_ROOT` resolved to a 4.0 MiB immutable
  store source with neither `.devcluster` nor `*.img`. The 320 GiB apparent
  node image stayed sparse under `/tmp/os-test-runner`; it used about 1.5--3
  GiB while the two VPSes were provisioned instead of being copied to the Nix
  store. NAT HTTP/SSH/outbound access and its repeatability passed, as did the
  routed network's route-only, active-state guard, changed-input, and stable
  UUID assertions.
- The same maintained run retained a routed-guest console failure before the
  two end-to-end examples: BusyBox 1.37 `ip` rejected iproute2's `nodad`
  address flag, then the test init exited. Commit `1a2800b Support IPv6
  configuration in the BusyBox test guest` removes the two unsupported fixture
  flags. The documentation-prefix addresses are unique and normal kernel IPv6
  duplicate-address detection remains enabled. `git diff --check`, the rebuilt
  `kb/kvm` test declaration, and full `bin/check --allow-missing` pass.
- Exact `745de40` GitHub runtime run `31414509338` failed after all five
  scripts executed. Its uploaded `kb-kvm-test-logs-31414509338` artifact was
  downloaded and inspected; the routed guest console contains the same
  BusyBox `nodad` rejection and PID 1 panic twice. This confirms the CI and
  local failures have the same fixture root cause rather than an unrelated
  runner failure.
- Fresh mandatory review approved exact commit `1a2800b` with no Blocking,
  Important, or Advisory findings. It independently confirmed the pinned
  BusyBox 1.37 address syntax, focused commit split, unchanged documentation,
  scripts, pins, and deployment surface, and normal DAD behavior for the
  unique documentation-prefix fixture. The reviewer approved the maintained
  networking rerun; executing the corrected initrd remains the residual test
  gap.
- The exact `1a2800b` networking rerun again passed NAT, port-forward
  reconciliation, route-only, active-state, changed-input, and UUID assertions.
  The routed guest progressed beyond the unsupported flag but then emitted
  `RTNETLINK answers: Invalid argument`: normal DAD left its just-added public
  IPv6 `/128` tentative while init immediately installed a default route with
  that address as the preferred source. Both end-to-end examples therefore
  reached their maintained timeouts.
- The unmerged fixture correction was amended into commit `394a206 Configure
  IPv6 with BusyBox in the KVM test guest`. Its bounded helper waits up to ten
  seconds for each requested IPv6 address, fails immediately on `dadfailed`,
  and installs the preferred-source route only after transit and public
  addresses are present and non-tentative. The generated `kb/kvm` test
  declaration, full `bin/check --allow-missing`, and whitespace checks pass.
- Fresh mandatory review approved exact final commit `394a206` with no
  Blocking, Important, or Advisory findings. It confirmed the exact built
  BusyBox applets support the helper syntax, every outcome is bounded or
  fail-closed under `set -e`, both exact address/prefix states are checked, the
  commit remains focused, and the vpsAdminOS pin is unchanged. The maintained
  libvirt/virtio rerun remains the required end-to-end proof and is approved.
- The exact `394a206` networking run passed examples 1--4 and proved the
  corrected guest completes IPv6 DAD and reaches its HTTP, SSH, and outbound
  service startup. End-to-end traffic was then rejected in both directions.
  Retained outer-VPS diagnostics show libvirt's `LIBVIRT_FWI/FWO` jumps ahead
  of an otherwise accepting `FORWARD` policy, while guest logs show repeated
  connection refusals. The public `/32` and `/128` routes sit outside the
  transit `<ip>` subnets covered by `forward mode='route'` filters.
- Commit `69ebe24 Leave routed libvirt filtering to the VPS firewall` changes
  the exact reusable script and both articles to `forward mode='open'`, which
  keeps kernel routing but asks libvirt not to create forwarding firewall
  rules. The articles explicitly assign filtering to the VPS firewall. The
  runtime contract protects that boundary, and failure diagnostics now retain
  complete IPv4/IPv6 filter tables. Full `bin/check --allow-missing`, the
  generated `kb/kvm` declaration, Bash syntax, and whitespace checks pass.
  Fresh mandatory review approved exact commit `69ebe24` with no Blocking,
  Important, or Advisory findings. It independently confirmed libvirt `open`
  semantics, the external-filtering boundary, bilingual sample identity,
  runtime assertions, and the unchanged vpsAdminOS pin. The maintained VM
  rerun remains the end-to-end acceptance proof and is approved.
- The guarded candidates were rebuilt from `69ebe24` and are byte-identical to
  the contract pages. Their SHA-256 hashes are
  `9d7b145a1ae1da710c82a37d298f7a513fe4a615a95af315c6edeca540980c20`
  (Czech) and
  `8f1b2bad044517e0a656af414e0d58e498727aad80d86732e00c8b697187314e`
  (English). Staging was reset to a clean production mirror and both current
  guarded manifests were staged and verified again. The two obsolete
  Czech pages matched `kb-deletions.yml` in both production and staging before
  their staging copies were deleted; post-delete checks show them absent in
  staging and present at the unchanged guarded hashes in production. Both
  candidate manifests still verify after the deletions. Production remains
  untouched.
- The exact maintained networking rerun at `69ebe24` passed the NAT scenario,
  repeatable/additional forwards, route-only outer-VPS state, active-network
  lifecycle and UUID preservation, and routed IPv4 inbound/outbound paths.
  Routed IPv6 alone timed out. Retained diagnostics show the `/128` route and
  running guest were correct and both IPv4/IPv6 filter tables had accepting
  policies with no rules; the guest's outbound IPv6 probe also timed out.
  This isolates the remaining failure to forwarding state rather than routes
  or firewall policy. A raw `0xff` kernel-console byte prevented the diagnostic
  JSON from being rendered, although each constituent command remained in the
  machine log.
- Commit `df15c0f Enable forwarding for the routed libvirt network` persists
  and applies both forwarding sysctls in the exact bilingual sample and
  asserts their live and on-disk values. Commit `c9a0f01 Keep KVM failure
  diagnostics valid UTF-8` independently scrubs binary diagnostic output.
  Whitespace, Bash syntax, the full `bin/check --allow-missing` suite, and the
  generated `kb/kvm` declaration pass. The first mandatory review found no
  technical defect but blocked the combined `e86feef` history because the two
  fixes were independently reviewable. The unpushed commit was split without
  changing its final tree. Focused follow-up review approved both commits with
  no Blocking, Important, or Advisory findings and approved the maintained VM
  rerun. No VM ran during review.
- The approved `c9a0f01` rerun was stopped before either test VM started when
  the user requested a network-section redesign. Its queued GitHub runtime was
  cancelled as superseded. The article must first explain and compare complete
  dual-stack NAT and routed topologies, then show essential commands before
  introducing full reusable scripts. The routed design should use the VPS's
  primary IPv6 `/64` for its next-hop address and a distinct delegated `/64`
  on the libvirt bridge, rather than making a selected `/128` from the VPS
  prefix the primary recommendation. Final runtime acceptance is deferred to
  the redesigned maintained scenarios.
- Commit `c72c38b Document complete dual-stack KVM networking` implements the
  redesign in the capture repository. The NAT topology now defines an explicit
  IPv4/ULA IPv6 network with NAT44, NAT66, and persistent IPv4/IPv6 port
  forwards. The routed topology gives each test VPS a production-shaped
  primary IPv6 `/64` and routes a separate `/64` through the routed VPS's
  primary address onto the libvirt bridge; public IPv4 remains routed through
  the VPS's private `/32`. Both articles compare the designs and explain their
  XML, essential commands, guest configuration, and script lifecycle before
  embedding the exact automation.
- The first mandatory review found one Blocking issue: the new NAT network
  reused the active libvirt `default` network's `192.168.122.0/24`, so both
  bridges could install the same connected route. It also advised against a
  mnemonic ULA that could silently collide when private networks are later
  interconnected. The unmerged commit was amended to use
  `192.168.124.0/24`, to keep `default` active and autostarted in the maintained
  coexistence test, and to use the random-looking example ULA
  `fd5f:6d2e:9c4a::/48`. Both articles explain when operators must generate a
  different ULA and change the host and guest addresses together.
- Quick verification for amended `c72c38b` passed `git diff --check`, the complete
  `nix develop -c bin/check` suite, Nix parsing, Bash and generated Ruby syntax,
  and a build and JSON parse of `.#tests.x86_64-linux."kb/kvm"`. The repository
  declares no hook framework. No VM ran; mandatory fresh-context review is the
  next required gate. The vpsAdminOS pin remains
  `837baf04054c6ee0e71d288b8870ac42a6990c38` and the shared framework is
  unchanged.
- Fresh focused re-review approved the pre-integration amended tree at
  `aba00f9` with no Blocking,
  Important, or Advisory findings. It confirmed distinct active libvirt
  subnets, the ULA collision guidance, exact bilingual sample hashes, the
  production-shaped route model, unchanged dependency pins, and the focused
  single-commit contract. No VM ran during review; the maintained exact-head
  networking integration is approved. Candidate rebuilding and staging remain
  deferred until the runtime result is known.
- The exact `aba00f9` maintained networking run completed after 1,983.77
  seconds and retained complete logs in
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b`. Its immutable source remained
  small and the 320 GiB apparent node disk stayed sparse; about 13--15 GiB of
  real test state was used and more than 440 GiB remained free. The control
  plane passed: the default and dual-stack networks coexisted, IPv4 and IPv6
  route-via state was correct, forwarding was enabled, and routed network
  lifecycle/UUID checks passed.
- The same run exposed two test-only defects before any endpoint could answer.
  Libvirt normalized `<nat ipv6='yes'/>` into a non-empty element with a
  generated port range, so the exact-string assertion rejected valid XML. Both
  guests then received an IPv6 default route from libvirt router advertisements
  before their BusyBox init used `ip -6 route add default`; the duplicate route
  aborted PID 1 with `RTNETLINK answers: File exists`. Amended `c72c38b`
  accepts the normalized NAT element and uses supported BusyBox `route replace`
  semantics for deterministic IPv4 and IPv6 defaults. Full `bin/check`, the
  generated test build and Ruby syntax pass; inspection of the exact built
  initrd confirms all four default-route paths use `replace`. No article or
  reusable user script changed in this correction. Fresh mandatory review is
  required before rerunning the maintained scenario.
- Fresh focused review approved exact head `c72c38b` with no Blocking,
  Important, or Advisory findings. It confirmed libvirt's normalized XML
  representation, BusyBox 1.37 `route replace` support in all four branches,
  the cohesive single-commit history, unchanged pins, and test-only deployment
  scope. No VM ran during review; the exact-head maintained networking rerun
  is approved.
- The exact `c72c38b` networking rerun completed in 1,628.70 seconds. Five of
  six examples passed: the complete NAT TCP/HTTP/SSH and outbound scenario,
  both routed control-plane/lifecycle scenarios, and routed IPv4 and IPv6
  traffic. Only the additional IPv6 UDP check failed, after the preceding IPv4
  UDP check had succeeded. Retained `services-shell.log` shows one successful
  IPv4 datagram followed by repeated empty IPv6 responses; the port-forward
  configuration itself completed successfully.
- The failure is isolated to the synthetic guest's BusyBox UDP echo listener.
  A local reproduction shows that one BusyBox `nc -u -l ... -e cat` listener
  answers the first IPv4 or IPv6 peer and then ignores the other family while
  remaining alive. The fixture now uses `socat UDP6-RECVFROM` with
  `ipv6only=0` and `fork`, which answered sequential IPv4 and IPv6 probes in a
  local reproduction. No article text or user-facing networking script changed.
  The cohesive amended capture commit is now `89c704b`.
- Quick verification for `89c704b` passed `git diff --check`, Nix parsing, the
  complete `nix develop -c bin/check` contract suite, and a build and JSON/Ruby
  parse of `.#tests.x86_64-linux."kb/kvm"`. Inspection of the built guest initrd
  confirms both the `socat` closure/symlink and the exact dual-stack listener
  invocation. The failed maintained run cleaned up normally, left 453 GiB free,
  and did not copy its sparse test disks into the Nix store. A fresh mandatory
  review is required before the next networking rerun.
- The fresh mandatory review of `89c704b` found no issue with the topology,
  commit split, exact bilingual contract, `socat` listener, dependency pins, or
  sparse-image design. It did identify one Important failure path in the new
  dual-stack hook: colon-only address-family checks accepted malformed IPv6,
  then the hook removed every live rule before `ip6tables` rejected the value.
- Amended commit `285f47f` validates both public and guest addresses with
  Perl's numeric `Socket::inet_pton` before calling `cleanup`. The maintained
  scenario appends a malformed IPv6 line, requires the hook to reject it,
  compares all four saved NAT/filter tables before and after, and then proves
  the existing IPv4 and IPv6 UDP forwards still carry traffic. Both articles
  embed the corrected script exactly and explain that a syntactically invalid
  line is rejected before active rules change; hashes and section fingerprints
  were refreshed.
- Quick verification for `285f47f` passed `git diff --check`, Nix parsing,
  representative valid/invalid `inet_pton` probes, the complete
  `nix develop -c bin/check` suite, a generated `kb/kvm` test build at
  `/nix/store/hja5c9jfqpa3p57vj2ijwxhbys0985bj-os-test-kb-kvm.json`, JSON and
  generated Ruby syntax, and inspection of the malformed-edit regression in
  the generated script. A fresh follow-up mandatory review is required before
  the long VM rerun.
- The fresh follow-up review confirmed the address fix and preservation checks,
  but found two further Important parser paths in `285f47f`: an unbounded
  digit-only port could wrap in Bash arithmetic before `iptables` rejected its
  original text after cleanup, and `read` skipped a valid final record without
  a newline, allowing cleanup to silently remove that forward.
- Amended commit `2da6dc6` restricts both ports to one through five decimal
  digits and canonicalizes them with base 10 before range checking. The config
  loop now processes EOF data when the final record lacks a newline. The
  maintained preservation regression also rejects the overflowing value
  `18446744073709551617` without changing any of the four saved firewall tables
  or either working UDP path. It then applies an unterminated valid final record
  and proves its forwarded UDP traffic before removing it again.
- Quick verification for `2da6dc6` passed `git diff --check`, Bash/Nix parsing,
  focused base-10/overflow/unterminated-record probes, the complete
  `nix develop -c bin/check` suite, and a generated test build at
  `/nix/store/76jn3xkz3gvgpygx52fxi6f5dlfr3w27-os-test-kb-kvm.json` with valid
  JSON/Ruby syntax and the expected generated failure-path examples. A fresh
  follow-up mandatory review is required before the long VM rerun.
- Fresh follow-up mandatory review approved exact head `2da6dc6` with no
  Blocking, Important, or Advisory findings. It confirmed that bounded,
  canonical base-10 ports cannot wrap, EOF data is processed exactly once,
  addresses remain family-validated before cleanup, all failure-path table and
  traffic assertions are sound, exact bilingual embeddings/hashes match, and
  the single commit remains cohesive. The reviewer ran the complete static
  suite but no VM test. Residual risk is limited to non-configuration backend
  or resource failures after cleanup; the script promises syntax safety, not a
  transactional cross-family firewall update. The exact-head maintained
  networking VM rerun is approved.
- The exact `2da6dc6` maintained run completed in 1,921.82 seconds. All four
  routed examples passed again, including control-plane/lifecycle and IPv4 and
  delegated-IPv6 traffic. Both NAT examples failed because the Nix-generated
  Ruby test source represented fixture scripts as double-quoted Ruby strings:
  Ruby interpreted the Bash fragment `10#$public_port` as interpolation of a
  global variable and transported `public_port=$((10))` into the VPS. The
  retained node log proves the received hook forwarded every configured port
  as 10, exactly explaining the HTTP and additional-UDP timeouts. Teardown
  completed normally; logs remain in
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b`.
- The capture-side correction emits every executable fixture as an escaped
  single-quoted Ruby literal, where `#` does not interpolate. A new pre-suite
  guard compares the runtime value of all five transported fixture strings to
  their Nix-computed SHA-256 before starting any cluster. This protects all
  maintained scripts and would have rejected the faulty generated value before
  provisioning. No article or user-facing fixture changed in this correction.
- The cohesive amended capture commit is now `ac4e4bd`. Quick verification
  passed `git diff --check`, Nix/Ruby syntax, the complete
  `nix develop -c bin/check` suite, and a generated test build at
  `/nix/store/h3ch6x9p0y5958n27zwbamc5446ncz60-os-test-kb-kvm.json`. A focused
  evaluator loaded each of the five generated Ruby methods and proved its
  returned bytes and SHA-256 exactly match the source fixture; the generated
  NAT value contains the intact `10#$public_port` expression and the pre-suite
  hash guard. A fresh mandatory review is required before another VM run.

## 2026-08-10 operator rework

- Current branch head `c62158e` passed GitHub static run `31350442321` and KVM
  runtime run `31350442322`. These results predate the requested rework and will
  not be used as final acceptance evidence.
- Correct the article to describe KVM inside a vpsAdminOS container as direct,
  first-class hardware virtualization rather than nested virtualization.
- Reduce feature availability to the KVM/TUN requirements, their default-on
  state, and the existing screenshot.
- Remove the redundant Debian `systemctl enable --now` command, the smoke test
  domain, the guest-networking non-section, and manual disk-image creation.
- Recommend a dedicated default-property subdataset mounted at
  `/srv/libvirt/images` and configured as a persistent libvirt directory pool.
- Explain `recordsize=128K` as the default maximum block size and retain raw as
  the default image format on ZFS, with qcow2 reserved for its extra features.
- Keep the maintained NFSv3 read-only installer-ISO workaround and deletion of
  the unlinked historical pages.
- Commit `0ff66a2 Rework KVM guide around direct virtualization and libvirt`
  implements the operator rework in both languages and in the durable runtime
  contract. It replaces the hand-created image and smoke-domain fixtures with
  the exact persistent libvirt directory-pool commands.
- Quick verification for `0ff66a2` passed `git diff --check`,
  `nix develop --command bin/check --allow-missing`, `actionlint`, the tagged
  test inventory, generated test-JSON build, and Ruby syntax for all four
  generated test scripts. The repository declares no hook framework and has
  no configured `core.hooksPath`.
- Mandatory review found that the direct/not-nested statement and the Debian
  template statement initially sat outside all section fingerprints. Both now
  live in a guarded article section with explicit claims. Focused
  follow-up review approved final commit `0ff66a2` with no blocking,
  important, or advisory findings. No VM tests were run by the reviewer.
- The exact maintained integration command
  `./test-runner.sh test --fresh --jobs 1 --filter 'tag=kb-runtime'` passed at
  `0ff66a2` in 1,540.24 seconds. Platform defaults passed both examples,
  libvirt passed package-managed startup/system-connection and direct KVM
  capability checks, storage passed the mounted inherited-property subdataset
  and persistent libvirt-pool volume checks, and NFS passed both the bounded
  no-NLM lock wait and exact read-only `nolock` sample.
- The NFS server fixture uses Ganesha only to make the failure condition
  deterministic: `Enable_NLM = false` serves NFSv3 while intentionally
  omitting `nlockmgr`. The Debian VPS still uses the normal Linux kernel NFS
  client. A kernel `nfsd` fixture would normally couple the export to kernel
  lockd/NLM and would not express this lockless-server contract directly.
- Commit `9b003c6 Clarify separate snapshots for KVM image datasets` removes
  all backup-plan instructions and says only that the image subdataset is
  snapshotted separately from the root dataset. Focused mandatory review found
  no findings and confirmed that another VM run was unnecessary because no
  command, fixture, test, workflow, or pin changed.
- Final all-page candidate validation replaced two stale KVM Features
  discovery IDs and removed two discoveries belonging to deleted
  troubleshooting paragraphs. Commit `27dd79f Refresh KVM navigation discovery
  inventory` records that mechanical result. Focused review found no findings;
  the final candidate files are byte-identical to the reviewed contract pages
  and validate with 67 bindings and 9 exceptions.
- Commit `7d06c98 Make the KVM guide read as final user documentation` removes
  the generic opening sentence and the unhelpful Availability heading while
  preserving its content under the libvirt installation section. It also
  describes `recordsize=128K` directly as the default maximum file-record
  size. Commit `19f34bc` refreshes the two resulting paragraph discovery IDs.
  Focused review approved both the prose/contract and final derived inventory
  with no remaining findings; another VM run was unnecessary because runtime
  code and samples did not change.
- Final release manifests use Czech candidate SHA-256
  `33301ea0738fdaaf958b303ae629aff38d265b847d0fd7d367e54a6be42e5662`
  and English candidate SHA-256
  `c06963453008c3b859b2c9ed80cfd9334b220c59ea276be6e0b2e044bd2a4c9e`.
  Staging was reset to a clean 116-Czech/70-English-page and 224-media
  production mirror, then both manifests were staged and verified. Rendered
  HTTP checks show both revised titles, `/srv/libvirt/images`, the OpenZFS link,
  both screenshots, and bidirectional language links.
- After exact production and staging hashes matched `kb-deletions.yml`, the
  two obsolete staging pages were deleted again. API checks show them absent
  from staging and present unchanged in production; rendered pages expose the
  DokuWiki missing-page marker.
- Final branch head `19f34bc` is pushed. The superseded runtime run
  `31371464090` for `0ff66a2` was cancelled after the follow-up push. Runs
  `31372223713` and `31372223776` both passed at the preceding documentation
  head `27dd79f`. Exact-final-head static run `31373225916` and runtime run
  `31373226340` are in progress.

## Decisions

- Debian/libvirt is the primary and only complete walkthrough.
- Historical Alpine/OpenRC instructions are removed rather than maintained as
  a second untested path.
- KVM and TUN are documented as enabled by default and verified at runtime.
- ZFS defaults remain unchanged. A subdataset is recommended as a boundary for
  future workload-specific property changes, while tuning remains
  measurement-driven.
- NFS troubleshooting remains only if the maintained test supports its narrow
  read-only ISO scope.
- Guest networking covers the public-VPS NAT case and production routed
  IPv4/IPv6 cases. The commands and traffic paths are covered by a dedicated
  maintained test; the outer routed VPS interface is never bridged.
- Permanent validation lives in `vpsadmin-kb-captures` and consumes the pinned
  vpsAdminOS test framework; no disposable one-time VM validation is used.

## Commands run

- `bin/dev-session current`
- Read-only production fetches for the current KVM, dataset, export, and
  historical Alpine/libvirt pages in both languages where present.
- Fetched `origin` in the reference bare repositories.
- Inspected current vpsAdmin dataset defaults, VPS feature/device mappings,
  WebUI dataset forms, capture contracts, cluster setup, and upstream OpenZFS,
  QEMU, NFS, and Alpine documentation.
- `git --git-dir=repos/vpsadmin-kb-captures.git fetch origin --prune`
- Created the `vpsadmin-kb-captures` feature worktree from `origin/master`.
- Read the repository-local `AGENTS.md`.
- Added four RSpec-style `kb/kvm` runtime scripts using the pinned external
  vpsAdminOS test framework and the existing capture-cluster topology.
- Added executable documentation samples, section fingerprints, bilingual page
  sources, screenshot/navigation bindings, and static/recurring CI.
- Verified the current official action releases before selecting
  `actions/checkout@v7`, `actions/upload-artifact@v7` through the pinned
  vpsAdminOS composite action, and
  `DeterminateSystems/nix-installer-action@v22`.
- `nix develop --command bin/check --allow-missing` (pass)
- `nix shell nixpkgs#actionlint -c actionlint` (pass)
- `nix eval --raw '.#tests.x86_64-linux."kb/kvm".drvPath'` (pass;
  derivation evaluated without booting VMs)
- `git diff --cached --check` (pass)
- Confirmed the repository declares no hook framework and has no configured
  `core.hooksPath`.
- Committed `45d8ca1 Add test-backed nested KVM documentation`.
- Mandatory review result: changes requested.
  - The dataset helper expanded an inner Ruby interpolation in the outer test
    process and would fail before querying the API.
  - The NFS export did not authorize or route the VPS public source prefix.
  - The NFS test bypassed another live client's valid lock, contradicting the
    documented single-client safety condition.
  - Static CI/test-framework support and the KVM feature need separate commits.
  - Sparse physical allocation must be asserted for qcow2 as well as raw.
  - Bilingual runtime bindings should enforce equal claim/test/sample sets.
- Resolutions implemented:
  - Build the dataset path without nested interpolation.
  - Replace the second NFS client with one read-only VPS client and an isolated
    NFSv3 Ganesha fixture with NLM deliberately disabled, an explicit return
    route, and authorization for the actual VPS source prefix.
  - Assert physical allocation for both image formats and enforce bilingual
    section parity with stable section keys.
  - Rewrite the unmerged branch into independent support and KVM commits.
- Replaced `45d8ca1` in the unmerged feature history with two commits. The
  first split (`87d10fc`/`e456c04`) still registered the KVM suite from the
  support commit before the suite existed. The final split is:
  - `1d1cffc Expose the vpsAdminOS external test framework`, with an empty,
    independently evaluable test catalog
  - `0cbfa2e Add test-backed nested KVM documentation`, which registers the
    KVM suite together with its implementation
- Post-fix quick verification:
  - `nix develop --command bin/check --allow-missing` (pass; runtime unit
    suite now has 6 examples and 16 assertions)
  - `nix shell nixpkgs#actionlint -c actionlint` (pass)
  - `nix eval --raw '.#tests.x86_64-linux."kb/kvm".drvPath'` (pass)
  - `./test-runner.sh ls --filter 'tag=kb-runtime'` (pass; four scripts)
  - `git diff --cached --check` and final worktree status (pass/clean)
  - exact `1d1cffc` commit through `git+file`: both `tests` and `testsMeta`
    evaluate to empty attribute sets (pass)
- Mandatory follow-up review of `1d1cffc..0cbfa2e`: approved, no remaining
  blocking, important, or advisory findings; no VM tests were run by reviewer.
- First maintained integration run:
  `./test-runner.sh test --jobs 1 --filter 'tag=kb-runtime'` (stopped after
  diagnosing a deterministic readiness failure). The helper requested
  `api.vpsadmin.test`, which resolved to the services VM but did not match the
  configured API virtual host. Nginx therefore selected the password-protected
  Adminer default host and returned HTTP 401 once per second. Logs and the
  generated Nginx configuration confirmed the mismatch; the run was stopped
  instead of waiting out the remaining 600-second timeout.
- Initial integration fix `6df342b` added `api.vpsadmin.test` as a test-only
  alias of the configured API virtual host. Focused review found that Varnish
  also dispatches by exact Host, so the alias would otherwise depend on its
  implicit default backend ordering.
- Amended integration fix `9b9d2ac` maps the stable name explicitly and routes
  it through matching Nginx and Varnish API entries. `nix develop --command
  bin/check --allow-missing` and Nix parsing pass. Focused re-review approved
  the fix with no findings.
- The second maintained integration run reached all four runtime scripts and
  proved the API hostname fix. Every script then stopped in the shared VPS
  setup helper: `vps new` completed successfully and returned the created VPS,
  but the immediately following `vps show ID` could not resolve that object.
  Since the tested documentation does not concern a separate start action, the
  helper now uses the create action's supported `start: true` input and waits
  for the resulting container directly. This also follows the transaction that
  owns creation instead of adding an unrelated API lookup between creation and
  runtime assertions.
- Replaced test-script constants with methods because the test runner evaluates
  the common prelude once per selected script in the same evaluator class;
  constants produced harmless but noisy redefinition warnings.
- Focused mandatory review approved the lifecycle semantics but required the
  independent warning cleanup to be split for reviewability. Rewrote the
  unmerged `6c7dfac` as:
  - `a2891e2 Start documentation VPSes in their create actions`
  - `a3b9204 Avoid repeated KB script constant warnings`
  The same reviewer approved `9b9d2ac..a3b9204` with no remaining findings and
  confirmed that the final tree is unchanged.
- Post-integration-fix quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass; 8 contract tests
    with 50 assertions, 7 annotation tests with 17 assertions, and 6 runtime
    contract tests with 16 assertions)
- The third maintained integration run passed API and local nodectld readiness,
  and `vps new --start` completed, but the container remained absent while the
  helper polled it. Upstream vpsAdminOS suites have a further required gate:
  the API must report both `node.status` and `node.pool_status` before any VPS
  provisioning transaction is submitted. The run was stopped once this
  deterministic missing gate was identified instead of waiting for its
  900-second container timeout.
- Commit `b38564d Wait for API node readiness before creating VPSes` adds that
  maintained API gate. `git diff --check` and the full static `bin/check` pass;
  focused mandatory review approved it with no findings. The reviewer
  confirmed that command failures retry, false readiness flags continue
  polling, and malformed successful responses fail visibly. A maintained rerun
  remains.
- The fourth maintained run proved the new gate passed before VPS creation,
  but the creation chain still did not yield a container. The run was stopped
  after several minutes of deterministic absence. Commit `54ba44a Report
  provisioning transaction failures directly` now waits on the chain itself
  and reports each transaction's node, queue, status, and bounded output before
  polling the container. This turns the opaque symptom into persistent suite
  diagnostics for the next run.
- Focused review of the first diagnostic commit found that its timeout raised
  before collecting transaction details and that Ruby's short-string tail
  slice returned `nil`. Both findings are fixed in amended commit `54ba44a`:
  the deadline now exits polling and emits the full diagnostic object with a
  timeout flag, and short outputs are preserved while longer outputs remain
  capped at 2,000 characters.
- Post-amendment quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - `nix eval --raw '.#tests.x86_64-linux."kb/kvm".drvPath'` (pass)
  Focused re-review approved `54ba44a` with no blocking, important, or
  advisory findings. The reviewer confirmed that timeout diagnostics are
  emitted before assertion failure and that bounded output preserves short
  values. No VM tests were run by the reviewer. The maintained integration
  rerun exposed the provisioning failure described below.
- The fifth maintained run reached the first storage scenario and failed its
  VPS creation chain at `netif_create_veth_routed`. The new diagnostic showed
  that all preceding create transactions completed and were then rolled back;
  the visible rollback error tried to lock the absent
  `/run/config/vps/1.yml`. The remaining scenarios were stopped because they
  share the same VPS setup.
- Root cause: the capture-cluster seed created a `Pool` database record but did
  not execute the pool-create transaction on the node. The node-side pool
  initialization that creates nodectld's working directories therefore never
  ran. This is a cluster-fixture failure, not a nested-KVM or networking claim.
- Three focused commits address the finding:
  - `5b6efa1 Allow runtime clusters to skip database pool seeds` adds a
    default-preserving cluster option for integration tests.
  - `6157112 Preserve provisioning phase errors in test diagnostics` reports
    structured execute/rollback errors with bounded values and backtraces.
  - `9e6d9ff Provision the KVM test pool through vpsAdmin` disables the pool
    seed for this suite, creates `tank/ct` through the normal API action, and
    waits for that chain before creating a VPS.
- Post-fix quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - `nix eval --raw '.#tests.x86_64-linux."kb/kvm".drvPath'` (pass)
  - built the generated test JSON without running VMs; the generated storage
    script passes `ruby -c`, and the exact runtime seed contains no pool-record
    seeding code (pass)
  Focused mandatory review approved all three commits with no blocking,
  important, or advisory findings. The reviewer confirmed the default is
  preserved, the commits are independently reviewable, pool creation is
  ordered before VPS creation, and both diagnostic phases remain bounded. No
  VM tests were run by the reviewer. The maintained rerun remains.
- The sixth maintained run proved the fixture fix end to end: pool chain 1
  completed with `storage_create_pool`, and VPS chain 2 completed all thirteen
  transactions, including routed-veth creation and `vps_start`. The resulting
  container existed but rejected `osctl ct exec 1 -- true` continuously for
  more than two minutes with only the generic error `executed command failed`.
  The remaining shared-setup scenarios were stopped.
- Commit `8b97933 Report container startup failures with runtime state`
  replaces the opaque 900-second exec poll with a 180-second maintained check.
  If startup does not succeed, it reports the API VPS object, full `osctl ct
  show`, the last exec result, and the final 8,000 characters of the last 200
  container-log lines.
- Startup-diagnostic quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - Nix derivation evaluation and generated test JSON build (pass)
  - generated storage script through `ruby -c` (pass)
  Focused review of the first version found that the pinned machine API raises
  on a command timeout, which could bypass all collected evidence. The amended
  commit routes readiness and diagnostic commands through a best-effort probe:
  every command records its status/output or exception, output is bounded, and
  one final assertion reports the combined evidence. Post-amendment full static
  checks, derivation evaluation/build, and generated-script syntax all pass.
  Focused re-review confirmed the blocking finding is resolved and found one
  advisory issue: timeout exception messages can themselves include unbounded
  buffered output. Amended commit `8b97933` applies the same 8,000-character
  tail bound to exception messages. Full static checks and derivation
  evaluation pass. Final focused confirmation approved `8b97933` with no
  remaining blocking, important, or advisory findings. No VM tests were run by
  the reviewer. A maintained rerun remains.
- The seventh maintained invocation did not reach container startup. The test
  runner reused the node's disk from the interrupted sixth run while creating
  a fresh API database; VPS ID 1 therefore collided with the existing
  `/tank/ct/1/private` dataset. Structured diagnostics identified the exact
  failing `mkdir` in `storage_create_dataset`. The other scenarios were
  stopped because they shared the stale machine disk.
- Commit `aa5af68 Run KVM documentation tests with fresh disks` adds the test
  framework's `--fresh` option to both documented local invocations and the CI
  command. This makes disk recreation part of the maintained validation path,
  rather than requiring manual or one-off cleanup.
- Fresh-disk quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - `nix shell nixpkgs#actionlint -c actionlint` (pass)
  Focused mandatory review approved `aa5af68` with no blocking, important, or
  advisory findings. The reviewer confirmed that `--fresh` reaches the pinned
  runner's disk recreation, preserves attempt logs/results, and removes only
  known machine disk images. No VM tests were run by the reviewer. The exact
  documented `--fresh` rerun remains.
- The eighth maintained run used fresh disks and completed both pool and VPS
  chains. Its startup diagnostic proved the VPS was actually healthy at both
  layers: the API reported `is_running: true`, and `osctl ct show` reported
  `STATE: running` with a live init PID. The helper itself was wrong: the
  pinned `osctl ct exec` treats `--` after the container ID as the command to
  execute, not as an option separator, so every probe tried to run a program
  named `--`. The other scenarios were stopped because all used the same
  helper.
- Commit `02056d1 Use the supported osctl exec argument form` removes that
  separator from readiness, scripted guest execution, and shell-command guest
  execution.
- Exec-syntax quick verification:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - Nix derivation evaluation/build and generated-script `ruby -c` (pass)
  - generated test script contains only `osctl ct exec ID COMMAND` forms
    (pass)
  Focused mandatory review approved `02056d1` with no blocking, important, or
  advisory findings. The reviewer confirmed all three exec sites and their
  quoting/argument boundaries against the pinned CLI. No VM tests were run by
  the reviewer.
- The ninth maintained run used fresh disks and exercised all four scenarios.
  Platform defaults passed all three examples, storage passed both examples,
  and libvirt passed both examples including a running nested KVM domain. The
  NFS scenario reached its server over the routed network, but both NFSv3
  mounts were rejected by Ganesha before the locking behavior could be tested.
  The complete run took 1,213.84 seconds and failed only
  `kb/kvm#nfs-locking`.
- The NFS fixture follow-up keeps the exact routed public `/32` model visible:
  it obtains the assigned public IPv4 from vpsAdmin, asserts its `/32` prefix,
  and checks that the guest route to the synthetic NAS selects that address as
  its source. It also uses Ganesha's recommended common v3/v4 pseudo-path form
  and adds bounded guest/export/journal diagnostics for any future mount
  failure. Commit `ae82639 Verify routed NFS clients in the KVM documentation
  test` contains the change.
- Quick verification for `ae82639`:
  - `git diff --check` (pass)
  - `nix develop --command bin/check --allow-missing` (pass)
  - generated test JSON build (pass)
  - concatenated generated test scripts through `ruby -c` (pass)
  Focused mandatory review approved the commit with no blocking, important,
  or advisory findings. The reviewer confirmed the routed `/32` contract,
  Ganesha 9.13 pseudo-path behavior, and the per-probe 8,000-character bounds.
  No VM tests were run by the reviewer.
- The tenth maintained run selected only `kb/kvm#nfs-locking` on fresh disks.
  It confirmed that vpsAdmin assigned `198.51.100.10/32`, that the guest route
  to the NAS selected `198.51.100.10` as its source, and that Ganesha saw the
  same remote address. The pseudo-path change fixed the previous mount denial.
  The exact read-only `nolock` example then passed. Without `nolock`, QEMU
  waited for NLM until the maintained 300-second outer command timeout instead
  of emitting the historical lock error. The article and first example are
  adjusted in commit `31bea4c Cover NFS lock waits in the KVM documentation`
  to cover both observed outcomes: a lock wait or an immediate lock error.
- Quick verification for `31bea4c` passed `git diff --check`, the full
  `bin/check --allow-missing` contract suite, the generated test JSON build,
  and generated-script Ruby syntax. Focused mandatory review found two
  important cleanup issues: a double-forked QEMU could escape `timeout`, and a
  bare status 137 did not prove that the test deadline had expired.
- Commit `cfea390 Clean up timed-out QEMU processes deterministically` adds a
  bounded pidfile-based TERM/KILL cleanup before unmounting, propagates cleanup
  failures, and accepts timeout exit statuses only when GNU `timeout --verbose`
  reports sending TERM at its deadline. Its quick verification passed
  `git diff --check`, the full `bin/check --allow-missing` contract suite, the
  generated test JSON build, generated-script Ruby syntax, and a local check of
  the GNU timeout diagnostic. Focused follow-up review and the maintained NFS
  rerun remain. The focused follow-up review approved the correction with no
  blocking or important findings. It noted that a hypothetical `rm -f`
  failure would not override a later successful unmount; this is accepted
  because pidfile removal is still attempted before unmount, while the
  material process-survival and unmount failures do propagate.
- The eleventh maintained run selected only `kb/kvm#nfs-locking` on fresh
  disks. The exact read-only `nolock` example passed in 6.64 seconds, while the
  no-`nolock` example reached its maintained 90-second outer timeout. Retained
  logs in `/tmp/os-test-runner/os-test-kb__kvm-1adc155b` show QEMU kept the
  command-substitution output pipe open after the inner deadline, so Bash
  could not reach the pidfile cleanup. This is test-harness behavior, not a
  contradiction of the documented NLM wait; the same fixture again proved the
  workaround.
- Commit `8e9b9c4 Keep QEMU lock diagnostics out of a substitution pipe`
  redirects GNU timeout diagnostics to a regular file, allowing the shell to
  observe the deadline, clean up the detached pidfile process, and then read
  the diagnostic. Its quick verification passed `git diff --check`, the full
  `bin/check --allow-missing` suite, the generated test JSON build, and
  generated-script Ruby syntax. Focused mandatory review approved it with no
  blocking or important findings and repeated the accepted advisory about
  hypothetical temporary-file removal failures. The maintained rerun remains.
- The twelfth maintained run selected `kb/kvm#nfs-locking` on fresh disks and
  passed. The no-NLM example observed the bounded lock wait and completed its
  pidfile cleanup in 23.11 seconds; the exact read-only `nolock` example passed
  in 5.24 seconds. The script completed in 627.69 seconds and the complete
  fresh test in 698.73 seconds. This validates both the conditional NFS warning
  and the narrowly scoped workaround on the routed public `/32` fixture.
- The final maintained integration used the exact documented command
  `./test-runner.sh test --fresh --jobs 1 --filter 'tag=kb-runtime'` from
  commit `8e9b9c4` and passed all four scripts in 1,289.13 seconds. NFS passed
  both examples (23.71 and 5.44 seconds), platform defaults passed all three
  examples, storage passed both examples, and libvirt passed both examples,
  including a running nested KVM domain. The complete fresh test succeeded.
- `bin/kb-contract-fetch` captured the guarded production corpus: 116 Czech
  and 70 English pages. The full-text backlink scan found no occurrence of
  `kvm-openrc` or `vpsadminos:libvirt`, so
  `navody:vps:kvm-openrc` and `navody:vps:vpsadminos:libvirt` are unlinked
  deletion candidates. Their guarded source hashes are recorded in the source
  index.
- Building the two full-page replacements exposed that the annotation checker
  discovered paragraph indexes from the old production body and then applied
  them to the rewritten candidate, raising an `IndexError`. Commit `13c7e20
  Validate navigation discovery on final KB candidates` makes independent
  discovery describe the final candidate corpus while retaining complete
  source/candidate/inventory identity checks, with a full-page-layout
  regression test.
- Commit `a1ca7eb Describe KVM defaults through the Features section` names the
  localized vpsAdmin **Features/Funkce** section in both articles, updates the
  candidate navigation inventory, and refreshes the availability fingerprints.
  The real 116/70-page candidate now validates with 67 bindings and 9
  exceptions. The full `bin/check --allow-missing` suite passes with 8/50,
  8/18, and 6/16 test results. Focused mandatory review found no implementation
  defect but required the README, canonical workflow, and one diagnostic to
  describe candidate rather than source discovery. Commit `c62158e Document
  candidate navigation discovery boundaries` makes that distinction and
  records the separate source-identity and release-integrity guards. Focused
  follow-up review approved the correction with no findings.
- Guarded release manifests were generated for one page per language:
  `kb-release-cs.yml` uses source revision `1697799832` and
  `kb-release-en.yml` uses source revision `1697799870`. The global staging
  container was claimed by this initiative, reset from 116 Czech pages, 70
  English pages, and 224 shared media objects, then both manifests were staged
  and verified at `navody:vps:kvm` and `manuals:vps:kvm`.
- The staged pages render their revised headings and OpenZFS/QEMU links, their
  Czech/English counterpart links point at each other, and all four referenced
  feature/dataset screenshot objects exist. Both old pages matched their
  guarded production hashes before their staging copies were deleted; API and
  rendered checks confirm they are absent in staging.
- `kb-deletions.yml` records both exact source revisions, SHA-256 hashes,
  localized deletion summaries, the 116/70-page source-index checksum, and the
  zero-backlink result. Production still has both exact source hashes. No
  production page has been edited or deleted.
- Branch `2026-08-09-kb-kvm-review` was pushed at `c62158e`. GitHub Actions runs
  `31350442321` (static check) and `31350442322` (maintained KVM runtime) use
  that exact head. The static check passed. The runtime job remains queued with
  no steps started; repository-runner status is not visible to the available
  GitHub token (HTTP 403). The identical final local runtime command is green.

## Review findings carried into implementation

- Compression must not be disabled categorically; the platform default is
  enabled and general OpenZFS guidance favors lightweight compression.
- The platform default record size is 128 KiB. A smaller value is not a
  universal VM-image optimum and must be justified by workload evidence.
- A separate dataset is an optional administrative and tuning boundary, not a
  prerequisite. It also creates an independent backup/snapshot concern.
- Raw is a defensible simple sparse-image choice, while qcow2 remains useful
  for its image-level features at the cost of another metadata/COW layer.
- KVM and TUN device mappings are current and default-enabled.
- The old Alpine, firewall, bridge, and e1000 material is unsafe or obsolete.
- The current English page diverges materially from the Czech page.

## Compatibility

- Planned repository changes are development/test and documentation-contract
  additions only. They do not change a deployed API, schema, protocol, state
  format, or node configuration.
- The test suite must remain compatible with the revisions pinned in the
  capture repository. Pin updates intentionally become a documentation
  regression signal.
- KB changes are staged and verified against source revisions before an
  approval-gated production promotion. DokuWiki revision history provides the
  content rollback path.

## Open work

- Commit `ac4e4bd Document complete dual-stack KVM networking` is the current
  capture head. A fresh standalone mandatory review of `c9a0f01..ac4e4bd`
  found no blocking, important, or advisory issues and approved the exact-head
  `kb/kvm#networking --fresh` run. The reviewer independently proved that all
  five generated Ruby fixture methods are byte-identical to their sources,
  the pre-suite hashes match, `10#$public_port` survives literal transport,
  and the hash guard runs before cluster provisioning. The residual validation
  gap is the unchanged Base64/stdin transport into the VPS and execution of
  the corrected NAT hook in the maintained VM environment.
- Rerun the exact maintained `kb/kvm#networking --fresh` integration at
  `ac4e4bd`.
- The exact `ac4e4bd` rerun completed in 1,696.3 seconds with five of six
  networking examples green. Both routed families and the primary dual-stack
  NAT HTTP/SSH/outbound example passed. The additional-forward example stopped
  at its first IPv6 UDP echo after the immediately preceding IPv4 UDP echo;
  the parser, invalid-input preservation, EOF, and lifecycle assertions were
  therefore not reached. IPv6 TCP forwarding and IPv4 UDP forwarding had
  already passed, isolating the observed failure to the test appliance's one
  dual-stack socat UDP listener rather than the documented DNAT rule shape.
  Logs are retained at
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b`. Teardown completed normally;
  the retained result is 572 KiB and the filesystem had 456 GiB free.
- The maintained guest now uses separate IPv4 and IPv6 socat sockets on port
  9000. This keeps the intended same-port IPv4/IPv6 forwarding coverage while
  removing cross-family socket behavior from the appliance. `git diff
  --check`, `nix develop -c bin/check` (8/50, 8/18, and 6/16), generated Ruby
  syntax, and the exact `tests.x86_64-linux.\"kb/kvm\"` build passed. The built
  initrd contains both explicit listeners. The amended single commit is
  `8b0ce019d06093867c5d82661c517c78e3ca2a3a`; the capture worktree is clean and
  one commit ahead of its pushed parent. A fresh standalone mandatory review
  found no blocking, important, or advisory issues and approved the exact-head
  rerun. It confirmed that the IPv4 and IPv6-only wildcard sockets can bind the
  same port with pinned socat 1.8.1.3, survive domain recreation, and preserve
  the intended same-port dual-stack UDP contract. The maintained rerun remains.
- The exact `8b0ce01` rerun completed in 1,721.91 seconds with the same five
  examples green and the additional-forward example again failing at its first
  IPv6 UDP echo. The split same-port listener did not change the result, so the
  earlier listener-state hypothesis is rejected. Teardown completed normally;
  retained logs are 568 KiB and the filesystem had 452 GiB free. The run still
  could not reach parser and lifecycle assertions because they shared the same
  example after the traffic probe.
- The maintained design is being hardened before another run: the guest uses
  distinct IPv4/IPv6 UDP ports with explicit listener liveness checks; traffic,
  parser-safety, and lifecycle/reconciliation are separate examples; and a UDP
  failure records client routing, a direct guest probe, VPS routes, IPv4/IPv6
  firewall counters and rules, domain state, and guest/QEMU console logs. This
  keeps diagnosis and downstream validation in the permanent integration test.
  Nix parsing, `git diff --check`, `nix develop -c bin/check` (8/50, 8/18,
  6/16), generated Ruby syntax, exact UDP-command evaluation, and the exact KVM
  derivation build all pass. The networking script now has eight examples and
  the built initrd contains both distinct live-checked listeners. The amended
  clean head is `644d9ee57d3bd2fd06dd24a5a00dfac8c1ca7638`, one commit ahead of
  the pushed parent. A fresh exact-head mandatory review is required before the
  next maintained run.
- Mandatory review of `644d9ee` found one Important test-design issue: parser
  EOF coverage and lifecycle setup still depended on the preceding traffic
  example, and duplicate traffic probes could skip EOF validation if IPv6 UDP
  failed again. The reviewer found no other issue and did not approve a rerun.
- The correction installs a clean pair of UDP rules independently at the start
  of every relevant example, removes duplicate parser traffic probes, and
  separates lifecycle restoration from idempotent update/removal. The final
  removal example explicitly restores the libvirt network and domain before
  resetting its rules. The generated networking script has nine behavior-based
  examples. Nix parsing, `git diff --check`, the full contract suite, exact
  derivation build, generated Ruby syntax, and exact UDP command evaluation all
  pass. The amended clean head is
  `8aafe7e8381b2585cb4742dc672bd68243641cf3`, one commit ahead of the
  pushed parent. Fresh standalone mandatory review found no blocking,
  important, or advisory issues, confirmed the prior state-dependency finding
  is resolved, and approved the exact-head maintained rerun.
- The exact `8aafe7e` maintained run completed in 1,736.38 seconds. The primary
  dual-stack NAT example and all four routed examples passed. The dedicated UDP
  example failed with actionable diagnostics: all 21 IPv6 probes hit both the
  documented DNAT and FORWARD accept rules, but a direct VPS-to-guest IPv6 UDP
  echo also failed. This isolates the remaining traffic failure to the
  synthetic guest echo service, not the documented forwarding rules.
- The independent examples revealed two additional maintained-test defects.
  Parser preservation compared `iptables-save` output whose generated timestamp
  comments can change, and its failed cleanup left the overflowing input record
  in the shared config. Later setup removed only port-5353 records and was
  consequently rejected by the stale overflowing record. All four routed
  examples nevertheless passed. Teardown completed normally; retained logs are
  under `/tmp/os-test-runner/os-test-kb__kvm-1adc155b` and the filesystem had
  448 GiB free.
- The synthetic socat service is being replaced by a small maintained C UDP
  echo binary with explicit IPv4/IPv6 sockets. Parser preservation now compares
  stable `iptables -S` output, and every UDP baseline reset removes all prior
  UDP test records before installing exact valid entries. The C program builds
  with `-Wall -Wextra -Werror`; Nix parsing, `git diff --check`, the contract
  suite (8/50, 8/18, 6/16), exact KVM derivation build, generated Ruby syntax,
  and initrd inspection pass. The clean amended head is
  `2729a8d5bfa9cb64baa7c9d609f52ebf3fcb7c76`, one commit ahead of the
  pushed parent. Fresh standalone mandatory review found no blocking,
  important, or advisory issues, confirmed the C socket/closure behavior and
  parser cleanup boundaries, and approved the exact-head maintained rerun.
- The exact `2729a8d` maintained rerun completed in 2,223.95 seconds. Six of
  nine examples passed: the complete IPv4/IPv6 TCP NAT scenario, parser
  preservation, idempotent updates/removal, routed topology and live-change
  guards, and routed IPv4 traffic. The two IPv6 UDP traffic examples and the
  routed guest's cached IPv6 outbound-source assertion failed. IPv6 DNAT and
  FORWARD counters both recorded all 21 probes, and the direct VPS-to-guest
  IPv6 UDP probe also failed, while IPv6 TCP reached the same guests in both
  network modes. This confines the UDP failure to the synthetic wildcard-bound
  echo appliance or `nc` probe exchange, not the documented libvirt network or
  firewall rule shape. The routed guest accepted inbound IPv6 HTTP and SSH;
  only its one-minute asynchronous `/outbound6` cache was unavailable. The
  retained result is under
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b`. Teardown completed normally,
  the 320 GiB node image remained sparse under `/tmp/os-test-runner` (about
  3 GiB physically allocated during the run), nothing copied it into the Nix
  store, and the filesystem retained at least 430 GiB free.
- The next maintained-test correction will bind each echo socket to the
  configured guest address, use a purpose-built UDP client with explicit
  errors instead of `nc`, retry the guest's outbound-source fetches for the VM
  lifetime, and route outbound assertions through the existing bounded
  domain/network/console diagnostics. Documentation fixtures and network setup
  remain unchanged.
- The first static-tool build attempt used `pkgs.pkgsStatic.runCommandCC`,
  which selected the musl derivation but failed before compilation because
  `cc` was absent from `PATH`. The full `bin/check` suite remained green. The
  tool now uses `pkgs.pkgsStatic.stdenv.mkDerivation` and `$CC`; the reusable
  Nixpkgs lesson is recorded in
  `notes/vpsadmin-kb-captures/2026-08-11-pkgsstatic-runcommandcc.md`.
- The correction is committed as clean head
  `2af630a8f9162dd5657c85e1d09ff8d378f84eed`, still one cohesive commit over
  parent `c9a0f01c6833aeabc4e287dd11f02a6ee022b34f` and one commit ahead of the
  pushed branch. `git diff --check`, Nix parsing, and `nix develop -c
  bin/check` pass (8/50, 8/18, 6/16, inventory 59/118). The exact KVM
  derivation builds as
  `/nix/store/z0w0ymsfiicbyn6i0h8r2kxyffr53dsq-os-test-kb-kvm.json`; its
  generated networking Ruby passes syntax validation. The 44 KiB musl tool is
  statically linked, belongs to the service VM closure, is byte-identical to
  the served VPS asset, and is present in the current guest initrd. Direct
  IPv4 and IPv6 loopback client/server exchanges passed. A fresh standalone
  mandatory review of this exact head is in progress before any further VM
  run.
- Fresh standalone review of `2af630a` found one Blocking documentation defect
  and one Important test inconsistency, so it did not approve a rerun. The
  concise bilingual NAT examples appended their direct `FORWARD` accept rule
  after libvirt's rejecting `LIBVIRT_FWI` path, although the full fixture
  correctly inserts its managed jump first. The EOF-record success assertion
  also remained on netcat and generic retry logic rather than the new
  observable client/diagnostics. Both concise examples now insert their DNAT
  and accept rules at position 1, their networking fingerprints are refreshed,
  and the EOF assertion uses `wait_for_udp_echo` with the static client. No
  finding concerned compatibility, pins, vpsAdminOS, sparse disks, security, or
  commit cohesion.
- The review corrections are committed in clean amended head
  `eb998dd247aafaeb74a47e8cf53b4b48a7f22e60`. `git diff --check`, Nix
  parsing, the full `bin/check` suite (8/50, 8/18, 6/16, inventory 59/118),
  generated networking Ruby syntax, and exact KVM derivation build all pass.
  The corrected exact derivation is
  `/nix/store/qzdz7axpvpf6rr0kbx0vb7gcmxi534in-os-test-kb-kvm.json`. A new
  fresh standalone review is required before the long rerun.
- Fresh standalone follow-up review approved exact head `eb998dd` for
  `./test-runner.sh test --fresh 'kb/kvm#networking'` with no Blocking,
  Important, or Advisory findings. It confirmed both prior findings are fully
  resolved, the single hash-bound commit is cohesive, fixture hashes and pins
  match, and no vpsAdminOS/configuration/sparse-source regression exists. The
  residual gap is execution of the static address-bound UDP exchange and
  lifetime outbound retries in the maintained nested cluster environment.
- The approved exact command `./test-runner.sh test --fresh
  'kb/kvm#networking'` passed at `eb998dd`. All nine examples succeeded:
  complete NAT HTTP/SSH/outbound over IPv4 and IPv6 (14.65 s), additional UDP
  forwards over both families (4.91 s), invalid-record preservation and EOF
  handling (16.48 s), lifecycle restoration (33.82 s), idempotent
  reconciliation/removal (17.62 s), routed topology state (18.92 s), safe
  live-change handling (37.82 s), routed IPv4 traffic/source without NAT
  (19.68 s), and delegated IPv6 inbound/outbound without NAT (5.71 s). The
  networking script was green in 1,366.44 seconds and the complete test,
  including teardown, was green in 1,766.8 seconds.
- The exact-head run removed its sparse machine images during normal teardown;
  retained logs/result occupy 572 KiB under
  `/tmp/os-test-runner/os-test-kb__kvm-1adc155b`. The filesystem recovered to
  438 GiB free. The 320 GiB logical node image was never copied into the Nix
  store and stayed under `/tmp/os-test-runner` throughout the run.
- Branch `2026-08-09-kb-kvm-review` is pushed at exact head `eb998dd`. Static
  GitHub Actions run `31456104982` passed in 5 minutes 55 seconds. Runtime run
  `31456104974`, job `93670094351`, passed at the same head in 25 minutes
  52 seconds. Contract/discovery checks, the maintained runtime tests, result
  evaluation, summary, and cleanup all succeeded. Log upload was intentionally
  skipped because the test was green. No CI failure or rerun occurred.
- User review requested a final operational wording correction: support, not
  the user, assigns the private IPv4 `/32`; additional IPv6 `/64` prefixes are
  already available to users; routed public addresses are not configured on
  any interface inside the VPS; and the IPv4 introduction must not end in a
  misleading colon. Both languages and their networking fingerprints are
  amended in exact head `984d7d00b8c9b90f9547595836fd2fad025136d6`.
  `eb998dd..984d7d0` changes only those two pages and `contract/runtime.yml`;
  the fixture and test tree objects are identical.
- Quick verification at `984d7d0` passes: `git diff --check`, the focused
  runtime contract (2 pages, 5 tests, 5 samples), and `nix develop -c
  bin/check` (8/50, 8/18, 6/16, inventory 59/118). A fresh standalone mandatory
  reviewer found no Blocking, Important, or Advisory issues, independently
  confirmed all requested wording, commit cohesion, unchanged pins and runtime
  behavior, and judged a new long VM run disproportionate. Existing `eb998dd`
  local and CI execution remains valid because the executable/test tree did
  not change. The operational availability of additional `/64` prefixes is a
  user-supplied policy; the integration test covers their routing mechanics.
- Amended capture head `984d7d0` was force-pushed with an exact lease over
  `eb998dd`; no superseded queued or in-progress runs existed. GitHub static
  run `31472977370` passed at the new head in 5 minutes 36 seconds. Runtime run
  `31472977319` was triggered automatically and passed at the same head in
  23 minutes 7 seconds. Contract/test discovery, the maintained tests, result
  evaluation, summary, and cleanup all succeeded; full-log upload was skipped
  because the test was green. No failure or rerun occurred.
- Production was fetched again and remains at the same 116/70-page inventory,
  KVM source revisions, page hashes, deletion hashes, and source-index hash.
  Rebuilt candidates are byte-identical to `984d7d0`: Czech SHA-256
  `de3edb64ae3a6c4d15d815409b0f58b2de59d23d0be7f7fef91d56a13e9fec45`
  and English SHA-256
  `b2a3bdc144b0129710254c7cb4c280066d8d0567400062d7a2f84cc987dc72d3`.
- Staging was reset from the superseded candidates to the current production
  mirror, both corrected manifests were staged and verified, and rendered
  output contains the corrected private-IPv4 and additional-IPv6 wording. The
  two obsolete pages matched their guarded production/staging hashes and had
  zero backlinks before their staging copies were removed again. Production
  remains untouched.
- A fresh read-only production fetch still contains 116 Czech and 70 English
  pages. The guarded KVM source revisions and hashes are unchanged. The
  replacement plan was synchronized with the final reviewed contract pages,
  then `bin/kb-contract-build` produced two changed pages and two media
  objects. The Czech candidate SHA-256 is
  `02a12923f2869c40417313d8bdb4b90806e1b46a439f5d571c06dc167eb45848`;
  the English candidate SHA-256 is
  `8dfcdf13ec7b21e4170a6b060af821115bd7e778c44b0215f3c15b9d25504e68`.
  Both candidates are byte-identical to the committed contract sources.
- The first replacement-plan synchronization used `File.binread`, causing
  Psych to serialize the article bodies as `!binary`; review generation then
  rejected mixed UTF-8/ASCII-8BIT strings. Regenerating from explicit UTF-8
  text fixed it. The reusable lesson is in
  `notes/cross-project/2026-08-11-ruby-yaml-binary-string.md`.
- The global staging container was still owned by this initiative but held the
  superseded KVM candidates, so guarded staging correctly refused to overwrite
  them. It was reset to the current 116/70-page, 224-media production mirror,
  then the final Czech and English manifests were staged and independently
  verified. The rendered pages expose the final virtual-machine networking
  headings and both maintained configuration scripts.
- The refreshed complete-corpus backlink scan still finds zero references to
  `navody:vps:kvm-openrc` or `navody:vps:vpsadminos:libvirt`. Their production
  and post-reset staging hashes matched the deletion guards before their
  staging copies were removed. They are now absent from staging and remain
  unchanged in production. `kb-deletions.yml` records refreshed source-index
  SHA-256 `80bf3afc3ef5f79ef9f001f56baee693a8a8b328bfcde2c95d6b299002aff58c`.
- The initiative plan, state, guarded 116/70-page source/candidate corpus,
  final manifests, and two reusable notes are committed on workspace `master`
  as `Track final KVM documentation release`. YAML/JSON parsing, candidate to
  contract byte comparison, and staging verification pass. A whole-corpus
  `git diff --cached --check` reports whitespace and conflict-marker-looking
  text already present in verbatim production DokuWiki pages; those guarded
  snapshots were intentionally not reformatted.
- Await explicit production approval before promoting either language or
  deleting the two obsolete production pages.

## Generic managed-article follow-up

- The user approved making the repository authoritative for an explicit
  managed subset of KB articles, using per-article runtime CI and three-way
  reconciliation for direct wiki edits.
- The selected GitHub name is `vpsfree-kb-contracts`. Existing GitHub web/Git
  redirects will remain available, while the old repository name must not be
  reused.
- The current capture worktree is clean at `984d7d0`. Upstream `master`
  advanced by one vpsAdminOS consumer-pin commit and will be rebased before the
  follow-up implementation.
- The shared workspace checkout contains unrelated edits and untracked files.
  Only initiative paths and isolated AGENTS project-name hunks will be staged.
- Other initiatives still have linked worktrees backed by
  `repos/vpsadmin-kb-captures.git`; they will not be modified or repaired by
  this initiative. A temporary `repos/vpsfree-kb-contracts.git` symlink will
  provide the new project identity until safe final local cleanup.
- Rebased the capture branch cleanly onto upstream `b670cf0`, including its
  vpsAdminOS `67fcc173` pin. The article registry and generic workflow use the
  same revision; no vpsAdminOS source change is part of this initiative.
- Capture commits `7481685` and `b1a006c` respectively generalize managed
  article contracts and adopt the `vpsfree-kb-contracts` identity. The first
  commit is behavior-focused; the second is the mechanical repository rename
  and deliberately retains the schema-5 capture provenance identifier.
- `nix develop --command bin/check --allow-missing` passes with 39 controls,
  29 paths, 69 annotation bindings, one managed article, five tests, five
  executable samples, and all 59/118 capture variants. The generic article
  checker unit suite passes 8 examples/20 assertions.
- Workspace commit `0c79f59` adds schema-4 managed-article candidate building,
  explicit three-way reconciliation, and compatibility tests. Schemas 1-3 and
  release manifest schema 3 remain unchanged. The focused workspace suite
  passes 25 examples/124 assertions.
- The guarded production corpus reconciles as the explicit KVM bootstrap at
  pre-feature base `origin/master`. Candidate construction produces four
  changed pages and the two existing dataset media updates. Complete-corpus
  navigation validation passes with two routed-address annotations per KVM
  language, including the IPv6 paragraph.
- Current candidate SHA-256 values are Czech authoring guide
  `da86d3e0d33aafa65640604b142cee6b09ac70a4499171041d1f2b7231788cc8`,
  Czech KVM
  `9572b9620482683ffd62d343e20d3e27986dabb53fa2ed68d136c2850fd79636`,
  English authoring guide
  `6f99ad0930c0259d56e6cda6eba164795734237c91266920d6a7ff710a5d2a20`,
  and English KVM
  `c105081b0a21772ebef99ed05529413693ca2bc5ebcbec753560104ecb5d4e97`.
  Both KVM candidates are byte-identical to their canonical article sources.
- Refreshed localized release manifests each contain two pages and one media
  update. Production and staging have not been written during this follow-up.
- Workspace commits `be2e835` and `d13f634` respectively prepare the guarded
  four-page release and update the workspace project identity. The unrelated
  pre-existing `AGENTS.md` session-ownership edit remains uncommitted.
- Exact-head quick verification passes: the workspace contract suite has 25
  examples/124 assertions; all three new Ruby entry points pass syntax checks;
  the capture repository reports 39 controls, 29 paths, 69 annotation
  bindings, one article, five tests, five executable samples, and 118 PNGs;
  its three unit suites pass 50, 18, and 20 assertions. Committed-range
  whitespace checks, both localized manifest parses, complete-corpus
  annotation validation, and byte comparison of both KVM candidates with
  their registered canonical sources also pass.
- A supplemental byte comparison initially referenced the superseded
  pre-registry `articles/...` path and stopped before the remaining checks.
  Repeating it with the registry's `contract/pages/...` source paths passed;
  this was a validation-command correction, not a content change.
- Mandatory change review of workspace range `d1b1344..30b00be` and contract
  range `b670cf0..b1a006c` rejected integration pending two Blocking findings,
  one Important finding, and one Advisory correction. It found that legacy
  release transformations could alter a reconciled or omitted managed page,
  that `testsMeta` coverage was only registry-to-tests rather than
  bidirectional, that movable Git bases and source identity were not retained
  in release artifacts, and that the cleanup note below named the superseded
  vpsAdminOS pin.
- Contract commits `fa690b0` and `289f358` address runtime-test coverage and
  document immutable provenance. The checker now inventories every
  `kb-runtime` tag and `kbArticle` label across all suites and rejects missing,
  unknown, untagged, and cross-suite labels before CI matrix construction.
  Eleven examples/31 assertions pass, including the three negative coverage
  cases requested by review.
- Workspace commit `cca890e` requires full 40-character base OIDs, committed
  registry and canonical sources, blocks every legacy page transformation and
  release-time sample expansion for registered pages, compares reconciled
  candidates exactly with canonical sources, and rejects changed registered
  pages omitted from `managed_articles`. Candidate artifacts now record base
  `b670cf0f780e11c8a92451418710c2811c227cfe`, contract HEAD
  `289f35849d0e5a8dafa36d4a995b80b41a1e9c72`, registry SHA-256
  `edde17892b447100c2c96538d8611965886ed0bfb8a78cbeb81d99ffa0d59021`,
  and both canonical page digests. Generated schema-3 manifests retain and
  validate the same provenance without breaking manifests that do not manage
  repository articles.
- Focused review-fix verification passes: candidate tooling has 29 examples/
  144 assertions and release validation has 27 examples/95 assertions. The
  rebuilt release still contains two pages and one media object per language;
  the KVM candidates retain their previously recorded canonical SHA-256
  values.
- Full post-review verification also passes at workspace `cca890e` and contract
  `289f358`: all Ruby entry points pass syntax checks; the complete contract
  check reports 39 controls, 29 paths, 69 annotation bindings, one article,
  five tests, five samples, and 118 PNGs; its unit suites pass 50, 18, and 31
  assertions. Both candidate articles remain byte-identical to canonical
  sources, complete-corpus annotations pass, both release manifests validate
  through `KbRelease::Manifest`, and committed-range whitespace checks are
  clean. All Mandatory review findings are therefore resolved before
  integration testing.
- GitHub already resolved the repository as `vpsfreecz/vpsfree-kb-contracts`;
  the old name remains a working rename redirect. The canonical bare-repository
  remote now uses `git@github.com:vpsfreecz/vpsfree-kb-contracts.git`, and
  `repos/vpsfree-kb-contracts.git` is a relative compatibility symlink to the
  old bare-directory path for concurrent worktrees. Updating the optional
  GitHub description was refused with HTTP 403 by the available API token, so
  the pre-existing description remains; Git over SSH and all repository links
  work under the new name.
- The reviewed feature branch was force-pushed with an exact lease from remote
  `984d7d0` to `289f358`. Branch Check run `31483626494` passed in 5m45s.
  Managed-article runtime run `31483626542` discovered the KVM matrix entry,
  passed contract/test selection, ran all maintained tests in 41m35s, and
  passed result evaluation, summary, and cleanup. Failure-log upload was
  correctly skipped because the run was green.
- A fresh target worktree fast-forwarded local `master` through upstream
  `b670cf0` and then to feature head `289f358`; the complete local static suite
  passed before `master` was pushed and the temporary integration worktree was
  removed. Master Check run `31487072088` passed. Master managed-article run
  `31487072110` passed discovery and all maintained KVM tests, with the VM test
  step completing in 36m05s; evaluation, summary, and cleanup also passed.
- Workspace `master` through release/provenance commit `3199cdd` was fetched,
  confirmed as a linear 17-commit fast-forward, and pushed without touching
  unrelated working-tree edits.
- Staging was reset to the current 116 Czech/70 English-page and 224-media
  production mirror, then both two-page/one-media manifests were staged and
  independently verified. A fresh complete production fetch has the same
  source-index SHA-256
  `80bf3afc3ef5f79ef9f001f56baee693a8a8b328bfcde2c95d6b299002aff58c`
  and still contains zero exact references to the obsolete Alpine and
  vpsAdminOS/libvirt pages. Both pages matched their guarded hashes in
  production and staging before only their staging copies were deleted again.
  Both release manifests continue to verify; production remains untouched.

## Cleanup

- The contract feature and temporary integration worktrees were removed after
  the fast-forward merge. Local and remote feature branches were retained as
  required; the compatibility bare-repository symlink remains for other active
  initiatives.
- The unconsumed vpsAdminOS worktree remains on the abandoned
  `2026-08-09-kb-kvm-review` branch. It contains uncommitted follow-up source
  resolver experiments, so it was not force-removed or discarded. None of
  those experiments is consumed, pushed, or intended for merge. The contract
  repository instead inherits upstream vpsAdminOS pin `67fcc173` from base
  `b670cf0`; this initiative changes no vpsAdminOS source.
- No temporary VM or ad hoc validation environment is permitted.
- Staging ownership must be released after publication or explicit abandonment.

## Invisible managed-page marker follow-up

- The user selected an invisible marker at the top of the page, immediately
  after the existing `<page>` language mapping. The normal page exposes the
  source through the right-hand toolbar only; the page ID remains plain text.
  The marker carries both the canonical source and automated-test GitHub links.
- Reused verified session `2026-08-09-kb-kvm-review`. Created these project
  worktrees and branches:
  - `dokuwiki-plugin-vpsadmindoc` at
    `worktrees/2026-08-09-kb-kvm-review/dokuwiki-plugin-vpsadmindoc`, branch
    `2026-08-09-kb-kvm-review`, based on `origin/master` `ed92a4d`;
  - `vpsfree-kb-contracts` at
    `worktrees/2026-08-09-kb-kvm-review/vpsfree-kb-contracts`, existing branch
    `2026-08-09-kb-kvm-review` at merged head `289f358`;
  - `vpsfree-cz-configuration` at
    `worktrees/2026-08-09-kb-kvm-review/vpsfree-cz-configuration`, branch
    `2026-08-09-kb-kvm-review`, based on current `origin/master` `6fa4063f`.
- The existing vpsAdminOS worktree and its uncommitted abandoned source-resolver
  experiments remain untouched. The shared workspace's unrelated changes and
  untracked files also remain untouched.
- Creating the configuration worktree ran its active Overcommit checkout hook
  in the ambient shell, which lacked the repository's bundled gems. The
  worktree was nevertheless created cleanly; hook installation and all commit
  operations will run from the repository's Nix development shell.
- Plugin commit `d8d5e8e4c1c38968441daf7d08ab95b434a7f62e` adds strict
  `<kb-managed>` parsing, metadata-only rendering, the localized GitHub page
  tool, and warnings for edit, preview, locked, and source views. Valid marker
  URLs are restricted to HTTPS GitHub blob links and every emitted value is
  escaped. The existing navigation annotation behavior is unchanged.
- `nix develop -c bin/check` passes for the plugin: all PHP files parse, the
  isolated behavior suite passes, and the real nixpkgs DokuWiki parser renders
  a valid marker invisibly while diagnosing an invalid marker. The plugin
  feature branch is pushed because the configuration needs an immutable
  fetchable commit. Its unpacked Nix hash is
  `sha256-BGv1DoCcTysyT5L82uju++OrxBU51DtzoJAp8KtzP4U=`.
- Contract commit `3c02342f3b56bc8f746667823bbd36afb0d5d1dd` replaces both
  visible maintenance notes with top-of-page markers and validates their exact
  registry-derived source/test links and position. The expanded checker suite
  passes 15 examples/43 assertions; the complete static contract check passes
  with 39 controls, 29 paths, 69 annotation bindings, one article, five tests,
  five executable samples, and all 59/118 capture variants.
- Configuration commit `19c688e1c30cb2c4b58ae2ec339b57e88572d257`
  pins the new plugin commit and hash for both aitherdev staging and production
  KB closures. `confctl ls` evaluates both affected targets, and the active
  Overcommit hooks pass Nix formatting from the repository's Nix shell.
- Rebuilt the four-page guarded candidate set and both release manifests from
  committed contract head `3c02342` and unchanged base `b670cf0`. The managed
  KVM candidates are byte-identical to their canonical sources. New candidate
  SHA-256 values are Czech KVM
  `f186a765bc0cc0f24bd4bf1e969dff2436fca7a02fb544fd9945258a99f3e75d`,
  Czech authoring guide
  `7951804ec275f99605b973d430ac1e1b27dce38c8556b1827f5254df060bfd5d`,
  English KVM
  `f53f3b340ed401bf5c4c6bf90fd9185561de09a37c951de60e4e783144942347`,
  and English authoring guide
  `1f213e9bc0b05d4137705f86b9bbf83573f4fbe0e46cf366aad8b73014894fa1`;
  each manifest still contains two pages and one media object.
- The authoring guides now identify managed pages by the **Source on GitHub**
  toolbar entry and the source/test warning in the KB editor. The focused
  candidate tooling suite passes 29 examples/144 assertions, and both generated
  manifests parse with the new contract provenance.
- Live `kb-release verify` still reports the authoring-guide pages from the
  previously staged release, as expected: staging has not yet been reset or
  written during this follow-up. Live verification will be repeated only after
  the reviewed plugin configuration is deployed and the new manifests are
  staged.
- Mandatory fresh-context review of plugin `ed92a4d..d8d5e8e`, contract
  `289f358..9ffe859`, configuration `6fa4063..19c688e`, and workspace
  `b60d1b2..9b5abc7` found no Blocking or Important issues. Its one Advisory
  noted that the contract checker counted only syntactically complete markers,
  allowing a second malformed marker start. The contract commit was amended to
  `3c02342` to count every `<kb-managed` tag start and add a regression. The
  focused suite now passes 15 examples/43 assertions and the complete contract
  and candidate-tool suites pass after regeneration. The reviewer independently
  confirmed the plugin archive hash, deployment pins, candidate/source equality,
  manifest provenance, hook API, escaping, and requested behavior. Remaining
  validation is the two full closures, exact-head CI, and deployed staging UI.
- Both full configuration builds pass. Aitherdev staging built generation
  `2026-08-11--16-01-17`, including the new plugin and both localized DokuWiki
  closures. The production KB container built generation
  `2026-08-11--16-05-08`. Neither generation was deployed.
- The first configuration feature-branch push was rejected by the mandatory
  pre-push hook because the ambient shell lacked the bundled Overcommit gems.
  Repeating it with `nix develop -c git push` ran the hook in the supported
  environment and succeeded; no hook was bypassed.
- Fresh integration worktrees fast-forwarded and pushed plugin `master` to
  `d8d5e8e` after `nix develop -c bin/check`, then configuration `master` to
  `19c688e` after both affected targets evaluated through `confctl ls`. The
  temporary integration worktrees and their generated `.bin`/`.bundle`
  directories were removed; the feature branches remain.
- Contract feature head `3c02342` is pushed. Exact-head GitHub Actions static
  run `31499807836` passed in 5m36s. Managed runtime run `31499807880` selected
  the KVM article correctly and is waiting for the maintained VM job to finish
  before the contract can be fast-forwarded to `master`. After 30 minutes the
  job API still reports `queued`, no `runner_name`, and the `self-hosted` label;
  there is no execution log or artifact to investigate. The available token
  cannot inspect organization runner availability. No duplicate rerun was
  started.
- The operator deployed aitherdev. The queued exact-head runtime job then ran
  on `gh-runner1.int.vpsadminos.org` and passed all five maintained KVM
  scenarios in 31m54s; contract discovery, exact test preview, result
  evaluation, summary, and cleanup also passed. The full-log artifact step was
  skipped because the tests succeeded.
- The first post-deployment render exposed the on-demand staging container's
  retained old DokuWiki closure: it rendered `<kb-managed>` as raw text even
  though the aitherdev host had been switched. `bin/kb-stage stop` followed by
  `bin/kb-stage start` retained this session's ownership and data while loading
  the new closure. Staging was then reset to the guarded production mirror and
  both manifests were staged again, ensuring the plugin was active before the
  marker pages were saved.
- Both staged releases verify after the restart and restage. Live anonymous and
  authenticated HTML checks in Czech and English confirm that normal article
  content contains neither the raw marker nor the test URL; authenticated page
  tools are ordered Edit, Source on GitHub, Old revisions, Backlinks, and Top.
  The editor displays the localized repository-managed warning with canonical
  source and automated-test links. The authoring guides and media objects are
  covered by the checksummed release verification.
- A fresh integration worktree fast-forwarded contract `master` to exact tested
  head `3c02342` after the complete `nix develop -c bin/check --allow-missing`
  suite passed again. The integration worktree was removed and the feature
  branch retained. Pushing `master` started static run `31510515984` and runtime
  run `31510515817` automatically for the same already-tested SHA; they are not
  superseded runs and were therefore not cancelled. Production KB content is
  untouched. The production KB container must load configuration `19c688e`
  before the separately approval-gated manifest promotion.

## Managed-page editing guidance follow-up

- Reused verified session `2026-08-09-kb-kvm-review`. Plugin and configuration
  feature worktrees started at their merged `master` heads `d8d5e8e` and
  `19c688e`.
- The repository identity is not hardcoded in the plugin: source and test URLs
  remain validated marker values derived from `contract/articles.yml`. The new
  editing-guide link uses localized local page IDs, preserving the current
  staging or production wiki host.
- The agreed notice permits direct editing but states that manual KB edits are
  not verified. Source, test, and editing-guide notice links, plus the toolbar
  source link, open in a new tab. The Edit action remains unchanged.
- Updated and pushed `dokuwiki-plugin-vpsadmindoc` feature commit
  `8ba88976e3ee0ceb1becd5ef21f007dcb02d9d82`; its unpacked Nix hash is
  `sha256-lIO9q4Mwqezzpr28hEIcsQExgDJZ9TbeOP9IqBT5HoU=`. `nix develop -c
  bin/check` passed, including syntax checks, unit checks, and the real
  DokuWiki integration test.
- Pinned that plugin revision and hash for both `aitherdev` staging and the
  production KB container. `nix develop -c confctl ls` evaluated
  `cz.vpsfree/machines/aitherdev` and `cz.vpsfree/containers/int.kb`; scoped
  `git diff --check` also passed. Configuration feature commit
  `c29a3c34` passed its Nixfmt pre-commit hook.
- Rebuilt the four-page candidate set and both manifests. The KVM candidates
  remain byte-identical to the contract sources. Only the two authoring guides
  changed: Czech SHA-256
  `dc830b84053d6afb89430f6f12f7e12386cb8278ff519c648075f2149483cf21`
  and English SHA-256
  `39522f21c7eb8275d4da8b798adcd1ed79c3707de39c3020b2818a890fe57047`.
  `ruby -Itest test/kb_contract_tools_test.rb` passed with 29 runs and 144
  assertions, both manifests parsed, and scoped `git diff --check` passed.
