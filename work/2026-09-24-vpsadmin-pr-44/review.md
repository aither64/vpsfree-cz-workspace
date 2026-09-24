# Review of vpsAdmin PR #44

Reviewed [PR #44](https://github.com/vpsfreecz/vpsadmin/pull/44) at base
`486350466e8fb6f966add1cde3fa2bc12b4d6b62` and head
`320af0e152ed223bf0365e0f1cf4b38cf00d7b1d` on 2026-09-24.

## Assessment

The change is justified. The old HaveAPI `from_id` predicate compares IDs,
while the affected resources display rows by assignment date, dataset name,
snapshot creation time, or property-history creation time. Those orders can
diverge. The proposed tuple comparisons, deterministic ID tie-breakers, and
filtered, authorized anchor lookups address the reported omission and repeat
behavior without schema changes. The new resource specs cover multiple pages,
ties, nonmonotonic values, scopes, and terminal pages. No authorization bypass
was found.

The PR is not ready to merge in its current form because the existing PHP
WebUI sends a first-page sentinel rejected by the new API. Review findings:

1. **Blocking — initial WebUI requests fail.**
   `webui/forms/networking.forms.php:924` and
   `webui/forms/backup.forms.php:115` send `from_id=0` on initial IP assignment
   and NAS backup requests. HaveAPI accepts zero and calls the pagination
   block; `api/lib/vpsadmin/api/resources/ip_address_assignment.rb:120-122`
   and `api/lib/vpsadmin/api/resources/dataset.rb:18-20` then look for row ID 0
   and return HTTP 400. Preserve zero as a first-page sentinel in the API and
   add focused `from_id=0` specs. Updating only the PHP caller would leave
   other old clients exposed.
2. **Blocking — split the first commit's independent work.** Commit
   `de1cf7b06` bundles the IP assignment tuple cursor and VPS user-data ID
   ordering, which have separate implementations, tests, and consumers. Put
   user-data in its own commit. Keep dataset-family work in `ee81404ca`;
   fold `320af0e15`'s dependent IP locale changes into the IP commit. Remove
   `de1cf7b06`'s obsolete statement that the proposal awaits approval to open
   an upstream PR. Squashing the whole PR would obscure independent changes.
3. **Important — generated API descriptions are false.** The dataset,
   snapshot, and property-history Index inputs in
   `api/lib/vpsadmin/api/resources/dataset.rb:69-78,524-526,885-891`
   retain HaveAPI's generic `from_id` description about greater/lower IDs.
   The new semantics use name/time plus ID and reject unavailable scoped
   anchors. Add action-specific descriptions in both catalogs and durable
   client guidance for ordering, filters, HTTP 400, rollout, and rollback.
4. **Important — PHP filters retain stale cursors.** The IP assignment and
   NAS backup filter forms preserve `from_id` when a user changes filters.
   The new API can reject the retained ID as outside the new scope. Clear the
   cursor and pagination history when filters change, and offer first-page
   recovery for deleted or stale anchors. The shared PHP `Pagination::System`
   does correctly use the last returned row ID for Next.
5. **Advisory — user-data PHP pagination still repeats page one.**
   `webui/forms/userdata.forms.php:9-24` renders `Pagination::System` links
   but does not forward `from_id` to the API. This predates the PR and needs a
   separate PHP WebUI follow-up if that page is expected to paginate.

## Consumers and rollout

The in-repository PHP WebUI needs a companion change or a compatible API
sentinel fix before API deployment. The open beta frontend PRs
[user-data #496](https://github.com/Kerrycek/clankerdev/pull/496),
[IP history #507](https://github.com/Kerrycek/clankerdev/pull/507), and
[storage #509](https://github.com/Kerrycek/clankerdev/pull/509) explicitly
depend on this backend revision; the latter two contain cursor and recovery
work but still describe joint live verification as pending. Deploy the API
contract before those frontend changes, and do not roll the API back beneath
them without accepting renewed pagination errors or omissions. No schema,
on-disk format, node protocol, or Nix module change is present. Existing
snapshot rows may have null `created_at` because the schema allows it; verify
production data or handle such anchors before claiming complete traversal.
Issue [#189](https://github.com/Kerrycek/clankerdev/issues/189) remains broader
than this PR, including SnapshotDownload ordering.

No PHP label or layout change is in PR #44 itself. If the companion WebUI work
changes visible help, labels, or screenshots, follow the
`vpsfree-kb-contracts/docs/webui-change-workflow.md` contract and review the
affected Czech and English KB material.

## Verification and review provenance

- `git diff --check` for the exact base/head passed.
- PR description reports 133 focused Ruby examples and clean RuboCop at
  `ee81404ca`; current-head GitHub status showed 59 completed successful
  checks and one integration check still in progress at the last read.
- No new local integration test or deployment was run for this review.
- Overall risk: **high**, because public pagination and HTTP error behavior
  changes across API clients and deployment versions.
- Mandatory review lanes: general, architecture, scope/proportionality, and
  risk/compatibility. Independent reviewer
  `/root/mandatory_pr44_review`, standalone default-team review-role fallback,
  GPT-6 Sol with xhigh effort. The verified retained roster is solo.
- Review found no additional architecture, scope, or authorization defect.

Project documentation was checked at `vpsadmin/docs/README.md` and
`vpsadmin/docs/storage/README.md`. No project documentation was changed in this
review-only task; API contract and rollout guidance are recommended PR work.
