# Use absolute maintenance spec paths in the API shell

Related initiative: `work/2026-09-09-ip-accounting-review`.

Running `nix develop .#api -c bundle exec rspec ../vpsfree-maintenance-tasks/...`
from the vpsAdmin root fails to load the external spec. The API development
shell changes directory to `api/`, so the relative path resolves inside the
vpsAdmin repository. Pass an absolute spec path and set
`VPSADMIN_API_SPEC_HELPER` to the absolute `api/spec/spec_helper.rb` path before
entering the shell. This preserves the maintenance task in its own repository
while using vpsAdmin's disposable database and fixtures.

Also run the command from the vpsAdmin root, not by referring to its flake
from the coordination workspace. The shell hook otherwise looks for a Gemfile
in the workspace and can create a `.gems` cache there. Both the absolute-path
spec run and a separate runtime smoke probe passed after using the correct
working directory.
