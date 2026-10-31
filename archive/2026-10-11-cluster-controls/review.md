# Independent final review: cluster controls

## Findings

**Important — General: the existing cluster rendering test fails after the
toolbar change.** In `dev-workspace`,
`portal/internal/web/server_test.go:1899` still requires
`class="cluster-footer"`, but commit
`74b2dc1079610182e8dde8b8cf81dc555152484c` removes that footer from
`portal/internal/web/templates/clusters.html` and moves Release to the toolbar.
The quick-check selection omitted
`TestSessionPageGroupsClusterServicesAndRepositoryRevisionState`, so its green
result does not establish that the changed template passes its existing tests.
The package suite will fail on this assertion.

Reproduced from the runtime worktree with:

```sh
nix develop --command go -C portal test -mod=readonly ./internal/web \
  -run '^TestSessionPageGroupsClusterServicesAndRepositoryRevisionState$' -count=1
```

Result: exit 1, `server_test.go:1904: session page lacks
"class=\"cluster-footer\""`; package execution took 0.081 seconds. Replace the
obsolete assertion with the intended toolbar/Release markers, include this
rendering test in focused verification, and fold the correction into the owning
unmerged toolbar commit. The lead acknowledged this correction; it was not yet
applied to the reviewed heads.

No Blocking findings or additional Important findings were identified.

## Reviewed scope and reviewer policy

Reviewed all four lanes directly: general, architecture and repetition, scope
and proportionality, and risk and compatibility. No nested agents or application
edits were used. The only reviewer-authored artifact is this report.

High risk is appropriate because the work adds browser entry points for VM
operations, exposes credential controls, and spans provider/runtime contracts
and deployment pins. The review used the repository trust boundary: the local
workspace operator administers the host, while remote clients remain untrusted.

The installed catalog's default development team is `lead_reviewed`; its
review-purpose role `reviewer` selects `gpt-6-astra`, `xhigh`, `read_only`, and
fresh context. The catalog and matching TOML identify
`dw_34bb6a768d6175719d13cda28b7adc221b586314b3fc5167` at
`/home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/agent-teams/lead_reviewed/reviewer-xhigh.toml`.
These configured values were checked directly. The lead attested that the
actual `/root/final_review` launch used `fork_turns: none`,
`model: gpt-6-astra`, and `reasoning_effort: xhigh`. The collaboration API does
not expose a custom native-role selector or read-only permission profile; the
role instructions and read-only application scope were supplied in the task.
Therefore this is a verified catalog-policy fallback and launch attestation,
not a claim that the native custom role was loaded or permissions were enforced
by the tool sandbox. The fallback reason is the session's unavailable retained
roster, as recorded in the packet.

Read the packet, plan, design, current state, rollout record, root and repository
instructions, applicable routed procedures, the mandatory-review skill and all
four lane references. Inspected actual Git history, final diffs, adjacent
provider/lifecycle/HTTP/process-group code, tests, owning documentation, and
consumer pins. All four feature worktrees were clean at review time.

## Whole-branch history and migration conclusion

| Repository | Base | Reviewed final head | Complete series after base |
| --- | --- | --- | --- |
| dev-workspace | `a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0` | `74b2dc1079610182e8dde8b8cf81dc555152484c` | `1c83d28` credential controls; `74b2dc1` cluster toolbar/control contract |
| vpsfree-dev-workspace | `3e5dc4681b0343ec236c3f3dfc0d6f725577c376` | `7157c8098dcf60127aa4df823fab82b4185ad22a` | `7157c80` retained Start and provider permissions |
| workspace | `0c82757629b48cef93df2c98677c07f5a9ba5059` | `72a2876bdefd6e64796fddd1047920716428af06` | `1deacf09` initial tracking; `72a2876` composition pins |
| vpsfree-cz-configuration | `decd92fe3926a4a4304c15957b05cc095948f8cc` | `04039ba97fbbdb56911a40e3b31e0994cbebda7d` | `04039ba9` matching host runtime pin |

The merge bases and heads match the packet. The complete series introduces the
final design directly; no superseded functional approaches, fixup chains,
obsolete compatibility paths, or intermediate pin updates remain. The initial
workspace tracking commit is separate from functional changes. Tests and docs
remain with their owning behavior; using one browser fixture to exercise both
requested controls is a reasonable integration-test grouping.

Each dependency update stream has one final update. The workspace directly pins
the intended extension and nested generic runtime; configuration selects the
same runtime revision and content hash. Sibling inputs and follows paths are
unchanged. The extension bump also includes upstream `3e5dc46`, whose complete
diff changes review-procedure documentation only. Generated configuration
commit-message width is an allowed repository exception.

**No migrations.** The final diffs add no database migration, persistent state
format, schema conversion, or transitional migration lineage. There are no new
migration versions with merge, release, deployment, or external-use provenance
to preserve. Per the packet and prepared rollout record, these feature changes
had not yet been deployed.

## Lane conclusions

- **General:** the implementation matches visible Start/Stop plus separate
  destructive Release, normal retained Start, aligned Reveal/Copy controls,
  and refresh without page reload. Error rendering uses text, and credential
  feedback names fields rather than values. The confirmed stale test assertion
  above must be reconciled. Owning feature documentation is discoverable;
  rollout details remain in initiative records.
- **Architecture and repetition:** generic portal code owns the status/HTTP
  contract; provider helpers own state selection, VM operations, and maintenance
  policy. The shared shell runtime owns action serialization and retained
  selection for both actual providers. Configured immutable provider commands
  prevent browser-selected commands or paths. No harmful new duplication or
  misplaced abstraction was found.
- **Scope and proportionality:** the change stays within retained-cluster
  controls. It reuses existing process-group cancellation, lifecycle locks,
  provider start/stop/reset operations, and template/copy infrastructure.
  First-time creation, force, topology editing, and maintenance recovery remain
  outside this interface. No speculative framework or abandoned mechanism was
  found.
- **Risk and compatibility:** new readers opt in to `actions`; old helpers
  omit it and retain Release-only behavior, while new helpers leave ordinary
  status JSON unchanged for old readers. Explicit empty actions disable all
  controls; busy/unavailable observations disable cached permissions. POST
  routes retain origin, generation, runtime and lifecycle admission. Fresh
  provider permissions, per-session/provider reservations, and native helper
  locks cover overlapping mutations. Retained selection is read under lock and
  refuses missing state/configuration/selection; ordinary source and
  maintenance checks remain authoritative. Stop/Start reuse existing disk
  semantics; Release is explicitly destructive. Archive's unconditional reset
  path retains ordinary locking. No coordinated update of developed nodes is
  introduced.

## Verification limits and next gate

Inspected the successful focused Go/Ruby/JavaScript/shell checks in
`quick-checks-3.log`; independently reproduced the rendering failure above.
No long tests, browser runs, cluster operations, deployments, or approval actions
were performed by this reviewer.

The new HTTP test proves overlapping-request refusal and browser-disconnect
survival. Shared process-group deadline coverage exists, but the new cluster
HTTP path does not directly test server shutdown/cancellation. Provider tests
exercise retained selection, missing prerequisites, maintenance action metadata,
and disk-content preservation on failed build; successful Stop/Start VM disk
retention still needs the planned known-file comparison. Real browser layout,
package checks, and composed deployment remain unexecuted at this review gate.

The rollout correctly records forward-only workspace package recovery: repeat
the candidate switch or select a newer compatible package. Retaining an old
source/generation for diagnosis does not authorize an unsupported backward
profile switch. A timed-out Start may leave its deliberately detached runner
active; the owning documentation explains refreshed status and Stop recovery.

After the narrow test correction and focused verification, the lead may proceed
under the mandatory-review remediation rules without another full review.
Update downstream pins and record the new exact heads if the owning commit is
amended. This report does not establish package/browser/live-deployment
readiness or authorize default-branch integration.
