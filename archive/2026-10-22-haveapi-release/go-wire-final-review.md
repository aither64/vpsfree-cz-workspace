# Go request-envelope assertions: final independent review

**No new Blocking, Important or Advisory findings.** General, architecture/
repetition and scope/proportionality lanes pass for this committed correction.
Final Go executable acceptance, final artifacts and final-head CI remain separate
verification work. Earlier failed executions retain their actual result.

## Identity and reviewed range

- Session: `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Retained independent reviewer: `reviewer0`, purpose `review`, thread
  `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Same-session live roster revision 34 confirms ready state and retained
  `gpt-6.1-sol` / `xhigh` / `read_only`. No model/effort override, fallback,
  nested agent or substantive authorship. `dev-session current` from the session
  directory printed the bound slug; both identity environment variables were
  absent. The workspace-root invocation has no current session; resolution was
  completed in the intended session directory before session files were read.
- Repository: `vpsfreecz/haveapi`, target `master`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Complete reviewed range: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  **`ee67d27419c48d27a01c83a29114adf9a82062ba`**, tree
  **`2e0d29769aff48b484c1ac331b11255d22abd0ae`**.
- Prior reviewed/executed head: `3fb91caf783eaeacf49bf3647b8409d536339d71`,
  tree `8698b4a7b707b2c165877931071d31505f346370`. The earlier
  [Go VCS review](go-vcs-final-review.md), [Python login review](api-doc-python-login-final-review.md)
  and [URL/runtime review](api-doc-url-final-review.md) remain preserved.

Read mandatory-change-review in full, Shared Reviewer Instructions, all three
selected references, applicable workspace procedures and HaveAPI development/
release guidance. Inspected the packet, source receipts, real fixture/template/
verifier, final messages and per-commit paths, complete-diff export, range mapping
and execution/input evidence. Unaffected substantive review conclusions are
retained through independently reconstructed exact equality, rather than a new
claim to have rerun those lanes. The overall release remains high risk; this
two-file test-assertion delta is low risk and changes no product risk contract.

## Affected-lane conclusions

**General — correct established wire expectation; strictness preserved.**
In Go owner `277c931a`, `clients/go/spec/documentation_acceptance.rb:19` now
shares its existing 16-case expectation table with the pure checker. Only
`object`, `hostile` and the three composed authenticated calls expect `_meta: {}`.
Those cases all invoke the same action and sample (`:148`–`:177`). Explicit
empty and omitted input use separate metadata-free actions and retain exactly
`{"widget":{}}`.

The expectation is independently supported by the actual fixture
`clients/go/spec/support/documentation_fixture.rb:43` and existing SDK code:
`action.go.erb:183` includes the global metadata field without `omitempty`,
`:604` assigns `makeMetaInputParams`, and `:640` returns a nonnil empty map when
metadata is not supplied. `go_client/utils.rb:121` adds no omission tag, and
`request.go.erb:224` marshals the complete request. The retained actual object
capture at `go-final-verification.log:123` matches the new expectation, including
null, false, zero and omission of `unused`.

The actual private verifier at `documentation_acceptance.rb:213` is byte-unchanged.
It still compares the entire parsed body with the exact case expectation at
`:223`; no metadata stripping, normalization or subset comparison was added.
Mounted paths, authentication, query, output, state follow-up and extra-request
checks remain intact. Authenticated action cases gain the same exact body check
while preserving their existing authentication expectations.

**Architecture/repetition — one expectation owner and the actual verifier.**
`clients/go/spec/documentation_wire_check.rb:38` allocates the real harness,
feeds its request queue and calls its real private verifier. It never constructs
the server or invokes generation, compilation or execution. Positive object
bodies are literal captured JSON, separate from the expected table; hostile and
metadata-free cases also have explicit inputs. Every mutation uses a deep copy.
The negative helper only accepts the actual body-mismatch exception prefix;
success or an unrelated failure cannot satisfy a negative control. Sharing this
small table avoids divergent expected-body rules without creating a new product
interface or adding optional generator dependencies to ordinary server bundles.

**Scope/proportionality — bounded correction.**
The two-file delta corrects an observed assertion mismatch and strengthens three
existing authenticated cases. It adds no SDK/renderer/runtime behavior, fixture
schema or route changes, new request key, fallback or metadata capability.
Seven positive cases and 52 mutations directly exercise the owned equality
boundary. The short owning comment explains the empty envelope; additional
product documentation would not explain a changed product behavior.

## Complete history, update streams and migrations

Independently reconstructed all 22 final commit positions from the stated merge
base. All commit messages match the predecessor series; the first ten commit
hashes are exact. **Twenty-one patches have equal raw diffs and stable patch IDs;
only Go owner position 11 changes (`cb21d5ce` → `277c931a`).** The entire old-to-new
semantic delta is the two reviewed paths. The full 137-path base-to-head diff
export matches Git exactly. Prefold `ea6d33a902449ec453f0f6536f4e670c91df9151`
and final have identical trees and complete binary base-to-head diffs. Whitespace
checks pass. Last commit has exactly the one-line message `Version 0.30.0`.

The correction is folded into its owning Go purpose. No fixup-only commit,
obsolete unmerged design, transitional workaround or abandoned compatibility
path remains. Other source, generated, diagnostic/cleanup and version purposes
remain independently reviewable. The three released maintenance patches retain
their `-x` provenance and independently match their referenced released-source
stable patch IDs (`9b53aa87`, `fda2e33d`, `f82ca890`).

Repeated-stream conclusion: **no new dependency, channel, lock, generated payload
or version stream**, and no redundant retained update. One cumulative JS bundle/
declaration commit `7cf39c5e` follows both authored JS features. Final shared
version metadata remains separate in `ee67d274`; its second browser-bundle touch
changes only the version literal. Node test types (`593fac92`) and final package
identity touch the same lockfile for distinct purposes. Highlighter pin/build/
license/bundle, PyPA publishing action, shared CI action-role and Rust release
source streams retain one final update per logical purpose. No intermediate pin
needs a release/consumer/state-boundary retention exception. Original reviewed
refs and execution records remain provenance rather than redundant branch steps.

Migration conclusion: **no migrations**. The entire final series/diff contains no
database schema migration, persisted-format conversion or transitional migration.
There is no migration merge/release/deployment/external-consumption lineage to
reconcile, and this assertion-only delta introduces none.

## Verification, input equivalence and remaining gaps

Reviewer independently ran the known quick pure checker in the declared root
tools-only Nix environment and explicit dedicated documentation bundle:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euc '
  export BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile"
  bundle exec ruby clients/go/spec/documentation_wire_check.rb
'
```

Exit 0: **7 accepted bodies, 52 rejected mutations**. Controls reject nonempty,
null or missing metadata, extra body/input keys, altered false/zero/null, missing
supplied fields, and accidental metadata or missing input namespace on
metadata-free cases. Owner syntax/style and commit hooks remain supporting
evidence, not reviewer-run checks. No compiler, listener, package build/install
or long acceptance was run by the reviewer.

Independently reconstructed both complete tracked trees: **749 predecessor
entries → 750 final entries, 748 exact mode/type/blob identities unchanged**.
Only the existing Go harness blob and new checker differ. Every row of the
baseline and final comparison inventory matches Git. All server, JavaScript,
Python, Rust, Ruby-client, release/workflow and toolchain inputs are unchanged.
The original artifact manifest SHA-256
`5f88d02da7d46395a3db53f7d508b7a1caec413d3fe23f65b3d396ac9b013859`
and source `3fb91caf` match; original tool metadata matches the inventory.
Independently derived all **nine** lock-content hashes from that actual manifest
and compared them with the live files: all equal.

The separate original Rust inventory SHA-256
`538c6330ad3647cf30b1ee2134e5e2594c91701419ae02b4f1b456086a3007f4`
matches. All **310** original mode/type/blob entries match both actual execution
head `48543f8cd254eb0fc087931a5dc98ea730fd94af` and final; `flake.nix` and
`flake.lock` separately match as well. Original generated Cargo/source/lock/tool
graphs remain retained with the successful Rust result at that actual head.

The prior `3fb91caf` batch remains **exit 1 after 196.15 seconds**. Its control flow
and log establish artifact build/verification and both installed dynamic runs
passed, and all 16 Go programs compiled before the first object assertion failed.
Wheel and sdist results each record 36 panels across six variants; CI records
remain bound to `3fb91caf`. Rust success remains the actual `48543f8c` run
(915.38 seconds, root/mounted, async/blocking, development/MSRV). Exact unchanged
inputs support retaining those results; none is literal execution at `ee67d274`.

**Remaining gate:** rebuild/verify final-head artifacts, complete the actual Go
rendered-program run, and obtain final-head CI as selected by lead. Pure verifier
controls do not establish network/authentication/state execution or success for
previously unreached cases. No new successful Go acceptance is claimed.

Final recheck confirmed exact head/tree, tracked source and index clean, and
empty `dist/`. Existing unrelated untracked PHP/Python caches were untouched.
Only this assigned report was written; no source/Git/default/tag/registry/
deployment/lifecycle mutation occurred. Lead owns state reconciliation and the
next verification run; the session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
