# Manual API deployment handoff

## Preparation status

Ready for user deployment. Both remote master branches contain the exact
reviewed/tested revisions, integrated by fast-forward after all 27 API Specs
jobs passed at f9. Integration CI was not awaited. No production or dry
activation was performed by the agent; session and feature refs remain open.

- [API](https://github.com/vpsfreecz/vpsadmin/commit/f9beb46e5206864bca9d37672e1419cf03661467):
  f9beb46e5206864bca9d37672e1419cf03661467.
- [Configuration](https://github.com/vpsfreecz/vpsfree-cz-configuration/commit/074b62fe4ca99bcb6e0b2cd186e43f039c666b36):
  074b62fe4ca99bcb6e0b2cd186e43f039c666b36.
- Retained feature branches: 2026-10-03-newadmin-exception.
- Channel/role: vpsadmin / vpsadmin -> vpsadminServices.
- Previous API pin: a65a4dfeb92a59df4a80a737a20bcbf8558793ff.
- Pre-integration configuration base: 7e32833aca1cb65902b50f61eb76dd1022691591.
- Targets: cz.vpsfree/vpsadmin/int.api1 and int.api2.

Final exact-tree builds passed in 119 seconds, generation 2026-10-03--22-46-01.
Both records select f9 and contain built switch scripts.
[Build result](configuration-updated-build-result.json),
[actual outputs](configuration-updated-outputs.json),
[Specs success](api-specs-60m-completion-result.json),
[integration proof](integration-result.json). Earlier generations are historical.

| Target | Built system |
| --- | --- |
| API1 | /nix/store/fp8zdihv05jha9kj3ziyg1qm21xg88y1-nixos-system-api1-26.05.20261002.774debe |
| API2 | /nix/store/249gzy475w9hxcsnm81b12wzjghw65p5-nixos-system-api2-26.05.20261002.774debe |

## Operator steps

Use the exact final configuration revision in an
operator-owned checkout or the retained session worktree. Both repositories
retain feature branch 2026-10-03-newadmin-exception after master integration.
Enter the configuration's declared environment with `nix develop`.

```sh
confctl inputs channel ls vpsadmin
confctl ls 'cz.vpsfree/vpsadmin/int.api[12]'
```

Confirm services revision f9beb46e and exactly the two API targets. In a separate
checkout, build that same configuration revision locally before deployment:

```sh
confctl build --yes 'cz.vpsfree/vpsadmin/int.api[12]'
```

When ready, the user can deploy incrementally:

```sh
confctl deploy --one-by-one 'cz.vpsfree/vpsadmin/int.api[12]'
```

After both workers update, verify normal WebUI access for affected users returning
after inactivity. A valid OAuth session linked to a tokenless SSO should
authenticate without recreating SSO. Watch for recurrence of nil.valid_to;
old workers may still raise until replaced. No WebUI update, migration, data
repair or forced reauthentication is required.

See [verification](verification.md), [independent review](review.md) and
[configuration report](configuration-result.md). Local persisted regressions
passed 72 examples. These checks do not establish production activation,
precise production cleanup chronology or a concurrent scheduling experiment.

## Recovery

Retain the actual previous deployment generation before activation. Prefer
restoring that generation over reverting unrelated configuration updates.
Rollback loads existing state: schema and token format are unchanged. Restoring
the old API pin/configuration generation restores the original exception and
requires no database conversion. Do not recreate deleted SSO tokens as a repair.

The channel has additional service consumers and the WebUI API follow link.
Scoped builds and recommended rollout cover API1/API2; broader service rollout
is an operator decision. Deployment and rollback execution remain user-owned.
