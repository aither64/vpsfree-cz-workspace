# Disposable 10-to-50 preparation reader experiment

Prepared for post-review verification. This artifact has not been executed or
compiled by implementer0. No source repository file or commit was changed.

The prior reader is fixed at dev-workspace
`6a972b9ab01077611b2c60e0fc726c185e050315`. This is the preceding ten-attachment
preparation reader, unlike the existing `924c0ec...` fixture baseline that
predates preparation. The current committed revision at preparation time is
`3edc605d81a30a4d49560426e0128b388b856493`; supply the actual independently
reviewed final revision if it changes.

After independent review, the lead's fresh utility watcher runs this exact
command in the caller's pinned repository Go/Node/GCC environment:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/older-reader-experiment/run.sh 3edc605d81a30a4d49560426e0128b388b856493
```

The script itself performs no Nix invocation or packaged runtime build,
dependency replacement, checkout, installed package switch, live Codex call or
deployment. Go compiles
the two disposable archived test packages using each revision's unchanged
`go.mod`/`go.sum`. Module fetching may be needed if the caller's cache lacks
their exact dependencies. Network/toolchain failures are failed evidence, not
permission to change pins or the runtime. The watcher must not diagnose or
retry on its own; return any failure to the lead.

## Fixture phases

1. Archive only `portal/` at the exact current and prior commits under a fresh
   private `/tmp/upload-reader.*` directory. Inject the common bookkeeping
   fixture into both trees, the current producer into the current tree and the
   previous-reader assertions into the previous tree. Existing repository test
   helpers are compiled with `preparation_compatibility`. The actual strict
   readers, directory loader and validation code are unchanged.
2. Run `TestUploadReaderExperimentWriteFifty`. The existing
   `compatibilityServer` helper uses explicit disposable workspace, profile,
   authority and user-state directories. Upload fifty one-byte files through
   Create/Append/Complete, POST their actual ordered IDs through the current
   50-file preparation flow, block the injected namer, and close the server
   normally. The actual durable record is paused, with real schema-1 input and
   snapshot digests, UUID, receipt and attachment-expanded wire text.
3. Run `TestUploadReaderExperimentPreviousRejectsFifty` in the exact prior tree.
   Its production `readPreparation` must return `invalid preparation prompt`
   for that original full record. The parsed record's identity and both digests
   must match the genuine current snapshot; prompt text is valid and within its
   unchanged byte bound. Its production `loadPreparations` must fail for the
   same request without admitting it. A fingerprint of all disposable state
   before/after detects changed bytes, modes, mtimes, directory entries and
   symlink targets. Atime changes caused by reading are excluded.
4. Run `TestUploadReaderExperimentCompactFifty` in the current tree. Reopen the
   same state, replay the identical POST, retry with its exact receipt/attempt,
   and reach ordinary handoff with the same IDs, digests and wire text. The
   existing creation-proof helper supplies a valid completed-session fixture.
   Production `updateCreation` validates proof, binds uploads and performs
   terminal compaction; production idle-receipt retirement follows. No fixture
   code deletes the full preparation or manually strips its snapshot. Assert
   its durable replacement/move to `session-preparation-mappings/`, preservation
   of the original digest/receipt/slug/epoch and all fifty uploaded bytes.
5. Run `TestUploadReaderExperimentPreviousAcceptsMapping` in the prior tree.
   Its production strict reader and directory loader must both accept the
   normal snapshot-free terminal mapping with the same identity. The complete
   disposable-state fingerprint must again stay unchanged.

Each of the four Go invocations selects one exact test, runs uncached with a
60-second timeout and emits JSON. The pinned Node interpreter verifies exactly
one run/pass, no skips/failures and a package pass. Thus a missing selector
cannot falsely pass. Overall evidence requires all four phases and the final
success line. The utility watcher's capture preserves the revisions, tool
versions, test events and state fingerprints; all temporary source/state/log
copies are removed when the script exits. Keep the captured log in this session's
verification artifacts and record its actual status separately.

## Evidence limits

This demonstrates the preceding production preparation reader's count boundary
and normal terminal mapping compatibility. The loader is invoked with only its
real workspace and state-directory inputs, avoiding `New` side effects; it is
the same method used by normal startup. This does not certify every old-package
constructor, writer, collector, browser or runtime behavior. It does not change
the forward-only workspace package switch policy or authorize a downgrade.

The completed session uses the repository's exact receipt/creation-proof helper;
the configured session CLI path cannot run. This is durable-format and compaction
evidence, without live App Server inference or actual session initialization.
It tests one genuine 50-file snapshot and its ready terminal mapping, rather
than every unfinished/outcome combination. Browser draft cleanup has separate
contract/acceptance tests and is not part of this reader experiment.

Only this artifact directory was added. State, design, portal, application files,
feature refs and installed packages remain owned by the coordinator.
