# Packaged dev-cluster command access

Related initiative: `work/2026-09-09-ip-release-mechanism/`.

The installed workspace command currently captures provider output until the
command finishes. A long `vpsadmin-devcluster start` can therefore have an empty
redirected log while Nix and the runner are progressing. The per-cluster
`runner.log` and `state/*-console.log` show VM startup. The normal status command
reports the running/ready state after startup completes.

The installed wrapper also does not forward caller stdin. A command ending in
`services -- bash -s` can exit successfully without executing a supplied heredoc.
For an ad-hoc multiline operation, pass the complete script as a shell-quoted
`bash -c` argument. Use Python `subprocess.run` with an argument array and
`shlex.quote(script)` for the last argument, preserving literal newlines and
shell metacharacters. Assert the expected output and data state. Do not put
credentials in the script or command arguments.

The deployed `vpsadminctl` wrapper still selected `http://api.vpsadmin.test`,
while this cluster's frontend served the configured review hostname. OPTIONS
returned 401 on the old hostname and 200 on the configured HTTPS hostname.
Append a profile for the configured URL to the development root user's client
configuration, reusing the existing test-admin credentials without printing
them, then pass `-u` explicitly. Deep-copy each profile before YAML serialization:
shared nested auth objects produce YAML anchors, which the current CLI refuses
with `Psych::AliasesNotEnabled`. This is a local review-cluster workaround;
no production configuration or reusable workspace code changed.

The database package exposes Bundler under `ruby-env/bin/bundle`, but its Ruby
executable is under `ruby-env-wrapped/bin/ruby`. `ruby-env/bin/ruby` does not
exist. Run seed tasks from the package's database directory with the deployed
seed service's RACK_ENV and SCHEMA settings.

A services update also runs the development seed reconciler. It reset the
explicit owners of its declared IP rows (IDs 1 and 2) to nil while preserving
interfaces, charge provenance and EnvironmentUserConfig usage. It also reapplied
the default ownership policy/languages. This is separate from ordinary database
migration seeding, which only runs at initialization.

For this initiative, the pre-update inventory and verified usage identified the
exact two assigned owners. Restored those owners through model updates inside
the shared IP current-lock helper, preserving their already-recorded quota.
Reapplied the review ownership policy, CS/EN preferences, notification overlay,
URL and IP free-chain definitions. Both members' IPv4/IPv6 usage then exactly
matched their owned allocations; the unsent campaign and all custom addresses
were unchanged. Avoid another cluster update after handing over interactive
fixtures without first recording and reconciling seed-managed state.

Use the repository-pinned Nix shell for Node when running temporary browser
checks. A Node store path reported by a completed reviewer was no longer
available when reused directly (exit 127). Reentering the pinned shell resolved
the executable. Do not assume an unrooted tool path remains available throughout
a long session; the exact reason that path disappeared was not investigated.
