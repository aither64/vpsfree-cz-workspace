# Advisory input validation and bounded reproduction

Package B owner: implementer1, retained Sol/xhigh, workspace-write. Session,
environment markers and roster verified. Investigation/proposal only; no
production source, branch history, authorization or assertions changed.

Completed bounded batch: the isolated example passed, then the full topic passed
239/239 examples with the failed native run's exact source, dependency lock,
seed, eight-file manifest and complete execution order. The target stayed at
position 237. The original native validation rejection was not reproduced;
its exact class/message/branch and underlying cause remain unknown. No
production fix is justified by these results.

## Source and input identity

- vpsAdmin worktree: `worktrees/2026-11-04-vpsadmin-advisory-visibility-ci/vpsadmin`.
  HEAD is `4ac49f49e63545200df8afa920c6eafda8722523`; tracked files clean.
- Public HaveAPI 0.32.2 source used for the initial trace:
  `/nix/store/n6513maww0nmp4g1x8hmfr7zqnpxmysf-ruby3.4-haveapi-0.32.2/lib/ruby/gems/3.4.0/gems/haveapi-0.32.2`.
  This is installed public gem content, not another session's checkout or records.
- Package A recovered full locks from public job logs. Reconstructed lock bytes
  match native environment SHA256 exactly: failing
  `aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21`, passing
  `cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47`.
  They are hash-verified log reconstructions, not native lock artifacts.
- Both native runs used the same source and eight-file topic manifest. The graph
  differs only in activemodel/activerecord/activesupport 8.1.4 versus 8.1.4.1,
  and mime-types-data 3.2026.1027 versus 3.2026.1103. Native seeds differ.
- Native CI used Ubuntu 26.04.1 and Ruby 3.4.12, Bundler 2.6.9, RSpec 3.13.6,
  MariaDB 11.8.6. Runner image/provisioner/region differs between native runs.
  Local reproduction uses the repository's Nix environment; its actual runtime
  identities are recorded separately and must not be called identical to CI.

The failing lock was copied to ignored `api/Gemfile.lock`. The isolated
instrumentation and launcher live under `evidence/reproduction/` only.

## Exact static path

Paths below are relative to the vpsAdmin repository, except `haveapi/...`, which
is relative to the installed gem's `lib/` directory.

1. `HaveAPI::Action#safe_exec` calls validation before `prepare`, `pre_exec` and
   `exec` (`haveapi/action.rb:400`). `#validate` filters allowed input, then calls
   `Params#validate` with context (`:618`). `Params#validate` calls each parameter
   cleaner, collects `HaveAPI::ValidationError` under its field name, and raises
   aggregate `input parameters are not valid` if any field failed
   (`haveapi/params.rb:293–343`). `Action#validate!` converts this into an API
   error using the configured validation HTTP status (`action.rb:348`). This
   explains HTTP 200/status false/no count metadata without proving its cause.
2. `Parameters::Resource#clean` rejects nonnullable null, selects the resource
   Show input layout's model adapter, runs `input_clean`, then authorizes the
   resolved record (`haveapi/parameters/resource.rb:107–127`).
3. `ModelAdapters::ActiveRecord::Input.clean` rejects arrays/hashes/booleans and
   malformed/nonintegral/negative integer IDs, strips strings and determines the
   primary-key type (`haveapi/model_adapters/active_record.rb:171–251`). It calls
   an explicitly supplied `fetch` block or, normally, `model.find(value)` at
   line 209. A missing record becomes `HaveAPI::ValidationError` with resource
   not found; conversion failures become invalid ID. Exact localized text and
   the branch for this failure require runtime evidence. Its `ArgumentError` and
   `TypeError` rescue covers the whole method, including lookup and model
   callbacks. An `invalid ID` message with a normal numeric input may therefore
   mask a lookup/callback failure; inspect the original exception cause.
4. `Resource#authorize_record!` constructs a child Show context and invokes
   `Show#authorized?`; it does **not** call `Show#prepare`
   (`haveapi/parameters/resource.rb:165–186`). `SecurityAdvisory::Show` permits
   anonymous/non-admin readers and blacklists sensitive output fields
   (`api/lib/vpsadmin/api/resources/security_advisory.rb:259–279`). The global
   pre-authorization scope hook skips anonymous users (`api/lib/vpsadmin/api.rb:177`).
   Therefore hidden advisory state alone does not statically cause input rejection.
   The parent visibility scope is in Show `prepare`, outside this input path.
5. CVE Index query joins its parent and merges `SecurityAdvisory.visible_to`,
   then filters by the cleaned parent object; count reuses query and exec adds
   includes/pagination (`api/lib/vpsadmin/api/resources/security_advisory_cve.rb:60–76`).
   `visible_to` returns all states for admins and published only otherwise
   (`api/models/security_advisory.rb:28–32`). If validation succeeds, the hidden
   parent's list is intentionally empty.
6. Resource output serialization checks both child Show authorization and
   `prepare` before exposing unresolved metadata or included content
   (`haveapi/model_adapters/active_record.rb:354–437`). Unlike resource input,
   this path does execute visibility-scoped Show preparation. Included parents
   therefore have an additional visibility check. Direct child Show also joins
   and merges parent visibility before `find`.

## Related consumers and proposal constraints

| Consumer | Parent filter | Query/count protection | Additional boundary |
| --- | --- | --- | --- |
| CVE Index | Resource | parent join + `visible_to` | anonymous allowed |
| Update Index | Resource | parent join + `visible_to` | anonymous allowed; reporter output restricted |
| affected-user Index | Resource copied from output params | parent join + `visible_to` | authentication; non-admin `user_id` restriction |
| affected-VPS Index | Resource copied from output params | parent join + `visible_to` | authentication; non-admin `user_id` restriction |

Nested node-status Index uses the path parent ID and applies the same parent
visibility query; it does not clean that ID as a Resource filter. It is a useful
control, but has a different invalid/missing-parent contract.

No integer-filter conversion is selected. Resource input carries Resource
metadata, strict identifier conversion, referenced-record existence validation
and referenced Show authorization. An Integer parameter can change all four,
including missing and malformed-ID responses and generated client types. A
proposal must follow the demonstrated failing branch, preserve ownership/auth
and all states/count/includes behavior, and cover all four consumers consistently.
No client regeneration is part of this diagnostic task.

The current Resource filter's statically established input contract is:

| Input | Current handling |
| --- | --- |
| omitted | optional; query applies only visibility/ownership and other filters |
| explicit null | `cannot be null` validation error; these filters are not nullable |
| blank string, array, object, boolean, fractional float, malformed string, negative integer | invalid-ID validation error |
| valid existing advisory ID | resolves the model; checks Show authorization; action query applies visibility/ownership |
| well-formed missing advisory ID | resource-not-found validation error |

String IDs accept surrounding whitespace and an optional sign; integral finite
floats are accepted by the integer-primary-key adapter. Plain Integer input
retains strict numeric coercion but permits negative values without a separate
validator and does not validate existence or referenced Show authorization.
Thus changing only the parameter kind would alter behavior even if ordinary
existing positive-ID requests still return the same rows. The isolated test
demonstrates existing hidden IDs succeed and return empty lists/counts for
non-admin readers under the failing lock in the local runtime.

Any later fix should focus regressions on the demonstrated branch, then cover
all four filters across draft/published/retracted and anonymous/user/support/admin
(401 remains required for anonymous affected-user/VPS lists). Check ownership
with a second user's retained projections, row/count agreement, included parent
content, direct hidden child 404s, omitted/missing/malformed IDs, and unchanged
retained history. Do not broaden into unrelated advisory hardening.

## First bounded experiment

The first operation runs the exact scoped ID
`spec/api/resources/security_advisory_spec.rb[1:3:2]`, seed 13353, full plugins,
with the recovered failing lock and `BUNDLE_FROZEN=true`. Runtime-only diagnostic
prepend wrappers report parent Resource cleaner entry/return/error, parent Show
authorization, whether a child query is reached, and validation/record-not-found
raise locations. They call the original methods unchanged. No assertions are
removed. Only synthetic fixture IDs and errors are recorded.

Fresh watcher: `/root/watch_isolated`, Luna/low, utility identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, catalog digest
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
The matching installed utility config requires full access/approvals never.
It owns Nix dependency preparation, execution and the process handle. Kernel
builds are an immediate authorized cancellation/escalation; quiet output alone
is not a timeout.

Command: `bash evidence/reproduction/run-isolated.sh` using the absolute session
path (launcher sets repository CWD). Logs: `evidence/reproduction/isolated.log`;
exit: `isolated.exit`; native JSON: `isolated-results.json`; runtime graph:
`isolated-environment.json`; Nix inputs: `source-flake.lock`.

The repository's existing test framework creates and shuts down its isolated
temporary MariaDB, normally `/tmp/vpsadmin-test-db-auto-*`. No production DB,
development cluster or public service is used. If the isolated example passes,
the next allowed operation is the exact eight-file platform-operations topic at
the same fixed graph/seed. Report that first discriminating result before any
further order/dependency experiments.

### Isolated result

Passed: 1 example, 0 failures, seed 13353, RSpec 334.608 seconds; about 6m40 total
including initial dependency preparation. Exit 0, no kernel build, no remaining
operation. The post-preparation lock SHA256 is unchanged. Loaded versions are
Rails trio 8.1.4.1, mime-types-data 3.2026.1103, HaveAPI 0.32.2, RSpec 3.13.6,
Bundler 2.6.9; plugins `all`. Actual Ruby is 3.4.9 and MariaDB 11.4.12, versus
native CI Ruby 3.4.12 and MariaDB 11.8.6. Local database isolation matches:
REPEATABLE-READ, `innodb_snapshot_isolation=0`.

The first anonymous draft Resource cleaner entry received String `"1"`, returned
the retained draft advisory with ID 1, and allowed parent Show authorization.
CVE and Update queries were reached. Across all reader/state combinations in
the example there were no Resource cleaner errors. Expected hidden child Show
requests raised `ActiveRecord::RecordNotFound` inside visibility-filtered find;
these are controls, not the reported validation failure. Both assertions for
empty list/count succeeded in the isolated example.

The effective installed gem's Resource and ActiveRecord-adapter source files
were compared byte-for-byte with the initial Nix-store source used for tracing;
both match. A passing isolated run with the failing graph is a counterexample
to a deterministic graph-only failure under this local environment. It neither
proves order dependence nor rules out Ruby/DB/native-environment dependence.

### Exact topic operation

Fresh watcher `/root/watch_topic` (same verified pinned utility model/effort and
identity, new operation/context) owns `run-topic.sh`. It uses Package A's native
eight-file manifest, same frozen failing lock, full plugins and seed 13353.
Logs/result/runtime identities are `topic.log`, `topic.exit`,
`topic-results.json`, `topic-environment.json` under `evidence/reproduction/`.
Diagnostic errors now also preserve cause class/message/backtrace to detect a
callback error masked by adapter `invalid ID`. Production source remains clean.

Native full-topic durations were 19–22 minutes; the local estimate was 30–60
minutes after the 335-second isolated example. This was an estimate, not a
cancellation deadline. No unexpected kernel build occurred.

### Topic result and complete native comparison

Passed: 239 examples, 0 failures, 0 pending, 0 errors outside examples, seed
13353, RSpec 2932.288 seconds (48m52s), exit 0. The target passed in 303.659
seconds. The runtime receipt confirms full plugins, Bundler 2.6.9, the same
failed lock SHA256, Rails trio 8.1.4.1, mime-types-data 3.2026.1103, HaveAPI
0.32.2 and RSpec 3.13.6. Ruby remains 3.4.9; MariaDB remains 11.4.12 with
REPEATABLE-READ and snapshot isolation OFF.

`evidence/reproduction/topic-vs-native.json` compares every native/local example
after normalizing only the harmless leading `./` in IDs:

- Both sets contain exactly 239 unique IDs; no missing or extra examples.
- Complete execution order is identical, not merely the seed or target position.
  Its normalized JSON-array SHA256 is
  `5d4cbe069392150467308971488faea9f3446d619be56f368621df1943c10769`
  in both results.
- The target is position 237 in both runs and is the only status difference:
  failed natively, passed locally. The other 238 examples passed in both.
- The target emitted 168 diagnostic events and no Resource cleaner errors.
  Its first anonymous CVE filter received String `"55"`, resolved draft advisory
  ID 55, allowed parent Show authorization and reached the visibility query.
  The Update filter followed the same path. All role/state assertions completed.

This is a counterexample to a deterministic failure caused by source + failed
dependency graph + native example order alone in the local environment. It does
not establish that dependencies or order are irrelevant in the native runtime,
that the failure was timing-only, or that a product defect has been fixed.

Final source check: HEAD remains
`4ac49f49e63545200df8afa920c6eafda8722523`, tracked files clean; effective
`api/Gemfile.lock` still has the exact failing hash. No further graph/order
matrix or native-aligned test was launched.

## Native runtime availability and preparation boundary

The read-only assessment is preserved in
`evidence/reproduction/native-runtime-availability.json` and its raw official
release/index metadata. It found no realized Ruby 3.4.12 or MariaDB 11.8.6 Nix
store outputs. Podman is installed; the queried `ubuntu:26.04` image is not
cached. No environment was prepared.

Native CI used a preinstalled Ruby at
`/opt/hostedtoolcache/Ruby/3.4.12/x64`; its log records revision `366f5fdc00`
but no binary/archive checksum. The official
[Ruby builder release](https://github.com/ruby/ruby-builder/releases/tag/ruby-3.4.12)
lists `ruby-3.4.12-ubuntu-26.04-x64.tar.gz`, 42,575,614 bytes, with metadata digest
`sha256:b4943e5d36b82f38c3f3c9f979a1d1b5dfb9769dcada5e70945e0fe63b6b8586`.
The archive was not downloaded or executed, so its runtime revision and equality
to CI's binary are not independently certified here.

Official Ubuntu [main](https://archive.ubuntu.com/ubuntu/pool/main/m/mariadb/)
and [universe](https://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb/)
indexes retain the exact native `1:11.8.6-5ubuntu0.1` server, client,
`libmariadb3`, development and compatibility-header packages for `amd64v3`.
These are public availability observations, not installed-package or complete
dependency-resolution receipts. No package binaries were downloaded/installed.

A normal binary/container preparation would still require a cold Ubuntu image
pull, exact apt dependency resolution/install, Ruby revision verification and a
separate frozen bundle with native extensions, including mysql2, built against
the matching client/header libraries. Source builds of Ruby or MariaDB are not
required in principle by the available artifacts. Setup time is unmeasured;
10–20+ minutes was a rough estimate, followed by one full-topic run (native
19–22 minutes; this host's Nix run took 49 minutes). This is not an execution-ready
tuple or a promise of full runner equivalence.

The lead accepted this availability boundary and selected completion of the
bounded investigation without another environment/test batch. A cold build or
image-preparation project, source/pin change and silent runtime substitution
were not undertaken.

## If the exact rejection remains unavailable

The smallest supported next change would improve a disposable reproduction's
failure diagnostics, rather than change advisory filtering. The existing spec
diagnostic deliberately records only `errors` class/field names. Its full
synthetic response error values would distinguish resource-not-found, invalid ID
and nullability messages. To identify an invalid-ID error that masks a callback
failure, capture `Resource#clean`'s validation error and its original cause
before `Params#validate` collects only its message into an aggregate error.
The isolated prototype demonstrates this boundary without changing behavior.
An API request-exception hook alone cannot recover the handled field-validation
cause from the returned envelope.

A native follow-up should retain the same source, failed lock, full topic,
manifest/order and seed, and carry this narrow diagnostic. If local Ruby/DB
alignment is available without a cold build/image project, the architect's
conditional brief calls for one complete topic in that aligned runtime; the lead
selects it only after the active result. Exact native runtime matching may still
leave runner/kernel/process/cache and binary-identity differences. No product
patch, graph freeze or authorization change is justified by an unreproduced
validation envelope.

Remaining uncertainty is specific: native CI lacks the raw parent ID, actual
context authentication state, field validation message, exact rejecting branch,
original exception/cause, complete machine/process/DB state and gem binary
checksums. Local Ruby/DB/client/header/native-extension and OS identities differ;
diagnostic instrumentation and timing also differ. Matching the complete RSpec
order does not freeze application random values or all process state. None of
these unresolved variables has been isolated as the cause.

The smallest justified next action is cause capture in a controlled native
reproduction, using the existing diagnostic prototype at the cleaner boundary
and complete synthetic error values. Preserve actual context role, raw ID type,
lookup/authorization/query progress and the original error cause. Then fix the
demonstrated owning component and run the focused regression surface above.
Do not convert filters to Integer, change authorization, skip assertions, add
retries or pin a graph as a product fix on the current evidence.

## Effects and handoff

Both operation-scoped watchers completed with exit 0; neither owns a running
check. The existing test-DB helper owns automatic shutdown/pruning on process
exit. No unfinished command effect is known. Raw evidence and the ignored local
bundle/lock remain preserved; no session lifecycle or cleanup action was taken.
The lead maintains state/portal tracking; no additional tracking commit is needed
for this package. Product documentation and generated clients remain unchanged
because the task changed no product behavior or exported contract.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-vpsadmin-advisory-visibility-ci/
