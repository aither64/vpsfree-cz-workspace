# Typed API language evaluation

Advisory findings, 2026-11-12. Owner: architect0. Audience: lead and maintainers
considering a rewrite. This is an investigation brief, not a rewrite decision or
implementation release. No implementation packages are currently needed or
authorized. Lead owns plan/state and acceptance; this package owns only this file.

## Recommendation

Evaluate **Kotlin first for the API and HaveAPI server**, with **Rust as the
comparison candidate** if extending one language across more of the control plane
is important. C# is a credible close alternative to Kotlin when maintainers prefer
.NET. This ordering is an architectural judgment from the sampled code, not an
empirical claim that an LLM writes one language more correctly.

The API's difficult work is permissions, resource accounting, explicit asynchronous
state transitions and recovery across MariaDB and nodes. Kotlin can express that
domain with sealed variants, explicit nullable types and conventional readable
application code. Rust can express it very well too; its ownership model provides
additional local memory/concurrency guarantees, but those do not establish database
isolation, correct authorization or safe distributed retries.

Rust business logic need not be dominated by lifetimes: owned command/result
objects, identifiers, ordinary structs and explicit SQL can keep ownership local.
Measure actual code and maintenance effort before assuming Rust is too expensive.

## Bounded repository evidence

Read canonical bare repositories with `git show`, without fetching or accessing
peer worktrees. These are local snapshots, not freshly verified upstream heads:

- vpsAdmin: `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`.
- HaveAPI: `7835acafdda19779815a0f1ba905d78e0085456d`.

Read root instructions, entry docs and relevant architecture/protocol pages.
Representative implementation inspection was limited to selected sections of
four API files, two HaveAPI files and the node signature verifier:

| Boundary | Evidence and implication |
| --- | --- |
| HTTP, policy and domain | `vpsadmin/api/lib/vpsadmin/api/resources/vps.rb`: Start/Stop enforce tenant restriction, maintenance and object-state checks before creating a blocking chain. A typed ID alone does not prove the current caller may use it. |
| Database preparation | `vpsadmin/api/models/transaction_chain.rb`: `fire2` constructs a staged chain inside a database transaction, acquires locks and exposes it as queued only after successful preparation. States include rollbacking, failed, fatal and resolved. |
| Nontrivial business change | `vpsadmin/api/models/transaction_chains/vps/update.rb`: dirty attributes drive node commands, deferred database edits, logs, ownership handling and resource reallocation. Translating an ORM model mechanically would miss this workflow. |
| Persisted command and confirmation format | `vpsadmin/api/models/transaction.rb`: signed JSON includes chain, dependency, handle, node, reversibility and command input. Confirmation records contain table names, primary keys and attribute changes; this is a persisted integration contract. |
| Node trust boundary | `vpsadmin/libnodectld/lib/nodectld/transaction_verifier.rb`: RSA/SHA256 verification operates on the supplied serialized data. A future serializer must preserve the verified message semantics and binding. |
| Framework behavior | `haveapi/servers/ruby/lib/haveapi/action.rb`: authorization hooks affect discovery; descriptions include action layout and metadata, and endpoint discovery can invoke preparation. |
| Input boundary | `haveapi/servers/ruby/lib/haveapi/parameters/typed.rb`: explicit coercion, nullability and validation precede domain use. Static application types cannot replace parsing these external values. |

The vpsAdmin `docs/overview.md`, `docs/transactions.md` and `docs/plugins.md`
establish the wider component map:

- HaveAPI supplies the API framework/protocol. PHP WebUI, Ruby CLI, generic clients
  and generated clients depend on its behavior.
- The API owns policy, models and chain preparation. Plugins can add models,
  actions, chains, hooks and independently tracked migrations.
- nodectld polls MariaDB for queued work and applies confirmations directly to
  database tables, without ActiveRecord callbacks. This shared database is part
  of the API/daemon interface, not merely an API implementation detail.
- Supervisor/node reports and RPC use RabbitMQ alongside the database queue.
  Scheduler, console router and download mounter have separate responsibilities.
- vpsAdminOS/osctld is an independent host platform. Node operations invoke its
  facilities; changing API language does not require rewriting that platform.

## HaveAPI contracts to preserve

Sources: HaveAPI `doc/protocol.md`, `doc/typed-input-validation.md` and sampled
implementation above. This list identifies pilot obligations; it is not a complete
conformance audit.

1. Versioned `OPTIONS` discovery at API/version/action levels; authorization can
   filter actions and parameter visibility. Static OpenAPI alone does not replace
   caller-dependent discovery or the existing generic-client behavior.
2. Nested resources, routes, HTTP methods, layouts, namespaces, associations,
   validators, defaults, examples and global/per-object metadata.
3. Authentication flows, response envelopes and parameter errors, localized text,
   and blocking actions exposing progress through `action_state_id`/ActionState.
4. Strict documented coercions and **omitted / explicit null / value** as separate
   states. A nullable field by itself cannot represent all three. Use an explicit
   patch-field variant and validate at JSON/query boundaries.
5. Authorization and tenant-scoped lookup remain runtime decisions. Domain values
   and command constructors should make validated intent explicit; they cannot
   replace transaction-time authorization and concurrency checks.

A typed replacement should derive descriptors and codecs from the same action
definition where practical, while retaining dynamic permission filtering. Avoid
recreating Ruby metaprogramming as unchecked dictionaries, casts or reflection
behind a typed façade. Decide explicitly whether plugins remain runtime-loadable
or become compiled modules; a closed type hierarchy and open plugin extension
points require separate boundaries.

## Language tradeoffs

| Candidate | Fit for this domain | Material cost or limit |
| --- | --- | --- |
| Kotlin | Strong first API candidate: sealed command/result hierarchies, exhaustive `when`, nullable types, concise domain-oriented code and JVM integration. | Java platform types, assertions and reflective mapping can weaken guarantees. Keep domain objects separate from mutable persistence/transport objects; SQL, mapping and migrations still need runtime tests. |
| C# | Credible alternative for typed application/domain code, records, generics and .NET integration. | Nullable references use static diagnostics; configure the build appropriately and do not treat annotations as runtime validation. Native union availability depends on selected compiler/runtime; this brief makes no unsupported claim that modern C# lacks unions. |
| Rust | Particularly attractive when the same language should cover API services and more systems work; enums/newtypes and explicit results can model domain boundaries directly. | Ownership and async integration add concepts to maintain, even with simple owned DTOs. Memory safety does not imply correct SQL, permissions, serialization, retries or compensating actions. |
| Go | Credible for small services, operational tools and node orchestration; conventional code can be easy to inspect. | Less direct expression of closed algebraic workflow states than Kotlin/Rust. Tagged values/interfaces and checks can work, but would not be my first choice when compile-time domain modeling is the principal reason to leave Ruby. |
| TypeScript | Good option for UI/client work and convenient discriminated-union domain modeling. | External JSON and database values need runtime schemas/codecs; casts and `any` can bypass the useful guarantees. It is less compelling if the central objective is a stronger authority boundary rather than web-stack familiarity. |

F# is a serious conditional alternative if maintainers actively want a functional
domain core on .NET. That is a team preference to establish, not an automatic
extra language in this plan. OCaml does not yet have a demonstrated project-specific
advantage sufficient to enlarge this bounded evaluation.

Primary language sources checked on 2026-11-12:
[Kotlin sealed hierarchies](https://kotlinlang.org/docs/sealed-classes.html),
[Kotlin null safety](https://kotlinlang.org/docs/null-safety.html),
[C# nullable references](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/null-safety/nullable-reference-types),
[Rust enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html),
[Go specification](https://go.dev/ref/spec),
[TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).
No specific ORM/framework or release version has been selected. Library support,
database-provider behavior and packaging need validation against pinned versions
in any later pilot.

## Scope changes the answer

**API/HaveAPI only:** prioritize comprehensible policy and transaction logic;
Kotlin is the initial recommendation. Preserve Ruby daemons and clients behind
existing contracts during evaluation.

**vpsAdmin control plane including daemons:** Rust becomes more competitive as a
common language. Kotlin, C# and Go can also orchestrate external host tools; a
node process is not automatically a low-level memory-management workload. Choose
based on measured footprint, integration and maintenance needs.

**All vpsAdminOS/native host integration:** this is a materially larger project,
outside the requested rewrite scope. Native liblxc and host-system interaction
would favor considering Rust separately, with FFI/unsafe review and operational
requirements. Language unification alone is not sufficient reason to rewrite it.

The immediately useful unification target is shared schemas, explicit domain
concepts and conformance tests. Different implementations can satisfy those
contracts without one language everywhere.

## Future evaluation, if separately authorized

Compare Kotlin and Rust using the **same bounded VPS Update workflow**, initially
the DNS-resolver change/clear path. Include existing tenant/admin permissions,
object-state checks, lock acquisition, signed node command preparation, deferred
confirmation and failure/rollback. Expand the sampled code evidence first to
settle the exact rollback/retry contract; the current reading does not certify it.

Keep transport DTOs, validated domain commands and persistence records distinct.
Use domain-specific IDs and explicit patch/result/state variants. Pick simple
SQL/repository boundaries before evaluating ORM convenience; confirm actual SQL,
isolation and schema constraints rather than equating typed queries with correctness.

Quick acceptance checks would cover compilation, missing-variant handling,
wrong-ID rejection, omitted/null/value decoding, denied access and existing-client
response/schema parity. Longer disposable-database checks would exercise old/new
API and daemon combinations, concurrent updates, duplicate delivery, restart at
commit/dispatch/confirmation boundaries, reversible failures and fatal rollback.
Compare resulting database rows, locks, command bytes/verification and observed
node effects. Passing compilation is necessary evidence, not the acceptance test.

Measure human review effort, clarity of the operation, implementation/repair time,
defects caught by compiler versus tests, and remaining unsafe casts/dynamic escape
hatches. If evaluating LLM assistance, use the same model, prompts, requirements,
time budget and held-out tests; repeat tasks. Do not infer general superiority
from one generated example or an unmeasured familiarity assumption.

Any future pilot needs its own approved package owners, paths, pinned dependencies,
commands and acceptance evidence before execution. No builds or tests ran here.

## Compatibility, recovery and unresolved decisions

A first pilot should use fixtures/disposable databases and make no production
schema changes or node writes. A later incremental rollout needs additive,
old-reader-compatible persistence and protocol changes; keep command handles,
signatures, confirmations, state meanings and client envelopes compatible.
Do not replace Ruby and typed writers concurrently without proving ownership and
concurrency semantics. Do not dual-execute real node operations for comparison.

Software rollback must tolerate already-enqueued commands and state written by the
new process. It cannot erase a completed node effect. Retain compensating actions,
operator recovery for fatal chains, resource-lock rules and supported old schema
readers. Required coordinated node updates would change the cost and must be
justified explicitly; none are proposed here.

Open product decisions: how far unification should extend; existing maintainer
language/runtime preference; willingness to change plugin loading; required
HaveAPI/client compatibility duration; desired migration budget; and whether the
rewrite has a concrete benefit exceeding incremental typing or boundary cleanup
in the current system. These do not block this advisory finding; they block
selecting and releasing a future implementation package.
