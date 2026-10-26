---
lifecycle: active
---

# Current status — 2026-10-26

Phase: implementation, independent final review, affected local verification and
feature publication complete. Both live interfaces are available for qualified
manual testing. Refreshed vpsAdmin exact-head CI remains in progress; no default
integration is approved. Provider fix F is ready, awaiting merge approval.

This is the current entry point. The preceding detailed checkpoints are preserved
byte-for-byte in [state history](history/state-before-consolidation-20261026.md)
(SHA256 `365a4210d02779eceeb5f380877a1d0ea6d74d0ac594b96a73e9244b87aae7fe`).
The session and development cluster remain open and running.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)

## Phase checklist

- [x] HaveAPI 0.30.2 server/client upgrade, documentation profiles, React npm client
      adoption and bilingual KB candidates committed; ordinary hooks/quick checks.
- [x] Independent final reviews include complete histories, final diffs and explicit
      no-migration conclusions. Refreshed vpsAdmin and provider F received separate
      final four-lane reviews with no findings.
- [x] Original consumer timing/auth/locale/output and representative SDK acceptance;
      React units/builds and bounded browser investigation completed.
- [x] Refreshed vpsAdmin affected services, core/full auth, PHP regression and browser
      auth checks passed with actual new dependencies.
- [x] Both PHP and React real OAuth login/logout, verified TLS, authenticated API reads
      and independent current four-guest closure/root proof accepted.
- [x] Provider F source fix, required local checks, feature publication and exact-head
      automatic CI successful; not installed.
- [x] Distinct refreshed vpsAdmin branch published/publicly registered; live original
      checkout, sources, locks and four guests preserved.
- [ ] Refreshed vpsAdmin CI: seven workflows successful; API and integration active.
- [ ] React PR74 exact protected history rewrite approval/publication.
- [ ] Legitimate KB staging/render/history checks and exact production approval.
- [ ] Explicit repository/target integration approval and fresh integration gates.

## Owners and remaining work

| Owner | Result / next action and acceptance |
| --- | --- |
| implementer2 | Sole exact-2c CI observer: nine runs, attempt 1. Final conclusions or explicit long-integration-only pending handoff; no retries/dispatch/cancel. |
| implementer0 | Successor publication, public comparison and unchanged-live proof complete; no owned operation remains. |
| implementer1 | F reviewed, checked, published, CI green; receipt reconciled. No installation/live repair. |
| implementer3 | Live UI/guest receipt complete; probes stopped, cluster retained. |
| architect0 / reviewer0 | Designs and separate final A/F reviews complete; no open source finding. |
| lead | Acceptance, records, PR/KB/integration approval boundaries. |

Sole watcher slot belongs to owner2's fresh exact-2c CI utility, retained catalog
`840de475…`, native `dw_b9dd4137…`, Luna/low, full access/never,
thread `01a1799f-017f-73a3-b705-d356db141047`. No duplicate CI queries.

## Exact repositories and lineage

Worktrees are under `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/`; canonical
repositories remain under `repos/`. Exact published heads:

| Registration / target | Branch | Head | Reviewed base |
| --- | --- | --- | --- |
| vpsadmin-refresh / master | 2026-10-24-vpsadmin-haveapi-upgrade-refresh | `2c6542941fde72c0ea7bb2991274981e98c5781c` | `898e2881e8230d24fb06baee1c58737ae55e0009` |
| vpsadmin / master | 2026-10-24-vpsadmin-haveapi-upgrade | `70a2ed54b98d0c2f359a9cc4484452a257a9807b` | `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` |
| vpsadmin-webui / main | dev/vpsadmin-haveapi-upgrade | `f10d3d48c4f21cc39187c3667ffffd9952404c11` | `5a2d2bdc3ad7a827038f877d75959916528db844` |
| vpsfree-dev-workspace / master | 2026-10-24-vpsadmin-haveapi-upgrade-boot-proof | `ab9346b0c4b942fccd0da6af760401fad3a55bd1` | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |

Successor A `5cfe8b0f8d809fc0d5b40956f0e8f6a539ace00f` plus B/head `2c654294…`,
tree `66fba1840081875860109ac208c9611ddc139a37`, is the preferred vpsAdmin
integration candidate. Independent reconstruction of old70a plus the upstream
four-file patch equals this tree. Only old-to-new delta: paired generated locks/
metadata preserve upstream Faraday 2.15.1 and Guzzle 7.16.1. B's binary diff,
authors/dates/messages retained; two logical commits, no migrations.
Old70a is a retained published/live nonancestor, not literally merged into the
successor. Do not edit/rebase/repoint its checkout/ref/config/ignored locks.
Successor is published but not deployed. See [packet](package-a-integration-refresh/review-packet.md)
and [publication](package-a-integration-refresh/publication/receipt.md).

WebUI has two logical commits/no migrations. The sole postreview test-only delta
corrects stale GET/raw-description to reviewed OPTIONS/envelope; lead accepted
five focused cases and lint/format checks. See [review](haveapi-0.30.2-review.md).
F has one functional commit/three files/144 additions and seven deletions, no
migrations/schema/policy/dependency/CI changes. [F packet](package-f/review-packet.md).

## Accepted checks and practical limits

Original-input evidence remains valid for its recorded scope:

- [R1 consumer](package-b/b3/performance-run-1/receipt.md): warm role/locale requests
  4.936/2.533/4.231 seconds; auth/locale/output isolation and 174 panels/168 programs/
  six limitations parity. R1 closed.
- [SDK](package-b/b3/sdk-run-1/receipt.md): 26 complete programs compiled, 20 actual
  plus six labelled synthetic fixtures; 148 actual programs uncompiled, six Go
  limitations remain explicit.
- [React](package-c/0.30.2/postreview-results.md): scripts 228, BFF 57, Vitest 1,899
  cases/303 files, production/Nix checks pass. Browser 60/62; both mobile expansion
  failures reproduce on independent exact base. Specific existing residual accepted;
  no clean-browser or CSS-cause claim.
- Original services 32/32; core/full foundation/auth/platform-config 4,248 examples,
  zero failures/74 expected pending; console 1/1, PHP auth 24/24, VPS operations 2/2.
  VPS native exit 0 proven; original Python wrapper exit unknown.
- Original automatic API CI all26 topics plus coverage: each mode 4,725 examples,
  zero failures, full eight/core404 pending. Original integration40336542935 was
  still active at final handoff; its observation assignment has ended.

[Successor affected checks](package-a-integration-refresh/postreview/receipt.md):
services32/32; actual fourHaveAPI0.30.2/Faraday2.15.1/Fiddle1.1.8/libffi3.8.0/assets;
core/full auth220each, zero failure/pending; PHPHaveAPI0.30.2/Guzzle7.16.1 load,
PHPUnit13tests/355assertions; webui auth native1/1 and24Playwright passes. Strict
actual/prepared package/config guards and same immutable source
`/nix/store/wv51bcflfw1hjjrg5ig44abq67ksqwya-source` throughout. Original full API
ignored lock restored exactly to `535137acb35136154ca615a8f5648a62fd1826136f2c8a82664a6f1983b4f544`.
PHP wrapper exit1 AFTER all15 steps passed: generated untracked PHPUnit cache
tripped final snapshot guard. Cache retained in receipts; final source/lock/status
proof passes. Preserve wrapper failure separately; no test repeat or invented0.
All test guests/processes reconciled, roots retained, live cluster unchanged.

[F checks](package-f/postreview-receipt.md): focused84cases/957assertions pass;
required flake check all9 passed (own371cases/3415assertions, one existing skip).
First smoke failed when pressureGC deleted app/tools; journal and partial result
preserved. Same input graph/source restored under normal owned roots; fresh full
declared smoke passed444s, complete202path closure/NAR/reference afterchecks.
Original flake outputs were later GCed; their successful evidence is historical.
No original app/tools NAR existed, so no unsupported byte-equivalence claim.
Exactab934 Check[40379808743](https://github.com/vpsfreecz/dev-workspace/actions/runs/40379808743),
attempt1, sole job121772673835: SUCCESS. F unmerged/uninstalled, no live repair.

## Current exact-head CI

Owner2 initial verified snapshot: all nine runs attempt1/head2c.
Seven SUCCESS: PHP40383178588, Migration40383178589, Client40383178603,
RuboCop40383178625, Console40383178633, Mounter40383178641, i18n40383178823.
API[40383178617](https://github.com/vpsfreecz/vpsadmin/actions/runs/40383178617)
queued with topics running; integration
[40383178746](https://github.com/vpsfreecz/vpsadmin/actions/runs/40383178746)
in progress. No overall CI-pass claim. Evidence in
`package-a-integration-refresh/ci-observation-1/initial-summary.json`.
Stop with explicit pending handoff if only long integration remains (native test/
workflow limits720/780min); do not wait12hours or resume old polling.

## Running interfaces and old boot-record limitation

PHP <https://webui.aitherdev.int.vpsfree.cz/>, React
<https://newadmin.aitherdev.int.vpsfree.cz/>, API
<https://api.aitherdev.int.vpsfree.cz/>, OAuth
<https://auth.aitherdev.int.vpsfree.cz/>.

[Runtime receipt](devcluster/runtime-verification/receipt.md) records actual
OAuth login2/2 and logout2/2 with TLS verified, PHP EN/CS selections and React
API7 authenticated reads200. Session response has token/session keys; values not
emitted. Missing optional authenticated boolean is not login failure. Internal
DNS/network, cluster CA trust and privately provided seeded credentials required.
Receipt includes public CA path/fingerprint and packaged HaveAPI identities;
no per-process gem introspection or React locale-switch claim.

Attempt `devcluster/activation/20261026T153200Z` completed nativeexit0, canonical
running/ready; runner2882335 and four QEMUs remain in
`vpsadmin-haveapi-upgrade-e-20261026T153200Z.scope`, 32GiB/12CPU/zeroOOM.
Global Nix daemon accounted separately. Runtimew6j9bzb/providerq19s1vj selected
at launch; fresh selected package/guide checks precede later operational work.
Live sources remain original70a/Reactf10, not refreshed2c.

The old launcher's saved full-boot record claims all guests were checked, but SSH
could consume the remaining names in its input loop. Its extra provider root is
present only on dns-primary. Independent checks proved all four exact current/
booted systems, valid closures and standard system-1-link roots. This supports
CURRENT manual testing; it does not validate the old certificate for future
pruning/update/cold recovery. F fixes future source behavior, has not been installed
or used to repair that old record. No immediate missing-system/root evidence;
leave cluster running. Six kernel alerts were broad-regex false positives:
three modules-closure and three initrd/cpio builders; actual kernels registered
before startup, buffered timestamps do not establish exact build timing.
No further guest/browser/network probes assigned; effects reconciled.

## Approval boundaries and next action

- No default integration approved. Readiness question is not merge direction.
  Short repository claims only after explicit repository/target approval and
  fresh preparation, never while awaiting CI/review/approval.
- PR74 reuse permitted, but exact protected force-with-lease rewrite unapproved.
  See [plan](package-c/pr74-publication-plan.md). Preserve PR63/oldrefs; no duplicate
  PR. Own React branch published; its triggers did not run CI, no CI-pass claim.
- KB candidates reviewed at workspace7d5ac686; three version substitutions/language.
  Foreign staging ownership preserved. Legitimate staging/render/history checks and
  exact production approval pending; no production write.
- No runtime installation, live root/envelope repair, cluster update/reset/stop,
  host deployment, foreign claim transfer, cleanup or session lifecycle action.

Component documentation stays with committed profiles/adapter/provider README;
execution evidence in linked receipts; [design](design.md) retains decisions.
Portal preserves original live registration and distinct successor alias.
Next: accept owner2's exact2c CI conclusion or final pending handoff, then present
concrete repository/target integration and PR decisions with remaining limits.
No broad rerun, source change or default integration is authorized meanwhile.
