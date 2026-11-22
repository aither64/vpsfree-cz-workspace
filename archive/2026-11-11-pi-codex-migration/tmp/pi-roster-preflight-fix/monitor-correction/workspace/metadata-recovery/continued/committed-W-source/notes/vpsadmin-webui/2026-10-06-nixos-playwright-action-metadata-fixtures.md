# NixOS browser setup and HaveAPI action fixtures

Session: work/2026-10-05-network-ipv4-left-counter.

The cached generic-Linux Playwright headless browser failed on NixOS with
stub-ld/exit 127 before page execution. Use the existing
E2E_CHROMIUM_EXECUTABLE_PATH option with Chromium from the repository's locked
nixpkgs input. Resolve its executable before entering the nested development
shell. The pinned Playwright CLI stays unchanged.

```sh
nix shell --inputs-from . nixpkgs#chromium --command bash
export E2E_CHROMIUM_EXECUTABLE_PATH="$(command -v chromium)"
nix develop --command node scripts/playwright.mjs test SELECTED_SPEC
```

The network-availability desktop run launched Chromium 154.0.8037.57 and passed
the old-API and disabled-inventory cases. It exposed separate fixture errors in
the toggle cases. No browser policy relaxation was used. Complete browser
verification is recorded in the session, rather than implied by this setup proof.

HaveAPI action OPTIONS fixtures must retain action-description structure.
Returning only input makes unwrapSingleResponse treat it as a namespace and
remove that key. Real HaveAPI 0.29.8 descriptions have method, scope, input,
output and other metadata. The fixture should also assert method=PUT for network
updates. A hidden availability control can therefore indicate malformed fixture
metadata even when the product's capability guard is correct.

Sources: W playwright.config.ts, scripts/playwright.mjs and
src/lib/api/haveapi.ts; HaveAPI action.rb and server.rb. See the session's
network-fixture-repair.md and post-review2-react-desktop.log for evidence.
