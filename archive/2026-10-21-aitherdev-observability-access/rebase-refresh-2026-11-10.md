# Configuration preparation, 2026-11-10

Package A is mechanical rebase and local preparation only. No build, push,
activation, credential provisioning, integration or lifecycle action is included.
Deployment status of earlier user-operated versions remains unknown/user-owned.
Reusable procedures stay in the configuration repository's two operations pages;
individual source/input/build/generation and rollout evidence belongs here.

## Saved identities and ancestry gate

- Canonical feature worktree: `worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration`.
- Old base: `c040c14cdbacc07998700b524996a89306188d7f`.
- Old published/local head and future lease: `98384b6b12fbc61c4df7c545d070cea446cc89bd`.
- Old tree: `51c606cbfec041e25b5b267216da6262e18708e5`.
- Fresh actual default: `refs/heads/master` at `0f3897b5b7dc53edee33f1289cbda25ec28910f5`.
- Fresh canonical SSH fetch was scoped to actual default and own feature only.
  The prior base is an ancestor of the target; none of the three feature commits
  is an ancestor of the target. The target adds 27 upstream commits. Feature
  worktree/index were clean, with active hooks and retained Sol/xhigh/write access.

## Reconstruction before rebase

Applying the complete old feature patch to the fresh target in a private temporary
Git index produced only three registration conflicts: README, flake checks and
MkDocs navigation. Application patches applied cleanly. Preserve the new grouped
README structure and append the old feature link paragraph under Operations;
insert both old feature check blocks and navigation entries alongside all new
upstream registrations. This keeps the feature text/expressions unchanged.

An independent aggregate-patch reconstruction with those explicit resolutions,
before changing the feature worktree, produced expected tree
`8bdfa6b5b7ada0201caed2dcd9cbdb7faaca7814`. Final replay must match it. This
is not a claim of entirely conflict-free replay or unchanged input identities.

## Inherited baseline risks

`flake.lock` changes seven nodes: codex-web, devWorkspace, vpsadminServices,
vpsadminWebui, vpsadminosOsStaging, vpsadminosStaging and vpsfreeWeb. Confctl,
nixpkgs, Gemfile/lock, gemset and hook configuration are unchanged. Exact changed
locked revisions/hashes are available in the saved old/new Git ranges.

The logger's production source is unchanged upstream. Proxy now imports a
separate blog module, adds the blog.vpsfree.org vhost, and changes blog headers
and upload routing. Thus a whole-host proxy activation can change unrelated blog
behavior. Source equivalence alone does not establish live-to-candidate service
effects; exact generation and service comparison remains a later deployment gate.
No migrations are present in the three-commit feature series, and persisted log
metadata/runtime credential recovery contracts remain supported.

## Frozen deliverable

Mechanical replay finished at `54b4f2737461ecca88d4e62c68df5e89f6f01ea9`,
whose tree exactly matched the pre-rebase reconstruction above. The architect's
focused proxy comparison checkpoint, after the lead's prose pass, was folded
into the owning docs commit with active pinned hooks and a temporary `-F` message.
Final head is `959e1d54cabc7ac5530dac6179acacb077a57754`, final tree
`d12a1746a0d11506559b5dc98c1b3105e1bd7fec`. The only delta from mechanical
replay is that proxy-guide paragraph and the split dry-activate/switch fence.

Final three-commit series above the new base:

1. `6f65dd5383643c27bcc7d33fe1b882c8b8981675` — logger.
2. `27868feec96aafa6cd458a6e919e5081fead4e4c` — proxy and shared registrations.
3. `959e1d54cabc7ac5530dac6179acacb077a57754` — operations guides.

Complete feature diff: 15 files, 1,577 insertions, 6 deletions. No migrations,
pin-update stream or obsolete feature commits remain. The complete lock graph is
bound by old lock blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86` and new lock
blob `9b6b86a9000a4411bb82c9623c3762f096d3325e`; the final lock equals the
new default's lock exactly. Mechanical source equivalence does not certify the
new guide paragraph or whole-host deployment effects; those need current review.

Quick checks at the clean committed head passed: 8 Nix format checks, 3 Python
ASTs, 17 shell snippets, MkDocs YAML, local links/shared registrations and diff
whitespace. Required pre-commit/commit-msg hooks passed; TextWidth emitted only
advisories for lines within the repository's 80-character limit.

Bounded evaluation returned the same derivations as the successful Nov2 receipts:

- Logger quick: `/nix/store/qx9n6649x74nm2pyx5pa1zdg4f75rbc9-log-reader-policy.drv`.
- Proxy quick: `/nix/store/378j6ca197c94gj4c47jbf0q2mnyfh6a-prometheus-query-access.drv`.
- Logger VM: `/nix/store/wgr200pz1sm8mr6svx0jk5672109n52y-vm-test-run-log-reader-access.drv`;
  exact identity appears in the successful Nov2 recovery log.
- Proxy integration: `/nix/store/jv9pghphqs0qb8aafyk34bvnqmaa2z3w-prometheus-query-access-integration.drv`.

All four output paths currently fail local store-validity checks; no fresh test
pass or retained realized artifact is claimed. No build or integration ran here.

## Prepared native plan commands, not executed

Pinned CLI help/source confirms these forms for either exact target
`cz.vpsfree/containers/prg/int.log` or `cz.vpsfree/containers/prg/proxy`:

```sh
confctl generation ls --local --remote "$TARGET"
confctl build --yes "$TARGET"
confctl generation ls --local "$TARGET"
confctl deploy --copy-only --generation "$GENERATION" "$TARGET"
confctl deploy --generation "$GENERATION" "$TARGET" dry-activate
confctl deploy --generation "$GENERATION" "$TARGET" switch
```

`GENERATION` is the retained local build name, not numeric remote profile 148/142.
`--copy-only` returns after closure copy, before activation. `confctl diff` compares
software inputs, not systemd/activation effects. Native dry-activate invokes the
candidate's `bin/switch-to-configuration dry-activate`, reporting unit actions and
running its dry-activation script; it was not invoked against a live machine.

Full built candidate and exact running closures are necessary for the later
comparison: package closure (`nix store diff-closures`), rendered systemd units,
activation scripts and nginx configuration, followed by candidate nginx syntax
validation with the required runtime files. The provided live closure prefixes
are not present locally, and no candidate was built. Candidate validation must
select its explicit configuration rather than implicitly test current `/etc`.
Reload support alone cannot certify activation effects. These are future
pre-activation gates; no additional comparison tool or live preparation is needed
for this plan. Source is frozen, Git ownership returns to the lead, and the
published feature remains the exact old lease above until a later decision.

## Exact inherited input identities

- `codex-web`: `d3a29bee90ef00a08816920408c596152339a637` → `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`.
  NAR `sha256-Hhh2EYZxKiM1fDfPGxDazhs/ElyOF4q6mMvK5JOUOu0=` → `sha256-JcQLZ4GPc5fOy2r4/iM4nhzqVTPWgZb6sNhJFd2nX+g=`.

- `devWorkspace`: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` → `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
  NAR `sha256-k6d90hicmnStL/tT6AeBLbYBQ5U7O/pmUls1zGYwsMg=` → `sha256-bgwQahEcT3ekDfMjmlDsgwhCdiKk+X6DDappoYKzknY=`.

- `vpsadminServices`: `097226b22edf8b59f80b5dfaa55265e9d0cac633` → `b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e`.
  NAR `sha256-NPeSoec5VuDuz/Gi6CR6LzkKmbKhRGIJwaW2zk0vxrg=` → `sha256-J7a/I+juHiy63uDAWxANp/THIX6+Zo7r4l0zaiicSeo=`.

- `vpsadminWebui`: `70bd11d983e7dfd11f99604791ad68562807ee2e` → `88ac13b89d6421c914cd57e18153de1fee6fc7b7`.
  NAR `sha256-LN2Z6e+sY9t8V9Lt+iTNsXaqFz5PzkByH5r7qmwgV1U=` → `sha256-rZ+HqRHYexxVlab3ErsfGeWna9tdTcltGpRZSNu8GRo=`.

- `vpsadminosOsStaging`: `b45b27b4330a08d85f413999e4bf66ba4503eee1` → `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
  NAR `sha256-Hir5K9vt1wQ0biMP98I3I2JB2iozeU92b50I+qMsCrg=` → `sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.

- `vpsadminosStaging`: `b45b27b4330a08d85f413999e4bf66ba4503eee1` → `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
  NAR `sha256-Hir5K9vt1wQ0biMP98I3I2JB2iozeU92b50I+qMsCrg=` → `sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.

- `vpsfreeWeb`: `307635a96bc3532af51ff5d08206d920704eee00` → `7fec3e3ccc5a1aa41bad7f06f83d01fa6cd15fe9`.
  NAR `sha256-/3QHdhSzFlEc7YqWZDjnVxIeS4n1OdImicvgUZjBGew=` → `sha256-AOCULuvrfGoWGTmOm2qbpop3vS6GGpOGwkpVnf3DZhE=`.

## Final range-diff

```text
1:  5e15c92c = 1:  6f65dd53 int.log: add unprivileged SSH log reader
2:  46bddfcd ! 2:  27868fee proxy: add dedicated Prometheus query access
    @@ Commit message
         monitors. Register the separate log-reader check and operations links.
     
      ## README.md ##
    -@@ README.md: See [API configuration and abuse notice processing](configs/vpsadmin/api/README.
    - 
    - ## Aitherdev operations
    - 
    +@@ README.md: confctl deploy "cz.vpsfree/nodes/stg/*" dry-activate
    + - [Operations index](docs/operations/README.md): mx2 relay checks and queue
    +   recovery, Aitherdev disk retention, vpsAdmin abuse notices and API documentation
    +   OAuth setup and recovery.
    ++
     +See [log reader access](docs/operations/log-reader-access.md) for SSH access to
     +central logs and [Prometheus query access](docs/operations/prometheus-query-access.md)
     +for the dedicated HTTPS API credential and its provisioning procedure.
    -+
    - See [disk cleanup and retention](docs/operations/aitherdev-disk-retention.md) for
    - Nix profile/test retention, coordination collection, and rollout/recovery.
     
      ## cluster/cz.vpsfree/containers/prg/proxy/config.nix ##
     @@
    @@ flake.nix
     +          pkgs = devPkgs;
     +          machines = confctlOutputs.machines;
     +        };
    +         mx2 = import ./tests/mx2.nix { pkgs = devPkgs; };
              nix-store-cleanup =
                devPkgs.runCommand "aitherdev-nix-store-cleanup-tests"
    -             {
     
      ## mkdocs.yml ##
     @@ mkdocs.yml: theme: readthedocs
    @@ mkdocs.yml: theme: readthedocs
      - Operations:
     +  - Log reader access: 'operations/log-reader-access.md'
     +  - Prometheus query access: 'operations/prometheus-query-access.md'
    -   - New vpsAdmin WebUI service: 'operations/newadmin-webui.md'
    -   - API documentation OAuth: 'operations/vpsadmin-documentation-oauth.md'
    -   - PHP WebUI OAuth logging: 'operations/oauth-client-log-protection.md'
    +   - Overview: 'operations/README.md'
    +   - mx2 backup mail relay: 'operations/mx2.md'
    +   - Aitherdev disk retention: 'operations/aitherdev-disk-retention.md'
     
      ## tests/prometheus-query-access.nix (new) ##
     @@
3:  98384b6b ! 3:  959e1d54 docs: describe observability setup and recovery
    @@ Commit message
         Keep inventory review in the logger's root terminal and leave manual
         root-key removal with the user after reader acceptance.
     
    +    Require a full running-to-candidate comparison before switching the shared
    +    proxy; nginx reload support alone does not constrain activation effects.
    +
      ## docs/operations/log-reader-access.md ##
     @@
      # Log reader access
    @@ docs/operations/prometheus-query-access.md
     -credentials remain in `/private/nginx/mon.htpasswd`: they do not authenticate
     -dedicated routes, and the dedicated credential does not unlock the human UI or
     -other API routes. This separation applies on both monitors.
    --
    --## API boundary and limits
     +```sh
     +install -d -o root -g nginx -m 0750 /var/lib/nginx-auth
     +umask 077
    @@ docs/operations/prometheus-query-access.md
     +chmod 0640 /var/lib/nginx-auth/prometheus-codex.htpasswd
     +```
      
    --Paths below are relative to `/codex/api/v1`. Only these exact routes are allowed:
    +-## API boundary and limits
     +Enter the password twice when prompted. The proxy already provides `htpasswd`.
     +This file is separate from the human monitoring password file.
      
    +-Paths below are relative to `/codex/api/v1`. Only these exact routes are allowed:
    ++## Save the credential on aitherdev
    + 
     -| Paths | Methods |
     -| --- | --- |
     -| `/query`, `/query_range`, `/series`, `/labels` | GET, POST |
     -| `/label/<name>/values` | GET |
     -| `/metadata`, `/targets`, `/targets/metadata`, `/rules`, `/alerts` | GET |
     -| `/status/buildinfo`, `/status/runtimeinfo` | GET |
    -+## Save the credential on aitherdev
    ++Run on aitherdev as `aither`. Create the private file before opening your editor
    ++(`vi` below):
      
     -HEAD accompanies GET. Label names use `[a-zA-Z_][a-zA-Z0-9_]*` in a single path
     -segment. Trailing slashes, encoded path spellings and unlisted paths or methods
    @@ docs/operations/prometheus-query-access.md
     -removes `/codex` and the `Authorization` header before contacting Prometheus.
     -Admin/TSDB mutation, reload/quit, receivers, remote read, config/flags, debugging,
     -federation and UI routes are unavailable through this credential.
    -+Run on aitherdev as `aither`. Create the private file before opening your editor
    -+(`vi` below):
    - 
    --The new routes share one budget across both vhosts: 2 requests/s with a burst
    --of 5 and at most 4 active requests. Excess requests receive HTTP 429. The fixed
    --quota key also counts unauthenticated requests; public clients can exhaust the
    --quota. Human UI and Grafana requests do not use it. Bodies are limited to 64 KiB,
    --with a 10s body timeout. Upstream connect/send/read timeouts are 5s/15s/30s.
    --The read timeout measures inactivity, not total execution time or CPU use.
     +```sh
     +install -d -m 0700 /home/aither/.config/vpsfree-observability
     +umask 077
    @@ docs/operations/prometheus-query-access.md
     +vi /home/aither/.config/vpsfree-observability/prometheus.curlrc
     +```
      
    --Use bounded ranges and `timeout=20s` in queries. That timeout is client courtesy,
    --not an enforced proxy CPU budget. The credential can read all metrics and the
    --listed operational metadata, without tenant isolation or redaction.
    +-The new routes share one budget across both vhosts: 2 requests/s with a burst
    +-of 5 and at most 4 active requests. Excess requests receive HTTP 429. The fixed
    +-quota key also counts unauthenticated requests; public clients can exhaust the
    +-quota. Human UI and Grafana requests do not use it. Bodies are limited to 64 KiB,
    +-with a 10s body timeout. Upstream connect/send/read timeouts are 5s/15s/30s.
    +-The read timeout measures inactivity, not total execution time or CPU use.
     +Save this content, replacing `SAME_PASSWORD` with the password entered at the
     +proxy's prompts:
     +
    @@ docs/operations/prometheus-query-access.md
     +max-time = 45
     +```
      
    --## Runtime credential files
    +-Use bounded ranges and `timeout=20s` in queries. That timeout is client courtesy,
    +-not an enforced proxy CPU budget. The credential can read all metrics and the
    +-listed operational metadata, without tenant isolation or redaction.
     +Keep the password out of Git, Nix, shell commands and chat. Enter it through
     +`htpasswd` and the editor rather than pasting it into a command line.
      
    --Provision these outside Git and Nix before activating the query policy:
    +-## Runtime credential files
     +## Deploy or roll back the proxy
      
    +-Provision these outside Git and Nix before activating the query policy:
    ++Provision the server hash and aitherdev curl configuration above before activating
    ++the proxy policy. Run these commands from the root of your
    ++`vpsfree-cz-configuration` checkout, inside `nix develop`.
    ++Before building, record the deployed generation and its matching retained local
    ++build `NAME`; retain that build and closure for rollback:
    + 
     -| Host and file | Owner | Mode | Contents |
     -| --- | --- | --- | --- |
     -| Proxy: `/var/lib/nginx-auth` | `root:nginx` | `0750` | Dedicated directory |
     -| Proxy: `/var/lib/nginx-auth/prometheus-codex.htpasswd` | `root:nginx` | `0640` | One username and bcrypt cost-8 hash |
     -| Aitherdev: `/home/aither/.config/vpsfree-observability` | `aither:users` | `0700` | Dedicated directory |
     -| Aitherdev: `/home/aither/.config/vpsfree-observability/prometheus.curlrc` | `aither:users` | `0600` | Basic credential and HTTPS curl defaults |
    -+Provision the server hash and aitherdev curl configuration above before activating
    -+the proxy policy. Run these commands from the root of your
    -+`vpsfree-cz-configuration` checkout, inside `nix develop`.
    -+Before building, record the deployed generation and its matching retained local
    -+build `NAME`; retain that build and closure for rollback:
    ++```sh
    ++confctl generation ls --local --remote 'cz.vpsfree/containers/prg/proxy'
    ++confctl build 'cz.vpsfree/containers/prg/proxy'
    ++confctl generation ls --local 'cz.vpsfree/containers/prg/proxy'
    ++```
      
     -Only the server pathname appears in Nix. Do not use `basicAuth`, `readFile`,
     -`writeText`, Home Manager content/source, or a Nix-generated credential file.
     -Neither plaintext nor the hash belongs in Git, the Nix store, command arguments,
     -environment variables, shell history, logs or chat. A missing runtime hash file
     -fails closed. Build and activation do not generate a default credential.
    -+```sh
    -+confctl generation ls --local --remote 'cz.vpsfree/containers/prg/proxy'
    -+confctl build 'cz.vpsfree/containers/prg/proxy'
    -+confctl generation ls --local 'cz.vpsfree/containers/prg/proxy'
    -+```
    ++Set `PROXY_ACCESS_GENERATION` to the new local build name and
    ++`PROXY_PREVIOUS_GENERATION` to the recorded prior name. Deploy that exact build:
      
     -Inspect the paths, mounts and ACLs before provisioning. Stop on unexpected
     -symlinks, foreign ownership, ACL grants or mounts rather than repairing them
     -blindly. Leave `/private` permissions and the human password file alone. File
     -permissions protect against other users; processes and sessions running as
     -`aither`, and root, can read the client credential.
    -+Set `PROXY_ACCESS_GENERATION` to the new local build name and
    -+`PROXY_PREVIOUS_GENERATION` to the recorded prior name. Deploy that exact build:
    - 
    --### Provision or rotate
     +```sh
     +confctl deploy --generation "$PROXY_ACCESS_GENERATION" \
     +  'cz.vpsfree/containers/prg/proxy' dry-activate
    ++```
    ++
    ++Build and copy the candidate while the running proxy serves traffic. Keep the
    ++running generation for rollback. Before switching, compare the full candidate
    ++with the running system: nginx configuration, packages, activation scripts and
    ++affected services. Validate the candidate nginx configuration. Use a reload when
    ++possible; do not deliberately stop nginx. Abort deployment if it would cause
    ++unexpected service disruption or more than a brief nginx reload or restart.
    ++A reload-capable unit can still be restarted during system activation.
    + 
    +-### Provision or rotate
    ++```sh
     +confctl deploy --generation "$PROXY_ACCESS_GENERATION" \
     +  'cz.vpsfree/containers/prg/proxy' switch
     +```
```

## Publication receipt, 2026-11-10

Lead confirmed final follow-up review PASS at exact
`959e1d54cabc7ac5530dac6179acacb077a57754`, with no findings; see
[review-followup-2026-11-10.md](review-followup-2026-11-10.md).
Binding, clean frozen head, active hooks and canonical SSH remote were verified.
Fresh fetch/ls-remote scoped to actual master and own branch matched expected
master `0f3897b5b7dc53edee33f1289cbda25ec28910f5` and feature lease
`98384b6b12fbc61c4df7c545d070cea446cc89bd`.

Executed in the canonical feature worktree, with pinned tools and no hook bypass:

```sh
nix develop --no-write-lock-file --command git push --set-upstream \
  --force-with-lease=refs/heads/2026-10-21-aitherdev-observability-access:98384b6b12fbc61c4df7c545d070cea446cc89bd \
  origin \
  refs/heads/2026-10-21-aitherdev-observability-access:refs/heads/2026-10-21-aitherdev-observability-access
```

Push exited 0. Post-push remote proof established the feature at
`959e1d54cabc7ac5530dac6179acacb077a57754` and actual default/master unchanged
at `0f3897b5b7dc53edee33f1289cbda25ec28910f5`. Local index/worktree remain
clean and upstream ahead/behind is `0 0`. Exact-branch GitHub Actions listing
returned `[]`; no runs were canceled or dispatched. No operation remains active.

Git ownership is released to the lead. This publishes reviewed source and plan
preparation only. Fresh candidate artifacts, reader acceptance and authorized
live execution remain future gates. No build, copy, activation, permissions or
credential write, root-key change, default integration or lifecycle action ran.

## Configuration integration preparation

After logger acceptance, a fresh scoped fetch/ls-remote still proved actual
master `0f3897b5b7dc53edee33f1289cbda25ec28910f5` and feature
`959e1d54cabc7ac5530dac6179acacb077a57754`. Source remained clean and unchanged.
Prepared a fresh detached, clean target at
`worktrees/2026-10-21-aitherdev-observability-access/configuration-integration`,
HEAD exactly that remote master, common Git directory
`repos/vpsfree-cz-configuration.git`. No merge or default push occurred and no
repository claim was acquired.

The feature's pinned environment successfully checked Bundler dependencies in
both source and target. Target/feature Gemfile, lock, Overcommit configuration
and flake lock blobs match. Ruby 3.4.9, pinned confctl and nixfmt are available;
repository pre-commit, commit-msg, post-checkout, post-merge and pre-push hooks
are executable at the default common hook path. An initial extra check for an
uninstalled pre-merge-commit hook was unnecessary: the declared Overcommit setup
has no such hook, and the required fast-forward path uses its active post-merge
hook. No hook was bypassed, disabled or replaced.

Ancestry proves target can fast-forward to the exact reviewed/deployed source.
The same three commits and 15-file +1577/-6 diff remain, with no migrations or
pin-update streams. Binary patch SHA256 is
`5dedb30e5946f24aec51cc7ebe8baf59c3da865e5e25f05b990f2e51608c78f9`;
source tree remains `d12a1746a0d11506559b5dc98c1b3105e1bd7fec`.
Preparation finished with no active command. Enter the prepared feature Nix shell
before acquiring the short merge claim, then use the detached target for native
fast-forward merge/hooks and non-force HEAD:master push with fresh remote proof.
The lead's proxy-verification gate still precedes that approved integration.
No root workspace Git, original branch refs, source or live service was changed.
