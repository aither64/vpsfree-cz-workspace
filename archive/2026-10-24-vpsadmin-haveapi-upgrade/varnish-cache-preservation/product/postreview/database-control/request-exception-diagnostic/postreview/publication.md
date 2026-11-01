# Final diagnostic source delivery and CI ownership

Exact reviewed/quick-checked product `0f450b89a5e39c203db0bbdfe0df86b386275343`,
tree `10860b8d771f12d71e99cec7587d52d248c57c9d`, is published and source-clean.
The source writer is released; all four exact-head automatic CI runs passed. This
observability change does not establish the cause of the historical auth500.

Source `/nix/store/mwf6ja4m5gf51lr0nqdm1ian7j5lpxj3-source`, NAR
`sha256-XIvp4xKpLXmhQHDZYp+CSPcSM1jdSu/bsvJ2UQ9eSoc=`. All3179 tracked entries
match clean Git. The complete flake input-lock graph and16 tracked locks/gemsets
match fbd. [Exact binding, graphs and hashes](binding/final-binding.json).

Minimal package realization73973 completed0 in11.244s. Actual API
`/nix/store/gs7bfng4ywl3pg94gfrk6xqfdcf758cv-vpsadmin-api-unknown` has2267 entries,
with only the two reviewed spec/support changes. Actual source-copy
`/nix/store/k0c7dbwjmay5ajabfswl11pp5wfiylp0-vpsadmin-source-unknown` has3514,
with exactly the three reviewed spec/doc changes. Installed PHP bundle
`/nix/store/cyl9q7aplj079hqq2fxggps9hxx1mr5n-vpsadmin-installed-php-proof` contains
a1120-entry WebUI with only its `.git-revision` changed to0f; nginx configuration
differs only by this WebUI-root address. Actual PHP/nginx binaries, ini, pool,
settings, page/vendor contents, Varnish/HAProxy/HaveAPI recursive dependencies,
kernel and relevant fixtures remain exact. Final runtime/source closure has316
paths. Accepted fbd→7219/45cb runtime proof scopes are reused explicitly; no new
services/PHP/cache/browser/client/fullfoundation execution or kernel compilation.

The old fbd source-copy output4adl95 is absent; its source, derivation, original
3514-entry inventory and actual API/PHP outputs remain. Comparison uses that
retained inventory, checked against intact exact source/filter/revision inputs;
ten ordinary stdenv shebang fixups retain exact old installed hashes in the final
output. This is not a fresh read of the absent old output. The final source-copy
is explicitly rooted. [Backing limit](binding/old-source-copy-backing-limit.json),
[installed comparison](binding/installed-reuse.json). Local inspector parse/path/
missing-backing/shebang-assumption failures are retained distinctly; they caused
no product change, suite retry or runtime-input mismatch.

Fresh canonical SSH guards proved masterac10/featurefbd/protected refs. Named
fbd recovery was published FIRST by ordinary nonforce push76086, independently
read back62968. Feature push7795 then advanced only its own branch linearly and
nonforce fbd→0f. Independent canonical readback35865 proves head0f/recoveryfbd/
defaultac10/allotherheads unchanged; supported comparison capture completed0.
[Publication proof](publication/final-proof.json), [guard](publication/guards.json),
[recovery proof](publication/recovery-proof.json). Complete7history/first6literal/
one released HaveAPI stream/NO MIGRATIONS and accepted all4/HIGH review remain
[the completed review scope](../review-acceptance.md).

Informational E1 handoff8ff01a64-e9cd-43fb-86e1-4840c00ed6b1 was delivered and its
native84676 consumed0. That informational handoff granted no site mutation.
After accepting final-head CI, lead separately released E1's final mechanical
site pin; E2 performed no site operation and preserved its prior source proof.
No default merge, deployment, claim, profile, PR, lifecycle or cleanup action.

After publication, the one exact old integration41252535439 was freshly confirmed
in_progress on samebranch/headfbd/attempt1. The superseded-own-head policy alone
authorized cancellation; gh cancel completed0. No current-head/otherbranch run
was canceled or rerun. Original observer47627 naturally exited1 and was consumed; PID2644845/start9149157
is absent. The actual old integration conclusion is cancelled; original API500/
failure evidence remains retained. [Effects](publication/superseded-effects.json). [Cancellation
receipt](publication/superseded-cancel-result.json).

One discovery found four automatic exact0f ownbranch push runs, all attempt1:

| Run | Workflow | Final outcome |
| --- | --- | --- |
| 41259553569 | CI | SUCCESS |
| 41259553556 | API Specs (topic parallel) | SUCCESS |
| 41259553534 | i18n health | SUCCESS |
| 41259553561 | RuboCop | SUCCESS |

The API run completed at01:31:50Z; original observer saved complete=true/errors0
at01:31:54Z. All four retained terminal receipts bind exact head0f and branch.
Original handle48564 was consumed with actual exit0, independently of saved
status. Its originalPID3617135/start9720964 is absent; no local signal or restart.
[Owner](ci/ci-owner.json), [saved status](ci/ci-status.json),
[terminal receipts and effects](ci/terminal-effects.json),
[one discovery](ci/discovery-receipt.json). Reconciliation used saved records and
the original native handle only: no new remote query, artifact retrieval, test,
rerun, dispatch, source/Git/site operation or lifecycle/cleanup action.

Lead accepted final-head CI at its exact scope. The historical fbd auth500
remains unexplained; this green result does not prove a causal fix. Original
failures/logs/private replay evidence remain retained.

All source/input/build/fetch/push/readback/message/CI handles are consumed;
there are no remaining E2-owned operations. Source writer remains released.
Live33d6/private/roots/recoveries and original updater3922 are untouched.
Lead owns state and E1's separately released site delivery.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
