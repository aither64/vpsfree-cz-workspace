# Exercise the public Rake dispatcher

Tasks.run uses ActiveSupport classify, which singularizes its argument. An
internal task class ending in Bounds was looked up as Bound and failed with
NameError; tests constructing the class directly missed it. A task class/key
ending in BoundsRepair works with the existing dispatcher.

Test the public Rake task using the existing isolated Rake/environment helpers,
including preview, apply and idempotent rerun. The packaged VM scenario can use
the bundle exec rake pattern in tests/suite/tasks/common.nix. Standalone local
Rake commands also need a configured DB; RSpec automatically supplies one.
The kernel-history public-entrypoint regression passes.

Related initiative: work/2026-09-14-kernel-history-fix.
