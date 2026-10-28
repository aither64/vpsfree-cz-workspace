# KB client terminology: mechanics checks

**Ready for lead commit and independent general review; not restaged.** Candidates and summaries are exactly the lead-supplied final/ files; no E3 prose changes.

| Artifact | SHA256 |
| --- | --- |
| `kb-candidates/cs/navody/vps/api.txt` | `0f054e9ae749bacb40926c41d6dffc5ea1c46237c00cf4448edcb23d7d6ea43c` |
| `kb-candidates/en/manuals/vps/api.txt` | `5f556795f66e3656a49ff7d80fcb51275b5d085f1d20d227b5e46b5541b5a7bf` |
| `kb-release-cs.yml` | `abda865c02494f52b343ab3f00044fdd933a50443cc0a087e69e864fd8d1a45e` |
| `kb-release-en.yml` | `e51643dbf0c5e666ee8efa50b791821e959072b12ed1ee576274a09244247404` |
| `release-changes.yml` | `957ee7e6d6320af0914f5dda0f34560ab9bd7e77a1c5e95bfb5f171cb0e0990d` |
| `kb-validation.md` | `ce073a4c0d0124437218204df597b8bcf7aed35a1a9855379a76c3da3ea34e3c` |

Existing canonical prepare-release.rb/schema3 plan + installed schema5 generators passed: **191 unique pages (114CS/77EN),2 changed,189 preserved**; one write per manifest, no media/deletions or invented managed provenance. Installed parser and candidate checksum reads pass. [Build](canonical-build.log), [inventory/guards](canonical-check.json), [parser](manifest-parser-check.json).

[Protected checks](protected-checks.json) PASS: exact code blocks, URL/version multisets, translation/navigation markers, introduction before the working section and authentication-to-end unchanged versus preserved0311. SDK/generated framing removed. Whitespace checks have no diagnostics (no-index exit1 denotes expected content differences). Client prose adds no WebUI action; navigation applicability and historical unrelated annotation baseline limitations in kb-validation.md remain unchanged. No package/snippet/typecheck/browser/capture repeat.

[Fresh production page-info/content/page-info guards](production-source-guards.json) PASS: CS1783860648/SHA2568ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13; EN1777543182/SHA2568006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3. Original source index remains SHA25687c999835a1015665ed985ce2f85e8f05348ae7f11e7c93625538933af6709d7. No baseline refresh or production write.

Prior221files (including full191-page candidates/index, manifests/changes/validation/canonicalplan/sourceindex and staged facts) saved in [prior/receipt.json](prior/receipt.json), SHA2569f2a436ca130813a23555e1953051d59a2269b708fdfbe7edc219e131b483ac3. Fresh prior/status-current.log: owner OURSLUG/up, pending oldEN1253694e0937ad3e696db8a2666a1d83efb53bbb6d8f0de0a422a86daabbb221 bound preserved predecessor manifest. Existing staged pages retain prior wording:

- CS http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api — revision1793140740/contentd3c707a1e2f7f7326cf83e036576ff561f93e8c003218b081e3bb3ad886602d3.
- EN http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api — revision1793140759/contente93f46443954778b4b03ec0c706150c4cb217c7e92c4d9d095739e41fa100288.

All local handles complete. No stage/reset/promotion/stop/release, cluster/provider/dependency/source/ref/index/lifecycle action or credential output. Lead owns commit+independent general review; owned reset/restage remains held until release.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
