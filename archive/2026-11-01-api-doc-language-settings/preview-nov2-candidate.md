# Reviewed Nov 2 preview candidate

Status: bounded candidate and capability acceptance passed; the lead subsequently
released the final live refresh after exact-head local/hosted checks. See the
[Nov 2 live receipt](preview-nov2-live.md). This file retains candidate evidence.

Source: `ef4c0cdcb349815538bb93cedab9d3964c565998`, tree
`c20bf6110013adad017ef989b9b305b099c2c6ca`. All 933 exported Git blobs match,
with no missing or mismatched files. [Source receipt](preview-nov2-source.json).
The application source was independently reviewed with no findings before these
candidate checks. No uncommitted worktree inputs are loaded.

New loopback service: `haveapi-doc-language-nov2-candidate-20261101.service`,
Ruby PID `1339526`, invocation `9ea3f8d382784e33ab4adb9e480c3657`, started
`2026-11-02 14:07:03 CET`, listening on `127.0.0.1:14568`. Health passed.
Working directory: this session's `preview-source-ef4c0cdc` export.
Log: [preview-nov2-candidate.log](preview-nov2-candidate.log).
[Runtime receipt](preview-nov2-candidate-runtime.json).

Actual Chromium acceptance passed:

- [New refinements](preview-nov2-refinements-candidate.json): JS/no-JS singleton
  whole-label visibility, two→one→two visibility with saved Thorough retained,
  exact one native `example_detail=simple` scalar and query/locale retention;
  Ruby Basic/token/init/action Thorough preamble requires the client once at
  top level before `begin`, setup inside, with localized comments.
- The same refinement receipt separately covers four signed-in Settings renders:
  en/cs × capability false/true. Existing `DocumentationOAuthFixture` rendered
  real app HTML in-process over its HTTPS request contract. Chromium inspected
  local rendered files: Switch user precedes Sign out only with capability;
  POST target, CSRF fields and `switch_user=1` are retained. No logout was
  submitted, no OAuth endpoint/service/proxy added, and no fixture cookie was
  saved outside the in-process renderer. This is capability-fixture DOM evidence,
  separate from ordinary preview/live browser evidence.
- [Retained native checks](preview-nov2-native-candidate.json),
  [UI](preview-nov2-ui-candidate.json),
  [localized comments/code/privacy](preview-nov2-comments-candidate.json), and
  [real generated Go/Rust/TypeScript profiles](preview-nov2-generated-candidate.json)
  all passed. No browser page errors occurred.

The optional style injection into local no-JavaScript account HTML hung; it was
removed as agreed. A bounded rerun passed all accepted DOM/form cases. The first
exporter invocation needed the explicit source Ruby-client load path; that
session helper was corrected. Neither condition was a product failure or required
project source/test changes. The new browser harness has a 55-second bound.

Before the refresh, the live URL was <http://aitherdev.int.vpsfree.cz:4567/v1.0/>, service
`haveapi-doc-language-preview-20261101.service`, PID `139933`, exact 51047.
The older `haveapi-doc-language-candidate-20261101.service`, PID `29112`, remains
on `127.0.0.1:14567`. Neither service was modified during candidate preparation. Current source,
profile preload, launcher and recovery receipts are retained. No dependency
installation, project source/index, host, lifecycle or cleanup operations occurred.
