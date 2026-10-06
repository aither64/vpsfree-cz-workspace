# 2026-08-14-advisories-6-12-95-5

## Goal

Add and publish a reviewed vpsAdmin security advisory for CVE-2026-64563, the
only CVE first covered by the cumulative vpsAdminOS 6.12.95.5 live patch. Add
durable repository guidance that live-patch descriptions and coverage are
documented under `vpsadminos/docs/os/livepatches/`.

## Affected repositories

- `security-advisories`: repository instructions, one advisory dossier,
  reviewed production evaluation, regression coverage, and the unpublished
  vpsAdmin submission baseline.

The vpsAdminOS, Linux, vpsAdmin, and vpsfree-cz-configuration repositories are
read-only evidence sources. The 19 already-published advisories first fixed by
live patches v2 and v3 remain unchanged.

## Approach

1. Verify CVE-2026-64563 against the Linux CNA record, introduction and stable
   fixes, vpsAdminOS live-patch documentation and source, and current platform
   source.
2. Add a bilingual denial-of-service dossier for the unprivileged
   `NETLINK_SOCK_DIAG` rhashtable walk. Record the exact fixed and open-ended
   stable ranges and bind mitigation only to reviewed active `livepatch_5`
   identities.
3. Collect fresh typed Node evidence, evaluate the full retained kernel
   history, and preserve actual mixed-rollout state. Require zero unknown
   conclusions before synchronizing an unpublished draft.
4. Keep repository guidance, the CVE dossier, and the generated remote draft
   baseline in separate reviewable commits. Run the mandatory fresh-context
   review before draft writes and use the same reviewer for follow-up.
5. Push and verify feature-branch CI, synchronize only the CVE-2026-64563
   draft, then fast-forward the repository default branch after final checks.
   After the user authorized publication, run a new freshness/readiness
   preflight and publish only the exact reviewed revision. A separate email
   notification remains prohibited.

## Compatibility and deployment

This work adds assessment data and an unpublished vpsAdmin record. It changes
no API, schema, protocol, runtime configuration, deployment, or persisted
platform format. A live patch mitigates only an interval where its exact
module, version, boot kernel, kernel source, and clean vpsAdminOS identity match
a reviewed tuple. Pre-v5, missing, inactive, or transitioning patch state is
not treated as fixed. Storage Nodes remain outside scope only if source and
workload review confirms that they do not expose the VPS trigger.

Draft synchronization and publication use fresh evidence, revision
preconditions, and exact readback. Concurrent Node or remote-review drift stops
the write. The user supplied the required publication approval after reviewing
the completed draft status; this does not authorize a separate email.

## Testing plan

- Validate every dossier and the new CVE individually.
- Collect and evaluate fresh production evidence with zero unknown Nodes;
  verify vulnerable-to-v5 transitions and storage-role exclusion.
- Run full RSpec, RuboCop, active Overcommit hooks, and `git diff --check` from
  `nix develop`.
- Run the mandatory standalone change review after local commits and quick
  verification, resolving significant findings before the remote draft write.
- Push the feature head and require exact-head GitHub Actions to pass.
- Dry-run and apply synchronization for CVE-2026-64563 only, commit the exact
  submission baseline, and run read-only readiness when all affected Nodes are
  resolved.
- Re-run repository checks in a fresh fast-forward integration worktree and
  require exact-head default-branch CI to pass.
- Collect fresh evidence after integration, repeat readiness, publish the exact
  reviewed advisory revision with the explicit approval switch, and verify the
  published readback without sending a separate notification email.
