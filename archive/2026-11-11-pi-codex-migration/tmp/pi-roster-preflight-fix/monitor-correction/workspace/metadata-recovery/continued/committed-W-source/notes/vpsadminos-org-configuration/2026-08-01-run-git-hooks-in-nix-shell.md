# Run repository Git hooks in the Nix shell

Initiative: `work/2026-08-01-test-framework-ci`

Running `git push` from the ambient shell failed in the pre-push hook because
Bundler could not find the repository-pinned `overcommit` gem. Run Git commands
that invoke hooks through `nix develop -c git ...`; the development shell
provides the repository's Ruby and bundled hook environment. The retry through
the Nix shell completed successfully.
