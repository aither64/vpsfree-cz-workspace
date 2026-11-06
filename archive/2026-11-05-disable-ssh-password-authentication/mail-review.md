# Independent final review: Alpine notice

Final full range `2fdc9f2889ac419136cd0cde0e0955c015ae7107..858b18811c9363fe6c2fd875b224a813d8e360d4`.
Original mail commit reviewed: e652e5b5cf24553ec71c9f4807ae9d99ac534121.
Reviewer0, thread01a1ac18-8de0-7551-9d54-4498d1ffd8cd, retained
review-purpose/read_only, gpt-6.1-sol/xhigh; session/env/live roster verified,
no overrides/fallback/nesting/writes. All four mandatory-review lanes completed.
Reviewer delivered report through session transport; lead persisted it.

## Findings and exact remediation

F3 Blocking, general/architecture: original includes(:pool) was invalid because
Vps#pool is a Ruby helper delegating to dataset_in_pool.pool, not an AR association.
Would raise AssociationNotFoundError for eligible rows. Corrected final line60
preloads actual dataset_in_pool: :pool chain. Original mock accepted arbitrary includes.

F2 Important, general/runtime: returning with no messages left empty Custom chain,
which actual TransactionChain.fire2 rejects unless allow_empty?. Corrected final
line55 declares allow_empty, allowing framework to destroy empty chain/noqueue.
Original fixture omitted actual empty-chain gate.

Exact remediation is only those two source hunks, folded into owning mail commit;
SSH parent unchanged. Reviewer and lead independently inspected complete old/new
diff. Strengthened fixture rejects old variants and models actual empty gate.
Three focused cases pass (~1s): zero-recipient default/execute successful/noqueue,
old noallowempty/invalidpool variants fail, nonempty preview/execute behavior retained.
Ruby syntax and full-range whitespace pass. Narrow requested fixes introduce no
new design/scope; lead direct verification under skill step9, no separate rerun.
No other findings; no remaining Blocking/Important/Advisory finding.

## Scope, correctness and risk

Bounded one-off task, five files/306 added lines: entry, 47-line parser,
CS/EN templates and README. No generalized parser/mail/override/dedup framework.
43 explicit script changes plus manually fixed30231 with operator-confirmed backup,
all current active-owner/active-Alpine/running/valid-status/pool filters applied.
30231 requires exact failed dozer evidence, not merely fixed ID. Other five failed
VPS excluded; no failed-VPS prose. No unrelated paid/environment/mailer filters.
One email/user, deterministic order, CS/EN/fallback; all bodies rendered before
mail preparation. Actual current-status/pool/model contracts verified in vpsadmin
b4ef8535a629ee8c9cd753afecdb05e0895d0eea. No scope/milestone concern.

Parser requires explicit terminal results, excludes incomplete, coalesces identical
repeats, aborts contradictory identity/outcome evidence before API load. Real
TransactionChain.fire2, mail_custom, MailTemplate.send_custom and TemplateBuilder
independently read: preparation/linking inside requires_new DB transaction;
nonempty default preview raises outside rescue, rolls back; only literal execute
permits queueing. Preview ERB trim mode matches real builder. Existing admin-role
recipient resolution and podpora sender/reply-to used. Execute reruns can duplicate
sends; mail cannot be undone by source rollback, accurately documented.

## Copy and verification

Committed templates independently byte-match lead final candidates. Writing skill
and both humanizers applied/reviewed. Exact '*' shadow-field/no usable password,
another real-password account, enabled SSH password auth and no-PAM context retained.
Precautionary wording does not imply detected compromise or vulnerable account on
every VPS. Confirmed changed list/backup includes manual30231. No failed discussion.
Key upload AND later deployment to existing running VPS, console access, localized
KB links, updates/restart/log review and restore implications present.

Primary sources independently retrieved: official OpenSSH release-10.6p2,
sshhole.com, both CS/EN SSH and console KB pages. No copy findings.
Independent syntax checks (original and final) and final full diff whitespace pass.
Isolated parser run read-only on external input:50 records=43changed/6failed/
1incomplete/0unchanged;44candidateVPS after manual correction, not44live recipients.
Original six grouped mocks inspected; their two missed runtime contracts corrected
as above. No write-producing fixture run by read-only reviewer. No live DB, delivery,
current-recipient count or fresh node/policy proof. Historical node/ownership cannot
be proved from log+globalID/currentpool; README requires operator preview. No raw
private attachment/recipient manifest embedded in source.

Standalone dated Custom task fits architecture; framework owns mail/transactions,
parser owns classification. No hidden cross-project interface or drift-prone policy
duplication. Localized equivalent prose intentionally separate.

## Whole-branch and migration conclusion

Independently inspected complete series/final diff, exact merge base. Exactly two
coherent commits: SSH2e7c9add2958e614a77e96236e92c55c8b22ad5c, then mail858b188.
SSH directory byte-unchanged from reviewed head; completed SSH review reused.
User reported node execution without exact deployed-SHA proof; no rewrite/lineage
claim needed. Original maile652e5b is provenance outside final series.
No obsolete approaches/fixups/transitional paths/history. No migrations or migration
lineage. No repeated dependency/channel/input/generated streams/pins or consolidation
needed. No API/schema/daemon/module contract or deployment ordering change. New mail
task not run/released/deployed here. Task-prefixed commit split appropriate, final
tree clean. High risk remains appropriate. Integration/sending require separate
user action; this review grants neither.

## Final copy-only addendum: 8b90ad54, passed

Same retained reviewer0 freshly verified session/env/roster, saved
read_only gpt-6.1-sol/xhigh and same thread; no overrides/fallback/nesting/writes.
General/copy and risk/factual lanes completed for exact858b188..8b90ad54f6c5450a207da89eb1d344582c372e84.
Prior architecture/scope/logic review reused. No findings.

Only two templates changed (19 insertions/27 deletions), matching requested two
sentence/paragraph removals, qualified stored-hash wording, redundant outer guard
removal and wrapping. Equivalent CS/EN facts/register retained. Precautionary framing,
'*'/no usable password, no-PAM/enabled-password-auth conditions, confirmed VPS list
and backup, update/restart/log advice, keys/deployment and localized links remain.

Independently read primary V_10_6_P1 auth-passwd.c and openbsd-compat/xcrypt.c:
one-character '*' leaves null salt; pick_salt scans dollar-prefixed stored hashes,
else DES fallback. Source-based inference supports 'described attack' needing
another stored hash, without requiring plaintext knowledge or usable login for
that other account. No universal exploit-test claim.

Removed outer guard is redundant: unchanged caller skips empty VPS sets before
render and changed_vpses equals nonempty qualifying list. Independently proved
Ruby source/filter/parser/README/SSH directory unchanged; F2/F3 remain intact.
Rendered exact committed templates in memory for single/mixed script/manual
fixtures using real ERB trim '-', correct lists/backup, removed paragraphs absent,
no residual ERB; exact lead-copy equality, complete diff whitespace and clean tree
pass. No live DB, delivery or production action.

Whole final range base2fdc9f2889ac419136cd0cde0e0955c015ae7107..8b90ad54f6c5450a207da89eb1d344582c372e84:
exactly two coherent commits, SSH2e7c9ad and consolidated mail8b90ad54. Earlier
mail858b188 is review provenance outside final series. No obsolete history,
fixups/transitional paths, migrations/lineage, repeated dependency/input/generated
streams/pins or consolidation needed. Runtime/provenance limits unchanged: no live
recipient-count/DB/send proof, log lacks historical ownership/node identity, execute
can duplicate mail. No further review rerun/optional wording recommended.

## Exact user-requested tone refinement: direct verification

Reviewed predecessor8b90ad54f6c5450a207da89eb1d344582c372e84 -> final
73165032bec0e2eb89e577b6ee3f799cf6449dd9. User requested replacing urgent CS
imperative with Doporučujeme systém aktualizovat; English matched to We recommend
updating/restarting. Lead applied writing skill directly and inspected full diff:
only these requested prose lines. Facts/recipient/interface/source/README/SSH parent
unchanged. Prior final independent review retained; bounded direct verification
under narrow-fix policy, no rerun merely to confirm exact requested wording.
Two focused render tests pass0.46s, byte equality/whitespacepass, cleantree; feature
exacthead verified overSSH and comparisonrefreshed. Same two coherent task commits,
no migrations/update streams/obsolete history introduced. No live DB or sending.
