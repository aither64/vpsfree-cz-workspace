# Configuration pin and final history review

No findings in the assigned mechanical configuration and final-history scope.
Read-only review; no source edits, nested agents or long checks. Existing
substantive runtime reviews remain authoritative; the parent records direct
verification of the requested narrow manual-retry deferral under review step 9.

## Exact final ranges

| Repository | Base | Final head | Complete feature series |
| --- | --- | --- | --- |
| dev-workspace | `960dd816b7e56cbdd4af0da15bf0b26257775151` | `9baeea528f2e270332afa13786ec85a49a68e4c3` | `9baeea52` teams: observe active development progress independently |
| workspace | `0fe886f56031da55d16aa30e6f110243a0ed0e28` | `217c03753fdb878bab2cae260b354ee6844eb4c7` | `c2b4cef1` verification policy; `30b77268` observer defaults; `217c0375` runtime selection |
| vpsfree-cz-configuration | `270d348a29a832e552a798ba8bb467152a2d36d6` | `7eaaafd718809e16867c9b4614f9b2e2d54fa62a` | `7eaaafd7` generated devWorkspace pin |

The fixes remain folded into the one owning runtime commit. Workspace policy,
catalog/defaults and generated selection remain separately reviewable.
Configuration has one generated commit with the expected upstream changelog.
No obsolete feature approaches or fixup commits remain. There is one final pin
update per consumer; **no repeated update streams require consolidation**.
The packet records no intermediate deployment or external state boundary.
**No migrations**, including no transitional progress-state migrations.

## Consumer mapping and deployment

Independently compared parsed base/final lock objects. Workspace changes only
`nodes.dev-workspace`; configuration changes only `nodes.devWorkspace`. Both
select `aither64/dev-workspace` revision
`9baeea528f2e270332afa13786ec85a49a68e4c3`, content hash
`sha256-+LdcAFur520XEwX6PZaA4el5AdudEnDNQzyuZIbTeRw=`. Node input edges,
lock root/version, extension and all sibling nodes remain unchanged.

The existing configuration channel maps `dev-workspace/devWorkspace` to flake
input `devWorkspace`. Aitherdev consumes it for the host module and existing
Codex assembly helper. The runtime feature changes no Nix module, Codex assembly
implementation or native executable selection. The workspace still consumes the
runtime through its existing nested extension input and installs the application
through its user profile. No application package was added to system packages.

Existing site operations specify verifying system activation before selecting
the application when both are updated; application selection must use the final
composed workspace package so observer defaults and scheduler arrive together.
The parent records that the exact workspace/configuration deployment checker
passed. User authorization covers aitherdev deployment, **not default-branch
integration**. Ordinary deployment ownership, admission, recovery and fresh
pre-merge checks continue to apply.

## Evidence and remaining limits

Read configuration AGENTS.md, channel mapping, aitherdev consumers and operations
guide; inspected all final feature histories, configuration diff and final
consumer pin mapping. All three feature trees are clean; configuration
`git diff --check` passes. Runtime and workspace cleanliness/history were also
rechecked. No substantive runtime rereview was performed.

Composed package validation, system build/dry activation, and live health and
continuity checks remain deployment evidence to collect. Before activation,
prove the old/new native executable identities remain unchanged for both the
workspace and system packages. The pre-existing workspace 0.163/system 0.164
difference is not created by this pin and this review makes no new mixed-version
compatibility claim. No activation is established by this review.
