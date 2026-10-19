# Preparation hook dependency refusal

The recovered preparation unit exited 75 before activation or new jobs.
Protocol checks passed; Git created the retained detached configuration checkout
at fbbda8e9, then the active post-checkout Overcommit hook refused missing gems.
No hook was bypassed. The parent initial preflight stopped on its failed status.

Configuration's declared Nix environment and existing absolute local bundle path
provide all exact Gemfile dependencies; bundle check passes. Preparation will
run in that environment with BUNDLE_PATH explicitly inherited from this owned
feature checkout's existing .bundle/config. The detached checkout has the same
committed Gemfile/lock, so ordinary Overcommit can run there too. No dependency,
head, approval, source, hook or package changes are required. Preserve failed
unit/log/status and inspect the normal retained-source retry before accepting
new success.
