# P4-A canonical accounts and provider switches

Committed source checkpoint:
**`6a3631ef6ee225d7c532f62bd5f0222bb6fc582d`**, exact parent
`a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b` (P3 account API/enforcement).
Exactly the eight owned paths below, 507 additions/11 deletions. Lead writing
pass closed before commit; the seven Go-source hashes match the final 0.091s
check, with no unchanged test rerun for prose. Exact staged/committed/current
blobs and whitespace verified; index empty and D window released immediately.
Normal tempfile `git commit -F`, no bypass/push/peer files. Final hash manifest:
`/tmp/p4-a-commit-manifest-2026-11-11-pi-codex-migration.json` (disposable).
This supersedes the dependency-held status below. Original source/check and
dependency provenance remain for combined review; consolidate the logical P4
stream before final review. No loader or native fallback activation is included.

Owner: implementer5. Source/fake milestone ready 2026-11-12, 12:18 UTC;
commit remains held on the committed P3 typed API, lead writing pass and D
index window. P4 plus identity fix were accepted before this continuation.
No other executing package. Saved contract: design.md canonical account
projection and provider-switch correction; architect0 accepted the private
complete-Resolved provenance detail during implementation.

## Owned source and dependency

Repository/worktree D:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`,
branch `2026-11-11-pi-codex-migration`. Observed starting head
`fc02306ab8e66f85fdae06519b1c907dc1728120`; final commit parent/head pending.

Exactly eight owned paths:

- New `portal/internal/piproviders/accounts.go`, `accounts_test.go`,
  `account_switch_test.go`.
- Modified `types.go`, `resolve.go`, `settings.go`, `piproviders_test.go`
  in that directory, plus `docs/pi-providers.md`.

P3 owns actual `piruntime.AccountBinding {Provider,AccountRef string}` and
`CanonicalCredentialRef = "canonical"`; no local substitute or P3 source was
edited/staged. The dependency exists in same-session working source but was
not yet committed at the starting head. Implementer1 separately reported its
clean full source checks and pending commit window. P4-A cannot be committed
before that buildable dependency parent.

## Delivered source boundary

`ProjectRuntimeAccounts(Catalog, []Target, canonicalRef)` strictly validates
the exact selected routes, thinking and canonical store/native provider key,
returning deterministic sorted/deduplicated native-provider/account bindings.
Unsupported selected mappings refuse. `SelectableRuntimeAccounts` instead
scans all available canonical model routes, including noninitial eligible
providers, and skips unrelated unsupported/unverified rows. Malformed/ambiguous
catalogs fail and empty/over-64 startup unions refuse. Neither projection changes
catalog gates/digest, reads tokens or infers auth from AccountRef labels.

Full all-chain policy availability remains unchanged. With fallback execution
disabled, strict runtime use covers the actual primary; enabling more physical
targets requires projecting them too, without truncating/re-resolving the frozen
policy. Raw public gates must be intersected with the frozen startup map and
full policy/target admission by P2 composition. Exact API/usage was sent to
implementer2; no central integration edits were made.

`Resolve` validates the complete policy/catalog and strict canonical primary
projection. It records process-local provenance of every exported Resolved
field: session/member/source/requested/settings/catalog+policy digests and
independent Chain/Budget/FallbackOn snapshot. `Apply` rejects fabricated,
deserialized or modified results, including changed scope with a matching
modified handle. Ordinary value copies retain provenance. Exported slices do
not alias proof. This evidence is neither authorization nor native readiness;
P2 still supplies admission/current policy and P3 verifies frozen old/new pairs,
generation and idle/no-unresolved state. Persisted snapshots rebuild through
normal Resolve against the exact frozen catalog/policy.

Apply is switch-only: complete verified current settings and positive revision
are required; Create owns initialization. Same pair permits model/thinking
changes, same-revision replay remains exact, changes use current+1. Changing only
provider or account refuses. Both may change after valid strict provenance,
then one Configure call preserves requested/effective/outcome/error cause.
Partial/unknown/apparent-success-with-error holds; no rollback, input resend,
native router, auth broker or fallback activation was added.

## Checks and scope evidence

Started 12:12:46 UTC. Concrete helpers and first source fixtures passed within
approximately four minutes; final focused fixtures passed before the requested
ten-active-minute milestone.

Command:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command sh -c 'gofmt -w portal/internal/piproviders/accounts_test.go && cd portal && go test -mod=readonly ./internal/piproviders'
```

Final result: `ok .../internal/piproviders 0.091s`. Earlier changed-source
fixture milestones passed 0.084s/0.090s. The command uses the retained repository
D development environment, avoiding partial P7 flake evaluation. No long or
broader suite was launched by P4-A. The full existing piproviders suite passed,
including original policy/store/identity/digest/fallback cases.

New tests cover startup's noninitial provider union, exact canonical mapping,
unsupported/unverified rows, malformed aliases/duplicate account mappings,
same-model alternate credential key, sorted/deduplicated bindings, unchanged
catalog/digest, inactive unavailable chain refusal, complete current settings,
zero calls on wrong scope/revision/pair/target/provenance, one permitted switch,
precise cause/outcome and unchanged resolved state, and deep proof isolation.
Runtime same-history/global/other-member isolation is P3-owned, not claimed by
these fake Configurer tests.

Owned eight-file whitespace passed. Source SHA-256/Git blob manifest saved at
`/tmp/p4-a-source-manifest-2026-11-11-pi-codex-migration.json` (disposable);
commit hashes will be refreshed after the lead prose pass. Index remained
empty and no process remains. No peer source/index edits, credential reads,
login, model requests, native activation, deployment, lifecycle, push or merge.

## Review and remaining dependencies

This is the same logical P4 stream as
`f8cd2941626eac5fbe8e12c4e5a3fee9e309735a` and identity fix
`fc02306ab8e66f85fdae06519b1c907dc1728120`. Lead owns consolidation before
combined final review. No schema/data migration or deployed predecessor format
is introduced; existing policy/digest encoding and raw catalog gates are intact.
No repeated package/dependency input update was added. P3 initialization/Apply
semantics are a coordinated source-only contract correction before live release.

Risk remains high for provider/account and runtime selection contracts; final
review packet should retain general, architecture, scope and risk lanes. The
documentation amendment belongs in the owning project reference
`docs/pi-providers.md`, for portal/runtime integrators. It explains the exact
projections, canonical mapping, selection restrictions, provenance and switch
failure/compatibility behavior; lead writing pass is requested before commit.
Index/packaging/catalog composition remain with P7/P2. This record is temporary
execution evidence and does not replace that reusable guide.

Next: P3 typed API committed parent; lead writing pass and short D commit window;
exact final inventory/hash/check packet. Later production gates remain P3
authoritative account-source/frozen-map/native-settings proof and P2/P7 trusted
composition. Upstream account/Daybreak availability and required native fallback
budget/effect gate remain separate and unactivated. P4-A retains capacity for
this package and fixes; no next package accepted.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>
