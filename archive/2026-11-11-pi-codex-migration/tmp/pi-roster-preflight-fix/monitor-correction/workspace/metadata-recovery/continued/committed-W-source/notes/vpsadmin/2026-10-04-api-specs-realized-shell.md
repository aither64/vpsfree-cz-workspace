# API-spec workflow setup in a restricted member shell

Observed in [API-spec optimization](../../work/2026-10-03-api-specs-optimization/state.md)
on 2026-10-04, vpsAdmin source f9beb46e, Nix 2.34.8.

A workspace-write member could edit its assigned worktree but could not access
the Nix daemon socket, resolve RubyGems DNS, or open the database sockets needed
by the mandatory API i18n pre-commit hook. These were execution restrictions;
repository write access and trusted session identity were valid. A writable
XDG_CACHE_HOME fixed the initial cache error but did not fix daemon access.

The unrestricted lead ran the repository's declared root/API Nix environments
and their shell hooks, installing dependencies in the owned worktree. It also
exported the realized environments with `nix print-dev-env .#vpsadmin` and
`nix print-dev-env .#api`. The member could activate those same realized store
tools and installed gems offline, preserving each shell hook's local exports.
Do not treat sourcing the generated environment as having executed shellHook;
confirm the declared setup was actually completed first. This approach was
verified for this shared-user environment, not a general privilege escalation.

The member retained source ownership, quick checks and staged commit preparation.
The lead executed its prepared normal `git commit -F` from the declared root
Nix shell. All mandatory hooks then passed, including temporary DB startup.
No hook bypass, config change, production DB or application edit was needed.
An unrelated sandbox failing network or sockets should be resolved at execution
ownership rather than weakening tests or hooks.

For YAML helpers in the API shell, use `bundle exec ruby -ryaml`, as documented
by the topic-reproduction command. Plain `ruby -ryaml` with RUBYOPT's Bundler
setup activated default date 3.4.1 before the resolved bundle required 3.5.1.
The Bundler-prefixed helper resolved the intended gems and selected exactly the
same platform-infrastructure manifest as the workflow. No dependency change was
needed.
