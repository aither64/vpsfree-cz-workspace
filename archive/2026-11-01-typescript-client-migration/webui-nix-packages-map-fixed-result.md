# WebUI Nix package verification

- Result: **passed** (exit status 0)
- Source revision: `7cad7ffb3a0a294c30349680e2eb4f80c63a3926`
- Build source: `/nix/store/6dakiqjksbcbzfxx2bimzj75qbgksj6n-source` (`sha256-qty7vrxXhqx7w//2ywj6eaoPTLbX4s+kx7UXFleoDr0=`)
- Command: the single five-output `nix build --no-link --print-out-paths` command in the full log.
- Elapsed time: approximately 56 seconds.
- Full stdout/stderr and preserved command exit status: `webui-nix-packages-map-fixed.log`.

## Output store paths

- Frontend: `/nix/store/fkrzrdh3ipyj545xaz2kmfa56rc9zmin-vpsadmin-webui-frontend-1.0.0`
- BFF: `/nix/store/8wra35xfakwm6hj7xb3qg7b5w00yj987-vpsadmin-webui-bff-0.1.0`
- Provenance check: `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance`
- Source contents check: `/nix/store/kjb21q31wmw8pffrpmddkz8sbw9rx47f-vpsadmin-webui-source-contents`
- Package contents check: `/nix/store/yigrf43ax9ldhbqyaqf8asrcrf72i9s9-vpsadmin-webui-package-contents`

Both package build-info files were read. Frontend and BFF report schema version 1, commit `7cad7ffb3a0a294c30349680e2eb4f80c63a3926`, `dirty: false`, and source `environment`.

This verifies the five requested Nix outputs for the pinned source. It does not establish host deployment, CI status, or whole-browser acceptance.
