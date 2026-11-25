# KB pin source-check disposition

Architect read-only assessment, 2026-10-31. Exact session verified from its
tracking directory; both environment variables absent, trusted thread binding
matches. No source changes, tests, builds, claims or runtime operations performed.

**Recommendation:** retain the five-file pin-only scope and document the observed
failure as a pre-existing post-stop retained-metadata check defect. Complete the
unexecuted source checks. Do not implement unconditional first-identity retention
to make this check green: a live process can exec without changing PID/start time.

Evidence reviewed: [diagnosis](kb-shared-source-evidence/source-diagnosis.md),
[native summary](kb-shared-source-evidence/native-failure-summary.json),
[targeted result](kb-shared-source-evidence/targeted-check-result.json),
[source packet](kb-shared-source-review-packet.md), and exact owned KB
`tools/test-machine.rb`, `cluster/lib/kb_process.rb`,
`cluster/lib/devcluster_runner.rb`, `bin/check` and repository guidance.

The original failing assertion compares retained child identity arrays after
`shutdown` returned. Native evidence records phase `stopped`, complete process
record, `gone=true`, zero claims, unchanged three listener identities, and only
the stand-in VM Ruby argv changing to empty. The companion unknown-pidfile
negative case records `stopping` and preserves its unknown entry as required.
This is evidence of successful stop with changed diagnostic metadata, not an
observed unsafe signal, namespace deletion or live-process abandonment.

`ProcessIdentity.read` obtains stat, exe and cmdline separately. Runner discovery
overwrites its retained `[pid,start_ticks]` entry from observations even through
the ensure path. A post-stat exit can explain empty cmdline; this remains a
supported race hypothesis rather than deterministic root-cause proof. Dedicated
stdin disproves the proposed PTY cause. Relevant source hashes are unchanged
across base ce2, prior1119 and staged9ffcfb0a. The single unchanged targeted test
passed 1 run/57 assertions; it does not erase original failure (34/1238, one failure).

## Minimal owner3 next batch

At exact staged9ffcfb0a in its pinned `nix develop` environment, execute the
unexecuted `bin/check` suffix from `ruby -c tools/test-node-ssh.rb` through its
final `bin/validate --allow-missing`. Recreate `tests_meta` using the original
`nix eval .#testsMeta.x86_64-linux --json`, set the original validation argument,
and preserve the suffix's fail-fast ordering. Do not edit `bin/check` or weaken
assertions. Use a fresh watcher with complete native stdout/stderr and exit
capture. No re-run of the successful101/1263 and19/150 groups or whole machine
suite is needed just to finish the checks that the failed command skipped.

Record original full batch **FAILED**, targeted diagnostic **PASS**, and suffix
results separately. Lead/reviewer can accept this explicit baseline-failure
exception for mechanical pin scope; do not describe the aggregate as full green.
Exact-final-head strict hosted Check and actual runtime/capture validation remain
their own required evidence. If this defect prevents a required final gate, a
separate bounded baseline correction needs deterministic partial-exit observation
coverage plus retained/live-exec, changed identity, reused/foreign PID and unknown
namespace refusal controls, and independent review before affected long checks.
The current evidence does not justify changing process authority semantics now.
