# KB captures need a supported owned runtime

Investigation: work/2026-10-05-network-ipv4-left-counter on 2026-10-06.

The capture repository's bin/devcluster supports screenshots topology through
config.topologies, despite stale help listing only single/dual/storage. Its
state is repo-local .devcluster, but socket paths hash only the slug into a
global /tmp directory. Start broad-kills matching socket processes, builds,
then removes that directory. There is no shared package-transition lock,
generation recheck or atomically recorded workspace socket identity. A fresh
slug and absent-state preflight cannot supply those ownership guarantees.

Current workspace lifecycle rules require them. Do not run this helper under
those rules or fabricate provider records. The installed catalog at this
investigation offered only vpsadmin/vpsadminos cluster providers; neither binds
the KB cluster. lib/dev-cluster.cjs reads KB-local state/cert paths and invokes
KB bin/devcluster; runner options provide no supported provider adapter.

No start/capture was attempted. Resolve the runtime binding in a separately
scoped compatibility change or supply a supported isolated capture environment.
Until then, preserve pending screenshots and distinguish static bin/check
success from actual visual verification. For bilingual capture, validate each
language immediately before the next overwrites tmp/capture-results.json.
