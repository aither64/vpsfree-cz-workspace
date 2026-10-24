# Folded final runtime repin

W `b9612bd2730e894dad9557bfb67bfa45d94695ba` (tree
`77104503810b5c21c71dc71c7cf398b10374f61a`) and C
`d7c0d2d3384142165072a0a475bf477c10e25a15` (tree
`4e060c9651dab832e88a61961ac689f947051bee`) are clean and SSH-published.
Both select B `e914c52a91d94192acd8368e77871b5a451196bd`; bases remain
W `9f6968eb` and C `50d263d4`. Each branch contains one final pin commit.

[final.json](final.json) binds old/new reviewed ranges, final trees, published
preservation refs, verified bundles, full series/diffs/graphs and quick checks.
[reconstruct.py](reconstruct.py) independently reconstructs complete locks,
flake content and raw Git root trees from reviewed c79 trees by substituting
only runtime URL/rev/NAR/time. Its output [reconstruction.json](reconstruction.json)
matches both final trees. Every other node, edge, follows path and source entry
is identical; there are no migrations. The complete original c79 review packet
remains unchanged, with checksums in preparation.json.

Formatter, matching deployment contract, diff checks and normal C hooks passed.
No broader tests repeated. One post-push CI inventory returned no runs for either
branch, with no CI wait. No product/system build or live/integration/lifecycle
action occurred. Lead owns independent mechanical review reuse and remaining
build/deployment gates; this report does not claim independent final review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
