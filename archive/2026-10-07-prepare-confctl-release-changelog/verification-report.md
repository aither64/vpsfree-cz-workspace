# confctl v3.0.0 candidate verification

Exact source: 1b56616eff41e760327f3a0dbed8875e4aa9dbec. Release commit is last.
Independent final review: no findings; see [report](review-report.md).

- Ruby 3.4.9: 35 RSpec examples, no failures.
- Minimum-supported series Ruby 3.3.10: 35 examples, no failures.
- Full RuboCop: 120 files, no offenses. Tracked Nix formatting passed.
- Clean final Git export: generated manual/HTML pages and built release gem.
- Package: 239 files, exactly committed source plus six generated doc files.
  Version 3.0.0, Ruby >=3.3.0, executable confctl. No local caches/dependencies.
- Extracted CLI: unbundled child retains dependency paths and asserts extracted
  ConfCtl.root, loaded confctl.rb and version, then successfully runs --help.
- Actual Nix confctl package and refreshed native dependencies built. Evaluated
  path-gem metadata, installed source gemspec and loaded source all identify
  3.0.0. Actual Nix launcher --help passed.
- Artifact checksum verified independently with sha256sum --check.

Artifact: worktree pkg/confctl-3.0.0.gem.
SHA-256: a91ac2d50a62edcb77d0b5575dd202bf5ea85c09647c823196c6a9061ee696c1.
[Metadata](gem-metadata.json), [inventory](gem-files.txt), [checksum](gem.sha256).

[Full batch log](revised-verification.log) contains successful Ruby/lint/gem
checks and Nix build. Batch exit 1 came from the helper incorrectly expecting
confctl's own installed gemspec in its dependency environment. The package
loads confctl directly from its Nix source; corrected focused verification
passed with exit 0: [log](nix-focused-verification.log). No project edit needed.

Earlier fixture-contamination and spec-load-path wrapper failures are retained
in revised-verification-first.* and revised-verification-loadpath.*. Each Ruby
process now uses a fresh working directory with explicit source helper/spec
paths. Original a2f27fc artifact/checksum/CI are superseded. After user approval, master and annotated tag were published at this exact
head and the exact gem was uploaded. RubyGems metadata and a fresh public
download match this checksum. GitHub RSpec/RuboCop passed; self-hosted Tests
remains queued and monitored. [Publication evidence](published-gem-verification.json).
