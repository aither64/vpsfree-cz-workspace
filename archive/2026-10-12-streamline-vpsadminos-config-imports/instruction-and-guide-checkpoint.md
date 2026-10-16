# Instruction and guide checkpoint

Permanent instruction owners:

- workspace 76a9033b1360cb52a6842324ef84161861a081cf; patch-equivalent rebase of 742865d1 onto fetched master 5204ffad. `git range-diff` reports equality.
- extension 9d2ae65; focused skill policy and pinned skill validator pass.
- product 84d2fbe0607aa768b10a5acf5f6e952e423493c5; declared hook-enabled commit passes.

Known exact checks:

- Workspace focused Ruby:8 runs / 144 assertions, with 0 failures/errors/skips.
- Extension focused Ruby:5 runs / 72 assertions, with 0 failures/errors/skips.
- Skill validator in the extension-pinned Python/PyYAML environment:0, Skill is valid.
- Product policy commit: precommit Nixfmt0 and commit-message hooks0. Advisory72-column warnings; every message line is within 80.
- Revised owning guide: `nix develop --profile result/config-imports-dev-shell --command make doc`, exit0; MkDocs built in 1.10 seconds. Existing unrelated missing-nav notice `os/faulted-write-ci-handoff.md` remains. Guide diff whitespace0. Main agent applied the English user-facing writing skill after settling the facts.

Policy/check logs:instruction-workspace-tests.log/.status, instruction-skill-tests.log/.status, instruction-skill-validator.log/.status.
Technical persistence revision remains implementer-owned and in progress. No independent final review, final-head runtime acceptance, merge, package activation or KB publication is claimed by this checkpoint.
