# PHP-only OAuth logging: final affected review packet

Committed, required quick checks PASS, clean. STOP for independent affected
source/security/history review before four-target builds or installed P0 retry.
The user canceled KB and Discourse: no further work or acceptance for them is
part of this package. Lead owns final review assignment and subsequent releases.

Repository `vpsfreecz/vpsfree-cz-configuration`, canonical SSH
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`; owned registered checkout
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration-oauth-clients`,
branch `2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs`.
Saved implementer1 `gpt-6.1-sol` / `xhigh` / `workspace_write` and exact session
binding verified. No other source writer or owned operation remains.
[Current PHP-only brief](../../oauth-client-log-protection-plan.md#current-php-only-correction-and-execution-boundary).

## Exact complete history and source

Full range `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627..60af1a1f0930c731d6f0bbabd0a0cb3ed21b550a`,
final tree `5ba2ab16c503be3e6e95a1d18006b49815782e29`.
Exactly FOUR direct logical commits, eleven full-range paths:

| Commit | Purpose |
| --- | --- |
| `02121132a4bafcaa061072e995290f2e17b8ede3` | Existing API/docs hook, frontdoor and operator commands, retained unchanged |
| `7493684fc59e20410b88e8767b9909d3263a972f` | PHP-only proxy/backend/HAProxy protections, two approved fixes and nginx quick fixture |
| `a68f7430d7587650e78e4e85fc5290c7f05b1b4b` | Parent's exact PHP-only operator guide and renamed existing MkDocs entry |
| `60af1a1f0930c731d6f0bbabd0a0cb3ed21b550a` | ONE unchanged generated final services pin4a21→75c, full message retained |

[Complete series](complete-series.txt), [full FCC diff](complete-final.diff),
[eleven paths](complete-paths.txt), [seven-path249f delta](prior249f-final.diff),
[249f path list](prior249f-final-paths.txt),
[reviewed7fdb-to-final delta](old7fdb-final.diff),
[old/new full-series comparison](old-new-range-diff.txt).
Final tree is independently reconstructed from all four complete patches.
No revert/fixup, repeated services pin or canceled P2/P3 commit remains.

Compared with accepted249f, exactly seven paths change: common/frontend.nix,
common/webui.nix, the tiny nginx fragment, retained nginx quick fixture, PHP-only
operator guide, MkDocs label and final services lock. All470 outside entries
retain exact path/mode/type/OID equality. Compared with old7fdb, only the exact
removal/restoration set, two PHP fixes and guide/label change; all469 outside
entries equal. Final477 entries vs old489 reflect twelve canceled source files
removed. [Removal/outside/reconstruction/ref proof](removal-outside-history-proof.json).

Registration originally began at249f. Both249f and7fdb are nonancestor retained
source/recovery boundaries; neither is claimed literally merged. Their original
checkouts remain untouched. Exact recovery refs include original249f, D002,
preconsolidation30a96, reviewed09299, and new before-PHP-only7fdb. Source, private
ignored state, five historical build receipts/roots and original failure records
remain; no session/artifact/checkouts/ref cleanup was performed.

## Scope reduction and remaining behavior

The user's instruction was: “drop the KB and discourse oauth changes”. Restore
these four shared files **exactly** to accepted249f: proxy.prg/config.nix,
int.kb/config.nix, discourse/config.nix and overlays/packages.nix. Remove all eleven
new DokuWiki/Discourse package files plus the Matomo fixture. Dropping P2/P3 and
the KB portion of P1 implements this directly in final history. No new KB or
Discourse source/config/plugin/analytics/header/log policy remains.
[Exact removed/restored path inventory](canceled-product-paths.json).
The one shared fragment still exposes only httpConfig/serverConfig/referrerConfig
and now has only PHP frontend/backend consumers; no global module/framework.

Retain legacy PHP production, maintenance and development edge/backend logging,
PHP HAProxy prod/dev request-log disable, explicit HTTP redirects and
strict-origin responses. Preserve auth values on wire, routes/listeners/aliases,
ACME challenge precedence, maintenance behavior and existing Basic auth. Retain
the existing021 API/auth/docs behavior and untouched React/source pins.

Two exact approved corrections are folded into owning P1:

- Common WebUI pool sets existing `php_admin_value[error_log]` to
  `lib.mkForce "syslog"`. Keep log_errors and catch_workers_output enabled in
  the unchanged selected module. P075c product bytes remain unchanged. The old
  selected destination `stderr` resolved as a store-relative filename; E2's
  actual FPM attempt failed to observe either the fixed callback diagnostic or
  ordinary native error. Syslog is the selected PHP-supported special sink.
- The rightmost dev vhost merges its generated phpClientVirtualHosts value with
  the existing basicAuthFile. This retains the safe TLS policy and explicit HTTP
  partner; the old shallow override discarded that policy and produced three
  dev servers. No new recursive abstraction or Basic-auth change is introduced.

Both changes are source/quick checked. Full generated configuration and actual
new native diagnostic transport are **not yet proved**. Do not infer success
from source text or from the old builds.

## Generated pin, compatibility and migrations

The final pin is an exact patch and FULLmessage replay of reviewed7fdb's normal
confctl-generated4a21→75c update. No new confctl command or interim pin ran.
[Final generated patch](final-generated-pin.patch),
[complete generated message](final-generated-pin-message.txt).
Full flake.lock bytes equal7fdb. Only services locked revision/NAR/lastModified
changed versus FCC/249f; siblings, follows, node channels, WebUI/notification pins
and selected nixpkgs remain unchanged. [Lock proof](semantic-lock-proof.json).

Selected P0 `75c691b17c48115f929b57ef55f78935be006ea6`, tree
`8a16a74b8a64b7118d629d43e14ae0049469fb61`, retains its independently reviewed
and published product scope. Original retained reviewer0 all4/HIGH review was
NO FINDINGS at75c; normal publication independently read back75c/defaultac10.
[Original P0 review packet](../../package-php-oauth-logs/review-packet.md),
[publication proof](../../package-php-oauth-logs/publication-final.json).
P0 focused16/full116 and final affected9 tests retain their exact source scope;
no new product review/native34/browser/SDK campaign is needed solely for these
configuration fixes. Installed transport remains separately required.

**NO MIGRATIONS.** The config changes no schema/migration. Complete selected
consumer4a21→75c preserves315 actual core/plugin migrations and33 migration specs,
all paths/modes/types/OIDs exact. No new merged/released/deployed/externally
consumed migration needs preservation; no migration rewrite or state transition.
[Current binding](migration-proof.json), [unchanged detailed inventory](../consumer-migration-inventory.json).
OAuth clients, keys, sessions, persistent state and protocols remain compatible.
Deployment order/rollback stay in the parent operator guide; reverting logging
policy can reopen its sink, without a schema/credential change.

## Quick checks, hooks and original failures

[Final quick summary](final-quick-result.json), [source quick log](source-quick.log).
Declared shell, CPU60–63/nice5/Nix1job2cores. Required scoped Nixfmt/parse and
complete-range whitespace pass. Literal approved syslog and dev merge checked
against formatted source. Parent guide bytes equal the saved handoff, its local
link resolves, both operations MkDocs targets exist and only the assigned nav
label changed.

Retained PHP nginx fixture ran once after scope reduction: seven actual safe
access records for302/502/200/unavailable/maintenance/HTTP301/ACME challenge.
Exactly one strict-origin header, original query/Cookie/Authorization/Referer/
Location/Set-Cookie/provider body preserved, public sentinels absent from actual
logs, ordinary diagnostics retained and owned processes/ports reconciled.
[Result](nginx-quick/result.json), [exact evaluated fragment](fragment-values.json).
This is a quick nginx fragment/wire/log check, not new installed-system or OAuth
login proof. No canceled suite was repeated.

Normal P1 amend/hooks and guide amend/hooks/replay pass; no bypass.
[Rebase edit](rebase-edit.log), [P1 amend/replay](P1-amend-replay.log),
[guide amend/pin replay](guide-amend-replay.log).
Initial authored-message width assertion stopped message preparation; subsequent
approved rebase effects were reconciled before continuing the same operation.
Messages were wrapped without repeating checkout/rebase or changing source.
[Preparation note](preparation-guard-note.json).
A final receipt check was also made whitespace-insensitive after Nixfmt expanded
the dev attrset; no product change followed that checker-only assertion.

An **optional** selected four-target config evaluation stopped31663, exit1,
31.948s with IFD disabled and jobs0. The WebUI package requires a generated-source
read; its source derivation exists but the corresponding output is not valid in
the store. The initial assumption that old build evidence established current
availability was corrected before any permissive eval ran. No source fetch,
realisation, retry or build was launched. This is incomplete optional proof,
neither a product failure nor a generated-config pass.
[Command](selected-quick-command.json), [original result](selected-quick-result.json),
[original stderr](selected-quick.stderr). Lead accepted required quicks as sufficient
for final review; generated proof belongs after it.

Original five successful builds belong ONLY to exact7fdb: proxy, both production
WebUI backends, dev WebUI and canceled KB. Their graphs/roots remain historical.
The owned Discourse build was canceled by direct user instruction: only its exact
PID/PGID1879421 received graceful SIGINT, original11886 ended1, no owned build
children remain. [Cancellation effects](../postreview/systems/attempt-1/discourse-user-cancel-effects.json).
No final60af output is claimed built or equivalent to old outputs.
Original P0 missing diagnostic transport remains failed acceptance until the
new sink is tested. Original P1 dev three-server failure remains failed until
new generated proof. The KB base-ini interpretation was withdrawn after wrapper
scan inputs were found; it is historical and now canceled, not a remaining fix.
No canceled app checks were run to prepare this packet.

Original configuration review at09299 was ONE Important OCL-R1, all4/HIGH;
its exact requested P3 fix was step9-accepted at7fdb. That original report is
preserved, not relabeled no-findings; P3 is now removed. Earlier E1 ONE Blocking
R1 remains accurately resolved as well. [Old7fdb packet](original7fdb-review-packet.md).
A new affected review is required for this reduced PHP boundary and its two
new configuration corrections, not a blanket reuse of the wider review.

## Requested review and next gates

Lead should assign retained independent reviewer0 saved Sol/xhigh/read_only,
GENERAL/history + ARCHITECTURE/repetition + SCOPE/proportionality +
RISK/compatibility, overall HIGH (OAuth logs and operations). Review complete
FCC..60af history/final diff and seven-path249f delta, cancellation removal,
syslog/dev merge semantics, parent guide, one generated pin and NO MIGRATIONS.
All intended source is committed and clean; no active writer/operation remains.

STOP until review and lead release. Next required package is exactly four normal
confctl builds: proxy.prg, int.webui1, int.webui2, int.webui-dev. Capture final
source/inputs/drv/output/root graphs; inspect generated HTTP/TLS/dev Basic auth,
ACME/maintenance/log/header inheritance, unchanged API/auth/React and all three
WebUI pools selecting syslog. E2 then retries only the minimal installed P0
fixture with those actual paths: fixed callback and useful ordinary diagnostic
presence, sentinel absence, unchanged auth/order/redirects. Equal production
runtime inputs need one sequence. Mutable dev source requires separate binding
before later real acceptance. No builds or P0 retry started for60af.

No feature publication, default integration, production access/client/secret/
login/deployment, lifecycle action, other session or original parent3922 action.
All existing recovery refs, source checkouts, private ignored files and roots
remain retained. Session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
