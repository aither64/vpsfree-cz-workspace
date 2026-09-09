# Risk and compatibility review

Reviewer: fresh gpt-5.6-sol / xhigh, review_risk.
Reviewed exact packet bases/heads and actual preceding production service pin
1acc1955f0e7b4f2b67a18674d02a6da8e9e8da4. No nested agents.

One Important finding; no other Blocking, Important or Advisory findings.

The original runbook let upgraded api1 serve while old api2 remained active.
Old authentication/password.rb verifies without a user lock/generation and
user_session/new_token_login.rb can publish a session after new User::Update
changes the password and closes sessions. ResumeToken does not bind sessions
to authentication_generation, so the session survives the subsequent upgrade.
The recovery flag does not protect ordinary password changes. The accepted
audit-detail gap did not cover this revocation gap. Rollback overlap has the
same defect.

Require both old API processes to exit before new api1 starts: runtime-mask
and stop api2 while api1 remains masked, verify both ActiveState=inactive and
MainPID=0, then start upgraded api1 and switch api2 under its mask. Pause manual
authentication/password-writing shells and scripts. During rollback, unmask
neither old API until both new processes have exited and both old configs have
been restored. The reviewer confirmed no additional credential issuer outside
vpsadmin-api.service; supervisor does not serve those paths. Stopping recovery
and auth-maintenance units also preserves the intended cutover ordering.
Existing MFA tokens/OAuth codes may cross the barrier because subsequent new
password changes revoke pending authority under the user lock.

Root implemented the recommended narrower deployment boundary in the existing
rollout-documentation commit. No application/schema/pin change. See remediation.md
for final commit and verification. The JSON repair is appropriately limited to
the demonstrated API dependency failure. Pending VM/build/CI/live checks remain
the validation gate after remediation.
