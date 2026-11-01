# Default-aware documentation specs: final affected review

Committed and quick-green; **STOPPED before native services-up and publication**.

Repository `vpsadmin`, worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-default-api-specs`, branch `2026-10-24-vpsadmin-haveapi-upgrade-default-api-specs`. New range `33d6c7723b392c828de2165854d106d9528f9305..a089b530376ca645456597df6a3533f720d24670`, final tree `812f360630ae61a9de37a5dc657bdc6a9ac24e20`. One test-only commit; exactly two paths, +45/-26. Source is clean; effective and packaged full lock SHA256 remains `ea0a24b176bd3526288fa217dbd43f38e715fe7c3b9f468a94682015559fa0a1`. [Exact proof](final-proof.json).

## Requested result and boundary

Apply architect design.md appendix “2026-10-30: default-aware documentation specs, isolated from update3922”, with the lead's explicit correction preserving the existing versioned OPTIONS identity seam. Reduce duplicated current-version selectors while keeping SDK/schema compatibility and identity/privacy assertions meaningful. No runtime, shared helper, profile registration, exporter, dependency, deployment or configuration changes.

`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb` now derives local version/path from the mounted server default. HTML uses the root with exactly one overview/page/resource selector. Renderer contexts use the default profiles and canonical version URLs; TypeScript requests literal `/?describe=default` with JSON Accept, asserts the canonical generated SDK base and rejects the actual discovery URL. Slashless redirect/legacy-login expectations derive the mounted default path; raw `page=resources&q=a%2Bb`, status308 and unsupported99/no-Location checks remain, with an explicit unmounted99 assertion. The focused7.0-profile/6.0-absence contract remains literal because generated SDK schema compatibility is explicit.

Both cookie/header isolation OPTIONS calls stay on the **same versioned endpoint as33d6**, selected through `default_api_path`. All nil/UserSession/PaperTrail checks and cookie/header/auth ordering remain; no discovery call was inserted in that sequence. The shared api_version/vpath helper is unchanged.

`tests/suite/services-up.nix` uses root overview/authentication/resource URLs for generated examples and retains every content/absence assertion. The existing root index example obtains default/versions through JSON OPTIONS describe=versions, asserts membership and the exact rendered default version anchor alongside the title. Ruby JSON is explicitly required. Embedded Ruby syntax and Nix parse/format pass; this changed native assertion has not yet run.

## History, retained boundaries and migrations

The complete new base-to-head series is one commit, `a089b530376ca645456597df6a3533f720d24670`. [New series](complete-series.txt), [final two-file diff](final.diff), [two-path inventory](complete-paths.txt).

Full inherited context `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..a089b530376ca645456597df6a3533f720d24670` contains three commits: released dependency update11b26c0, owning consumer33d6, and this single test maintenance commit. There are36 aggregate changed paths. The published33d6 is a protected selected release/recovery boundary while parent update3922 remains separately owned; this task does not consolidate, move or rewrite it. There is no repeated dependency-pin stream or superseded implementation inside the new commit. The message-only amend retained identical tested tree; its original hook advisory and final clean hooks remain available. [Inherited series](inherited-series.txt), [inherited final diff](inherited-final.diff), [36-path inventory](inherited-paths.txt), [old/new range comparison](inherited-range-diff.txt).

**NO MIGRATIONS** in either range: no schema/migration paths and empty migration history. No introduced merged/released/deployed/externally-consumed migration requires disposition. [Migration history](migration-history.txt).

All3170 mode/type/OID entries outside the two test files equal exact33d6. Runtime/authentication, shared helpers, package metadata, locks, SDK pair, private optional hook/proxy and PHP/JS artifacts are unchanged. Published0332 ref remains exact33d6. Canonical/source/private inputs, all rollback worktrees/refs and parent3922 were untouched. [Outside equality](outside-equality.json).

## Quick results and original failures

Final related batch exec69286 passed: full **8/8**,68.796s; core **8/8**,56.926s, same eight descriptions/outcomes,0pending. Ruby syntax/RuboCop, Nix parse/nixfmt, diff checks and extracted embedded native Ruby syntax passed. Normal commit/amend precommit and commit-msg hooks passed; final message has no warnings. Full API lock restored toea0a24b1. Original registered path repair used normal declared-shell setup/Overcommit --sign and direct post-checkout execution, then public existing-path registration completion; all19 manifest entries were preserved and no checkout was repeated. [Quick proof](quick-proof.json), [quick log](quick.log), [final hook log](amend.log), [registration repair](repair-result.json), [hook byte equality](hook-byte-equality.json).

The first full run deliberately remains **6pass/2fail** in [original JSON](attempt-1/full.json). An OPTIONS parameter hash did not form the desired discovery URL; correcting it to the literal query made TypeScript pass. The corrected-query focused run remained **1pass/1fail**: root OPTIONS retained prior docs-cookie User.current rather than satisfying the existing nil assertion. Source confirms root authenticated_versions calls do_authenticate directly, while versioned authenticated? invokes post_authenticated, where vpsAdmin clears per-thread state. The lead accepted preserving the original versioned identity contract and deriving its path, rather than changing runtime or weakening assertions. This package neither fixes nor declares root OPTIONS identity cleanup safe. No upstream/runtime campaign ran. [Focused native JSON](corrected-query-focused.json), [finding and disposition](root-options-finding.json).

Temporary MariaDB identity651889 is gone; all owned check/commit handles ended. Existing generated dependencies and own temporary roots remain, with no cleanup or copied private state. [DB effects](quick-proof.json), [registration before](registration-before.json), [registration after](registration-after.json).

## Requested review and later work

Lead owns assignment to retained independent reviewer0 (saved Sol/xhigh/read_only), with affected test correctness, architecture/scope and identity/SDK compatibility assessment plus explicit complete-history consolidation and **NO MIGRATIONS** conclusion. Treat the authentication verification and inherited release context as high risk; no new runtime behavior is claimed. The inherited package's original review had one Blocking A032-R1 and no additional findings; lead accepted its exact deletion remediation under step9. Do not relabel that review as no findings or rerun unchanged package campaigns here.

Relevant procedures/design and existing docs/README/testing guidance were checked. No product guide change is useful because this is test maintenance; runtime documentation and exporter/schema contracts are unchanged. No arbitrary-version SDK compatibility is inferred from default selection.

After accepted final review and lead release, ONE affected services-up run remains, with normal selected preparation and exact input/derivation identity governing reuse of prior package/VM evidence. No old native pass is relabelled for this new test. Publication is held. No source-level dev/prod redeployment is required solely for these test changes; later source/history coordination belongs to parent after its original update reconciliation. Default integration remains unauthorized; initiative stays active.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
