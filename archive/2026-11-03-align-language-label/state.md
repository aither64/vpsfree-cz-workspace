---
lifecycle: archived
---

# Align the HaveAPI documentation Language label

## Status
Phase: merged and verified; previews remain running.
Remote haveapi/master is the exact reviewed/previewed final feature head
b606b4b3c32bf05779c05babeaa1c31a33dee6fa. User confirmed visual alignment
on port4567 and explicitly said "confirmed, merge the changes" on 2026-11-04.
Session and both preview services remain open/running. No production deployment.

## Phase checklist
- [x] Scope and bounded implementation (implementer0)
- [x] Quick checks and focused commit
- [x] Independent final review (reviewer0; no findings)
- [x] Feature publication and nine exact-head CI workflows passed
- [x] Interactive preview and user visual acceptance
- [x] Approved fast-forward integration and remote proof
- [x] Merge claim released and resulting state verified
- [x] Final CI metadata inspection and temporary target cleanup
- [ ] Production deployment (not requested)

## Repository, history and review
Repository git@github.com:vpsfreecz/haveapi.git, target master.
Feature branch 2026-11-03-align-language-label, worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-align-language-label/haveapi.
Reviewed base f29c1e4675bc1f79641faa619b8c68ecec923c71; exact final head
b606b4b3c32bf05779c05babeaa1c31a33dee6fa. One commit,
servers/ruby: align documentation language label; one CSS insertion/deletion.
No rebase, history change, obsolete approaches, repeated update streams or
migrations. Final range unchanged from independent final review. Comparison
captured publicly before merge. Feature branches/worktree retained.

[Implementation evidence](implementation-result.md): stronger scoped Language
label selector and margin: 0 0 .4rem resolve generic sidebar margin override.
make doc, nine language-settings examples, RuboCop206 files, range diff check
and all mandatory hooks passed. No markup/JS/prose/translation changes.
No project documentation update useful for a cosmetic margin correction.
[Setup evidence](nix-prepare-result.md) records fresh Luna/low Nix preparation.

[Review packet](review-packet.md), [independent review](review-result.md):
reviewer0 thread01a1a353-d493-7b52-8e6d-210d4955431c, saved
gpt-6.1-sol/xhigh, read_only, general and architecture/repetition lanes, low risk,
no findings. Explicit whole-history/no-migrations/no-update-stream conclusions.
[Feature publication](publication-result.md) and [CI report](ci-watch-result.md):
all nine exact-head workflows passed on first attempt including server/performance.

## Integration approval and execution
Explicit user direction after preview confirmation: "confirmed, merge the changes".
Scope: HaveAPI remote master only. [Integration record](integration-result.md).
Implementer0 prepared clean detached haveapi-merge-target from fresh base and
verified hooks outside claims. Lead independently checked full range and diff.

Claim70e016a6-dc27-4acf-b4bc-1bf864762e48 briefly waited, then authoritative
status verified held. Fresh target/feature/cleanliness check matched reviewed
range. Ordinary git merge --ff-only passed with hooks; SSH push
HEAD:refs/heads/master succeeded. ls-remote proved remote master exactly
b606b4b3c32bf05779c05babeaa1c31a33dee6fa. No uncertain mutations.
Claim explicitly released and authoritative resulting state released verified
at12:23:19Z before records/CI/cleanup. No machine reservation or deployment.

Workspace CLI in project Nix shell failed before claim mutation due Ruby JSON
extension/GLIBC mismatch from inherited project gems. Coordination CLI ran
successfully from ordinary workspace shell; Git/hooks stayed in prepared Nix
shell. [Reusable lesson](../../notes/haveapi/2026-11-04-workspace-cli-ruby-environment.md).

## Preview and access
[Preview record](preview-result.md). Current user-confirmed reachable URL:
http://172.16.106.40:4567/v1.0/?doc_lang=en
Managed service e60a076c-4d7d-4b97-ad97-46b03edf019e. Original service
1fd4affd-9359-4f0e-b32a-cbbfc2ef5b92 remains on18761. Both use existing
in-memory test API from exact fixed worktree; no production data/credentials.
Page/health/CSS200, CSS exactly matches reviewed stylesheet SHA256
5d9a9bf0ccd821921c81552c5048e6b5f28477e6f4486e93d7feae16d4059542.

Port18761 was blocked for user; no supported HTTPS forwarding found. Prior
claim that only SSH/ingress changes could provide access was too broad.
User supplied known accessible4567; it was free, so second managed service
started there without firewall/proxy/source/env changes. User confirmed alignment.
No preview service stop or session lifecycle action authorized.

## Ownership and next action
Implementer0 (saved workspace_write, gpt-6.1-sol/xhigh) finished temporary target
cleanup and CI metadata inspection. Lead owns tracking/acceptance. Fresh remote
proof confirmed both master and retained feature ref at exact final head.
Master push triggered the same nine checks on the same SHA: six passed at final
inspection, three still running (server RSpec41828804935, Rust41828805104,
performance41828804918); no failures or additional master-only checks. Existing
nine successful exact-head results remain verification evidence. No redundant
watcher/test campaign started. Clean detached target was removed using Git after
confirming no process/preview used it; feature checkout and branches retained.
No new test campaign needed for unchanged exact commit. Production deployment not requested.
Leave session active while running previews remain owned; do not stop/archive.
Initial tracking committed aa94433b2; subsequent tracking follows normal cadence.
External screenshot stays outside version control.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-align-language-label/)
