# Strict-check action reference verification

Official release pages and GitHub API metadata were read before the bounded
workflow edit. Checkout's current latest release is v7.0.1 and the workflow
keeps its v7 major ref. The Nix installer latest release is v23; the existing
workflow selects v22.

This strict-mode edit retains v22 intentionally so source and explicit strict
runs use the same existing installer setup. Installer upgrades require their
own pipeline qualification; no unverified incompatibility of v23 is claimed.
Record this reason beside the unchanged reference in the workflow. This is the
workspace verification rule's explicit older-ref exception, not a dependency
upgrade bundled into the media-mode change. Required hosted source and strict
checks still run at their own exact heads.

Primary sources:
- https://github.com/actions/checkout/releases/tag/v7.0.1
- https://github.com/DeterminateSystems/nix-installer-action/releases/tag/v23

Native release/ref identities are retained in finish-k-{checkout,installer}-
{release,ref}1.json. No workflow, dependency, test or CI operation was launched
by these read-only queries.
