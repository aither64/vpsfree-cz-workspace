# Mounted URL and execution-cleanup final review

**No new Blocking, Important or Advisory findings.** The affected-lane review
gate passes for the completed URL/authentication contract correction and native
fixture/diagnostic follow-up. Actual installed-package acceptance and final-head
verification remain outstanding; this is not a release or integration approval.
Earlier reports are preserved, including the original findings and their narrow
remediation record.

## Identity and exact reviewed range

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Retained independent reviewer `reviewer0`, purpose `review`, thread
  `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Live same-session roster independently confirmed ready state and saved/assigned
  `gpt-6.1-sol` / `xhigh` / `read_only`. No overrides, fallback reviewer or nested
  agents. `dev-session current` printed the bound slug; identity environment
  variables were both absent and the trusted thread binding supplied ownership.
- Repository `vpsfreecz/haveapi`, intended target `master`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Complete reviewed history: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`.
- Final tree `fed8aea303bb91eb488c4c4bbc639356a7488c21`; exact last complete
  commit message `Version 0.30.0` with no body.
- Prior reviewed/remediated and core-verified head
  `27b4f8f895a4e5401357a402187c2a4590699aec` remains supporting evidence.
  Independently inspected its 27-path semantic delta to the new head and the
  complete 22-commit final history, rather than treating old CI as current proof.

Applied all four lanes at high risk: general, architecture/repetition,
scope/proportionality and risk/compatibility. Read the mandatory-review skill,
Shared Reviewer Instructions and all four lane references; applied repository
guidance, the frozen mounted-URL contract, packet and owner receipts. The new
public URL/authentication boundary required this review; unchanged previously
reviewed behavior was assessed through exact history/diff comparison.

## URL, authentication and compatibility conclusions

JavaScript has one owning resolver policy in `protocol.ts`: strict descriptor
paths bind against `base.origin`. Callback action invocation already uses that
strict path; ordinary actions, token request/continuation/renew/revoke and
callback action-state helpers therefore acquire the correction together.

The async shared pipeline distinguishes descriptor requests through internal
`RequestContext.pathMode`. Published resource contexts use descriptor mode,
including action-state requests through their retained invocation context.
Token authentication's sender explicitly uses descriptor mode. Public raw
`AsyncClient.request`, discovery and available-version requests keep API-base
mode. No public `RequestSpec` field, prefix detection, route-dependent retry,
guessed version or alternative endpoint fallback was added. Snapshot and stale-
binding checks remain in their existing owner.

Reviewed descriptor validation and pre-transport behavior: authority switches,
absolute descriptor URLs, userinfo/control/backslash forms are rejected; callback
validation precedes auth-provider credential/header/query access. Async schema
validation uses strict descriptor rules and the request pipeline validates again
before transport. The newly rejected credential-bearing base is consistent with
the destination boundary. Root-mounted URLs remain equivalent. Existing OAuth
relative/absolute URL handling and the exact trusted-origin allowlist stay in
their separate path, and ordinary descriptors do not inherit that exception.

Python changes only its common request owner. The internal resolver default stays
API-relative for base validation/discovery. `build_request` selects origin-root
descriptor mode, validates the static path before binding encoded IDs, and then
constructs the URL from the configured origin plus bound path. Existing facade
`_action_request` still applies `validate_destination` before requesting auth
headers. Same-origin and configured-mount restrictions are preserved; no transport,
state/provider or public raw API was changed. Both sync/async action, token and
operation paths consume the same owner. Encoded slash/space/percent ID data stays
distinct from invalid static traversal/query/fragment/authority input.

Synthetic descriptions were corrected to contain their real mounted paths rather
than changing the server contract. The actual Rack fixture still emits
`/mount/_auth/token/tokens` and
`/mount/v2/parents/{parent_id}/children/{widget_id}`. The server route, resource and
action implementations, Go/Rust code, Python state owner and transport have no
semantic delta in this follow-up. Captured Rack descriptor tests and native client
tests exercise the actual advertised routes, including the authentication challenge.

Documentation and release notes describe the correction and retained raw-request
semantics. Manually fabricated/cached API-relative descriptors under mounted bases
must be refreshed from OPTIONS; there is no ambiguous compatibility mode. New
clients consume the existing server route contract independently of server
deployment. Rollback restores the known old client bug and introduces no stored
state compatibility problem. No protocol, schema or coordinated node deployment
is introduced.

## Native process ownership and diagnostics

The PHP change correctly replaces shell-command `proc_open` with an argument
vector. Bundler exec leaves the Ruby fixture as the native process signaled and
reaped by the existing stop path. Descriptor redirection preserves merged output;
removing pipe-2 setup matches PHP's redirected-pipe behavior. The actual TCP closure
test checks a live listener before stop and its absence afterwards, with an
idempotent finally stop. Inspected original before/after native receipts: the old
tracked shell left its Ruby child/listener alive; the corrected tracked PID is
Ruby, has no child, is reaped, leaves no listener or owned process and needs no
manual cleanup. No PHP production runtime or process-discovery mechanism changed.

Dynamic acceptance now saves subprocess output before exit/completion assertions
and keeps existing-token versus challenge output separate. The fixture trace is
limited to JSON method/path/status; headers, query strings and bodies stay out.
Tests exercise failed execution and a credential-bearing query/body/header without
including those values in the trace. Runtime failures remain failures, and no
fixture route or response was normalized to conceal the mounted-path problem.

## Whole-history, update-stream and migration conclusions

Independently verified the actual merge base, complete 22 commit messages and final
134-path inventory; all new runtime source is committed. `git range-diff` proves
the first 13 hashes are unchanged from `27b4f8f8`; the existing dynamic-renderer,
highlighter and packaging/CI commits remain patch-equivalent. PHP cleanup,
diagnostics, Python correction and JS correction are distinct reviewable purposes.
The final metadata/changelog commit remains last, with the exact requested message.

Independently proved `05bf78563d2eb0fa92a64437977dfde0ff153670` and final head have
the same tree and identical complete binary base-to-head diff. There are no
obsolete unmerged approaches, fixup-only commits, abandoned path modes, transitional
shims or unresolved intermediate implementation revisions in the final series.

Repeated-update conclusion:

- Old helper generation `659ede0f` and intermediate URL generation `5b1dd07c`
  have been consolidated into one cumulative bundle/declaration update
  `71c22cd8`, after both authored features. The final version literal change is
  ordinary shared metadata, not a redundant generated-feature update.
- Shared 0.30 metadata/locks occur once in `ee150c85`; npm test declarations
  occur in their distinct `593fac92` dependency stream. Rust/Python local lock
  entries change only in final metadata, without new registry-resolution changes.
- Highlighter pin/build/license/bundle remains one `8947b16a` stream; PyPA pin
  remains one `1e810107` update. Shared Ruby workflow action-role pins remain in
  `cb41affb`. There is no new URL dependency/channel stream.
- `flake.lock` and the private Rust runtime `Cargo.lock` are unchanged. No
  intermediate pins/payloads need retention for a release/consumer/state boundary;
  prior exact refs and execution receipts correctly remain separate provenance.
- The three supported released maintenance patches still have exact diff
  equivalence to `c305117`, `1973057` and `62cb54e`, with original and release-branch
  cherry-pick provenance retained.

Migration conclusion: **no migrations**. Complete final history contains no
database/schema or persisted-state conversion changes, no transitional migrations,
and no migration merge/release/deployment/external-use lineage to reconcile.

## Independent checks and remaining gates

Reviewer ran known quick checks in the declared top-level tools-only Nix shell:

```sh
node --test clients/js/test/compatibility/mounted_paths.spec.cjs
cd clients/python
uv run --locked pytest -q tests/unit/protocol/test_mounted_urls.py \
  tests/unit/client/test_clients.py tests/integration/test_mounted_description.py
cd ../../servers/ruby
bundle exec rspec spec/client_examples/dynamic_mounted_paths_spec.rb \
  spec/client_examples/dynamic_acceptance_spec.rb
```

Passed: **10 native JavaScript tests; 168 Python tests (3.85 seconds); six Ruby
examples (1.93 seconds)**. Python/Ruby Rack checks use in-memory requests and no
listener. Native tests cover root/mount/trailing slash, discovery, raw query paths,
global/versioned token challenges, renew/revoke/state, encoded IDs, rejected
destinations before credentials and retained OAuth behavior. Whole-range whitespace,
identity, tree equivalence, history/stream and migration checks passed. An ignored
concurrent Nix evaluation-cache busy message did not affect the completed JS test.
Owner broad quick/style/hook and PHP native proof receipts are supporting evidence,
not relabeled reviewer-run checks.

No long build, package/compiler acceptance, new installed wheel/sdist/npm execution,
registry helper, default integration, tag or lifecycle action was run by this
reviewer. Prior successful core/CI/artifact results at `27b4f8f8` do not prove final
runtime acceptance. The actual installed mounted token challenge and ordinary
action must now be retried using exact final artifacts, retaining complete output
and status. Finish remaining Go/Rust documentation acceptance, including selected
Rust development/MSRV execution, according to the lead's existing verification
plan. Preserve failed/prior artifacts and use fresh exact-head CI evidence.

Application tracked source/index stayed clean at exact `ee150c85`. Only this
assigned report was written. Lead owns state reconciliation and subsequent
authorized verification; session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
