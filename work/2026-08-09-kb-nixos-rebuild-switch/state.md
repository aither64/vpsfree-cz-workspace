# 2026-08-09-kb-nixos-rebuild-switch

## Repositories

- Coordination workspace: shared `master` checkout
  `/home/aither/workspace/ai/vpsfree.cz`; only files under this initiative's
  `work/2026-08-09-kb-nixos-rebuild-switch/` are in scope.
- vpsadmin-kb-captures: workflow and validator used at `fe07bdf`; no code
  changes. The clean validation worktree was removed after publication. Local
  branch `2026-08-09-kb-nixos-rebuild-switch` is retained at `fe07bdf`.

## Status

- Complete. Both reviewed pages are published and verified in production,
  staging ownership is released, and the validation worktree is removed.

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
- After explicit user approval, verified production identity and ACL 255 on
  `navody:distribuce:nixos` and `manuals:distributions:nixos`.
- Restaged, verified, promoted with `--approved-production`, and
  production-verified the Czech manifest, followed by the English manifest.
- Read both production pages directly, compared their SHA-256 digests with the
  reviewed candidates, and inspected rendered HTTPS pages and language links.
- Confirmed staging had no pending release, then ran `bin/kb-stage release
  --yes` and removed the clean validation worktree with `bin/dev-session
  worktree remove`.

## Results

- Verified initiative isolation: `2026-08-09-kb-nixos-rebuild-switch`.
- Production publication was explicitly approved by the user on 2026-08-09.
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
- Both production pages return HTTP 200 and render
  `nixos-rebuild switch --flake /etc/nixos#vps`.
- Production page content matches the reviewed candidate hashes exactly:
  Czech `05712001f24afe6fd00430d3f4f64cf4da2ba401fec512e3bb6cdc5f864e3ca4`
  and English
  `946181f0540d4c8f1a219992f9dae65f38bd22cf1cb1350acfe02fb02bcf7fd8`.
- Both rendered production pages link Czech `navody:distribuce:nixos` and
  English `manuals:distributions:nixos` bidirectionally.
- Production URLs:
  - `https://kb.vpsfree.cz/navody/distribuce/nixos`
  - `https://kb.vpsfree.org/manuals/distributions/nixos`
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
- Decision: continue without candidate changes. Production promotion was
  subsequently completed and verified after explicit approval. No separate
  manual browser visual inspection was performed; API, HTML, command text,
  HTTP status, checksums, and bidirectional language links were verified
  programmatically.

## Open questions

- None currently.

## Cleanup

- Staging ownership released with retained mirror data; container is down and
  `pending_release` is null.
- Clean `vpsadmin-kb-captures` validation worktree removed. Its local feature
  branch remains at `fe07bdf` as required.
