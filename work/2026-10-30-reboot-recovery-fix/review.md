# Independent final change review

No Blocking, Important, or Advisory findings.

Reviewed directly by the fresh standalone fallback reviewer
`/root/final_review`, using `gpt-6.1-sol` with `xhigh` effort. The owning
threadless initiative has no retained reviewer. High risk; general,
architecture/repetition, scope/proportionality, and risk/compatibility lanes
were assessed after reading the mandatory skill, all four lane references,
applicable repository instructions and routed workspace procedures. No nested
agents, source changes, long checks, or session mutations were used.

## Exact reviewed history

| Repository | Base | Head | Complete branch series |
| --- | --- | --- | --- |
| codex-web | `9d337b70987fdf1dd42a5d8efff31f755a122550` | `d3a29bee90ef00a08816920408c596152339a637` | `d3a29bee` |
| dev-workspace | `4155d0099d03028b43d5f08d225a88156cb4155a` | `f05f50eed6dbfa2794502653176f0bbbbf20f1fa` | `6c9a6337`, `f05f50ee` |
| workspace | `3fa192f600293128871245efe55c6587ed82fb20` | `1deb88301418722ed1aebeaa2bebafd9b2e007d8` | `1deb8830` |
| vpsfree-cz-configuration | `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627` | `f9a6996153daec9e20a3feb58e05981b5907ef7b` | `f9a69961` |

Inspected every commit, its message, the complete final diffs, relevant callers,
tests, documentation, dependency declarations and consumer locks. All four
worktrees were clean at their packet heads. The series is focused: the public
option includes its tests/documentation; runtime dependency metadata is separate
from recovery behavior and its supporting tests/documentation; each deployment
consumer has one pin update. No obsolete unmerged approaches, superseded fixes,
unused compatibility paths or consolidation work remain.

There are no repeated update streams within these branch histories. The
codex-web input/module/vendor identities advance once together in `6c9a6337`.
The workspace's nested runtime and configuration's `devWorkspace` channel each
advance once to `f05f50ee`; their codex-web lock changes propagate that runtime's
single selected dependency. These are distinct consumers, not redundant
intermediate pin commits. No release or deployment exception is needed.

No migrations. No database, persisted-state format, journal, receipt, or native
thread schema changes occur in any reviewed range; consequently there is no
merged, released, deployed or externally consumed migration lineage to retain.

## Correctness and ownership

The fix matches the reported failure and remains proportional: expose an
existing native list filter in the public client, then select it at the shared
retained-discovery boundary. `nil` omits `modelProviders`; the explicit empty
slice is copied into a non-nil slice and encodes as `[]`, preserving the crucial
distinction. A selected list also preserves its values. Other callers retain
their preceding default behavior.

`RequireExactActiveConversations` still verifies only the already proved
root/member set, exact CWD, root source, member project identity, duplicate
identities, bounded pagination and cursor validity, then unions positively
verified loaded identities. Discovering more providers cannot adopt an unknown
identity: extra rows cause refusal. It also cannot resume threads, start turns,
replay submissions or rewrite history. Both semantic observation and archive
preflight use this owning function; their surrounding ownership, activity,
submission and repeated identity checks remain intact.

Consumer inspection covered the library's list API, runtime retained observation
and archive preflight, neighboring creation/member listing, and threadless
absence proof. The latter already sends an explicit all-provider raw request
under its separately owned project-partitioned negative-proof contract. This
change does not duplicate that contract or introduce a generalized recovery
framework. The library owns wire encoding; the runtime owns retained-set policy.

The wire test covers omitted, empty and selected provider filters. The runtime
regression models an empty loaded manager, provider-hidden saved rows, a root
and project member on separate pages, and refusal of an unknown extra row.
Existing focused tests cover changed CWD/source/project, missing retained rows,
unknown saved/loaded identities and disagreement between discovery sources.
The reported removal experiment reproduces the original missing-retained-row
failure, providing evidence that the regression exercises the fix.

## Compatibility and remaining verification

The Nix and Go pins select the same exact library revision, with one updated
vendor hash. Both downstream locks select the same runtime. The workspace
extension and unrelated inputs are preserved. The host imports the matching
runtime host module, while the user profile owns the application, consistent
with the prepared system-before-profile rollout. Native Codex is unchanged.
There is no new state that an older package must interpret; supported recovery
still uses the existing forward-only profile-switch procedure. An older
runtime would retain the discovery failure rather than gain a new state-format
incompatibility.

Documentation in `codex-web/docs/reference.md` and
`dev-workspace/docs/workspace-portal.md` explains the lasting filter semantics
and retained-identity invariant. Individual deployment steps remain in the
initiative rollout record. The documentation is consistent with the code.

Quick-check commands/results were inspected in `quick-checks.md`: library wire
test, focused runtime discovery/threadless tests, negative removal experiment,
diff checks, configuration hooks and the final cross-composition checker passed.
Library exact-head CI is reported passed there. No verification was rerun by
this read-only reviewer.

Remaining risks/test gaps: the current generated-schema corpus does not
explicitly exercise `modelProviders`, so the new Go wire tests alone do not
certify that field against a future native version. The recorded native probes
and the unchanged selected native version support the present fix. Packaged
runtime checks, disposable native restart verification, configuration/profile
builds and dry activation, deployed health, and exact retained recovery still
need the lead's planned post-review verification. This review does not claim
deployment, continued sessions, integration or readiness for use is complete.
