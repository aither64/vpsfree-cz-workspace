# Test maintenance entry points through the installed loader

The `vpsadmin-api-ruby` interpreter loads the requested Ruby script with `load`
without changing `$0` (vpsAdmin `nixos/modules/vpsadmin/api-runners.nix`). A script
using `exit cli(ARGV) if $0 == __FILE__` therefore does nothing and exits 0 when
run through its installed shebang, even though direct `ruby script.rb` tests pass.

Keep importable code in a task helper and invoke the CLI unconditionally from
the small executable. Test the loader boundary with
`ruby -Ilib -e 'load ARGV.shift' SCRIPT ARGS...` in the matching API environment.
The kernel-history task exercises help, dry-run, apply and idempotent rerun on a
disposable MariaDB database this way; all 29 task examples pass.

Related initiative: `work/2026-09-14-kernel-history-fix/`.
