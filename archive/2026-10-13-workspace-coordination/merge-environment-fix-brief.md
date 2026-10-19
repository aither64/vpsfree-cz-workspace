The user requested fixing the merge process after the live configuration merge
exposed missing hook dependencies and SSH. Keep preparation outside claims and
the execution section short. Parent owns application edits; Astra owns the
precise recovery design and independently reviews the final fix.

Observed operation: ec09fd84-f48c-4ea6-92fe-a2392f08e7a2, attempt
bb975e20-0b90-42c3-a09a-a6476353823c. The exact approved configuration head was
fast-forwarded locally; push failed because the saved hook PATH omitted SSH.
The saved environment also missed the dev-shell's Bundler bootstrap. Remote
master remains the approved predecessor. Original request, phase, result,
artifacts and claim stay immutable and retained.

Bounded runtime correction: prepare the declared repository shell including its
shellHook, retain only allowed hook variables (no complete environment dump),
check its framework dependencies, and preserve the selected runtime's transport
executables when applying the hook PATH. Hook preparation and transport checks
finish before admission. The worker does no builds or dependency installation.
Old artifact/ledger/worker formats remain readable; no schema migration, machine
ownership change, approval waiver or generic automatic replay is introduced.

Acceptance: a repository shell with a restricted PATH and shellHook-installed
Bundler gems can execute actual Git hooks and SSH from an independent worker;
missing framework dependencies refuse during preparation before any job/claim.
Allowed environment capture excludes secrets. The original hook environment is
restored after success/failure. Existing interrupted-push ownership semantics
remain unchanged. Focused regression tests and the existing coordinator suite
are the relevant checks; source-identical browser and VM checks need no rerun.

Recovery must prove the original owner, approval, request digest, exact retained
target checkout and local/remote heads under worker and Git locks, run required
hooks with the corrected declared environment, perform only the original exact
non-force push, then let ordinary reconciliation settle the original job.
Do not edit the old snapshot/artifact/result, replace the job, release its claim,
activate a package during its uncertain attempt, or replay the local merge.

Workspace shared history remains separately blocked on the exact publication
question for three already committed foreign tracking records. Preserve all
foreign files/index contents. Machine reservation remains deployed_review.

Astra read-only design confirmed the fault and exact retained checkout. The
source-only bin/recover-bootstrap-push-2026-10-14 binds just this job/attempt,
source heads and selected package. It uses the already initialized configuration
shell, original artifact PATH plus selected SSH/declared bundle, actual hooks,
and original worker/Git locks. No runtime package switch is needed for recovery.
The permanent correction initializes and preflights the repository shell before
admission and applies its environment to worktree creation and final hooks.
Quick regressions pass3/14. Runtime formats and old request/result bytes remain
unchanged. Whole-source review is required before external recovery.
