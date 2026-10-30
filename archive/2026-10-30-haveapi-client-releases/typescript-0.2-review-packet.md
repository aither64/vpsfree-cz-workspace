# TypeScript 0.2.0 affected final review

User correction: generated formatting changes qualify for the requested client
minor release. The earlier no-release decision is superseded; its original
review/CI/artifact receipts remain historical evidence. Lead supplied final
release prose and reports explicit user approval for the named integrations
and publications. Lead owns those operations after review and artifact gates;
this packet concerns the bounded TypeScript release preparation only.

## Exact complete final range

Repository `vpsfreecz/vpsadmin-typescript-client`, target `main`, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/vpsadmin-typescript-client`.
Branch `2026-10-30-haveapi-client-releases`.

- Base: `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`.
- Previously reviewed/pushed head: `d14ee69953d0664b4b6d96d7b8f2a3ede4383d88`.
- New final head: `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
- Complete series:
  1. `d14ee69953d0664b4b6d96d7b8f2a3ede4383d88` — Refresh offline generation for HaveAPI 0.32.
  2. `e5786f69b7c223c3bb5b1de99b7f97186eec368a` — Prepare version 0.2.0 for the generated formatting update.
- New delta: seven files, +14/-10. Full base-to-head: 687 files, +57561/-19326;
  the large generated formatting delta remains exactly the previously reviewed
  bytes. Tree/index clean and final comparison captured.
- No migrations. No obsolete dependency/input resolutions or repeated version
  updates: formatter dependency/tooling belongs to the first coherent commit;
  the second adds the one requested 0.2.0 release identity and notes. Its lock
  changes affect only the two root package-version fields, with no dependency
  graph change. Separate generated/tooling and release-metadata commits follow
  the lead's explicit conventional release-boundary brief. No new intermediate
  source pin or obsolete compatibility path was introduced.

## Bounded implementation and evidence

- `package.json` and both root `package-lock.json` version fields are 0.2.0.
  Registry latest remains 0.1.1; 0.2.0 and remote v0.2.0 were absent at preflight.
- Only `tools/generator.json`'s bound package-lock SHA256 changes, to
  `da67cb3a5430a26f86b9df6b912d14e66214f1d8239fd1a35446bb6c61e62e15`.
  Every other generator field remains equal to reviewed d14ee699.
- HaveAPI `0e7166a0f8f15827bfac051666a53bf449e999ec`, generated code/manifest,
  all three schema inputs, formatter config/version, shared source identities,
  regeneration tooling, toolchain and flake are byte-identical to reviewed head.
  No rerendering was done. Runtime peer/dev remains exactly 0.30.2; dev-only
  Prettier remains exactly 3.9.10.
- Root `CHANGELOG.md` describes the formatting-only release and unchanged API,
  public types and runtime behavior. README install version is 0.2.0. Existing
  development/release guides receive only lead-approved stale-version wording
  corrections; historical bootstrap instructions and commands remain intact.
  Lead applied the required writing skills directly before supplying final prose.
- Original four-lane review, 674/674 formatter equivalence and actual npm 0.1.1
  baseline proofs remain in [original packet](typescript-review-packet.md),
  [correspondence](typescript-metadata-correspondence.md), and
  [preparation](typescript-preparation.md). Do not repeat unchanged provider CI
  or source-equivalence investigation. Acknowledge the release-eligibility
  correction without treating semantic equivalence as a reason to skip 0.2.0.

## Quick checks and execution incident

Fresh pinned-policy standalone Luna/low utility, explicit full access/never
approval, ran [quick batch](typescript-release-quick-command.sh). The **first
execution passed exit 0 in 38.345 seconds**: locked npm install, exact-source
offline `--check`, build, typecheck, strict consumer typecheck and ten unit/release
tests, zero failures. JSON comparisons independently prove version-only package
changes and the one corresponding digest update. `git diff --check` passed.
No declared repository hook framework/AGENTS.md/hooksPath exists; commit ran
inside the repository's pinned Nix environment.

The utility failed to create its requested separate log, then violated its
no-retry brief while attempting to capture that log: it launched a redundant
batch and interrupted it after 11.997 seconds during read-only `--check`.
Parent reconciled effects: no running operation remains; all generated/source/
schema/tool inputs remain byte-identical to d14ee699 and only intended metadata/
docs changed. The first successful run's full raw output and the separate
interruption are retained in [launcher log](typescript-release-quick-watcher.log),
with candid [utility report](typescript-release-quick-report.md). No additional
duplicate rerun was used solely to manufacture a missing log.

## Remaining gate

Use retained reviewer0 with saved settings for affected final history, scope,
metadata, documentation and package-identity review. Preserve prior lane results
for unchanged code. Require explicit complete-series/no-migrations/no-repeated-
streams conclusions. Push remains held because it starts longer package CI.

After accepted review, publish the exact feature head over SSH and let a fresh
watcher collect its own 0.2.0 CI archive/receipt and extracted consumer validation.
The earlier d14ee699 0.1.1 artifact cannot be a 0.2.0 publication candidate.
No default merge, tag, npm publication or publisher mutation is performed by this
owner; lead coordinates approved integration/publication and final HaveAPI
publication correspondence.
