# 2026-07-20-security-advisory-review

## Goal

Register `security-advisories` in the workspace project map and prepare an
isolated feature worktree for reviewing security advisories against current,
typed vpsAdmin Node evidence once the user supplies an authentication token.
Investigate the production token-creation failure, fix it, then complete an
evidence-backed review of every advisory against every active Node.

The current follow-up shortens advisory summaries to the historical localized
vulnerability-class title, removes repeated generic Node notes, and adds an
explicit bilingual note contract for genuinely exceptional per-Node
circumstances. It also adds localized Node-note storage and presentation to
vpsAdmin, with an explicit deployment boundary because the normalized schema
does not retain the legacy single-note column.

## Affected repositories

- Top-level coordination repository: project-map documentation only, committed
  directly on `master`.
- `security-advisories`: isolated review branch and worktree, initially with no
  source changes; inspect the exact requested token scopes and client payload.
- `vpsadmin`: inspect the deployed token table schema and API integration.
- `haveapi`: inspect token option/scope serialization and validation used by
  vpsAdmin.
- `vpsfree-cz-configuration`: after the vpsAdmin fix is committed, reviewed,
  and pushed, pin the `vpsadmin` channel's `vpsadmin` role to that exact feature
  revision using `confctl`.
- Production vpsAdmin API data remains an external read-only review input; no
  production data changes are currently planned.
- `vpsadmin-kb-captures`: pin the localized-note WebUI revision and run the
  required bilingual documentation contract. No security-advisory binding is
  currently registered, so no screenshot or KB page change is expected.
- `vpsfree-notification-templates`: keep the managed Czech advisory mail label
  consistent with the approved `Ošetřeno` terminology. This repository does
  not consume per-Node notes, but its installed template can override the
  corrected built-in vpsAdmin template.
- `vpsf-status`: inspection only. Confirm that its advisory/status views do
  not consume per-Node advisory notes before concluding that no change is
  required.

## Approach

1. Add `security-advisories` to the top-level `AGENTS.md` project map.
2. Fetch its canonical SSH bare clone and create
   `2026-07-20-security-advisory-review` from the current upstream default
   branch in the matching initiative worktree directory.
3. Keep the authentication token ephemeral: do not write it to initiative
   notes, repository files, command-line URLs, commits, or captured output.
4. After the token is supplied, verify its identity and permissions, inspect
   the repository's API and evidence documentation, then perform the requested
   read-only advisory review against typed vpsAdmin data.
5. Do not synchronize drafts, modify vpsAdmin data, or publish advisories
   without a separate explicit user request and the repository workflow's
   required review gates.
6. Trace the reported `tokens.opts` overflow from the advisory client's scope
   list through HaveAPI serialization to vpsAdmin's schema. Reproduce the size
   boundary locally if possible and report the root cause and safe remediation;
   do not implement a fix unless requested.
7. Implement the requested vpsAdmin fix as one focused commit containing the
   reversible schema migration, core schema update, migration coverage, and
   end-to-end long-scope MFA token regression coverage.
8. Run quick focused verification, commit the complete vpsAdmin change, and
   push the feature revision so the configuration flake can resolve it.
9. Set the `vpsadmin` channel's `vpsadmin` role to that exact revision with
   `confctl inputs channel set --commit` and verify the generated configuration
   commit.
10. Run the mandatory standalone change review over both committed repository
    changes before broader tests. Address significant findings, then run the
    broader verification and push the final configuration branch.
11. After authentication is available, collect one canonical typed evidence
    snapshot and assign every advisory to its own fresh standalone reviewer.
12. Classify storage Nodes by their backup/NFS workload. They do not host VPSes
    and an older kernel does not make them affected by a VPS-only trigger;
    storage is applicable only when the vulnerable operation is reachable from
    its real storage workload.
13. Independently cross-check each reviewer result, resolve all active Nodes,
    validate every dossier, and run the complete test and lint suites. Do not
    sync or publish vpsAdmin drafts without a separate explicit request.
14. Commit and push the reviewed dossier and workflow-instruction changes only
    after the mandatory standalone change review has no unresolved significant
    findings.
15. Replace the ignored per-CVE evaluation cache with a tracked
    `advisories/<CVE>/evaluation.json` review record. Keep raw production
    evidence ignored, and compare fresh in-memory evaluation results with the
    committed record before sync or readiness can proceed.
16. Normalize English and Czech public text into the same factual structure;
    remove generic user non-action statements, editorial first-person language,
    and internal storage-role explanations from public fields.
17. Recollect one coherent production snapshot after the dossier text is final,
    regenerate every tracked evaluation, run mandatory standalone review, and
    push only after the complete local and GitHub checks pass.
18. Restore the useful kernel-warning monitoring note with one factual English
    and Czech sentence on the four memory-lifetime advisories, while keeping the
    non-UAF overwrite advisory unchanged.
19. Treat periodic sample revisions and their raw evidence digest as audit
    provenance rather than conclusion drift. Before a draft write, continue to
    require the exact Node set and all per-Node result fields to match the
    committed review.
20. After standalone review, complete verification, push, and green GitHub
    checks, synchronize all five reports to vpsAdmin as drafts. Verify every
    remote draft against the committed dossier and evaluation; do not publish.
21. Replace advisory summary sentences with the historical English/Czech
    `Local privilege escalation` title and require future summaries to remain
    short vulnerability-class titles.
22. Remove evaluator-generated generic Node notes. Allow only explicit
    dossier-authored English/Czech notes for exceptional individual Nodes;
    retain detailed evidence reasons in the tracked evaluation.
23. Add localized Node-status note translations to vpsAdmin. Remove the
    legacy `note` API field instead of retaining an English alias. Migrate its
    data into English translation rows and remove the old column. On rollback,
    recreate the column from English rows before dropping the translation
    table; Czech notes are intentionally lost because the old schema cannot
    represent them. Make the WebUI select the current language with English
    fallback.
24. Permit the advisory reconciler to clear empty notes through the deployed
    legacy API, but require the localized API before syncing any non-empty
    bilingual note. Migrate existing submission baselines without hiding remote
    review drift.
25. Run the vpsAdmin KB contract against the exact feature revision and inspect
    the renamed `vpsfree-notification-templates` advisory templates and
    `vpsf-status` advisory consumers. Do not deploy vpsAdmin, change
    configuration channels, stage KB content, or publish an advisory in this
    follow-up.
26. Narrow date and localized-note inputs in both the embedded new-advisory
    Node table and the standalone existing-advisory Node table. Cover bulk and
    per-Node rows, and update browser fixtures to use the translation table
    instead of the removed legacy column.
27. Standardize Czech advisory mitigation wording on `Ošetřeno`, document the
    approved examples in vpsAdmin and security-advisories instructions, and
    remove `Mitigováno` from advisory UI, mail, and test examples.
28. Fix the unrelated publish-form alignment in its own commit by storing the
    content revision outside visible table cells. Redeploy the development
    cluster for visual review, but keep default-branch integration and the
    production configuration channel paused until the user approves the UI.
29. Address mandatory review by separating localized browser/VM fixture repair
    from the input-width commit and correcting the canonical managed Czech mail
    template. Re-pin the rewritten exact vpsAdmin head, re-review the complete
    committed series, and only then run the long browser integration test.
30. After user visual approval, integrate every reviewed feature branch into
    its current upstream default by fast-forward from a fresh temporary
    worktree. Update the `vpsadmin` configuration channel through `confctl`,
    build the complete vpsAdmin configuration group, push the generated commit,
    and remove only the temporary integration worktrees. Do not deploy the
    production configuration.
31. Correct the five production draft reports after default-branch integration:
    keep the historical short vulnerability-class summaries, move any lost
    subsystem or trigger detail into the bilingual descriptions, and clear all
    repeated generic Node notes. Re-evaluate changed dossiers, review and test
    the committed report data, then synchronize with revision preconditions and
    verify that every advisory remains an unpublished draft.
32. Clarify that the GhostLock research demonstrated host root from a container
    on Google's Linux 6.12.80 kernelCTF target, while cross-container access is
    a separate untested post-compromise step. Use lowercase `node` consistently
    in all public English prose, refresh the evaluations, and reconcile the
    five drafts without changing their Node conclusions or publishing them.
33. Grant newly issued repository tokens the distinct
    `security_advisory#publish` action scope, while recording that the scope is
    never exercised without explicit user approval for the exact advisory and
    content revision. Treat email notification as a separate external action
    that also requires explicit approval. Issue a replacement token to a
    temporary path, verify its effective publication authorization without
    publishing, revoke the old token, and only then install the replacement at
    the standard path.
34. After explicit user approval, publish the five exact reviewed revision-28
    drafts with publication time `2026-07-21 22:00 Europe/Amsterdam` and
    `send_mail: false`. Do not refresh evidence when the user explicitly asks
    to publish the already reviewed records. Require immediate remote
    state/revision preconditions before each write and read back every resulting
    publication state and timestamp.

## Compatibility and deployment

The initial preparation changes only workspace documentation and creates Git
worktrees. The later review is intended to be read-only and therefore must not
change production state.

The advisory review changes local dossiers and assessment instructions only.
Evidence collection is read-only, ignored runtime state. Role-based exclusion
of storage Nodes is compatible with existing evaluations because every active
Node remains present in the output; only the real attack surface determines
whether its kernel history is applicable. No vpsAdmin draft synchronization or
publication is part of this stage.

The per-Node evaluation is now a committed review artifact rather than an
ignored short-lived cache. Its schema remains unchanged. A reviewed evaluation
does not expire solely because of age: `sync --apply` and `ready` collect fresh
evidence and require the current Node set and every per-Node conclusion field to
match before proceeding. Periodic sample revisions and the resulting evidence
digest remain audit provenance but do not by themselves change a conclusion.
This changes no vpsAdmin API, database, or protocol and remains safe for mixed
repository versions.

The authorized synchronization creates or updates vpsAdmin records only in the
`draft` state. It uses stable external IDs, remote content-revision checks, and
read-back verification. Draft creation is reversible through the ordinary
draft workflow and has no Node or VPS runtime effect. Publication is excluded
and remains a separate administrator action.

The final report correction changes only user-facing draft text and clears
redundant note translations. It does not change the API schema, Node
conclusions, affected intervals, CVE associations, or running infrastructure.
Descriptions retain the vulnerability-specific subsystem and primitive that no
longer fit in the summary. Empty Node notes are intentional because no active
Node has a distinct live patch, BPF program, or other exceptional mitigation.

The GhostLock clarification and lowercase terminology follow-up is likewise a
draft-text-only change. It makes the demonstrated kernelCTF result and the
inferred cross-VPS consequence explicit, without changing impact
classification, evidence, or runtime state.

Adding the publication action changes only the scopes requested for newly
issued repository tokens; existing tokens are immutable and keep their old
authority until rotated. Rotation must avoid overwriting the only copy of the
old credential before it is revoked: issue and verify the replacement at a
temporary mode-0600 path, revoke the old token through its saved file, then move
the replacement into place. The repository continues to have no automatic
publish command, and publication remains gated by explicit user approval and
the API's exact content-revision precondition.

Publishing intentionally changes the five vpsAdmin records from `draft` to
`published` and creates their affected-VPS snapshots. It does not change their
reviewed text, CVEs, Node statuses, content revision, or runtime infrastructure.
Email notification is disabled explicitly. Publication is externally visible;
the ordinary retraction workflow can supersede a report but does not erase the
publication event.

Localized Node notes replace the single `note` column with a translation table.
Migration up copies every non-empty legacy note into the English row before
removing the old column. Migration down recreates the column, copies English
back, and then drops the table; Czech translations are intentionally lost
because the old schema cannot represent them. Old API code reads and writes the
removed column, so the database migration must run only after all old API and
WebUI processes have been stopped or drained. New code and the migration must
be activated as one coordinated service boundary rather than a rolling
mixed-version deployment. Current draft rows will contain no notes, so this
follow-up creates no Czech rollback loss. The security-advisories client can
clear legacy generic notes before deployment, but does not silently flatten
non-empty bilingual notes.

The investigated failure requires a vpsAdmin schema fix before the review token
can be issued through MFA: widen `auth_tokens.opts` from `VARCHAR(255)` to
`TEXT`, retain its existing JSON serialization, and add a long-scope MFA
regression test. This is backward-compatible with old API processes because
they read and write the same JSON value. Deploy the migration before retrying
token creation. Pinning the `vpsadmin` channel updates the vpsAdmin service
containers together, including the API and database migration service. A
rollback to `VARCHAR(255)` is unsafe while any continuation row contains more
than 255 characters. Authentication continuations expire logically after five
minutes, but their rows remain until `vpsadmin:auth:close_expired` removes them.
Before rollback, wait for expiry and successful cleanup or explicitly close the
temporary rows, then require `SELECT COUNT(*) FROM auth_tokens WHERE
OCTET_LENGTH(opts) > 255` to return zero. Assess the ordinary MariaDB DDL lock
before applying the column change. No HaveAPI, vpsAdminOS, node, protocol, or
client rollout is required.

## Testing plan

- Verify the top-level documentation diff contains the intended project-map
  entry while preserving unrelated shared-worktree edits.
- Verify the advisory worktree uses the initiative branch at the fetched
  upstream default-branch commit and starts clean.
- Record exact branch, worktree, base commit, commands, and results in
  `state.md`.
- Reproduce the exact 34-scope request against the current vpsAdmin test schema
  with MFA enabled and confirm the `auth_tokens.opts` overflow.
- Run the existing focused token-config spec to establish that current coverage
  remains green despite omitting a long-scope MFA case.
- Run the new migration spec in both directions, the focused token-config spec,
  migration-spec inventory check, `git diff --check`, and applicable Overcommit
  hooks before committing.
- After standalone review, run the broader relevant API spec groups and verify
  the configuration channel update through `confctl` evaluation/build checks
  appropriate to the affected vpsAdmin service machines.
- Verify authenticated collection returns every active Node without revealing
  the token, then evaluate all five dossiers from one fresh snapshot.
- Require one fresh standalone reviewer per advisory and independently inspect
  every resulting accepted build, historical attestation, per-Node state, and
  role-based exclusion.
- Run `bin/security-advisory validate` for all advisories, evaluate all five
  against a final fresh evidence snapshot, and run full RSpec, RuboCop, and
  Overcommit checks before committing.
- Verify `evaluate` writes beside the dossier, missing reviewed evaluations fail
  closed, old matching records remain usable, and fresh mismatches block both
  apply and readiness without rewriting the committed record.
- Verify all five tracked evaluations contain the exact 13 reviewed Node IDs,
  resolved completeness summaries, matching dossier/evidence digests, and the
  storage Node as `not_affected`.
- Verify every English and Czech response uses the shared status closing and no
  public field contains generic non-action, editorial first-person, or internal
  storage-role wording.
- Verify all five localized summaries exactly match the historical privilege-
  escalation title and all current public Node notes are absent.
- Verify the descriptions still identify nf_tables corruption, the GhostLock
  futex escape, the epoll race, the KVM shadow-paging use-after-free, and the
  crafted UDPv6 overwrite in both languages.
- Verify the GhostLock description names the Linux 6.12.80 kernelCTF target and
  says explicitly that the researchers did not test the cross-container step.
  Require lowercase `node` throughout every public English summary,
  description, and response.
- Dry-run each production reconciliation and require that it contains only the
  reviewed parent-text update and clearing of the 13 generic Node notes. After
  apply, read back every draft, rerun readiness, and confirm the Node states and
  intervals are unchanged and no publication timestamp exists.
- Verify explicit per-Node notes require both languages, remain short and
  single-line, and are reproduced by fresh evaluation rather than hand-edited
  in the tracked JSON.
- Verify migration of existing English notes, removal of the legacy column,
  rollback restoration of English with intentional Czech loss, localized API
  round trips, bulk translation loading, rejection of the removed legacy
  field, WebUI locale selection, English fallback, and bilingual administrator
  inputs.
- Verify legacy submission digests are accepted only for the exact old remote
  snapshot and are upgraded after a successful checkpoint; actual remote drift
  must still stop synchronization.
- Pin the exact vpsAdmin feature revision in `vpsadmin-kb-captures` and run its
  contract. If it reports a security-advisory page or screenshot binding,
  review and regenerate precisely that Czech/English material; otherwise keep
  KB production untouched.
- Verify the four memory-lifetime advisories use the exact bilingual monitoring
  sentence and the non-UAF advisory does not.
- Verify fresh sample/evidence revisions are accepted only when the exact Node
  set and every per-Node conclusion field remain unchanged.
- Dry-run all five synchronizations, apply them only after the committed branch
  passes review and CI, then run `ready` for each draft. Confirm that every
  remote report remains a draft and matches local content and Node results.
- Verify the embedded and standalone Node-status forms use size 14 for both
  date and localized-note inputs in their bulk and per-Node rows.
- Verify localized browser fixtures create translation rows and exercise both
  `en_note` and `cs_note`; no integration fixture may write the removed `note`
  column.
- Verify the publish form has exactly one hidden content-revision input and its
  publication-time row begins with the visible label rather than an empty
  table cell.
- Verify Czech security-advisory wording uses `Ošetřeno` consistently and the
  translation instructions explicitly reject `Mitigováno`.
- Verify the configured and documented scopes include exactly
  `security_advisory#publish`, issuance sends that scope, and repository policy
  requires explicit user approval for the exact revision plus separate
  approval for email. Verify a replacement token's effective action authority
  without invoking publication before revoking the old token.
- Before publishing, verify IDs 6 through 10 are still the expected drafts at
  revision 28. Publish each with the exact revision precondition, timestamp,
  and `send_mail: false`, then read back all five as revision-28 publications at
  the equivalent UTC instant.
