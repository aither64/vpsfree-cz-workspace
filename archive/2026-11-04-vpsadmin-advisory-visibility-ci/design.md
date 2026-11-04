# Advisory CVE visibility investigation design

Architect: architect0, retained Astra/xhigh. Status: investigation brief;
diagnosis and proposal only. See [user handoff](user-handoff.md) and [plan](plan.md).
Identity verified with `dev-session current` and both matching environment markers.
This design does not authorize a fix, integration, publication, deployment or
session lifecycle action.

## Scope and intended behavior

Investigate public vpsAdmin source `4ac49f49e63545200df8afa920c6eafda8722523`
in this session's registered vpsadmin worktree. Current fetched default
`b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e` is a separate reference, not the
reproduction source. Only public HaveAPI source may supplement the framework
validation trace. Do not access originating-session records or checkouts.

The exact failed example is `security_advisory_spec.rb[1:3:2]`, source line 487,
full/platform-operations, seed 13353, run 41822368583. Its first anonymous draft
CVE index request returns HTTP 200 with envelope status false, error field
`security_advisory`, and no count metadata. The assertion expects a successful
empty list. This establishes a validation-shaped rejection, not yet the rejecting
method, reason or dependence on previous examples.

Public feature documentation says that only published advisories and related
records are visible to anonymous and non-admin readers. The example further
expects list filters referencing hidden draft/retracted parents to succeed with
zero rows/count; corresponding child show requests return 404. Verify the exact
framework contract before recommending how that list expectation is implemented.

Visibility invariants:

- Anonymous, ordinary and support users must not read draft/retracted parent
  content, CVEs, updates or node rows through direct, filtered or included output.
- Admin readers retain all states. Count, cursor and include paths obey the same
  visibility predicate as rows; includes cannot reintroduce a hidden parent.
- Affects-user/VPS projections retain ownership and authentication requirements.
- Read operations preserve original fields, retained history and projections.
- Generic HaveAPI must not acquire vpsAdmin advisory policy. Do not loosen
  resource validation globally, skip assertions, add retries, or freeze the
  dependency graph as an unexplained fix.

## Interfaces, files and causal hypotheses

Trace request parsing and resource parameter cleaning/lookup/authorization before
the action query, then compare with query filtering and include serialization.
Relevant vpsAdmin files are `api/lib/vpsadmin/api/resources/security_advisory*.rb`,
`api/models/security_advisory*.rb`, the exact spec, request/auth helpers and cached
app setup in `api/spec/`, and `.github/workflows/api-specs.yml`. Exact HaveAPI
0.32.2 resource parameter and model-adapter files must be identified from source,
not inferred from the handoff. Relevant docs are `docs/security-advisories.md`,
`docs/agent-instructions/{development,testing}.md` and `docs/api-schema-export.md`.

Keep these alternatives open until evidence discriminates them:

1. A resource parameter resolves a hidden advisory through a Show/read permission
   path and rejects it before the intentionally visibility-filtered list query.
2. RSpec order leaves shared resource/action/authorization state or app caches that
   change validation; login cleanup and fixture identities are competing causes.
3. Changed dependencies alter conversion, lookup, relation or cache behavior.
   Rails versions alone establish correlation. mime-types-data and any other
   effective graph differences remain inputs until ruled out.
4. Fixture/model state differs from the test's assumptions, or another request
   path produces the apparent field error. Capture the exact error and branch.

### Preliminary counterevidence from Package B

The lead relayed B's HaveAPI 0.32.2 source trace: `Resource#authorize_record!`
calls the referenced `SecurityAdvisory::Show#authorized?`, not `Show#prepare`.
The vpsAdmin Show authorization block permits public readers while blacklisting
administrative output fields; the published-state restriction is in `prepare`.
Therefore a hidden draft/retracted parent does not by itself explain this input
rejection. Hypothesis 1's presumed invocation of visibility-filtered Show lookup
is unsupported and must not motivate an integer-filter or authorization change.

B still needs to identify the actual rejecting branch and exact validation error,
including adapter lookup/type conversion and any shared authorization-state
mutation. This is a reported source-level counterexample, not yet a runtime
reproduction or an explanation of why the two CI runs differ. The original
visibility invariants and proposed regression surface remain unchanged.

Architect source inspection confirms that the ActiveRecord input adapter also
rescues `ArgumentError`/`TypeError` across its complete lookup/callback block and
maps them to invalid ID. An invalid-ID message alone therefore would not prove
malformed request input: retain the underlying cause or raise location if raw
input is otherwise valid. Do not alter an active diagnostic run for this caveat.

## Input and evidence inventory

Package A recovers complete native results and environment JSON, file manifest,
job logs and available effective generated API locks for runs 41822368583 and
41679570284 (artifacts 13318816860 and 13254476736). Keep run and attempt identity,
source SHA, seed, example ID and all dependency versions/hashes separate. Record
retrieval failures and missing locks honestly; reconstructed locks are not native
artifacts and must be marked as reconstructions.

Reported failed/passing lock SHA256 are respectively
`aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21` and
`cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47`.
Reported differences: Rails 8.1.4.1 vs 8.1.4; mime-types-data 3.2026.1103 vs
3.2026.1027. Reported equal tools: Ruby 3.4.12, Bundler 2.6.9, RSpec 3.13.6,
HaveAPI 0.32.2, MariaDB 11.8.6, REPEATABLE-READ with snapshot isolation OFF.
These are supplied facts pending independent verification. The packaged lock
is not CI's generated API bundle. Preserve full graphs and command/environment
receipts, including plugin selection, Nix inputs and temporary DB settings.

Raw artifacts remain untracked under this session. Markdown findings retain
compact provenance, commands, outcomes and caveats. No unrelated records are read.

Package A has retrieved the native results/environment and full attempt-1 logs
for both runs. Architect inspection independently confirms that the lockfiles at
`evidence/ci/<run>/attempt-1/log-reconstructed-api.Gemfile.lock` hash exactly to
the corresponding native environment JSON's `gemfile_lock_sha256` above. They
remain correctly labeled log reconstructions, with byte identity established by
the recorded digest. Their complete diff contains only activemodel, activerecord,
activesupport 8.1.4 -> 8.1.4.1 and mime-types-data 3.2026.1027 -> 3.2026.1103.
Native environment JSON confirms equal full/platform-operations mode/topic,
Ruby 3.4.12 revision 366f5fdc00, Bundler 2.6.9 and RSpec 3.13.6. This supplies
controlled dependency graphs; it does not establish causal blame or certify that
a local run reproduces the original runner and DB environment.

Package A's completed [CI receipt](ci-evidence.md) verifies identical source tree,
eight-file manifest and all 239 scoped example IDs. Only the target's result
differs; it ran at position 237 in the failure and 205 in the passing run. Besides
seed/order and the four changed gems, the Ubuntu runner image, provisioner and
region differ. Native evidence lacks the actual validation message/branch, record
ID, complete process/machine state, gem binary checksums and database contents.
The passing run is a useful counterexample but does not isolate one changed input.
No artifact retrieval blocker remains. See [Package B trace](validation-reproduction.md)
for the source mechanism and controlled reproduction receipts.

### First local runtime result

Package B's isolated `[1:3:2]` at seed 13353 passes (one example, no failures)
with the exact failed lock hash retained after preparation, loaded Rails 8.1.4.1,
mime-types-data 3.2026.1103 and HaveAPI 0.32.2, Bundler 2.6.9, full plugins.
The trace shows anonymous draft raw String `"1"` resolving to draft advisory ID 1,
Show authorization returning true, then the CVE and Update list queries running.
This runtime counterexample supports the static visibility/authorization trace.
Neither hidden parent state nor this dependency graph alone is sufficient to
trigger the failure in the local isolated environment.

The local Ruby is 3.4.9 rather than native CI's 3.4.12, and local MariaDB is
11.4.12 rather than 11.8.6; OS context and prior
examples also differ. Do not infer that dependency drift is irrelevant or that
order dependence is proven. The next bounded discriminator is the exact native
eight-file topic at seed 13353 with the same graph, comparing complete executed
IDs/order to native evidence before selecting another experiment.

### Full-topic synthesis and conditional follow-up

The lead assigned conditional fallback design without authorizing another batch.
B's fresh `/root/watch_topic` utility completed the full topic; no operation remains.
Architect read-only acceptance checks found:

- RSpec 3.13.6 `Ordering::Random#order` sorts by a Jenkins hash of seed plus
  scoped example ID. Its ordering is distinct from the global `Kernel.srand`
  stream used by fixture/application code. Compare actual execution IDs/order;
  do not assume random data or runtime state is controlled merely because order
  agrees.
- HaveAPI `parameters/resource.rb`, `model_adapters/active_record.rb`, `action.rb`
  and `params.rb` are byte-identical between the installed Nix gem used for the
  initial trace and the bundle actually loaded by the local reproduction.
  This resolves a local trace-source mismatch concern; CI gem binary identity
  remains unavailable.

No additional package for A is useful now. Broad upstream Rails/Ruby source diffs
would not identify the absent native rejection and would overlap unresolved
experimental questions. A's existing complete graph/order/runner receipts are
sufficient for the next decision. No new tests or environment setup were launched.

Final first-batch result: 239 examples passed, zero failures/pending/errors outside
examples, seed 13353, duration 2932.288 seconds. Architect independently compared
native/local result JSON: all 239 unique IDs and their entire order agree. The
target is position 237 in both and is the only status difference, failed natively
and passed locally in 303.659 seconds. Its first anonymous draft request receives
String `"55"`, resolves draft ID 55, authorizes successfully and reaches the query.
The target has 168 diagnostic events, 24 successful Resource cleaner calls and
no cleaner error. Runtime receipt retains the exact failed lock and loaded graph.
Thus the source/graph/recorded sequence together are insufficient to cause the
failure in the local instrumented runtime; runtime interactions or transient
state remain open. This is not a diagnosis of the native rejecting branch.

B completed the bounded read-only exact-runtime availability/setup-cost
assessment. Official Ruby builder offers the Ubuntu 26.04 x64 Ruby 3.4.12 archive
(42,575,614 bytes, SHA256
`b4943e5d36b82f38c3f3c9f979a1d1b5dfb9769dcada5e70945e0fe63b6b8586`),
and official Ubuntu indexes contain MariaDB `1:11.8.6-5ubuntu0.1` server/client/
library/header/compatibility packages. Exact Nix outputs and a cached Ubuntu image
are absent; Podman is installed. No source cold build is inherently required, but
image pull, exact apt setup, Ruby revision verification and a separate 104-gem
bundle/native mysql2 build remain unmeasured work. The native runner's preinstalled
Ruby archive checksum is unavailable, preventing exact binary-identity proof.
See `evidence/reproduction/native-runtime-availability.json` for metadata receipts.

Lead decision: finish this first-batch investigation at the known/unknown boundary;
no automatic new environment or test batch. Nothing from the native-runtime
proposal has been installed or launched. The following is the concrete next
experiment if investigation resumes, not an active or automatically selected run.
The smallest justified change proposal is vpsAdmin-side test diagnostics retaining
the original Resource validation error/cause before aggregation. Product filtering,
authorization and generic HaveAPI policy remain unchanged; no project patch exists.

If the local topic fails, B first classifies whether the exact target/first
request/error recurred and captures the raw ID, resolved record, validation
branch and original cause. Minimize the observed mechanism only after that result.
If result JSON is incomplete, examples differ, or native order does not agree,
resolve that specific discrepancy before interpreting a pass as a counterexample.

If all 239 matching examples pass in matching order, the smallest meaningful
next environment comparison is **one complete original eight-file topic**,
seed 13353, full plugins, same source and frozen failing dependency graph, in a
disposable runtime aligned to native Ruby 3.4.12 (revision 366f5fdc00) and MariaDB
11.8.6, with the native Ubuntu client/header version and a newly built mysql2
extension. This retains the preceding-example history that the native failure
had; an isolated-only test cannot rule out an environment-by-history interaction.
This proposal changes the environment tuple, not one individual component, and
therefore would not by itself assign blame to Ruby or MariaDB.

Preparation boundary for that conditional experiment:

1. B verifies available exact public runtime artifacts/packages and records their
   hashes and complete inputs before execution. Prefer disposable Ubuntu 26.04.1
   userland matching native packaging; do not modify host packages, repository
   pins, the source checkout or the existing bundle. Use a separate bundle/DB
   directory so native extension/library identities cannot mix with Nix's build.
2. Record the actual Ruby binary/revision, DB server/client/header versions,
   mysql2 extension/library identity, tool versions, loaded gems, frozen lock
   hash, plugin mode and relevant environment, plus native-like database startup
   with REPEATABLE-READ and snapshot isolation OFF. Reuse the exact fixture/schema
   bootstrap. Do not claim complete runner equality: image/provisioner/kernel,
   caches and hidden process state may remain different.
3. Use a fresh pinned Luna/low watcher and the same diagnostic/native JSON outputs.
   One topic result is the stopping condition; no second graph, seed, retry or
   automatic environment matrix. Preserve complete order and the exact failure
   cause if present. Native runtime was about 19–22 minutes; the local Nix topic
   estimate is 30–60 minutes. Assess matching-environment cost after artifact
   availability, before launching a cold build or broad image-preparation effort.
4. If exact artifacts cannot be obtained within a bounded normal setup, report
   the missing input and best explicit partial match to the lead instead of
   silently substituting. If this controlled topic is green too, report that
   the original rejection remains unreproduced; diagnostics/instrumentation,
   runner internals and transient DB/process state remain possible factors.
   A speculative product fix would still be unsupported.

Only the lead selects any follow-up when investigation resumes. A diagnostic
experiment or graph pin used to control inputs is not a proposed production fix.

## Independent execution packages

### A: public CI evidence and input comparison — proposed implementer0

Own `ci-evidence.md` and raw `evidence/ci/` in this session. Read-only public
GitHub retrieval and canonical Git inspection; no project edits or tests. Recover
both runs' exact evidence, verify source/runtime differences, enumerate ordered
example IDs where available, and provide effective dependency inputs to Package B.
Validate JSON parsing, artifact/run identity, hashes and native failure details.
Acceptance: independently supported input table plus native result/log paths;
exact gaps stated. B's source trace does not depend on A; controlled reproduction
does. Stop at missing/unrecoverable evidence with a precise recovery proposal.

### B: validation mechanism and bounded reproduction — proposed implementer1

Own `validation-reproduction.md`, raw `evidence/reproduction/`, and isolated
diagnostic prototypes only. Read the public vpsAdmin worktree and HaveAPI 0.32.2
source; map cleaner -> adapter -> authorization -> query/includes with exact
locations. Capture the rejection text/class and the rejecting branch using
synthetic fixture IDs. Before longer checks, consume A's input receipt. Keep
the source fixed; label every uncontrolled dependency difference.

Start with the exact example under the closest verified failing graph/seed,
then the exact platform-operations manifest if isolated behavior differs.
Use a fresh pinned Luna/low monitor per long/uncertain check under the monitor
skill. No unbounded matrix, production DB, cluster or temporary public service.
If native inputs cannot be recovered, a local matched/reconstructed graph can
demonstrate a mechanism but cannot silently become an exact CI reproduction.

If order dependence is observed, minimize a preceding-example sequence with
the graph held constant and identify the state transition; if graph dependence
is observed, compare seeds at fixed graph and vary one dependency group while
holding order/source constant. Retain counterexamples. Do not run a broad matrix
before one discriminating result. First batch: source trace plus at most one
isolated and one topic reproduction; report mechanism/input gaps before more.

Acceptance: exact rejection mechanism with minimal synthetic evidence, or exact
known/unknown boundary and next bounded experiment; propose the smallest secure
owner-local change and focused regression plan. No production patch required.
If a substantive patch becomes necessary, route scope through lead first;
implementer1 owns any hook preparation/signing and checks before commits.

Architect owns this design and final synthesis. Lead assigns saved members,
accepts deviations, maintains plan/state and resolves shared edits/Git operations.
The packages share read-only source but have disjoint evidence paths; only B may
write diagnostic prototype inputs. Neither changes registered branch history.

## Compatibility, security and recovery

Investigation changes no persistent schema/data, migration lineage, protocol,
API metadata, generated Nix configuration or deployed component. Diagnostic data
must be disposable. No deployment ordering or rollback is required for evidence.
Stop and identify ownership before any cleanup; leave the session open.

Any later proposal must explain valid/missing/hidden/malformed reference behavior,
API envelope/count/includes semantics, public existence disclosure, admin behavior,
and old clients submitting IDs. An integer filter may avoid resource validation
but can alter generated schema and parsing semantics: evaluate these explicitly,
not as an automatic choice. A scoped validator change may preserve metadata but
must retain authentication and prevent serialization leaks. Schema/client changes
would need Go/Rust/TypeScript assessment and regeneration under project guidance;
none is performed merely to deliver an investigation. Persistence remains readable
by old software; software rollback reinstates the old request behavior.

## Verification and delivery boundary

Quick checks: source/ref identity, artifact hashes/JSON, exact example and resource
path, query/inclusion visibility, and small diagnostic syntax checks if needed.
Longer checks: monitored exact example/topic with native JSON, explicit graph,
seed and isolated DB; only causally justified order/dependency controls afterward.
Unexpected kernel builds stop for investigation. A green rerun is a counterexample,
not proof that the defect is harmless or solely timing-related.

Final findings must distinguish observed facts, demonstrated mechanism and open
causality; identify the smallest proposed remedy versus optional hardening; and
give security regressions across anonymous/user/support/admin and all advisory
states, valid/missing/malformed filter IDs, counts and includes. Routine evidence
needs no automatic review. A completed substantive patch would instead require
commit, quick checks and independent final review before long integration checks.
