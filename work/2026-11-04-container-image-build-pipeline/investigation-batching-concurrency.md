# I4: batching, builder reuse and concurrency

Investigation only, 2026-11-05, implementer0. Previous I0 accepted/complete;
capacity confirmed. Session/current and both environment bindings matched.
Canonical bare source: `repos/vpsadminos.git`, explicit immutable SHA
`2951a632c4254a44747a8da326e3dde897eaa0e2` throughout. All file:line citations
refer to that revision. Current production remains unverified. Workspace
guidance and repository AGENTS were read; documentation/handoff skills reused.
Only this evidence file was written; no code edits, builds, tests, CI, hosts,
fetch/push, branches/worktrees or commits.

## Settled result

One fresh VM per batch, serial image operations, `jobs=1`, failed-container
retention off, and one repository writer is the smallest safe first option.
It already reuses builders across separate CLI calls. Per-image VMs repeat
boot and builder setup; separate processes inside one VM do not require that
repetition, but concurrent processes lack a shared test-IP allocator and
builder lifecycle coordination.

## Builder lifecycle and reuse

- `os/modules/services/osctl/image-repository/build.rb:130-176` loops images
  sequentially, spawning `osctl-image deploy` for each image/variant with the
  same build dataset, output cache and repository. `:268-275` waits for each
  child. This is one CLI process per image, not one VM per image.
- Builder CT ID is `builder-<first 8 hex characters of SHA2(builder name)>`
  (`osctl-image/lib/osctl/image/builder.rb:35-38`). It does not encode image,
  source/config revision, batch, process or output directory.
- `operations/builder/use_or_create.rb:22-31` finds that CT, starts/reuses it
  and waits for network; otherwise it creates it. Existing builders do not
  rerun setup or validate their configuration against current scripts.
- `operations/builder/create.rb:30-37,56-97` imports the bootstrap image,
  sets nesting/networking, starts it, mounts inputs and runs builder setup.
  Setup failure deletes the CT (`:107-115`).
- `operations/image/build.rb:88-95,230-268` always cleans per-build mounts,
  work/output datasets and copied source. It does **not** stop/delete the
  reusable builder CT. Consequently later images using the same builder
  reuse its prepared root/package installation even in separate CLI calls.
  Builder destruction is explicit `osctl-image ct del`
  (`cli/containers.rb:46-62`) or VM/pool teardown, rather than per-image
  success cleanup.
- Work/download datasets are per build and destroyed; package installations
  in builder root persist. Thus setup is reused, but the per-image download
  directory is not a lasting download cache (`build.rb:67-70,255-266`;
  `image-scripts/bin/runner:102-104,124`). Archive reuse is separate:
  `Build#cached?` checks file existence only (`build.rb:107-109`). Keep cache
  scoped to the known source/input batch; it is not provenance validation.

## Test IP lifetime and scope

`cli/image.rb:193-214` constructs a fresh `IpAllocator('10.100.10.0/24')`
for each `test_images` method call. This is even narrower than CLI-process
lifetime: deploy invokes that method separately per successful image
(`:120-128`). `operations/test/image.rb:30-41` iterates tests sequentially.

`ip_allocator.rb:7-32` keeps available/taken addresses in Ruby memory and
protects them with a Ruby `Mutex`. There is no cross-process allocation file,
daemon reservation or pool/network namespace in this allocator. Each fresh
instance takes the first available address, independently of other instances.

`operations/test/run.rb:72-90` obtains the address immediately before the
test script, exports `OSCTL_IMAGE_TEST_IPV4_ADDRESS`, then returns it in an
ensure **before** container cleanup. `image-scripts/tests/veth_routed.sh:1-8`
assigns it as a routed /32 and starts the test container. Overlapping calls
can therefore assign the same routed IP to different CTs on the same host.
Random test CT IDs (`run.rb:103-104`) do not prevent this.

The allocator is not used for builder networking: builder creation adds an
ordinary bridged `eth0` on `lxcbr0` (`builder/create.rb:59-65`). The fixed
test-address issue is specifically visible in routed tests.

**Retention caveat:** `run.rb:93-99` keeps failed CTs when `keep_failed` is
true, but their IP has already been returned. A retained failed CT can still
have its routed address/networking. Even sequential later CLI calls reset
the allocator and can conflict with it. Initial batching must disable
`--keep-failed`/`keepAllFailedTests`/per-image retention, or explicitly stop
and remove retained networking before proceeding. Serial execution with
ordinary cleanup avoids overlapping address users; it is not unconditional
when failed CT retention is enabled.

## Other concrete collision boundaries

| Boundary | Evidence and implication |
| --- | --- |
| First use of the same builder | `use_or_create.rb:25-30` is a find-then-create sequence without a builder lock. Concurrent first uses can both try the deterministic ID. A failing `Create` finds/deletes that ID (`create.rb:107-112`), so handling the losing creation is not independent of the other call. |
| Shared builder root | Subsequent builds share its container/package state. Per-build mount paths use random IDs (`build.rb:271-284`), and `image-scripts/bin/runner:57-68,155-157` creates a private mount namespace, reducing mount leakage. These do not isolate arbitrary build-script writes to builder root or package-manager state. Do not claim unrestricted same-builder parallel safety. |
| Build datasets | `build.rb:67-70` chooses a random 4-byte hex suffix below the supplied parent; normal calls use separate child work/output datasets and clean only those children. The parent need not be duplicated for serial batching. This is randomized separation, not reservation/locking or a guaranteed unique namespace. |
| Export files | `build.rb:74-83` names outputs only by distribution/version/arch/vendor/variant. `operations/image/export.rb:43-59` opens final filenames for writing directly. Parallel builds of the same tuple/output directory can truncate/overwrite or expose a partial file to existence-based cache checks. Give workers separate output directories even when their temporary datasets differ. |
| Repository index/tags/defaults | `operations/repository/add_image.rb:35-50` calls local repository add. `osctl-repo/lib/osctl/repo/local/repository.rb:24-60` copies payloads, changes tag symlinks and saves the index; `local/index.rb:8-18,70-75` loads a private snapshot then writes it. There is no transaction lock around this read/modify/write path. Parallel distinct-image additions can lose index updates; same tuples/tags add payload/symlink races. Serialize adds/defaults/GC/publication. |
| Pool selection | `osctld_client.rb:38-40,52-77` submits CT lookup/create/import without a pool argument; image CLI flags expose no worker pool selector (`cli/app.rb:22-26,45-81,105-132`). Merely providing separate datasets does not select separate CT pools. Per-worker pool binding requires explicit changes through Ruby client and shell-test commands, not just configuration of a new dataset. |

## Minimal execution options

1. **First slice: existing serial coordinator in one fresh VM.** Keep its
   subprocess loop, reuse builders, fresh source-scoped archive/cache/output
   roots, `jobs=1`, retention off and serial repository mutation. Retain the
   tested output files outside guest teardown as in I0. No allocator change
   is needed while one test runs at a time and cleanup succeeds; stop or
   diagnose incomplete cleanup before the next call. Builders stay warm for
   the batch and disappear with the fresh job guest. No performance campaign
   is needed to establish these mechanisms.
2. **Build parallel, test serial:** a CLI mechanism already exists:
   `build/deploy --jobs N` (`cli/app.rb:57-58,120-121`), with threaded builds
   (`cli/image.rb:152-175`, `operations/execution/parallel.rb:29-35,46-72`)
   followed by sequential tests/deploy (`cli/image.rb:120-146`). It does not
   fix first-use builder races or shared mutable builder state. Before
   enabling it for a full batch, precreate/serialize builders and schedule
   at most one build per builder, or add builder ownership/locking. Keep
   tuples/output paths distinct and all tests/repository writes serial.
   Current build.rb launches one image at a time, so it needs a bounded
   scheduling change to exploit such concurrency across images.
3. **Parallel tests in one VM:** would need a shared allocation mechanism
   or explicitly disjoint configurable per-worker test CIDRs, with release
   tied to actual CT/network cleanup and retained-failure handling. CIDRs
   alone do not resolve builder IDs, shared builder roots, output files or
   repository writers. Per-worker pools alone do not isolate host routed IPs;
   both pool binding and network/address isolation need design changes.
4. **Later bounded worker VMs:** keep serial batching inside each worker,
   separate state/disks/output/host ports and a single aggregation/publication
   writer. VM networking isolates identical internal test subnets and builder
   IDs. This avoids changing allocator internals; it repeats setup once per
   worker, rather than once per image. Capacity and runtime behavior remain
   unmeasured and are outside this investigation.

These are source-derived mechanisms and proposals, not runtime verification.
No current production behavior or performance benefit is claimed. Findings
were sent directly to architect0 and lead; next dependency is their design
synthesis and package acceptance.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
