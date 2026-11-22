# Subdirectory `.gems` can break vpsAdminOS Nix builds

Initiative: `work/2026-07-24-ct-start-hang`

## Symptom

After running `nix develop .. -c bundle exec rspec ...` from `osctld/`, a
subsequent test-runner evaluation failed while building the osctld gem:

```text
Gem::InvalidSpecificationException
["CHANGELOG.md", "LICENSE.md", "README.md", "bundler.gemspec",
"exe/bundle", "exe/bundler"] are not files
```

The build log listed many paths below `./.gems/` before `osctld.gemspec`.

## Cause

The development shell sets `GEM_HOME="$(pwd)/.gems"`. Entering it from the
`osctld/` subdirectory therefore creates `osctld/.gems`, not the expected
repository-root cache. `.gems` is gitignored, but the osctld Nix source still
includes that subdirectory. `gem build` then discovers cached dependency
gemspecs and validates them against files that are not present in the copied
cache layout.

## Workaround

Enter `nix develop` from the repository root. Run an osctld spec only after the
shell is established, for example:

```sh
nix develop
cd osctld
bundle exec rspec spec/osctld/cgroup/container_params_spec.rb
```

If `osctld/.gems` already exists, move or remove that generated cache before a
Nix build. In this initiative it was moved to
`/tmp/osctld-gems.VDbFAt/.gems`, after confirming git classified it as ignored
and no tracked file was involved.
