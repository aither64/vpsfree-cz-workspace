# Live pending-draft diagnostic

The user ran the requested read-only diagnostic with their logged-in gh on macOS
and supplied its output in this conversation:

```sh
gh release view v0.29.11 --repo vpsfreecz/haveapi \
  --json databaseId,tagName,isDraft,apiUrl
```

The returned databaseId is417635025, tagNamev0.29.11, isDrafttrue, apiUrl
https://api.github.com/repos/vpsfreecz/haveapi/releases/417635025.
Exact JSON: [user response](pending-tag-live-draft-user-response.json).

This is actual authorized pending-draft resolution through gh. Together with the
reviewer's inspection of the exact gh2.102.0 pending-tag implementation and the
candidate's matching GraphQL-to-ID lookup, it satisfies the requested live-draft
diagnostic before the next tag. It is user-run evidence; the lead did not execute
the candidate with the user's credentials or fetch this private draft response
independently. The session token still cannot see drafts. No create, upload,
publication or approval was requested or performed by this diagnostic.

The displayed intended tag does not capture the raw REST tag_name for this draft;
no synthetic raw REST payload is claimed. Existing regressions model the upstream
contract. Both failed versions and their original files remain preserved.

Ordinary releases require no manual gh diagnostic. After human protected-release
environment approval, the publishing job uses its own github.token as GH_TOKEN
with contents:write to create/read the draft, retain approved files and finalize
the Release after all destinations succeed. That token is separate from this
development-session token. Source: .github/workflows/release.yml publish job and
utils/release/publish.rb prepare_github / github_release / finish_github.

Both source candidates remain clean at their reviewed exact heads/diff hashes.
No source edit or new check is needed for this evidence-only gate update. Full
checks and11safe Actions already passed. Ready, awaiting fresh authorization to
integrate HaveAPI master and haveapi-0.29 and push annotated v0.29.12. Publication
then waits for its own human release-environment approval. Session remains open.
