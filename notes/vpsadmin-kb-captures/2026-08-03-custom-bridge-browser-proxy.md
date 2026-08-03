# Custom bridge addresses and the capture browser proxy

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`

## Symptom

A screenshot cluster using a checked-free custom bridge range started and
seeded successfully, but checkpoint fixture setup timed out while looking for
the seeded `Praha` location. Direct SQL against the cluster's services VM
showed the expected locations, while a browser diagnostic showed
`test-location` from a different concurrent development cluster.

## Cause

In bridge mode, `lib/browser.cjs` opens its CONNECT tunnel to the requested
WebUI hostname. The hostname has a static address, so it does not follow the
custom services IP in the cluster's ignored `config.json`. A unique slug,
socket directory, and bridge addresses isolate the VMs, but are not enough to
route the capture browser to them.

## Workaround

When the fixed hostname belongs to another live cluster, stop only the
capture-specific cluster, verify the local forwarding ports are free, and
restart the disposable screenshot topology with `--network local`. The browser
proxy explicitly sends local-mode WebUI traffic to `127.0.0.1:10443`.

Do not retry captures against the custom bridge cluster or use `--force`: both
can silently capture the other cluster. A durable bridge-mode fix would make
the browser proxy connect to the configured services IP while preserving the
original hostname for TLS.

## Verification

Compare fixture data directly through `bin/devcluster ssh SLUG services` with
the page rendered through the capture browser. They must identify the same
locations before accepting any screenshots.
