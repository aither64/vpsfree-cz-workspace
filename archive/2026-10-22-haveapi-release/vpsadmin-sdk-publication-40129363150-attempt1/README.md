# Native publication rejected: verified email required

Recovery release run40129363150, attempt1, sourceb6f846/tagv0.1.0 annotated77b40, reached native bootstrap publication and failed with Cargo exit101. The registry returned HTTP400: **“A verified email address is required to publish crates to crates.io.”** It directs the account owner to https://crates.io/settings/profile. No account identity, credentials or settings were inspected or changed here.

Candidate/native compile/capture, bootstrap-presence/HTTP404 prerequisites and tag recheck all passed. The native publish step ran ordinary Cargo with its scoped workflow credential, then received that registry response. Native evidence retention passed even on failure. Both original native candidate and publish archives were downloaded separately from this exact run: candidate artifact12574917980 and actual-publish artifact12573838827. Their bytes match: SHA2562099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0, size178978. Each has697 members,689 source-equal Rust files/runtime8/current clean VCS/source/manifests/lock proofs. Actual helper validation correctly remains failed because child101; the archive alone does not prove acceptance. No CI/localcandidate was substituted.

[parent-assessment.json](parent-assessment.json) binds native outcomes and original whole terminal ZIP/exact publisher log/artifact hashes. [public-verifier-handoff.json](public-verifier-handoff.json) supplies the actual native stream contract with terminal-success false: normal successful-publication verification is not yet eligible. Lead must route exact registry reconciliation and the verified-email owner action before any retry. No automatic retry, upload, yank, retag, version change, authentication repair or registry probe occurred here.

The fresh observer ended and yielded source/runtime/utility ownership; no local process or remote job remains. Source and immutable new tag77b40 remain unchanged, as do the historical oldtag/failedrun/oldapproval/403 records. Session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
