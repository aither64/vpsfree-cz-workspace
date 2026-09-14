# DDNS update exception investigation

## Goal

Explain the `undefined method 'role' for nil` DDNS exception in the attached
2026-09-14 21:00 +0200 email and recommend a fix if required. Scope: investigation
and a fix proposal. Implementation and deployment are outside this step.

## Affected repositories

- `vpsadmin`: API DDNS resource, update operation, lifetime helper, and specs.
- Workspace: investigation records only. Inspect the canonical bare clone;
  no project feature branch or worktree is needed for this diagnosis.
- The email is an external local input and must remain outside version control.
  Do not retain its update token or raw request environment in artifacts.

## Approach

1. Extract the exception, action, authentication context, and deployed revision
   without retaining credentials.
2. Follow the request path from token lookup through the account-state check
   and compare deployed code with freshly fetched upstream master.
3. Inspect history and existing tests to explain the trigger and coverage gap.
4. Reproduce the failing helper using actual source and synthetic objects;
   validate a proposed change in memory, preserving non-active account checks
   and the authenticated administrator exception.
5. Record evidence, scope, limitations, and a concrete recommended patch.

## Compatibility and deployment

The anticipated fix is confined to an API nil-user guard. Preserve record-token
authentication and account-state enforcement. No database schema, persisted
format, client contract, node protocol, generated configuration, or vpsAdminOS
change is expected. API instances can be updated independently; old instances
remain susceptible until updated. Rolling back requires no state conversion
but restores the bug. No production mutation or live DDNS request is needed
for the investigation.

## Testing plan

Use local source-level reproduction with synthetic active and non-active
owners, anonymous callers, regular authenticated users, and administrators.
Inspect HTTP DDNS specs for ownerless versus user-owned zone coverage. Describe
the request regressions needed before implementation is accepted. Do not claim
database-backed or live endpoint validation from the helper reproduction.
