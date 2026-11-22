# Non-interactive `confctl build` needs confirmation enabled

## Symptom

Running `confctl build <machine>` from a non-interactive shell evaluates the
machine list, prints `Continue? [y/N]:`, and exits with `end of file reached`
before starting a build.

## Cause and workaround

`confctl build` confirms its resolved machine set through standard input by
default. Add `-y` or `--yes` for an unattended build:

```sh
confctl build -y cz.vpsfree/vpsadmin/int.api1
```

The retry built all selected vpsAdmin API and WebUI hosts successfully. Related
initiative: `work/2026-09-03-webui-vps-ipv6`.
