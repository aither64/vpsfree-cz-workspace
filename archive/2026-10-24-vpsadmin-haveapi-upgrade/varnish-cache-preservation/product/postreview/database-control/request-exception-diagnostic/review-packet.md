# API spec exception diagnostic: committed quick-green review packet

Clean head `0f450b89a5e39c203db0bbdfe0df86b386275343`, tree
`10860b8d771f12d71e99cec7587d52d248c57c9d`, is committed and quick-green.
**Source writer released. STOP before publication, CI control or site pin changes.**
Lead owns retained reviewer0 assignment and acceptance: affected all four lanes
at HIGH whole-branch context, retaining reviewer0 Sol/xhigh settings. This is
not independent acceptance or a repair of the historical auth500.

Session `2026-10-24-vpsadmin-haveapi-upgrade`; source worktree:
`worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs`.
Authoritative boundary: `design.md:7256`, accepted/released directly by lead.
Plan/state remain lead-owned; this packet supplies their current evidence.

## Outcome and bounded implementation

Caught request errors can produce a generic500 without retaining their cause.
Exactly three assigned paths change, +190/-3:

- `api/spec/support/app_helper.rb`: attach one instance `request_exception`
  observer when the actual default app is created/cached. A private helper emits
  one JSON stderr line prefixed `API_SPEC_REQUEST_EXCEPTION `. It allows the
  scoped current example ID, at most four cause classes, first allowed API
  lib/models/spec source path+line and actual Mysql2::Error integer errno plus
  validated five-character uppercase/digit SQLSTATE. Unknown optional fields and
  outside/eval locations are omitted. Incoming hook ret is returned unchanged.
- `api/spec/smoke/harness_spec.rb`: preserve the harness example and add seven
  focused regressions through the actual cached app/hook. Existing auth-smoke
  assertions remain literal. No topic/manifest/workflow changes.
- `docs/agent-instructions/testing.md`: one technical paragraph explains the
  allowed fields, omissions and existing CI-log retention, with unchanged API
  response behavior.

No exception message, inspect/to_s, rendered traceback/method label, SQL/binds,
request/context/header/body/URL/credential or model data is serialized. Reporter
failure attempts only a fixed structured marker; stderr failure is contained.
No retries, timeouts, isolation/error-setting, authentication, production logger,
application model/schema, dependencies or Varnish/site policy change here.
The owner is existing API spec support, consumed by the same cached Rack app;
no public formatter or cross-project logging framework is introduced.

## Complete history, authorship and migration inventory

Base `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a` to final has seven commits:

| Commit | Purpose |
| --- | --- |
| `11b26c0a5f6fa51fc6eb63b8f28dd5e8ccbaf721` | Released HaveAPI0.32 packages |
| `ccb08e3cebb06f46b4dddea3a86baec31f1ff5b3` | OAuth docs/client consumer |
| `967da811892062ffc82d4cd98a43ed6a7e7a5a28` | Derived documentation selectors |
| `9cff7f2a14f8316468623d57a81482598beef98e` | PHP callback diagnostics |
| `7219ab22a49f666077056fc2f093424547294aeb` | Persistent-log defaults, restored Varnish/cache proof |
| `fbd0b9379839dd0e747a00b5bd63e4be98880889` | Test snapshot contract and worker cleanup |
| `0f450b89a5e39c203db0bbdfe0df86b386275343` | Safe test-only request exception evidence |

All first six commits are **literally unchanged**, including authorship/messages;
[range comparison](literal-history.range-diff) and [full history](complete-history.txt)
bind that claim. New commit author remains Jakub Skokan
`<jakub.skokan@havefun.cz>`. Its observer, acceptance specs and documentation are
one coherent test-support behavior. It is separate from the preceding inherited
DB repair: the new CI500 lacks exception evidence and its cause remains unknown.
No accepted history is rewritten; all earlier live/recovery provenance remains
in the [accepted six-commit packet](../review-packet.md) and
[review acceptance](../review-acceptance.md), with earlier product consolidation
in [the prior product review](../../../review.md).

[Correction/authorship](correction-commit.txt), [exact old/new diff](correction.diff),
[complete base-to-final diff](complete-final.diff), [full diffstat](final-stat.txt),
[all changed paths](changed-paths.txt), [identity/hash proof](final-proof.json).
The whole branch has51 paths; generated released client JS accounts for most
line growth and is unchanged by this correction.

One released HaveAPI0.32 dependency stream remains, unchanged; no repeated pins,
obsolete bypass or superseded new approach is introduced. **NO MIGRATIONS:**
there are no migration/schema paths in the complete base-to-final diff or new
commit. No new persisted state or supported upgrade/rollback path is introduced.
Local named `...-oauth-client-logs-fbd-recovery` was created at exactfbd before
edits. All local refs except this feature's ordinary fbd→final advance are
unchanged. No remote/default/live33d6/private/root mutation occurred.

## Exact focused quick evidence and effects

The dirtyfbd tested patch is byte-identical to the final committed correction:
SHA256 `31e4dabfa6d36f3689496c21c56f4046c21ae3e892c12a9c3e201bfc8d9638b5`.
[Proof](final-proof.json), [tested bytes](tested.diff),
[commands](quick.sh), [quick receipt](quick-result.json).

- Native23918 completed0. Sequential full/core ordinary `nix develop .#api`,
  retained frozen generated mode lockfiles, seed16772; only existing harness and
  auth-smoke files. Each mode: **11 examples,0 failures,0 pending**. Full examples
  58.789s; core47.003s. Both changed Ruby files pass syntax and component RuboCop.
- Finite acceptance passes: one parseable safe line for deliberate real-app
  error/cause/1205/HY000, message/request/SQL sentinels absent, generic500 unchanged,
  nonempty hook ret retained by identity, repeated app lookup no duplicate,
  ordinary auth200/no diagnostic, bounded causes, missing/invalid/outside/eval
  metadata omissions, reporter+stderr failure containment.
- [Full native result](full-result.json), [core native result](core-result.json),
  [full input/gems](full-environment.json), [core input/gems](core-environment.json).
  Ruby3.4.9/Bundler4.0.23, MariaDB11.4.12 RR/snapshot0. Exact lock/gem hashes and
  flake.lock hash are retained; no CI11.8 equality is asserted.
- Normal root declared shell commit79478 completed0: Nixfmt, MigrationSpecs,
  WebUI/API i18n and RuboCop hooks pass, as do commit-message hooks. TextWidth
  issued advisory >72-column warnings; every line satisfies the80-column rule.
  [Hook output](commit.log). `git diff --check` and final clean-index/source guards
  pass. No source edits followed the checked patch.
- Two lint-only attempts and two fixture-development failures remain separately
  recorded. First request fixture injected into vpath OPTIONS before the intended
  route; second compared a LocalizedMessage object with serialized text. Both
  corrected only harness setup/assertion representation. Original logs/results,
  patch/env bindings and statuses are retained, never counted as passes.
- [Effects](effects.json) verifies all five captured final quick shell/Ruby/DB
  process identities absent. Native handles26643/61230/53745/71514/23918/79478 are
  consumed. Prior attempt4 process absence is recorded separately. No fixture
  daemon remains; no lifecycle/cleanup or other-session operation was performed.

## Limits and next boundary

Original fbd API run41252535538/core seed16772 had1432/1/52 with admin auth
expected200/generic500 after51.65s; full seed33586 had1432/0/3. Its actual
MariaDB11.8.6 RR/snapshot0 is observed, but the caught request exception is absent.
[Original facts](../final-ci/ci-41252535538-failure-facts.json).
The one unchanged-source local original-manifest replay passed1432/0/52 with no
request exception; [replay receipt](../auth-smoke-replay/receipt.json). Local11.4
versus CI11.8 and Ruby differences remain explicit. That pass and these focused
quicks neither explain nor fix the historical CI500. No further local foundation,
seed sweep, bisect or environment campaign was run.

Independent review must cover containment/redaction and unchanged hook/API
semantics, then explicitly assess complete7history/one released dependency
stream/NO MIGRATIONS. No long checks or publication are released at this boundary.
Actual final packaged-input/filter/derivation/revision effects must be assessed
postreview before deciding site-pin refresh or proof reuse; priorfbd/7219 runtime
proof is not relabeled as new output validation.

Existing sole integration observer47627 remains separately accountable for exact
fbd run41252535439; its saved state is retained without an added remote query,
watcher or CI control. Published product remainsfbd and site5e is unchanged.
Lead owns review assignment, state incorporation and later release decisions.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
