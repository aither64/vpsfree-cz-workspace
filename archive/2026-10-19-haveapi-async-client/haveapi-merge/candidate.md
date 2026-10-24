# Reconciled HaveAPI candidate

Final source `e16526d42949bae96bf35e8db6cd984d739dcc2a`, tree
`32b6099b5ec3e367c9ce86b81afa8c4ee74b461c`, based on incoming master
`c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`. Working tree and index are clean.
No rewritten feature or master publication has occurred. The original reviewed
403 (and ancestorf94) is retained locally and on origin at ordinary branch
`2026-10-19-haveapi-async-client-before-master-rebase`.

Eight original substantive commits remain in order with identical authors,
author dates and messages. [Mapping, stable patch IDs and whole-tree
reconstruction](equivalence.json), [range-diff](range-diff.txt), and
[complete new series](reconciled-series.txt) bind the old/new ranges.
Stable IDs match for commits1/3/4/5/6; commits2/7/8 include the recorded upstream
context and overlap reconciliation and require affected review, not automatic
certified equivalence.

Only five overlapping paths required the accepted union: Makefile, README,
release guide, artifacts.rb and release_spec.rb. The exact resolution is recorded
[against old403](five-path-resolution-vs-old.diff) and [against incoming
master](five-path-resolution-vs-upstream.diff). [Final base-to-head
diff](reconciled-final.diff). All57 incoming nonoverlap path states and all146
feature nonoverlap path states (including deleted/renamed source paths) match
original blobs/modes; untouched paths match the original baseline. Full tree
reconstruction includes incoming additions, feature deletions and the five
explicit resolutions. No migrations, database/state conversions, new pins or
new generated update stream. Existing client stages retain their independent
purposes and original evidence; affected review decides final history acceptance.

[Quick receipt](quick-receipt.json): syntax, metadata0.29.0, scoped lint,
53releaseRSpec and6Pythonartifacttests passed once. Actual quick commandexit0;
overall finalguardexit1 only from upstream test's generated Python bytecode.
[Disposition](generated-output-disposition.json) records that single owned file's
hash/header and its authorized move outside the repository, restoring clean
status without source edits, deletion or rerun. No disposable uv fixture
adaptation was needed. Normal hooks passed; nonblocking width/ambient extension
warnings are retained. Hook trust recovery used only inspected exact upstream
configuration and ordinary signing while the repository claim was held.

[Installed npm proof reuse inputs](proof-reuse.json): all51 original403 packed
files equal final committed candidate blobs; entire clients/js subtree equal403;
runtime+44declarations remain f94. Extracted inspect_npm/smoke_npm methods and
consumer fixture are unchanged. Compiler/dependency input hashes, actual selected
Ruby/Node/npm Nix paths and recorded Node/npm binary hashes match original proof.
The complete artifacts.rb file changed for upstream Python metadata/inspection;
no whole-file identity is claimed. Reuse recommendation is limited to the prior
actual installed npm CJS/types proof; reviewer owns acceptance of this scope.
No new package build/pack/install or broader client/server/WebUI campaign ran.

Lead released the preparation claim after source completion; source is frozen
while final affected review runs. Any further shared Git operation requires a
fresh held HaveAPI claim and lead release. Feature publication needs an explicit
lease against403 after review; master integration remains ordinary fast-forward
and non-force SSH only. No WebUI, release/tag/registry, runtime/deployment or
session lifecycle/cleanup operation is part of this candidate preparation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-async-client/
