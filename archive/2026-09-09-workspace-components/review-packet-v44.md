# Mandatory change review packet v44

## Review target

This is the final focused rerun for the aitherdev deployment boundary after
reconciling review v43. Review the exact pushed heads below; concentrate on the
forward-only cutover changes in workspace commits
`120de27e384987e042c1b9424da20418cd0d56fe..8d7bfb46b4342110cd568a50f1288ef1eebae4d6`.

| Component | Base | Exact pushed head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `4b3d426d0484a62bac5bcfc7d5c7b6ff2140b045` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `3e3f0ff7c2d23f08f19887822efa12f969bbb56f` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `8d7bfb46b4342110cd568a50f1288ef1eebae4d6` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `6956ff4197d36e731084b3167b0d5e76b5003583` |

The workspace is explicitly authorized for fast-forward integration to
`master`. The configuration branch is deployed from its feature worktree and
must remain unmerged. Other component default branches are outside this
integration action. The site procedure is forward-only; the operator has
explicitly accepted stopping old sessions, resetting development clusters and
resolving any deployment fault in place.

## Review v43 reconciliation

- Admission now validates exact source commits and clean package-relevant
  trees. The reviewed workspace commit is supplied to `prepare`, persisted and
  rechecked by all phases.
- The live-state gate now proves authoritative tracking lifecycle, manifest
  phase, lifecycle journals, exact thread identity/materialization, all ten
  old authorities, nine recreated sessions, three dormant active tracking
  records and the exact cluster inventory before its first mutation.
- Old tmux sessions are stopped through exact audited authority records. The
  recorded tmux session ID, slug, and identity where available must match
  before the session is killed. No legacy preservation/restart loop remains.
- `prepare` and `forward` are stage-resumable. State replacement fsyncs both
  the file and parent directory. Existing migration journals provide the
  component-level replay contract.
- A runtime systemd condition holds the router closed across both nested
  `workspace-host switch` calls. `forward` never opens admission. `accept`
  performs local authority, conversation, environment, command and credential
  gates first; TLS and authenticated HTTPS failure close admission again.
- Credential, CA, TLS, auth and password trees are inventoried through the
  restricted root SSH path before mutation and compared after host migration,
  configuration activation and immediately before admission.
- The final process scan inspects user-process environments for legacy
  variables and namespace paths, in addition to command-line checks.
- Automated site rollback was removed by explicit operator decision. The
  reusable organization-private migration primitive retains its tested reverse
  direction for other consumers, but this aitherdev procedure neither invokes
  nor validates rollback.

## Verification already complete

- Workspace Bash syntax and ShellCheck pass.
- Workspace cutover contract: 9 runs / 90 assertions, no failures or errors.
- Component test suites and no-build flake evaluations passed at their exact
  heads as recorded in packet v43. No further long build repetition is planned
  before deployment.

## Lane focus and response contract

Risk is **High** because the procedure changes persistent user/root namespace
state and activates a NixOS configuration. Run the required General,
Architecture, Scope and Risk lanes from fresh context with `gpt-5.6-sol` at
`xhigh`. Report findings only when concrete and actionable, classified as
Blocking, Important or Advisory with exact file/line evidence. State `clean`
when the lane has no such finding. Do not request redundant long validation or
re-litigate the explicitly accepted forward-only/no-process-preservation site
policy.
