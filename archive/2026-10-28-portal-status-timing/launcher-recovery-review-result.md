# Packaged launcher recovery review

**No Blocking, Important or Advisory findings.** The shell launcher corrects the
lost packaged runtime environment for both recovery entry points. This review
does not run or approve a restart; actual-input rehearsal and the remaining
operational gates still apply.

## Reviewed correction

Reviewed committed rollout range
`867320a0e581206127a8f46cdeab82504d7cdf31..0560c7569d67d4c1eb507641c43671e69f2630c8`
under the general and risk/compatibility lanes, retaining prior conclusions for
the unchanged adapter, partition and application code. Reviewer remains
`/root/final_review`, gpt-6.1-sol/xhigh. No delegation, source edits or live actions.

The preceding review missed the raw Ruby entry's dependency on the packaged
shell PATH. The recorded second attempt exposed that defect: ambient Python
lacked `jsonschema`. The new correction restores the wrapper environment rather
than bypassing the failed validation. The earlier proof/claim/state-machine
assessment remains valid; its assumption about the complete launch environment
is superseded by this review.

I independently reconstructed the launcher from the exact selected package
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`:

- All of `bin/workspace-host` except its final dispatch is retained, including
  its shell shebang, host mode, extension catalog, activation aliases and
  namespace/router defaults.
- All PATH setup from `libexec/workspace-host` is retained in the same order,
  omitting only its redundant shebang and final dispatch. This includes the
  package's Python environment as well as its other declared tools.
- The final command uses the exact Ruby path from the installed
  `libexec/.workspace-host-wrapped` shebang and passes quoted arguments to the
  adjacent adapter.

That reconstructed text equals the committed `migration-host.sh` byte for byte.
It preserves the tooling of ordinary packaged execution; only the dispatch
target changes. No protocol/schema check is removed or weakened.

The Python runner now invokes the shell launcher when the candidate is already
selected. The adapter's exact nested candidate `_activate` interception likewise
invokes that launcher, preserving its activation environment and the existing
Host state machine. Other subprocess calls remain unchanged. The adapter
additionally permits only the two exact old/new `check-codex --codex PATH`
commands. I inspected the installed check implementation: it generates schemas,
runs the package's Python protocol validator and probes native socket startup
in private disposable home/SQLite/log directories. This adds bounded preflight
access, not a check-skipping or live-service path.

The previously reviewed source-home quiescence restrictions, source-native
identity guards, post-publication private home, claim/transition checks,
journals, inotify/fingerprint admission and exchange recovery are unchanged.

## Evidence, history and remaining gates

The working rollout equals committed `0560c7569`. I independently recomputed all
nine fenced source checksums and checked byte equality with their raw mirrors;
all match. Committed diff whitespace is clean. The supplied completed quick
evidence comprises six adapter cases/21 assertions, sixteen Python partition
fixtures, syntax checks and real old/new native `check-codex` calls through the
new launcher. I did not rerun them. The real launcher checks address the runtime
environment gap that mocked adapter routing alone did not detect.

The new operational range contains one focused correction. No application
feature head, package bytes, consumer pin, schema or migration changed. Earlier
complete branch history and consolidated pin conclusions therefore stand.
There is no repeated dependency-update stream and no new SQL migration. The
executed operational lineage must remain intact: both failed attempts stopped
with the candidate selected, original native still running and no publication
hook, copy or exchange. Preserve their shared-master commits, original config,
source revision, package, claim, journal and append-only switch log; this fix
does not permit starting a replacement operation or rolling the package back.

I read the supplied actual-input rehearsal source as context. It uses read-only
source database connections, copies portal history and partitions databases
under an owned disposable directory, and starts the candidate native against
that copy without copied login/configuration credentials. Its cold-read loop
checks each portal identity/path and that no thread became loaded. It does not
resume a production thread or run the publication hook. Rehearsal results remain
a separate verification gate; this review did not execute it or certify a
successful run. A live-source rehearsal also does not replace the final offline
inventory, writer exclusion and conservation checks.

After successful rehearsal and remaining required checks, any authorized retry
must refresh only the changed private source files with verified hashes and
mode-0700 launcher, then use the exact failed unit and retained operation.
Observe current client/daemon state before retry; do not interrupt reopened stock
clients. Full migration/deployment acceptance and the same-attempt original
message reconciliation remain required. No restart, message, merge, reboot or
backup removal was performed by this reviewer.
