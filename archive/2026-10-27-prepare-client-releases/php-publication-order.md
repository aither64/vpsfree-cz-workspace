# PHP mirror publication with a short repository claim

Prepared operation design only; no publication or repository mutation performed.
Lead accepted preparing this route after the tagged artifact exists. The user
must explicitly approve `vpsfreecz/haveapi-client-php/master`, its `v0.31.0` tag,
and publishing PHP before the other registries.

## Existing behavior and limits

Selected package policy was read through `workspace-host coordination guide`:
`/nix/store/3jagad4cag0xq36fnr12vyinaiq1rpxy-dev-workspace-0.2.0`.
Repository claims cover only fresh checks, merge/hooks, push and remote proof.

HaveAPI `utils/release/publish.rb` has no preparation-only publisher operation.
`sync_php` combines preparation, commit, tag and push. Its `preflight_php`
accepts an existing tag only if its file contents/modes match the retained PHP
tar, excluding mirror-owned `AGENTS.md` and `.github`, and the tagged commit
message contains the exact `HaveAPI-Source: <SHA>` line. `sync_php` then returns
without a push. The ordinary Git preparation below uses that existing verified
match path. Do not call `publish` or `sync_php` locally, spoof `GITHUB_*`, modify
the workflow, or hold a claim across registry uploads.

`Workflow.artifact_id` only queries the current `GITHUB_RUN_ID`. Cross-run
artifact reuse is not supported. A normal branch validation and later tag run
therefore build separately under their existing contracts; this is justified.
Only the tag run's retained original artifact is used for this operation. Do
not add another local release build. Tag-run retries retain the original files
under the documented recovery rules.

Mirror instructions evidence: GitHub tree at
`a02dd2506209f54ea782fbd949243207bf9f93bc` has no `AGENTS.md` or declared
Overcommit/pre-commit/Lefthook/npm hook configuration. Root files include README,
CHANGELOG, LICENSE.txt and composer.json. Recheck instructions and configured
hooks at the fresh preparation base; preserve any mirror-owned files.

## Implementer0 preparation package, outside ownership

1. Let the reviewed HaveAPI `v0.31.0` tag run finish its build job and wait at the
   protected `release` environment. Hold no repository claim during that wait.
   Record the exact run ID, artifact ID, source SHA and manifest hash.
2. Download `release-<RUN_ID>` with `gh run download <RUN_ID> --repo
   vpsfreecz/haveapi --name release-<RUN_ID> --dir <fresh-artifact-directory>`.
   At the exact HaveAPI source, verify with
   `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c ruby utils/release/cli.rb verify
   <artifact-directory>`. No rebuild or manifest editing.
3. Register the PHP repository for this session using canonical
   `git@github.com:vpsfreecz/haveapi-client-php.git` and default `master`, with a
   normal isolated feature worktree. Prepare a separate clean target worktree
   at the recorded remote master base. Both are owned by this session.
4. Verify a clean feature checkout, expected current release tag/base, no existing
   conflicting 0.31.0 tag, required hooks and ordinary SSH access. Read-only
   `Publisher#preflight_php` may validate the current mirror against the retained
   artifact. It must return false for a new release, or true only for an exact
   already-published match, which should be reconciled instead of rebuilt.
5. Extract the verified `haveapi-client-php-0.31.0.tar` into a fresh directory.
   Copy its files/modes over the clean feature worktree, deleting obsolete
   library files while preserving `.git`, `AGENTS.md` and `.github`.
   A conventional copy is `rsync -a --delete --exclude=/.git
   --exclude=/AGENTS.md --exclude=/.github <snapshot>/ <feature-worktree>/`.
   Inspect the resulting diff before staging only the intended mirror files.
6. Make one normal hooked commit using a message file with these exact contents,
   substituting the tagged HaveAPI source SHA:

   ```text
   Release 0.31.0

   HaveAPI-Source: <HAVEAPI_SOURCE_SHA>
   ```

   Use `git commit -F <message-file>` and `git tag -a v0.31.0 -F
   <message-file>`. The author identity need not impersonate github-actions;
   snapshot and provenance are the helper's acceptance contract. Record exact
   PHP commit and annotated tag object. Publish the preparation feature branch
   under the normal workspace rule, without pushing master or the release tag.
7. Validate the candidate using existing read-only methods from the exact
   HaveAPI source in its top-level tools-only shell:

   ```ruby
   require './utils/release/publish'
   artifacts = HaveAPI::Release::Artifacts.new(Dir.pwd)
   publisher = HaveAPI::Release::Publisher.new(artifacts, ARGV.fetch(0))
   raise 'PHP candidate differs' unless publisher.preflight_php(ARGV.fetch(1))
   ```

   Pass the retained artifact directory and isolated PHP candidate worktree.
   Constructor verification checks the original artifact set; preflight checks
   the annotated tag's tree/provenance. Also require the tag's peeled commit to
   equal candidate HEAD and that HEAD descends from the saved remote base.
   This invokes no publishing command or credential path. Include the generated
   mirror diff, exact base/head, original artifact identity and no-migrations
   conclusion in normal review/acceptance. No additional application tests are
   needed for byte-identical mirrored PHP already covered by the tag build.

## Lead's short integration critical section

After the concrete candidate is reviewed and the named PHP integration/tag/order
approval is recorded, acquire only the registered PHP repository. Inspect the
exact claim with `claim-status`; act only while held.

- Check the prepared source/tag, clean target and fresh SSH remote master/tag
  refs. Remote master must still equal the prepared base and the 0.31.0 tag must
  still be absent, unless it is an independently reconciled exact completed
  operation. Release and repair outside ownership on stale preparation.
- In the prepared target, run `git merge --ff-only <PHP_FEATURE_HEAD>` with
  ordinary hooks. Inspect results, including post-merge hook status.
- Push the prepared commit and tag atomically:
  `git push --atomic origin HEAD:refs/heads/master refs/tags/v0.31.0`.
  Never force. Prove remote master equals the intended PHP head and the remote
  tag object and peeled SHA equal the saved values with `git ls-remote origin
  refs/heads/master refs/tags/v0.31.0 'refs/tags/v0.31.0^{}'`.
- Release ownership immediately and verify released status, before records,
  Packagist waits, protected-environment approval or other workflow monitoring.
  On an uncertain push, reconcile both refs while actively holding the claim;
  do not retry blindly or release while shared mutation effects remain unknown.

After release, refresh read-only PHP equality/provenance evidence and approve the
protected HaveAPI publishing job. It clones the mirror and validates the matching
tag in preflight; its later `sync_php` is a no-op. No PHP claim is needed for that
read-only path. Diagnose any refusal rather than deleting or moving the tag.
Verify Packagist and the other destinations outside repository ownership.

PHP becomes public before RubyGems/npm/PyPI and the final GitHub Release. This is
a deliberate partial-publication boundary. Retain all original artifacts and
tags if later destinations fail; ordinary original-artifact recovery still
applies. No protected workflow approval is inferred from the earlier PHP approval.
