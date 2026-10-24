# Package A: semantic lock ancestry guard

Implemented by implementer0; Git ownership handed to implementer1 for the
combined A+B feature commit. Source ownership and follow-up fixes remain A's.
No A-only commit, integration or deployment occurred. B published the combined
A+B feature at final `7ba361d22a4aac044cb02abf8397800bcf5726bf`; its predecessor
`d58181a4d8b0de716fdb93c56f524175dd36cce4` differs only in guide/manual final-blob
publication instructions. A code and inputs are identical across that refresh.

Confctl SSH origin was fetched before worktree creation; base:
`cc40679d267165aecfa569128438bb55fe910268` (`origin/master`). Final shared
worktree: `worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl`;
branch: `2026-10-24-flake-update-downgrade-guard-replacement`.

## Owned paths and contract

- `lib/confctl/inputs/lock_graph.rb`: version-7 semantic graph rooted at the
  declared root; full follows resolution, terminal update selectors, all
  reachable logical paths, dangling/malformed/cyclic graph refusal.
- `lib/confctl/inputs/forward_guard.rb`: `ForwardGuard.new.validate(old, new)`
  accepts FlakeLock or parsed hashes, returns status/changes/issues and
  success?/rejected?/error?. All changed descendants checked; exact ancestry
  requests (including failures) deduplicated within one validation.
- `lib/confctl/inputs/github_compare.rb`: full immutable SHA comparisons via
  fixed HTTPS GitHub API, summary consistency checking independent of paginated
  commit lists; explicit GITHUB_TOKEN/GH_TOKEN credentials, no redirect or
  automatic retry, 10s connect and 30s read timeouts, sanitized failures.
- `spec/inputs/{lock_graph,forward_guard,github_compare}_spec.rb`: focused
  graph/policy/provider fixtures. These are the only A project files.

B owns existing FlakeLock/FlakeLockDiff, transaction, CLI, lasting input/manual
documentation, and final combined commit. Architect accepted the initial
github.com GitHub-fetcher-only provider scope; raw `flake = false` GitHub
sources are supported. Changed other fetchers/hosts/unknown attributes error;
unchanged unsupported sources remain. Known non-forward revisions, removed
logical paths and recognized source/extraction changes reject. Equal-SHA
changed locked attributes reject. Ancestry permits later upstream reverts;
equivalent cherry picks do not establish containment.

## Verification

From the confctl worktree in its declared Nix shell:

```sh
nix develop -c bash -c 'bundle exec overcommit --install && bundle exec overcommit --sign && bundle exec ruby -v'
nix develop -c bash -c 'bundle exec rspec spec/inputs/lock_graph_spec.rb spec/inputs/forward_guard_spec.rb spec/inputs/github_compare_spec.rb && bundle exec rubocop lib/confctl/inputs/lock_graph.rb lib/confctl/inputs/forward_guard.rb lib/confctl/inputs/github_compare.rb spec/inputs/lock_graph_spec.rb spec/inputs/forward_guard_spec.rb spec/inputs/github_compare_spec.rb'
```

Setup passed under a fresh Luna/low verification watcher (100s); Ruby 3.4.9.
Quick checks passed: 94 examples, zero failures; six Ruby files lint clean.
Logs: [package-a-shell.log](package-a-shell.log),
[package-a-quick.log](package-a-quick.log). Initial lint offenses were corrected
in owned files, then these final checks passed. Bundler emitted repeated
Gem::Platform reinitialization warnings without failures.

Initial registration returned a post-checkout Overcommit signature failure
after physically creating the clean worktree. Installing/signing reviewed
hook configuration in the Nix shell and retrying registration succeeded.
No hook bypass occurred. Overcommit stashes unstaged tracked edits during
commits; with B editing concurrently, lead chose one combined A+B commit after
all intended paths are staged. An unused temporary checkout-index snapshot was
prepared as a proposed hook workaround, never used for hooks/commit, then
removed. No command remains running. Six A paths were staged at Git handoff;
no B path was staged or committed by A.

No migrations or persistent-format changes. Live API smoke, full suite,
package checks and independent final review remain later lead-owned gates.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
