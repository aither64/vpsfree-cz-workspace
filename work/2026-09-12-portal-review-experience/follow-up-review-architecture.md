# Architecture and repetition review

Review result against the frozen packet revisions: **0 Blocking, 1 Important, 3 Advisory**.

Reviewed ranges:

- `codex-web` `83770217d63f2c206689d2c569e1c81950544504..de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`
- `dev-workspace` `d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2..ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1`
- `vpsfree-dev-workspace` `a30de6c62d2bcd1ff41ee48018c595140c6d4042..534d0f2c5530bbbbf36d8254d282a9945cef9bfc`
- `workspace` `5dbe312b1edf6a4454c4e86ec06f68baa3b5f4b4..77ca31a5e3e5e4f44c907b34b0f30bd99aec6980`

## Findings

### Important — viewport and loading exemptions defeat the eight-editor resource bound

**File:** `portal/internal/web/static/repository-review.js:229-241`
**Related contract:** `portal/review-ui/highlight-client.js:1-3`
**Commits:** `a10fcb658c72213d263f0f48649c49188e2688ab`, `5eeed4e3759c37050d9bab3719c1af4e9a67906c`

`trimEditors` counts every record with either an editor or retained content, but it refuses to evict the selected record, any loading record, and every record within 700 pixels of the viewport. The loop can therefore exhaust its candidates while `count` remains greater than eight. A tall viewport containing many short file sections is a deterministic example: the observer loads more than eight records, every record passes the near-viewport exemption, and none is released. Concurrent loads create another path above the cap because all loading records are exempt.

This is more than an imprecise cache target. A record can retain both file sides and a CodeMirror instance, while each side may approach the advertised 512 KiB preview limit. `highlight-client.js` separately fixes `MAX_PENDING` at 17 on the assumption that at most two sides of eight mounted files plus warmup can exist. Once the UI violates that invariant, source retention and syntax requests are governed by different limits; the worker may reject excess work, but the mounted content remains above the promised bound. Comparisons allow up to 5,000 files, so the retained set can grow with viewport/layout behavior rather than with the intended constant.

The actual-browser fixture uses 100-line files in a 900-pixel viewport and checks navigation and rendering, but never counts retained editors/content. Fix the eviction algorithm so it always finishes at `<= 8`, preserving the selected/current renderer explicitly. Evicting a loading record must also invalidate its render generation and cancel or ignore the in-flight result so completion cannot recreate the evicted editor. Add an actual-browser case with many short files and a tall viewport that asserts the hard bound after loads settle.

### Advisory — server and worker disagree at the exact line-limit boundary

**Files:** `portal/internal/repository/review.go:24-27,545-550`; `portal/review-ui/highlight.js:44-50`; `portal/review-ui/editor-model.js:4-5`; `portal/internal/web/static/repository-review.js:224`
**Commit:** `5eeed4e3759c37050d9bab3719c1af4e9a67906c` (interaction with the existing Go limit)

The Go reader defines the limit as at most 12,000 newline bytes. The worker defines it as at most 12,000 logical lines. A nonempty file with 12,001 logical lines and no final newline contains exactly 12,000 newline bytes, so the server returns it as a supported text preview while the worker rejects syntax highlighting. The source remains readable through CodeMirror, which keeps this advisory, but the UI reports syntax highlighting as unavailable for input the API classified within the supported limit.

The repeated rule has already drifted: `editor-model.js` exports `MAX_BYTES` and `MAX_LINES`, but neither export is consumed; `highlight.js` and the user-facing metadata text hardcode the values again. Existing tests cover 12,001 newline bytes on the Go side and byte overflow on the worker side, not the logical-line boundary with and without a final newline. Choose one definition, apply it consistently, consume or remove the unused JS declarations, and add exact 12,000/12,001-line fixtures for both newline endings.

### Advisory — language detection and bundled grammar support are a manually mirrored registry

**Files:** `portal/review-ui/editor-model.js:23-46`; `portal/review-ui/highlight.js:4-34,49-50`; `portal/review-ui/editor.test.mjs:55-89`
**Commit:** `5eeed4e3759c37050d9bab3719c1af4e9a67906c`

`languageForPath` maps extensions and special filenames to language identifiers, while `highlight.js` independently imports and registers the corresponding Shiki grammars. The source comment explicitly requires the two lists to be kept aligned. If a detector entry is added without its grammar, `tokenizeSource` silently returns an empty token set and the file loses highlighting without an error that identifies the omitted registration.

A focused inspection initialized the bundled highlighter and confirmed that every identifier currently returned by the detector is loaded, so there is no present user-visible mismatch. The checked-in tests only sample the registry, however. Add bidirectional coverage that enumerates every detector output and verifies that each is loaded; it may also reject bundled grammars that are accidentally made unreachable. A broader configuration abstraction is unnecessary if an exhaustive contract test makes the intended two-site boundary explicit.

### Advisory — the runtime commit series contains a nonfunctional UI increment

**Files at the named commits:** `portal/internal/web/static/repository-review.js:198,258,294,318`; `portal/review-ui/editor.js:7-21`; `portal/internal/web/repository_review.go:206-285`
**Commits:** `a10fcb658c72213d263f0f48649c49188e2688ab`, `b924a157043b7c3535cccde514d63fad52cbffdb`, `5eeed4e3759c37050d9bab3719c1af4e9a67906c`

Commit `a10fcb6` changes the browser to call the new history/file batch operations and to await `editor.ready` and call `editor.revealLine`. The batch operations do not exist until `b924a15`; the editor at `a10fcb6` still returns only `destroy`, and the new methods do not arrive until `5eeed4e`. The Go test added in `a10fcb6` exercises exported URL/metadata helpers only. The Playwright harness file is present but is not referenced by the repository's test/package definitions at that revision, so it does not reveal the missing runtime interfaces.

The exact downstream pins consume the final head, so this does not break the proposed deployment. It does make the feature history unsafe to bisect, test per commit, or selectively revert. Because the branch is not yet integrated, reconstruct the series in dependency order (backend/editor contracts before the UI consumer) or squash the three tightly coupled increments into one functional commit.

## Architecture and consumer assessment

The final-tree ownership is coherent. Native Git parsing and resource limits remain in `portal/internal/repository/review.go`; HTTP authorization and session binding remain in the web service; immutable cache/coalescing and bounded batch orchestration have separate owners and the batches reuse the single-item service methods. Durable descriptors are additive, scoped to the tracking directory identity, thread, and repository registration, and the recovery tests cover restart, archive rename, branch movement, object loss, and registration replacement. I found no duplicate Git parser, alternate authorization path, or caller-controlled filesystem/revision boundary in the changed implementation.

The shared copy control belongs in `codex-web`: `createTranscriptCopyButton` wraps the additive generic export, and the provider tests cover current callback resolution and clipboard failure. The runtime is a representative consumer and its browser harness imports the real provider module. The final pins form the documented one-way chain: runtime pins `codex-web` at `de83e9c`, the organization extension pins runtime at `ebc0e4a`, and the workspace pins the organization extension at `534d0f2`. Older profiles can ignore the additive descriptor directory, so the provider-to-runtime-to-organization-to-workspace rollout remains compatible.

## Residual validation gaps

- This review did not run long Nix, VM, or deployment integration tests, as required by the packet. The browser acceptance test mocks the API, while Go tests cover Git, authorization, cache, and persistent descriptor behavior separately; the packaged end-to-end composition remains for post-review validation.
- The focused grammar-registry check used the pinned Node/Shiki dependencies and found no missing language at the frozen head. It is not a substitute for the repository-level exhaustive test requested above.
- Findings and line numbers refer to the frozen packet heads. Remediation commits created after those heads were outside this review and require focused coordinator verification; a new architecture rerun is needed only if the remediation changes the described contracts or introduces a broader design.
