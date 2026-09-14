# Risk and compatibility review

Lane: risk and compatibility. Overall risk: high. Reviewed the committed
series and repository rules for all five packet heads:

- codex-web `aec4ea2ff13a053e340a2a47616d6fbc89aeeac1..62a8b3626f7defcbca343b2408c7dd1fd753cf11`
- dev-workspace `f41d4220dd1d5ade08ba3bb28f964e9570a11ed9..f371105cf1d19e8f7fa7fd09aced419e15478c3b`
- vpsfree-dev-workspace `213a3db57dea9298f61309eb157c0853f2310e9b..a23002ffe2e89f5ecbf35913d074fae2695c8c11`
- workspace `bfd4fb78732bc747995c2dd715309d7bdd58b984..3337cc45f00647b3ed6df575c3318e083e598b70`
- vpsfree-cz-configuration `3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea..4582592a1d1ca6a1c1aa26fdee67e57332107b4e`

## Findings

### Blocking: an unrelated indexed thread is not proof that the requested directory is fully indexed

Commit `e76de162c44b7c1e8298181e7777d3247989eb95`,
`dev-workspace/portal/internal/workspacecodex/client.go:94-129,138-148,331-379,389-414`.

When an indexed directory lookup is empty, `listIndexedThreads` checks only
whether an unfiltered state-DB-only query can return one arbitrary thread. If
it can, the code accepts the empty directory result without consulting rollout
history. That distinguishes a wholly unavailable empty database from the
normal populated database, but it does not distinguish a complete database
from a partially indexed one.

The pinned Codex 0.154.0 behavior makes the latter a real state. Its own
`codex-rs/rollout/src/recorder_tests.rs` coverage creates a rollout missing
from SQLite and demonstrates that `list_threads_from_state_db` omits it while
another normal scan discovers and repairs it. With the portal implementation,
an unrelated indexed row makes the canary pass. Creation then reaches
`StartThreadWithSettings`, fork reaches `ForkThread`, or retirement treats the
missing row as absent. In the creation and fork cases this can allocate a
second thread for one working directory; retirement can leave a thread active
after the session operation treats it as absent. The loaded-thread check does
not cover an unloaded rollout.

Do not use global index non-emptiness as per-directory completeness proof.
An empty result that can authorize creation/fork or absence during retirement
must fail closed unless the exact directory/recorded identity is proven
complete by a stronger signal. Add a regression where the indexed query for
the target is empty, the global indexed canary contains an unrelated thread,
and persisted history contains the target.

The proposed one-time auth-email recovery is narrower than this generic
failure mode: it retains the old private `dev-session` entry, current host
generation/token, shared transition lock, exact receipt/evidence and saved goal,
and substitutes only the candidate portal binary while Codex remains 0.154.0.
The creation lock serializes a competing retry, and a successful recovery marks
the existing creation journal ready before the profile switch. I found no
separate generation, receipt-identity, or prompt-replay issue in that procedure.
Its recorded phase and the packet's read-only evidence can support this exact
recovery, but they do not make the shipped global-canary rule safe for other
partial-index cases.

### Important: an exact saved comparison can be overwritten for the same head

Commit `f371105cf1d19e8f7fa7fd09aced419e15478c3b`,
`dev-workspace/portal/internal/web/repository_comparisons.go:74-99,264-314`.

Comparison files are keyed by repository and head, but `saveComparison` permits
a different warning-free pair to replace an existing warning-free pair. The
flock and atomic rename prevent torn concurrent writes; the rename still
overwrites durable state. Both automatic status observation and the explicit
CLI use this writer. A later observation whose merge base changed, or a second
explicit capture naming another valid ancestor of the same registered head,
can therefore rewrite the base shown by the default Repositories view. This
violates the packet's immutable exact base/head requirement. Hash-addressed
durable review descriptors remain immutable, but that separate store does not
protect the saved default comparison.

Preserve an existing exact base/head pair. An identical identity can be a
no-op, and upgrading a marked fallback to an exact pair can remain allowed, but
a different warning-free base for an already saved head should be rejected or
left unchanged. Cover automatic observation racing/following an explicit
capture and a repeated explicit capture with a different ancestor.

### Important: another open window keeps a stale cluster card after reset completes

Commit `451d25ddbf9f33aa0e696a0cd4b2896eb24dd333`,
`dev-workspace/portal/internal/web/server.go:884-896` and
`dev-workspace/portal/internal/web/static/app.js:1529-1546`.

During a mutation, the details endpoint correctly returns the cached status
with a local notice. Once reset removes the provider state, `MayExist` is false
and the endpoint returns no cluster entries. The browser refresh loop only
updates cards present in `payload.clusters`; it never removes or clears a card
whose provider is absent. The window that initiated portal release reloads on
success, but every other already-open session window can continue to show the
old running state and “Cluster is changing” notice indefinitely despite the
notice promising an update when the operation finishes.

Make a successful details response authoritative for cluster presence, or
return rendered cluster state that can add/remove cards. Preserve cached cards
only while the server explicitly reports busy or failure. Add the cross-window
sequence running -> busy with retained observation -> reset/absent and assert
that the old card disappears without a page reload.

## Checked boundaries and residual risks

- The retained request is rendered through `html/template` and subsequently
  updated/copied through `textContent`; JSON encoding also escapes HTML-significant
  characters. Creation mutations retain exact-Origin checking, body limits,
  receipt binding, private evidence, and creation/slug locking. I found no new
  prompt injection, cross-request replay, or authorization bypass.
- Parallel guest stop gives every machine its own 120-second complete stop
  budget and a bounded 10-second KILL attempt. The provider wrapper retains the
  lifecycle lock for the operation, waits at most 150 seconds for old or new
  runners, verifies socket/process ownership before cleanup, and the portal's
  180-second deadline leaves cleanup margin. Focused tests do not exercise real
  QEMU shutdown; that remains an appropriate post-review integration check.
- The matched profile pins codex-web, generic dev-workspace and the organization
  providers consistently. An old portal will interpret new provider exit 75 as
  unavailable during a mixed window, while the matched new generation presents
  it as busy; this is a temporary presentation degradation rather than an unsafe
  state transition. Rollback readers ignore the additive comparison files and
  the additive receipt response field.
- Comparison records deliberately do not retain Git objects. Historical views
  can still become unavailable after object collection; the packet records
  repository object retention as a non-goal.

Long creation/browser acceptance and live cluster tests should wait until the
Blocking finding is fixed, and the Important findings are fixed or explicitly
decided and recorded.
