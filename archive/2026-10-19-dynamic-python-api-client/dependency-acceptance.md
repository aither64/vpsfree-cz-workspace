# Dependency refresh acceptance inspection

Exact base: c1823f3d70365b0442d0e2171bdf83bd4c6dbe31.
Exact head: 18331877660ed0f736a25b29914756da89df0df9.

Lead inspected clean status, the complete three-commit series, and final changes
to flake.nix, flake.lock, pyproject.toml and CONTRIBUTING.md. The only source
configuration change selects Ruby 3.4 at three existing sites. The existing Ruff
version gate, dependency ranges, build backend and release files are unchanged.

Implementer0 independently compared all 27 parsed lock records. Exactly certifi
and Ruff change version; 25 other versions remain fixed, with 24 full package
records identical. The project metadata changes only its Ruff dev specifier.
Dependency edges, sources and resolution markers are unchanged. Lock format 1,
revision 5, Python floor and marker split are preserved. All 20 target artifact
URLs, SHA256 hashes and sizes match official PyPI metadata. No lock-data concern
was found. This is acceptance support, separate from retained final review.

Implementer1 owns the committed changes and quick evidence. The refreshed native
Ruff and locked distribution both report 0.17.1; certifi 2026.10.19 loads a
verifying SSL context. Python checks pass 261 units, strict typing and formatter/
lint checks. The ordinary Ruby 3.4 setup and flake checks passed separately.

No application behavior, API, auth, database, migration, version or publication
change is included. Only publication of the follow-up branch is authorized.
