# Go client final review and narrow G1 remediation

Lead saved this condensed report from independent reviewer0's full delivery.
One **Important** finding, G1; no Blocking finding or other findings. Meaningful
changes support the proposed first v0.1.0 after G1 and remaining gates. Review
is not integration or tag/publication permission.

## Exact reviewed scope

Reviewer0, independent retained gpt-6.1-sol/xhigh/read_only; saved identity and
same-session binding verified without overrides, fallback or nested reviewer.
All four mandatory review lanes applied, high risk for public field/type removals
and copied runtime/authentication/language behavior. Read workspace and local
instructions, complete series/diff, source context, input/verification evidence
and maintained HaveAPI source/tests. No source edits, tests or remote writes.

Repository git@github.com:vpsfreecz/vpsadmin-go-client.git; target master.
Reviewed base `73f164dd5eeebfc494705ae27981d30872fa88c3` to
`2c4f55bb5682c37601bddc5aba9ff8d1f6a7f101`:

1. `8a7483d535ac8caf86d318c89a773afde79c5ee2`: generated client.
2. `2c4f55bb5682c37601bddc5aba9ff8d1f6a7f101`: README/changelog.

Clean, whitespace check passes. 611 files +22475/-13488, generated output plus
36 documentation lines. Root go.mod, shell.nix and dependency graph unchanged.
No new handwritten runtime or release mechanism. Fresh output and deliberate
stale-file removal follow generator ownership. Recorded compile22seconds and
minimum-compiler check are bounded results, not aggregate working-time evidence.

## Important G1: inherited Custom input boundary

Generated IpReleaseCampaign.Create/Exempt and IpReleaseRequest.Keep omit required
Custom `addresses`; WebuiUserSetting.Set omits required Custom `value`. Their
typed request builders cannot satisfy the saved contract. Existing maintained
emitter intentionally excludes Custom inputs; compilation and deterministic
output do not detect this. Original release notes announced these operations
without the limitation.

Reviewer requests the smallest fix: accept and document the inherited boundary,
name the affected typed calls, and explain existing low-level DoBodyRequest with
a complete body and suitable response type or another client. No request for
new generator support or generated hand patches. Full typed Custom support would
require revised provider design/regeneration/review. A narrow documentation fix
may be inspected directly by the lead under the mandatory skill's narrow-fix rule.

## Independent inventory, compatibility and provenance assessment

- Hashed all682 current files against both checked inventory and fresh candidate;
  reconstructed all648 old hashes from exact base. 84 additions,50 removals,
  475 changes; repeated generation identical. All46 executable/library/template/
  metadata/shared-schema inputs, including i18n_messages.yml, match receipt.
  No generated hand patch evidenced.
- Independently traversed previous Client type/constructor graph: none of50
  removed files reachable. Exported stale types remained directly callable, so
  cleanup is source-breaking and correctly documented.
- Confirmed Message→CsMessage/EnMessage; Node-update drops Cpus/TotalMemory/
  TotalSwap; advisory Note→CsNote/EnNote and NodeId/NodeName→Node. Inspected
  setters/maps/composition. No surviving field type changes found.
- Variadic NewValidationError preserves zero-argument calls and old struct
  literals but changes exact constructor function type; docs correctly require
  wrapper for func() *ValidationError variables. No masking shims introduced.
- Language headers and localized errors are copied from HaveAPI. Existing auth/
  HTTP-client handling stays. OAuth revoke uses captured HTTPS endpoint while
  retaining same/explicit-trusted-origin checks before sending tokens; no trust
  exemption added. API7, module identity and Go1.16 declaration retained.
- Maintained provider specs cover language/validation/header/legacy literals,
  timeout, OAuth form-body/origin behavior; exact-head provider CI remains gate.
- Logs show format/compile with Go1.26.8 and official Go1.16.15 under CGO0/Nix
  loader. Verifies language/stdlib floor, not protocol behavior. No tests or
  workflow in SDK; go test is compilation smoke.
- Accepted public snapshot hash70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d,
  profile public-live-api-7.0,151/519 application and1/5 authentication. Capture
  permissions/plugins bound API surface, declarations do not grant permission.
  No production operation invoked during review.
- Generation sourcef046; reviewed successor0e7166 changes only two CI Ruby
  selectors, same source/ten locks. Keep truthful acquisition and bind final
  release artifact evidence. Retained-gem correspondence not yet established.

**Complete history:** generated/docs split justified; no obsolete approaches,
fixups, transitional paths, repeated updates or superseded pins. No consolidation
remaining. **No migrations** introduced/changed. API binding names referring to
migrations are not DB migrations; no persistent-format/fleet transition.

Remaining gates: resolve G1, final retained Go/shared-schema artifact identity
and exact-head provider tests, input evidence, separate integration/publication
authorization. Authoritative remote has no tags; v0.1.0 is first proposed version,
not a next minor following an existing release. Session open.

## Lead acceptance and direct remediation inspection

Lead accepts the inherited Custom-input boundary and implements the requested
narrow documentation remedy. No generator scope expansion. Final lead-written
README/changelog explicitly document the four new affected calls plus inherited
WebAuthn required public_key_credential and SystemConfig optional value. They
explain complete namespaced request bodies, generated-validation bypass, manual
error/API-status checks and that low-level calls do not populate Output.

Owner amended only docs commit to
`134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`; generated commit unchanged.
Final range `73f164dd5eeebfc494705ae27981d30872fa88c3..134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`,
611 files +22505/-13488. Lead directly inspected full old/new diff: only the
requested README/changelog clarification; client/ and go.mod byte-identical.
Whitespace and clean-tree checks pass. Compiler, generation and input evidence
remain applicable. G1 **closed** by documented accepted boundary, no new behavior;
no review rerun needed under narrow-fix rule. Old reviewed range retained in
review-g1-remediation.json; final two-commit history has no superseded update.
Owner force-with-lease published only its dated feature branch with exact old
head; remote final head proved, default unchanged; no workflows to cancel.
Native final comparison captured. Artifact checks and approvals still pending.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
