# P3 Discourse log-protection quick-check handoff

2026-10-30, implementer3. Product source writer is released to implementer1.
This retrospective pointer records already-observed output; no check was rerun
to prepare it. Original P3 quick output and intermediate failures were retained
in tool history, not separate raw log files. The excerpts below are summaries,
not newly generated execution receipts.

## Source and existing evidence

- Worktree: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration-oauth-clients`,
  starting HEAD `249f2eb5896b0a2697ed94e44657294847b3e606`.
- Only owned package files: `default.nix`, `plugin.rb`,
  `lib/oauth_log_protection.rb`, `patches/discourse-oauth-logging.patch`,
  `tests/source_fixture.rb`, all under `packages/discourse-oauth-log-protection/`.
- E1's existing [functional-source-hashes.json](functional-source-hashes.json)
  contains all five exact SHA256 values, matching E3's final source-hash output
  (tool chunk `046d60`). No product-file read/check was repeated for this handoff.
- E1's [functional-assembly.log](functional-assembly.log) and
  [functional-commit-results.json](functional-commit-results.json) are assembly
  evidence owned by E1, separate from the P3 quick results below.
- Exact inspected source provenance, including the rejected tag archive, remains
  in the [plan](../oauth-client-log-protection-plan.md#read-only-source-provenance-and-limits).
  Accepted Discourse source is `oauth-log-source-inspection/discourse-pinned/`,
  recursive hash `sha256-j3JjLYNcv3lluoCekyUUKMfkSX/ExeDsa8zrQ+pDrwg=`.
  Logster source is `oauth-log-source-inspection/logster/`, version 2.21.0;
  its gem SHA256 is `5edc71ea98d5f89fe081556893f77b7c4d2617341dae7d421fc37539cfb13a02`.

## Final observed quick results

| Check | Retained result / tool-history reference |
| --- | --- |
| Focused source fixture | `PASS 73 focused source-fixture assertions; actual logger outputs, pinned patch, unchanged inputs` (`046d60`; also `dadb98`) |
| Ruby syntax, plugin/library/fixture | Three `Syntax OK` results (`4a31ce`, later `986370`) |
| Scoped RuboCop, cache disabled | `3 files inspected, no offenses detected`, exit 0 (`2de54d`) |
| Nix parsing | `nix-instantiate --parse .../default.nix`, exit 0 (`4a31ce`) |
| Lightweight Nix interface evaluation | Returned name `discourse-oauth-log-protection` and expected package source path (`986370`); this used a small `mkDiscoursePlugin` stand-in, not a package build |
| Final source/addition whitespace | PASS (`046d60`), preserving standard unified-patch blank context markers |

Commands used the declared-shell Ruby
`/nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9/bin/ruby`.
From the worktree, the fixture invocation was:

```sh
ruby packages/discourse-oauth-log-protection/tests/source_fixture.rb \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/oauth-log-source-inspection/discourse-pinned \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/oauth-log-source-inspection/logster
```

The fixture applies the patch to stdout with fuzz 0, compiles all four patched
upstream Ruby files, and leaves inspection sources unchanged. The native
unprotected Logster control intentionally demonstrates sentinel params/URI in
output before plugin activation. Protected ordinary/exception/Logstash/chained,
provider error/timeout/HTTP rejection, debug-enabled and both rate-limit paths
then exclude the public sentinels. Success/failure responses, redirects and
original auth inputs are checked; benign unrelated diagnostics remain.

## Retained intermediate failures and corrections

| Earlier observation | Diagnosis / disposition |
| --- | --- |
| First fixture stopped at `/auth/failure: logging URI has no query` | Actual helper chose callback Referer ahead of failure path. Fixed field priority: request path/URI before Referer; final assertions retain this regression. Prior-context tool output was not saved separately. |
| Rails version fixture `TypeError` (`4a0863`) | Fixture used a Struct for the `Rails::VERSION` module. Corrected stand-in; no product workaround. |
| `Integer#minute` missing (`d3a02f`) | Native rate-limit method reached an absent ActiveSupport fixture helper. Added the narrow helper; rate-limit code unchanged except approved URI arguments. |
| Scoped lint initially failed (`bf245e`; correction output `ad934a`) | Resolved filenames/style/fixture-specific findings within the package. Final clean result is `2de54d`. |
| Outer command exited 1 after successful Nix interface/syntax output (`986370`) | An overstrict whitespace script treated standard blank patch context markers as source whitespace. Corrected check distinguished patch context from added lines; final check passed (`046d60`). Patch context was preserved. |

## Scope and remaining verification

Real pinned implementations exercised: Logster Message, Logger and
DebugExceptions, DiscourseLogstashLogger, and the four patched owning source
files. Rails/Rack/provider/Redis dependencies are isolated stand-ins; output
uses native sink implementations with StringIO/JSON capture. Activation before
fixture initializer callbacks is tested and actual startup ordering is
source-backed. This is not full installed Rails boot or real OmniAuth
state/CSRF/GitHub acceptance. Those flows, complete boot ordering and effective
plugin/patch package selection remain for the released post-review installed
synthetic fixture. No production/log-history absence claim follows.

E3 performed no Git/index/ref/hooks/shared-configuration/deployment writes.
E1 owns formatting/hooks/commits; lead owns final review coordination and
operational prose. No migrations or credentials were changed. Full source
handoff report: `c6cd7f6d-23b6-47fb-a732-79867c68fc2b`; E1 handoff:
`9d4dec82-6802-4e54-aa55-5b8c1e38051f`.
