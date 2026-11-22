# Keep project gems out of workspace CLI commands

During HaveAPI integration, an execution helper exported the project's GEM_HOME
before invoking dev-session current. The workspace command uses its own packaged
Ruby. It loaded the project's native JSON extension, which was built for a newer
Ruby/glibc closure, and failed before any Git mutation.

Scope project Ruby variables to project commands. When a workspace command must
run inside that prepared shell, clear the inherited project gem/Bundler/load-path
variables for that command only:

```sh
env -u GEM_HOME -u GEM_PATH -u BUNDLE_GEMFILE -u RUBYOPT -u RUBYLIB \
  /home/aither/bin/dev-session current
```

Keep the declared project environment for Git hooks. The corrected identity
command and real post-merge/pre-push preparation passed in the same shell; the
ordinary hooked fast-forward merge and SSH push then succeeded. No dependency
installation or hook bypass was needed. The failed attempt was reconciled and
its repository claim released before repairing the helper outside the claim.

Evidence: work/2026-11-01-api-doc-language-settings/haveapi-integration.json and
cachefix-driver-identity-prep.log. This concerns a project environment inherited
by the workspace CLI; it does not change either component's dependency contract.
