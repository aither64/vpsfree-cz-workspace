# Local test-runner verification environment

In `work/2026-11-03-redhat-image-releases`, focused runner specs initially
loaded no examples because `nix develop .#test-runner` did not provide
`libosctl/native`. Use the existing native extension built for the shell's
Ruby ABI. Set its `RUBYLIB` with `nix develop .#test-runner --command env
RUBYLIB=... bundle exec ...`; an outer `RUBYLIB` assignment is replaced by the
shell hook. The exact tested dependency and commands are in the session's
`metadata-result.md`. The corrected environment passed 42 focused examples.

The native `test-json-runner <json> <state-dir>` entrypoint can reuse a cached
VM configuration without Nix builds. At the investigated revision it does not
forward the JSON resource requirements into `Test.new`, so its scheduler sees
zero resources. A diagnostic invocation needs an immediate native
`ResourcePool.can_reserve?` check using `TestResources.from_h` on the preserved
JSON requirements. Wait when capacity or reserves do not fit; do not rely on
an oversized-test fallback. Keep source/kernel/input paths, diagnostic changes,
runner ownership and cleanup evidence in the owning session. No entrypoint
resource-propagation fix was included in the source-identity change.

A retained image-test JSON does not necessarily root its shared source tree.
The image template's environment-derived source path is a string without a
Nix reference edge in that JSON. In the cached diagnostic, on-pressure GC
collected the original source while the VM was booting; the later guest mount
then lacked the required source directories. Retaining the JSON symlink rooted
kernel/system inputs but not this source. Use the normal runner invocation to
hold `RepositorySource`'s GC root across the whole batch, or retain all exact
shared-source roots explicitly before any separately authorized cached reuse.
The normal command's source lifetime spans synchronous prebuild and executor
execution; the cached failure did not require weakening checkout validation.

A live temporary CI watch does not establish an idle-lead wake-up. For an
asynchronous handoff, this session used an existing retained member to own the
check package, keep its turn active while a fresh utility observes, and explicitly
call authenticated `report_to_lead` on the outcome. The installed runtime source
routes that report to `turn/start` for an idle lead (cold recovery queues then
activates). Readiness receipts into an active lead prove active delivery only;
source contract and actual owner/observer readiness were verified before yield.
Do not rely on passive utility completion or manufacture a reporting identity.
See the session's reporting-contract-checkpoint.md and ci-managed-result.md.
