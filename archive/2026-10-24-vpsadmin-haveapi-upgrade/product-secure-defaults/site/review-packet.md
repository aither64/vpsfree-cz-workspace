# Site consumes product OAuth protections: final review

Clean `b56cd2e7ac714ff99b8cc3d43c67f6130ac1ce27`, tree `9ff7bd8ea86e7d7a8005984f5b9bda4f7eb69fc9`, based on freshmaster `e34f08314b6db1ac38facc2386b79111daee864f`. [Full series](series.txt), [final diff](full.diff), [old4e→final](old4e-final.diff), [range comparison](old-new-range.diff), [complete machine-readable packet](review-packet.json).

Three coherent commits: one normalgenerated complete45cb productpin `821f04ad03824714b37417d9178c8d146e25c598`, site/APIintegration `15e40e85da939ba5aaaf288f9b422fd32ed9ace2`, leadexactoperatorguides `b56cd2e7ac714ff99b8cc3d43c67f6130ac1ce27`. Old4e/60af/frozen249f and earlier refs/private paths remain. Obsolete sitepolicy add/remove and intermediate75c stream are absent. NO MIGRATIONS in owned delta; upstream/deployedhistory retained. OriginalAPIhook/README/spec/nav content stays exact4e.

Eight paths change, all467 outside entries exactbase. Only serviceslocked rev/NAR/time change rawlock;158 semanticpaths, threealiases to sameexisting follows node. Generic6f54/unrelatedinputs/configidentity preserved. Product45cb/source d38 is reviewed/checked/published (E2 services34/34 + installedPHP5 PASS); no duplicate E2 suite or overallCI claim.

Site retains domains/aliases/listeners/certs/ACME/frontendforceSSL, private inputs/trusted origins/topology and directHAProxy routes; eightAPI/authlocations retain only the four additional edge header clears, devBasicAuth additive. Product owns logging, headers/FPM/HAProxy defaults and HTTP redirects. Stale site fragment/fixture removed; commonwebui exactfreshbase.

Quick actualpureproxy/backend evals0. [Generated sevenhost topology/policy proof](generated-quick-proof.json), [backend syslog/nginx proof](backend-quick-proof.json). Unchanged publishedproduct nginxfixture with the four actualsite clears added to equivalent generatedfixturelocations passes24checks, sentinels absent/auth/wirequery/ACME/maintenance/diagnostics/effects verified. [Native result](native-1/result.json). It is isolatedpolicy proof, not fullsite installedruntime/PHP/login acceptance. Parse/diff0; normalNixfmt/RuboCop/commit hooks0; exactleadPHPguidehash0d75/APIinsertion99bf, allotherAPIguidebytes unchanged. Known artifact-reader failures/corrections preserved, no repeated producteval or source workaround.

Request all4/HIGH independent finalreview of completehistory/consolidation/TLS+trust+rollout/migration boundaries. Product protectedsamehost transformation and documented customsnippet/one-sidedlistener limits are accepted; actualsite uses normaldual listeners and no conflictingserverrewrite. Rollout requires edge/HAProxy before backend/application; rollback retains protection while callbacks enabled.

**STOP before the four affected builds and generated/syntax verification.** All owned execution handles ended/PIDs gone, source clean/no uncertain effect. No consumer publication/default merge/claim/deploy/live/lifecycle/cleanup. Parent owns finalreview and records; sessionopen.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
