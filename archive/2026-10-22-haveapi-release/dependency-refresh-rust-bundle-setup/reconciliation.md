# Frozen Rust bundle prerequisite: failed one-shot

The single granted setup exited **5** after **54.0 seconds** at HEAD
`090a188cb4ef3477324718627f4ae3415d1c0975`. The fresh Luna/low utility and
parent handle80513 have exited. No retry or release quick rerun followed.

The entry was parsed `nix print-dev-env --no-write-lock-file --json
.#client-rust`, followed by explicit exact Bundler4.0.23/Fiddle1.1.8 installs and
`BUNDLE_FROZEN=true bundle _4.0.23_ install` in new own ignored component paths.
The normal automatic shell hook was **not exercised**. Ruby3.4.11 and its
selected Nix default gem directory are recorded in reconciliation.json.

Bundler4.0.23 and native Fiddle1.1.8 reported installation success. The complete
frozen bundle failed while building Prism1.9.0: `prism.h is required`. The
captured mkmf.log compiled/linked its Ruby probe successfully, then could not
find prism.h, including with the gem include directory supplied. This evidence
does not establish why the header was absent. The final own/nondefault Fiddle
activation assertion was not reached, so complete bundle readiness is unproven.

All tracked/nonignored source hashes and the JS manifest/lock, ignored root
lock and committed Rust lock stayed unchanged. Existing JavaScript105 checks,
47-file baseline/determinism equality, release-check and Ruby style successes
remain valid. Both earlier release-fixture failures are preserved. The final
170-example release quick and candidate freeze remain pending. No Git/index,
application source, lock, release or registry mutation occurred.

See install.log, result.json, exit, effective-launch.json, watcher-final.md and
the compact reconciliation.json in this directory. Release0.30.1 remains held.
