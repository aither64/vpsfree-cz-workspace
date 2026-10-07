# Configuration Nix tools shell needs the checkout cwd

Enter `nix develop` with the shell working directory set to the configuration
checkout. Selecting its flake by an absolute path from the coordination root
can fail with `mkConfigDevShell mode tools requires ./Gemfile`: the tools shell
loads the Gemfile relative to cwd.

For worktree creation, enter an existing configuration checkout's shell first,
then invoke `dev-session worktree add`. The command selects the coordination
workspace separately. Continue subsequent hooks, confctl pinning and builds
from the new owned configuration checkout.
