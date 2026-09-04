# Adding a new flake input with confctl

Related initiative: `work/2026-09-03-dev-session-portal`

After declaring a new flake input and channel role in `flake.nix`, running
`confctl inputs channel set --commit` fails with `unknown input` while the input
is absent from `flake.lock`. The setter only changes lock nodes that already
exist.

Use `confctl inputs channel update --commit <channel> <role>` for the first
lock entry. It adds the input through `nix flake update` and creates the normal
generated input commit. Once the input exists in `flake.lock`, use `channel set`
when a later update must select an exact revision.

For a feature input whose URL already names its branch, first push the desired
branch head and confirm the generated lock entry selected that full revision.
