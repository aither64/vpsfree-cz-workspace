# HaveAPI README and release verification: final review

## Request and acceptance

User requested updated project documentation for JavaScript and TypeScript
clients and an audit of the release process. One haveapi-client npm package
ships JavaScript UMD and declarations, with callback and async APIs. Acceptance:
accurate README examples; consistent version/lock metadata; installed-artifact
runtime/type checks; normal hooks and focused quick tests; independent review
before real retained-tar verification. No version release is requested.

Session: 2026-10-19-haveapi-async-client.
Workspace: /home/aither/workspace/ai/vpsfree.cz.
Worktree: worktrees/2026-10-19-haveapi-async-client/haveapi.
Branch: 2026-10-19-haveapi-async-client.
Brief: design.md, README/release-check section; plan.md and state.md.
Complete base: c58704a08451a231fdf6c6123437133422af46dc.
Immediate task base: f94e65e35166a0bf8048a27c9d57c7d36957d65b.
Final head/tree and full series: recorded in the final committed identity below.

## Deliverable and rationale

The existing TS source version path, gulp compilation, declaration emission and
npm files list already support the distribution. The audit found three gaps:
make version missed the two npm lock root versions; release-deps npm install
could dirty the tracked lock; artifact smoke only loaded Client through checkout
NODE_PATH and did not prove AsyncClient or shipped types.

Owner0's 3a79c8ec0863de22823ab5f2031a6e845f612afb changes Makefile,
utils/release/artifacts.rb, utils/release/npm-consumer.ts and the existing release
RSpec. It updates only lock root versions during an actual future version bump,
uses npm ci for JS build dependencies, checks exact packed entries/docs/license,
and installs the retained tar normally into a temporary consumer. CJS checks
package-name resolution, alias identity, version and both constructors. The
existing pinned compiler checks a package-name TS consumer and confines resolved
declarations to the installed package, consumer and compiler standard libraries.
Negative fixtures exercise missing transitive and outside declarations.

Owner1 updates README.md, clients/js/README.md and
doc/agent-instructions/releases.md. Main accepted the exact final prose and
CommonJS example after reading code. It describes one package, both client APIs,
shipped JS/types, callback-only setup and the actual release checks. Documentation
and code are separate reviewable commits; neither changes client runtime.

## History, dependencies, consumers and migrations

Inspect the complete base-to-final series and final diff, not just the new pair.
Prior six provider commits were independently accepted by this same reviewer;
see webui-replacement/final-review.json and owner0's earlier HaveAPI inventory.
The series has callback fixtures/migration, async implementation, guidance,
callback naming and recursive wire-error compatibility, followed by the release
checks and documentation. No obsolete alternate implementation is intentionally
retained. Assess this conclusion independently.

No new dependency/pin/version/generated-output stream is introduced by this task.
Provider lock/toolchain adoption and generated stages retain their earlier
substantive source boundaries; inspect their disposition in the complete series.
NO MIGRATIONS: no database, persisted-session, on-disk or protocol state changes,
merged/released/deployed or externally consumed migration stages. Existing wire
and client runtime remain unchanged from f94. Software rollback restores prior
release helpers/docs; no coordinated backend or WebUI upgrade is needed.

HaveAPI owns the public package and release checks; normal CJS/TypeScript
consumers and browser UMD consumers are the affected contracts. Representative
WebUI replacement uses its exact f94 archive; that source remains published and
the archive is unchanged. This task does not repin WebUI. WebUI source/history
consolidation approval is a separate held work item; no inspection/mutation of
foreign rollout sessions is needed.

## Verification and limits

Normal top-level Nix quicks: Ruby syntax PASS; scoped RuboCop 2 files/no offenses;
make release-test 49 examples/0 failures in 8.6s; make release-check validates
0.29.0; whitespace PASS. Disposable make-version regression proves both roots
and nested dependency-byte preservation, without bumping the real version.
Normal precommit HaveapiI18n/RuboCop and commit-msg passed. Nonblocking >72-column
warnings (all <=80) and ambient Ruby extension warnings are retained honestly.
Owner receipt: readme-release/owner0/inventory.md and code.diff; raw logs under
/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/release-update/.
Docs: 20 local Markdown links and whitespace pass.

Real npm install is stubbed in focused fixtures; actual pinned TypeScript runs.
A real final-source pack/install/runtime/type smoke remains AFTER review, through
one fresh utility watcher. No full Ruby/WebUI/multilanguage release rerun is
planned for this bounded correction. No actual version bump, npm publication,
tag, manual workflow dispatch, default merge, deployment or lifecycle action.
Publisher/workflow/approval/artifact reuse contracts are unchanged.

## Independent assignment

HIGH risk: public package/release compatibility at a cross-language boundary.
All four lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Retained reviewer0, saved gpt-6.1-sol/xhigh/read_only; no model
or effort override, fallback or nested reviewers. Read mandatory-change-review
SKILL.md and all four lane references, workspace applicable routes and repository
AGENTS/procedures. Report severity/lane/file/commit findings, full-history and
repeated-stream conclusions, explicit migration conclusion and residual gates.
This is final committed-deliverable review, not integration/publication approval.

## Final committed identity (lead verified)

Head 349aacd53790c6c820fe2dacc8cb6d151c92d0fc.
Tree c80eaddb6e42633d154c15b020e4e74b9faa8d76.
Working tree and index clean. Complete base-to-head whitespace check passes.
Eight-commit series: 991101f2, 0d2111e5, 8f8e5766, f3fcd33f, 19c20c90,
f94e65e3, 3a79c8ec, 349aacd5. Exact full IDs and final diff are retained in
readme-release/owner1-committed/{full-eight-series.txt,full-final.diff}.
Immediate task range f94..349: 7 paths, 285 additions/25 deletions.
Docs commit normal hooks passed, Jakub author/committer, exact three paths;
see owner1-committed/{inventory.md,receipt.json}. Client source/dist, package
manifest/lock, VERSION, workflow and publisher remain equal to f94.

## Subsequent user-requested overview correction

The root paragraph was removed after the review, leaving only the client-list
bullet. New final head40365b47a1a0c946367bc4596db6060853b52c0a/tree
3fe6010640cf64a063731fe8c49eb5819ca94b59, parent3a79 unchanged. Lead verified
exact old349-to-final deletion, clean tree and unchanged code/client guide/
release guide. See final-review.md and owner1-overview-correction. This packet's
reviewed349 identity remains historical; final403 acceptance includes the narrow
scope reduction under skill steps9-10. Actual smoke is bound to final403.
