# Advisory read visibility correction

## Approved contract and evidence

The user explicitly agreed to hiding retracted advisories from every non-admin,
retaining administrator history, and keeping direct retraction silent. This
supersedes any earlier public-retraction behavior. Only `published` advisories
are public/member readable; both `draft` and `retracted` are admin-only.
The user's subsequent correction is authoritative: “visibility is handled by
the server completely. the UIs shows what the server sends them, it is useless
to implement retracted advisory hiding also in UIs”. The API is the sole
visibility authority. This removes the proposed additional UI filtering,
render/cache guards and public-route restrictions for administrators.
The user also authorized updating this session's development preview with the
fixed, reviewed sources. Production, default-branch integration and session or
cluster reset/stop remain outside this package.

Inspected starting sources are vpsAdmin `49f5a29e5a7d85559d06d31496acb5c08895bcda`
and modern WebUI `1c8478bceb3943645ec06ccde895ee4b0985873f`. Anonymous reads of
the own preview confirm IDs 2 (published) and 3 (retracted) in the API list,
ID 3 Show returning 200, and ID 1 (draft) Show returning 404. Draft exposure was
not reproduced; retain negative draft regressions. Implementers have additional
same-preview role-matrix evidence; record their exact commands/results with
implementation acceptance rather than treating reports as new product scope.

| Reader | Published | Draft or retracted |
| --- | --- | --- |
| Anonymous | Public report and public relations | Detail 404; absent from lists and relations |
| Member or support | Same public report; existing own-resource limits remain | Detail 404; absent from lists and relations |
| Administrator | Existing authorized access | Existing authorized access and history retained |

Existing action authorization, token scopes and field restrictions still apply.
A hidden parent must not leak through child Show, list rows, counts, includes,
pagination cursors, affected-user/VPS projections or advisory-filtered outages.
Hidden direct resource reads return the ordinary not-found response; scoped
collection queries return no hidden rows. Resource-input validation can use its
existing error convention, but cannot return hidden report or relationship data.

## API package — implementer0

Change the existing `SecurityAdvisory.visible_to(user)` in
`api/models/security_advisory.rb`: admins retain `all`; everyone else receives
only published rows. Do not invent a new permission framework or endpoint.
The following proven consumers already use this scope and must retain it:

- `api/lib/vpsadmin/api/resources/security_advisory.rb`: Index, Show,
  pagination cursor and nested NodeStatus Index.
- `security_advisory_cve.rb` and `security_advisory_update.rb`: Index/Show.
- `user_security_advisory.rb` and `vps_security_advisory.rb`: projection lists,
  together with their existing user/owner restrictions.
- `plugins/outage_reports/api/resources/outage_security_advisory.rb`:
  Index/Show, together with the outage's own visibility scope.

Intersect Outage Index's `security_advisory` filter in
`plugins/outage_reports/api/resources/outage.rb` with the same parent visibility
scope. Its existing join does not explicitly apply that scope. Cover this
concrete reverse relationship with request tests, including authorized admin
access. Test flat filters using the actual HaveAPI resource wrapper so an ignored
query parameter cannot create a false pass. Existing child/includes regressions
prove the connected owners; no further architectural investigation or generic
transaction/history overhaul is part of this correction.

Legacy PHP already reads through these API owners. In
`webui/forms/security_advisory.forms.php`, the list forwards filters and detail
loads the parent before children; the dashboard already requests published.
Leave its implementation unchanged. Verify guest/member direct URLs, lists and
related links against the corrected API, including ordinary not-found handling,
published public access and full authorized admin access. Existing legacy
browser coverage is in
`tests/playwright/webui/specs/security-advisories.spec.cjs`. UI acceptance reads
the server's authorized results; it does not add local hiding or malformed-server
fixture defenses.

Update `docs/security-advisories.md` with the read matrix and intentional loss
of non-admin access after retraction. Retraction still keeps original content,
publication information, update posts and projections; direct retract sends no
mail. Separate update announcements retain their explicit mail option and their
existing mutation contract. Parent visibility controls reading those posts.
Deletion remains the separate permanent operation. No revision, locking,
publication, correction, draft-sync or storage semantics change here.

## Modern restoration and UI acceptance — implementer1

The previous 15-path React visibility candidate is **SUPERSEDED by the user's
server-only decision**. Implementer1 completed the exact `f7` candidate →
`1c8478bceb3943645ec06ccde895ee4b0985873f` restoration. The lead confirms the
peer receipt: exact `1c8478bc` is pushed and clean. Preserve that receipt's
ref/equivalence evidence and the previously accepted advisory editing/lifecycle
implementation at that exact head and its existing PR scope.

Do not deliver the candidate's additional list filters, published-only render
or child-query/cache guards, defensive mock tests, or related product-doc changes.
Do not impose a published-only public-route rule on admins: the API retains
authorized access to all states and the existing UI displays its responses.
Keep existing routes, queries, cache ownership, transport and behavior at the
restored head. No client-side hiding, cache framework, generated client or BFF
change is required.

Verify the unchanged modern UI against the corrected API with ordinary read-only
guest/member/admin navigation and direct links. These are server-policy acceptance
checks, not a new UI implementation package. No new modern documentation or code
changes are authorized by this visibility delta.

## Checks and delivery order

Both owners follow current repository procedures and preserve existing hooks.
Implementer0 solely owns API, legacy and KB work, including their Git operations
and KB pin refresh. Implementer1 owns the completed modern restoration.
API and KB committed deliverables
still require their affected checks/review before the authorized preview update.

Before review, run the focused visibility regressions, touched Ruby lint and
declared hooks. The full multi-file API commands below are longer checks and run
after the affected committed-source review, not as the quick pre-review gate.
The lead reports API `a38c` and KB pin `4fd4` committed and quick checks complete,
with affected review about to be assigned; neither production nor preview
activation is recorded by this checkpoint.

The API shell starts in `api/`. Extend existing specs rather than a new test
framework. The role/state matrix must cover list and direct Show, explicit state
filters, representative counts/cursors, CVE/node/update children and their
includes, authenticated projections, outage links and the reverse outage filter.
Verify admin access and published access, not only denials. Any targeted model
or lifecycle assertion also proves retraction retains history/projection rows
and remains silent; reading changes must not mutate content or revisions.
Run touched Ruby lint and declared hooks. Keep spec topic coverage unchanged.
The exact modern restoration can use existing exact-head verification evidence;
do not rerun the superseded candidate's test/build campaign as a new deliverable.
Long/uncertain required checks use a fresh Luna/low verification watcher under
the existing monitor procedure.

After committed-source quick checks, the lead arranges the mandatory affected
final review, including the complete final branch history and disposition of the
superseded UI candidate. Then run the full multi-file API coverage in both modes:

```sh
VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb spec/api/plugins/outage_reports/security_advisory_spec.rb
VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
```

Relevant existing legacy browser coverage can run with
`./test-runner.sh test 'webui#security-advisories'`. The real-preview read-only
UI checks below establish that both unchanged UIs consume the server policy;
browser fixtures alone are not API authorization proof.

Follow the mandatory canonical KB workflow already specified by package D in
`design.md`: after final vpsAdmin source is pushed, refresh the owned contract
pin and run the full strict `nix develop -c bin/check`. The established advisory
forms have no page/capture bindings; do not fabricate them or fetch unrelated KB
content/screenshots. Record actual check impact and any pre-existing drift.

The lead releases the reviewed API source and exact restored modern `1c8478bc`
preview update to implementer0/1 using the existing provider and retained data.
Verify source/runtime
provenance, then repeat read-only acceptance for IDs 1/2/3 using verified TLS:
anonymous, member/support and admin API cases; guest/member list/direct URLs in
both UIs; related children/links; admin retained history. Confirm normal OAuth,
published public rendering and no new advisory mail caused by this correction.
Use ordinary portal credential access without copying credentials into evidence.
Existing preview stays running; no reset or new fixtures are required merely
to repeat the known state matrix. No screenshot campaign is needed to prove a
new UI change: no new UI behavior is delivered by this delta.

## Compatibility and recovery

This deliberately changes the previous public retracted-read contract: old
public links become unavailable and public/member lists, feeds and related
resources omit retracted reports. Admin content and history remain intact.
No schema, persisted-format, protocol, daemon, Terraform or draft-sync client
change is required. Existing admin client access remains subject to its scopes.

The corrected API enforces the policy for both existing UIs. Modern source stays
at exact `1c8478bceb3943645ec06ccde895ee4b0985873f`; no companion UI upgrade is
required. Mixed old/new API instances cannot guarantee the policy. Previously
delivered browser content or mail cannot be recalled; this does not authorize
client cache redesign or duplicate UI visibility enforcement.
Software rollback remains data-compatible but restoring the old server policy
would re-expose retracted reports, so do not treat it as a privacy-preserving
recovery. Preserve the read-scope fix during recovery. No data migration/reset.

No product decision remains open. The modern restoration is complete. Finish
affected review and the ordered API/KB checks, then verify both UIs against the
reviewed preview API after its authorized update.
