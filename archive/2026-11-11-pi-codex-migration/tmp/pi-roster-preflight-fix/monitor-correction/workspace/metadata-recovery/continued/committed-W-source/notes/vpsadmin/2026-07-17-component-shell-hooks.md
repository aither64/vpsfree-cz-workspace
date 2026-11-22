# vpsAdmin component shells and hooks

Related initiative:
`work/2026-07-13-security-advisory-automation/`

The component development shells can change the working directory to the
selected component. For example, `nix develop .#libnodectld` enters the
`libnodectld` directory already, so a following `cd libnodectld` fails.

Final vpsAdmin commits must run inside `nix develop .#vpsadmin`; the installed
Overcommit hooks need the Nix-provided RuboCop, gettext, and MariaDB tooling.
Ambient-shell commits are rejected when those tools are absent.

The libnodectld bundle does not include RuboCop. Run its lint from the API
shell while selecting the component configuration, for example:

```sh
nix develop .#api --command bundle exec rubocop \
  --config ../libnodectld/.rubocop.yml FILES...
```

Focused libnodectld specs run normally in `nix develop .#libnodectld`.
