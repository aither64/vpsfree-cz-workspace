# 2026-10-26-client-readme-improvements

## Goal

I'm looking at javascript/typescript client in haveapi and I find the readme insufficient and confused. we should clearly state what's available: callback/async pure-javascript client and the typescript client (not sure it this is async-only). the readme must include usage examples for all these options. right now it includes only callback client and some questionable info about async client:

```
const { AsyncClient } = require('haveapi-client');

async function main() {
  const api = new AsyncClient('https://api.example.test/v7.0');
  const result = await api.request({ method: 'GET', path: '/items' });
  console.log(result.data);
}

main().catch(console.error);
```

why does the caller specify API version? why does it make "raw" request using method and path? haveapi clients should use and show haveapi resources and actions. use default api version and don't complicate it.

python client readme is confused as well, it should be targeted at end-users of the client and not describe some internals. see readme's of other clients for comparison.

rust client readme could also find inspiration in go client readme. go/rust clients could also link vpsadmin-go-client/vpsadmin-rust-client as an example of generated clients.

look it over and suggest solutions.

## Affected repositories

- `haveapi`: JavaScript/TypeScript, Python, Rust and Go client READMEs and their implementation/tests as read-only evidence.
- Generated vpsAdmin Go/Rust repositories: public example-link checks only.

## Approach

The user accepted the proposal with “proceed”; implement the README and linked documentation changes, verify, independently review and publish the feature branch. Integration remains unapproved. Architect `architect0` owns source-backed interface investigation and `design.md`; the lead owns scope, acceptance inspection, recommendations and session tracking. Preserve project files and refs.

Backlog:

| Owner | Result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Interface and README findings/design | All requested client variants addressed with accurate resource/action examples, defaults and generated-client links | Read current README/source/tests; label unexecuted examples |
| implementer0 | Python publication diagnosis | Public package/version and correct end-user install command | Bounded public PyPI metadata check; no publishing |
| lead | User-facing proposal | Explain concrete recommended changes and important caveats | Architect report; bounded evidence inspection |

## Decisions

- Prefer default API version and discovered/generated resources/actions in introductory examples.
- Distinguish dynamic JavaScript interfaces from generated TypeScript and describe actual async support after inspecting implementation.
- Keep implementation, publication and integration outside this advisory pass. User subsequently identified Python release wording as stale; public PyPI check confirmed `haveapi-client` 0.30.2 (Python >=3.11), so remove the stale disclaimer in the proposed rewrite.

## Compatibility and deployment

Documentation proposal only: no runtime, schema, persisted-state, API or deployment changes. Future examples must describe existing supported behavior without inventing APIs or requiring version pinning. No deployment or integration planned.

## Documentation

Readers are application developers consuming HaveAPI clients. Proposed permanent changes belong in each client README, with maintainer details linked separately. Investigation and proposed execution boundaries belong in this session’s `design.md`.

## Testing plan

Read source and tests to verify example signatures, imports, discovery/version defaults and result shapes. Check generated-client link destinations. No builds or tests needed for investigation; snippets remain source-checked proposals until implemented and exercised. Final deliverable review will apply if substantive README changes are later implemented, not to investigation records alone.

## Accepted implementation packages

| Owner | Files/result | Acceptance and checks | Dependencies |
| --- | --- | --- | --- |
| implementer3 | HaveAPI worktree/environment/hooks preparation; final coordinated Git operations | Fresh default base, active declared hooks, serialize commits and push | Initial tracking commit before project commits |
| implementer0 | Python README and linked reference | Published install instructions; complete sync/async resource examples; preserve detailed behavior in reference; syntax/link checks | Prepared worktree, design.md |
| implementer1 | JS/TS README and linked guides | Four variants, default discovery, resource calls, accurate TS and result handling; syntax/type checks | Prepared worktree, design.md |
| implementer2 | Rust/Go READMEs and linked contributor docs | Generator/use split, complete async/blocking examples, generated-client links; signature/link checks | Prepared worktree, design.md |
| lead | Writing/acceptance pass and review packet | Apply user-facing writing skill, preserve technical facts, inventory whole branch | All drafts/checks |
| reviewer0 | Independent general final review | Explicit whole-history/no-migration conclusion; reconcile findings | All intended changes committed, quick checks pass |

Use one HaveAPI worktree with independent file ownership; all Git index/ref mutations serialized by implementer3. No runtime/generated artifact changes, migrations, releases or deployment. No broad integration suites expected for this documentation-only change.
