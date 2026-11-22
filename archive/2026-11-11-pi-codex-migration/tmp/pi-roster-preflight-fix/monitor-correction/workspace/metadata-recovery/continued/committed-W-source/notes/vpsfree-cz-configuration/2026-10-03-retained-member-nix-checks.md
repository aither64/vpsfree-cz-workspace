# Functional Nix checks from retained team members

During infra-monitoring implementation, retained native architect/implementer
shells could read the repository and use realized tools, but a Nix evaluation
failed connecting to `/nix/var/nix/daemon-socket/socket` with "Operation not
permitted". The operation did not start a build. Their saved workspace-write
access was valid; this was a Nix daemon boundary, not a Git/source permission
failure.

A fresh verification watcher under the installed catalog utility policy ran
session-authorized Nix operations successfully. It installed the frozen bundle
in the repository's pinned `nix develop` environment and later ran the metadata,
configuration and Prometheus checks. The lead supplied the implementer only
selected nonsensitive tool environment variables from that already-realized
shell for local formatter, Bundler and active Git hooks. No member access or
sandbox policy was changed; daemon-requiring checks remained watcher-owned.

When this recurs, distinguish local source/tool access from functional Nix
verification. Do not claim a denied evaluation is a code failure or a test
pass. Use the session monitor workflow for uncertain operations, preserve the
failed evidence, and report actual check results from the authorized execution
path. Avoid capturing a full environment, which may contain credentials.

Related records: work/2026-10-03-infra-monitoring/{state,design,
implementation-result}.md. Frozen bundle setup and all four focused/adjacent
checks passed; declared hooks ran on both behavior commits.
