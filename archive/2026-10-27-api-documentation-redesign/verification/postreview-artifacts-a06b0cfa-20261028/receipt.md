# Static artifact inspection stopped

Archive12842017816 from a06b0cfa/run40745814145 was safely extracted under
`release-40745814145/` after ZIP SHA256 matched the captured API digest.
`manifest-proof.json` proves exact source/version/run identity, all11 manifested
file hashes, all10 lock contents/hashes and all12 recorded tool fields.
The existing repository static Python distribution inspector exited0 without
imports or installs. `ci-locks/` preserves all declared CI locks separately.

The subsequent static source equality comparison stopped exit1 at
`AssertionError: pyproject.toml`: the sdist pyproject bytes do not equal the
checkout pyproject bytes. No follow-up diff/classification was attempted.
This may be generated build metadata; it is not yet a product or artifact
corruption conclusion. The first-failure boundary is retained in
`first-failure.json` and reported to lead before further inspection.

The npm identity/runtime/declaration comparisons and Python src comparisons
preceded the failure, but their aggregate final proof was not written because
the command stopped. The905-source-blob comparison and complete execution-ready
harness command remain unreached. No package was installed or snippet executed;
no tests/builds/network/source/Git/service operation or repair/reconstruction.
No active command/watcher; utility capacity was not taken. Existing archive,
manifest and old receipts are retained unchanged.
