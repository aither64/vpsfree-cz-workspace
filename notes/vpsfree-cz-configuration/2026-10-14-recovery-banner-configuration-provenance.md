# Configuration rebase provenance

During recovery-banner integration, final configuration ac001928 and tested
cf698664 had the identical complete Git tree. Independent review found that
confctl embeds inputs.self.rev in /etc/confctl/configuration-info.json. The
runtime/module tests remained applicable, but deployment preparation produced
a new artifact from ac001928. Its embedded clean revision was verified before
activation; the coordinator later verified its live system and profile paths.
See work/2026-10-14-dismiss-recovery-banner/merge-config-baseline-review.md and
final-artifact-provenance.json for the finding and exact evidence.

A merge preparation invocation using nix develop with an explicit configuration
path from the coordination root failed with “mkConfigDevShell mode 'tools'
requires ./Gemfile”. Repeating the exact request from the configuration worktree
succeeded with its existing BUNDLE_GEMFILE/BUNDLE_PATH. The shell initialization
uses its working directory even when the flake path and Gemfile environment
variables are explicit. No hook was bypassed.
