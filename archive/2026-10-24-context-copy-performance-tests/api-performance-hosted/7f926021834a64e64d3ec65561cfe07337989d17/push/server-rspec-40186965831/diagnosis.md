# Exact-head server RSpec failure

Source/run: `7f926021834a64e64d3ec65561cfe07337989d17`, push run40186965831,
attempt1. Full logs/jobs retained locally; artifact query succeeded with zero
artifacts, matching the workflow's lack of failure-upload step.

Observed: Ruby3.2,3.3,3.4 each run540examples with the same2 failures:
`runner_spec.rb:22` clean live worker exit expected0 got3;
`runner_spec.rb:72` sqlite-clean worker with absent/development RACK_ENV expected0
got3. Documentation-assets succeeds. No subprocess stderr appears in the
RSpec failure because these expectations report only the returned exit code.
Exact child error text is therefore unavailable in the hosted logs. No local
reproduction or checks ran during C's campaign.

Source/config mismatch: Worker.inputs quick requires ROOT/Gemfile.lock and
ROOT/servers/ruby/Gemfile.lock after scenario measurement/validation. Both
lockfiles are deliberately untracked. Each RSpec matrix job only invokes
ruby/setup-ruby with working-directory servers/ruby; actual setup logs show
bundle lock writing servers/ruby/Gemfile.lock and vendor/bundle preparation.
No matrix step prepares root Gemfile.lock. The documentation-assets job has
its own independent checkout, so its Nix preparation cannot supply that input.
The missing-root-lock contract is deterministic for a fresh matrix checkout.

This explains positive clean workers returning3 at postmeasurement input proof,
while the earlier query/wrong-output fault checks pass their expected errors.
Strict source/runtime/dependency proof in production remains required; C owns
isolated spec/control input preparation and better child-error assertions. D
routed full evidence/source/config proof to C and lead, with the explicit
limit that child stderr was not retained by these failing assertions. No
A/B production fixture behavior is implicated by the available evidence.
No source change, rerun, installation or budget relaxation was performed.
