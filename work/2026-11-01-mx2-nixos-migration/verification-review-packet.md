# Automated verification final committed-deliverable review packet

Ready: intended source complete/committed, quick checks passed; no long test/build.

## User scope and acceptance

Original import/rebase and suggestion delivered at reviewed head e4c1ac0c.
User then asks to minimize their input and let agent perform verification. Current
scope: executable isolated verification and necessary candidate fixes, with user
separately authorizing internal mail-zone source correction against public DNS as
correct authority. No production deployment/cutover, primary changes, real message
submission or default integration. Keep original source and reviewed-import refs.

Architect-owned current design.md specifies conventional runNixOSTest with three
restricted KVM guests (sender, candidate, primary/localDNS), production-shared mail
module and explicit fixture timeouts/network only. No new input/framework.
Candidate corrections: exact intended relay domains/no implicit subdomains,
TCP25 firewall allowance, modern Postfix settings, primary-observed100MiB limit.
Preserve primary transport and queue paths, untrusted relay policy, DNSBL and
missing-milter fail-open settings. Tests must prove actual message content and
envelope, allowed/denied relay from untrustedv4/v6, greylist/error behavior,
accepted queue persistence across Postfix and guest restart plus recovery/drain,
4xxdeferral/5xxDSN, selfsigned-primary opportunisticTLS/plaintextfallback.
Production inbound certificate and real recipient synchronization are outside
this bounded implementation; disclose those limits without inventing mechanisms.

DNS source package only changes related mailrecords/SOA in internalcz zone, not
public DNS or unrelated splitDNS data. No internalorg zone needed. Validate syntax,
public-record equality, consumer impact and preserve independent DNS commit.

## Provenance and operational evidence

Original base0bcc165f13059782bf686da39a3a9b5698b10275 to
40411d67ee97cea800bcccd89b0473432b4502c4 preserved. Prior reviewed import
c040c14cdbacc07998700b524996a89306188d7f to
e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c; prior review.md remains historical.
No database/schema migrations, no known deployed feature. Historical source
consumption remains unknown; do not assert undeployed. No lock/input update
expected. Consolidate obsolete unmerged host-followups, preserve reviewed ref.
Append exact final range/series/diff dispositions before final assignment.

primary-baseline.md distinguishes operator fact Debian13/external management from
observations: splitDNS; public3domainMX10prasiatko-mail/MX15mx2; primaryPostfix
EHLO104857600+STARTTLS, selfsigned certificate (verified client refused), no
MAIL/RCPT/DATA/AUTH. Strict SSH trust/access unavailable. No production state
inspection; real recipient/trust/filter/queue policies unknown. Public DNS source
was user-designated correct; internalzone source repair is explicitly authorized.

## Owners and review policy

Architect0 design; implementer1 baseline/internalDNS package first;
implementer0 dependent sharedmodule/test/docs and history consolidation next;
lead acceptance/tracking; retainedreviewer0 final independent review. Serialize
all repo writes/Git across owners. Review remains independent/read-only.

High risk (relay authorization, durablequeue, firewall/DNS/host behavior).
General, architecture/repetition, scope/proportionality, risk/compatibility lanes.
Use mandatory-change-review skill/all four references and saved reviewer settings
(gpt-6.1-sol/xhigh), reverify same-session ready identity. No nested reviewers.
Review full final series/diff, exact module reuse/fixture fidelity and isolation,
wholehistory/migration/repeatedstream disposition, tests and source documentation.
Prior import review cannot stand in for this new substantive final review.

## Pending final evidence

Final base/head/series/diffstat; actual override inventory; quick Nix/Python/parser/
normalhook checks; test and production/affectedDNS-system derivations; exact
commands; docs entrypoint; source/input graph identities; final scope reconciliation.
Long integration/build starts only after final review/finding reconciliation,
under fresh policywatcher. No build/test yet in new verification phase.

## Exact final range and full series

Freshly fetched unchanged base `c040c14cdbacc07998700b524996a89306188d7f`;
final head `f3789413a53bcd12e2352940a0ec3e88009c5d9f`,
tree `0cfad62780eee89d51e17d0b9deba2d1a5738d9a`.
Complete series in order:

1. `36ae652962d0217dd5b22965cd44fd711790d77a` cluster: configure mx2 backup mail relay.
2. `91595bef8847063d76246b292293a687362af420` internal-dns: align mail records with public DNS.
3. `f3789413a53bcd12e2352940a0ec3e88009c5d9f` tests: verify mx2 relay and queue behavior in isolated VMs.

Full diff:13paths,715additions/4deletions. Includes originalimport plus50line shared
policy,195line conventional Nixfixture,287line driver,32lineSMTPhelper,72line opsdoc,
smallflake/READMEglue and13line DNSzone edit. Inspect entire diff directly.
No optional framework/dependency/CI addition. Old host correction folded into
owning hostcommit; no obsolete broken initial host iteration in final series.
Preconsolidation head `13e0ad185a7254ca3814167d28832d6276b107e0` has identical final
tree (lead independently checked). DNS old655851e5/new91595bef patch-ID equal
`87bf97c34572a6e79d3635773555be5e77ca9fd1`. Original40411 and reviewede4c1ac0c refs
retained. No database/schema migrations or repeated dependency/update streams.
No input/lock change; no feature deployment claimed. Three commits separate
hostbehavior, independently requested DNSsource correction and tests/docs.

## Completed quick checks and documentation

Implementer reports Nixfmt/parse, Pythoncompile, pyflakes-F with generated machine
hints, normal source/test commit/amend hooks passed. Lead independently confirmed
fullrange whitespace/cleanworktree and consolidation tree equality. Test/production
derivations evaluated on identical precommit source; final-commit exact identities
being recorded, metadata only. No further source edits intended.

Generated main.cf comparison realconfctl vs test differs only hostname and seven
short retry/policy overrides; transportexact, enabledfirewallTCP25 equal,
Postgreyunit only300s->2s. Raw mail-fidelity-generated.json and
fixture-mail-evaluated.json available; durable Markdown inventory coming.
Negative unrelated/subdomain test names resolve locally to isolate relaydenial
from unknown-domain denial. Unknown-domain separate. Assess actual code fidelity
and isolation independently.

DNS BINDnamed-checkzone/compilezone passes for allfour actual templateconsumers;
canonical RRsets prove only six intended mailRRsets plusSOA changed, all unrelated
records preserved (482->485total). See internal-dns-reconciliation.md for public
query authority/userwording/time/TTLs, exactpaths, targetbuilds and parser evidence.

Opsdoc docs/operations/mx2.md linked fromREADME covers reusable testcommand,
modulebehavior, explicit fixture differences and live/container/recipient/TLS/
queue recovery limits; no runreceipts in project. Lead applied required writing
skill directly; plain facts/commands preserved, no prosechanges needed.
Primary-baseline.md is operational observation, not public policy/config proof.

## Review assignment

Retainedreviewer0 ready and independent, same-session thread
01a19caf-15c8-74a2-baf1-6594cf30d117, saved gpt-6.1-sol/xhigh/read_only verified.
No override/fallback. Read skill/all four lanes and relevant local guidance.
Report fullreview text to lead (read-only reviewer must not write files). Lead
will record verification-review.md. Explicit conclusions on fullhistory/migrations/
repeatedstreams, tests' production fidelity/network isolation, actual supported
scope and accepted operational limits. No builds, production access or mutations.
