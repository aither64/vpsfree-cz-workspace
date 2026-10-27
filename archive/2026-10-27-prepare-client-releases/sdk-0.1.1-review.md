# SDK 0.1.1 final review

No Blocking, Important or Advisory findings. The source/configuration review gate passes for `4689d00ca4acf0cc26a3507fc3c238b687b53475`. Full CI, explicit main integration approval and actual OIDC publication remain pending.

## Scope and reviewed history

Reviewed general, scope/proportionality and risk/compatibility under mandatory-change-review. Reused the unchanged 0.1.0 substantive-content review and independently inspected the complete final series/diff and new settings. Operational risk is high because publication persists and GitHub authorization settings are live; no new implementation/workflow logic warrants an architecture lane.

Canonical repository/target: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`, main. Base `149c72f11acef67224a47ed77711a3abb805fbd4` equals the merge base against the retained origin/main ref. Complete series:

1. `38a25ad88d0bf3018670184620cf69cdb71e92e7`: first public 0.1.0 preparation.
2. `4689d00ca4acf0cc26a3507fc3c238b687b53475`: prepare 0.1.1 for trusted npm publication.

The new commit changes four metadata files, +5/-5: package and both root-lock versions, their bound digest and the README installation literal. The cumulative seven-file diff is +81/-18. The result and recorded short preparation milestones match the added user request; static native GitHub settings implement existing documented prerequisites without a new framework or speculative hardening.

**History/consolidation conclusion:** no obsolete approaches, superseded fixes or unused compatibility paths remain. The package-version/root-lock/digest stream updates twice for a valid boundary: 0.1.0 is actually published, and 0.1.1 is the final candidate. A fresh public npm read confirms publication at 2026-10-27T17:40:04.673Z and integrity matching the retained receipt bound to exact source `38a25ad8`. That exact consumed source must remain; it is not a redundant intermediate pin. There are no dependency upgrades or other repeated update streams. 0.1.1 is not yet public. **No migrations**, including transitional migration lineage.

## Source and GitHub configuration assessment

The final lock SHA256 `949ca1c8a761e9ca73d6562f7a0542ff3f0d1c2d5a79a0628083d44029cf7ab6` matches tools/generator.json. Runtime haveapi-client@0.30.2, generator 18b45aed, schema/provenance/generated source, license, toolchain, helper and workflow remain unchanged. No public API, protocol, persisted-state or compatibility change is introduced. The clean checkout is one commit ahead of the published feature branch. Existing six release tests and focused metadata checks are recorded as passing; no tests/builds were run during review.

Independent live read-only GitHub GETs confirmed the receipt:
- Release environment `25494232596`: sole required reviewer aither64/User `4717906`, self-review allowed, custom deployment policies.
- Sole deployment policy `64571929`: `v*`, type tag.
- NPM_RELEASE_ENABLED is exact string `true`.
- Sole active tag ruleset `25982494`: refs/tags/v*, no exclusions, creation-only restriction and sole RepositoryRole 5/admin bypass, always. Caller aither64 is admin and current_user_can_bypass is always.

This provides the intended tag-creation and protected-approval path. No extra update/deletion/signing/status rules were added.

The actual unchanged workflow gates publishing on canonical-repository pushed tags, successful build and the release environment. Only the protected publish job has id-token:write. Preflight requires exact version/tag/package/license/lock identity and ancestry on main. Publishing downloads the immutable build artifact by ID, verifies its receipt and uploads that exact tarball with scripts disabled. There is no stored npm credential, token fallback, rebuild or repack in the publish job.

The native settings are a conventional completion of documented release prerequisites. Their exact empty-baseline/resource IDs and restoration limits are recorded in sdk-trusted-publishing.md. GitHub readback cannot prove the private npm publisher's account fields or OIDC acceptance. The authorized 0.1.1 tagged run must establish that; do not substitute manual-token publication if it fails.

## Boundaries and identity

Source/settings review is complete. Next are canonical full CI/artifact acceptance, explicit SDK/main approval, short-claim integration and remote proof, then the authorized v0.1.1 protected release and registry-integrity/provenance verification. Preserve original artifacts and reconcile uncertain uploads before retrying the failed publish job. No main integration or protected approval is inferred here.

Session current/environment binding and live retained reviewer0 identity matched: thread 01a17e59-3823-76f0-9764-5525072525a2, gpt-6.1-sol/xhigh/read_only, unchanged settings, no fallback. Read packet, setup receipt, appended design, relevant source/guidance and selected references; reused unchanged applicable procedures. No writes, builds, tests, nested agents, claims, merges, tags or publication performed. Report returned to the lead for saving as sdk-0.1.1-review.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
