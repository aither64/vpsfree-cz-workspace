# Downstream risk and compatibility review

Reviewed the final downstream checkpoint at high risk in the mandatory
risk/compatibility lane:

- vpsAdmin `791ab3aa89e2f613979da6090b89785c78245db5..2a312616b0bf10465c33bbca97c79b31b22e8ec8`;
- vpsfree-cz-configuration `249bed1ee28e69a907edd09ea97a1144dbcdefeb..4145e961376f064bccd665b36a7f7ef02de66867`;
- vpsfree-kb-contracts `919577d0c770e47b623c591f8bf0cce4e8d30666..0770dcfae7834a43d8bc1a59f468aed037de2d80`;
- the prepared deployment, repair, and rollback procedure in `rollout.md`.

## Findings

### Important: `APPLY=1` is not bound to the separately reviewed preview

References:

- `rollout.md:67-92`
- vpsAdmin `2a312616b`,
  `api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:9-44`
- vpsAdmin `2a312616b`,
  `api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:148-155`

The procedure tells the operator to review every proposed event, interval, and
evidence ID, obtain separate approval, and then start a second invocation with
`APPLY=1`. Each invocation independently queries the current event IDs and
recomputes its proposals. The fingerprint recheck protects a proposal only
between inspection and writing inside that one invocation; it does not compare
the apply run with the earlier approved preview.

The supervisors are running during this separate preview/apply phase. A new
public or internal event snapshot can therefore appear after preview, or new
evidence can make an older event repairable. The apply invocation can then
tighten a row that was absent from the reviewed output. Its post-write output
does not restore prior authorization for that history change.

Bind apply to the reviewed proposal set and fingerprints, or quiesce all event
writers across an immediately adjacent preview and apply while also verifying
that the exact proposal output is unchanged. The former provides the stronger
audit boundary. Until then, a production repair approval must not be treated as
approval of the exact rows shown by the earlier preview.

### Important: the rollout does not prove the supervisor units remain masked

References:

- `rollout.md:10-23`
- `rollout.md:44-51`
- vpsfree-cz-configuration `4145e961`,
  `cluster/cz.vpsfree/vpsadmin/common/api.nix:70-87`
- vpsAdmin `2a312616b`, `nixos/modules/vpsadmin/supervisor.nix:116-145`

Both API hosts enable a supervisor unit wanted by `multi-user.target`, and the
new recorder can reference `last_confirmed_at` only after migration
`20260914120000`. The runbook correctly says that both writers must remain
masked through both application switches, but its only pre-switch check is
`systemctl is-active`. An inactive unit can still be unmasked and be started by
activation. There is also no mask check after switching API1 and before running
the migration.

This matters especially because the installed `confctl ssh` implementation
runs the command on every selected host and prints individual failures without
making the overall invocation fail. A partial `systemctl mask --now` failure can
therefore be followed by two apparently inactive units, one of which remains
eligible to restart during the API1 switch. That can start the new recorder
against the predecessor schema and lose the intended all-writers-paused
boundary.

Check both `UnitFileState` and `ActiveState` on both hosts after masking, require
runtime-masked and inactive results, and repeat that check after API1 activation
before migrating. Use host-labelled output and make deviation an explicit stop
condition. Apply the same per-host result scrutiny when unmasking, restarting,
and checking final health.

### Advisory: the future deployment commands do not assert the reviewed pin

References:

- `rollout.md:3-6`
- vpsfree-cz-configuration `4145e961`, `flake.lock`

The configuration and build under review are exact, but the runbook only says
to run from the session worktree. It does not check that the future rollout is
still at configuration commit `4145e961376f064bccd665b36a7f7ef02de66867`,
that the tracked tree is clean, or that `vpsadminServices` still resolves to
`2a312616b0bf10465c33bbca97c79b31b22e8ec8`. Since the session and feature
branches intentionally remain open, later work can otherwise change what the
same commands deploy. Add exact revision, cleanliness, and lock-pin assertions
before the build/deploy commands, with the configuration revision replaced only
by a separately reviewed and approved successor.

### Advisory: node 400 may not provide the required stable confirmation check

References:

- `rollout.md:53-64`
- `rollout.md:75-81`

The prose calls for inspecting a node with a complete stable report, but the
command fixes `Node.find(400)`, and the same document warns that node 400 may be
incomplete or legacy-ambiguous. A null confirmation on that node therefore does
not distinguish a compatible conservative result from failure of the deployed
recorder. Parameterize this check and select at least one known complete stable
baseline; retain node 400 as the separate repair target.

## Pin and compatibility checks

No pin-diff finding was found. The configuration commit changes only the
`vpsadminServices` lock entry from the stated base to the exact pushed vpsAdmin
head. `vpsadminStaging`, `vpsadminProduction`, and all three vpsAdminOS inputs
remain unchanged. The channel maps role `vpsadmin` to `vpsadminServices`, and
the recorded inventory contains the expected 11 consumers.

The KB contract commit changes the exact vpsAdmin revision in its five canonical
files. Comparing all locked revisions confirms that the vpsAdminOS and transitive
runtime pins are identical to the base; the canonical check passed with no
content or capture drift.

The schema migration itself is additive and nullable without a default or
backfill. The first-API/migration/second-API ordering is compatible once the
writer-mask finding above is resolved. Old application packages can operate
with the retained column, and the documented rollback correctly keeps both the
column and evidence-supported repairs. No node rollout, reboot, or vpsAdminOS
change is required.

Consumer builds and the two long integration runs were still in progress at
this review checkpoint. Production rows were not inspected, so retained
evidence may legitimately yield no node 400 proposal. Those are validation and
evidence limits rather than additional compatibility findings.
