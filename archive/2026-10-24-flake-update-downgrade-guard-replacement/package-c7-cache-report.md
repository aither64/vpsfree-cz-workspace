# Consumer Git-cache rework checkpoint

Cache adoption and lead-approved prose are implemented, with the existing R pin
held in every workflow. The sole final provider revision, adoption consolidation,
ordinary hooks/local commits, independent affected/history review and publication
remain pending. This is interim evidence, not final immutable-source acceptance.

[Quick receipt](package-c7-cache-quick.json) records all commands and current
heads/owned paths. [Starting inventory](package-c7-cache-start-inventory.json)
binds the original published heads and exact local backup refs.
[Official action evidence](package-c7-cache-actions.json) records latest releases,
resolved refs and runner/runtime compatibility.

Five ordinary workflows add restore/save pairs for `~/.cache/confctl`; both
configuration workflows retain their pairs. All seven save under
`${{ !cancelled() }}`. Cache miss never skips the guard. Non-cache YAML semantics
are identical to each current HEAD, and both edited helpers change usage text
only. All source/deployment input pins and locks remain unchanged.

The lead directly approved the five cache paragraphs and the HaveAPI/TF/IRC
removal of obsolete comparison-token instructions. Workflow token environments
remain unchanged. JSON alias metadata, selections, update subjects and the final
committed-HEAD lock check are preserved. No standalone configuration docs were
added; the shared backend guide/manual remain with confctl.

Known quick checks passed in each declared Nix shell: 40 ordinary and 20
configuration actual shell-body fixture scenarios, plus 98 cache scheduling-model
scenarios and 14 negative controls. YAML/Bash parsing, three fixture AST checks,
all seven diff checks, two helper-body equivalence checks and seven non-cache
workflow equivalence checks passed. The cache model checks GitHub scheduling;
it does not execute Actions cache uploads or duplicate provider ancestry logic.
The first cache-check negative control exposed a fixture KeyError; its validator
was corrected before the passing seven-project run. No application failure was
found. Initial backup-ref existence inspection stopped before any mutation;
all seven exact backups were then atomically created and verified.

All seven original feature heads remain unchanged, with empty indices and only
owned unstaged edits. HaveAPI stays on tested 74f/7ac; later default1103 movement
is deliberately deferred. Existing status independent vendor/metrics fixes and
all R review/runtime/CI roots are retained. No migrations or deployment change.

After final local provider+consumer heads, prepare separate new selected-path
manifests/drivers and a shared owned mirror cache. The accepted scope is seven
guarded updater/commit/final-lock paths, actual IRC/configuration caller hooks,
real cold/warm cache receipts and a local Git target race. It omits unchanged
dependency refresh/build stages and TF8; historical full R runs stay historical.
No API-only token loader will be carried into new drivers. Root owns serialized
runtime after final committed quick checks/review/publication.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/
