# Approved-60 authenticated advisory preflight

Completed read-only inventory at 2026-10-19T21:11:59Z using the repository
APIClient/Config through Nix-provided Ruby. Session command and both environment
identity values match the assigned session and workspace. The credential file
exists, is owned by the current user and has mode 0600. No credential contents,
headers, exception bodies or raw production responses were printed or saved.

Authenticated GET and OPTIONS reads succeeded for security_advisories and
security_advisory_cves. The unfiltered inventory contains 56 advisories, all
published, and 57 CVE associations. No draft or retracted advisory was returned.
Both cursor streams end in an empty page. Advisory pagination uses descending
IDs; associations use ascending IDs. The server ignores offset pagination; an
earlier attempt detected repeated IDs and failed closed before accepting a
ledger. The completed ledger supersedes that attempt and the preliminary
status report. CVE associations use the API field cve_id, checked explicitly.

There are zero matches to the exact 60 approved CVEs in remote associations,
zero matching stable external IDs, and zero approved-CVE local dossier or
submission matches among the 51 inspected dossier directories. Every association
joins a returned advisory. The sanitized ledger records advisory/association
IDs, CVEs, states and content revisions, plus local dossier/submission IDs and
revision baselines. The approved input hash and exact repository revision are
recorded in [inventory.json](inventory.json). The read-only reproduction script
is [inventory.rb](inventory.rb); its saved hash identifies this run's code.

No existing matching record needs an adopt/update/replacement decision at this
snapshot. This is an inventory under the existing token's effective visibility:
it cannot prove records hidden by server authorization, and is not a transaction
reservation against later draft creation or edits. Revision preconditions and
fresh duplicate lookup remain required by the normal guarded sync workflow.
The phase-three dossier brief is not yet required for this bounded preflight;
it must be read when supplied before later assigned assessment work.

No Node resources, private Node evidence, source/index edits, tests, commits,
credential changes, remote create/update/delete/adopt/sync/publication or email
operations were performed. Only draft-preflight files were written.
