# Repository and conversation follow-up

Approved 2026-09-12. Reuse all current initiative branches. This follows the
already deployed profile29 implementation; do not integrate or archive branches.

## Behavior

- Accepted steers remain above the composer, including across same-tab reloads,
  until the canonical transcript matches their message ID and digest. Keep
  accepted, observed and unknown outcomes distinct. Preserve queue deletion.
- Waiting label: "Waiting for instructions". Shared accessible SVG copy icons
  replace transcript Copy text and copy full commit hashes or comparison links.
- Local branch action: Compare. Commit rows have subject, ellipsis message
  disclosure, external arrow and copy hash. Details show original full message.
- Comparison totals and each file show additions/deletions and change status;
  no statistics on overview commit rows. Binary counts remain explicitly unknown.
- Split is the default/saved preference. Full-file Before/After defaults to After,
  except deletions use Before. Reuse already-loaded blobs.
- URLs identify exact immutable comparisons, optional commits, files, layout,
  file version, and old/new line anchors. Real links support new tabs. Direct
  navigation and Back/Forward restore state and expand linked hidden context.

## Implementation

Keep native Git. Remove full discovery from registered repository requests;
share 5-second discovery caching for discovered worktrees. Cache immutable
responses in a 64 MiB LRU and coalesce duplicate work. Four Git jobs at a time,
with deadlines including queue admission. Batch initial histories (8), states
(32) and file content (4); include selected/first file preview in comparison
responses. Preserve single endpoints and current authentication. Read full
messages using %B and stats using --raw --numstat -z in one native Git command.

Persist versioned small exact-comparison descriptors, scoped to session and
registered repository identity, separately from existing manifests/journals.
Restart and cache eviction reconstruct views. Branch movement never silently
changes a shared review; missing objects give an explicit unavailable result.
File selection is checked against issued comparison files. Git objects are not
retained or fetched solely for links.

Retain CodeMirror 6 and add maintained Shiki 4.4.3 (release 2026-08-10, active
2026-09-11). Tokenize complete old/new sources independently with Shiki's JS
regex engine in a same-origin worker. Use public CodeMirror decorations and
nonce styles for split/full. Build unified projected rows from public Chunk.build
results, preserving source line maps, syntax and change marks, dual gutters,
collapsed context and viewport virtualization. Stock unifiedMergeView lacks
original syntax context. Package selected grammars and github-dark theme with
the worker; no CDN, WASM, eval, extra Git or icon dependency. Keep existing
512 KiB/12,000-line blob limits and bounded mounted editors.

Sources: https://github.com/shikijs/shiki/releases,
https://codemirror.net/docs/ref/, https://shiki.style/guide/install.
Pierre Diffs 1.4.2 was evaluated but its rendering ignores useCSSClasses and
emits inline token styles incompatible with the portal CSP. No vendor fork.

## Validation and rollout

Focused receipt/clipboard/browser contracts, Git stats edge cases, authorization
and durable-link restore tests, batch/cache/cancellation checks, and syntax/
projection tests precede committed four-lane xhigh mandatory review. Then Nix
package/integration and real browser checks, CI and feature-profile deployment
to aitherdev. Compare direct and HTTPS latency with recorded ~600 ms direct
baseline: no registered-request workspace scan and >=75% median direct metadata
improvement. Verify all line anchors, offscreen/collapsed navigation, full-file
versions, frozen links after restart/branch movement, and strict CSP.

New fields/endpoints and private descriptor state are additive. Old package
versions ignore new records and retain existing session/lifecycle formats.
Refresh codex-web -> dev-workspace -> organization -> workspace package pins in
that order. Preserve old profile rollback readability; do not interrupt other
sessions for a profile switch. No merge, archive, delete or branch deletion.
