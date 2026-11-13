# IRC bot daily updater: failure mechanism (E0)

Owner: implementer2. Investigation only, 2026-11-13 UTC. D0 was accepted
before this package. No application changes, builds, reruns or publication.

## Source and failed attempt

Verified `dev-session current`, both environment markers and the retained
same-session roster. Current GitHub default is `vpsfreecz/vpsfree-irc-bot`
`master` at `7d7a48b2b2dc45732cf5853deca196b1ae05571f`, unchanged from D0.
The complete immutable source tree contains no `AGENTS.md`. Read its README,
flake, Gemfile, lockfile, Overcommit configuration and daily updater.

[Run 43425361187](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/43425361187)
uses that same head and fails `Update package dependencies`.
The preceding two schedules also failed; this investigation reuses the
downloaded failed-attempt log and does not rerun anything.

## Causal sequence

| Stage | Environment and observed behavior |
| --- | --- |
| Enter `nix develop` | The flake selects Ruby 3.3 and installs application gems under `$PWD/.gems`. The log shows Ruby 3.3.13. Bundler 4.0.24 is installed, then the existing lock causes an automatic switch to Bundler 4.0.12. Nokogiri 1.19.3 is installed as `x86_64-linux-gnu`; 70 gems finish installing. |
| Finish the shell hook | The hook exports `BUNDLE_GEMFILE`, `BUNDLE_PATH`, `GEM_HOME`, `GEM_PATH`, and finally `RUBYOPT=-rbundler/setup`. Every subsequent Ruby invocation inherits automatic application-bundle activation. |
| Mutate the bundle definition | Inner `bash -lc` sets local `force_ruby_platform=true`, then removes `gemset.nix` and `Gemfile.lock`. The previously installed binary-platform Nokogiri no longer satisfies the selected Ruby-platform bundle. |
| First failure | The next `bundle lock --add-platform ruby` invocation fails during Ruby startup in Bundler 4.0.24 `setup.rb`, before its lock command can resolve/install anything. Only `nokogiri-1.19.3-x86_64-linux-gnu` is present; Ruby-platform Nokogiri is missing. The return to Bundler 4.0.24 is consistent with the old lockfile having been removed. |
| Cascading failure | Inner `bash -lc` has no fail-fast option, and the log shows execution continuing into the second tool environment. Nixpkgs’ Bundix wrapper selects its own Ruby/Bundler and replaces `GEM_HOME`/`GEM_PATH` with its tool bundle. Inherited `RUBYOPT` still tries to activate the IRC bot Gemfile. Ruby 3.4.11/Bundler 2.7.2 then reports missing `overcommit`, which is deliberately absent from the tool bundle. This occurs before Bundix’s command body. |
| Exit | Bundix is the final inner command, so its failure makes `nix develop` fail. Actions’ outer `/usr/bin/bash -e` stops before `git add` or `git commit`. No commit hook runs in this attempt. |

The exact command attribution is inferred from the immutable script order,
the two distinct interpreter stacks, and their `bundler/setup.rb` entry points;
the log does not enable shell tracing. The errors and installed versions above
are direct observations.

This corrects D0’s initial attribution of the second exception to a hook
environment. It is a tool-startup cascade. The original workflow also places
commit outside the Nix shell, which is a separate latent environment problem
for required hooks after fixing generation.

## Official dependency contracts

- [Bundler 4.0.24 setup](https://github.com/ruby/rubygems/blob/3b396e42bdf993c7cbf64647fca2a31177eab734/bundler/lib/bundler/setup.rb)
  activates the application bundle when inside a Gemfile directory. The failed
  stack enters its noninteractive `Bundler.setup` branch.
- [Bundler 4.0.24 configuration](https://github.com/ruby/rubygems/blob/3b396e42bdf993c7cbf64647fca2a31177eab734/bundler/lib/bundler/man/bundle-config.1.ronn)
  defines `force_ruby_platform` as selecting Ruby-platform gems and compiling
  native extensions from source. The installation made before that switch
  does not satisfy the new selection.
- [Bundler 4.0.24 lock command](https://github.com/ruby/rubygems/blob/3b396e42bdf993c7cbf64647fca2a31177eab734/bundler/lib/bundler/man/bundle-lock.1.ronn)
  resolves a lock without installing gems. Locking alone cannot repair the
  installed application environment needed by hooks.
- The bot’s effective `nixpkgs` input resolves through `vpsadminos` to
  `c56a87d8e41ce69bd2af57eb35dcc117a9dfca33`.
  Its [Bundix package](https://github.com/NixOS/nixpkgs/blob/c56a87d8e41ce69bd2af57eb35dcc117a9dfca33/pkgs/by-name/bu/bundix/package.nix)
  pins Bundix 2.5.2, inherits Bundler’s Ruby, and explicitly replaces
  `GEM_HOME` and `GEM_PATH` with its own tool environment.
- [Bundix 2.5.2 command line](https://github.com/nix-community/bundix/blob/e9f533a9a28555aa759b7418a739d79c06192bfb/lib/bundix/commandline.rb)
  clears several Bundler variables only inside `handle_lock`; it does not
  remove inherited `RUBYOPT` before Ruby starts. Its `-l` option conditionally
  invokes `bundle lock` before converting the lockfile.
- [Overcommit installation](https://github.com/sds/overcommit#installation)
  requires installing repository hooks before expecting commits to run them.
  The flake shell installs the gem but does not install hooks.

## Smallest faithful fix candidate for the architect

Keep the current source-platform Bundix workaround, schedule, permissions,
tracked outputs and ordinary push. Change the workflow’s update block:

1. Use a non-login, fail-fast Bash invocation inside `nix develop`.
2. Clear inherited `RUBYOPT` before changing bundle configuration, removing
   the lock, invoking Bundler or invoking Bundix. Those are maintenance tools,
   not application execution. Preserve the project Gemfile/path settings.
3. Retain forced-Ruby-platform locking and regenerate `gemset.nix` from it.
4. Install the refreshed application lock before hook execution. Preserve the
   existing `NIX_ENFORCE_PURITY=0` install setting required by the flake’s
   documented prism native-extension workaround.
5. Install/activate required Overcommit hooks and stage/commit the two generated
   files inside the same bot Ruby environment. A generation, installation or
   hook failure must stop before publication. Do not bypass hooks.

Setting `BUNDLE_FORCE_RUBY_PLATFORM=true` before entering the shell can also
make its initial installation use the intended platform immediately; clearing
`RUBYOPT` for tools remains necessary because Bundix owns a separate Ruby
environment. Changing only Overcommit, clearing only Bundix’s preload, or
installing gems before changing the lock would leave part of the causal chain.

The README’s Bundix recipe mirrors the failing command, so a released fix
should keep that recipe consistent. No general updater framework is needed.
No runtime schema, bot behavior or deployment change is involved; recovery is
reverting the workflow/documentation change. Preserve the generated-output
boundary and avoid updating dependencies merely to test the workflow.

Before implementation, the architect must settle the exact workflow/README
scope and check ownership. Official releases checked during E0 are
[checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) and
[install-nix-action v31.11.5](https://github.com/cachix/install-nix-action/releases/tag/v31.11.5).
The current workflow imports `checkout@v6` and `install-nix-action@v31`;
any ref selection must follow the workspace’s latest-compatible-action rule.

## Minimum verification after release

Quick checks: parse the changed workflow, syntax-check its extracted shell,
and verify ordering/environment boundaries. A stubbed command test alone
cannot establish bundle/platform correctness.

The smallest faithful execution uses a fresh session-owned disposable checkout
and clean `.gems`, runs the exact update/install/hook-managed local commit block
with push omitted, and confirms: maintenance commands run without application
preload; the forced-Ruby Nokogiri bundle installs; generated lock and gemset
agree; hooks run under the selected bot Ruby; and only intended output files
are committed. Record interpreters and resolved tool versions without dumping
the environment. Check the no-change publication guard without another
unnecessary network update.

Native gem installation is uncertain-duration verification and may compile
Nokogiri/prism, so it needs the verification watcher and the normal independent
review/long-check ordering. It was not launched in this investigation. Full bot
VM integration is not required merely to prove this environment repair unless
the implementation expands into runtime or package behavior.

## Delivery

E0 is ready for acceptance. Architect0 and lead received the mechanism and
minimum-check proposal during the first checkpoint. Implementation remains
blocked on the architect-owned brief and lead package release, not on missing
diagnostic evidence. Application head remains
`7d7a48b2b2dc45732cf5853deca196b1ae05571f`; no branch, source commit or migration
was created. Temporary downloads live in `/tmp/scheduled-workflow-irc-e0` and
the D0 raw-evidence directory; durable evidence is this Markdown file.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/).
