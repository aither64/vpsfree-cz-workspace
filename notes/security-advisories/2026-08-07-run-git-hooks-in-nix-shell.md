# Run security-advisories Git hooks in the Nix shell

## Symptom

`git push` can stop in the pre-push hook with Bundler reporting that the locked
RuboCop and support gems are not installed, even after the worktree bundle was
installed successfully through `nix develop`.

## Cause

The ambient shell does not expose the same Ruby and worktree-local bundle that
the repository development shell configures for hook commands.

## Workaround

Run Git operations that invoke repository hooks from the declared shell, for
example:

```sh
nix develop -c git push --set-upstream origin BRANCH
```

Do not bypass the hook. The retry should run the normal pre-push checks.

## Verification

The retry pushed branch
`2026-08-07-security-advisories-6-12-95-2` successfully, and its RSpec and
RuboCop GitHub Actions runs both passed.

Related initiative:
`work/2026-08-07-security-advisories-6-12-95-2/`.
