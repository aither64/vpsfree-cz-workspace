# C final affected-lane review: authenticated shell storage

Reviewer0 returned: no Blocking or Important findings; one Advisory prose issue,
C-shell-1. No runtime correctness, mutation-permission or compatibility defect
was established. Prior full C/OAuth review remains applicable to unchanged
source, including accepted C-1. This record condenses the returned full report,
retained in the lead conversation as “Final affected-lane review — C
protected-shell storage correction”. It is not initiative readiness or merge,
deployment or release approval.

## Identity and exact range

Session identity and live reviewer verified: reviewer0,
thread01a2178b-ad92-7421-94c0-062258b3674b, saved Sol/xhigh/read_only,
purpose review. No settings override, fallback, nested reviewer or team change.
High risk; general, architecture/repetition, risk/compatibility, plus scope
limited to newly affected boundary. Current packet, source/tests, adjacent
lease/acquisition, representative consumers, docs and focused receipts inspected.
No tests/builds/services/writes/publication/integration/deployment performed.

Repository vpsfreecz/vpsadmin-webui, target main, dev/oauth-theme-20261126.
Basee311b1c0af0f50fa4c6f6ce83c514c1a866eb042 → reviewed clean successor
2b3e9c7e18d8e6465b364ead4ed9298aafba3b82,
tree3afcf6e08f10ebb27e4cfd509e71c6d34c1568a6. HEAD/tree/merge-base/index verified.
Complete one-commit series, auth: preserve appearance through OAuth login,
39files+1132/-153. Exact predecessora28c59c6..2b3e9c7e:7files+295/-42,
three runtime sources, two test homes and two docs only. Original OAuth/BFF/
entry/settings/cookie exchange and C-1 unchanged.

## Advisory C-shell-1

CONFIGURATION.md originally said acquiring a mutation lock requires verified
persistence before dispatch. Existing ordinary callers intentionally use
best-effort persistence, while durable:true selects the verified/refusing branch.
Qualify the reference to “a durable mutation lock”; do not change ordinary
behavior to match overly broad prose. Advisory only: no implementation
regression and durable acquisition remains guarded. Direct lead step9 inspection
suffices; no new full review.

Lead directly inserted exactly “durable” in the reference sentence after source
facts settled, using the writing skill. Exact working diff and whitespace checked;
exclusive window returned to owner for consolidation/identity/hooks/docs gate.
Final successor identity and docs-only equivalence remain to be recorded before
publication. No runtime suite rerun justified for this word.

## Independent runtime and scope conclusions

Actual native authentication/prepaint succeeded before the denied-localStorage
shell crash. Guarding optional display reads and obsolete local PIN cleanup is
necessary within accepted usable login return. No mutation redesign or optional
OAuth sessionStorage follows. Most growth is real-shell/integrity regressions;
existing reader moved to existing storage home is proportionate. No new format,
protocol/framework/dependency/state machine/permissions model. Structural and
lint rules not relaxed; no unrelated dependency-array refactor. Consolidation
with the newly supported denied-storage feature is appropriate.

AppLayout catches only obsolete localStorage PIN-removal failures, preserving
required sessionStorage cleanup. Initial failed display hydration yields no
known display guards and does not constitute durable permission. Existing
migration preserves legacy data unless durable migration can be proven.
Background read/orphan recovery failure retains displayed state without unhandled
rejection; lease/generation/marker/permission rules are unchanged. Pending/corrupt
guards remain non-expiring and non-acknowledgeable through the existing model.

Extracted readStorageEventDisplayLock recognizes existing area/prefixes, identifies
one object through existing key/inspection rules, re-reads current persisted
uncertainty/ordinary state instead of trusting stale event data, and returns a
bounded update/null verified absence/undefined unreadable-invalid refresh.
Called inside the functional updater with captured event timestamp, it preserves
previous state on unreadable refresh and other object locks on ordinary updates.
Uncertainty wins over ordinary; corrupt guards and verified expiry helper retained.
No new deletion/acknowledgement rule.

Durable branch and representative awaited callers were inspected. Denied getter/
getItem rejects before a generation capability or dispatch. persistGuard still
requires write/read-back; failed lease/persistence/missing Web Locks refuses.
No catch converts acquisition/write/removal/reducer/bind/settle/dispatch failure
into permission. Ordinary callers retain prior best-effort semantics; review
neither claims every mutation requires durability nor requests that expansion.

## Evidence, history and docs conclusions

Real AppLayout/settings/theme test uses opposite OS, successful cookie and
normal surrounding auth/API fixtures, covering denied getter and local-only
removeItem, authenticated menu/returned scheme/cookie consumption. Integrity
tests cover durable refusal, retained guards on failed background/event refresh,
current storage over stale event, target-only deletion and corrupt guard refusal.
Targeted retained-log inspection confirmed40passing across6files9.11s. Exacta28
lint comparison shows same4 inherited findings, moved helper/tests clean;
type/structural/docs/format/whitespace evidence remains scoped, no suppression
or debt exception. No successor native/package/CI result was claimed.

Complete current history contains one final logical commit, no obsolete approach,
fixup/shim/superseded update. Publisheda28 is explicitly nonancestor, used in
isolated verification/provisional E only; preserve exact old receipts without
calling artifacts successor builds or literal lineage merged. No migrations at
any checkpoint, none merged/released/deployed/externally consumed. No repeated
pin/dependency/generated stream or state conversion.

All3locks independently byte-identical a28..2b3:
package-lock.json eee6460485c5aea039721b682839b58d44ce19b7acb3e42f50c59650cd9d429d;
bff/package-lock.json 50ffa053cd8b22d78505d10117fa2a42db62f73f6aa0b6de18138cbca9277d5a;
flake.lock 6ea5fc4d9d7b43a6c4d6b18a70dc7206f3ba760053513215093b58e24721fa99.
No SDK/API/schema/stored lock/OAuth state/PKCE/session requirement or cosmetic
protocol change; upstream compatibility/recovery conclusions remain applicable.
E final inputs require actual successors and final graph/artifact evidence.

CONFIGURATION is the correct reachable durable reference home, subject to
C-shell-1 qualification. Required dated work-log correctly separates old checks,
real first success/failure, current correction, remaining review/rebuild/native
and unchanged production. No authentication/storage/account/session/rollback/
prerequisite/recovery guidance removed or weakened. Main writing pass recorded.
Placement/preservation: appropriate homes and truthful evidence separation.

Next: close exact prose finding, lead direct acceptance, publish accepted final
head, bounded artifact/CI/native checks. Fixture HOLD and deployment/integration
boundaries retained. [Owner evidence](C-evidence.md), [state](state.md).
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-oauth-dark-theme/

## Direct step9 closure

Final successor4f894ffc88870ef17f6982f775bd9460b26f3f7d,
treea7e1ab0049d50fa5877ce3bca0d7d43d5c74d605. Lead inspected exact2b3..4f diff:
only CONFIGURATION sentence adds “durable”,+1/-1. All runtime/test/other reviewed
files byte-identical; clean consolidated one-commit history on same base. Owner
docs/identity/staged-final whitespace checks passed; no hook framework declared
or bypassed. Evidence c-shell-final-source.json/c-shell-2b3-to-final.diff SHA256
f6b9f05d90e50d349926ca445da745aeda11c3f345e8407a57eb70530954e206.
C-shell-1 closed directly, review inherited; no reviewer/runtime/type rerun.
Feature publication and exact successor package batch released. No integration,
release or deployment authorization. Native fixture window remains held pending
actual new immutable artifact and registered fixture handoff.

## Subsequent CI test-fixture correction

Final4f CI's only unit failures were the two new real-shell tests: mocked user
had no time_zone, so UTC enabled unrelated SidebarTips settings discovery and
the strict unexpected-XHR assertion failed. Other379files/2609tests passed;
script/BFF failure count0. Exact UTC two-case reproduction failed before the
patch; adding only mocked user time_zone:'Europe/Prague' passed both cases in
UTC, Prague and Amsterdam. Real shell/providers/storage cases and strict XHR
assertion retained; no responder, runtime, docs, dependencies or protocol edit.

Consolidated successor d5aea5ffe1c6171ff4f4e887531d3bcd99538444,
tree31c1bd278a6ad4ba25f7fbcb2954d86efc12e6c4. Lead inspected exact4f..d5 diff:
one test-fixture field only,+1/-1, clean one-commit history, unchanged base/locks,
no migrations. Exact-file lint/format/whitespace/identity quick gates pass.
Evidence c-test-fixture-successor-source.json and c-test-fixture-4f-to-successor.diff,
SHA256853233cc7bffe3f662116b0e52e88e411943073b45c71231e9670ccc8b187c53.
Accepted directly as narrow fixture correction, without reopening unchanged
runtime review or repeating broad passing tests. Publication and honest final
artifact metadata are separate gates; neither was presumed from4f results.
