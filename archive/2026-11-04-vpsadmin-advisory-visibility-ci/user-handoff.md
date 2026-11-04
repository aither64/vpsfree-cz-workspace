# Deliberate user handoff (task constraints and exact evidence)

User: "start a new workspace session with a full team to investigate this failure,
find the root cause and suggest a solution."

Own session/worktrees; installed default delegated Full team with two implementers,
retain settings and verify own runtime/roster. Architect owns substantive
investigation/design; bounded independent implementer packages after scoping.
Lead is user contact. No originating-session roster/checkouts/files/transcripts.

Goal: explain anonymous advisory CVE visibility failure in automatic default-branch
API workflow with reproducible root cause or exact remaining uncertainty and
smallest correct solution. Actively investigate dependency drift, randomized
order/shared state, resource input validation and other plausible causes. Do not
assume Rails caused it merely because version changed. Diagnosis/proposal only,
not production fix. Isolated instrumentation/prototypes/disposable reproduction
allowed. Keep proposal reviewable and distinguish implemented/merged fix. No
master merge, package publication, production access/data, deployment or originating
session lifecycle/cleanup. Do not weaken authorization, retries/skips/pending,
graph freezes, broad guards or assertions without demonstrated intended behavior.

Use public vpsfreecz/vpsadmin Git primarily. Public HaveAPI only actual validation
boundary; no vpsAdmin policy in generic HaveAPI docs. Read procedures. Existing
4ac49f49e63545200df8afa920c6eafda8722523 docs-only integration is complete;
separate follow-up. Fetch public defaults, preserve supported source/migration
lineage, record exact reproduction revisions. Commit substantive initial records
before project commits/external mutation; architect design before substantive
implementation. Evidence/findings alone no automatic final review; completed
substantive patches require commit/quick checks/review before long checks. Fresh
pinned Luna/low watchers for uncertain/long checks. Stop unexpected kernel builds.
Prefer exact topic reproduction/small experiments over repeated full matrices.

## Exact failure evidence deliberately supplied by user

Repository git@github.com:vpsfreecz/vpsadmin.git
Source head 4ac49f49e63545200df8afa920c6eafda8722523
Failed master push run https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583
Topic job https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583/job/126548402180
Coverage job https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583/job/126562400379

full/platform-operations: 239 examples, 1 failure, seed 13353.
api/spec/api/resources/security_advisory_spec.rb:487, ID [1:3:2],
"VpsAdmin::API::Resources::SecurityAdvisory Read visibility scopes CVE, node and
update reads and included parents without changing retained history".
Assertion failed line 522. Actual job diagnostic:
role anonymous; path /v7.0/security_advisory_cves; advisory state draft;
HTTP status 200; response status false; error class Hash;
error_fields [security_advisory]; requested meta {count:true,includes:security_advisory};
returned_meta nil. Expected successful response with no visible rows.
No timeout or API_SPEC_REQUEST_EXCEPTION runner marker. full/core aggregate all
13 manifests per mode, all 417 eligible paths covered; correctly failed because
full matrix failed, not manifest absence. Other 25 topic jobs succeeded.

Example last changed 8225229aa0e3306f8b1723c5583969a33c64571c; present in predecessor
942c6eaed41331f823d8e0f670ed239e2b308440. 4ac49f49 changes only AGENTS.md and
docs/api-schema-export.md, no runtime/test/workflow/dependency change.

Same source earlier green feature run:
https://github.com/vpsfreecz/vpsadmin/actions/runs/41679570284
Example passed seed 56402. Effective dependency graphs differ:
Failed lock SHA256 aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21
Rails activemodel/activerecord/activesupport 8.1.4.1, mime-types-data 3.2026.1103.
Passing lock SHA256 cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47
Rails activemodel/activerecord/activesupport 8.1.4, mime-types-data 3.2026.1027.
Matching: Ruby 3.4.12, Bundler 2.6.9, RSpec 3.13.6, HaveAPI 0.32.2,
MariaDB 11.8.6, REPEATABLE-READ, innodb_snapshot_isolation=OFF.
Older green is NOT equivalent inputs; graph and order both changed. No causal or
timing-only-flake conclusion. Initial inspection: resource cleaner converts and
looks up referenced record and checks authorization. Saved response lacks exact
validation message, so specific rejection unproven.

Independently retrieve public result/environment artifacts:
failed rspec-results-full-platform-operations artifact 13318816860;
passing counterpart artifact 13254476736. Retain complete native result/environment
JSON, relevant logs, effective locks, seeds, exact input graph and hashes in this
session. Re-fetch; do not read originating private records/transcripts. This is
complete deliberate text handoff; no cross-session communication grant implied.

## Acceptance

1. Exact rejection/expectation and intended anonymous/public behavior; distinguish
   validation, authorization, query filtering and test fixture state.
2. Fixed source/input reproduction, failure diagnostics, independent dependency/order
   variation as warranted. Narrow experiments/counterexamples; green rerun not proof.
3. Causal evidence; if not reproduced, precisely known/unknown and next bounded
   experiment. Never invent root cause.
4. Smallest solution, owning component, compatibility/security and focused regression
   plan; required fix versus optional hardening. Proposed patch scoped/reviewable,
   no merge/deploy without later explicit authorization.
5. Concise findings/records and report in this NEW session; leave sessions open.
Prior release and six-repository documentation integration complete: do not reopen.
