# 2026-08-07-security-advisories-6-12-95-2

## Goal

Add vpsFree.cz platform security assessments for the 14 CVEs covered by the
vpsAdminOS 6.12.95.2 cumulative kernel live patch, validate them against
current production Node evidence, commit the reviewed per-Node evaluations,
and prepare matching unpublished vpsAdmin drafts.

## Affected repositories

- `security-advisories`: new advisory dossiers, analyses, evaluations, and
  draft submission baselines.

The Linux, vpsAdminOS, vpsAdmin, and vpsfree-cz-configuration repositories are
read-only evidence sources for upstream fixes, container reachability,
deployed kernel/live-patch state, and workload applicability.

## Approach

1. Verify each CVE against its primary record and upstream Linux fix, including
   mainline and stable introduction/fix boundaries.
2. Review current vpsAdmin, vpsAdminOS, and production configuration source for
   tenant reachability, relevant kernel options/sysctls, hardening, and Node
   role applicability.
3. Add one bilingual dossier and detailed analysis per CVE. Represent
   `6.12.95.2` as an accepted live patch only for the exact reviewed kernel
   source identity and patch version. For legacy reporters that omit the Linux
   source revision, require the exact reviewed booted vpsAdminOS revision with
   trusted, clean revision provenance.
4. Validate all dossiers, collect one coherent production evidence snapshot,
   evaluate every dossier, and resolve all unknown results.
5. Commit focused advisory changes with active Overcommit hooks, run the
   mandatory standalone change review, and address significant findings.
6. Dry-run vpsAdmin synchronization, apply only unpublished draft changes,
   commit the resulting submission baselines, and run read-only readiness
   checks. Do not publish and do not send email without separate explicit user
   approval.

## Compatibility and deployment

The repository changes are assessment data and unpublished draft preparation;
they do not change APIs, schemas, protocols, persistent runtime state, or
deployed configuration. Old and new vpsAdminOS versions may coexist: dossier
rules classify ordinary kernel versions independently and accept live patch
`6.12.95.2` only when its reported ID and version match the reviewed artifact
and either its kernel source revision matches exactly or a legacy reporter has
the exact reviewed booted vpsAdminOS revision with trusted, clean provenance.
Nodes without that exact mitigation remain affected or unknown rather than
being treated as fixed.

Draft synchronization uses revision preconditions and fresh evidence matching,
so concurrent remote review or Node-state drift stops the write. Rollback is
removal or correction of unpublished drafts and repository commits; no
publication or notification is authorized by this initiative.

## Testing plan

- Validate each dossier with `bin/security-advisory validate`.
- Run `bundle exec rubocop --parallel --force-exclusion` and `bundle exec rspec`
  from `nix develop`.
- Collect production evidence once and evaluate all 14 dossiers.
- Inspect evaluation completeness and require zero unknown/vulnerable current
  Nodes before draft preparation.
- Dry-run and then apply draft synchronization for each CVE, followed by
  `bin/security-advisory ready`.
