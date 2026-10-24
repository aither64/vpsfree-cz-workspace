#!/usr/bin/env bash
set -euo pipefail

bundle exec overcommit --install
bundle exec overcommit --sign
bundle exec overcommit --sign pre-commit
bundle exec overcommit --sign pre-push

hooks=$(git rev-parse --path-format=absolute --git-path hooks)
test -x "$hooks/pre-commit"
test -x "$hooks/commit-msg"
test -x "$hooks/pre-push"
test -x "$hooks/post-merge"
