# vpsAdminOS staging merge

User direction: “i suppose it's useless to wait for the CI workflow, so let's merge it”. Scope is vpsadminos -> refs/heads/staging, as discussed;
no KB/workspace/extension integration or deployment is included. The user directs
proceeding without waiting for remaining broad CI. Focused local acceptance,
all6current images, normal persistence/compatibility/disk checks and RSpec pass.
Broad CI remains queued/running; it is not represented as green.

Fetched target 7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8; clean published feature d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5, tree07e8de78.
No rebase needed: target is an ancestor and the branch is exactly2commits ahead.
Current complete diff exactly equals the committed reviewed/dispositioned final
artifact; SHA256 9f8fda77fc1cef7f71f1eaca065564d5381e9875d7e202a37d38fe40ef7ea83c.

b2669ce00d440c1e05eb07b0e5bb4d201f3e5161 os: select NixOS guest compatibility by release (v5)
d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5 os: expose persisted allocation maps before legacy users (v10)

Independent Astra/xhigh complete four-lane/whole-history review and its explicit
no-migrations/no-obsolete-history conclusion remain applicable. I1 was resolved
with direct focused verification under mandatory-review step9. The later20line
fixture construction fix was directly checked under steps9–10; no product API,
format, pin, stateVersion or migration boundary changed. No new source changes
or unresolved review findings. No repeated production input-update streams,
shipping fixup/WIP or instruction owner. NO MIGRATIONS; no release/deployment/
external-consumption state boundary requires an intermediate branch version.

Feature refs remain retained. Session remains active after this integration.
Runtime coordinator creates its private target checkout, preserves hooks and
performs the fast-forward/normal SSH push. No direct Git bypass.
