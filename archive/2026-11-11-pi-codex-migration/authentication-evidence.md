# Shared Pi authentication: one login, coordinated refresh

Package J, implementer5, 2026-11-12. Package I was reported and accepted before
this assignment; capacity confirmed. Exact session/current/environment binding
verified. Unchanged workspace procedures and documentation skill reused;
same-session roster confirms saved implementer5/architect0 access. Only this
evidence file is owned here; lead owns plan/state and architect0 design.md.
This refines [accepted provider evidence](provider-fallback-evidence.md).

## Recommendation

**For Pi-only workers using one account, one initial Pi login and one canonical
writable file store can serve multiple independent OS processes. A separate
login per worker or a broker is not inherently required.** The pinned file
backend deliberately coordinates refresh across processes. This is supported
source behavior, not a live concurrency/entitlement test or crash-proof guarantee.

With per-session mount namespaces, share the **containing credential directory**
so every participant sees the same authoritative data, lock sidecars and mutable
rotation/replacement effects. Binding only an auth.json file into separate
private directories can leave independent adjacent locks; sharing file contents
or an inode alone does not establish common refresh ownership. Canonicalize the
configuration and preserve permissions. Distinct copies, snapshots, alias keys,
paths resolving to different stores, and custom backends do not inherit this
guarantee. No namespace/bind-mount experiment ran.

This means one initial **Pi grant per account**, not importing the same rotating
grant from an active legacy Codex installation. Codex uses its own credential
format/store and locking; Pi's lock does not coordinate that writer. Reusing a
grant across them needs a common refresh authority or separately validated
coordination. Do not copy credentials among workers or assume a personal
codex-lb already implements the required subscription flow.

## Exact implementation evidence

All Pi links below bind **a22b888a58fe55b668cc45b80749ec88d4eb4ddc**. The source
snapshot is main, not a claim that every behavior is in release v1.5.2.

| Question | Source conclusion |
| --- | --- |
| Complete lock scope | `FileAuthStorageBackend.withLockAsync` acquires proper-lockfile, then reads current JSON, awaits the callback, writes its returned JSON synchronously, and releases in `finally`. The network OAuth refresh is inside that callback. The file lock serializes the entire store, stronger than the interface's per-provider minimum. Async contention waits are cancellable, bounded near 30 seconds; the lock uses a 30-second stale setting and detects compromise. [File backend][file] |
| Reread and rotation | `AuthStorage.modify` parses JSON read after lock acquisition and passes the current provider entry to the callback. `refreshStoredOAuthCredential` rechecks expiration there, so another process's completed refresh suppresses a duplicate. The rotated credential is written before unlock. It does not refresh from a stale cached credential inside the lock. [Mutation][mutation], [refresh][refresh] |
| Cancellation and exit | The caller may cancel its wait. Once refresh starts, refresh/persistence deliberately ignore caller cancellation because the provider may have consumed the old refresh token; the refresh has a 15-second timeout. `RuntimeCredentials.settled()` waits for started modifications to finish or fail. Abrupt process death is not equivalent to that graceful wait. [Refresh][refresh], [runtime overlay][overlay] |
| Cache freshness | File reads compare dev/inode/size/mtimeNs/ctimeNs, then reload under lock when changed. In-process reloads may coalesce; that cache is not the refresh lock. Mutation always rereads storage. Already dispatched requests retain their resolved access token; cache invalidation is not recall of in-flight auth. Sync reload preserves the last valid snapshot on failure; un-signalled reads can serve cached data on reload failure, while signalled reads propagate the failure. [Read/cache][cache], [revision][revision] |
| Failure effects | OAuth refresh failure raises `ModelsError("oauth")`; storage/lock failure raises `auth`. Failed refresh does not silently fall back to environment auth or erase the credential. A lost response after server-side rotation, failed disk write, lock compromise, or process death can still leave the persisted refresh token unusable. The file write is not an fsynced atomic transaction with the provider; browser reauthentication can be necessary. [Resolution][refresh], [file backend][file] |
| Refresh-on-401 | Inspected `Models.applyAuth` resolves credentials before provider dispatch. Normal refresh is expiry-based, at least five minutes before stored expiry. No forced refresh-on-401 path was found in that resolver, Models dispatch, ModelRuntime, or inspected OpenAI Responses/Codex adapters. Do not promise immediate repair of a revoked but apparently unexpired token; a repeated request is not proof of a fresh grant. [Dispatch][dispatch], [refresh][refresh], [Responses][responses], [Codex adapter][codexadapter] |
| Account key | `CredentialStore` is keyed by `Provider.id`, one credential per provider, not by member/account. Same provider ID in one store means one account slot. Distinct accounts need explicit store/account namespaces. Different aliases of the same rotating grant must still map to one refresh authority; copying it into separate keys creates stale independent refresh state. [Contract][contract] |

The pinned source includes contention, concurrent modification, symlinked-path
locking, cancellation, malformed-file and storage-failure tests. They were read,
not run. The inspected auth-storage test is not a new independent-process or
mount-namespace acceptance result. Symlink aliases are explicitly intended to
resolve to the same lock; hard-link/file-only bind aliases are not certified by
that test. [Tests][tests]

## Which stores share safely

The coding-agent defaults to `AuthStorage.create()` at its agent directory's
auth.json; SDK ModelRuntime permits an explicit auth path/store. Lower-level
pi-ai `Models` defaults to an **in-memory** store, not this file backend.

| Store arrangement | Concurrency/ownership implication |
| --- | --- |
| Canonical Pi file backend, same existing directory/file/provider key | Cross-process refresh coordination is implemented. Initialize/login once before launching workers; all participants must cooperate with the same lock. Sharing auth does not require sharing conversation/session files. |
| In-memory or ephemeral stores in separate processes | Promise-chain locking is local to each instance/process. Copying an OAuth credential into each is not shared refresh ownership. [In-memory store][memory] |
| Custom keychain, database, remote store or SDK integration | `CredentialStore.modify` requires serialized current-value read/modify/write, cross-process where the backing store supports it. A keychain's atomic set alone does not cover network refresh. Prove the entire refresh transaction and logout/login interaction for that implementation. [Contract][contract] |
| ReadOnlyAuthStorage | Loads a cached snapshot and rejects modify/delete. It cannot perform OAuth refresh and does not follow mutable rotation as the writable store does. It is not the shared-refresh solution. [Read-only store][readonly] |
| Runtime API-key override/access-token snapshot | The overlay stores a nonpersistent string and shadows the credential. It does not independently provide OAuth expiry/refresh. A token broker must reacquire temporary auth before expiry and supply the provider's required account/header context. [Runtime overlay][overlay] |

## Browser login, hardware key and later refresh

Pi's two OpenAI subscription mechanisms are distinct:

| Native provider/login source | Exact pinned contract |
| --- | --- |
| `openai-codex` OAuth | Offers browser authorization-code + S256 PKCE with localhost:1455 callback/manual redirect input, or a device-code flow using OpenAI's `/codex/device` browser verification. Scope: `openid profile email offline_access`. Token exchange and refresh require access token, refresh token and expiry; Pi extracts the ChatGPT account ID from the access-token claim. Subsequent refresh uses refresh_token/client_id without a browser callback. [Codex OAuth][codexoauth] |
| `openai` Sign in with ChatGPT | Separate dynamic public client with state/nonce and S256 PKCE, installation host UUID, resource `https://api.openai.com/v1`, and scopes `openid profile email offline_access resource.invoke chatgpt.tokens.use.direct`. Callback supplies an issued client ID. Initial token response requires an ID token; credential creation requires nonempty access/refresh/scope, positive expiry and the direct-token scope. Stored credential includes client ID/scopes; refresh uses that client ID/resource and validates the new token contract. This inspected flow offers browser callback/manual URL entry, not the Codex device-code selector. [Direct OAuth][directoauth] |

The actual browser authentication challenge belongs to OpenAI/account/SSO policy.
Neither inspected Pi module implements WebAuthn or promises a hardware-key-free
flow. If the user's Daybreak login presents a hardware-key challenge, it must be
completed by the user in the real browser during initial login or reauthentication.
Device authorization relocates browser approval; it does not establish that MFA
or a model-specific challenge is bypassed. These modules and the inspected Pi
provider guide do not document a Daybreak-specific grant or hardware-key contract.
Generic OAuth availability does not prove Daybreak entitlement or endpoint access.

[Official OpenAI Codex authentication documentation][openaidocs], read on
2026-11-12, confirms browser subscription sign-in, automatic token refresh during
use (active sessions **usually** avoid another browser login), and device login
requiring enablement in account/workspace settings. Its MFA guidance does not
promise a specific hardware-key mechanism. This current web documentation is
context, not a version pin or evidence that Pi implements every Codex feature.
Revocation, account policy changes, expired/invalid refresh grants and uncertain
rotation can require a new browser login. No perpetual credential promise follows.

## Shared store versus a personal broker or inference proxy

| Option | Practical fit and additional responsibility |
| --- | --- |
| One canonical locked Pi auth store | Smallest solution for cooperating Pi-only workers on one account. One browser login per account, then coordinated refresh; workers can access the refresh credential. Validate actual namespace visibility and exact provider/model access later. |
| Broker returns temporary access tokens | Appropriate when workers should not possess refresh tokens or cannot share the canonical lock/storage. Broker is sole refresh authority; workers must not refresh copies. Requires token lifetime/freshness, caller/account binding and correct provider auth context. It is additional implementation, not required merely because workers are separate processes. |
| Personal codex-lb/inference proxy | Can own login/refresh and expose inference, so workers receive neither refresh nor upstream access tokens. It must support the exact upstream subscription API, request/response streaming, account routing and Daybreak model authorization; it sees full request/history content. A generic Responses-compatible URL does not prove those properties. This package did not inspect or validate the user's proxy. |

Recommendation: begin with one supported Pi login into one shared canonical
directory/store per actual account/provider binding. Choose a broker/proxy only
for a concrete credential-access or routing requirement. Keep legacy Codex's
rotating grant under its original authority until common ownership is proved;
never synchronize refresh-token copies between the two. All options retain the
same development-session namespace/tool authority; auth sharing is not process
or permission isolation.

## Scope and checks

Source investigation started 07:56 UTC and finished within the six-active-minute
first-pass cap. Fresh public source copies and the public OpenAI page are under
`/tmp/pi-auth-evidence-2026-11-12-implementer5` (disposable). A guessed catalog-data
path returned 404; it supplied no Daybreak evidence and was not used to infer
absence. No credentials/token files, peer-session records/transcripts/worktrees,
login attempts, hardware-key prompts, model calls, installations, tests/builds,
services, deployments or lifecycle actions were accessed or run. No application
edits, branches, commits or migrations. Source/reference and owned whitespace
checks only; no live safety, entitlement, crash or namespace proof. Evidence alone
does not trigger automatic independent review. Next: lead acceptance and
architect0 auth-only design reconciliation.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[file]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts#L63
[mutation]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts#L451
[refresh]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/resolve.ts#L102
[cache]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts#L377
[revision]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/utils/paths.ts#L80
[contract]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/types.ts#L50
[memory]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/credential-store.ts
[readonly]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts#L205
[overlay]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/runtime-credentials.ts
[dispatch]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/models.ts#L883
[responses]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/api/openai-responses.ts
[codexadapter]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/api/openai-codex-responses.ts
[codexoauth]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/oauth/openai-codex.ts
[directoauth]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/oauth/openai-chatgpt.ts
[tests]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/test/auth-storage.test.ts#L370
[openaidocs]: https://developers.openai.com/codex/auth/
