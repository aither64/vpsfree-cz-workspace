# HaveAPI branch inventory

Base: `feda9518634a89b0ff5724fa32bea3c694deebdc` (`origin/master`).
Head: `ed88e2a814b3e1f8bbf85067f84cf64032c20f63`.
Branch: `2026-10-11-diagnose-vpsadmin-api-exception`.

## Complete commit series

```text
8053a2292396bb3a982431f2df6ef99a2a5b7b6f servers/ruby: ship shared documentation in release gems
ed88e2a814b3e1f8bbf85067f84cf64032c20f63 ci: update shared Ruby workflow actions
```

The functional commit includes the runtime fix, release prerequisite/check,
regression specs, matching CI preparation/triggers, ignore rule and developer
guidance because they implement/verify/document one packaging failure. The
separate mechanical CI commit updates imported actions to current compatible
upstream majors, required by workspace policy for edited workflows.

No superseded branch approaches or fixup commits remain. No schema changes or
migrations; no migration was merged, released, deployed or externally consumed.
No HaveAPI version bump, release, backport, vpsAdmin dependency or configuration
update is present. Dependency update streams are checkout v6→v7 and setup-go
v6→v7, each updated once in the mechanical commit; no repeated streams.

## Final diff

[Complete diff](haveapi-final.diff)

```text
.github/workflows/_ruby-rspec.yml                  |   8 +-
 .github/workflows/servers-ruby-rspec.yml           |   8 ++
 Makefile                                           |   2 +-
 doc/agent-instructions/development.md              |   2 +
 doc/agent-instructions/releases.md                 |   8 ++
 servers/ruby/.gitignore                            |   1 +
 servers/ruby/Rakefile                              |  19 ++++
 servers/ruby/lib/haveapi/server.rb                 |   7 +-
 servers/ruby/spec/documentation_spec.rb            |  14 +++
 .../ruby/spec/extensions/exception_mailer_spec.rb  |  33 ++++++
 servers/ruby/spec/packaging_spec.rb                | 124 +++++++++++++++++++++
 11 files changed, 222 insertions(+), 4 deletions(-)
```

## Review remediation

The reviewer assessed the original two-commit series and confirmed clean
history/no migrations/no repeated streams. One Important test-environment
finding was fixed narrowly and folded into the functional commit before
publication. The final series still has exactly two logical commits; its diff
against reviewed head is confined to the requested packaging-spec correction.
See [review reconciliation](review.md) and [remediation diff](review-remediation.diff).
