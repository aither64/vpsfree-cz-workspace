# OSVM specs need the local libosctl native extension

Running the OSVM RSpec suite in nix develop initially failed loading libosctl/native.
From the repository root, run nix develop, then bundle install and bundle exec
rake compile in libosctl, followed by bundle install and bundle exec rspec in osvm.
This matches .github/workflows/scripts/run-rspec-all.sh. Compilation creates
ignored native outputs and an untracked libosctl/tmp build tree; do not commit it.
The full OSVM suite then passed (111 examples for the persistence change).

Overcommit push also required re-signing the verified .overcommit.yml in the Nix
environment, then running git push from that same environment; no hook was bypassed.
Related initiative: work/2026-09-11-devcluster-packaging-investigation.
