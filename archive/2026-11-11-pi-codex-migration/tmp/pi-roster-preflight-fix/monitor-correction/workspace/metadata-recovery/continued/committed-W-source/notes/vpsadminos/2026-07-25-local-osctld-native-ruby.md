# Local osctld specs require the patched Ruby

## Symptom

An osctld spec run can fail while loading `libosctl/native.so` with:

```text
undefined symbol: rb_thread_start_timer_thread
```

## Cause

The named `libosctl` and `osctld` development shells use the generic Ruby
package. vpsAdminOS's native helper calls timer-thread symbols exported by the
project's patched `ruby_vpsadminos`, which is provided by the repository's
default development shell. Rebuilding the helper in a named shell leaves a
locally valid ELF object linked to the wrong Ruby.

## Workaround

Build and run through the default development shell, select the component
Gemfile explicitly, and change the test process's directory with `env -C`
instead of entering a named shell. The ignored ruby-lxc helper must also have
been built with the same patched Ruby.

For `libosctl`, run its `clobber compile` task from the default shell. For
osctld, use the osctld Gemfile and include the local ruby-lxc and libosctl
library paths in `RUBYLIB`.

From the vpsadminOS repository root:

```sh
nix develop -c env \
  BUNDLE_GEMFILE="$PWD/libosctl/Gemfile" \
  BUNDLE_PATH="$PWD/.gems" \
  bundle exec rake -C libosctl clobber compile

nix develop -c env -C osctld \
  BUNDLE_GEMFILE="$PWD/osctld/Gemfile" \
  BUNDLE_PATH="$PWD/.gems" \
  RUBYLIB="$PWD/.native/ruby-lxc:$PWD/libosctl/lib" \
  bundle exec rspec
```

## Verification

Rebuilding `libosctl/native.so` this way linked it to the same
`ruby_vpsadminos` store path as the ruby-lxc helper and allowed the osctld
suite to load again.

Related initiative: `work/2026-07-24-ct-start-hang/`.
