# C0312 committed patch: affected final review packet

At submission: source complete, all intended changes committed and quick checks
passed. Lead subsequently accepted reviewer0 affected final/whole-history review
with no findings and no migrations at exact911..2e32/treeae4, and released
postreview checks plus conditional own publication. This packet retains original
source/quick evidence; actual check/publication results are recorded separately.
See the [completed postreview/publication handoff](postreview-results.md).

Session `2026-10-24-vpsadmin-haveapi-upgrade`; accepted architect brief in
`design.md`: “2026-10-28: authorized 0.31.2 patch adoption”. Lead owns tracking,
review assignment and later check/publication release. Canonical SSH remote:
`git@github.com:vpsfreecz/vpsadmin-webui.git`.
Own registered checkout: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-0312`.
Own branch: `dev/vpsadmin-haveapi-0312` (unpublished).

## Complete range and retained lineage

Accepted base **`9113caa0915b2908373ecd616f8f752e779ed4c9`**.
Final head **`2e32c814d3af70ac39257f2542075bd580ee38d4`**.
Tree `ae4e282a33886faff151818255a99bd5710de832`. Tracked checkout clean.

Exactly two logical feature commits:

1. `73070a17e07cfffdf972d85690ffa5011172c53e`: direct final npm0.31.2 pin,
   lock, provenance, normal dependency hash and retained data-driven source guards.
2. `2e32c814d3af70ac39257f2542075bd580ee38d4`: unchanged reviewed production
   adapter/R2/OPTIONS, with current technical dependency docs and dated0312 entry.

Both original author name/email/date are preserved from ea842820/e468;
normal saved contributor identity, message-file commits and hook checks used.
No hook framework/configured hook path/active non-sample hooks are declared;
no bypass or identity/configuration change. [Commit preflight](commit-preflight.json).

[Complete series](commit-series.txt), [final diff](final.diff),
[old/new range-diff](old-new-range-diff.txt), [mapping](content-mapping.json),
[diffstat](final-diffstat.txt). Full carried feature:75 paths +1533/-615.
Old reviewed/deployed range is **911..e468**; new range is **911..2e32**.
One final dependency update stream, then its production adoption; no obsolete
0.30/0.31.0/0.31.1 intermediate pins, fixups or unused compatibility paths.

**No migrations**: no DB/schema, persisted-format, session, wire or node
protocol change. No feature migration was merged, released, deployed or
externally consumed because none exists. Live/published e468 is retained as a
supported exact predecessor, not an ancestor or literally merged commit of the
consolidated successor. Original rollout/source evidence remains intact.

Fresh main `40653dffed4561dd6086716fd506a7223d3631d7` adds73 product paths;
lead/architect explicitly exclude them from this patch milestone. Repository
AGENTS permits current-main exception when the task explicitly depends on
another branch; the accepted reviewed/deployed911/e468 lineage is that dependency.
No reconciliation of406 or current-default merge-readiness claim is made.
[Accepted base](accepted-base.json), [fresh remote boundaries](final-remote-boundaries.txt).

## Actual release, installed package and unchanged scope

Use [E2's completed release facts](../../package-0.31.2/release-facts.md), not a
duplicate release campaign. Source819bba5110e089465535ecd71ca2eb37a7d39caa,
tagv0.31.2, workflow40661462796/attempt1. Provenance record consumes E2's verified
registry/source/ref/workflow/invocation fields; no new signature verification.

Owner [installed artifact proof](installed-artifact-proof.json) independently
checks actual bytes recovered from normal npmci's content-addressed cache,
without another archive network fetch: SHA256
`4fbe3543cea865aee70d858e3c65c2e182b2208aa977eb031ed49ff949a8118a`, integrity
`sha512-cksLaGqdGk9c4yTm4Egwl3G4MKXUm9ICP7V+2ptW8pGe+cKICwXQvFCXZMCgqbz/Rf9rFWGdmrxC4o7gGwQs5Q==`.
All53 installed files equal the archive **and** local tagged release source.
Compared with0311, only package.json and actual distributed JS bundle change;
bundle equals its predecessor after version substitution, all46 declarations
are byte-identical. [Implementation diff](js-runtime-source.diff).

Only root/client lock entries change. XHR1.8.0, all unrelated root resolutions,
BFF security graph/hash, Node and flake inputs remain exact e468. New normal
npmDepsHash: **`sha256-EPQkMRkwpmmQAsf2T2WbK2x9We9M78A/lT8R17x7+vs=`**.
No adapter policy, fixture/assertion/timeout, SDK or provider change.

The complete src/BFF/E2E/scripts/build/nix/nixos/tests/tooling/configuration/
flake scopes are byte-identical to e468 ([empty scope diff](unchanged-runtime-scope.diff)).
Delta from e468 is only12 dependency/technical-doc paths
([paths](predecessor-delta-paths.json), [delta](predecessor-to-successor.diff)).
Original R2 contradictory-receipt ambiguity/no-replay guards and OPTIONS
correction are preserved. No seven-overlap or new product reconciliation is needed.

## Actual quick evidence

Pinned Nix Node24.21.0/npm11.19.0. A0 owns sole utility slot; explicit visible
parent fallback uses CPU60–63/nice5/Nix1job2cores and reconciles every handle.
No competing watcher, arbitrary timeout, retry, live mutation or extra campaign.

- Setup **PASS0/50.960s**: ordinary root lock/install, new normal prefetch,
  zero-vulnerability production audit, six source-guard cases.
  [Command](setup-command.json), [log](setup.log), [exit](setup.exit).
  Existing six optional-WASI missing-resolved warnings retained.
- Eight existing actual-library files **123 cases PASS**: transport/auth/
  renewal/public/error/abort, VPS/nodes and R2 shared mutation guards.
- Complete **ci:quick PASS0**; combined focused+quick duration **137.139s**.
  Root/tooling/E2E/BFF declarations, lint/format/docs/structural/product audits
  passed; E2E type coverage82 adopted/192 deferred.
  [Command](quick-command.json), [log](quick.log), [exit](quick.exit).
- Final prose/runtime/diff checks **PASS**: actual Client.Version0.31.2,
  docs150/requirements76, inventory257 routes/64 API modules.
  [Log](final-docs-runtime.log).
- Exact committed Gitless Nix-filtered source guard **PASS15**.
  [Log](filtered-source-guard.log), [source NAR](filtered-source-identity.json).
  Rooted source `/nix/store/c054hj749wd59b2qv5784bmkaxb8yg4f-source`, NAR
  `sha256-ZaLAoXcf21glVgdjvUQ47TqCxsMli1ZSXbS30DKF9eU=`.
  Ordinary provenance eval exact2e32/dirtyfalse; this is evaluation/source proof,
  not a realized frontend/BFF package result. [Provenance](provenance-eval.json).

## Review and later checks

Carried whole-branch risk remains high because auth/mutation policy is included;
the patch delta introduces no new behavior. Lead assigns retained reviewer0 at
saved Sol/xhigh/read_only settings for narrow affected metadata/docs/source
mapping plus explicit whole-history/consolidation/no-migrations conclusion,
using applicable lanes under mandatory review. Prior e468 review is retained
context, not automatic new-range acceptance. No review is claimed yet.

Current HAVEAPI_CLIENT/PACKAGING, dated0312/index and minimal historical pointers
updated; developer-facing prose only, documentation skill applied directly.
No member-writing pass or new UI prose is needed.

Required affected package/build checks await final review and a complete lead
release. Old full1923-unit/BFF/browser proof is reusable only within exact
unchanged source/dependency scope; not relabeled as new-head execution. No
automatic full browser/paired expiry/SDK campaign. Prior3/6 and5/6 failures,
separate f10/baf desktop expiry passes and old60/62 limits remain
at their original scope; no synthetic green/cause/preexisting claim.

The accepted native unknown embeddedmetadata limitation remains separate:
previous e468 manual-dev acceptance used complete independent filtered-source/
derivation/service-chain proof. New native activation needs its own actual
source/output proof; this package does not fix the provider or infer native
output equality from standalone results. Lead/E3 own any later reset/rebind,
actual TLS/login and Go documentation acceptance.

Published/live e468, baf/f10, PR74 alias/head5dd, PR63 and defaults are untouched.
New0312 ref remains unpublished. [PR74 exact plan](pr74-publication-plan.md)
is still a separate protected published-history approval gate. No default
merge, native/source-path move, deployment, provider/runtime/KB/lifecycle action.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
