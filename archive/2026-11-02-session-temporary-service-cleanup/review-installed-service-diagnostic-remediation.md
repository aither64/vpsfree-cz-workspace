# Installed-service diagnostic review remediation

Blocking D1 is CLOSED by direct mandatory-change-review step9 verification at
local runtime `2b23f9765410bcb0985dbdd57411de00479bc0d0`, tree
`e1b65c92314edf21e286352086c15b1f1fd9c86d`. This accepts the diagnostic source gate
only. No producer correction, candidate VM result, publication, downstream pin,
production rollout, default integration or lifecycle permission follows.

Retain immutable reviewer0 report [review-installed-service-diagnostic.md](review-installed-service-diagnostic.md),
SHA256 d198897d72592a8ab61ee3e94be6b3d17382f6084d39781606785baa0ce3cc6e,
at reviewed d07e8f2db5b8045a10aa65cdc2df5efe83909e29. Same retained independent
Sol/xhigh/read_only reviewer performed all four lanes and found no additional
Important/Advisory issue. Its D1 remains historically open at d07; this closure
binds only the corrected committed successor. No automatic reviewer rerun.

The exact committed d07→2b delta changes only six existing lines by four spaces
in nix/tests/session-archive-lifecycle.nix, 6insertions/6deletions. Diff SHA256
69457a96e196d99603aa8ec39a34b7eb5c05170568879a8880659e150d90847a matches the focused
remedy. All Go, docs and other content are byte-identical to reviewed d07.

Lead independently parsed the exact evaluated script, hash
eb554f18118b777de69fe5b86fde5b3e21d83b6e53000775fda38f4a9be8fbe9: the GET and
try/except are inside the registered-candidates subtest; the handler contains only
diagnostic and raise; the original assertion is identical; all19 original trailing
statements are identical reachable siblings after try/except. Read the closed,
nondelegating focused control and actual RED/GREEN logs: success executes the
privacy/invocation/refusal/retry/retirement/foreign/revival paths; count failure
records one diagnostic and reraises before that tail; privacy failure stops before
invocation. Each path uses one GET. This is control-flow proof, not native proof.
The earlier ast.walk assertion-text validation did not establish reachability.

Lead independently matched source NAR
`/nix/store/9h8x9ccvhh1cq8qmcgfzim76kp3s571a-source` to
`sha256-Ugj//2al3dspjdt7jTPpcVAn8gG69kIIJcSVKiQNYVs=`. Compared all679 immutable
source entries with reviewed2aq: only the Nix fixture differs; its bytes equal the
committed Git blob. Paths, symlinks and executable modes match transitively.
Direct parent remains actual deployed0872; all six deployed commits are exact
ancestors. The single unconsumed diagnostic seventh was amended normally; d07/ref/
source/report/receipts remain retained. No fixup stack, new migrations, API/state
schema/capability or input stream. Lock/full9graph remain unchanged.

Owner final receipt installed-service-diagnostic/d1/final-receipt.json SHA256
38a30ea8c8f1c23e4e9cdb54a292629543d73622b0553ed2f52831f620213938 and focused receipt
ffa4291e9ef4f2138e3fe39299a60ab9057e0419b1f3a3af2f3994a5804128e7 are bound.
All source/index/commands settled. No Go rerun or native/build action was needed
for this precise indentation remedy. B may rebind the actual immutable corrected
input and execute its already-scoped candidate build package after verification;
main separately owns one labeled diagnostic VM. Deployed0872/SITEhyjx remains
selected under the held machine claim. Original failed installed verification and
historical first ambient effects remain unresolved/UNKNOWN independently.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
