# Dev vpsAdmin clusters state

Date: 2026-05-30

Affected repositories/workspaces:

- coordination workspace: `/home/aither/workspace/ai/vpsfree.cz`
- reference only: `/home/aither/workspace/vpsf-dev`
- consumed worktrees: `worktrees/<slug>/vpsadmin`, optional `vpsadminos`, optional
  `haveapi`, optional `vpsfree-cz-configuration`
- vpsadminos branch/worktree:
  `2026-05-30-dev-vpsadmin-clusters` at
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadminos`
- vpsadmin branch/worktree used for bridge verification:
  `2026-05-30-dev-vpsadmin-clusters` at
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadmin`
- vpsfree-cz-configuration branch/worktree:
  `2026-05-30-dev-vpsadmin-clusters` at
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsfree-cz-configuration`

Progress:

- Implemented workspace-local dev cluster tooling under
  `dev-clusters/vpsadmin/`.
- Added `.dev-clusters/` to `.gitignore` for runtime state.
- Added topologies `single`, `dual`, and `storage`.
- Added HTTPS certificate workflow:
  `cert import-vpsf-dev`, `cert init`, and `cert show-ca`.
- Imported the existing vpsf-dev CA/cert into ignored runtime state for local
  validation.
- Generated an ignored runtime SSH key at `.dev-clusters/vpsadmin/ssh/`.
- Added `--network local`, which runs QEMU without bridge privileges using
  localhost forwards and an inter-VM QEMU socket network.
- Booted a single-node QEMU cluster for slug
  `2026-05-29-security-advisories`; it is currently running and ready.
- Added OSVM support for optional bridge network `opts.helper`, rendering QEMU
  `-netdev bridge,...,helper=...` only when configured.
- Added a restricted `qemu-bridge-helper` setuid wrapper to the `aitherdev`
  host configuration, using the existing `br0`/`virbr0` bridge allowlist.
- Wired workspace bridge-mode cluster JSON to pass
  `/run/wrappers/bin/qemu-bridge-helper` by default, configurable with
  `VPSADMIN_DEVCLUSTER_BRIDGE_HELPER`.

Commands/results:

- Initial inspection confirmed `vpsf-dev` uses fixed aitherdev DNS/IPs and local
  CA/cert files.
- Initial inspection confirmed current host has `br0` at `172.16.106.40/24` and
  DNS names such as `webui-tmp.aitherdev.int.vpsfree.cz` resolving into the dev
  network.
- Created initiative worktrees for `vpsadminos` and
  `vpsfree-cz-configuration`. The bare `vpsadminos` clone had no local HEAD, so
  local branch `staging` was anchored to `origin/staging` before adding the
  feature worktree.
- `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
- `ruby -c dev-clusters/vpsadmin/lib/devcluster-runner.rb`: passed.
- `dev-clusters/vpsadmin/bin/devcluster cert import-vpsf-dev --force`: passed;
  imported CA fingerprint
  `87:53:34:E0:1E:07:88:F5:FE:E9:3A:86:08:B3:6E:52:DB:4C:67:13:B9:D8:F6:E7:6F:7F:B7:C7:74:A3:05:5B`.
- `dev-clusters/vpsadmin/bin/devcluster urls 2026-05-29-security-advisories`:
  printed the expected `*-tmp.aitherdev.int.vpsfree.cz` HTTPS URLs.
- `nix eval --raw --impure ...#packages.x86_64-linux.cluster-config.drvPath`
  with `topology=single`: passed.
- `nix build --impure ...#cluster-config` with `topology=single`: passed and
  built `/tmp/vpsadmin-devcluster-config-check`.
- `nix run --impure ...#runner -- help`: passed as an expected usage exit,
  proving the Ruby runner can load OSVM.
- `nix eval --raw --impure ...#packages.x86_64-linux.cluster-config.drvPath`
  with `topology=dual`: passed.
- `nix eval --raw --impure ...#packages.x86_64-linux.cluster-config.drvPath`
  with `topology=storage`: passed.
- After correcting the generated seed to point `core.auth_url` at
  `auth-tmp.aitherdev.int.vpsfree.cz`, single-topology Nix evaluation passed
  again.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-05-29-security-advisories
  --topology single --network bridge`: reached QEMU launch, then failed because
  unprivileged `qemu-bridge-helper` cannot create the bridge tap device for
  `br0` in this shell.
- Committed the vpsAdminOS OSVM bridge-helper support as
  `b4230c479 osvm: support explicit QEMU bridge helper`.
- Rebuilt vpsAdminOS packaged gems with `nix develop --command make gems`.
  The build published `25.11.0.build20260531170948` gems and updated
  `.build_id` plus `os/packages/*/{Gemfile,Gemfile.lock,gemset.nix}`.
- Committed the generated vpsAdminOS gem refresh as
  `dfed89a5d os: update gems to 25.11.0.build20260531170948`.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-05-29-security-advisories
  --topology single --network local`: passed after fixing short socket paths,
  services CPU topology, cert paths inside the VM, services virtiofs mounts, and
  nginx SSL/internal redirect configuration.
- `dev-clusters/vpsadmin/bin/devcluster update
  2026-05-29-security-advisories services`: passed twice and switched the
  running services VM in place.
- `dev-clusters/vpsadmin/bin/devcluster status
  2026-05-29-security-advisories`: running, topology `single`, network `local`,
  ready `yes`, PID `199279`.
- `curl -k -I --resolve
  webui-tmp.aitherdev.int.vpsfree.cz:10443:127.0.0.1
  https://webui-tmp.aitherdev.int.vpsfree.cz:10443/`: passed with HTTP 200.
- `curl -k -I --resolve api-tmp.aitherdev.int.vpsfree.cz:10443:127.0.0.1
  https://api-tmp.aitherdev.int.vpsfree.cz:10443/`: passed with HTTP 200.
- `ssh -p 10022 root@127.0.0.1`: services VM reachable; nginx,
  `container@webui`, and `vpsadmin-api` active with no failed systemd units.
- `ssh -p 10122 root@127.0.0.1`: node1 reachable; `tank` pool active and
  `osctld`/`nodectld` running.
- In local network mode, browser testing needs the dev hostnames resolved to
  `127.0.0.1` and port `10443`, e.g.
  `https://webui-tmp.aitherdev.int.vpsfree.cz:10443/`.
- `ruby -c osvm/lib/osvm/machine_config.rb`: passed in the vpsadminos
  feature worktree.
- `ruby -c osvm/spec/osvm/machine_config_spec.rb`: passed in the vpsadminos
  feature worktree.
- `bundle exec rspec spec/osvm/machine_config_spec.rb` from the ambient shell
  failed because locally installed gems did not include `md2man`.
- `nix develop .#test-runner --command ...rspec...` failed because that shell
  resolved Ruby 3.3 while `osvm` now requires Ruby 3.4.
- `nix develop --command ...rspec...` with `BUNDLE_GEMFILE=osvm/Gemfile`
  installed OSVM dependencies but failed before examples because
  `libosctl/native` was not built in the worktree shell.
- Direct Ruby checks of `OsVm::MachineConfig::BridgeNetwork` passed:
  without helper it rendered `bridge,id=net0,br=br0`; with helper it rendered
  `bridge,id=net0,br=br0,helper=/run/wrappers/bin/qemu-bridge-helper`.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
  cluster/cz.vpsfree/machines/aitherdev/config.nix`: passed.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
  dev-clusters/vpsadmin/flake.nix dev-clusters/vpsadmin/nix/test.nix`:
  initially reported both files as not formatted; running `nixfmt` on those
  two files and rechecking passed.
- Re-ran `bash -n dev-clusters/vpsadmin/bin/devcluster` and
  `ruby -c dev-clusters/vpsadmin/lib/devcluster-runner.rb` after formatting:
  passed.
- `nix develop --command confctl ls | rg 'aitherdev|machines/aitherdev'`:
  passed and showed `cz.vpsfree/machines/aitherdev`.
- `nix develop --command confctl build cz.vpsfree/machines/aitherdev`: reached
  the interactive confirmation prompt, then exited on EOF.
- `nix develop --command confctl build -y cz.vpsfree/machines/aitherdev`:
  passed; built generation `2026-05-30--13-55-13`.
- `nix build --impure ...path:dev-clusters/vpsadmin#cluster-config` with
  `VPSADMIN_DEVCLUSTER_NETWORK=bridge` and vpsadminos overridden to the feature
  worktree: passed before and after formatting the devcluster Nix files, output
  `/nix/store/5crfhsmr4x434cdd86bpn71lb8yljrxk-os-test-vpsadmin-devcluster-2026-05-29-security-advisories.json`.
- `jq` inspection of that bridge cluster JSON showed both `services` and
  `node1` bridge networks include
  `{"helper":"/run/wrappers/bin/qemu-bridge-helper","link":"br0"}`.
- `git diff --check` passed in both the vpsadminos and
  vpsfree-cz-configuration feature worktrees.
- `/run/wrappers/bin/qemu-bridge-helper` is not present on the current running
  host generation yet, so actual bridge-mode boot remains pending until the
  `aitherdev` configuration is deployed/switched.
- Committed the `aitherdev` configuration change in
  `vpsfree-cz-configuration` as
  `76675f0a cluster: add qemu bridge helper on aitherdev`.
- Created a fresh temporary `master` worktree from current `origin/master`,
  fast-forwarded it with `git merge --ff-only
  2026-05-30-dev-vpsadmin-clusters`, and validated the merged target.
- In the fresh `master` worktree, `nix shell nixpkgs#nixfmt-rfc-style -c
  nixfmt --check cluster/cz.vpsfree/machines/aitherdev/config.nix`: passed.
- In the fresh `master` worktree, `nix develop --command confctl build -y
  cz.vpsfree/machines/aitherdev`: passed; built generation
  `2026-05-30--14-05-13`.
- Re-fetched `origin/master` before pushing; local `master` was exactly one
  commit ahead and zero behind.
- `git push origin master`: passed; pushed `a0e0f0ee..76675f0a` to
  `github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Removed the temporary `vpsfree-cz-configuration-master` merge worktree after
  pushing.
- After deploying `aitherdev`, verified host files:
  `/run/wrappers/bin/qemu-bridge-helper` exists as `root:wheel` with setuid
  permissions, and `/etc/qemu/bridge.conf` contains only `allow br0` and
  `allow virbr0`.
- Created a `vpsadmin` worktree for slug
  `2026-05-30-dev-vpsadmin-clusters` from current `origin/master` so the
  bridge verification cluster could use the existing vpsAdminOS worktree with
  OSVM helper support.
- `ping -c 1 -W 1 172.16.106.53` before bridge startup: no response, so the
  bridge service IP was free.
- `dev-clusters/vpsadmin/bin/devcluster start
  2026-05-30-dev-vpsadmin-clusters --topology single --network bridge`:
  passed; cluster is running with PID `252563`, topology `single`, network
  `bridge`, ready `yes`.
- `pgrep -af 'qemu-system|qemu-kvm'` confirmed both QEMU processes use
  `-netdev bridge,...,br=br0,helper=/run/wrappers/bin/qemu-bridge-helper`.
- DNS resolves `webui-tmp.aitherdev.int.vpsfree.cz` and
  `api-tmp.aitherdev.int.vpsfree.cz` to `172.16.106.53`.
- `ping -c 1 -W 2 172.16.106.53` and `ping -c 1 -W 2 172.16.106.41`: passed.
- `curl -k -I https://webui-tmp.aitherdev.int.vpsfree.cz/`: passed with
  HTTP 200.
- `curl -k -I https://api-tmp.aitherdev.int.vpsfree.cz/`: passed with HTTP 200.
- SSH to `172.16.106.53`: `systemctl is-active nginx container@webui
  vpsadmin-api` returned `active` for all three, and `systemctl --failed
  --no-legend` returned no failed units.
- SSH to `172.16.106.41`: `sv status /service/osctld /service/nodectld`
  reported both services running, `zpool list -H tank` showed pool `tank`
  online, and `osctl pool list` showed `tank` active.
- Corrected devcluster domain modeling after comparing with `vpsf-dev`:
  primary web UI domain is `webui.aitherdev.int.vpsfree.cz`; the
  `*-tmp.aitherdev.int.vpsfree.cz` domains are separate secondary frontend
  entries for maintenance/internal access.
- Found the browser reachability issue for `webui-tmp`: services VM had the
  QEMU user-network default route via `10.0.2.2`, so clients outside
  `172.16.106.0/24` could not get replies. Applied a live route fix and made
  bridge mode set the services VM default gateway to `172.16.106.1` on `eth1`.
- Added the same bridge-mode default route replacement to vpsAdminOS node
  networking setup so node VMs also route through the bridge network.
- Switched the running services VM after the domain/routing changes with
  `devcluster update 2026-05-30-dev-vpsadmin-clusters services`: passed.
- After the switch, `curl -k -I https://webui.aitherdev.int.vpsfree.cz/` and
  `curl -k -I https://webui-tmp.aitherdev.int.vpsfree.cz/`: both returned
  HTTP 200 and both served the PHP web UI.
- Renamed devcluster environment variables from `VPSFREE_DEVCLUSTER_*` to
  `VPSADMIN_DEVCLUSTER_*`. `rg` confirmed no remaining `VPSFREE_` references
  in `dev-clusters/vpsadmin` or this initiative's plan/state notes.
- Re-ran `nixfmt --check` for the devcluster Nix files and
  `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
- Re-ran `devcluster update 2026-05-30-dev-vpsadmin-clusters services` after
  the environment-prefix rename to validate the new `VPSADMIN_DEVCLUSTER_*`
  path: passed and copied zero paths.
- Updated internal DNS in `vpsfree-cz-configuration` so
  `api.aitherdev.int.vpsfree.cz`, `auth.aitherdev.int.vpsfree.cz`,
  `console.aitherdev.int.vpsfree.cz`, and `vnc.aitherdev.int.vpsfree.cz` all
  CNAME to `frontend.aitherdev.int.vpsfree.cz`, matching the existing primary
  `webui`/`download` records and `*-tmp` maintenance records. Bumped the
  `vpsfree.cz` internal zone serial to `2026053000`.
- `nix shell nixpkgs#bind -c named-checkzone vpsfree.cz
  configs/internal-dns/zone.vpsfree.cz.`: passed with the existing `@fqdn@`
  check-names warning and loaded serial `2026053000`.
- `git diff --check` in the vpsfree-cz-configuration feature worktree: passed.
- `nix develop --command confctl build -y
  'cz.vpsfree/containers/*/int.ns1' 'cz.vpsfree/containers/prg/int.mon*'`:
  passed for `cz.vpsfree/containers/brq/int.ns1` and
  `cz.vpsfree/containers/prg/int.ns1`; `confctl` only consumed the first target
  pattern in this invocation.
- `nix develop --command confctl build -y cz.vpsfree/containers/prg/int.mon1`:
  passed; built generation `2026-05-30--15-41-55`.
- `nix develop --command confctl build -y cz.vpsfree/containers/prg/int.mon2`:
  passed; built generation `2026-05-30--15-42-55`.
- Committed the DNS change in `vpsfree-cz-configuration` as
  `437ae501 dns: point aitherdev vpsadmin names to frontend`.
- Created a fresh temporary `master` worktree from current `origin/master`,
  fast-forwarded it with `git merge --ff-only
  2026-05-30-dev-vpsadmin-clusters`, and validated the merged target.
- In the fresh `master` worktree, `nix shell nixpkgs#bind -c named-checkzone
  vpsfree.cz configs/internal-dns/zone.vpsfree.cz.`: passed with the existing
  `@fqdn@` check-names warning and loaded serial `2026053000`.
- In the fresh `master` worktree, `nix develop --command confctl build -y
  'cz.vpsfree/containers/*/int.ns1'`: passed; built generation
  `2026-05-30--15-47-01` for `cz.vpsfree/containers/brq/int.ns1` and
  `cz.vpsfree/containers/prg/int.ns1`.
- In the fresh `master` worktree, `nix develop --command confctl build -y
  cz.vpsfree/containers/prg/int.mon1`: passed; built generation
  `2026-05-30--15-48-09`.
- In the fresh `master` worktree, `nix develop --command confctl build -y
  cz.vpsfree/containers/prg/int.mon2`: passed; built generation
  `2026-05-30--15-48-53`.
- Re-fetched `origin/master` before pushing; local `master` was exactly one
  commit ahead and zero behind.
- `git push origin master`: passed; pushed `76675f0a..437ae501` to
  `github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Login to `https://webui.aitherdev.int.vpsfree.cz/` initially failed before
  showing the credential form. The webui container nginx journal showed
  `HaveAPI\Client\Exception\ProtocolError: Invalid OAuth2 authorize_url: URL
  must use the configured API origin or a trusted OAuth2 origin`.
- Added `https://auth.aitherdev.int.vpsfree.cz` and
  `https://auth-tmp.aitherdev.int.vpsfree.cz` to the web UI's trusted OAuth2
  origins in the devcluster config.
- Found the running API still advertised
  `https://auth-tmp.aitherdev.int.vpsfree.cz/_auth/oauth2/authorize` because
  the persistent dev database had been initialized before the primary-domain
  seed correction. Manually reran the dev seed file on the services VM and
  restarted `vpsadmin-api`; the API then advertised the primary auth URL.
- Added a `vpsadmin-devcluster-seed.service` on the services VM. It runs after
  `vpsadmin-database-setup.service` and before `vpsadmin-api.service`, applying
  the dev seed overrides even when the database already exists.
- Updated `devcluster update <slug> services` to restart `vpsadmin-api` after
  switching when `vpsadmin-devcluster-seed.service` exists. The API restart
  pulls in the seed service through systemd dependencies, so URL seed changes
  are applied to existing dev databases.
- `devcluster update 2026-05-30-dev-vpsadmin-clusters services`: passed after
  adding the host-scoped dev seed service.
- Direct restart check confirmed `systemctl restart vpsadmin-api` reruns
  `vpsadmin-devcluster-seed.service` first; the seed invocation ID changed and
  `vpsadmin-api` returned to `active`.
- `curl -k -X OPTIONS https://api.aitherdev.int.vpsfree.cz/v7.0/` confirmed
  OAuth2 `authorize_url`, `token_url`, and `revoke_url` now use
  `https://auth.aitherdev.int.vpsfree.cz`.
- `curl -k -D - -X POST
  'https://webui.aitherdev.int.vpsfree.cz/?page=login&action=login'` now
  returns HTTP 302 to
  `https://auth.aitherdev.int.vpsfree.cz/_auth/oauth2/authorize...`, with no
  PHP 500 response.
- After submitting credentials, the web UI rendered `Authentication error:
  vpsAdmin was unable to obtain access token from the authorization server`.
  The callback returned HTTP 200 because the exception is caught by
  `webui/pages/page_login.php`, so nginx/PHP logs did not include the underlying
  token-exchange exception.
- Verified from inside the webui container that
  `curl https://auth.aitherdev.int.vpsfree.cz/_auth/oauth2/authorize` failed
  certificate validation with `unable to get local issuer certificate`. The
  server-side token request therefore never reached `/_auth/oauth2/token`.
- Added the devcluster CA certificate to `security.pki.certificateFiles` on the
  services VM and inside the webui container.
- Re-ran `devcluster update 2026-05-30-dev-vpsadmin-clusters services`: passed
  and switched the webui container with the trusted CA bundle.
- After the switch, the same curl from inside the webui container reached the
  auth endpoint over verified HTTPS and returned the expected HTTP 400 for a
  request without OAuth2 parameters, confirming TLS trust now works.
- Ran a full command-line OAuth2 login with a cookie jar using
  `test-admin` / `testAdminPassword`: auth returned a code, the web UI callback
  exchanged it for an access token, redirected to `?page=cluster`, and the final
  page showed `Logout (test-admin)`.
- HAProxy logs confirmed `POST /_auth/oauth2/token` returned HTTP 200 during
  that flow.

Open questions/limitations:

- First version targets one active VPN-visible cluster at a time because DNS/IPs
  are fixed.
- The web UI is live-mounted from source; Ruby services and vpsAdminOS node
  services require `devcluster update` to switch to rebuilt code.
- `devcluster update` currently builds the full cluster JSON, including disk
  image derivations, before copying only the selected machine toplevel. It works
  but should be optimized to build toplevels directly.
- Internal DNS changes are merged and pushed to `master`; they still need to be
  deployed to the internal DNS machines.

## Seeded storage, networking, users, and mail

- Added a reusable `dev-clusters/vpsadmin/default-config.json` model for
  inventory and seed data. It now covers service IPs, node IPs, primary and
  `-tmp` domains, topologies, mail capture, users, resource packages, pools,
  networks, IP addresses, and mail recipients.
- `devcluster start` copies the default config into the per-cluster directory on
  first use. `devcluster config <slug>` prints that path so a cluster can be
  customized without editing the default.
- The current cluster config is
  `.dev-clusters/vpsadmin/clusters/2026-05-30-dev-vpsadmin-clusters/config.json`.
  Its seed pool filesystem is `tank/ct`, which matches the node-side ZFS pool
  layout.
- Added a `vpsfree-mail-templates` worktree for this initiative at
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsfree-mail-templates`. The
  devcluster seed imports those templates from the worktree through the Nix
  closure, not a runtime virtiofs mount, so it works with an already-running
  cluster update.
- Added Mailpit to the `mailer` container. It receives SMTP on port `1025` and
  exposes the web/API UI on `http://172.16.106.53:8025/`.
- Seeded two non-admin users:
  `test-user1` / `testUser1Password` and
  `test-user2` / `testUser2Password`.
- Seeded a hypervisor pool, two networks, twenty IP addresses, default VPS
  resources, per-user resource packages, and a daily-report recipient
  `dev-admin@example.test`.
- Added `devcluster refresh <slug>`. It waits until the services database has a
  seeded pool, prepares node-side pool directories such as
  `/tank/ct/vpsadmin/config/vps` and `/tank/hook/ct`, then restarts nodectld so
  the node sees the seeded pool state. It runs automatically after cluster start
  and after a services update, and can be run manually.
- Found that database-seeded pools bypass the normal node transaction side
  effects. Without `devcluster refresh`, nodectld can have an empty pool cache
  or miss the vpsAdmin pool working directories.
- Found that VPS creation also exposed a vpsAdmin-side nodectld issue:
  `CtHookInstaller` copied hooks into `/tank/hook/ct/<vps-id>/` without creating
  that per-container directory.
- Patched `libnodectld/lib/nodectld/ct_hook_installer.rb` in the vpsAdmin
  worktree to create the hook directory, and added
  `libnodectld/spec/nodectld/ct_hook_installer_spec.rb` for the behavior.
- `nix develop .#libnodectld -c bundle exec rspec
  spec/nodectld/ct_hook_installer_spec.rb` did not run because the libnodectld
  spec helper requires a configured test database:
  `No test DB configured. Set DATABASE_URL or create api/config/database.yml
  with a 'test:' section.`
- Ran `nix develop -c rake vpsadmin:gems` in the vpsAdmin worktree to rebuild
  packaged nodectl/nodectld/libnodectld gems. It produced build id
  `20260530174802` and updated generated files under
  `packages/libnodectld`, `packages/nodectl`, and `packages/nodectld`.
- Ran `dev-clusters/vpsadmin/bin/devcluster update
  2026-05-30-dev-vpsadmin-clusters node1` after the gem rebuild. The update
  copied the rebuilt `libnodectld`, `nodectld`, and `nodectl` packages and
  restarted nodectld.
- `dev-clusters/vpsadmin/bin/devcluster refresh
  2026-05-30-dev-vpsadmin-clusters`: passed; it waited for pool `tank/ct`,
  prepared node1, and restarted nodectld.
- Database verification on services showed users `test-admin`, `test-user1`,
  and `test-user2`; pool `tank` with filesystem `tank/ct`; two networks; twenty
  IP addresses; and 52 installed mail templates.
- Mail recipient verification showed `Dev admins` with recipient
  `dev-admin@example.test` linked to `daily_report`.
- Sent a fresh daily report with
  `bundle exec rake vpsadmin:mail_daily_report` in the running API closure.
  Mailpit then reported one accepted message to `dev-admin@example.test` from
  `vpsadmin@vpsfree.cz` with subject `vpsAdmin daily report 29/05/2026`.
- Created a VPS as `test-user1` on node1 with:
  `vpsadminctl --raw --timeout 240 vps new -- --user 2 --node 101
  --os-template 1 --hostname dev-seed-check4 --cpu 1 --memory 1024 --swap 512
  --diskspace 4096 --ipv4 1 --ipv4-private 0 --ipv6 0 --no-start`.
  The action completed successfully.
- Runtime verification for that VPS showed API VPS id `5`, assigned IPv4
  `198.51.100.10`, osctld container `tank:5` in the stopped state, ZFS dataset
  `tank/ct/5`, generated config `/tank/ct/vpsadmin/config/vps/5.yml`, and hook
  `/tank/hook/ct/5/veth-up`.
- Final health check:
  `devcluster status 2026-05-30-dev-vpsadmin-clusters` reports `running` and
  `ready: yes`; services `vpsadmin-api`, `container@webui`,
  `container@mailer`, and `nginx` are active; node1 `/service/osctld` and
  `/service/nodectld` are running.

Open follow-ups:

- The vpsAdmin worktree now contains both the nodectld functional fix and the
  generated gem package updates. If this is kept, split them into separate
  commits per repository policy.
- Add a smoother way to run API/libnodectld specs in this workspace, or document
  the required test database setup.

## Mailpit HTTPS frontend

- Added `mailpit.aitherdev.int.vpsfree.cz` to the devcluster configurable
  domain map and exposed Mailpit through the services nginx HTTPS frontend.
- Added configurable Mailpit basic-auth seed values under
  `mail.capture.webAuth`; the current credentials are
  `mailpit` / `mailpitPassword`.
- Changed Mailpit to listen on `127.0.0.1:8025` inside the services VM, so the
  raw HTTP listener is no longer exposed on `172.16.106.53:8025`.
- Updated `devcluster urls <slug>` to print the HTTPS Mailpit URL and its
  development basic-auth credentials.
- Changed certificate generation to derive SANs from configured
  `domains`/`tmpDomains`, so new configured service names such as Mailpit are
  covered automatically.
- The imported `vpsf-dev` CA key is encrypted. Since the CA passphrase is not
  available to unattended tooling, the running cluster generated a fresh
  workspace-local devcluster CA and reissued the leaf certificate with SAN
  `mailpit.aitherdev.int.vpsfree.cz`.
- The new devcluster CA is at
  `.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`; its SHA-256
  fingerprint is
  `1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`.
- Added support for `VPSADMIN_DEVCLUSTER_CA_PASSPHRASE` so a user can reissue
  from an encrypted imported CA instead of falling back to a fresh CA.
- Deployed the updated services VM twice: first for the Mailpit HTTPS/auth
  frontend, then for the final domain-map cleanup that made
  `frontend.aitherdev.int.vpsfree.cz` configurable.
- Verification with an explicit host resolution showed:
  unauthenticated `https://mailpit.aitherdev.int.vpsfree.cz/` returns HTTP 401;
  `mailpit:mailpitPassword` returns HTTP 200; and
  `http://172.16.106.53:8025/` times out from outside the services VM.
- Services verification showed no failed units, with `nginx`,
  `container@mailer`, `container@webui`, and `vpsadmin-api` active. `ss` showed
  Mailpit listening only on `127.0.0.1:8025`.
- Added internal DNS record
  `mailpit.aitherdev.int CNAME frontend.aitherdev.int.vpsfree.cz.` in
  `vpsfree-cz-configuration` and bumped the zone serial to `2026053001`.
- `nix shell nixpkgs#bind -c named-checkzone vpsfree.cz
  configs/internal-dns/zone.vpsfree.cz.` passed with the existing `@fqdn@`
  check-names warning and loaded serial `2026053001`.
- `nix develop --command confctl build -y
  'cz.vpsfree/containers/*/int.ns1'` passed in both the feature worktree and
  the fresh fast-forward merge worktree; it built
  `cz.vpsfree/containers/brq/int.ns1` and
  `cz.vpsfree/containers/prg/int.ns1`.
- Committed the DNS change in `vpsfree-cz-configuration` as
  `cf5903c9 dns: add aitherdev mailpit name`.
- Fast-forwarded a fresh merge worktree from `origin/master`, revalidated the
  DNS zone and ns1 builds there, and pushed `cf5903c9` to
  `github.com:vpsfreecz/vpsfree-cz-configuration.git` `master`.
- Removed the temporary merge worktree after pushing.

## Authoritative DNS in the devcluster

- Added configurable devcluster DNS server inventory under `dns.servers` in
  `dev-clusters/vpsadmin/default-config.json` and the active cluster config.
  The default running topology now includes:
  - hidden primary `dns-primary` / `dev-dns-primary` at `172.16.106.61`,
    vpsAdmin DNS name `ns-hidden.aitherdev.int.vpsfree.cz`;
  - public secondary `dns-secondary` / `dev-dns-secondary` at
    `172.16.106.62`, vpsAdmin DNS name
    `ns-public.aitherdev.int.vpsfree.cz`.
- Reused vpsAdmin's existing
  `tests/configs/nixos/vpsadmin-dns-server.nix` module for the DNS machines,
  so the runtime is BIND plus nodectld processing normal vpsAdmin DNS
  transactions.
- Changed `devcluster` topology expansion so enabled DNS servers are started
  in addition to the selected node topology. `machine_ip`, `ssh`, local SSH
  forwarding, RabbitMQ node users, socket peers, and generated `/etc/hosts`
  now include configured DNS machines.
- Made devcluster SSH ignore per-VM host keys via `/dev/null` known-hosts.
  QEMU VMs are ephemeral enough that persisted host keys caused post-restart
  refresh failures after a root image changed.
- Extended the seed to upsert `DnsServer` rows, create confirmed internal
  reverse zones for seed networks with `reverseZone = true`, attach each zone
  to the configured DNS servers, and refresh existing `IpAddress` reverse-zone
  links. Existing IPs such as `198.51.100.10` now have
  `reverse_dns_zone_id` assigned.
- The current seeded reverse zones are:
  `100.51.198.in-addr.arpa.` for `198.51.100.0/24` and
  `0.106.10.in-addr.arpa.` for `10.106.0.0/24`.
- Ran `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt
  dev-clusters/vpsadmin/nix/test.nix` and
  `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
- Ran `devcluster update 2026-05-30-dev-vpsadmin-clusters services` after the
  DNS seed changes. It built the new generated cluster config, switched the
  services VM, and the seed completed successfully.
- Restarted the running bridge cluster so the new DNS VMs were launched.
  `devcluster status 2026-05-30-dev-vpsadmin-clusters` reports `running`,
  topology `single`, network `bridge`, ready `yes`, PID `470082`.
- Ran `devcluster refresh 2026-05-30-dev-vpsadmin-clusters` after fixing the
  SSH known-host handling: passed.
- Verified on both DNS VMs that `bind` and `vpsadmin-nodectld` are active.
  Primary has zone files under `/var/named/vpsadmin/primary_type/`; secondary
  has transferred zone files under `/var/named/vpsadmin/secondary_type/`.
- Database verification showed all four reverse `DnsServerZone` links
  confirmed: both zones on hidden primary as `primary_type` and both zones on
  public secondary as `secondary_type`.
- DNS query verification:
  `dig @172.16.106.61 SOA 100.51.198.in-addr.arpa +short` and
  `dig @172.16.106.62 SOA 100.51.198.in-addr.arpa +short` both return serial
  `2` after transfer.
- PTR workflow verification used
  `TransactionChains::DnsZone::SetReverseRecord.fire` for host IP
  `198.51.100.10`, setting
  `10.100.51.198.in-addr.arpa. PTR dev-seed-check4.example.test.`.
  The transaction chain reached state `done`, and both
  `dig @172.16.106.61 PTR 10.100.51.198.in-addr.arpa +short` and
  `dig @172.16.106.62 PTR 10.100.51.198.in-addr.arpa +short` return
  `dev-seed-check4.example.test.`.
- Added internal DNS records in `vpsfree-cz-configuration`:
  `ns-hidden.aitherdev.int A 172.16.106.61` and
  `ns-public.aitherdev.int A 172.16.106.62`.
- `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.` passed
  with the existing `@fqdn@` check-names warning and loaded serial
  `2026053001`.
- `nix develop -c confctl build -y 'cz.vpsfree/containers/*/int.ns1'` passed;
  it built `cz.vpsfree/containers/brq/int.ns1` and
  `cz.vpsfree/containers/prg/int.ns1`, generation
  `2026-05-30--19-17-17`.
- Committed and pushed the internal DNS records to `vpsfree-cz-configuration`
  `master` as `6d223481 dns: add aitherdev devcluster nameservers`.
- After adding DNS server names to generated host maps, switched the running
  `dns-primary` and `dns-secondary` VMs with `devcluster update`; both switches
  copied only small `/etc/hosts`/system closure updates and completed
  successfully.

## Node status seed issue

- Investigated `dev-node1.lab` showing down in vpsAdmin with kernel
  `devcluster`.
- Verified the node VM was alive at `172.16.106.41`, `osctld` and `nodectld`
  were running, and RabbitMQ had an active `dev-node1.lab` connection.
- Found `vpsadmin-supervisor` rejecting every node status message with
  `Mysql2::Error: Unknown column 'NaN' in 'VALUES'`.
- The `NaN` was produced inside the API, not by the node payload: the
  devcluster seed created a placeholder `node_current_statuses` row with
  `update_count = 0`. On the first real status update, supervisor logging
  divided existing rolling-average sums by `update_count`, yielding `NaN` and
  preventing the placeholder `kernel = devcluster` from being overwritten.
- Fixed `api/lib/vpsadmin/supervisor/node/status.rb` to reset invalid rolling
  average state when `update_count <= 0` before logging.
- Added an API spec covering a seeded status row with `update_count = 0`.
- Changed the devcluster seed to create placeholder node statuses with
  `update_count = 1` instead of `0`.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
  dev-clusters/vpsadmin/nix/test.nix`: passed.
- `DATABASE_URL=mysql2://vpsadmin_spec:vpsadmin_spec@127.0.0.1:13306/vpsadmin_status_spec
  bundle exec rspec spec/supervisor/node/status_spec.rb` inside
  `nix develop .#api`: passed, 5 examples, 0 failures. The database was a
  throwaway DB reached through an SSH tunnel to the services VM; the temporary
  DB and user were removed afterwards.
- Ran `devcluster update 2026-05-30-dev-vpsadmin-clusters services`: passed,
  switched the services VM, ran the seed, refreshed node pool runtime, and
  restarted `nodectld`.
- Verified `node_current_statuses` for node `101` now updates successfully:
  at `2026-05-30 17:58:18 UTC`, `updated_at = 2026-05-30 17:58:04`,
  `age_s = 14`, `kernel = 6.12.91`, `vpsadmin_version = 4.1.0`, and
  `update_count = 5`.
- Verified no `vpsadmin-supervisor` warnings/errors after the fixed supervisor
  start at `2026-05-30 17:56:56 UTC`.

## Fresh-state devcluster smoke

- Question checked: whether deleting cluster state and starting from scratch
  seeds DNS, users, storage, networks, IPs, mail templates, and node runtime
  correctly for each feature devcluster.
- Created temporary detached smoke worktrees under
  `worktrees/2026-05-30-devcluster-fresh-smoke/` for `vpsadmin`,
  `vpsadminos`, and `vpsfree-mail-templates`.
- Stopped the old local-mode `2026-05-29-security-advisories` cluster to free
  localhost forwards used by the smoke cluster.
- First fresh start of `2026-05-30-devcluster-fresh-smoke` in local/single
  mode exposed a race in `devcluster refresh`: services had seeded pool
  `tank/ct`, but node `tank` was not yet importable, so the refresh failed
  with `cannot create 'tank/ct/vpsadmin': no such pool 'tank'`.
- Fixed `dev-clusters/vpsadmin/bin/devcluster` to wait up to 180 seconds for
  the node-side ZFS pool before creating `tank/ct/vpsadmin` runtime datasets.
- Second fresh start passed the pool refresh.
- Fresh seed verification showed:
  - users `test-admin`, `test-user1`, and `test-user2`;
  - pool `tank/ct` on node `101` with current space metrics;
  - public `198.51.100.0/24` and private `10.106.0.0/24` networks;
  - 20 `ip_addresses` and 20 `host_ip_addresses`;
  - 52 `mail_templates` and 94 translations from the template worktree;
  - hidden primary `ns-hidden.aitherdev.int.vpsfree.cz` and public secondary
    `ns-public.aitherdev.int.vpsfree.cz`;
  - reverse zones `100.51.198.in-addr.arpa.` and `0.106.10.in-addr.arpa.`;
  - all primary/secondary `dns_server_zones` confirmed.
- Tested a real PTR mutation with
  `TransactionChains::DnsZone::SetReverseRecord.fire2` for host IP
  `198.51.100.10`, setting
  `fresh-smoke-ptr.aitherdev.int.vpsfree.cz.`. The primary updated to serial
  `2`, but the secondary initially stayed on serial `1`: the hidden primary
  allowed AXFR, but did not explicitly notify the secondary by IP.
- Fixed `libnodectld/lib/nodectld/dns_config.rb` to render
  `also-notify { <secondary-ip>; };` for internal primary zones with
  configured secondaries.
- Added `libnodectld/spec/nodectld/dns_config_spec.rb` coverage for internal
  primary `also-notify` rendering.
- `nix develop .#libnodectld -c bundle exec rspec
  spec/nodectld/dns_config_spec.rb` did not run examples because the component
  spec helper requires a configured test DB; no local test DB was configured.
- Rebuilt and published vpsAdmin node gems with
  `OS_BUILD_ID=25.11.0.build20260524195326
  VPSADMIN_BUILD_ID=20260530204700 nix develop . -c rake vpsadmin:gems`.
  Running the same command with `VPSADMINOS_PATH` set failed because the local
  vpsAdminOS gemspecs expected the timestamp suffix in `OS_BUILD_ID`, while
  vpsAdmin's packaged gemspec dependencies need the full published gem
  version.
- Repeated the fresh smoke start with the repackaged
  `libnodectld/nodectld/nodectl` gems. Primary `named.conf` now contains
  `also-notify { 172.16.106.62; };` for both reverse zones.
- Repeated the PTR mutation. Both authoritative servers answered
  `10.100.51.198.in-addr.arpa PTR
  fresh-smoke-ptr.aitherdev.int.vpsfree.cz.` and both returned SOA serial `2`.
  Secondary BIND logs show it received notify from `172.16.106.61` and
  transferred serial `2`.
- Ran `VpsAdmin::API::Tasks::Dns.new.check_reverse_records` inside the
  services VM: `2 records ok`, `0 dns errors`, `0 records incorrect`.
- Node/runtime verification after the fresh start:
  - `dev-node1` has `tank ONLINE 19.5G`;
  - `osctld` and `nodectld` are running on node1;
  - `bind` and `vpsadmin-nodectld` are active on both DNS VMs;
  - `node_current_statuses` for node1 has kernel `6.12.91` and
    `update_count = 5`, not the placeholder `devcluster` kernel.
- Ran `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
- Ran `git -C worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadmin diff
  --check`: passed.
- Ran `git diff --check -- dev-clusters/vpsadmin/bin/devcluster
  work/2026-05-30-dev-vpsadmin-clusters/state.md
  notes/cross-project/2026-05-30-devcluster-fresh-state-smoke.md
  notes/vpsadmin/2026-05-30-internal-primary-dns-notify.md`: passed.
- Cleaned up the temporary smoke cluster with
  `devcluster reset 2026-05-30-devcluster-fresh-smoke` and removed the three
  temporary smoke worktrees.
- The main bridge devcluster remains running:
  `devcluster status 2026-05-30-dev-vpsadmin-clusters` reports topology
  `single`, network `bridge`, ready `yes`, PID `470082`.

## Web UI post-login 500 and plugin config

- Reported on 2026-05-31: after logging in as `test-admin`, the web UI at
  `https://webui.aitherdev.int.vpsfree.cz/?page=` returned HTTP 500.
- Webui PHP logs showed the fatal error came from
  `list_transaction_chains()` calling the API `transaction_chain index` action.
- API logs showed ActiveRecord STI failing to load persisted transaction-chain
  type `DevclusterDnsRefresh`. This was a one-off class used by the DNS refresh
  maintenance script; normal API workers do not load that script, so rows with
  its class name in `transaction_chains.type` break transaction-chain listing.
- The dev DB also had a payments plugin chain from the scheduled
  `vpsadmin-api-payments-report.service`. After restarting the API with all
  plugins enabled, restoring that row to
  `VpsAdmin::API::Plugins::Payments::TransactionChains::MailOverview` worked,
  confirming the API process can load plugin chain classes when the plugin set
  is enabled.
- Runtime DB cleanup:
  - changed custom one-off chain rows `DcDnsRefresh` and
    `DevclusterDnsRefresh` to a loadable existing chain type so the dashboard
    can list recent transactions;
  - restored the payments mail overview row to its real plugin chain class.
- Verification:
  - `vpsadminctl --raw transaction_chain list -- limit=3` succeeds through the
    running API and shows the payments row with label `Mail overview`;
  - anonymous `curl -k -I https://webui.aitherdev.int.vpsfree.cz/?page=`
    returns HTTP 200;
  - no new API or webui PHP fatal errors appeared after the API restart.
- Implemented devcluster-owned plugin configuration:
  - `dev-clusters/vpsadmin/default-config.json` now contains
    `"plugins": { "enabled": "all" }`;
  - `dev-clusters/vpsadmin/nix/test.nix` resolves `"all"` to every plugin
    directory bundled in the selected vpsAdmin worktree, supports `"none"` and
    explicit lists, and forces the resolved list into both services and the
    webui container;
  - the running cluster's ignored `config.json` was backfilled with
    `plugins.enabled = "all"` and the current resolver defaults so
    `devcluster config` exposes the setting.
- Re-ran `devcluster update 2026-05-30-dev-vpsadmin-clusters services`;
  the effective toplevel stayed the same because the base test config already
  enabled the same six plugins, but the devcluster config now owns that choice.
- Committed the vpsAdmin DNS-server forwarder option as
  `e398a8c32 tests: allow DNS server forwarders`.

## Bridge cluster DNS runtime update

- Updated running bridge DNS VMs to the rebuilt vpsAdmin node package:
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters dns-primary`
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters dns-secondary`
- Both switches copied `libnodectld`, `nodectld`, and `nodectl`
  `4.1.0.build20260530204700` and restarted `vpsadmin-nodectld`.
- Existing bridge zones had been rendered by the old package. Restarting
  `nodectld` does not rewrite every persisted zone config, so queued a
  one-off `DcDnsRefresh` transaction chain (`id=8`) that sent
  `DnsServerZone::Update` plus `DnsServer::Reload` for all four server-zone
  rows. Chain `8` completed with state `done`.
- Verified `dev-dns-primary:/var/named/vpsadmin/named.conf` now contains
  `also-notify { 172.16.106.62; };` for both reverse zones.
- Set a real PTR through
  `TransactionChains::DnsZone::SetReverseRecord.fire2` for host IP
  `198.51.100.10` to `bridge-ptr.aitherdev.int.vpsfree.cz.`. Chain `9`
  completed with state `done`.
- Verified both authoritative servers answer:
  `10.100.51.198.in-addr.arpa PTR bridge-ptr.aitherdev.int.vpsfree.cz.`.
  Both primary and secondary return SOA serial `3` for
  `100.51.198.in-addr.arpa.`.
- Secondary BIND logs show notify from `172.16.106.61`, transfer of serial
  `3`, and transfer status `success`.
- Ran `VpsAdmin::API::Tasks::Dns.new.check_reverse_records` inside the
  services VM: `2 records ok`, `0 dns errors`, `0 records incorrect`.
- Rechecked the production comparison after the operator pointed out that
  `ns0`/`ns3`/`ns4` works without explicit `also-notify`. The devcluster
  difference is name resolution: on `dev-dns-primary`, `getent hosts
  ns-public.aitherdev.int.vpsfree.cz` resolves from `/etc/hosts`, but DNS
  lookup with `host ns-public.aitherdev.int.vpsfree.cz` returns NXDOMAIN. BIND
  notify target lookup is DNS-based, while production nameserver names are real
  DNS names. The `also-notify` change therefore masks a devcluster
  DNS-name-resolution gap; it is not required to explain production behavior.

## Devcluster resolver correction

- Replaced the temporary `libnodectld` `also-notify` workaround with a generic
  devcluster resolver model.
- Removed the `libnodectld/lib/nodectld/dns_config.rb` change, its spec
  addition, and the generated `packages/{libnodectld,nodectl,nodectld}` gem
  pin changes for build `4.1.0.build20260530204700`. The vpsAdmin worktree now
  only carries the DNS-server Nix forwarder option from this DNS fix, plus
  unrelated pre-existing status/hook-installer changes.
- Added `resolver` config to `dev-clusters/vpsadmin/default-config.json`:
  default mode `cluster`, upstream nameservers `172.16.9.90` and
  `172.19.9.90`.
- In `dev-clusters/vpsadmin/nix/test.nix`, `resolver.mode = "cluster"` runs
  dnsmasq on the services VM. It serves all generated `devHosts` records and
  forwards misses to `resolver.upstreamNameservers`. Other VMs use
  `172.16.106.53` as resolver. Modes `upstream`, `gateway`, and `none` are
  also supported.
- Extended `tests/configs/nixos/vpsadmin-dns-server.nix` with
  `vpsadmin.test.dnsServer.forwarders`. The devcluster DNS VMs set BIND
  forwarders to the services resolver so named can resolve SOA/NS notify
  targets through DNS.
- Updated the running bridge cluster in place:
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters services`
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters node1`
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters dns-primary`
  - `devcluster update 2026-05-30-dev-vpsadmin-clusters dns-secondary`
- Verification after the switch:
  - services `dnsmasq` is active and `/etc/resolv.conf` uses `127.0.0.1`;
  - services resolves `ns-public.aitherdev.int.vpsfree.cz` to
    `172.16.106.62` via `127.0.0.1`;
  - DNS VMs use `172.16.106.53` in `/etc/resolv.conf`;
  - BIND config on both DNS VMs contains `forwarders { 172.16.106.53; };`;
  - after a one-off `DevclusterDnsRefresh` transaction, primary
    `/var/named/vpsadmin/named.conf` has no `also-notify` lines.
- Set host IP `198.51.100.10` PTR to
  `bridge-resolver-ptr.aitherdev.int.vpsfree.cz.`. Both authoritative servers
  answered the new PTR and both returned SOA serial `4` for
  `100.51.198.in-addr.arpa.`.
- Secondary BIND logs show notify from `172.16.106.61`, transfer of serial
  `4`, and transfer status `success`.
- Ran `VpsAdmin::API::Tasks::Dns.new.check_reverse_records` inside the
  services VM through `vpsadmin-api-ruby`: `2 records ok`, `0 dns errors`,
  `0 records incorrect`.
- The main bridge devcluster remains running:
  `devcluster status 2026-05-30-dev-vpsadmin-clusters` reports topology
  `single`, network `bridge`, ready `yes`, PID `470082`.
