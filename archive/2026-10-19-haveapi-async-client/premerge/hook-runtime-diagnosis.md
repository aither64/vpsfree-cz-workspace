# Hook runtime diagnosis

Read-only findings by implementer1 for session `2026-10-19-haveapi-async-client`.
The selected coordinator cannot prepare the authorized HaveAPI merge because its
Ruby differs from the repository Ruby. No dependency install was attempted.

## Exact source and runtime

- Selected package: `/nix/store/i144xnc9p02svar5kz6jxjjpp6gz4cwh-dev-workspace-0.2.0`.
- Retained HaveAPI source: `/home/aither/.local/state/dev-workspaces/coordination/sources/19c20c90cc957d4225ece50a92e190855f252710/checkout`, HEAD `19c20c90cc957d4225ece50a92e190855f252710`.
- Coordinator: `/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby`, Ruby **3.4.9**, extension API
  **3.4.0**, `x86_64-linux`.
- Repository: `/nix/store/mdxh20cd9flvz6bbr7xw0qsh1aa3mhni-ruby-3.3.10/bin/ruby`, Ruby **3.3.10**, extension API
  **3.3.0**, `x86_64-linux`. The default flake selects `ruby_3_3`.

Direct absolute Ruby `--disable-gems -rrbconfig` reads confirmed both versions and
APIs. The retained JSON/Prism native build logs and Makefiles independently name
Ruby 3.3.10. No `nix develop` or shell initialization ran during this diagnosis.

## Failure and dependency state

The retained [prepare log](prepare.log) reports `Bundler::GemNotFound` for
`json-2.21.2`, `racc-1.8.1`, `prism-1.9.0`, and `bigdecimal-4.1.3`. All four have
`gem.build_complete` under `.gems/extensions/x86_64-linux/3.3.0`; there is no
`3.4.0` extension directory. The installation exists for the repository API.

`libexec/workspace-coordination-execution.rb:355` enters the repository's Nix
shell, whose hook assigns `GEM_HOME=$HAVEAPI_REPO_ROOT/.gems`, then explicitly runs
its own absolute `RbConfig.ruby`. `Bundler.setup` therefore checks the 3.3 gem home
using Ruby 3.4 and fails before publishing `WORKSPACE_MERGE_HOOK_ENV`. The lead
reports no job was admitted; this diagnosis did not run coordinator commands.

## Why a second install is not a safe local repair

The native files also exist in shared `.gems/gems/<version>/lib` paths. The
coordinator Ruby's standard RubyGems configuration has
`install_extension_in_lib=true`; `rubygems/ext/ext_conf_builder.rb:49-60` copies
built native outputs into that shared library directory with
`cp_r(..., remove_destination: true)`, as well as the API-specific extension tree.
A standard same-home install with Ruby 3.4 can overwrite the repository's 3.3
library files. Merely keeping both extension completion trees does not establish
safe dual-ABI loading. This overwrite risk was established from source and file
layout, not by attempting an install.

An external separate gem home is outside the current supported preparation:
coordinator entry clears incoming gem variables, and the repository hook selects
its own `.gems`. Repeating normal repository `bundle install` builds for Ruby 3.3
and leaves the coordinator's runtime mismatch.

## Minimum correction proposal

In `prepare_merge_hooks`, change the executable argument after `--command` from
`RbConfig.ruby` to `'ruby'`, so Nix resolves the repository shell's Ruby through its
entered `PATH`. Preserve shell initialization, Bundler/Overcommit validation,
the environment allowlist, normal hooks, and coordinator approval/queue gates.
Architect0 owns design and checking the latest canonical source. A corrected,
reviewed package must follow the supported package workflow; this is not a
proposal to edit the selected store package or bypass coordination.

No dependency-only command for the current package is recommended. After a
corrected package, only if a dependency install is still needed, the standard
repository command from the retained checkout is:

```sh
nix develop /home/aither/.local/state/dev-workspaces/coordination/sources/19c20c90cc957d4225ece50a92e190855f252710/checkout --command bundle install
```

That command is **unexecuted**, conditional on the corrected package and the
lead's authorization. Existing 3.3 completion markers already indicate successful
native builds for the declared repository runtime.

## Scope and preservation

The diagnosis ran only quick file reads and absolute Ruby configuration reads.
It ran no install, Nix development shell, test/build/browser, watcher, merge or
push. It changed no source, index, configuration, ledger, selected package, or
profile. Only this Markdown file and its [JSON receipt](hook-runtime-diagnosis.json)
were added under the assigned evidence scope. The JSON records evidence hashes
and the hashes of every pre-existing immediate premerge JSON file; all remained
unchanged when these two files were created. No tokens or environment dumps are
included. Product verification is unaffected; merge preparation remains blocked
until the runtime-selection issue is resolved through the supported workflow.
