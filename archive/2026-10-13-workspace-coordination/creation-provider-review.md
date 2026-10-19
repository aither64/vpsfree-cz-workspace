# Independent final provider-enabled creation review

No Blocking, Important or Advisory findings in the final reviewed change.
The previous Advisory portal-guide finding is resolved.

Reviewer: retained independent `/root/coordination_confctl_review`, GPT-6
Astra/xhigh under the original assignment. No model/effort override, nested
agent, application edit, live session mutation or deployment was performed.
This evidence report is the only reviewer-written file for this follow-up.

All four mandatory lanes were assessed: general, architecture/repetition,
scope/proportionality, and risk/compatibility. The review used the packet,
`creation-provider-runner-fix.md`, complete final inventory, final patches,
range-diffs, prior reviewed heads, applicable repository/workspace instructions,
mandatory-change-review skill and lane guidance. Unchanged prior conclusions
remain applicable; the provider correction and subsequent narrow changes were
inspected directly.

## Correctness and boundaries

`DevSession::Runner#initialize` retains `@command_runner`; it never initializes
the erroneous `@runner` used by `native_provider_arguments`. The correction at
`libexec/dev-session:8677` uses that retained command runner and unpacks stdout
from its `[stdout, stderr, status]` result. CommandRunner continues to reject an
unsuccessful child before JSON interpretation.

The existing provider executable, workspace selection, environment and argv
validation are preserved. The helper still accepts only the expected JSON argv
shape and `-c` pairs; terminal dispatch still shell-escapes every argument and
appends the exact retained socket/thread. Provider selection and generation/
admission checks remain owned by `workspace-host`. No fallback runner, duplicate
provider selection, new authority or recovery path was added.

The new public creation regression uses the real CommandRunner and actual
terminal-reconciliation method. It verifies quoted native arguments, one terminal
dispatch, the retained thread/socket, ready creation state and one initial
request. The invalid-argument regression refuses before terminal dispatch.
The existing disconnected-client test preserves ordinary terminal recovery.
These checks cover the reported regression without replacing the method under
test with a stub.

The change is proportional: one production-line correction plus focused
regressions for an existing supported path. Provider/session documentation already
describes the intended behavior, so no additional lasting prose is needed.
The earlier portal-guide correction now accurately names single/count badges
and links Reservations. The intervening asynchronous tab-activation listener,
cache-version updates and timing-library fixture wiring were also inspected;
they preserve the earlier accepted behavior and are folded into their owning
commits.

## Exact history and consolidation

These complete feature series were independently verified against Git, along
with their saved final patches and clean worktrees:

| Repository | Base | Complete final feature series |
| --- | --- | --- |
| dev-workspace | `fea04c6de25448751239099eca7101c43cb495c2` | `2727495fc43228d8fff9c214c1fd79ff7709019d` → `0264c6b4564397ee0e750808ed2b795ac8b6af51` → `ef4ec58d1838ed01706c0e85e306117821a0a114` → `a10af6c4539c4c7a6a97a883d89825346d5451ad` |
| vpsfree-dev-workspace | `505ffc457b3329af0b124075f417953c9cc42edd` | `01faecf62e57e15ef756243adb8a657c279f2d10` → `c697acc70b05c9bc6cf7bf53fe63700f1f6c1276` |
| workspace | `90005ea3a7a170b23699c38933b111b046ce43f8` | `4ae8cea78f59952cf7e3a3c54109ab2adfa3e7d8` → `2c21246627a5cd9751d19f0f19c101c859c569c3` |
| vpsfree-cz-configuration | `0e394507395c04a6c11fd6d25c8284621061c140` | `787137d4fe2a7c8d5baf142b113265e1b4675de5` → `fbbda8e90f44270eadc38c482b2f33a743e6252c` |

No obsolete approaches or redundant intermediate pin updates remain in these
series. The provider correction is an appropriate separate fourth runtime
commit: Git blame attributes the original defect to upstream `5421e563`, and
that commit is an ancestor of this initiative's base. The fix must not rewrite
that pre-existing history or be disguised as a coordination implementation fixup.

Each consumer retains one final runtime-selection commit. Workspace routing and
configuration documentation remain separate logical commits. Configuration's
generated changelog covers the original `7c07b540` selection through `a10af6c4`,
including the correction. Only the intended `dev-workspace` and `devWorkspace`
lock nodes change from the preceding deployed consumers. The extension remains
`c697acc7`; its selected source and sibling inputs are preserved. The recorded
final composition check confirms the common `a10af6c4` runtime selection.

Deployed workspace/configuration predecessors remain in both local and
remote-tracking `2026-10-13-workspace-coordination-operations-tab-deployed` refs
at `90d9e110` and `af938a39`. Runtime predecessor `ef4ec58d` remains an ancestor
of the final head. This preserves exact deployment provenance separately from
the consolidated active pin streams.

**No migrations.** The correction changes no authority, ledger, timing,
manifest, provider state, journal, worker-envelope or receipt format. Old and new
packages read the same persisted state; the predecessor still has the startup
bug. No transitional migrations or obsolete compatibility paths remain. The
earlier deployed coordination formats and retained recovery evidence continue
to be supported.

## Verification and remaining work

Independent checks in the runtime Nix environment passed:

- `ruby test/dev_session_test.rb -n
  '/test_creation_launches_terminal_with_configured_provider_arguments|test_terminal_provider_arguments_are_validated_before_dispatch|test_attach_restarts_terminal_client_after_app_server_disconnect/'`:
  3 tests, 24 assertions, no failures or errors.
- `node --test portal/internal/web/coordination_browser_test.cjs`: 10/10 passed,
  including asynchronous Reservations-tab activation and incarnation guards.
- Complete final `git diff --check` in all four repositories: passed.

The saved deployed reproduction fails at the reported nil runner. The first
implementation-test failure was separately explained by a fixture exposing tmux
before tracking existed; the corrected fixture exposes it at creation and passes.
There is no unexplained rerun. Nix emitted an ignored concurrent SQLite-cache
message while preparing focused checks; the tests completed successfully.

Remaining verification is the corrected packaged session/provider path, exact
composed package/system selection, and successful fix deployment under the
existing reservation. The focused fixture substitutes the host provider command,
tmux and portal transport; it proves the caller's real capture/reconciliation
logic, not a live native session against the selected installed provider.
No duplicate live conversation or mutation of the user's failed session was
used as a test.

No review finding prevents the planned longer verification. Merge approval
remains conditional on successful fix deployment. Before integration, the lead
must establish the supported coordinated route for the retained threadless
bootstrap owner and repeat the required final-head checks. This report does not
supply that route, prove deployment success, or authorize reservation release,
reboot or session closure.
