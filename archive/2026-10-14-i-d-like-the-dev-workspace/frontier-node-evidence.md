# Named Node contract evidence

The initial member command was node --test portal/internal/web/attention_browser_test.cjs.
Its preserved frontier-runtime-static-node.log reports one passing file. That
output alone does not establish the inventory's claim of 15 named passes. No
specific reporter/environment cause has been established; retain the original
record and this correction rather than attributing it speculatively.

The reviewer raised that evidence gap during affected review. The lead ran one
justified focused direct invocation against the unchanged frozen runtime at
bb9e6291bec10227c961c36559fba406938f1eaa:

    source runtime-dev-env.sh
    node /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace/portal/internal/web/attention_browser_test.cjs

New frontier-node-lead-environment.json records Node v24.19.0, no NODE_OPTIONS
and no NODE_TEST_CONTEXT in that invocation. New frontier-node-lead-named.log
names all 15 contracts and reports tests15/pass15/fail0/cancelled0/skipped0.
Duration173.545307ms; exact revision and exit0 are recorded in
frontier-node-lead-named.status. No product/source or test implementation changed,
and no native browser/provider operation ran.

The current named-count claim is supported by this direct lead run. The
original one-file aggregate output remains evidence only for that original
invocation. Prior named15 evidence at b8a6 also remains historical, not a
replacement for this exact-head run.
