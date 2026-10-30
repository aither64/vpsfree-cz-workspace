# Post-review documentation verification: CI failure stop

Candidate `35c1fb964735639c0873aacf078e18569f05f9bc`, tree
`756b61de87833d8ded478b5d7785618671b4ddcb`. This is a stopped package,
not completed installed-snippet acceptance. Source/index remain clean.
All 2,148 protected input/evidence SHA256 values still match the publication
receipt. No tests, builds, package installs, artifact extraction, Git mutation,
source repair, live HTTP/browser/service or lifecycle action ran.

## Current-head CI, attempt 1

All four runs are completed push events for the exact candidate:

- Server `40723980063`: assets passed; Ruby 3.4.11 passed 846 examples,
  seed 17265; Ruby 3.3.12 and 3.2.11 each failed one of 846 examples,
  seeds 8310 and 50541.
- Branch build-only release `40723979876`: passed. Restore-original-artifacts
  step was skipped; Test-and-build-maintained-packages executed successfully.
  Publish-approved-artifacts job skipped. The log proves unrestricted server
  846/0, generated-profile target 18/0 and supplemental exact
  dynamic_protocol_spec + dynamic_python_login_spec target 7/0; all three
  documentation Node scripts and current JS build also executed. Thus these
  scopes need no duplicate local run for the candidate's actual CI graph.
- JavaScript `40723979827`: passed its declared npm test command.
- Python `40723979835`: Python 3.11-3.15 checks and integration passed.

Full run/jobs/artifact API JSON and complete logs are `ci-*.json`,
`jobs-*.json`, `artifacts-*.json`, and `log-*.txt`. The source's unrestricted
RSpec default discovery includes all 78 server spec files, including all
10 performance specs; see `ordinary-performance-discovery.json`. The server
Ruby 3.4 lock text is retained as `ci-server-ruby34-lock.log`. No claim is
made that CI graphs equal local or frozen graphs. Full release locks/tools
remain to be obtained from its source-bound artifact manifest.

## Concrete failure

Both older-Ruby failures are the same test-only portability assumption at
`servers/ruby/spec/documentation/validators_spec.rb:83`: it demands
`extra: false`, Ruby 3.4's Hash#inspect display. Actual older-Ruby output is
`{:extra=&gt;false}` inside the correctly labelled lossless Ruby fallback.
The product intentionally renders `value.inspect`; labels, key and false are
preserved. Owner0 owns the smallest assertion repair, retaining Additional
details / Ruby value / false semantics. No product or test edit was made here,
and no CI rerun was requested. Lead received the exact finding before further
execution. The branch-build success does not waive the failing matrix.

## Remaining authorized package scope

Release artifact `12830949266`, name `release-40723979876`, is available,
1,193,104 bytes, API zip SHA256
`2ee47c3bd898fc9f94540e32974c5b64505c5c136b680df113d145c9ae84ace7`.
It has not been downloaded or accepted for local use. Its source/version,
manifest/locks/tools, npm tarball, wheel/sdist and package contents need proof.
Then the existing dynamic acceptance harness must run twice with this same npm
and wheel, then sdist, in distinct outputs. This executes six thorough variants;
no installed simple-program equivalence can be claimed. No local docs/encoder/
generated-profile duplicate is currently needed based on executed CI above.

## Watcher and handoff

Fresh retained 3ff7 utility `dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`
completed the bounded four-run log download, exit 0, about 18 seconds command
time. Native turn_context confirms gpt-6-luna / low / danger-full-access / never;
see `ci-watcher-native-policy.json`. No watcher or owned command remains active.
Single utility capacity is released. A later operation requires a fresh watcher.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
