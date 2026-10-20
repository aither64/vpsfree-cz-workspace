# Bot merge-hook environment diagnosis

Read-only diagnosis of failed selected-package queue preparation. No source,
runtime/tool, dependency, hook-signature or coordination-state changes performed.
Bot feature/source remains `a5d1dfe565526c3532183d756c592a26e7270675`.

## Cause and support boundary

Selected package:
`/nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0`.
Its `libexec/workspace-coordination-execution.rb:335` enters the retained
source's declared Nix shell, then at line355 runs absolute `RbConfig.ruby` for
the Bundler/Overcommit validator. The runtime Ruby is:
`/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby`.

The bot shell selects Ruby3.3, sets `GEM_HOME=.gems`, `GEM_PATH=.gems:lib`,
`BUNDLE_PATH=.gems`, and installs its bundle in `.gems/ruby/3.3.0` before setting
`RUBYOPT=-rbundler/setup`. The checker then uses Ruby3.4 with that BUNDLE_PATH;
Bundler correctly seeks `.gems/ruby/3.4.0`, which is absent. This is the observed
GemNotFound in `vpsfree-irc-bot-prepare.log`, not failed RuboCop or application
verification.

Installing the same frozen bundle for the selected runtime Ruby alongside3.3 is
ordinary dependency setup within the selected package's stated preparation
contract: `workspace-host coordination guide` says dependency installation occurs
in retained source outside claims, with Bundler Overcommit checked before
admission. It does not require source/runtime changes or bypass hooks. The
underlying package has a real interpreter-selection mismatch; side-by-side bundle
setup satisfies both interpreters without pretending it was fixed in source.

Read-only probe using locked Bundler4.0.12 from existing3.3 gems, loaded under
selected3.4.9, returned:

```text
Ruby 3.4.9; Bundler 4.0.12
bundle_path=.../checkout/.gems/ruby/3.4.0
frozen=true
lockfile readable: 79 specifications
```

The existing Gemfile.lock has Ruby and x86_64 Linux platforms and no explicit
Ruby-version restriction. Bundler uses ABI-specific install/extension directories,
so existing3.3 dependencies remain in place. Native extensions must be built for
3.4, not copied/symlinked from3.3.

## Proposed exact setup (NOT EXECUTED)

Lead assessment and fresh watcher required before execution; installation duration
is uncertain. Use the selected package/runtime paths above, not another runtime.
Working directory is the exact coordinator-owned retained source from the failed
preparation:

```sh
cd /home/aither/.local/state/dev-workspaces/coordination/sources/a5d1dfe565526c3532183d756c592a26e7270675/checkout
nix develop --command bash -c '
  set -euo pipefail
  unset RUBYOPT
  export BUNDLE_FROZEN=true
  NIX_ENFORCE_PURITY=0 \
    /nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby \
    -I "$PWD/.gems/ruby/3.3.0/gems/bundler-4.0.12/lib" \
    "$PWD/.gems/ruby/3.3.0/gems/bundler-4.0.12/exe/bundle" install
  /nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby \
    -r bundler/setup -r overcommit -e '\''puts "selected runtime hook bundle OK"'\''
  git diff --exit-code
  test -z "$(git status --porcelain)"
'
```

Nix shell supplies compiler/stdenv, gnumake, pkg-config, OpenSSL, zlib,
libxml2/libxslt and repository environment variables. The absolute selected Ruby
supplies its3.4 headers/config. Native gems include json, bigdecimal, prism, racc,
nio4r, rinku, io-console and potentially nokogiri. Existing shellHook uses
NIX_ENFORCE_PURITY=0 for prism generated headers; reuse it only for install.
No new dependency versions or force-ruby-platform flag are needed. Existing
locked Bundler4.0.12 avoids auto-switch/reexec choosing shell Ruby3.3; loading it
explicitly is pure Ruby and was tested read-only under3.4.9. Unset RUBYOPT for
installer bootstrap because its premature Bundler.setup otherwise fails before
install can run. The final checker restores equivalent `-r bundler/setup`.

BUNDLE_FROZEN prevents Gemfile.lock resolution/rewrites. Only ignored `.gems`
and normal local Bundler setup paths may change. Require clean tracked status
and unchanged Gemfile/lock/config hashes after setup, then retry the public
selected-package `dev-session coordination prepare` through the lead. Do not
invoke its Ruby helpers directly or merge around the queue.

If the frozen install rejects the3.4 interpreter/platform or exact checker still
fails, preserve the error and report a selected-package mismatch; do not change
locks, add interpreter aliases, alter source/runtime, disable hooks or bypass the
coordinator. No install has been attempted in this diagnosis.
