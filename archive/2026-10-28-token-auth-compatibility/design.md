# Go token documentation compatibility

Design owner: architect0. Implementation brief ready for lead acceptance.
Scope: one HaveAPI fix and its regressions, followed by the requested master
integration and 0.31 backport/release. No application changes were made during
this investigation.

## Diagnosis and inspected revisions

Remote `master` is `2fc2b8f86c71a6062434bb60a24e174b20c1a520`;
`haveapi-0.31` is `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, also the
peeled `v0.31.1` tag. Read-only `git ls-remote` confirmed these revisions and
no `v0.31.2` tag. The bare clone's local master/release heads are older;
implementation must start from the remote target, not those local heads.

`Token::Config#query_parameter` defaults to `:_auth_token`.
`ClientExample::Profiles#finalize` captures the mounted description through
`StructuralSchema.copy`, whose real JSON round trip converts that scalar to
`"_auth_token"`. The Go adapter copies hash keys but preserves scalar types.
Its `Documentation#render_auth` token branch compares both transport names
with strict equality, incorrectly rejecting the matching automatic profile.
Existing Go unit fixtures use String names on both sides, hiding this case.

## Implementation and invariants

Add one small private/protected comparator in
`clients/go/lib/haveapi/go_client/documentation.rb`, used for the token branch's
`http_header` and `query_parameter` comparisons. Both operands must be a String
or Symbol; compare their `to_s` values only after that type check. Reject other
types rather than coercing them or mapping them to a shared nil sentinel.

Equality stays exact and case-sensitive: no stripping, case folding, aliases,
or fallback to only one matching transport. Both names must match. Preserve
the existing requirement that saved provider, visible provider and supplied
authentication descriptor all exist. Keep existing limitation messages and
environment-token example unchanged. Basic and OAuth2 behavior is outside
this fix and remains unchanged.

Do not change token configuration defaults, shared JSON copying, scalar copying
throughout the adapter, generator/runtime authentication, or other renderers.
The comparator is local to the documentation compatibility decision and must
not mutate either description. A brief nearby comment may explain the JSON
String/Symbol boundary; no new public configuration or documentation framework
is needed.

## Execution package and regression acceptance

One implementer owns the complete source/test package; splitting overlapping
adapter tests among implementers would add coordination without useful parallelism.
Permitted files:

- `clients/go/lib/haveapi/go_client/documentation.rb`: comparator and token call site.
- `clients/go/spec/unit/documentation_spec.rb`: focused acceptance/rejection cases.
- `clients/go/spec/documentation_profile_check.rb` and
  `clients/go/spec/support/documentation_profile_fixture.rb`: extend the existing
  real mounted fixture and pure check, with no compiler or listener required.

Unit cases must render `api.SetExistingTokenAuth(os.Getenv("HAVEAPI_TOKEN"))`
for equal String/String, Symbol/Symbol and mixed String/Symbol names in both
directions. Exercise supported header and query-name normalization. Freeze the
saved adapter before changing the visible description so drift is real.
Changing either header or query name alone must return the existing mismatch
limitation. Numeric/boolean/nil values must not become equivalent names through
coercion. Missing saved or visible token provider, or absent auth descriptor,
must remain unavailable. Reuse existing Basic/OAuth2 checks.

The mounted regression enables a token provider using a minimal subclass of
`HaveAPI::Authentication::Token::Config` with its default transport settings,
registers an automatic Go profile using only `import_path`, and mounts the real
server under the existing `/mounted/` path. Use the actual profile adapter and
request-visible description from that server. Assert the live query parameter
is `:_auth_token`, the captured adapter value is `"_auth_token"`, and token
rendering returns code containing the environment-token call. Do not stub
`StructuralSchema.copy`, supply a manually normalized saved schema, or bypass
mount finalization. This must fail before the fix and pass afterward.
The existing `documentation_profile_check.rb` is a standalone check, not an
automatically discovered `_spec.rb`; run and record it explicitly.

## Checks and delivery order

Quick checks in the repository's prepared Nix environment:

1. Focused Go documentation unit specs, explicitly selecting sibling Ruby-client
   and Go sources as in `make test-go-cli`.
2. Run the existing pure mounted profile check from the prepared server bundle:
   `bundle exec ruby -I../../clients/ruby/lib -I../../clients/go/lib ../../clients/go/spec/documentation_profile_check.rb`
   from `servers/ruby`. Run `make doc` before server-side checks.
3. RuboCop for changed Ruby files using the declared development environment;
   `git diff --check` and ordinary required commit hooks.

Commit intended changes, then obtain independent final review of the full
base-to-head series and final diff, explicitly recording no migrations.
After review, run relevant broader Go/server documentation checks and required
CI, including the existing performance gate for client changes. Use the
dev-session-monitor watcher for uncertain or long checks. Do not add benchmark
fixtures or performance tooling for this comparator. Stop once required checks
pass; repeat only for relevant changes or unresolved failures.

After master integration, backport the fix with `git cherry-pick -x` onto a
feature branch based on fresh `origin/haveapi-0.31`, rerun the focused checks,
and review any nonmechanical difference. The four scoped files above currently
match between the inspected master and 0.31 targets.

## Compatibility, release and recovery

This changes documentation selection only. API wire formats, actual token
authentication, generated SDKs, persisted state, database schemas/seeds,
protocols, daemon interaction, Nix options, CLI and Terraform behavior do not
change. There are no migrations, token rotations, or coordinated node updates.
Existing String names remain valid; equivalent Symbol names now display the
same example. Genuine transport/provider drift remains rejected.

Deploy the updated Go generator gem in the documentation server environment,
normally with the matching HaveAPI server version because automatic profiles
default to the server's generator version. Existing SDKs need no regeneration.
Ordinary package rollback is safe and restores the old documentation limitation;
new software creates no state that an older version cannot read. Infrastructure
deployment is not part of this assigned execution package.

The supported patch target is `haveapi-0.31`; the next observed version is
`0.31.2`. Recheck the target and tag before release. Keep fix and release metadata
in separate commits. Follow that branch's release procedure: prepare dependencies
in top-level `nix develop`, use `make version VERSION=0.31.2`, add the existing
dated changelog heading with a Go-generator fix entry, and run release checks.
All maintained components share the release version. The lead owns integration,
publication authorization and the protected GitHub `release` environment step;
this design assignment performs no publishing. Preserve tags, original artifacts
and receipts on failure; do not overwrite published versions or rebuild accepted
artifacts. Record execution evidence in state, not in this proposed procedure.
