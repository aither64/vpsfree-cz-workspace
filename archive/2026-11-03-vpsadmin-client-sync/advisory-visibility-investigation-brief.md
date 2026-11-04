# Investigate vpsAdmin advisory visibility CI failure

User instruction: "start a new workspace session with a full team to investigate
this failure, find the root cause and suggest a solution."

Start this investigation in its own session/worktrees. Use the requested Full
team with two implementers (`delegated`), the installed default Full-team preset,
retaining its lead/architect/implementer/reviewer/observer settings. Verify your
new session's own runtime binding and roster before work. Architect owns the
substantive investigation/design brief; assign bounded independent execution
packages to the implementers after scoping. The coordinating lead remains user
contact. Do not borrow the originating session's roster or checkouts.

## Goal and scope

Determine why the existing anonymous security-advisory CVE visibility test failed
in the automatic default-branch API workflow, establish a reproducible root cause
or the exact remaining uncertainty, and suggest the smallest correct solution.
Investigate actively; do not stop at speculation or a blind CI rerun. Use
controlled reproduction and evidence to separate dependency drift, randomized
order/shared state, resource input validation and other plausible causes.
Do not assume Rails caused it merely because its version changed.

The requested deliverable is diagnosis and a proposed solution, not an approved
production fix. Isolated diagnostic instrumentation/prototypes and disposable
reproduction are allowed as needed; keep any proposed patch reviewable and
explicitly distinguish it from an implemented/merged fix. No default-branch merge,
package publication, production data/access, deployment or lifecycle/cleanup of
the originating session is authorized by this request. Do not weaken authorization
or hide the failure with retries, pending/skipped examples, graph freezes, broad
compatibility guards or changed assertions without demonstrated intended behavior.

Use vpsfreecz/vpsadmin public Git as the primary source; inspect HaveAPI public
source only where needed to trace the actual validation boundary. Read current
repository/workspace procedures. Keep HaveAPI generic: vpsAdmin-specific policy
must not be added to its documentation. The completed documentation-only commit
4ac49f49e63545200df8afa920c6eafda8722523 is already integrated; this is a separate
follow-up investigation. Fetch current public defaults, preserve supported source
and migration lineage, and record the exact revisions used for reproduction.

Create substantive plan/state and commit initial coordination records before
project commits/external mutation under the ordinary procedure. Architect writes
work/<your-new-slug>/design.md before substantive implementation. Findings and
investigation evidence alone do not require automatic final change review; any
completed substantive code/config/docs patch does, after commit/quick checks and
before long integration checks. Use fresh pinned Luna/low utilities for long or
uncertain tests/CI; stop unexpected kernel builds. Prefer exact existing topic
reproduction and small controlled experiments, not repeated full matrices.

## Exact failure evidence (deliberately handed over)

Repository: git@github.com:vpsfreecz/vpsadmin.git
Source head: 4ac49f49e63545200df8afa920c6eafda8722523
Failed automatic master push run:
https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583
Failed topic job126548402180:
https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583/job/126548402180
Consequent topic-coverage job126562400379:
https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583/job/126562400379

The full/platform-operations topic ran239examples with1failure, seed13353.
Example: api/spec/api/resources/security_advisory_spec.rb:487, ID[1:3:2],
"VpsAdmin::API::Resources::SecurityAdvisory Read visibility scopes CVE, node and
update reads and included parents without changing retained history".
Assertion failed at line522. Diagnostic in actual job log:
role anonymous; path /v7.0/security_advisory_cves; advisory state draft;
HTTP status200; response statusfalse; error class Hash;
error_fields [security_advisory]; requested meta {count:true,includes:security_advisory};
returned_meta nil. Expected a successful response containing no visible rows.
No timeout or API_SPEC_REQUEST_EXCEPTION runner marker was observed for this
failure. The full/core coverage aggregate had all13manifests per mode and all417
eligible paths covered; it correctly failed because the full matrix failed,
not because a manifest was missing. All other25topic jobs succeeded.

The test/behavior source predates this documentation task: example last changed
at8225229aa0e3306f8b1723c5583969a33c64571c and is present in the predecessor
942c6eaed41331f823d8e0f670ed239e2b308440. Commit4ac49f49 changes only AGENTS.md
and docs/api-schema-export.md; no runtime, test, workflow or dependency change.

Same exact source-head earlier feature run was green:
https://github.com/vpsfreecz/vpsadmin/actions/runs/41679570284
The identical example passed with seed56402. However, effective dependencies differ:

- Failed lock SHA256:
  aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21
  Rails activemodel/activerecord/activesupport8.1.4.1,
  mime-types-data3.2026.1103.
- Passing feature lock SHA256:
  cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47
  Rails activemodel/activerecord/activesupport8.1.4,
  mime-types-data3.2026.1027.
- Matching observed environment: Ruby3.4.12, Bundler2.6.9, RSpec3.13.6,
  HaveAPI0.32.2, MariaDB11.8.6, REPEATABLE-READ,
  innodb_snapshot_isolation=OFF.

Therefore the older green run is NOT equivalent-input evidence; both dependency
graph and order changed. No causal conclusion or timing-only-flake label was
established. Initial source inspection found the resource-input cleaner converts
and looks up the referenced record and checks authorization. Saved response lacks
the exact validation message, so the specific rejection mechanism remains unproven.

Result/environment artifacts to retrieve independently from these public runs:
failed rspec-results-full-platform-operations artifact13318816860;
passing counterpart artifact13254476736. Retain complete native result/environment
JSON, relevant job logs, effective locks, seeds, exact input graph and their hashes
in YOUR OWN session. Re-fetch public evidence instead of reading the originating
session's private records or transcripts. You have this complete deliberate text
handoff; no cross-session communication grant or peer-file access is implied.

## Acceptance and final report

1. Identify the exact rejection/failed expectation and intended public/anonymous
   visibility behavior. Trace the implementation and distinguish validation,
   authorization, query filtering and test fixture state.
2. Reproduce with fixed source/input identities, preserve failure diagnostics,
   and vary dependencies and order independently where warranted. Narrow the
   experiment and retain counterexamples; do not equate a green rerun with proof.
3. Explain the causal mechanism with evidence. If the original failure cannot
   yet be reproduced, state precisely what is known, unknown and the next bounded
   experiment instead of inventing a root cause.
4. Suggest the smallest solution, its owning component, compatibility/security
   implications and focused regression/verification plan. Separate required fix
   from optional hardening. If proposing a patch, keep it scoped/reviewable and
   do not merge or deploy without later explicit authorization.
5. Maintain concise findings/records and report the root cause, solution and
   remaining risks to the user in the NEW session. Leave sessions open.

This new task starts from the residual evidence above; the preceding release and
six-repository documentation integration are complete and must not be reopened
or rewritten merely to start this diagnosis.
