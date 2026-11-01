# OAuth client logging: final configuration review packet

Complete committed source and quick checks PASS. STOP before long builds,
installed-stack fixtures or feature publication. Lead owns review assignment.

Session `2026-10-24-vpsadmin-haveapi-upgrade`; implementation owner implementer1,
saved `gpt-6.1-sol` / `xhigh` / `workspace_write`, verified at this boundary.
[Approved plan](../oauth-client-log-protection-plan.md) and [design](../design.md)
control scope, including the final postreview E1/E2/E3 split. E2 and E3 released
all package writers; parent released the settled guide. No active owner command,
Git/index/source writer, fixture process or listener remains.

## Exact repository, scope and complete history

Repository `vpsfreecz/vpsfree-cz-configuration`, canonical SSH
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Own registered worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration-oauth-clients`.
Branch `2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs`.

Final full range `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627..09299a95778807307cb9ca4c66f749de4c3a8f9b`,
tree `a564069618c7763a05fd2b85864156e4af5dfbd2`, clean source/index.
Prior published range was `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627..249f2eb5896b0a2697ed94e44657294847b3e606`.
Registration initially started at exact249f; authorized consolidation changed
only this new branch's lineage. Prior249f is **not** an ancestor of final and is
not claimed literally merged. Prior behavior remains carried and independently
reviewable through the full final diff.

Six coherent commits, in order:

| Commit | Owning stream |
| --- | --- |
| `02121132a4bafcaa061072e995290f2e17b8ede3` | Retained API-docs hook/proxy/operator guide and links from accepted249f |
| `e6b6b628c390ca6a4249acaf074ab54870c7bf24` | P1 selected client proxy logs, headers, HTTP redirects and focused nginx fixture |
| `ab7f4bbe333cff2c44e8195074227e2963dd67ce` | P2 KB plugin/core patch, PHP/Matomo wiring and focused checks |
| `c1a0e7eab8359a11ac8b12de4cdf0dd8fc94a59c` | P3 Discourse plugin/owning source patch, service wiring and focused checks |
| `921fc5289674e6b574c5b8168da9821ef7bc54df` | Parent-settled reusable operator guide and MkDocs link |
| `09299a95778807307cb9ca4c66f749de4c3a8f9b` | ONE normal generated services channel update, baseline4a21 to final75c |

[Complete series](complete-series.txt), [full FCC diff](complete-final.diff),
[27 full-range paths](complete-paths.txt), [prior249f delta](prior249f-final.diff),
[23 new-scope paths](prior249f-final-paths.txt),
[old/new full-range comparison](old-new-full-range-diff.txt),
[final identity](final-source-proof.json).
All466 entries outside the23 intended new-scope paths are mode/type/OID-equal
to249f. All functional source hashes equal the precommit quick inputs.
[Outside proof](outside-equality.json), [source hashes](functional-source-hashes.json).
The complete six-patch series was replayed into an independent index from FCC;
its reconstructed tree exactly equals final. [Reconstruction](reconstruction-proof.json).

## Consolidation, generated pin and migration provenance

The inherited249f generated33d6 services update was removed only from this new
branch. After normal-hook functional commits, ordinary
`git rebase --onto 02121132a4bafcaa061072e995290f2e17b8ede3 249f2eb5896b0a2697ed94e44657294847b3e606`
replayed exactly four byte-identical functional patches/full messages; only
flake.lock changed back to the original FCC baseline. No manual lock edit,
whole-worktree reset/stash/clean, hook bypass or protected-ref rewrite occurred.
[Rebase proof](consolidation-proof.json), [four-stream range diff](consolidation-range-diff.txt),
[normal rebase log](consolidation-rebase.log).

Then exactly one normal declared-shell command ran:
`confctl inputs channel set --commit vpsadmin vpsadmin 75c691b17c48115f929b57ef55f78935be006ea6`.
Native handle27465 ended0 in34.426s, normal hooks enabled. It generated the final
4a21-to75c patch and full changelog/message, preserved without rewriting.
[Exact command](final-pin-command.json), [log](final-pin.log),
[result](final-pin-result.json), [generated patch](final-generated-pin.patch),
[full generated message](final-generated-pin-message.txt).
Only `vpsadminServices.locked.{rev,narHash,lastModified}` changes. All other
nodes, channel mappings, sibling revisions and follows are identical to FCC and
prior249f. [Semantic lock proof](semantic-lock-proof.json).
No repeated pin/fixup stream remains. Historical exact249f/D002 refs, old source
checkouts, prior review/build/publication records, roots and recovery contracts
remain intact. Own preconsolidation30a96 recovery ref is retained. Frozen
canonical33d6, original parent3922 and remote defaults were untouched.

**NO MIGRATIONS.** No configuration schema/migration path changes. Full selected
consumer4a21-to75c comparison preserves all315 actual core/plugin migrations
and33 migration specs, including every path/mode/type/OID.348 is the inventory
count, not348 migration implementations. No new migration has merge/release/
deployment/external-use provenance to preserve.
[Consumer inventory](consumer-migration-inventory.json),
[configuration conclusion](configuration-migration-history.txt).

## Implemented boundaries and quick evidence

P1 uses only the three strings in `configs/nginx/oauth-client-logs.nix`;
callers own vhosts/redirects. Selected PHP prod/maintenance/dev, KB cz/org and
Discourse logs retain safe method/query-free path/status/size/timing records.
Scoped raw nginx errors are suppressed, upstream Referrer-Policy copies hidden,
strict-origin emitted, PHP HAProxy prod/dev request logs disabled. Preserve
names/aliases/listeners/certs/ACME/maintenance/routes/cache choices/auth wire
values. Imported common/frontend declares the edge safe format exactly once;
old combined global default and unrelated/React/API configuration remain.
Generated whole-host inheritance and exact runtime composition remain postreview.

Actual nginx quick PASS, seven access records: success302, provider502,
ordinary200, unavailable502, maintenance503, HTTP301 full-query target and ACME
challenge precedence. One strict-origin header, original query/Cookie/
Authorization/Referer/Location/Set-Cookie/provider body preserved; public
sentinels absent from actual nginx output, benign diagnostics retained, owned
process/listeners reconciled. [Result](p1-nginx-quick-v2/result.json).
Reproduce using `tests/oauth-client-log-protection/nginx.py --nginx BIN
--fragment-values JSON --output-dir FRESH_DIR` with [exact values](p1-fragment-values-v2.json).
This is fragment/wire/logger evidence, not a whole installed host or real login.

P2 exact6file handoff/source hashes: [E2 handoff](../oauth-log-p2-kb/handoff.md).
Ordinary plugin `oauthlogprotection`, per-site appended core Logger patch,
auto_prepend PHP marker from five query keys by presence; no request mutation,
no native admin setting preventing request-local log policy. Failclosed500 if
callback native log_errors cannot be disabled. Native fatal termination retained.
Ordinary diagnostics remain; allowdebug0 and production display/trace settings
use existing per-site PHP options. Matomo entire JS+noscript omitted using the
same marker until clean navigation.
Ten actual pinned core/Event/ErrorHandler/native PHP CLI cases PASS; original
hook-only sink failure and fixture corrections retained. Reproduction command,
exact pinned source/hash and limits are in E2 handoff; [final results](../oauth-log-p2-kb/quick-final/results.json).
New config integration34cases PASS across both sites using actual per-site _raw
PHP expressions plus the handed-off bootstrap, with ordinary JS+noscript and
parsed inputs unchanged. [Matomo result](matomo-quick/result.json),
[actual expressions](matomo-quick/expressions.json).
Reproduce `python3 tests/oauth-client-log-protection/matomo.py --php BIN
--nixpkgs EXACT_SOURCE --output-dir FRESH_DIR`.

P3 exact5file handoff: [E3 source/check reproduction](p3-handoff.md).
Normal mkDiscoursePlugin plus ONLY the four-file owning-source patch appended
to per-service selected Discourse; existing patches/src/deps/signup plugin kept.
Early Rails filters/logging-copy adapters cover Logster/exception middleware/
optional Logstash; own strategy diagnostics install after initialization.
Patch removes raw provider warning/debug payloads and callback/failure query
rate-limit URIs without copying auth methods or replacing loggers.
Reported73 pinned-source assertions, three syntax checks, scoped RuboCop,
Nix parse/interface PASS. Exact quick outputs/failures remain in E3 tool history;
its retrospective handoff labels that scope rather than inventing raw logs.
Actual Logster sinks and patched source run with isolated Rails/Rack/provider/
Redis stand-ins; not installed boot/OmniAuth state/CSRF/GitHub acceptance.

P0 selected exact published `75c691b17c48115f929b57ef55f78935be006ea6`, tree
`8a16a74b8a64b7118d629d43e14ae0049469fb61`. Setup/provider lookup/token/login
Throwable containment stays only inside code-bearing callback, with one fixed
ordinary error_log diagnostic and existing generic response. A0 focused16 and
full116 tests passed; final formatting-only affected9/107assertions passed.
[Original P0 review packet](../package-php-oauth-logs/review-packet.md) and
[publication proof](../package-php-oauth-logs/publication-final.json).
Lead accepted retained reviewer0 native01a18e25-f990 all4/HIGH NO FINDINGS at75c.
This consumer pin carries that fix, not an independent installed-FPM proof.

Normal functional commits/hooks and final pin hooks PASS; authored72-column
advisories do not exceed repository80-column limit; generated message preserved.
[Assembly results](functional-commit-results.json), [first log](functional-assembly.log),
[continuation](functional-assembly-resume.log), [final quick](final-quick-result.json).
First assembly stopped on required blank unified-patch context whitespace;
checks were corrected to inspect patch additions separately. No source changed,
no hooks bypassed. Unchanged nginx/Matomo/P2/P3/old source quicks were not repeated.
Final focused Nixfmt/parse, Python syntax, both operations MkDocs targets and
whitespace pass. All source bytes match the quick/handoff hashes.

## Documentation, review request and remaining gates

Reusable site guide `docs/operations/oauth-client-log-protection.md` is the
parent context-writing pass, covering actual P0/P2/P3 controls, residuals,
ordered verification/rollout/rollback and no blanket read-only approval rule.
It is linked in MkDocs. Existing docs OAuth guide/hook/API README remain carried.
Prior E1 full review at aead had ONE BlockingR1 (nginx log-format ordering),
resolved atD002 and preserved in249f; it is not relabeled no-findings.
[Original/resolved E1 packet](../package-e1/review-packet.md),
[accepted249f guide review scope](../package-e1/guide-commands/review-packet.md).
D002 builds remain D002 evidence; final configuration outputs have not been built.

Request retained independent reviewer0 saved Sol/xhigh/read_only, all four
lanes: GENERAL/history, ARCHITECTURE/repetition, SCOPE/proportionality,
RISK/compatibility. Overall HIGH: OAuth secrets/logging, configuration and
operational rollout. Independently assess complete FCC..09299 series, final diff,
23-path249f delta, pin consolidation and explicit NO MIGRATIONS conclusion.
No reviewer assignment was made by E1; lead owns that turn.

After accepted final review and explicit check release, plan split is E1 six
normal exact systems/output graphs/generated config; E2 actual installed FPM/
P0 transport; E3 actual Rails/OmniAuth sinks. Nothing launched yet. Generated
whole-host nginx/HAProxy syntax/inheritance, exact installed patch/plugin/P0
selection, namespace/sink behavior and actual Rails boot remain unverified.
KB pre-prepend engine/startup failures and existing manual fatal HTML are
explicit residuals, not a hidden logging pass. PHP dev checkout remains mutable
and is not inferred equal to P0. No historical/production disclosure absence,
universal privacy, actual OAuth acceptance or deployed usability is claimed.

No dependency/SDK/nixpkgs version campaign, source/default integration, CI,
production requests/logs/credentials/client provisioning/login, deployment,
dry-activation, lifecycle/cluster operation or parent3922 action was performed.
Source remains available only for lead-directed findings; all roots/old refs/
private ignored files and existing effects retained.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
