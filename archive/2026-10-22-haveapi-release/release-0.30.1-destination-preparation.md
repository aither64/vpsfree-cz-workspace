# HaveAPI 0.30.1 independent destination verification

Prepared only; no 0.30.1 destination was queried. Owner2 owns prerequisite and
collision reads. Await the lead's final published-manifest handoff and a separate
actual-verification grant. No watcher has been launched.

The retained [0.30.0 result](release-destination-verification.md) confirmed all
18 checks and eleven public assets against its original tagged-run artifact.
Preserve that evidence. This package uses the same identity chain, adds explicit
RubyGems name/version/platform checks and a separate npm dist-tag observation,
and takes all new identities and hashes from the eventual 0.30.1 handoff.

## Handoff and operation boundary

Copy [the input template](release-0.30.1-destination-handoff.template.json) to a
new completed handoff file. Lead supplies the exact source, tag, terminal run and
attempt, successful build/publish job IDs, original artifact ID and archive digest,
absolute original-file directory, manifest SHA-256 and publisher receipt link.
Every unset identity is a blocker. No guessed hashes, moving branch bytes or
earlier local build may substitute for the tagged run. The original directory
must contain exactly the eleven retained files and remain unchanged.

The helper at HaveAPI `090a188cb4ef3477324718627f4ae3415d1c0975` invokes npm
publish without `--tag`; no tracked npmrc was found. Record `npm_dist_tag=latest`
if the final tagged command retains that default, or the actual explicitly
configured tag if the final accepted workflow changes it. A later moving-tag or
PHP-master advancement is a separate observation to reconcile, not evidence that
an immutable published version was overwritten.

The fixed publisher checks exact gem identity, `platform=ruby` and SHA-256; npm
name/version and SHA-512 integrity; exact nonduplicate Python filenames/hashes;
PHP source provenance and normalized content; and final GitHub assets. Its GET
confirmation has a bounded deadline, no-cache and cache-distinct reads, strict
conflict refusal and no repeated upload. Publisher confirmation is an operation
receipt. The observations below are separately collected public evidence.

Use a new session evidence directory such as
`release-0.30.1-destination-evidence-RUN-attempt-N/`. Refuse an existing directory;
never overwrite original files or older attempts. Downloads and observation
records go only there. The final receipt must bind the completed input file and
its digest, timestamps, requests/statuses, all expected/observed hashes and any
visibility gap. No package install, application test, build, source/ref change,
publication, workflow rerun, tag change, registry configuration or downstream
crate action is included.

## One bounded observation pass

After authorization, one fresh policy watcher may own the complete download/
observation command batch and execution handle. The lead coordinates the shared
utility slot, resolves the pinned Luna/low policy and supplies explicit
full-access/never launch settings. Do not reuse a prior utility thread or poll in
parallel. The verifier itself is offline and needs only Python's standard library.

Use public HTTPS GETs without registry tokens, cookies or upload credentials.
No shared credential files are read. For metadata, send `Accept: application/json`
and `Cache-Control: no-cache`, disable redirects, and bound each request to 45
seconds total with `curl --max-time 45`. Save its body even on an HTTP error,
status and observed UTC time. Retain only `Age`, `Date`, `Cache-Control`, `X-Cache`
and `Retry-After` diagnostic headers (printable, at most 200 characters); never
save Authorization, cookies or a signed redirect URL. A transport/read failure,
rate limit, non-200 result or partial valid metadata remains **unconfirmed**.
A successful identity/hash/schema mismatch is a **conflict**. In particular,
404 after publication does not establish absence or authorize another upload.

This independent pass performs one GET per listed metadata endpoint. It does not
repeat the publisher's ten-minute loop. Preserve every result and report a
visibility/indexing gap to lead without automatic retry, alternate upload or
polling. A later bounded observation is a separately assigned operation. No
cache-distinct read is required to finish this one-pass evidence package.

Collect the following keys in `index.json`; substitute only validated handoff
values. `API` below means `https://api.github.com/repos/vpsfreecz/`.

| Key / body filename | Exact GET URL suffix or official URL |
| --- | --- |
| `run` / `run.json` | `APIhaveapi/actions/runs/RUN` |
| `jobs` / `jobs.json` | `APIhaveapi/actions/runs/RUN/jobs?per_page=100` |
| `artifacts` / `artifacts.json` | `APIhaveapi/actions/runs/RUN/artifacts?per_page=100` |
| `haveapi_tag` | `APIhaveapi/git/ref/tags/TAG` |
| `haveapi_tag_object` | `APIhaveapi/git/tags/ANNOTATED_TAG_SHA` from the previous response |
| `gem_haveapi-client` | `https://rubygems.org/api/v2/rubygems/haveapi-client/versions/VERSION.json` |
| `gem_haveapi` | `https://rubygems.org/api/v2/rubygems/haveapi/versions/VERSION.json` |
| `gem_haveapi-go-client` | `https://rubygems.org/api/v2/rubygems/haveapi-go-client/versions/VERSION.json` |
| `gem_haveapi-rust-client` | `https://rubygems.org/api/v2/rubygems/haveapi-rust-client/versions/VERSION.json` |
| `npm` | `https://registry.npmjs.org/haveapi-client/VERSION` |
| `npm_tags` | `https://registry.npmjs.org/-/package/haveapi-client/dist-tags` |
| `pypi` | `https://pypi.org/pypi/haveapi-client/VERSION/json` |
| `php_tag` | `APIhaveapi-client-php/git/ref/tags/TAG` |
| `php_tag_object` | `APIhaveapi-client-php/git/tags/PHP_ANNOTATED_TAG_SHA` |
| `php_commit` | `APIhaveapi-client-php/commits/TAG` |
| `php_master` | `APIhaveapi-client-php/commits/master` |
| `packagist` | `https://repo.packagist.org/p2/haveapi/client.json` |
| `github_release` | `APIhaveapi/releases/tags/TAG` |

Each omitted body filename is the key plus `.json`. Resolve only the exact
annotated-tag SHA from the saved ref; validate its 40 lowercase hexadecimal
characters before using it in the next URL. The verifier requires both annotated
tags to resolve directly to commits. If pagination reports more results than the
saved page, stop for a bounded collection adjustment rather than assuming the
requested artifact/job is missing.

Representative capture command, after the lead fills the exact values:

```sh
curl --silent --show-error --proto '=https' --max-time 45 \
  -H 'Accept: application/json' -H 'Cache-Control: no-cache' \
  --output /NEW_EVIDENCE/run.json --write-out '%{http_code}\n' \
  'https://api.github.com/repos/vpsfreecz/haveapi/actions/runs/EXACT_RUN'
```

The wrapper must record the command exit status independently of the returned
HTTP code and preserve failed-response bodies. Do not use `--fail` to discard
them, `--retry`, redirect-following metadata requests or shell tracing. Read-only
GitHub API access through the ordinary declared `gh api --method GET` command is
also acceptable if anonymous API limits prevent this pass; record that access
path and failure, never inspect or copy its credentials and do not retry it
silently.

After the saved metadata validates the tag/commit and exactly eleven asset names,
download the immutable PHP snapshot to `php-tag-snapshot.tar.gz` and public assets
to a new `github-release-assets/` subdirectory. Use only:

```text
https://api.github.com/repos/vpsfreecz/haveapi-client-php/tarball/PHP_TAG_COMMIT
https://github.com/vpsfreecz/haveapi/releases/download/TAG/EXPECTED_FILENAME
```

These public downloads may follow HTTPS redirects (at most three, total request
deadline 180 seconds per file) without credentials. Keep only the original public
URL in the receipt; do not log or persist signed redirect locations. Require
terminal HTTP 200. Do not download dynamic unexpected filenames, use an automatic
GitHub source archive as a substitute, or extract an archive into a checkout.
The offline comparison reads tar members in memory, rejects unsafe/nonregular/
duplicate paths, removes only the GitHub archive root and mirror-owned
`AGENTS.md`/`.github/**`, and compares contents plus normalized executable modes.

## Observation index and offline command

`index.json` is a collection record, not a success assertion. Use this shape;
repeat entries for all collected keys and all eleven downloads:

```json
{
  "schema": 1,
  "collected_at": "ACTUAL_UTC_TIME",
  "responses": {
    "run": {
      "url": "EXACT_PUBLIC_GET_URL",
      "status": 200,
      "body_file": "run.json",
      "observed_at": "ACTUAL_UTC_TIME",
      "transport_exit": 0,
      "headers": {"Date": "OBSERVED_DATE"}
    }
  },
  "downloads": {
    "php_snapshot": {
      "url": "EXACT_IMMUTABLE_PUBLIC_URL",
      "status": 200,
      "transport_exit": 0,
      "observed_at": "ACTUAL_UTC_TIME"
    },
    "assets": {
      "EXPECTED_FILENAME": {
        "url": "EXACT_PUBLIC_BROWSER_DOWNLOAD_URL",
        "status": 200,
        "transport_exit": 0,
        "observed_at": "ACTUAL_UTC_TIME"
      }
    }
  }
}
```

Do not invent a 200 status for a local copy or infer it from a publisher message.
For failed transport retain its actual nonzero exit and status 0/null, so the
offline verifier records uncertainty. Keep publisher logs under the supplied
`publisher_receipt` reference rather than mixing their assertions into this index.

Run the prepared [offline verifier](release-0.30.1-destination-verify.py):

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/release-0.30.1-destination-verify.py \
  /ABSOLUTE/COMPLETED_HANDOFF.json \
  /ABSOLUTE/NEW_EVIDENCE \
  /ABSOLUTE/NEW_EVIDENCE/independent-result.json
```

It performs no HTTP, subprocess, Git or publication action and refuses to
overwrite its result. It checks the original catalog/eleven hashes, exact source
tag/run/attempt/jobs/original artifact, four gem identities/platforms/SHA-256,
npm SHA-512 plus moving dist-tag, both PyPI filenames/hashes, PHP provenance/
snapshot/master, exact Packagist source, public release body/eleven asset names
and every downloaded hash. It rechecks original bytes after comparison. All
expected checks must be confirmed; missing observations never count as success.
The reported check count need not equal the prior receipt's 18 because the npm
moving tag and original immutability are explicit additional named checks.

The plan and script are prepared evidence, not a completed release proof. Only
syntax/JSON parsing was checked while preparing them. Final interpretation and
user-facing release acceptance remain lead-owned. Existing runtime/schema facts
and the separately generated vpsAdmin crate are unchanged; this package never
publishes that crate.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
