# 2026-08-09-kb-nixos-rebuild-switch

## Repositories

- Coordination workspace: shared `master` checkout
  `/home/aither/workspace/ai/vpsfree.cz`; only files under this initiative's
  `work/2026-08-09-kb-nixos-rebuild-switch/` are in scope.
- vpsadmin-kb-captures: workflow consulted at bare repository `HEAD`; no code
  changes expected; validation worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-09-kb-nixos-rebuild-switch/vpsadmin-kb-captures`
  on branch `2026-08-09-kb-nixos-rebuild-switch`, based on `fe07bdf`.

## Status

- Staging is prepared and verified for both languages. Mandatory standalone
  review passed without findings. The candidates are ready for human review;
  production has not been changed and still requires explicit approval.

## Commands run

- `bin/dev-session current` (verified current slug matches
  `VPSFREE_DEV_SESSION_SLUG`)
- Inspected shared workspace status without modifying unrelated changes.
- Read `vpsadmin-kb-captures` `AGENTS.md` and
  `docs/webui-change-workflow.md` from the canonical bare repository.
- Inspected the KB contract/release tooling and content-replacement format.
- Verified production API identity as `aither` for Czech and English wikis.
- `bin/kb-contract-fetch --output
  work/2026-08-09-kb-nixos-rebuild-switch/kb-sources`
- Searched all fetched pages for case-insensitive `nixos-rebuild`, independent
  `--flake` usage, and command lines without a recognized action.
- Created the initiative `vpsadmin-kb-captures` validation worktree after
  fetching its SSH remote.
- `bin/kb-contract-build --source .../kb-sources --plan
  .../kb-replacement-plan.yml --output .../kb-candidates`
- `ruby .../vpsadmin-kb-captures/tools/check-kb-annotations.rb
  --source-index .../kb-sources/index.json --candidate-index
  .../kb-candidates/index.json`
- Reviewed the changed-page list, exact unified diffs, and generated
  `kb-candidates/review.md`.
- Generated `kb-release-cs.yml` with summary `Doplnit akci switch do příkazu
  nixos-rebuild` and `kb-release-en.yml` with summary `Add the switch action to
  the nixos-rebuild command`.
- `bin/kb-stage status`, `bin/kb-stage start`, and
  `bin/kb-stage reset --yes`.
- Staged and verified the Czech manifest, then staged and verified the English
  manifest; verified both manifests again after both page sets were present.
- Read both staging pages through `bin/kb-page get`, compared their SHA-256
  digests to the manifests, and inspected rendered HTML and language links with
  `curl`.
- Verified all 186 source/candidate pairs against their index hashes and
  asserted that the changed set contains exactly the two intended pages.
- Read both production pages again after staging; their hashes and original
  commands still match the guarded sources.

## Results

- Verified initiative isolation: `2026-08-09-kb-nixos-rebuild-switch`.
- Production writes are out of scope until explicit user approval.
- Fetched 116 Czech and 70 English production pages.
- The only executable commands missing an action are the paired NixOS overview
  pages `navody:distribuce:nixos` and `manuals:distributions:nixos`, each with
  one `nixos-rebuild --flake /etc/nixos#vps` occurrence.
- All other executable uses already specify `switch` or `boot`. Bare
  `nixos-rebuild` mentions in the userdata pages name the command or its output
  log and are not invocations.
- Candidate validation passed: 2 changed pages, 2 guarded content replacements,
  65 valid navigation bindings, and 9 valid exceptions. Exact diffs contain one
  insertion of `switch` per affected page and no other content changes.
- Czech candidate SHA-256:
  `05712001f24afe6fd00430d3f4f64cf4da2ba401fec512e3bb6cdc5f864e3ca4`.
- English candidate SHA-256:
  `946181f0540d4c8f1a219992f9dae65f38bd22cf1cb1350acfe02fb02bcf7fd8`.
- Staging was reset from 116 Czech pages, 70 English pages, 58 language pairs,
  and 224 shared media objects, then both one-page releases were applied.
- Both staging pages return HTTP 200 and render
  `nixos-rebuild switch --flake /etc/nixos#vps`.
- Both rendered pages link Czech `navody:distribuce:nixos` and English
  `manuals:distributions:nixos` bidirectionally.
- Review URLs:
  - `http://kb-cs.aitherdev.int.vpsfree.cz/navody/distribuce/nixos`
  - `http://kb-en.aitherdev.int.vpsfree.cz/manuals/distributions/nixos`
- The English release is the current pending manifest, digest
  `5c75e6e26091b226f870d8bb66fd6ee17a7a213455f27274c1bc9beb0aff2101`.
  Staging the second language replaces only the pending-promotion record; both
  languages remain staged and independently verify against their manifests.
- A workspace-wide `git diff --check` reports trailing whitespace and a
  conflict-marker-like DokuWiki line inherited from production in the complete
  byte-for-byte source/candidate snapshots. These bytes cannot be normalized
  without breaking source fidelity and release checksums. The authored files
  and the two changed page diffs are clean.

## Mandatory change review

- Standalone fresh-context review completed for coordination commit `af13032`
  against base `d64eb76`.
- Blocking findings: none.
- Important findings: none.
- Advisory findings: none.
- The reviewer independently fetched production and matched all 116 Czech and
  70 English committed sources, verified all 186 source/candidate hashes and
  the exact two-page change set, checked both staging manifests and rendered
  pages, and confirmed that production remains unchanged.
- The reviewer accepted the single commit because the inventory, replacement
  plan, candidates, manifests, and tracking form one integrity-bound staging
  packet.
- Decision: continue without candidate changes. Residual gaps are the
  intentionally untested production promotion and lack of a separate manual
  browser visual inspection; API, HTML, command text, HTTP status, checksums,
  and bidirectional language links were verified programmatically.

## Open questions

- None currently.

## Cleanup

- Release the staging claim after production promotion or explicit abandonment;
  retain it while the staged review is pending.
- Remove the clean `vpsadmin-kb-captures` validation worktree after this
  initiative is published or abandoned; keep its branch as required.
