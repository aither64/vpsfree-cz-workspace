# Risk and compatibility review

Reviewed the committed packet heads and commit series, repository guidance, consumer pin chain, installed profile, lifecycle recovery paths, public CLI/API contracts, private sidecar state, and timer deployment. The change is **high risk** because it can archive or abandon sessions and changes profile activation and rollback behavior. This report covers `dev-workspace` `df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933..ef1fa85451ee98f9d0a1d167d586ea2765b67cf7`, `vpsfree-dev-workspace` `89a03581b13056fa83114e592f2e2993e6a87887..bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce`, and workspace commits `bba4a38` and `89f8efe2f7171b2a0b388e0349c24121da0ceef6`. Concurrent remediation after those heads is outside this review.

## Findings

### Blocking — failed observations continue aging a candidate toward a destructive action

- **Severity:** Blocking
- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File/lines:** `libexec/workspace-auto-archive.rb:241-249` (with the destructive eligibility calculation at `:92-112` and activity observation at `:339-358`)

When snapshot construction fails before producing a fingerprint, for example because the conversation activity command is unavailable, malformed, or times out, the rescue path records a blocker but preserves the previous `idle_since` and `fingerprint`. The first healthy scan can therefore find the old fingerprint unchanged and archive immediately, counting the unknown-observation interval as proven idle time. This conflicts with the stated invariant that a failed idle check never ages a candidate and weakens the fail-closed boundary immediately before a destructive operation. Mark the persisted observation for a fresh grace period after every such failure, while preserving a journaled operation's existing recovery semantics.

### Important — persistent hold and result state is keyed by a reusable slug rather than the current session identity

- **Severity:** Important
- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File/lines:** `libexec/workspace-auto-archive.rb:71-78`, `:92-113`, `:133-156`

The store is scoped to the workspace, but each session record is retrieved only by slug. `Policy.observe` compares conversation identity for timing while copying the old record wholesale, including `hold`, result, and archive fields. More directly, `hold`, `release`, and `status` never compare the sidecar identity with the current manifest. After an explicit delete followed by creation of a different session with the same slug, the new session inherits the old session's persistent Keep open setting and can expose its stale result/status until later observations. This violates the packet's identity-binding contract and makes a public persistent control apply to the wrong lifecycle object. Bind control and result fields to the current conversation identity, and discard identity-specific state when a slug is reused; keep operation receipt handling subject to its existing journal checks.

### Important — a successful JSON scan can emit command output before the JSON document

- **Severity:** Important
- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File/lines:** `libexec/workspace-auto-archive.rb:170-203`; `libexec/dev-session:223-266`, `:5913-5920`, `:7594-7642`

The scanner redirects the runner's `@out` to stderr, but `DevSession::CommandRunner` captured its own output stream when the runner was constructed. A real successful archive calls `CommandRunner#run` for the tracking commit, and Git's commit summary is written to stdout before `run_auto_archive` writes the JSON result. Consequently, `dev-session auto-archive scan --json` is not a single valid JSON document precisely when it archives a session. Redirect command-runner output for the complete scan or otherwise reserve stdout for the declared JSON contract, and exercise the JSON option through a real archive rather than only a waiting/deferred scan.

### Important — first deployment can leave the new timers active after candidate activation fails

- **Severity:** Important
- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File/lines:** `libexec/workspace-host:559-582`, `:593-604`, `:723-811`

The actual installed profile predates this feature, so the first switch is initiated by a host implementation that does not know how to remove these timers. Candidate `_activate` calls `install_links`, which links and enables the timers, before later fallible user-service configuration and Codex reconciliation. If a later step fails, or `systemctl enable --now` changes some unit state and then raises, control returns to the predecessor's compensation code. That predecessor cannot stop the workers, disable the timers, or remove the newly managed links. Generation checks limit what a stale worker can do after rollback, but rollback still leaves enabled or loaded units and dangling links that can repeatedly fail. Candidate activation needs its own cleanup for partially installed timer state, and timer enablement should be the final activation step after other fallible reconciliation. Cover the old-initiator/new-candidate boundary and partial `systemctl` success.

### Important — timer-stop failure bypasses terminal and timer recovery during rollback and unregister

- **Severity:** Important
- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File/lines:** `libexec/workspace-host:467-525`, especially `:477-482`; `:612-664`, especially `:628-630`; timer stop at `:782-793`

Both unregister and rollback quiesce terminal clients and then call `stop_auto_archive_services` before entering their recovery `begin` blocks. If disabling a timer or stopping a worker fails, the method exits without restoring the quiesced clients. A partial stop can also leave timer state changed without an attempt to restore it. This breaks the existing remote-client continuity guarantee even though no registry or profile transition has begun. Include timer shutdown in the same recovery scope as the rest of each transition, and record recovery errors while restoring both the timer and quiesced clients.

## Compatibility and residual validation

The generic runtime remains the archive authority; private schema-1 sidecars do not change the existing session manifest or archive-journal schemas, so predecessor packages ignore them. The operation receipt, archive journal ownership, exact merged-head proofs, exclusive transition lock, exact portal target/origin checks, and host-generation validation preserve the principal session-integrity and concurrency boundaries. I found no database, node, daemon, or cross-tenant protocol change and no new secret exposure within the trusted-local-operator boundary.

The consumer order is exact and appropriate: generic runtime, then the organization extension pin, then the workspace package pin and user-profile switch. Because the installed consumer is a predecessor without timer support, packaged validation must exercise that exact old-to-new activation failure boundary as well as successful activation, rollback to the predecessor, restart/persistence behavior, a real JSON-producing archive, same-slug delete/recreate, and activity-service outage recovery. Long packaged and live checks were not part of the reviewed quick-verification evidence.
