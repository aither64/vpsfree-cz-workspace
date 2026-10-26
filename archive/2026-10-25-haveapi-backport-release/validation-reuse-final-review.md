# Final affected review: validation reuse and count ceiling

Reviewer0: PASS, no Blocking, Important or Advisory findings. Retained
gpt-6.1-sol/xhigh/read-only, independent, no nested reviewer or source/Git edits,
tests or campaigns. Session binding reverified. All four mandatory affected
lanes covered at High risk. Prior be520 and40b514 formal reports remain intact
for unchanged runtime/consumer/JSON/footer/watchdog conclusions.

Exact complete range: integrated1741a25e1df45f06f9966942d5c34a97967ebb3e to
bdb034436e0dffbc39537a481442c3a2880cea9c, HaveAPI haveapi-master worktree,
branch2026-10-25-haveapi-backport-release-master. Reviewer independently found
one coherent commit,18files+1246/-205, clean final HEAD/index/worktree.
Full-index diff SHA2564717088e0cc5df6f7ed7d91985c1e05dff8cebed70fcbccb7264aca8a0ac461e.
Affected40-to-bdb diff exactly8authorized paths,
SHA256f3fd73aff298b17827df7d90c9ce33d2bb48e3b3c38b91b7125b28f15fb61d71.
All787complementary tracked entries and current retained input/lock/budget
hashes match; independent diff check clean.

Correctness/risk ACCEPT: Worker#measure owns immutable proofs per measurement
or warmup. Every response is hashed and exact-byte compared; collisions reject.
Scenario.validate! runs for every response, keeping HTTP/content type, called
index and operation-counter checks outside reusable body semantics. Identity
metadata is verified before reuse. New bodies receive complete semantic and
canonical proof, including duplicate-key/raw agreement. No proof escapes across
samples, users, scenarios, sources or workers; snapshots prevent mutation.
Comparator validates raw/canonical body proof once, then every reference's
existence, digest, status, envelope, byte count and comparison context, including
source VERSION. Mode/version changes reject; counters, cardinality/order,
same_outputs and source/input/lineage checks remain. Shared100000 ceiling applies
to selection/worker/replay; common baseline counts, one adjustment, adequacy,
budgets, warmups and watchdogs are unchanged. Oversized counts reject and capped
inadequate timing stays inconclusive.

Architecture ACCEPT: existing fixture boundary separates operation checks from
body semantics; shared immutable snapshots support worker/replay. No global
cache, persisted proof, alternate report schema or registry. Scope ACCEPT:
measured validation cost and inadequate cheap cases justify the8-path correction;
no timeout/dependency/calibration/product expansion. General ACCEPT: docs and
tests cover later body/status/header/collision/counter/canonical/duplicate-key,
index/user/sample/mutation/reference/count negatives and existing protections.

Evidence independently bound: four production-neutral code hashes equal final
Git blobs. tested_base40 is disclosed as precommit base, not candidate identity.
Old/new16subset rows,100852references, source/output/body/counter/metric hashes
and8worker hashes match; old175.328s/new1.144s validation and worker0.630/0.250s
are diagnostic savings, not campaign passes. Original diagnostic composition
failure is retained; corrected path uses validate_sample plus same_outputs.
Live cheap files match hashes/bytes/cardinalities; common16979/27027counts and
warmups,1body/case; baseline wall/CPU1.5599/1.5594s and2.4699/2.4696s adequate,
candidate1.6780/1.6776s and2.5335/2.5332s retained. Results~4.67/7.43MB;
peakRSS199164/192516KiB; exact source blobs and87-gem environment verified.
123/0suite receipt honestly discloses absent complete stdout; final9/0 has a
log, lint/hooks/message checks pass. No unreported full-suite rerun.

Session-only stage preload observes supported CLI read/parse/compare/report
serialization/write/RSS/exit, preserving original identities/schema. Smoke
passes; outer whole-command timing is separately required because preload timing
starts after helper initialization.

Whole-branch/history/streams ACCEPT: one coherent final commit, obsolete coarse
policy/fixups/timeout/footer/JSON/validation iterations folded. JSON2.21.2 dev
preparation remains one consolidated stream, no new dependency/generated stream
or changed external graph. NO MIGRATIONS, seeds, persisted-state conversion or
production API/protocol changes; migration merge/release/deploy/external-use
inventory empty, prior compatibility/rollback conclusions unchanged.

This is source-review acceptance for exactbdb only. Original40221259354 remains
cancelled/failed/unclassified, with no report/runner exit. Subset/live evidence
does not prove full replay or hosted margin. Next: full supported immutable
retained replay in NEW directory with original IDs and stage/whole-command
receipts, then final-head quick and one weekly proving complete34-case adequacy,
report/exit and margin. No integration/publication/operational success claimed.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/)
