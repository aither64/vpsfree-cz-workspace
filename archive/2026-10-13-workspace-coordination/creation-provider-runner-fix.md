# Provider-enabled terminal startup correction

The deployed creation error occurs in `Runner#native_provider_arguments` while
reconciling the terminal after the initial goal. The method calls `@runner`, but
`Runner#initialize` retains `@command_runner`; its `capture` returns stdout,
stderr and process status. The faulty helper originates in upstream 5421e563,
before this initiative's base. The actual provider-enabled path was absent from
session tests and was not covered by the read-only UI acceptance harness.

This is a bounded lead-owned correction: use the initialized command runner and
unpack stdout. Preserve argv validation, configured provider selection, command
environment, shell escaping, ownership, creation receipts, recovery and runtime
generation checks. No state/schema, public interface or deployment order change.
Old and new versions read the same data; an old rollback retains the startup bug.

Verify a provider-enabled terminal restart with the real command runner and an
isolated executable returning native arguments. Assert the complete shell-decoded
command reaches the exact retained thread/socket with correct arguments and that
invalid output refuses before terminal dispatch. Exercise the real reconciliation
method during an isolated creation fixture without overriding it. Run focused
checks before an independent retained-reviewer assignment, then exact packaged
verification. Keep the prior UI/VM evidence for unchanged components; test the
affected session/provider path. Deploy an exact successor under the same held
reservation, without touching the user's failed session or launching a duplicate
conversation. Keep every predecessor source/evidence and consolidate consumer
pin updates. Merges remain paused.

The current threadless initiative has no valid roster; the lead owns this edit.
The scope is a two-line command-runner correction with existing contract checks,
so a direct lead brief is sufficient. Any broader lifecycle or provider change
requires revisiting this scope and verification plan.
