The BFF production dependency audit failed on proxy-addr 2.0.7 for
[GHSA-jqcg-44mw-7w3h](https://github.com/advisories/GHSA-jqcg-44mw-7w3h).
That version was already in main. This separate maintenance patch updates the
transitive dependency to 2.0.8 and refreshes its owning Nix dependency hash.
The generated lock adds verified funding metadata and reorders unchanged
dependency keys. Other dependencies and the existing loopback proxy trust
configuration are preserved. There are no migrations or API changes.

Both production dependency audits reported zero vulnerabilities. Focused checks
passed 57 BFF tests, 14 package/policy script fixture cases and 43 runtime-bootstrap/OAuth
unit tests across three files. The full `ci:quick` gate passed, including all four
type-check domains, and the final documentation audit passed with 68 documents
and 70 requirement IDs. Scoped Nix formatting and dependency/hash guards passed.

At this checkpoint, exact committed Nix package builds and paired clean
provenance checks are pending. Their final revision and receipts will be linked
from the [session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/).
This patch is unmerged and undeployed. The evidence does not assess deployed
exploitability. Requirements: REQ-068 and REQ-064.
