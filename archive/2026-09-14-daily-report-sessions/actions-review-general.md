# Individual authentication actions: General review

Reviewed the complete committed functional ranges:

- `vpsadmin`
  `5ac49802f892da6fd37a88c8349b9cc7ea826538..014fbc78422f3660b295add7a50f35cc7acdf0c8`
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`

The review covered the baseline feature and its separately requested follow-up
against `plan.md`, `state.md`, and `actions-review-packet.md`. I inspected both
repository `AGENTS.md` files, the linear commit series, final source trees,
aggregation and detail-query behavior, built-in text and organization HTML
renderers, migration/schema changes, focused database specs, selective CI
mapping, and delivered-mail assertions. The existing configuration branch
still pins the reviewed baseline heads by design; final source pins are a later,
separately reviewed phase after the source heads are pushed.

## Findings

No Blocking, Important, or Advisory findings.

The source histories are clean and match the requested split. In vpsAdmin,
`f7996f5df67d82c9627c73aae8e2b40101609570` contains the coherent aggregate
report feature with its migration, built-in renderer, tests, and CI mapping;
`014fbc78422f3660b295add7a50f35cc7acdf0c8` adds the requested individual
action payload, text rendering, and focused and delivered-mail coverage. In the
template repository, `08402ffd8010384f950b1ec4a1b95de8e5410ba3`
implements the aggregate consumer and
`6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333` adds the individual HTML rows.
Each commit has one reviewable purpose, no fixup or superseded behavior remains,
and commit messages follow the local conventions. Both ranges pass
`git diff --check`.

The follow-up uses the same half-open report relations as the summaries and
orders every event by `created_at, id`, so repeated rows and timestamp ties are
stable. It selects only recorded client IP fields, resolves current logins in
one `User.unscoped` query, retains IDs for missing users, and eagerly returns
plain hashes under additive `events` keys. Both renderers hide empty or absent
event arrays. The HTML helper escapes the generated href, login, user ID,
source, mechanism, reason, and client IP; missing users are not linked. The
focused specs cover repeated rows, half-open boundaries, tie ordering,
default-scope-hidden and missing users, missing client IP without API-IP
fallback, hostile HTML values, and empty, aggregate-only, and older payloads.

Post-rebase focused verification in `actions-final-specs.log` completed with
19 examples and 0 failures. The packet also records passing RuboCop, Nixfmt,
template flake validation, and commit hooks.

## Residual risks and test gaps

- The follow-up delivered-mail integration scenario has not run after these
  commits. Its added fixture and assertions exercise both action types through
  the scheduled report path; running it after mandatory review is the planned
  long-test phase.
- Aggregate and event queries are separate eager reads. Concurrent writes can
  make counts and detail-row totals differ within one generated report. This is
  an accepted generation-time reporting limitation rather than a historical
  snapshot contract.
- The action lists intentionally have no row cap. An unusually busy report
  window can increase query memory, rendering time, and message size; this is an
  explicit user decision and has not been load-tested.
- The configuration worktree still references the baseline source heads. That
  is the stated sequencing boundary, not a functional defect: push the reviewed
  source heads, regenerate exact pins with `confctl`, then review and build the
  final configuration commits.
