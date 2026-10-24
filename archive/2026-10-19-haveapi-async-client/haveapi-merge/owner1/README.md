# HaveAPI incoming-master docs union

Preparation only, using exact old403 and incomingc182 blobs. Actual source writes
wait for owner0 docs-edit release; owner0 alone owns index/rebase continuation.
Main must inspect the exact union before staging.

Root README equals c182 plus exactly the approved JS/TS bullet label. Python's
synchronous/asynchronous bullet stays; no detailed JS paragraph returns.
Release guide keeps all incoming Python/PyPI/uv/artifact/version/provenance,
recovery and protected-publication text, adding only accepted403 JS table/alias,
committed npmci lock and gulp/installed-runtime/type-smoke paragraphs.
clients/js/README.md is untouched.

incoming-to-union.diff is the complete proposed two-file patch on c182;
old403-to-union.diff shows the preserved incoming additions. draft-receipt.json
binds content hashes and static links. No source/index/ref/Git mutation, test,
build, install, or WebUI operation occurred.
