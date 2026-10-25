# HaveAPI 0.30.0 destination verification plan

Prepared by implementer1; **not executed**. The user confirmed the new RubyGems
and PyPI publishers in [release-authorization.md](release-authorization.md).
This package makes no fresh destination probes, publication or configuration
changes. Existing receipts/artifacts remain preserved. No separate crate action.

## Inputs and one-pass rule

Lead supplies the terminal tagged-run/publish result, original run ID and artifact
ID, exact source commit and absolute directory containing the original tagged-run
`release-<run-id>` files. Expected tag/version are `v0.30.0`/`0.30.0`; approved
source is `b64fb25bea8d8222fb3263b99956c0b61438a859` unless lead supplies a
separately accepted exact source. Do not substitute earlier local or branch-run
artifacts. Use a separate session evidence directory for downloaded public assets.

Perform one read-only external verification pass after terminal publication.
Record timestamps, HTTP statuses, run/source/artifact identity and every observed
hash/ref. Report a missing destination, mismatch or indexing lag without polling,
rerunning, rebuilding, republishing, moving tags or changing registry settings.
A later followup is separately coordinated by lead. Do not invoke publisher
commands (`github-prepare`, `pypi-prepare`, `publish`) for verification.

## Original artifact and run identity

The following commands are templates; substitute only the lead-supplied inputs.
`gh api` is explicitly GET. Ordinary authentication is used without inspecting
credentials. None of these commands edits Git refs or the application checkout.

```sh
gh api --method GET repos/vpsfreecz/haveapi/actions/runs/RUN_ID \
  --jq '{id,event,head_branch,head_sha,status,conclusion,html_url}'
gh api --method GET repos/vpsfreecz/haveapi/actions/runs/RUN_ID/jobs?per_page=100 \
  --jq '{jobs:[.jobs[]|{id,name,status,conclusion,html_url}]}'
gh api --method GET repos/vpsfreecz/haveapi/actions/runs/RUN_ID/artifacts \
  --jq '{artifacts:[.artifacts[]|{id,name,expired,digest,workflow_run}]}'
gh api --method GET repos/vpsfreecz/haveapi/git/ref/tags/v0.30.0
```

Require the original run's `event=push`, exact head source, terminal successful
build/publish jobs, the supplied original artifact ID named `release-RUN_ID`,
and a nonexpired artifact. Resolve the annotated tag object's `object.url` with
one GET to prove its final commit equals the run head; tag creation alone is not
publication proof. Compare the local original manifest's
`schema=1,version=0.30.0,tag=v0.30.0,source=SOURCE,run_id=RUN_ID`. Hash every file
in `manifest.files`; require the exact ten-file helper catalog and no symlinks.
Do not rewrite the manifest. Its eleven release assets are those ten files plus
`release-manifest.json`.

At the exact tagged checkout, the existing read-only verifier is available:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 GITHUB_RUN_ID=RUN_ID nix develop -c \
  ruby utils/release/cli.rb verify /ABSOLUTE/ORIGINAL_TAG_RUN_ARTIFACTS
```

Use this only when the checkout is already the exact supplied source and lead
includes it in the verification grant; do not switch refs. Otherwise perform
manifest identity and SHA-256 comparisons directly from the artifact directory.
This check inspects existing packages; it does not build or install them.

## Exact registry checks

Query these official endpoints once each. Capture JSON/status in the evidence
receipt; a 404 after terminal publish is a missing confirmation, not a reason to
upload or retry automatically.

```text
https://rubygems.org/api/v2/rubygems/haveapi-client/versions/0.30.0.json
https://rubygems.org/api/v2/rubygems/haveapi/versions/0.30.0.json
https://rubygems.org/api/v2/rubygems/haveapi-go-client/versions/0.30.0.json
https://rubygems.org/api/v2/rubygems/haveapi-rust-client/versions/0.30.0.json
https://registry.npmjs.org/haveapi-client/0.30.0
https://pypi.org/pypi/haveapi-client/0.30.0/json
```

- Four gems: compare each `sha` to original manifest
  `files["GEM-0.30.0.gem"]`, as `Publisher#gem_present?` does. Record the exact
  version identity and package endpoint for each independently.
- npm: require `name=haveapi-client`, `version=0.30.0`. Compute
  `sha512-BASE64(SHA512(original haveapi-client-0.30.0.tgz))` and require it in
  the whitespace-separated `dist.integrity` tokens, as the helper does. Record
  `dist.tarball`; SHA-256 of the local tarball must already match the manifest.
- PyPI: require info name/version `haveapi-client`/`0.30.0`; require exactly one
  each of `haveapi_client-0.30.0-py3-none-any.whl` and
  `haveapi_client-0.30.0.tar.gz`, no duplicate/unexpected files, and exact
  `digests.sha256 == manifest.files[filename]`. Record both URLs and hashes.

The hash computation can use only the standard library:

```python
import base64, hashlib, json
from pathlib import Path
artifact_dir = Path('/ABSOLUTE/ORIGINAL_TAG_RUN_ARTIFACTS')
manifest = json.loads((artifact_dir / 'release-manifest.json').read_text())
for name, expected in manifest['files'].items():
    path = artifact_dir / name
    assert path.is_file() and not path.is_symlink()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
npm_integrity = 'sha512-' + base64.b64encode(hashlib.sha512(
    (artifact_dir / 'haveapi-client-0.30.0.tgz').read_bytes()
).digest()).decode('ascii')
```

## PHP mirror, source snapshot and Packagist

```sh
gh api --method GET repos/vpsfreecz/haveapi-client-php/commits/v0.30.0 \
  --jq '{sha,message:.commit.message,html_url}'
gh api --method GET repos/vpsfreecz/haveapi-client-php/commits/master \
  --jq '{sha,message:.commit.message,html_url}'
gh api --method GET repos/vpsfreecz/haveapi-client-php/git/ref/tags/v0.30.0
```

Require tag commit message to contain the exact complete line
`HaveAPI-Source: SOURCE`, version 0.30.0, and immediate post-publish master to
match that commit. Resolve the annotated tag object to the same commit.
If master has advanced, report its new identity for lead reconciliation rather
than resetting it or assuming the release was overwritten.

Download the immutable tagged commit snapshot once from
`https://api.github.com/repos/vpsfreecz/haveapi-client-php/tarball/PHP_TAG_COMMIT`.
Read it in memory with `tarfile` rather than extracting into a repository.
Remove only GitHub's single archive-root directory, ignore directories and
mirror-owned `AGENTS.md`/`.github/**`, and reject traversal, symlinks, duplicate
paths or nonregular entries. Compare exact remaining paths, file contents and
normalized executable mode (0644/0755) to original
`haveapi-client-php-0.30.0.tar`, matching `Publisher#mirror_snapshot` semantics.
Require composer identity `haveapi/client` and version `0.30.0`. This proves
content as well as provenance; neither a tag nor version field alone is enough.

Query once: `https://repo.packagist.org/p2/haveapi/client.json`. Find exact
`version=0.30.0` and require source URL to identify
`vpsfreecz/haveapi-client-php` and source reference to equal PHP_TAG_COMMIT.
Record missing indexing separately from successful mirror synchronization.
No webhook mutation or polling is part of this pass.

## Final public GitHub Release and all assets

```sh
gh api --method GET repos/vpsfreecz/haveapi/releases/tags/v0.30.0 \
  --jq '{id,tag_name,name,draft,prerelease,published_at,html_url,body,assets:[.assets[]|{id,name,size,digest,browser_download_url}]}'
gh release download v0.30.0 --repo vpsfreecz/haveapi \
  --dir /ABSOLUTE/SEPARATE_SESSION_EVIDENCE/github-release-assets
```

The download directory must be new and separate from original artifacts. Require
`tag_name=v0.30.0`, `draft=false`, `prerelease=false`, a publication timestamp,
and exactly the expected eleven asset names. Compare every downloaded asset's
SHA-256 to its original tagged-run counterpart, including the manifest itself;
require the release body to match original `release-notes.md` modulo outer
whitespace. Automatic GitHub source archives are not listed release assets and
are not replacements for the retained PHP/package files. Record the public URL
`https://github.com/vpsfreecz/haveapi/releases/tag/v0.30.0`.

## Receipt and standby

Save one compact `release-destination-verification.json` plus a prose result
under this session, binding exact run/artifact/source/tag identities and every
registry/PHP/Packagist/Release comparison. Distinguish confirmed, missing,
conflicting and temporarily unreadable destinations. Do not call a partial
release complete. Full workflow success does not replace destination hashes;
registry success does not replace public Release/PHP/Packagist confirmation.

Prepared only. Await lead's exact tagged-run inputs and terminal publish result
before a single actual pass. No probes or waits are started by this plan.
