# HaveAPI 0.30.1 prerequisite snapshot

One authorized read-only batch on **2026-10-23 20:06:00 UTC**, under owner0's
safe boundary. Python observation completed in **0.873 seconds**, declared top
Nix invocation exited **0**; no command remains. Exact response bodies, safe
headers, URLs, response hashes and invocation/source identities are retained in
[the snapshot JSON](release-0301-publication-prerequisites-ready.json).

Binding: clean `haveapi-fixes-master-target` at
`090a188cb4ef3477324718627f4ae3415d1c0975`, tree
e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2. Used the prepared tools-only top shell
and reviewed `haveapi-hook-env.sh`; external followup `.gems` was read-only.
No setup, install, build, compiler, package download, CI observation, retry,
registry/configuration write or Git mutation occurred. Owner0 was notified of
completion and the safe boundary was yielded before further source setup.

| Destination/prerequisite | Actual response and conclusion |
| --- | --- |
| Four RubyGems exact 0.30.1 versions | Each official canonical v2 GET returned HTTP404. No metadata hash available. |
| npm/PyPI exact 0.30.1 | Each official canonical GET returned HTTP404. No identity/file/integrity hashes available. |
| GitHub HaveAPI tag/release | Exact `v0.30.1` ref and release endpoints returned HTTP404; no observed tag/release collision at this snapshot. |
| PHP mirror | `v0.30.1` ref returned HTTP404. Master is `397c95ff71ded9db98b214d58ea14a61c9973442`, message `Release 0.30.0`, source trailer `b64fb25bea8d8222fb3263b99956c0b61438a859`. |
| Packagist | HTTP200, no 0.30.1 version entry; latest 0.30.0 source ref equals the PHP master above. |
| Protected environment | HTTP200, required reviewer `aither64`; custom tag policy `v*` is present. `can_admins_bypass=true`, `prevent_self_review=false`; these are observations, no policy change requested. |
| Enabled publication variable | HTTP403, `Resource not accessible by personal access token`: **UNKNOWN**, not disabled or missing. |

No 0.30.1 collision was observed. Canonical404 does not establish registry name
ownership, guaranteed fresh absence or failure of an earlier upload. This batch
has no cache-distinct retry and makes no freshness or recovery inference. Exact
0.30.1 candidate/run/artifact/manifest/package identities remain pending.

Registry account trusted-publisher settings, PHP deploy credentials and webhook
configuration were not read or changed. Reviewed source still expects
`vpsfreecz / haveapi / release.yml / release`; public metadata and the source
contract cannot prove account configuration unchanged. Actual tagged-workflow
preflight/OIDC and independent destination verification remain authoritative.
Lead owns candidate-specific approval after the reviewed original artifacts.

The [earlier offline/max-jobs-zero shell stop](release-0301-publication-prerequisites.json)
remains unchanged as historical prerequisite UNKNOWN; its script never started
and it has no registry/publication conclusion. No publisher-code change follows
from either that local closure symptom or this access-denied variable read.

Next: owner0 prepares the reviewed 0.30.1 source/tag; lead coordinates the
actual tag run and artifact/protected approval gates in the
[acceptance checklist](release-0301-publication-acceptance.md). No upload,
approval, dispatch, failed-job rerun or automatic follow-up probe is authorized
by this snapshot.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
