# Independent consumer refresh review

**No findings.** The committed consumer refresh is accepted for the exact ranges
below. It preserves the accepted archive selection and the upstream shared-login
authentication correction. This is source/history acceptance; exact-generation
verification and coordinated deployment remain with the lead.

Reviewer: `/root/archive_final_review`, retained catalog `gpt-6-astra` / `xhigh`.
This bounded follow-up covers the general and risk/compatibility lanes. The
earlier reports remain unchanged. The reviewer performed read-only Git, source,
lockfile and evidence inspection, and wrote only this report. No tests, builds,
deployment, integration, source edits or nested agents were launched.

## Exact final series

| Consumer | Base | Head | Complete ordered feature series |
| --- | --- | --- | --- |
| workspace | `4344bbe5c4b5490c1ed16c457f888c711619ba4f` | `2145891816cf88d2a648ace32018e975e810afda` | `ad62b06e9fcff0dba1818ae3eeff6a53c378b22a` documentation; `2145891816cf88d2a648ace32018e975e810afda` runtime selection |
| vpsfree-cz-configuration | `aed7d5071e24793d7bd811af11ccfa80e6f049d6` | `cf0c0d5b1d980c668b8d5bd588f644ef1b53afcb` | `cf0c0d5b1d980c668b8d5bd588f644ef1b53afcb` generated runtime selection |

Both worktrees were clean at these heads. Their actual logs and merge bases
match `refresh-heads.json`; each recorded base is an ancestor of its final head.
The complete diffs contain only the lifecycle procedure and runtime selection in
the workspace, and the `devWorkspace` lock node in configuration.

There is exactly one runtime-pin commit per consumer. No repeated update stream,
obsolete unmerged approach, redundant replay or separate remediation commit
remains. The documentation and pin have independently reviewable purposes. The
configuration message retains confctl's generated old/new revisions and runtime
changelog. Already integrated upstream history is preserved.

## Preservation and compatibility

- Workspace lifecycle commit `ad62b06e` has the same stable patch ID as accepted
  `078e8c88`: `6405695e88d0127f51501e3398f0042dff0c1973`. It retains local
  completion, independent tracking retries, supervised browser execution,
  revival/coalescing and legacy synchronous-journal guidance. All workspace
  files outside coordination records and notes are identical to accepted head
  `ec7fcf142a77b1e0c976db0f1f907aedc42672e6`.
- The skills composition now comes from upstream `7ce778f0`. The final
  `flake.nix` retains the merge with `previous.extensions.skills` and the local
  `update-codex` addition. It also retains the direct nested runtime override;
  no top-level substitute or extension-lock rewrite was introduced.
- Each consumer's complete lockfile is identical to its previously accepted
  lockfile. Against the new bases, only workspace node `dev-workspace` and
  configuration node `devWorkspace` change. Both select
  `b8fc991417720b9f354140c25d038df12912e2fd`, with hash
  `sha256-unRRjgA2me8t+5lnZ3sr+lKdPKzToT/Ifh2Q2Myv1kg=`. Input edges/follows and
  unrelated locked identities are preserved. Extension
  `767dfd587e346168e1443e65ccdb67ce748f3fe3` and codex-web
  `a0561fad8decb794117f8959fa2dd629547c5ba7` remain selected.
- Configuration's former provider replay is now inherited through upstream
  `9721c331`. Its additional upstream correction `aed7d507` is preserved
  byte-for-byte in `cluster/cz.vpsfree/machines/aitherdev/config.nix`,
  `docs/operations/codex-deepseek-aitherdev.md` and
  `skills/update-aitherdev-codex/SKILL.md`. Those three files are the only tree
  differences from accepted configuration head
  `88b16e5a6603aa5340b6d46196796208ccac77de`.
- The DeepSeek wrapper still exports `DEEPSEEK_API_KEY`, and the provider still
  uses that `env_key`. The profile no longer sets `forced_login_method = "api"`,
  which could reject/remove the shared ChatGPT login before provider startup.
  The removed obsolete profile fields remain absent. The operational guidance
  retains the corresponding authentication boundary and isolated-probe rule.
  Refreshing the archive pin therefore does not restore the known harmful login
  restriction or overwrite the deployed correction.
- The configuration channel remains `dev-workspace` / `devWorkspace`; its host
  module and assembled system Codex use that input. The workspace application
  remains a separate user-profile package. Matching runtime selection and the
  existing system-before-profile activation order are preserved.

**No migrations in either consumer range.** This refresh adds no schema,
journal, receipt, recovery format, protocol or compatibility shim. Runtime HEAD
is still `b8fc991417720b9f354140c25d038df12912e2fd`; its two archive commits now
follow integrated base `3c57e2ea`. The earlier reviewed format lineage and
legacy-reader/package-capability conclusions remain applicable. No intermediate
migration for an abandoned branch iteration remains to consolidate.

## Evidence continuity and remaining gates

The original reports accept the runtime history and format lineage after R1–R4
remediation. R5's exact narrow type-check/full-copy fallback was directly
verified by the lead as permitted in the follow-up report; the retained log
records 2 runs / 58 assertions, including the symlink-placeholder case. This
consumer refresh does not reopen or change that runtime behavior.

The packet and state retain successful runtime CI/flake checks, recovery
regressions, real-manager survival and scale acceptance. Those are earlier
verification results, not tests rerun by this reviewer. Reuse of consumer build
results still requires the lead's exact derivation/input comparison; source
equivalence alone is insufficient, especially for workspace checks that include
tracking content and the configuration generation that embeds `self.rev`.

Proceed with that comparison and the required exact configuration build. Before
admission, reconcile any further upstream or deployed changes so the eventual
candidate preserves intervening work. Existing aitherdev reservations, package
generation fences, forward recovery and live acceptance remain required. This
review grants neither reservation bypass nor default-branch integration approval.
