# Execution backlog

See [design](design.md) for exact file boundaries, contracts, invariants and
acceptance checks. The user authorized autonomous implementation, SDK changes
through its generator, and periodic rebasing; no merge/publication/deployment.

| Package | Owner | State | Dependencies / next evidence |
| --- | --- | --- | --- |
| G generator | implementer0 | Source done, focused checks pass; broader unit running | Commit exact head, mandatory review before actual-runtime integrations |
| S schema/SDK | implementer1 | Two byte-identical full exports; package/consumer source prepared | G committed head, SDK dependencies, regenerated candidate |
| W shared policy | implementer2 | Read-only diagnosis done; dependencies installed | Actual S archive and G contract; RequestSpec executor / zero-call checks |
| VPS/storage | implementer3 | Prepared, source hold | W pilot; list/start and output narrowing |
| Networking/DNS | implementer4 | Prepared, source hold | W pilot; network describe and input-contract dispositions |
| Users/settings | implementer5 | Prepared, source hold | W/S; nullable date and TOTP/settings route conclusions |
| Infra/operations | implementer6 | Prepared, source hold | W/S; node static/live boundary, advisory observed revisions |
| Finance/content | implementer7 | Prepared, source hold | W/S; shared public models, null language, outage/payment contracts |

Architect owns bounded API-source disposition, not an unrelated backend repair
campaign. Generated contracts must not be widened to excuse unsupported inputs.
Domain owners own direct consumer fixes and focused regression cases; no local
protocol decoder or fabricated required values. Lead serializes Git operations
and shared edits. Every upstream refresh rescans new custom call sites.

Long checks: fresh Luna/low utility, one batch at a time. Source input capture
and dependency preparation are complete/underway separately from final runtime
integration. Default-branch integration, npm publication, release tags and
machine deployment remain separate explicit actions. Session stays open.
