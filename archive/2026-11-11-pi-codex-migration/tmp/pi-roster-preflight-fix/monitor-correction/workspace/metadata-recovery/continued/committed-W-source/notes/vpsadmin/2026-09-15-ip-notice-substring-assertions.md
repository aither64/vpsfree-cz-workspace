# Compare complete addresses in notification specs

The IP release API Specs core-engine job failed with seed 24922 even though the
mail correctly excluded an ineligible address. `not_to include('192.0.2.20')`
also matches an eligible `192.0.2.200/32` or `192.0.2.204/32`.

The fixture helper generates addresses from `IpAddress.maximum(:id)`. RSpec
database rollbacks remove rows without resetting auto-increment IDs, so this
collision depends on preceding examples and can disappear in a focused rerun.

Reproduce with explicit overlapping IP strings, then assert the rendered
address plus prefix (`192.0.2.20/32`). Both the initial-notice and reminder
examples failed deterministically with the old assertions. Retain those
fixtures as the regression coverage; do not rerun CI blindly or change
production filtering to satisfy a bare-substring assertion.

After the assertion fix, the complete core-engine suite passed with the failed
CI seed: `VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec
spec/models --seed 24922` (912 examples, zero failures, 50 existing pending).

Related initiative: `work/2026-09-09-ip-release-mechanism/ci-investigation.md`.
