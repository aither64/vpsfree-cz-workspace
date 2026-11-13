# Final review packet

## Scope, identity and acceptance

Session 2026-11-13-osctld-start-recovery-errors. User requests actionable start diagnostics, concrete read-only July comparison and a safe shutdown/reboot race proposal. No lifecycle rewrite, integration, deployment or old-session mutation/contact. [plan](plan.md), [state](state.md), architect [design](design.md), [incident](incident.md), [July comparison](july-comparison.md), [race evidence](race-evidence.md), [contract/check inventory](contracts-checks.md).

Affected repository: vpsadminos, canonical repos/vpsadminos.git; own worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctld-start-recovery-errors/vpsadminos, branch 2026-11-13-osctld-start-recovery-errors, target staging. Exact base c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62; exact head 45086fb34ebc2bf7ad6a965b27c286c580ce44cb. Full base-to-head series is one commit:

- 45086fb34ebc2bf7ad6a965b27c286c580ce44cb osctld: explain container start admission failures

Review complete series and final diff using git log/show/diff at these exact revisions. 8 files, +293/-31. One logical change includes daemon reason selection, CLI delivery, operator manual and regressions because together they make the existing rejection actionable across ordinary/foreground entry points. No superseded approaches, dependency/input/pin/generated update streams, transitional compatibility layers or migrations. **No migrations** were created, deployed, merged, released or externally consumed. Initial message-only commit 35bab705d was amended before publication to fix wrapping; source tree unchanged. No feature deployment/publication yet. Metadata refresh was empty.

## Behavior and constraints

Keep five-gate Boolean result and short-circuit order, guard before force/no-op and every Start side effect. Container shares one blocker decision with read-only nil/String reason. Recovery reason uses available taint/interface identity records; it cannot claim a historical cause or live-link proof. Conditional full cleanup advice names safely shell-quoted pool/ID; absent ownership acknowledgment retains all stopped/no-init, both-name-and-index, IFB and shared-owner refusals. No netlink/ZFS/LXC probe, mutation, taint clearing or cleanup policy changes in diagnostics.

Normal Restart and custom Boot preserve the common failed message. Foreground start/restart/boot close/wait/restore terminal before raising existing Client::Error, with GLI failure exit/message. Existing raw console and queued/autostart acknowledgement semantics remain bounded as documented. Boot's earlier preparation/stop effects and guest --reboot path are not changed.

The public error envelope remains status:false/message:String. No YAML/runtime schema, hook protocol, CLI options, Nix module, API/client generator or configuration pin change. Node-by-node userspace update and ordinary rollback remain compatible. vpsadmin consumer inventory at 2d0946c4e699aa61092228d8a7cb275477ee46d0 found no parsing of old literal; representative nodectld shells osctl -j and records exit/output. Other external scripts could depend on free-form wording. No fleet update coordination or deployment authorized.

Race implementation is explicitly proposal only. Review evidence/claims for scope and fidelity as context, without demanding future proposal mechanisms be implemented here. Earlier DB.add alone, unconditional taint/link clearing, guessed reboot, and importing July reducer are rejected. Exact incident hook response/initiator not proved. July refs/functions/tests and old recorded CI are distinguished from independently rerun checks.

## Quick verification and documentation

Implementer0 owns complete A and follow-up fixes; architect owns D. Lead read final source/man diff and directly applied vpsfree-user-facing-writing plus English Humanizer before commit. Final disabled-pool advice corrected to status/import/export logs (no enable CLI). Lead verified full series, stat and diff --check. All intended substantive edits committed; tracked tree clean, only .native/ generated ruby-lxc test extension untracked.

Executed `nix develop --command bash /tmp/2026-11-13-osctld-start-recovery-errors-quick-checks.sh` in repository root; inspected script/log. Root declared shell with isolated session GEM_HOME/GEM_PATH/BUNDLE_PATH, per-component BUNDLE_GEMFILE, built libosctl/osctld/ruby-lxc native inputs. Script runs:

- osctld: bundle exec rspec -I spec spec/osctld/container_spec.rb spec/osctld/commands/container/lifecycle_spec.rb spec/osctld/commands/container/start_spec.rb spec/osctld/container/recovery_spec.rb spec/osctld/net_interface/veth_spec.rb spec/osctld/commands/container/recovery_and_send_spec.rb spec/osctld/generic/client_handler_spec.rb — 236 examples, 0 failures, seed 21837.
- osctl: bundle exec rspec -I spec --require spec_helper spec/osctl/client_spec.rb spec/osctl/cli/container_spec.rb — 40 examples, 0 failures, seed 3380.
- osctl: bundle exec rake md2man:man — exit 0; rendered new manual paragraphs inspected.

Log /tmp/2026-11-13-osctld-start-recovery-errors-focused-checks-final.log. Initial focused failures were fixture/assertion issues, fixed before this passing final run; no suppressed failures. RuboCop explicit pass; declared Overcommit signed/installed normally and final hook-enabled commit passed Nixfmt/RuboCop/commit-message checks. `nix develop --command make osctl osctld .` passed (77s) and produced no metadata diff. Full suites/VM/CI not run yet; required longer checks follow this review using fresh monitoring utility.

Documentation routing/fidelity:

| Topic | Reader/class | Authoritative home | Evidence/limit |
| --- | --- | --- | --- |
| Start gates/error and conditional recovery | Operators/reference and recovery how-to | osctl/man/man8/osctl.8.md existing start/recover sections; normal osctl man entry point | Render passed; preserves strict forget selectors/live-reuse refusal and distinguishes read-only from reconciliation |
| Diagnostic implementation invariants | Maintainers/source reference | Container blocker/reason and Start/foreground source comments | Existing docs entry point links osctl/man; no new documentation subsystem needed |
| July source/test comparison and current incident explanation | Session developer/investigation | july-comparison.md and race-evidence.md | Exact refs/functions/tests; no reproduction/July test rerun claimed |
| Future terminal-intent/admission reconciliation | Future developer/proposal | design.md | Explicit authority/launch/legacy/Stop/downgrade blockers; not released or deployed |
| Ruby ABI preparation workaround | Developers/reusable environment lesson | notes/vpsadminos/2026-11-13-isolated-ruby-gems.md | Same-session preparation evidence; no shared-cache deletion or dependency changes |

## Independent reviewer

High risk because this touches node admission/recovery guidance and a public CLI/API failure path, despite unchanged safety policy. Lanes: general; architecture/repetition; scope/proportionality; risk/compatibility. Lead read all four references. Retained reviewer0 verified eligible/ready/independent, read_only, gpt-6.1-sol/xhigh, thread 01a1d707-8aee-7940-bdb3-d35f482eb249. No overrides/fallback.

Read mandatory-change-review skill and all four lane references, applicable repository guidance, user scope, complete commit series/final diff, relevant tests and docs. Stay read-only, no nested reviewers or builds. Report concrete findings ordered Blocking/Important/Advisory, residual gaps and explicit whole-branch history, repeated-stream, no-migration and documentation placement/preservation conclusions. Save final report in this session's review-result.md and use report_to_lead. Lead will reconcile findings before longer checks. Do not infer integration/deployment approval.

## Narrow remediation receipt
Final head 25101c51e893c480f083c1812f07d3b1d3788a62, same base. Independent review of 45086fb and its whole branch is preserved in review-result.md. R1/R2 fixed by implementer0 and directly inspected/verified by lead under skill step 9; no design/public-contract expansion, no rerun needed. Final one-commit series +349/-31 (8 files), no migrations/repeated streams. Two-file old-to-final source delta adds socket shutdown before parent close and real fork/socket regressions. Old code failed 3 timeouts, fixed 3 passed; final affected CLI/client/Console 49 examples pass and RuboCop/hooks clean. Exact logs/results in state. All daemon/manual files and dependency manifests identical to reviewed range. Narrative validation added to amended owner message for R2. Final feature is not yet published/tested in VM at this receipt.
