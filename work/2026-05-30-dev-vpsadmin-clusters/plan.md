# Dev vpsAdmin clusters

Goal: implement a workspace-local way to run branch-selected vpsAdmin development
clusters for inspection, with isolated state per feature slug, useful seeded data,
HTTPS access over the existing aitherdev VPN/DNS setup, and a hybrid runtime
update path.

Affected components:

- coordination workspace: add `dev-clusters/vpsadmin/` tooling and docs;
- vpsadmin: consumed as a source worktree and reused for test modules/seeds, but
  not changed in the first implementation unless necessary;
- vpsadminos: extend OSVM bridge network rendering with an optional QEMU bridge
  helper path;
- vpsfree-cz-configuration: add the restricted `qemu-bridge-helper` wrapper on
  `cz.vpsfree/machines/aitherdev` and point aitherdev vpsAdmin internal DNS
  names at the dev frontend address.

Approach:

- leave `~/workspace/vpsf-dev` untouched;
- build new helpers in this workspace that select feature worktrees by slug;
- store generated QEMU state/certs/results under `.dev-clusters/`;
- use the existing `aitherdev` VPN-reachable dev network for the first active
  cluster and require explicit reset/stop before reusing clashing fixed IPs;
- expose primary and `-tmp` aitherdev vpsAdmin names through internal DNS,
  with both sets pointing at the dev frontend service IP;
- provide topology choices: single, dual, storage;
- run webui from mounted source, while API/nodectld/osctld/Nix changes use
  rebuild plus switch;
- make bridge mode work for unprivileged development by using QEMU's bridge
  helper through `/run/wrappers/bin/qemu-bridge-helper`, with `/etc/qemu/bridge.conf`
  continuing to allow only `br0` and `virbr0`.

Implemented shape:

- `dev-clusters/vpsadmin/bin/devcluster` is the operator entry point;
- `dev-clusters/vpsadmin/flake.nix` builds an OSVM/test-runner JSON config from
  selected worktrees using flake input overrides;
- `dev-clusters/vpsadmin/nix/test.nix` reuses vpsAdmin/vpsAdminOS test modules,
  adds deterministic dev nodes, per-slug writable services state, HTTPS
  frontend domains, mail capture, configurable seed data, and a generated seed
  file;
- `dev-clusters/vpsadmin/lib/devcluster-runner.rb` starts/stops the OSVM
  machines and keeps a ready marker for the shell helper;
- `dev-clusters/vpsadmin/default-config.json` is the reusable default inventory
  and seed model; each cluster gets a copied config under `.dev-clusters/` that
  can be edited for service IPs, node IPs, domains, users, pools, networks,
  addresses, resource packages, mail recipients, and topology membership;
- the seed imports `vpsfree-mail-templates` when that worktree exists, configures
  Mailpit as the development SMTP sink, exposes its UI through the HTTPS
  frontend with development basic auth, and seeds non-admin users with usable
  resource packages;
- the seed creates a simplified authoritative DNS topology with one hidden
  primary and one public secondary, and creates reverse zones for configured
  vpsAdmin seed networks so host IP PTR workflows can be tested;
- `devcluster refresh <slug>` reconciles node-side pool directories after a
  database seed and restarts nodectld so the running node sees seeded pools;
- `.dev-clusters/` holds ignored runtime state, SSH keys, imported/generated
  certificates, VM disks, logs, and result links;
- bridge-mode machine JSON passes `opts.helper` to OSVM by default, configurable
  with `VPSADMIN_DEVCLUSTER_BRIDGE_HELPER`.

Compatibility:

- production systems are not modified;
- dev database state is per slug, so feature migrations do not cross-contaminate;
- old and new code can be compared by starting different slugs sequentially;
- one active VPN-visible bridge cluster is supported initially because DNS/IP
  names are fixed;
- local QEMU networking supports one active localhost-forwarded cluster per
  slug/port set without bridge privileges;
- the OSVM `opts.helper` field is optional, so existing bridge configurations
  that only specify `opts.link` keep rendering the same QEMU arguments;
- the setuid bridge helper is limited to `root:wheel`, and QEMU's own bridge
  allowlist remains restricted by `/etc/qemu/bridge.conf`.

Testing plan:

- run shell syntax checks for helper scripts;
- run Nix parsing/evaluation checks for cluster definitions where possible;
- verify certificate import/init paths without committing private keys;
- record commands and any limitations in `state.md`.

Runtime expectation:

- web UI files are served from a symlink tree backed by the selected vpsAdmin
  worktree, with Composer/vendor content from the Nix package;
- Ruby services and node-side changes are rebuilt and deployed into a running
  cluster with `devcluster update <slug> [machine|all]`;
- `devcluster config <slug>` prints the per-cluster JSON config path;
- `devcluster urls <slug>` prints HTTPS endpoints, Mailpit, and seeded login
  credentials;
- `devcluster reset <slug>` removes the per-slug VM state, including the
  persistent development database.
