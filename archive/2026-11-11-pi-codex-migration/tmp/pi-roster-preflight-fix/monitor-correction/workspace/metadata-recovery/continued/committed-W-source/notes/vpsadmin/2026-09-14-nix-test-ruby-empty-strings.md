# Empty Ruby strings inside Nix integration scripts

An empty Ruby single-quoted string terminates the surrounding Nix indented
string. Nixfmt then reports an unexpected closing brace on a later line rather
than a Ruby error. Use an empty double-quoted Ruby string in that context.

Nixfmt and Ruby syntax checks passed after the correction in the standalone
kernel-history integration fixture. Related initiative:
work/2026-09-14-kernel-history-fix.
