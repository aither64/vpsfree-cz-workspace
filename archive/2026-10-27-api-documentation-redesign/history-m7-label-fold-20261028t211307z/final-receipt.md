# M7 narrow label/assertion fold — complete

Base `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Final feature HEAD `24ec424c9592951da38584379b43379b0c39f115`,
tree `288376a727deb3905d2c368150543a6d7cfc0971`. Exact five commits:

- A: `73b86b21d7d076c540d0d2fd52d0930e953e3afd`
- B: `2b51d9eb585ab6ce44221b45e512b4937e8ebd0f`
- C: `c83522c91d26b4643b891e7207d3276c04e2202c`
- D: `fabc27ca14501ae8e8c3551a391629cebc7224ec`
- E: `24ec424c9592951da38584379b43379b0c39f115`

A/B/C are literal previous SHAs. D is oldD plus ONLY the accepted profile label
expectation TypeScript(generated)→TypeScript API client (test-only.delta.patch,
SHA256 bdc8953ea476e07a52cf17da89d5dfebbfc819d80849814963690a33114fae62),
matching owner0's updated D snapshot. All five messages are verbatim. E is the
original13-path full-index/binary patch PLUS exactly one lead-approved equivalent
assertion: json_activation_spec.rb's plain /Could not find/ becomes
include('Could not find'). The subject String comes from Open3 stderr; the regex
has no flags/anchors/metacharacters, so both require that exact substring.
No production/runtime/guide/API behavior or graph changed. Raw E patch identity
is explicitly relaxed only for this assertion; old-E.patch/staged-E.patch and
new-E.patch/mechanical-test-delta.patch retain the comparison evidence.

Initial E ordinary hook failure is preserved (commit-E.log/execution and initial-
failed copies). Current frozen root tools are Ruby3.4.11, Git2.56, Bash5.3p20,
Overcommit0.73.0, RuboCop1.85.1, rubocop-rspec3.9.0. The offending line exists
unchanged at f6/oldD/439/6872. Prior E hookPASS remains actual priorNix scope; a
full prior process environment was not retained, so the discrepancy cause is
unknown. Config bytes and root lock identity are unchanged. No Nix realization,
install, dependency/pin/config edit or bypass occurred. Identical-config routine
Overcommit signing was used for fresh scratch and original path-sync setup.

Affected existing json_activation_spec quick ran ONCE:10/0 seed50232. Normal D
and corrected E HaveapiI18n/RuboCop and commit-message hooks passed. Before the
expected-old6872 feature move: an independent temporary index was seeded from
6872 and changed only the one equivalent assertion; its tree equals committed
final tree, accepted6872→final diff equals that sole patch, and f6 aggregate
full-index/binary patch is byte-identical to the independently constructed tree.
Exactfive/messages/A-B-C/Dlabelonly/Eoriginal+onecopfix, clean both worktrees/indexes,
logical flags and2148inputs passed. See before-move.json/aggregate.expected.patch.

Guarded ref move completed. Because final tree differs by the approved assertion,
original file/index needed exact one-path synchronization from final commit. The
initial postmove clean assertion detected it; git restore --staged --worktree of
ONLY that path completed its source/index update but post-checkout returned1 for
missing original-worktree signature. Effects were read-only reconciled exact/clean
and identical config ordinarily signed. No extra file change or uncertain effect.
The final original index equals the final tree; only the intended one blob differs
from6872, all other index entries and all flags preserved.

Final SAME combined extracted-gem/mounted-profile quick ran ONCE on exact final
head:10/0 seed50232, frozen server bundle. No duplicate make doc, A22 or C/D runtime
smoke. Original439's10/1 final quick and all old receipts stay historical. C smoke
remains bound to unchanged actualC; oldD smoke source/runtime/guide bytes are
unchanged except this spec literal, not relabelled as a new run.

After checks:2148 hashes equal, original and scratch clean/indexempty, no active
owned command/uncertain effect. All refs/scratches/messages/receipts preserved,
including unique accepted6872/failed439 backups and externally selected d67.
No migrations, no feature dependency/version/channel/input update streams;
complete five-series, changed paths, diffstat and range-diff supplied. Original
obsolete split/sidecar histories remain recovery refs, not final ancestors.
Peer d67 all-five-sibling graph pin remains supported by its retained exact ref;
deployment unreported, no nonancestor-merged/source-equivalent claim.
Independent final review remains pending. No push/fetch/network/preview/service/
provider/TLS/private-fixture/longgate or lifecycle operation.

SOURCE/Git/hooks slot RELEASED.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
