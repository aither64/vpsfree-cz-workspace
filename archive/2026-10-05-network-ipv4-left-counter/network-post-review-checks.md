# Prepared post-review checks

Source and command preparation only. No command below has been executed. The
lead must first clear the complete committed V/W/C/K deliverable through final
independent review, then launch each selected operation with a fresh watcher.
Exact reviewed V, W and C heads are required by the wrapper; changed/dirty
worktrees refuse. Every mode stops on a failure and records logs/exits beneath
this session. The watcher reports and stops; it does not diagnose, retry, edit,
approve or deploy.

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/run-network-post-review-check.sh MODE V_SHA W_SHA C_SHA
```

| Mode | Exact operation |
| --- | --- |
| sql-admission | All-plugin isolated MariaDB `ip_ownership_concurrency_spec.rb --tag network_admission` |
| vm-routes | `network/network-interface-routes-and-host-ips` |
| vm-export | `network/export-lifecycle` |
| vm-migration | `vps/migrate-with-data-check` |
| vm-restore | `storage/restore-after-reinstall-with-descendants-remote` |
| legacy-admin-cluster | `webui#admin-cluster` |
| react-desktop | `network_availability.spec.ts`, Chromium, both EN/CS toggle scenarios |
| react-mobile | Same scoped spec, mobile-chrome, both EN/CS toggle scenarios |
| react-build | Existing production `npm run build`, output beneath tracking |
| config-build | Exact 12 channel consumer hosts in `network-affected-config-hosts.txt`, serial build only |

## Fixtures and limits

SQL mode refuses an inherited DATABASE_URL or API database.yml and uses the
existing temporary DB bootstrap. Five tagged cases cover disable-before-use,
admission-before-disable, parallel same-pool admissions and owned registration
serialization/denial. The established connection-thread fixtures and cleanup
remain in the existing spec; this is real SQL with synthetic objects.

VM selectors are registered in V `tests/all-tests.nix`; each changed scenario
has one testScript. The legacy script key is defined in
`tests/suite/webui.nix:5103`. Its seed and Playwright fixtures run in owned test
VMs, not production. Four changed VM scenarios retain existing setup and known
sentinel/checksum assertions; migration and restore explicitly attach an address
because the common VPS fixture requests zero IPv4 addresses by default.
Existing exportfs service state is asserted after disabling its endpoint pool.
Runner state is separately scoped beneath this tracking directory. No reusable
development cluster is started, stopped or reset by these commands.

React uses the installed pinned Playwright CLI and `network_availability` mock
fixtures, without a live API or credentials. Tests capture implemented EN/CS UI
with `testInfo.outputPath`, so desktop/mobile images land beneath tracking. The
wrapper uses a fixed loopback development port, CI server ownership checks,
serial workers and zero retries. It does not reuse an existing server, download
packages or change Chromium policy. The pinned browser must already be installed;
if absent, stop and report the required setup separately. The production build
uses the existing BFF runtime mode and does not build an NixOS host itself.

C maps channel vpsadmin to vpsadminServices and vpsadmin-webui to vpsadminWebui.
Eleven modules under `cluster/cz.vpsfree/vpsadmin/int.*/module.nix` select the
vpsadmin channel; the React host selects vpsadmin-webui. All eleven legacy/API
hosts import common/all.nix, whose module and overlay come from the selected
vpsAdmin input; the React config selects the WebUI module/packages. This is why
DB, RabbitMQ, Redis and mailer hosts are included in the bounded 12-host source
mapping even though their service behavior is unchanged. Build commands do not
activate services or run a live migration. No node channel or other host is added.

## Kernel substitution and cancellation evidence

V's locked vpsAdminOS revision is
`8e44a5124439b1f3048ffc56b1717614a5360358`. Its
`.github/workflows/kernels.yml` detects every lib.kernelVersions entry, builds
`ci-toplevel-kernel-VERSION`, and publishes the closure and a profile generation
to the binary cache. This is source evidence for the substitution contract,
not a fresh proof that every needed path is available in the current cache.
No kernel source/configuration/input changes are part of this feature.

The workspace verification procedure requires stopping an unexpected local Linux
kernel build and reporting the derivation/cache miss for lead diagnosis. The
watcher must apply that rule during VM/config setup or execution and must not
silently accept a local kernel build. Do not stop the Nix daemon, unrelated jobs,
the development session or another session's resources.

The pinned test-runner CLI defaults to one job and supports --stop-on-failure
and --state-dir; the wrapper sets these explicitly. Its executor stops scheduling
after an unexpected result with that option. W scripts/playwright.mjs maps an
owned child SIGINT/SIGTERM result to 130/143. These are source facts; graceful
cancellation of the entire process tree has not been newly tested. The fresh
watcher uses its operation ownership/cancellation policy to cancel only its
owned command when required, preserving all diagnostics and escalating uncertain
remaining processes. There is no session lifecycle or background cleanup helper.
