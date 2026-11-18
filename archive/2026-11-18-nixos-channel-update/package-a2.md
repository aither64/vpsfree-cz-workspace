# Package A2: adopt confctl in vpsFree.cz configuration

Owner implementer0. Prior C complete and accepted, capacity confirmed before A2.
Bound session/current environment and live workspace-write roster verified.
Lead owns plan/state, scope, review and integration. Architect0 owns D6.

Scope: generated confctl lock update only; exact source target
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`. Preserve nginx one-time revision
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, complete original `nixos-26.05`
tracking, sibling inputs and follows. No workflow text, deployment, source
feature, release or PR.

## Preparation

Existing same-session clean worktree/branch retained. Fresh configuration default
is `828c390c7e1857f11522933977afd852634b85f8`, equal to its merged prior package A
head. No merged history rewrite or rebase required. Nix-shell ff-only current
default reported already up to date; `bundle check` and Overcommit install passed.
Fresh fetched confctl upstream master equals exact required `d8ab7d4`. Channel
inventory confirms confctl is an unqualified root GitHub input, not owned by a
channel, currently locked to `ff5e0177`. Applicable unchanged workspace
procedures reused, repository AGENTS reread, deployment channel procedure
rechecked. D6 read in full and lead release received before pin generation.
Root update completed with generated useful changelog enabled.

All source, generated-commit, graph/tool/metadata verification and publication
evidence will stay here. A routine adoption needs no separate project docs:
confctl C owns the reusable behavior and its docs; this is individual adoption
evidence. Final base/head/series/no-migration and preservation proof follow.

## Generated change and quick proof

- New adoption base `828c390c7e1857f11522933977afd852634b85f8`, final head
  `bf19f6aacae7f57c8bd06746ff10481b242baf2f`.
- One new generated commit, `inputs: update confctl to d8ab7d4c`, `flake.lock`
  only, three insertions/three deletions. Existing merged package A history is
  retained unchanged; no rebase, obsolete attempt or consolidation needed.
- Exact root command: `nix develop --command confctl inputs update --commit confctl`.
  Useful generated message retained unchanged, including source changelog from
  `ff5e0177` to `d8ab7d4c` and its logical source commit.
- Required precommit Nixfmt passed; commit-message hooks passed with the ordinary
  generated TextWidth 72-column warning. `git diff --check` passed, source clean.
- Parsed graph assertions passed: node set/root edges identical; only the
  root-resolved confctl node's `locked.rev`, `locked.narHash`,
  `locked.lastModified` differ. Every full original object, nested dependency,
  sibling node and follows edge remains identical. `flake.nix` and workflows
  are byte-identical, with no other changed path.
- Adopted source is exact `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`, NAR hash
  `sha256-078svbFUIAjS3aZMN4XCkRwUAz0dJf/QtGqZwJxmUxM=`, timestamp 1795026729.
  Its original remains unqualified `{owner=vpsfreecz, repo=confctl, type=github}`.
- Root `nixpkgsStable` retains complete exact locked identity
  `4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, original `nixos-26.05`, NAR hash
  `sha256-zX+62p0XLF5AbMgzy8JgNBH6cTJSiDovTOSk2NBc0GQ=` and timestamp 1795018498.
- No migrations, schema/state format, original-ref, workflow, deployment or API
  change in the adoption diff. No repeated source-input update stream or
  superseded new commit remains. Previously merged nginx pin is preserved.

## Updated environment smoke

Read-only updated `nix develop` smoke passed exit 0. B2 held the single fresh
verification utility slot, so A2 used visible bounded-output parent monitoring.
Only the changed tool/dependency shell derivations built; no fleet/system build.
Exact commands: `command -v confctl`, `confctl inputs ls --json confctl`,
`confctl inputs channel ls`, machineNames length evaluation, confctl source path
evaluation. JSON reported exact new revision above; channel mappings unchanged,
110 machine metadata entries. Full log is disposable
`package-a2-raw/mapping-smoke.log`.

Selected tool `/nix/store/vcxb3mrqcr4yrglwf9fmv7q6gc2igviz-confctl/bin/confctl`
sets RUBYLIB and executes the source entrypoint from
`/nix/store/zh2jpdp1hcllnb761v1n61z2yykdkamq-source`, matching the newly locked
input's evaluated outPath. No actual update/daily workflow was used as a smoke
test. Source C's exact review, RSpec/RuboCop/matrix/integration evidence is reused
from package-c.md, without rerunning unchanged source or machine inventory.

Fresh pre-publication fetch still resolves default to the exact adoption base;
zero behind/one ahead and clean source. No broadened upstream revision selected.
Ordinary feature-only SSH push inside the pinned Nix environment succeeded.
Fresh `git ls-remote --heads origin refs/heads/2026-11-18-nixos-channel-update`
equals exact final `bf19f6aacae7f57c8bd06746ff10481b242baf2f`; source remains clean.
Comparison capture saved exact new adoption base/head. One bounded Actions API
read found no runs for this final head; no workflow dispatch was attempted.

Package ready for lead acceptance and independent mechanical-history conclusion.
Git/index/rebase/hook/publication window explicitly released to lead after exact
remote proof. All owned command sessions are quiescent. No default integration,
deployment, PR, machine reservation or lifecycle action performed.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/
