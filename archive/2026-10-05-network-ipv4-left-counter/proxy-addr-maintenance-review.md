# Separate BFF dependency maintenance

[Draft PR #20](https://github.com/vpsfreecz/vpsadmin-webui/pull/20) updates the
transitive proxy-addr dependency to the version patched for
[GHSA-jqcg-44mw-7w3h](https://github.com/advisories/GHSA-jqcg-44mw-7w3h).
This is separate from network availability PR #19.

Branch `dev/proxy-addr-patch`, registered as `vpsadmin-webui-proxy-addr`, has one
commit, a7361bb2912485b61a5a0b1472d51158ac08ec96, directly after main base
02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51. Its four-file diff contains the
generated BFF lock, owning npm dependency hash, current packaging hash record
and dated work log. The lock changes only proxy-addr 2.0.7 to 2.0.8, its verified
package metadata and npm ordering of existing dependency keys. Other dependency
identities/constraints, frontend lock/hash, runtime/trust configuration and API
contracts are unchanged. No migrations or superseded commits remain.

The parent inspected the entire diff and normal hook configuration. This meets
the mandatory-review skill's mechanical dependency-only exemption: there is
no substantive handwritten implementation or policy change. Source and behavior
beyond this scope would require the normal review gate.

Both production audits report zero vulnerabilities. Verification passed 57 BFF
tests, 14 package/policy tests, 43 focused unit tests and complete ci:quick.
The final documentation audit checked 68 documents and 70 requirement IDs.
Both Nix packages and the three provenance/source-content/package-content
checks passed at the exact clean committed head. The
[paired metadata receipt](proxy-addr-maintenance-final-paired-package-metadata.json)
contains the actual output identities, equal full revisions, dirty=false and
installed proxy-addr 2.0.8.

The exact feature head is published over SSH. Maintenance CI 37494845158 passed
at that exact head. Default integration and deployment remain unauthorized.
Network feature/configuration heads were not changed to
bundle this maintenance patch; its proper integration remains a prerequisite
for the network WebUI dependency audit.
