# Extracted-gem tests must preserve Bundler dependency paths

`Bundler.with_unbundled_env` restores the original GEM_HOME/GEM_PATH. A local
Nix shell with dependencies in its original GEM_HOME can hide a failure that
occurs when CI installs dependencies only through Bundler's vendor/bundle path.

Capture resolved `Gem.dir` and `Gem.path` before unbundling, then pass them to
the artifact child explicitly. Clear Ruby source load overrides and assert the
framework loads from the extracted artifact. Test an empty original gem home.

A configured-path fixture must include the complete resolved dependency closure,
including Ruby-bundled non-default gems: linking only `.gems` omitted net-pop
and made the parent fail before exercising the artifact child. The full closure
fixture and exact-head CI passed after the correction.

Related session: `work/2026-10-11-diagnose-vpsadmin-api-exception/`.
