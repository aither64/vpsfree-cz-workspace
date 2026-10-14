# Focused source commits

Do not execute until the new scoped checks pass. Preserve mandatory declared
hooks. Stage exactly the path lists beneath this session, inspect the cached
diff, and commit using the adjacent message file.

1. vpsadmin: `commit-v-api.paths` and `commit-v-api.message`. Additive schema and
   API metadata; new-use guards; network-before-IP transaction boundaries;
   enabled public IPv4 counter; model/resource/migration behavior tests;
   concurrency scenario source; migration/restore/export continuity scenario
   source; owning IP-locking and upgrade documentation.
2. vpsadmin: `commit-v-webui.paths` and `commit-v-webui.message`. Legacy network
   availability form, inventory and selector behavior; EN/CS gettext catalogs;
   CSRF and stale assignment regression coverage; live browser scenario source.
3. vpsadmin-webui: `commit-w.paths` and `commit-w.message`. Typed optional API
   inputs/capabilities, administrator controls, disabled owned-address inventory,
   cached-address revalidation, EN/CS catalogs, unit/DOM tests, strict adopted
   browser scenario source, requirements/contracts/evidence/work-log/inventory.

Commands from the respective worktree root:

```sh
git add --pathspec-from-file=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/commit-v-api.paths
git diff --cached --check
git diff --cached --stat
nix develop .#vpsadmin --command git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/commit-v-api.message
```

Repeat with `commit-v-webui` for the legacy UI split. For W, use `commit-w` and
its default `nix develop` shell. Review complete stage contents before each
commit. Refresh only the owned W inventory/path list after its generator.

# Publishing and downstream pins

Fetch upstream default branches and inspect the complete incoming/default
comparison before feature-only publication. Stop for a meaningful upstream
conflict or rebase need. Push exact feature refs over SSH; W needs the scoped
draft PR represented by `network-webui-pr-draft.md`, after final evidence is
reconciled. Do not merge.

After exact V and W final commits are published, the lead can launch the
reviewed, parameterized command with a fresh watcher:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/prepare-network-pins.sh config V_SHA W_SHA
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/prepare-network-pins.sh kb V_SHA
```

Config invokes exactly two channel-set commits and preserves their generated
messages. K edits only the four exact source revision records, updates its
vpsAdmin flake input normally, and runs the static contract check. Inspect lock
changes and all reported impact; do not refresh fingerprints blindly. Stage
and commit the K pin separately using `commit-k.message` only after static
checks and semantic diff review. No cluster capture, build or deployment is in
these wrappers.

# Migration provenance

`20261006120000_add_network_enabled` is the only new migration. It follows the
core schema at V base `c4d9b50f4e74417ed37b5fe410cca3ec1addc24e`, defaults all
existing/new networks to true, adds no fallback predecessor schema guards, and
has isolated forward/reverse behavior coverage. It has not been merged,
released, deployed or externally consumed in this initiative. Source feature
heads and final lineage remain pending commits and publication.
