# Final member-report transport review

The retained independent reviewer
`01a0cb4d-69fe-7bc3-a722-6ea267aa29b9` ran read-only at GPT-6 Sol/xhigh
on the High-risk General, Architecture, Scope, and Risk lanes. It reviewed
codex-web `2a228e7`, generic `04bb52a`, extension `08f576a`, and workspace
`7db8779` against `review-transport-packet.md`. It found no Blocking issue.

## Important: uncertain assignment across a package switch

Generic `1529d96` changes assignment text and binds a package-specific MCP
executable path. These enter the client's durable send identity. Reusing an
old, uncertain message ID after a forward package switch can fail before the
client checks whether the original send was accepted. This is not a rollback
requirement, but an automatic retry gap for an in-flight assignment.

Decision: accept this bounded gap for the sole aitherdev development host.
The user explicitly prioritizes a forward-only cutover and permits restarting
idle sessions; no known assignment is awaiting an uncertain retry. The package
switch will quiesce sessions and refuse active or queued member turns.
Maintaining a cross-generation identity or an old-envelope compatibility path
would expand the durable client contract and force another cross-project pin
cycle for an unobserved state. If a pre-switch uncertain ID is encountered,
inspect that member's transcript. Send a new assignment with a new ID only
after confirming the prior assignment did not arrive; otherwise do not resend
until the outcome is resolved. Generic documentation commit `b7883be` records
this operator action. This does not claim old IDs can be retried after a later
package-path change.

## Advisory: identity-bound tool on fork

The shared client guide implied an identity-bound MCP policy could be passed
unchanged to a fork. That could give the destination the source member's report
identity. The generic runtime already leaves start and fork unbound until the
destination thread ID exists. Codex-web documentation commit `86aaa2e`
clarifies that policy rule. This is a narrow documentation correction, not a
new protocol or security boundary; no reviewer rerun is needed.

Long verification remains: pinned-binary two-turn MCP contract, packaged
check, aitherdev switch, and live read-only and workspace-write member reports
to the correct lead with stale/wrong-session refusal. The two post-review
documentation commits are not repinned downstream because they change no
package code or behavior.
