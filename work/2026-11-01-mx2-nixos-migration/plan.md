# mx2 NixOS branch recovery and verification proposal

## Goal and scope

Locate the NixOS backup-mail-server branch in
`/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`, copy its committed
history into this workspace, and rebase onto current upstream defaults. Preserve
the source checkout and original refs. Suggest evidence needed before replacing
the CentOS 6 mx2. Production deployment and default-branch integration are outside
this request.

## Affected repositories

- `vpsfree-cz-configuration`: expected owner of mx2 configuration.
- Additional repositories only if source history proves an unmerged dependency;
  architect identifies these before expanding execution scope.

## Approach and owners

1. Architect `architect0`: locate source refs, inspect dependencies and mail
   behavior, record design and verification brief in `design.md`.
2. Implementer `implementer0`: import exact source history, create/register the
   session worktree, rebase onto fetched default, resolve bounded compatibility
   issues, run quick checks, preserve old/new ranges and publish feature branch.
3. Lead: accept evidence, maintain scope/tracking, coordinate independent final
   review of committed substantive configuration before long checks.

Use one implementer for this dependent repository package; other implementers
are retained and available only for demonstrated independent work.

## Compatibility and deployment

Assess SMTP relay policy, primary-MX routing, TLS, IPv4/IPv6 and durable queue
behavior. Do not assume a CentOS Postfix spool can be copied to modern NixOS:
propose queue draining and retaining the old host for rollback. Establish any
supported mixed-version or input/module compatibility from source evidence.
No production credentials, live mail, network identity changes or deployments.

## Documentation and readers

Operators need a staged verification proposal and cutover/rollback acceptance
criteria; preserve these in session design/findings for this requested proposal.
Record exact refs, rebase resolutions, check results and unresolved risks in
session state and linked evidence. Avoid adding an unsolicited testing subsystem.

## Verification

Quick checks follow repository instructions and available declared tooling:
Git range/diff integrity, formatting and Nix evaluation for mx2 as feasible.
Independent review covers full branch history, final diff and migration provenance.
Long builds/tests use a fresh policy watcher if required. Proposed runtime tests
must distinguish isolated repeatable checks from production acceptance evidence.

## Decisions

- User authorizes branch import/rebase and a verification recommendation.
- No default-branch integration or deployment approval supplied.
- Session remains open and active.
