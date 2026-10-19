# Independent final review

Reviewed `dev-workspace` base `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03`
through head `a373216d5c4f78fa8930e351e5f60204f2584b9c`.
The runtime reader correction appears sound. The packaged acceptance suite must
be corrected before its long integration run: the current driver has guaranteed
contract mismatches as well as assertions that can pass without proving the
accepted behavior. This review does not establish deployment or merge readiness.

All findings below concern commit `a373216d5c4f78fa8930e351e5f60204f2584b9c`.
Paths are relative to the runtime repository unless stated otherwise.

## Blocking

1. **Solo roster proof treats a supported null member list as an array.**
   `nix/tests/session-creation.nix:169` calls `len(saved["members"])`, and
   line 173 iterates that value. A new `Roster` has a nil `Members` slice
   (`portal/internal/teamruntime/runtime.go:742`), and `ApplyPresetSpec` only
   appends actual members (line 1061). The solo preset therefore retains nil;
   the list command encodes the roster directly (`portal/cmd/workspace-portal/main.go:519`),
   producing `"members": null`. The first successful solo creation reaches a
   Python `TypeError` instead of passing its proof. Normalize this documented
   empty representation to an empty list inside the test, while preserving
   strict checks of the roster identity and the expected member count.
   Lane: general.

2. **Fork and approved-plan navigation expects a field their status does not return.**
   `test/creation_acceptance_browser.cjs:77` unconditionally waits for
   `origin + record.canonicalUrl`. New preparations return that field, but
   ordinary slug-based creation statuses used by fork/plan return `url` and
   only populate `canonicalUrl` for a conflict
   (`portal/internal/web/creation_store.go:98`). A ready fork/plan consequently
   waits for a URL ending in `undefined`. Resolve the expected same-origin
   destination according to the two existing endpoint contracts, validate it
   against the returned slug, and retain the actual browser navigation check.
   Lane: general.

3. **The fork proof requires a ready journal that the successful workflow deletes.**
   `nix/tests/session-creation.nix:156` reads `<slug>.fork.json` and requires
   `state == "ready"`. Fork journals only allow the creating state
   (`libexec/dev-session:4318`); normal successful fork writes completion
   evidence and deletes that journal (`libexec/dev-session:1642`). Even after
   correcting navigation, the fork scenario must fail on `cat`. Check the
   fork's real retained receipt/completion evidence, manifest and native
   identities, and require absence of the temporary fork journal. Keep the
   ready creation-journal assertion for new and plan sessions. Do not change
   the product's fork lifecycle to satisfy the test.
   Lanes: general, architecture, risk.

## Important

4. **The post-send interruption can use a stale barrier from the previous scenario.**
   `test/creation_transport.py:35` writes the global `send-accepted` marker
   for every successful proxied `turn/start`. The preceding `before` scenario
   completes both its initial turn and follow-up through that proxy. Nothing
   removes the marker before `nix/tests/session-creation.nix:263` waits on it
   for `after`. The wait therefore succeeds immediately and may kill the
   portal before the new initial send is accepted. A green retry would prove
   a different recovery boundary. Use a fresh barrier for each scenario and
   bind its observation to the intended root/initial request and accepted turn
   identity. A marker for any unrelated turn must not satisfy the wait.
   Lanes: general, architecture, risk.

5. **Follow-up success is not tied to the submitted turn.**
   `test/creation_acceptance_browser.cjs:67` accepts a user marker plus any
   two previous `CREATION_REPLY_` entries. A fork already contains the source's
   initial answer and follow-up answer. Merely persisting its new user message
   therefore passes even if that turn never finishes or fails. Locate exactly
   one newly submitted user marker, require an assistant sentinel in that same
   `turnId`, and require completion for that turn. Check the expected provider
   suffix as well. The parent's proposed same-turn/completed-status fix directly
   addresses this finding.
   Lanes: general, risk.

6. **Attachment checks stop at upload storage and portal presentation.**
   `nix/tests/session-creation.nix:214` checks the transcript for the filename
   and searches the upload store for its bytes. Neither check establishes that
   the initial native/model request received the attachment reference. The
   synthetic provider returns the same answer regardless of attachment input,
   and the independent native proof checks only the textual initial marker.
   Dropping attachment expansion before native submission could leave these
   assertions green. Check the exact attachment reference in the native initial
   user item or its captured external Responses input, bind it to this request,
   and verify the referenced file has the fixture bytes. Existing captured
   provider requests are sufficient; this does not require a product test hook
   or an autonomous model tool call.
   Lanes: general, scope.

7. **The accepted multiple-member case contains only one retained member.**
   `nix/tests/session-creation.nix:46` defines just `reviewer0` alongside the
   root. This is a two-agent team, but it does not exercise creation of multiple
   retained members or detect one native identity being reused for two members.
   The accepted handoff explicitly asks for solo/multi-member teams and unique
   root/member identities. The smallest existing-catalog adjustment is
   `initial_member_counts.reviewer = 2` and `max_open_agents = 2`; schema 6
   already supports this and the declared capacity of 4 suffices. Expect and
   independently inspect `reviewer0` and `reviewer1` in the team scenarios.
   No new production role, abstraction or session team is needed. If the lead
   instead interprets the accepted wording as root plus one member, record
   that decision and the untested multiple-retained-member boundary explicitly.
   Lanes: general, scope, architecture.

## Advisory and residual verification limits

No separate advisory code findings. The recorded model/effort/instruction
assertions establish captured roster settings; root model/effort also have a
transcript assertion. They do not demonstrate that an idle member executes an
assignment under those instructions. That additional behavior is outside the
stated creation/follow-up acceptance and need not expand this change.

The suite has not run. After the corrections, the authorized watcher must run
the actual packaged VM acceptance and preserve any failed-run diagnostics.
The old-reader experiment must fail at runtime on the journal rejection. Since
the new Go contract test accesses `CreationJournal.Provider`, simply reverting
the production file can fail compilation; package unit-test failure also does
not prove a whole-process regression. Use a diagnostic old-reader package that
can actually reach the browser scenario, retaining stock native Codex. Record
the exact negative-control source and observed terminal failure. The deployed
default/alternate provider, team, fork and plan creation/follow-up checks remain
mandatory before the user's conditional integrations and reservation release.

## Whole-branch history, migrations and consolidation

Inspected the complete two-commit series and final diff, not only the latest
commit:

- `98ae6b38b2830b612f68d3d5a84f96c1d7caf5ca`: optional provider reader correction
  and real Ruby-producer/Go-consumer regression.
- `a373216d5c4f78fa8930e351e5f60204f2584b9c`: packaged creation acceptance,
  fixture helpers, flake export, mandatory CI and corresponding documentation.

The split is coherent. Tests and documentation support their owning behavior;
the workflow action patch alignment accompanies the edited workflow under the
workspace's current-action requirement. No obsolete unmerged implementation,
transitional reader, follow-up fixup commit or abandoned approach remains.
Narrow driver corrections should be folded into the acceptance commit.

**No migrations.** Persisted schema versions remain 1/2/3 and the Ruby writer
already emits the optional field. There is no intermediate migration lineage to
retain or consolidate. The packet records no merge, release, deployment or
external consumption of these two commits; nothing in the reviewed series
contradicts that provenance.

**No repeated dependency or generated-pin update streams.** There is one
workflow-action revision update, and no flake lock or consumer pin change in
this range. The later workspace/configuration streams remain separate work.
The merge base equals the supplied base and `git diff --check` passes. The
runtime worktree was clean throughout review.

## Lane and compatibility conclusions

General: the production fix is narrowly matched to the demonstrated bug; the
acceptance defects above prevent accepting the larger deliverable yet.

Architecture/repetition: the shared `agentteams` reader is the correct owner.
It reuses the existing provider identifier validator without importing mutable
provider discovery. The test uses real form routes, initializer, native service
and receipt paths; its finite helper split is proportionate. Correct the driver
to the existing endpoint and journal contracts instead of broadening product
interfaces. The transport barrier may remain transparent and test-only.

Scope: no native Codex patch/rebuild, product hook, speculative framework or
new team is introduced. The requested fixture corrections fit the accepted
whole-process boundary.

Risk/compatibility: absent providers keep inheritance; syntactically valid
providers no longer need current catalog membership just to decode persisted
state. Unknown, duplicate, malformed and cross-schema fields remain rejected.
The Ruby and Go identifier syntax agrees. Existing schema-1/2/3 and
creating/ready cases are exercised by the real producer contract. Rollback to
the broken reader still cannot read explicit-provider journals, accurately
documented in `docs/session-preparations.md`. No new remote-input authority,
credential exposure or destructive runtime behavior was found.

The actual workspace consumer pins the generic runtime through the extension's
nested override at this review base; the extension calls the generic
`lib.mkPackage`. The generic runtime owns the parser and its portal consumers.
Deferred host/profile pins must preserve that composition and the recorded
system-then-application rollout order. This runtime review does not certify
those future pin commits or any prepared activation.

Reviewer: standalone `/root/creation_final_review`, selected catalog fallback
`gpt-6-astra` / `xhigh`, catalog digest
`ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`.
Verified the exact bound session with `dev-session current` and both environment
markers; the live roster is null. Read the mandatory review skill and all four
lane references, workspace/repository instructions and applicable routed
guidance, packet, plan, design, state and handoff. Source inspection only;
no VM, long test, deployment, integration, lifecycle action or nested agent.
Only this requested report was written. The lead owns remediation acceptance.
