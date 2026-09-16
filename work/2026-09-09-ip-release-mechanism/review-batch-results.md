# Atomic batch release review and remediation

High risk: ownership release, asynchronous cleanup, quota, schema and admin/member
boundaries. All four required lanes reviewed committed vpsAdmin b282bbe77
(follow-up b76affa12..b282bbe77); first six prerequisites remain unchanged.
Every reviewer used fresh gpt-6-astra/xhigh context, without nested reviewers.
General used collaboration; architecture/risk/scope used ephemeral read-only
processes after the retained-thread limit. No blocking findings.

## Reconciled findings

1. Important (general/scope): known preparation exceptions erased the attempt.
   Catch ConfigurationError and UserResourceMissing inside its savepoint boundary.
   Verify unavailable signer and missing quota; no ownership change survives.
2. Important (general/architecture/scope): outer database rollback lost selected
   membership. Capture IDs before chain preparation and restore them when
   recording contention in the fresh transaction. Deadlock/timeout tests pass.
3. Important (general/risk): attention state allowed reasons/exemptions and
   assignment links while recovery could still release the address. Use the
   owning attempt's active? check for row editability, fail closed if history
   is missing, and verify resolved-with-pending confirmations remains protected.
4. Important (architecture/scope; risk rated advisory): retries rewrote resolved
   historical outcomes. Count released markers only for the relevant chain;
   verify an earlier recovered failure remains failed after a later release.
5. Important (architecture): nested Attempt.Show lacked its parent resolver.
   Add the established HaveAPI resolver returning campaign and attempt IDs,
   check response metadata/traversal, and use the association in WebUI.
6. Important (scope): missing coverage inventory entries for both attempt
   endpoints. Register the existing endpoint coverage and run inventory check.
7. Advisory (scope), addressed: remove obsolete per-IP last_error column/API/UI
   and writers. Attempt errors own the diagnostics. Rewrite unmerged migration
   directly and regenerate core schema/locales; no compatibility shim.

These are direct remediations within the reviewed design, with no expanded
contract or new abstraction; no reviewer rerun required. Shared disown helper
and commit split were accepted. Remaining limits: fatal recovery is an operator
operation; distributed cleanup can enter fatal state, but owners/quota stay
reserved until recovery, and no automatic retry is provided.

## Verification after remediation

- Recovery/serialization + endpoint inventory: 12 examples, 0 failures.
- Attempt association/auth HTTP check: 1 example, 0 failures.
- Updated migration up/down: 2 examples, 0 failures.
- Missing quota/history focused rerun: 2 examples, 0 failures. The first run
  exposed a fixture-only AR association delete_all nullification; deletion via
  the model relation fixed the fixture without changing production behavior.
- API locales regenerated; core schema diff removes only obsolete last_error.

Final commit hooks and the exact KB pin passed. DNS and networking browser
integrations passed, and the reset review cluster passed read-only administrator
and member checks. The storage/backup/export browser integration also passed
on final35e. Current-head hosted workflows are tracked in state.md. Earlier quick checks and package
assumptions are in review-batch-packet.md. Raw review process logs are transient
/tmp/ip-release-batch-{architecture,risk,scope}-{review.log,result.md}.

## CI fixture isolation correction

Hosted API engine jobs exposed a committed concurrency-fixture leak: refreshing
SpecSeed.node status made the shared seeded pool eligible for later migration-key
discovery. The ordered concurrency14 + migration-key3 reproduction failed exactly
those three key cases. Restoring the original node/status and audit rows makes
all17 pass. This changes only the campaign concurrency spec; production and
existing key-generation assertions are untouched. The fix is folded into the
owning campaign commit. Final review/CI revisions are recorded in state.md.

The test-isolation delta d2ebb98f4..2a9fdf2dd received fresh general and
architecture reviews (gpt-6-astra/xhigh), both with no findings. Low risk,
test-only fixture restoration; no new scope/security/compatibility boundary.
It is folded into API5dab29165, resulting vpsAdmin head35e400de2. Runtime
integrations on d2ebb98f4 remain applicable because only unit-test setup/teardown
changed. Review packet: review-batch-fixture-packet.md.
