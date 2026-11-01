# Final independent development-consumer review

Reviewer0 completed final review on2026-10-28: **one Important finding,
DEV-R1; no other findings in the reviewed scope**. The finding is open pending
owner remediation. This is not deployment, integration or release approval.
Lead records the report here; original reviewer message remains in the session.

## Reviewer and exact scope

Retained independent reviewer0, review-purpose, gpt-6.1-sol/xhigh/read_only;
thread01a16f67-b886-7573-a065-dcf2f4b7c262, native review turn
01a18436-1956-7f33-be0b-fcdb71ec906d. Reviewer verified session binding, absent
ambient markers, live saved roster and actual native model/effort/CWD. No
setting override, fallback or nested reviewer. Read-only instructions honored.

HIGH risk: OAuth/private config, proxy origin/logging, cross-project packaging
and deployment/rollback. All four lanes completed directly: general/history,
architecture/repetition, scope/proportionality, risk/compatibility.

Repository alias vpsadmin-haveapi-dev, branch
2026-10-24-vpsadmin-haveapi-upgrade-devdocs; complete range
08c3bd7e3cb4dc324a0381df6a1eec190daab1a7..
c413b07cf8120eb6159b4249b150a6aff99ecaed, tree
61ea05a80724ac0f714b06e011ea15515f56041e. Four actual commits:

1. 32608935ebf3f446656f8531cd3dc4f9c8bcfe26
2. 8102179cf7f7e9bb534965c8acb3e02ef723045f
3. 3a92d6458cf76c9338afd6106c48b069575e196d
4. c413b07cf8120eb6159b4249b150a6aff99ecaed

Complete39-path final diff and8102..head diff independently match the packet;
source was clean. Earlier0312 review reused only for unchanged carried content,
with the full history independently assessed anew. [Packet](review-packet.md).

## DEV-R1 — Important — risk/compatibility

At c413b07, tests/configs/nixos/vpsadmin-services.nix:262–284 protects nginx logs
and:614 disables API HAProxy request logging, but:664–668 retains API frontend
transport through /run/varnish/vpsadmin-varnish.sock. Varnish return(pass) in
nixos/modules/vpsadmin/varnish.nix:86–94 avoids caching, not VSL logging. No
request/response tag masking is configured at:166–171. Default VSL can retain
ReqURL/BereqURL and headers including callback code/state and docs cookies.
This contradicts the configured proxy logging boundary described in
 docs/api-client-examples.md:111–115 and the accepted HTTPS contract.
Source/config evidence only: reviewer made no live request or log query.
Preliminary report426d2353-230f-4326-bc83-0bb41803bbe3 identified the same issue.

Requested fix: smallest existing supported routing/logging configuration,
verified with nonsensitive markers; no provider/tool redesign or wider campaign.
Lead accepted architect's [two-file direct-routing brief](../../design.md:3203):
API nginx directly to the existing HAProxy socket, same as auth.test, plus
owning docs explanation. Keep shared modules/PHP/React unchanged. Dev/test
metrics deliberately lose the Varnish60s cache. Never restore the Varnish hop
while docs OAuth remains enabled. Actual generated-config proof precedes later
bounded runtime logging proof for both request and response sensitive values.

A0 released via assignment01ab12cd-3782-4d7e-a1ea-584dc7bb8414, turn
01a18442-6bf8-7f72-bae0-3d558a992428. Source fix/quick evidence pending. Lead
will inspect the direct remediation under mandatory review's narrow-fix rule;
no full rerun is required for this accepted boundary. Broader module/routing
changes require affected-lane review. Build/services/activation remain held.

## Explicit history, streams and migration conclusions

Reviewer accepts all four commits as coherent released0312 dependency/profile
adoption followed by development API packaging and its OAuth/docs integration.
Retained0312 has concrete supported CLI/download-mounter/PHP/browser consumers;
8102 is a coherent source/config rollback boundary. This release/consumer
boundary, not development deployment alone, justifies the separate streams.
Unpublished4a792 is consolidated, not an ancestor. No35c/transitional pin,
obsolete unmerged approach, follow-up fixup, abandoned adapter or redundant
new development stream remains. Commit split is reviewable.8102 is an ancestor;
older nonancestor refs remain provenance and are not described as merged.

**NO MIGRATIONS.** No DB migration/schema/seed or persisted-data format change;
no transitional/reworked migration or merge/release/deployment/external-use
migration lineage. Private OAuth config/key/client are operational inputs to
preserve and restore, not migrations. Rollback requires matching protected
predecessor config; no client deletion/provider/session lifecycle is implicit.

## Accepted source and evidence boundaries

The five-Git-only recursive discovery shim is bounded at existing gemConfig
hooks. Actual selected Nix installer lacks the recursive glob; no copied
installer, source slicing, wrapper gemspec, runtime preload or packaging
framework. Caller options, explicit globs and unrelated Git/Path behavior are
preserved; RUBYOPT unset/empty/value restores before inherited postInstall.
Server make-doc precedes standard staging/gemspec installation.

Optional private config uses configure-before-mount, disabled when absent and
redacted startup errors when invalid; outside source/Nix. Standard cookie-only
HTML/search and nil cleanup hooks are correctly used without an adapter; ordinary
API/JSON/OPTIONS/provider handling stays separate. No arbitrary-exception
ensure guarantee. VPS example name-to-login matches its schema/label; regression
uses the actual mounted example. Docs cover routes/config/package/rollback and
SDK pairing; exporter remains deliberately fail-closed for development0310.

All five gems bind d67bebcb37f2d4558a97caa208465147da19dbef/tree
cd91bf06fd14d297aaa2470844f679f0998d85f9, intentional0.31.0 metadata and one hash
0a2y4467shd7w0bl645yc9ga20k792x5pdpjb4siac49d752mfqv. Reviewer independently
compared all122 entries: other117 byte-identical. Full ignored/packaged lock
matches4ded33e27ae206ce6f7ea9352a591f4a373634c767c0d58bc1865717bfa1c0a6.
Protected consumers/inputs match8102. Installed source head/digests matchd67;
real retained archive hash and12 file digests match package-proof.

Native core8 distinct passes (retained5 plus corrected3), full8/8, private
sample8, actual selected installer fixture metadata/library/scope/RUBYOPT and
ordinary hooks/lint evidence inspected. Zero-example wrapper excluded. Original
failures remain distinct. No broad client/browser/performance result relabelled.

Remaining gates: actual five Nix outputs and docs/assets/source/config/input
closure proof, then services-up. The lock records Bundler4.0.23 while actual
Nix installer smoke uses2.7.2; final execution must prove the package rather
than infer equivalence. Fixture/archive passes do not replace this. Later
strict-CA OAuth round trip, cookie/API/locale/cleanup, origin and logging proof
precede dev usability. M7 and producer gates stay separate.

Reviewer performed no tests/builds/fetch/push/live queries or source/index/state,
cluster/provider/KB/lifecycle mutations. No owned review operation remains.

## Lead narrow-fix acceptance — cba6265

DEV-R1 is resolved in source at
cba626581a698256e873319983ac51312f40398c/tree
40375b83d5077e0fe16c0c47b8307ff467a82b4f. Lead independently inspected actual
Git head/tree/clean status, full four-commit inventory, exact two-path11+/4-
diff, range comparison, final-proof/result and generated before/after nginx
upstreams/locations/log/header config and complete HAProxy output. The exact
accepted API direct route replaces the Varnish hop; safe logging/headers remain,
HAProxy no-log/backend/config is unchanged, PHP/auth/console routes are equal.
Native React overrides and actual runtime log absence remain deployment gates.
Owning English prose was inspected directly with the workspace writing skill;
no wording correction was needed. No other tracked entries changed.

Normal amend/hooks and focused actual imported services/frontend/HAProxy/QEMU
configuration evaluation passed; original missing-QEMU evaluator failure is
retained as setup failure before assertions or Git mutation. Full ignored and
packaged lock remains4ded33e2, no writer/owned process remains. Package3a92 and
published8102 unchanged; frozen c413 survives on its reviewed ref. The complete
final series is32608935,8102179,3a92d645,cba6265, with NO MIGRATIONS and unchanged
accepted history-stream boundaries. [Addendum](dev-r1/addendum.md).

Accepted under mandatory-review steps9–10: direct requested correction inside
reviewed boundary, no new interface/design; no reviewer rerun or unaffected
quick-suite repeats. This resolves the Important source finding, not actual
HTTPS/logging validation. A0 is released for real API package/all-five output
and documentation proof, existing services-up and ordinary feature publication
at this exact head, assignmentbb0f335d-7625-4245-a48c-b8d6a21ec108,
turn01a1844b-0ed6-7631-9d1d-9546356354bb. No deployment/default integration yet.
