# Final B/D feature publication

Published only after the frozen affected final review passed all four lanes with
no findings. Fresh SSH fetch/default/feature checks matched the reviewed ranges;
no rebase or source change was needed. Source-bound details, observation times,
review/log hashes, push order, CI inventories and clean status are in
[package-final-publication.json](package-final-publication.json).

| Repository | Exact published feature head | Publication |
| --- | --- | --- |
| confctl | `bdaed19e901237e05bd0a779f368e76cb311143f` | Ordinary fast-forward from reviewed 7ba, before consumers |
| vpsfree-cz-configuration | `7b0609cf41fc9fe54b6d09129246ff100fb4197a` | Exact lease against prior `f5bf3f026210d30c0b9b219aac47ff6490e4cddc` |
| vpsadminos-org-configuration | `4352f16fb967e3b9da829972c9799157badd0494` | Exact lease against prior `30ea016491f78d88037508e3a7e9c9a20d50511b` |

All use SSH `git@github.com:vpsfreecz/<project>.git` and feature ref
`refs/heads/2026-10-24-flake-update-downgrade-guard-replacement`. Fresh post-push
remote queries returned every exact head. Defaults remain the original reviewed
bases: confctl `cc40679d267165aecfa569128438bb55fe910268`, vpsFree
`50d263d4127c05163d660fae1c4b9b887584032d`, org
`6b04b48e9c076e5525ccb7c38ce174232414f0b5`. All three worktrees remain clean.

Pushes ran in each repository's declared development shell with active ordinary
pre-push hooks; no bypass or repository claim was used. Logs:
[provider](package-b-final-push.log), [vpsFree](package-d-final-push-vpsfree.log),
[org](package-d-final-push-org.log). Provider publication and exact remote proof
were reported immediately to root and C before consumer publication.

Same-branch CI inventories contained no superseded queued/in-progress runs, so
no cancellation was needed. Current-head CI was left untouched. This is a
point-in-time inventory, not completed CI evidence. No CI was awaited and no
local package/runtime/long verification was launched by the publisher.

The accepted source histories remain two coherent provider commits and one
adoption per D repository. Original guard/review/source ranges, failed attempts,
invalid negative-control evidence and owned candidate links remain preserved.
No migration, configuration runtime input change, default integration, release,
machine action, deployment or session lifecycle action occurred.

Root now owns serialized final-P startup/exported RSpec and all seven real
nonpublishing patterns, race and Terraform VM verification. B/D retain diagnosis
and follow-up ownership. Prepared commands remain in
[package-b-final-rspec.md](package-b-final-rspec.md) and
[package-d-live-checks-final.md](package-d-live-checks-final.md); their final
verification has not been inferred from publication or precommit checks.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
