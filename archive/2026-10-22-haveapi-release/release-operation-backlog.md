# Authorized release operation backlog

| Owner | Package / expected result | Acceptance | Dependency |
| --- | --- | --- | --- |
| implementer0 | Clean target and enabled hooks | Exact reviewed head/tree/history, unchanged remote base, supported hook readiness | Complete |
| implementer1 | Read-only publication preflight | Official metadata and explicit account/API limits | Complete |
| implementer0 | Integrate HaveAPI/master | Held single-repository claim; ff-only merge/hooks, normal SSH push, exact remote proof, explicit release/status | Complete: remote master exact b64; claim released and verified |
| implementer0 | Create official release branch and annotated tag | haveapi-0.30 and v0.30.0 at exact integrated/reviewed source; no conflicts, no tag movement | Complete: atomic branch/tag push; exact tag run 39849807897 |
| fresh Luna/low utility | Observe tagged release and related new CI | Exact run/head/event; terminal result or prompt failure/protected approval escalation; logs retained; no retries/approvals | Active: /root/publication_watcher; exact tag/master IDs |
| lead | Inspect retained candidate and approve protected publication | Exact source/version/manifest, workflow build success, original retained artifact identity, user's release authorization | Tagged build ready |
| implementer1 | Confirm publication destinations | RubyGems/npm/PyPI hashes, PHP mirror/tag/source and Packagist version, public GitHub Release | Publishing terminal result |
| lead | Reconcile final state/handoff | Accurate integrated/published identities, remaining risks, session left open | Publication verification |

No source implementation work is planned. Any concrete failing check returns to
the owning implementer for bounded diagnosis; no blind reruns or tag movement.
No separate Rust crate publication, deployment, lifecycle action or cleanup.
