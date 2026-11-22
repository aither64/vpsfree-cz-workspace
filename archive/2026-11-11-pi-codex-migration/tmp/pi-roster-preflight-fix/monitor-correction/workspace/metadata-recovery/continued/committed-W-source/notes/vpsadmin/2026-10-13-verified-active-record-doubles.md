# Verified doubles for ActiveRecord columns

A strict instance double can reject a real database column reader before
ActiveRecord has generated its attribute methods. An example that passes after
another example creates a model may fail when randomized first in its group.

API run38310941934 exposed this in the release-mail rendering example: core
seed27800 rejected `IpReleaseCampaign#deadline`, while the full-mode example
passed after earlier campaign examples. Native JSON and source confirmed the
real columns and preserved the original failure; no local reproduction ran.

Initialize the relevant model's attribute methods in the owning example before
constructing verified doubles. Keep strict doubles and assertions; avoid a
global workaround or weakening method validation. Corrected-source API38364190560 passed that exact example in both native
modes at59097cb4. The required API matrix still failed a different address-fixture
setup, so that run remains failed; it is not all-pass branch acceptance.

After a dependency rebase, ordinary hooks may also encounter an ignored stale
component Gemfile.lock/cache. Refresh it through that component's documented
Nix shell and Bundler setup, then repeat the normal hook. Do not bypass it or
commit the ignored lock merely to repair a local development environment.

Evidence: `work/2026-10-05-network-ipv4-left-counter/finish-final-target-api8-artifacts/`
and `finish-api-render9-committed-proof.json` in the same initiative.
