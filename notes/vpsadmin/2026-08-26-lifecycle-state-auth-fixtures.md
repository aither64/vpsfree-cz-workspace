# Keep lifecycle-denied users out of authorization fixtures

Initiative: `work/2026-08-18-vpsadmin-password-reset`

## Symptom

Both core and full `users-auth` CI topics failed the state-log endpoint tests.
The examples expected HTTP 403 from an administrator-only endpoint, but
received HTTP 401 before endpoint authorization ran.

## Cause

The state-log fixture deliberately made its target user's newest requested
state `soft_delete`. Once authentication began checking both materialized and
requested lifecycle state, that user could no longer authenticate. The test
was accidentally using the lifecycle-denied target as its ordinary-user
caller.

## Fix

Authenticate endpoint-authorization examples as a separate ordinary user
whose effective lifecycle state remains active. Continue targeting the user
whose state-log history includes the destructive request.

When a resource test intentionally creates a pending destructive state, do
not reuse that object as an authentication fixture unless the test is meant to
exercise lifecycle denial.

## Verification

The focused state-log resource suite passes 13 examples with zero failures.
The corrected examples reach endpoint authorization and receive the intended
HTTP 403 response.
