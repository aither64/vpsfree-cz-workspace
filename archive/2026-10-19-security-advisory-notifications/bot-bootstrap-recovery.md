# Bootstrap recovery review remediation

Status: accepted by lead and reviewer under step-9 narrow-fix policy, consolidated
and published as `49a8ff8086b7b325f9f1a8f4825619f8e03245ce`. Prior reviewed head
was `2756ee653fb844a611a9f2083ca8890a1f70f72d`. No full review rerun required.

The reviewer found that a bootstrap list/CVE exception escapes the one-shot API
setup timer after `api_setup?` becomes true. The new initialized guard then skips
all later polls forever. Accepted narrow repair retries unfinished advisory
bootstrap from the existing minute check under the existing mutex, returning
silently on that tick. Store and startup watermark are established once for the
bootstrap; retries reuse them. Readiness/deadline are set after complete success.
No shared Api change, public contract, new retry timer/framework or prose change.

The lead accepted this exact approach. Proposed patch is
[bot-bootstrap-recovery.diff](bot-bootstrap-recovery.diff). Source is 18 changed
lines; four new examples add 76 spec lines. The cases exercise repeated list
failure, partial CVE failure across all modes, silent recovery without update
queries, original cursor/single store allocation, future consumption/output and
full summary interval after successful recovery.

Exact verification, from bot worktree in documented Nix environment:

```sh
nix develop -c bash -c 'bundle exec rspec spec/vpsfree/irc/bot/security_advisories_spec.rb && bundle exec rubocop lib/vpsfree-irc-bot/security_advisories.rb spec/vpsfree/irc/bot/security_advisories_spec.rb && bundle exec rspec && bundle exec rubocop && nixfmt --check tests/suite/vpsadmin-events.nix'
```

PASS exit 0: focused 38 examples/0 failures, focused RuboCop 2 files clean;
full 150 examples/0 failures, full RuboCop 63 files clean; Nix formatting clean.
`git diff --check` also passes. No long checks, builds or CI dispatch performed.
Lead owns narrow-fix acceptance under mandatory-change-review steps 9–10.

Lead released publication after final old-head review. The approved YAML quoting
note/sample correction is also included in the exact committed old-to-new
[bot-review-remediation.diff](bot-review-remediation.diff). No source behavior
changed after the successful 38-example focused and 150-example full quick runs.

Final publication replaced only the expected old head using explicit
`--force-with-lease=refs/heads/2026-10-19-security-advisory-notifications:2756ee653fb844a611a9f2083ca8890a1f70f72d`.
Superseded old-head queued Integration Tests 39315420422 is confirmed cancelled;
old-head RSpec 39315420448 was already successful. Current-head workflows were
left active and handed to lead: RSpec 39317498639; Integration Tests 39317498503.
