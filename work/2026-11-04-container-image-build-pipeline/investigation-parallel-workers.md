# I5: parallel workers and streaming results

2026-11-05, implementer0; investigation/proposal only. I0–I4 accepted;
capacity confirmed; session/current and environment bindings match. Workspace
guidance hashes unchanged from I4; reused full reads and documentation/handoff
skills, reread repository AGENTS. Source: canonical bare `repos/vpsadminos.git`,
fixed `2951a632c4254a44747a8da326e3dde897eaa0e2`; citations below are at that
SHA. Uses [I4](investigation-batching-concurrency.md), without retracing it.
Only this file written; no code changes, runtime checks, Git mutations or hosts.
User reports latest run 04:00–22:00 (18h), some nearly 24h; unverified here.
Useful parallelism is now required for first release; I4's serial-only initial
recommendation is superseded, while its collision evidence remains applicable.

## Current phase barrier: confirmed

`osctl-image/lib/osctl/image/cli/image.rb:97-100` finishes `build_images`
before testing. That method calls `Parallel#execute` at `:174`;
`operations/execution/parallel.rb:29-35,80-81` joins **every** build thread.
Then `cli/image.rb:120-131` tests every successful image before `:142-146`
deploys **any** image. Thus quick results wait for the slowest build and then
for other tests. Adding `--jobs` alone cannot provide early tested results.
The repository coordinator `os/modules/services/osctl/image-repository/build.rb`
`:133-176,268-275` instead finishes one image subprocess before the next;
neither existing mode supplies independent streaming image pipelines.

## One VM with worker namespaces: feasible, additional source changes

One serial build→test→result pipeline per worker could share the VM if these
boundaries are introduced together, rather than only increasing `--jobs`:

- Add a stable worker namespace to `Builder`'s CT ID calculation
  (`osctl-image/lib/osctl/image/builder.rb:35-38`) and propagate it from CLI
  through build options to `operations/image/build.rb:64`. One process at a
  time owns each worker's builder; other workers get separate builder roots.
- Make `cli/image.rb:197`'s fixed test CIDR configurable per worker, with
  explicitly disjoint subnets that avoid guest bridge/uplink ranges. Existing
  `image-scripts/tests/{veth_routed,ssh_key,ssh_password,nixos_rebuild}.sh`
  read `OSCTL_IMAGE_TEST_IPV4_ADDRESS` (`:1` or nixos_rebuild `:6`), so these
  scripts do not require hardcoded-address rewrites. CT identity is passed
  into `image-scripts/bin/test:49-52`; random test CT IDs already exist
  (`operations/test/run.rb:103-104`). Prefixing them is useful for ownership.
- Give each worker its own build-parent dataset, output/cache/log directories;
  pass existing CLI flags. Serialize the common repository writer, tags,
  defaults and GC; workers report successful files, not concurrent repo writes.
- Carry worker settings through every per-image invocation. Keep failed CT
  retention off or reconcile its network before continuing: I4's IP return
  before optional preservation remains relevant within each worker.

Remaining common state: osctld/default pool, guest kernel/ZFS, guest Nix store,
bridge/DHCP and guest-wide resources/failure domain. `lxcbr0` is fixed in
builder creation (`operations/builder/create.rb:59`) and bridge tests
(`image-scripts/tests/veth_bridge.sh:13`); that test discovers its address
(`:6`), rather than imposing a second fixed test IP. Console scratch files use
`mktemp -d` (`tests/console_login.sh:1-3`); builder control-script filenames use
random suffixes (`operations/builder/controlled_runscript.rb:66-83`). No
additional fixed CT/network identity blocker was found in this bounded scan.
Exact search for `10.100.10` under image-scripts/osctl-image/os modules/configs
found only this allocator and specs, not a second subnet-specific runtime rule.
This is feasibility evidence, not proof that arbitrary scripts cannot mutate
guest-wide state. No per-worker pool feature is required for this option.

## Bounded batch worker VMs: smaller production-code surface

Prefer a configurable, bounded number of run-lived VM workers, each owning
one image pipeline at a time and reusing its builders for subsequent images.
VM boundaries isolate existing builder IDs and fixed internal test subnets,
avoiding new worker/CIDR options throughout osctl-image. Source seams:

- `os/modules/services/misc/build-vpsadminos-container-image-repository/shared.nix`
  `:17-55` constructs machine config and output/source shares; `:63,73-81`
  scopes state and creates a persistent machine; `:83-110` starts once,
  executes guest commands and stops at the end. Replace the single command
  `:99-102` with one owner command loop per worker. Distinct machine/state/
  disk/cache/log/output paths and disabled or unique host forwarding are
  mandatory; do not share worker repository mounts as writers.
- Use a small parent dispatcher with a bounded work queue and one serialized
  result/repository writer. Each available VM receives the next image, runs
  build plus tests, exposes its exact successful files/metadata, and immediately
  returns that outcome before taking more work. Existing `osctl-image test`
  produces archives and exits nonzero on failed tests (`cli/image.rb:60-67`);
  parent ingestion can use those files without a second build. Do not call
  the entire repository `build.rb` per dispatched image: it also performs
  defaults/GC/postBuild at run end (`:71-88`).
- Start known long images early; dynamic assignment prevents a fixed shard
  from stranding other workers. Builder affinity is optional and must not
  withhold available work. Successful quick images reach validation/ingestion
  while Guix/Gentoo continue; final run inventory still records all outcomes.

The dispatcher/result-writer change is needed for either design. Worker VMs
also need module options/lifecycle wiring but leave image-builder identity and
IP APIs unchanged; one-VM workers save guest overhead at the cost of those
additional API changes and a shared failure domain. Recommend VM workers for
the first release, with measured/tunable count >1 under sufficient capacity,
per-image streaming acceptance and isolated worker cleanup. No speedup or
particular count is proven without authorized measurement. Production remains
unverified; optional performance/hardening investigation stops here.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
