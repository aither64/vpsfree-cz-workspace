# 0.31 final review disposition

Retained reviewer0, purpose review, gpt-6.1-sol/xhigh/read_only, thread
`01a16f67-b886-7573-a065-dcf2f4b7c262`, verified exact session from tracking cwd
with both ambient markers absent. No model/effort override, fallback or nested
reviewer. Routine records below do not add a review gate.

## D4 bilingual KB

Final completed-deliverable general review of workspace commit
`7b9a1d4bbc1e17f36ad0b7b1ad663f25f58714f2`, parent
`03ed7537c04f2e3d319bf0df6bcd286136a42007`: no Blocking/Important findings.
Advisory D4-A1: linked SDK README demonstrates createVpsAdminClient, not the
real but unmentioned createClient export. Lead corrected that prose pointer in
each language, directly compared both pages to reviewed bytes and read the
published README; E3 regenerated/checksummed canonical guarded outputs without
repeating consumer tests. Narrow fix committed
`0019dd4e5e96afef4de0e0d2e1b573ad461e13fc`. No new behavior or review rerun.
[Current checks and exact hashes](kb-checks.md), [packet](kb-review-packet.md).
Reviewer independently accepted coherent one-commit range/no obsolete stream and
NO MIGRATIONS. Earlier coordinationmaster history stays immutable. Foreign
staging owner/pending release remains a blocker to rendered/history review;
production promotion requires exact staged approval.

## C4 React

High-risk carried auth/mutation boundary; final general, architecture/repetition,
scope/proportionality and risk/compatibility lanes all completed with NO findings.
Exact canonical vpsadmin-webui range
`5a2d2bdc3ad7a827038f877d75959916528db844..baf00acc31d34ab37720643c5833b4476a341f3b`,
dependency `4d040e0357e405761432075a23783b4d0d779432`, tree
`2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`, registered vpsadmin-webui-031.
Whole two-commit/73path branch reviewed, only ten metadata/technical-doc paths
differ from f10. Runtime, BFF, fixtures and guards match reviewed consumed f10.
Actual 53packed/installed/sourcefiles, npm integrity/provenance fields, normal
Nix hash and unchanged unrelated locks independently verified. Runtime-source
release delta only Client.Version; carried R2 uncertainty policy preserved.

Explicit history conclusion: final0.31 dependency stream consolidated directly;
no obsolete pins, transitional paths or fixups. NO MIGRATIONS/schema/persisted
session/protocol boundary. Live f10 and pilot are retained nonancestors, not
literally merged. Protected PR74 rewrite and defaults still unapproved.
[Packet](../package-c/0.31.0/review-packet.md),
[released proportionate checks](../package-c/0.31.0/postreview-plan.md).
Required postreview test/build/Nix/browser outcomes are separate evidence;
review is not deployment, publication, merge or overall readiness approval.

## A4+B4

Final four-lane review completed at exact canonical vpsAdmin range
`08c3bd7e3cb4dc324a0381df6a1eec190daab1a7..d258591f81e49365b02206dd184296f5f5e7d045`,
A `3f113098e8cdb90ad90426144f37594265b4a571`, tree
`c1b1b533ba286661cd41b97dab2ec3f40e4266b4`, clean vpsadmin-031. All four lanes,
high risk for public docs authorization/locale/cross-project SDK/package boundary.
Explicit complete-history conclusion: two coherent authored commits/29paths,
direct0.31 update stream, no obsolete pins/fixups/shims. Broad381-entry schema/
migration/seed comparison equal across feature and upstream refresh; NO MIGRATIONS.
No authorization/locale leak found; private structural model remains separate
from each request's authorized description. Released artifact/config/profile/
quickcheck evidence corroborated. No additional findings beyond A31-R1.

**A31-R1 IMPORTANT (open):** enabling TypeScript at api/lib/vpsadmin/api.rb:53
exposes provider c9124da/haveapi-typescript-client0.31 normalization at128/148/158/186.
Each generated action recursively copies the full authorized description at least
three times; authenticated examples commonly five. Page cost multiplies fullAPI
size by sample count. Static repeated copying established, absolute0.31 latency
unmeasured. Quick init/action checks do not prove full-page cost.
Provider-local shallow selected subtrees, preserving auth/collision behavior and
without cross-user/page cache, is the recommended minimum remedy. No consumer
workaround/renderer fork is accepted.

Lead explicit limited decision: permit ONLY the existing real role/locale GET
measurement at final d258 before broad suites, anonymous first then memberCS/
adminEN unless first severe result warrants escalation. Capture actual wall/CPU,
locks/source/visibility/locale. This investigates impact and does not close the
Important finding or declare readiness. Full/core documentation/services-up/
broad integration remain held. Architect owns minimum provider boundary; A0 owns
measurement/any later assigned source work. No reviewer timing/test/build/GET.
[Packet](vpsadmin/review-packet.md) and [receipt](vpsadmin/receipt.md).

## C4 browser and E4 operational gates

C4 units/build/Nix passes stand. Targeted browser first3/6, one corrected4CPU
run5/6; desktop expiry remains failed while genuine401/hardredirect succeed and
public lazy page remains Loading near assertion deadline. Exact source and185path
FHS closure unchanged, processes/port reconciled. No preexisting/green claim;
architect/C1 bounded disposition pending. No further blind rerun.

User separately authorized exact session devcluster reset/redeploy after gates;
[E4](../devcluster/e4-preparation.md) remains prepared only. No native reset/start,
Git path move, config restore, package install or staging takeover has occurred.

### Narrow A test-contract correction after review

Architect/lead source inspection confirmed old70a..2c documentation spec unchanged,
but d258 introduced an incorrect anonymous action-absence assertion. Anonymous
GET help deliberately shows full API (endpoint/current_user nil); memberCS
help remains filtered. Reviewer acknowledged this missed test-oracle finding.
A0 amended B to `9c1b3f773555faa1b4af2ee6b8e26f04a7a012f1` with normal hooks
PASS0/73.789s. Lead independently inspected d258->9c: exactly one file, one
line replaced with positive full-help assertion; member hidden actions/IP and
internal paths unchanged. Saved qualified body proves the changed expectation;
no repeat GET/core/full campaign. Direct narrow-fix inspection accepted, no full
review rerun. Old d258 retained under an own local provenance ref.
[Qualified actual measurement](vpsadmin/A31-R1-qualified-anonymous/receipt.md):
15.23135wall/15.21839CPU, verifiedanon200/fullhelp/EN, native1example0fail/exit0.
A31-R1 performance issue remains OPEN; broad suites/deployment stay held.
