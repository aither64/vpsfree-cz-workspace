# Proxy correction review reconciliation

All four mandatory lanes reviewed committed config 0e0a985a at sol/xhigh.
General, scope and risk reported no findings. Architecture reported one
Advisory: the runbook described proxy rollback twice with different target
terms. There are no Blocking or Important findings.

The advisory is fixed in final cleanup commit
a310b87625e53434655fd1c3e215f16999615982. The guide now has one proxy rollback
step, after both APIs are masked, targeting the retained pre-rollout system
generation and followed by checks of other proxied sites. The subsequent
WebUI/API rollback retains its existing API masking and startup order.

The final revision differs from the reviewed revision only in that narrow
runbook correction. Root inspected the exact diff, reran strict MkDocs and
active commit hooks, and confirmed the duplicate instruction is gone. This is
mandatory-change-review step 9 verification; no affected interface, design or
runtime behavior changed, so a reviewer rerun is unnecessary.

The original routing workaround is absent from the retained branch. The four
other original feature patches remain unchanged. Input declarations, generated
pruning and their immediate shared-proxy deployment instructions stay in one
focused cleanup commit, as agreed. Generated pin-commit messages are unchanged.

Full proxy build and generated-config/closure inspection pass on final
a310b876. Its built configuration metadata has revisionDirty=false and the
exact reviewed input mappings. Both auth hosts have exactly one copy of each
expected route with the correct upstream and maintenance error handler. The
normalized Nginx diff against the preceding built proxy contains only the
Nginx include version update and the module-owned recovery route on the admin
auth host; the production recovery route and other virtual hosts are preserved.

The closure diff records the broader package advance, including nginx
1.30.3 -> 1.30.4, HAProxy 3.3.9 -> 3.3.11, OpenSSL updates and the
vpsAdmin download-mounter update. No local kernel build occurred. The comparison
baseline is the previously built bb49f262 proxy, not a new capture of the live
production generation. The operator must still compare the then-active
production generation before rollout.

Production switch/rollback remains an operator action. No live production
testing, deployment, cluster change or session lifecycle action occurred.

Published final a310b876 with an exact lease protecting prior remote bb49f262.
Remote head matches and the configuration worktree is clean. There are no
feature-branch workflow runs or push-triggered checks in this repository; its
scheduled dependency-update workflow was not invoked. No CI wait or runtime
deployment was performed. See result.json and built-validation.json.
