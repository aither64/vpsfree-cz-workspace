# Prepared post-review verification; not released or launched

Owner implementer0. Preparation snapshot: vpsAdmin
`70a2ed54b98d0c2f359a9cc4484452a257a9807b`, clean index/worktree.
`postreview-preparation-inputs.json` records effective development lock and
packaged-lock/gemset/Composer/flake hashes. Source review and the R1 source remedy
decision remain pending. This file authorizes no command execution. Wait for the
lead's explicit post-review release and recheck the exact released head/locks.

## Proposed bounded sequence

1. Packaged services and native dependency proof. Run the repository's required
   `./test-runner.sh test --jobs 1 --state-dir "$receipt_tmp/services" services-up`.
   Existing assertions cover API startup, shared JSON schema/protocol/client docs,
   actual Go/Rust tabs/public action examples, PHP public entrypoints and JS
   assets, and console-router proxy/direct assets. One services VM declares
   8192MiB RAM/eight vCPUs; it also starts the configured mailer container.
   Do not replace this mandatory packaged test with local Ruby specs.

   Build/reuse the exact packaged API output from the same graph, then run its
   `ruby-env-wrapped/bin/ruby` to require Fiddle, HaveAPI, HaveAPI client and both
   Go/Rust documentation adapters. Assert all four HaveAPI versions0.30.2,
   Fiddle load and libffi linkage, record loaded source paths and hashes, and
   verify packaged shared doc/template/highlighting files. The exact derivation
   expression is:

   ```nix
   let
     f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin";
     pkgs = import f.inputs.nixpkgs {
       system = "x86_64-linux";
       overlays = [ f.overlays.default ];
     };
   in pkgs.vpsadmin-api
   ```

   Use `nix build --no-link --json --impure --expr <expression>` after release.
   Retain the resulting store output/derivation and recursive input graph. This
   is a host-side load of the same packaged closure; actual application mount
   and served asset/example proof comes from services-up. No repository test
   edit or ad hoc change to a VM's source is proposed.

2. Affected API checks in both modes. Use the current API workflow's actual
   `foundation`, `auth` and `platform-config` patterns, sort/deduplicate each
   manifest, and run each topic with:

   ```sh
   env VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec <manifest-files> --format documentation --format json --out <full-topic.json>
   env VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec <manifest-files> --format documentation --format json --out <core-topic.json>
   ```

   Commands are prepared for six sequential topic processes, each with its own
   disposable MariaDB identity. These are targeted full/core checks, not a claim
   that all13 CI topics ran. Retain normal pending/generator filters. B2 owns
   the `documentation_clients_spec.rb` actual-page/authorization/locale work;
   either schedule this platform-config topic after B2 completes, or consume
   B2's exact-head matching full/core native results for that file and explicitly
   partition the remaining manifest. No silent exclusion or duplicate coverage
   claim. Lead selects this scheduling before launch.

   Serialize API shell setup and prevent overlapping RSpec processes against
   the same automatic database. Capture the effective ignored api/Gemfile.lock
   before/after each mode (not just packages/api/Gemfile.lock), Ruby/Bundler/RSpec
   versions, manifests, native result JSON and exit status. Stop if setup would
   unexpectedly change source or effective dependency resolution.

3. Legacy consumer regression on disposable test clusters, sequentially:

   ```sh
   ./test-runner.sh test --jobs 1 --state-dir "$receipt_tmp/console" console-router
   ./test-runner.sh test --jobs 1 --state-dir "$receipt_tmp/browser-auth" 'webui#auth'
   ./test-runner.sh test --jobs 1 --state-dir "$receipt_tmp/browser-console" 'webui#vps-user-ops'
   ```

   console-router exercises a real VPS console login and command via the
   packaged client/router; auth covers actual PHP/OAuth/session/locale browser
   behavior. vps-user-ops is the existing actual console-sidebar/API browser
   script and also includes its prerequisite clone/swap/delete test. Do not
   mislabel curl-only console coverage as browser JS coverage. Retain Playwright
   console/network failures, native report, trace/screenshots and test status.

   console-router: services8GiB/eight vCPUs + node8GiB/four vCPUs.
   webui auth starts services+node1 (same16GiB/12vCPUs); its test graph includes
   node2 even when not started. vps-user-ops prepares the cross-location fixture
   and starts node2: peak24GiB/16vCPUs, plus host/Nix build overhead and sparse
   20GiB disks per node. Have KVM and adequate /dev/shm/disk capacity. Schedule
   one cluster scenario at a time, with runner resource limits agreed with lead.
   Keep the test-defined user/socket networks; this is not a devcluster network
   selection or physical-machine deployment/reservation.

The conservative integration CI selector maps these dependency/package/flake
changes to the complete `tag=ci` suite. This bounded local sequence does not
claim that the entire selected CI suite ran. Publication and any later CI scope
remain lead-owned. No CI, push or default-branch operation is proposed now.

## Resource and ownership coordination

Use a fresh pinned catalog verification_watcher (gpt-6-luna/low; utility
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`) per long/uncertain related
batch, with explicit danger-full-access and approval never. Each owns its
operation handle and complete local log/status files. No reuse of completed
utilities, duplicate launch, source edits, diagnosis/retry or deployment by a
watcher. Parent diagnoses failures; lead decides affected retry/review needs.

B2's uninstrumented/instrumented R1 timing needs a quiet same-host interval:
do not overlap Nix compilation, VM boot/browser tests or API suites with those
measurements. Separate test state/DB names are necessary but do not remove CPU
contention. Launch only after lead allocates the released operation/time slot.

At execution, create a uniquely owned `$receipt_tmp` under /tmp for runner
state/disks and retain compact logs/receipts under this session. Record all
paths and native ownership. Stop/release owned guests/runners through native
controls when finished; no session lifecycle/other-session cleanup is allowed.

## Revision, input and failure receipts

Capture exact final head/tree, clean status, complete flake.lock and source graph,
HaveAPI registry identities and effective development/package dependency locks.
Pinned vpsadminos is8e44a5124439b1f3048ffc56b1717614a5360358; followed nixpkgs is
`a9e6d84f9c2f9012f5fe7d964a7851352300e61a`. Resolve fresh immutable source paths
and every test/package derivation only after release; retain recursive derivation
inputs plus built system/profile and Ruby/gem paths, native logs/status/result
files, and source/hash/version observations. Bind each result to its own exact
head, plugin mode and environment; no validation transfer solely by version.

Unexpected local Linux kernel build: watcher promptly stops the exact owned
command and reports derivation/cache evidence, active children and cancellation
status. Parent reconciles effects and investigates missing cache/runner outputs;
no silent local kernel build or retry. Resource contention waits are not failure.
An ordinary failed check retains logs/artifacts and root-cause evidence before
rerun. A quiet process alone is not canceled; no arbitrary silence timeout.

This preparation launched no shell setup, Nix evaluation/build, test-runner,
RSpec, browser, VM, API GET, provider, remote/default or deployment command.
