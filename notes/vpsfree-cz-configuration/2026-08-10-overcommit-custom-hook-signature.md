# Overcommit installation does not sign custom plugins

## Workflow

Install repository hooks with `bundle exec overcommit --install`, then sign
trusted repository-local pre-commit plugins with
`bundle exec overcommit --sign pre-commit` before creating commits.

## Symptom

A fresh checkout successfully installs Overcommit, but its first commit fails
with a message that `.git-hooks/pre_commit/nixfmt.rb` was added or changed.

## Cause

Overcommit installation automatically records the `.overcommit.yml`
configuration signature. It does not record signatures for repository-local
hook plugin implementations. Those plugins remain untrusted until their hook
type is signed explicitly.

## Fix and verification

Sign the `pre-commit` hook after installation. A disposable clone reproduced
the rejection after installation alone and successfully created the same empty
commit after signing. This was diagnosed for
`work/2026-08-10-vpsfconf-daily-update`.
