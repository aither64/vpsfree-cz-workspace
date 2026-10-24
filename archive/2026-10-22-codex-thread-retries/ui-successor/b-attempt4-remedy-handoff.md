B e7ccc364 is published and frozen for composer-only capture5. Only
portal/internal/web/composer_handoff_browser_test.cjs differs from e1. Every
attachment selection now waits for the actual attachment toggle to enable,
including after reload. Exact filename/Ready, zero-dispatch, draft, original
identity and receipt/ack assertions remain. Bounded upload request/readiness
state is retained on failure. Original capture4 evidence remains unchanged.

The omitted readiness fence is source-proven. Capture4 did not record upload
intervals, so its empirical root cause remains unproved. No product correction
or increased timeout was introduced. Product/config/docs/pins and passing retry
and required-keyboard fixtures are byte-identical to e1. Their actual passing
results remain scoped to e1/capture4, rather than claimed as a new e7 run.

Syntax and Go fixture compile passed (0.046s) in the declared Nix shell. The
checked preconsolidation tree exactly matches final tree
72ee1924492404722c731694ffeec44def7aba2c. Full 10-commit series, range-diffs,
566 exact materialized source blobs/modes, NAR, bundles and SSH proof are bound
in b-attempt4-remedy-final.json. The first eight commits are unchanged; the
remedy is folded into the owning composer commit. No migrations or pin changes.

Lead accepted the exact one-file delta under review step9. Next verification
is one fresh lead-owned watcher using:

    bash ui-successor/capture-attempt-5.sh

Run from this session tracking directory. Guard: exact e7 plus clean worktree;
composer_handoff_browser_test.cjs only, Go timeout360s. capture-command.py owns
the subprocess and its unique stdout/stderr/result/screenshots. Script hashes
are in capture-attempt-5-prepared.json. Owner did not run any browser, native,
build, live send or lifecycle operation and has no active process. Lead owns
the watcher and subsequent terminal close-icon package; source/pin stays frozen
through this capture. No capture5 result is asserted in this packet.

CI one-shot snapshot: current40024500854 and superseded40022639730 in progress;
no poll/wait or repeated cancellation after retained HTTP403. Separate9f CI
failure diagnosis remains lead-owned. No deployment/integration performed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
