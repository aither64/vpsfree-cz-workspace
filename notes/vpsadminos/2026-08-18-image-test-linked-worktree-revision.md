# Image tests from linked Git worktrees can lose the revision

## Symptom

Running `./test-runner.sh test image-scripts/test@guix` from a linked
vpsAdminOS worktree failed during test evaluation with:

```text
error: cannot coerce null to a string: null
```

The failure came from channel registration while rendering
`config.system.vpsadminos.revision`, before the test VM or image build started.

## Cause

At the initiative base, the test runner resolves its repository source through
a Nix path. A linked worktree has a `.git` pointer file rather than a `.git`
directory. The copied flake therefore has no revision metadata and cannot infer
the revision from an embedded repository.

This does not affect GitHub Actions' normal checkout. It is also separate from
the image-script revision passed later through `TEST_RUNNER_REPO_REV`.

## Workaround

Run the exact committed head from a temporary local clone with a real `.git`
directory. A local shared clone is sufficient and avoids changing the tested
tree:

```sh
tmp=$(mktemp -d /tmp/vpsadminos-image-test.XXXXXXXX)
git clone --shared --branch BRANCH repos/vpsadminos.git "$tmp/repo"
cd "$tmp/repo"
./test-runner.sh test image-scripts/test@guix
```

Remove the temporary clone after the test. Do not paper over the failure with a
test-only system revision override, because that changes the evaluated path.

Related initiative: `work/2026-08-17-image-build-failures/`.
