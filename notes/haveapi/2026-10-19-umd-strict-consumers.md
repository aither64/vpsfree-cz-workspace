# HaveAPI UMD inside strict browser modules

Session: work/2026-10-19-haveapi-async-client.

A raw non-strict UMD bundle passed browser tests but its named npm import failed
at startup after Vite embedded it in an ES module. The source deliberately kept
legacy undeclared Authentication/ret/v1/v2 assignments; ES module strictness made
the first assignment throw even though Rollup output.strict was false.

The selected fix uses a finite internal host-global bridge and explicit property
reads/writes, preserving observable legacy values, live registry replacement,
callback returns and module evaluation order. Guard globalThis and retain
window/self/global fallbacks; do not use eval or disable consumer minification.
Both callback-only and async-producing commit stages must regenerate their own
bundle and declarations. The strict-context VM fixture and the actual minified
Vite/browser package proof passed at HaveAPI76f190f.

Package proof setup also matters: npm install --package-lock=false re-resolved
96 unrelated dependencies after npm ci. Reading the disposable lock with
--no-save --package-lock=true retained all407 existing package paths/versions
and manifest/lock bytes. The pilot now checks these before consumer tools.
Nested Playwright configs default preview cwd to the config directory; specify
the snapshot root for root-relative Vite commands. Production fixture builds
must explicitly select BFF mode and supply a synthetically validated session
through the existing real binding/remember helpers; do not relax app guards.

On Nix, exact cached WebKit binaries and static library checks alone were
insufficient. A blank-page probe logged WPE EGL display creation failure.
A substitute-only Mesa26.1.8 from the locked WebUI nixpkgs input supplied its
vendor JSON and GBM backend via scoped __EGL_VENDOR_LIBRARY_FILENAMES and
GBM_BACKENDS_PATH. No host graphics symlink, LD override or browser-validation
bypass was needed. The blank probe and final native-XHR WebKit case passed.
Use the current pinned browser manifest/closure for a future run; these package
versions/paths describe this session rather than a universal runtime pin.
