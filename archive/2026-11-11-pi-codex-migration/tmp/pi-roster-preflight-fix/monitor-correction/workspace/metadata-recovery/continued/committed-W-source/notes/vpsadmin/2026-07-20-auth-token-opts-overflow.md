# MFA token scopes overflow `auth_tokens.opts`

## Symptom

Creating a least-privilege API token with many action scopes and an account
that requires MFA returns a server error from `/_auth/token/tokens`:
`ActiveRecord::ValueTooLong` / `Data too long for column 'opts'`.

## Cause

vpsAdmin stores the token request's lifetime, interval, and split scope list as
JSON in the temporary `AuthToken#opts` continuation row. The column originated
as `VARCHAR(255)` and remains a string in the current core schema. The
security-advisory client's 34 scopes serialize to 1,042 bytes and cross the
limit at the ninth scope. Password-only token issuance bypasses this temporary
column, while MFA and forced-password-reset continuations use it.

HaveAPI accepts the scope string but does not persist this application-specific
continuation state, so the schema defect is in vpsAdmin.

## Fix

Add a vpsAdmin core migration that changes `auth_tokens.opts` to `TEXT` with a
65,535-byte limit and regenerate the core-only schema. Add a focused token
configuration spec that requests a representative long scope through MFA,
completes the continuation, and verifies the final session scope.

Deploy the migration before retrying token creation. Existing API code is
compatible with both column types because the serialized JSON contract does not
change. Continuations expire logically after five minutes, but rows remain
until the scheduled `vpsadmin:auth:close_expired` task removes them. Before
rolling back to `VARCHAR(255)`, wait for expiry and confirmed cleanup or
explicitly close the temporary rows, then verify that `SELECT COUNT(*) FROM
auth_tokens WHERE OCTET_LENGTH(opts) > 255` returns zero. Assess normal MariaDB
DDL locking for the production migration.

Do not work around the failure by disabling MFA or broadening the token to a
short wildcard scope.

## Verification

On vpsAdmin `1bca29dfa`, a temporary RSpec example using the exact advisory
scope list and an MFA-enabled user reproduced the expected
`ActiveRecord::ValueTooLong` (1 example, 0 failures). The existing focused
token-config spec remained green (6 examples, 0 failures) because it uses the
single `all` scope and has no MFA token-request case.

Related initiative:
`work/2026-07-20-security-advisory-review/`.
