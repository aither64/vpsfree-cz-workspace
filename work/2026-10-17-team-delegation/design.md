# Team delegation design and verification brief

## Ownership and scope

This thread owns implementation because the new initiative was created without
a Codex roster. Runtime, site policy, docs and matching deployment pins are in
scope. No existing session prompt or member is reconfigured.

## Catalog and creation contract

Schema 5 adds optional team-level `initial_member_counts`, an object mapping
existing non-lead catalog role names to positive integer counts. Omitted roles
have one member. Unknown roles, lead counts, null/noninteger values, counts
above 63 and expanded totals above 63 specialists are invalid. A count-bearing
team must fit max_open_agents. Schema 4 forbids this field and keeps its exact
existing digest and interpretation. Nix accepts both input versions; Go accepts
both installed catalog and metadata versions. New site configuration emits 5.

Sorted role names expand into contiguous canonical zero-based addresses. Keep
designer -> architect mapping and one native role policy per role, not per
member. Creation member/role lists remain the saved authoritative selection.
All Go/Ruby receipt and preset validators check contiguous indices per role,
including interleaved roles, and reject duplicates, gaps and noncanonical
spellings. ApplyPresetSpec stores the actual index. Existing manual add/fork
logic already supports numbered members; verify it with repeated-role creation.

The site's Full team uses implementer count 2 and max_open_agents 4; native child
capacity stays 4 because direct team threads require no native capacity. The
legacy unmanaged Full-team recipe remains unchanged so preceding interrupted
reservations keep their exact retry path. Other preset composition is unchanged.
Fresh selection acceptance bounds the serialized creating-journal envelope,
including JSON escaping, a maximum filesystem-length slug and trailing newline,
against the existing 64 KiB limit. The writer checks its exact encoded record
before publication. Retained snapshots keep their existing readers and limits.

## Coordination policy

Full-team lead performs initial scoping, routing, acceptance inspection, session
tracking, approval-bound coordination and user communication. Architect owns
substantive investigation/design and independent implementation boundaries.
Implementers own bounded end-to-end packages, diagnosis, source/tests/technical
docs, quick checks, commits and review fixes. The lead maintains a small owner,
dependency and acceptance backlog and assigns useful independent work to both
implementers. Serialize overlapping edits and staging/commits; do not duplicate
specialist investigation or take over blocked assignments. Short coordination
steps are permitted; dependent implementation remains delegated. Lead-designed
keeps lead-owned design. With no implementation members, the lead implements;
temporarily unavailable members do not qualify for that fallback. Long checks
retain the separate utility watcher and independent review retains its gates.

## Compatibility, deployment and recovery

No roster/creation receipt field change or database migration. Both old and new
single-member selections remain readable by the new runtime, with saved settings
unchanged. Old binaries reject new repeated-role creation receipts; recovery is
forward-only. Existing forks/retries preserve their saved lineup, even after
catalog change. No API client generation, service protocol or node update is
needed. Publish runtime before selecting its exact feature revision in the
workspace nested override and configuration dev-workspace channel. Preserve the
extension revision and other inputs. Verify paired locks, deploy aitherdev under
its coordinator reservation, then select the composed application user profile.
No master integration has been authorized. Retain generations, branches and logs.

## Acceptance and checks

- New Full team has lead, architect0, implementer0, implementer1, reviewer0 with
  existing role policy and settings; portal count/summary reports five/two.
- Both managed and unmanaged creation store index 1 correctly, retries reuse
  exact identities, forks preserve them, and subsequent add chooses index 2.
- Every receipt reader rejects gaps, duplicates and malformed addresses and
  accepts old receipts and the expanded selection; schema-4 digest stays stable.
- All four mode prompts and workspace guidance agree on ownership and review.
- Quick: focused Go catalog/runtime/web/lead-policy tests, Ruby receipt tests,
  instruction tests and Nix evaluation/format checks. Commit and independently
  review final history and compatibility before long packaged checks.
- Longer: packaged catalog/site policy and affected Go/Ruby suites; paired-pin
  deployment check, composed package build, scoped aitherdev build/dry activation,
  guarded deployment and member creation/assignment smoke check.
