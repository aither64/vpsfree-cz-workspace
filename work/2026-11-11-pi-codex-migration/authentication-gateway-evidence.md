# Shared authentication or a personal inference gateway

Package L, architect2, 2026-11-12. G was reported complete and accepted before
this assignment. Only this evidence file is owned; architect0 owns design
synthesis and the lead owns tracking and the user answer. Current/environment
and the same-session roster match the bound session. Required guidance and the
documentation skill were reused from this context; additional owning source
instructions were read. This is a bounded source assessment, not an auth audit.

**A personal codex-lb can centralize login and renewal, but it is not necessary
merely to avoid logging in each Pi worker.** Pi already coordinates renewal
through one canonical credential store. Use that simpler option initially for
trusted same-user Pi workers, with explicit account/profile selection. Prefer a
central inference gateway when keeping upstream credentials out of workers,
central account policy or sharing the same credential authority with legacy
clients is a real requirement—and only after its exact Daybreak path passes
acceptance. A token broker is a third design, not another name for that proxy.

“Login once” means reusing a renewable grant. Revocation, account changes,
expired refresh credentials or an upstream step-up challenge can require
interactive login again. None of these designs guarantees permanent login or
multiplies the subscription's quota/rate limits.

## Three distinct designs

| Design | Credential and request ownership | Benefit | Cost / failure boundary |
| --- | --- | --- | --- |
| Locked canonical Pi store | Pi workers share one authoritative provider credential and lock; each worker sends inference directly and may perform the serialized refresh | Smallest change, no new service, one Pi login per account/profile rather than per worker | Workers can read refresh credentials and alter shared login/logout state. The same underlying store and lock must be visible across mount namespaces; copying files creates independent rotation authorities. Store/lock failure affects users of it |
| Token broker | Broker alone retains/refreshes the grant; workers obtain short-lived access credentials and use their own upstream transport | Central refresh and account selection without relaying every response; workers need no refresh token | Workers still possess usable bearer tokens. Custom trusted integration must supply expiry, correct account/audience/client binding and refresh-before-expiry. Worker SDK still owns all Daybreak/Responses/WebSocket compatibility. Broker failure blocks new tokens; already issued valid tokens may keep working until expiry |
| Inference gateway, such as codex-lb | Gateway owns upstream credentials/refresh and sends upstream requests; workers use gateway credentials | Upstream tokens stay out of workers; centralized profile selection, accounting and admission | Every inference depends on gateway availability/capacity and its protocol handling. Gateway receives prompts/results and owns account routing, streaming, reconnect and errors. Its key is not an upstream subscription OAuth token |

An auth/inference service is an external control-plane resource, not a shared
agent host. Keep every development session's lead, workers and tool processes
inside its own cgroup/mount namespace. Account for gateway resources separately.
Shared files or a gateway do not themselves isolate credentials from a trusted
operator with unrestricted host access; they define ordinary application access
and reduce what worker processes need to receive.

## What the pinned source establishes

P = Pi `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`; N = Codex 0.165.0
`360319d8dee62d87e2d59fc0c21805d79519cfed`. Reuse
[provider/fallback evidence](provider-fallback-evidence.md) for the wider
provider contract; no repeated architecture inventory was performed.

- P [`AuthStorage`][store] locks the resolved file, including symlink aliases.
  [`refreshStoredOAuthCredential()`][refresh] rereads under the store lock,
  refreshes only if still needed and persists before release. Once exchange
  starts it survives caller cancellation so a rotated refresh token is not
  discarded. This coordinates cooperating Pi writers, not native Codex or a
  gateway using a different store/protocol.
- The store holds one credential per **provider ID**, not arbitrary account or
  member IDs. Two profiles under the same provider need separate canonical
  stores or an explicitly account-aware view/service. Model/member switching
  must not mutate a shared provider's account globally. Separate profiles must
  not be independent copies of the same rotating grant.
- P [`openai-codex` OAuth][codex-oauth] has browser PKCE and device-code paths,
  uses the Codex client `app_EMoamEEZ73f0CkXaXp7hrann`, scopes
  `openid profile email offline_access`, and extracts the ChatGPT account ID.
  Its browser flow uses a localhost:1455 callback or manual redirect input.
  Browser authentication is a suitable place for an upstream hardware-key
  challenge, but source support for opening the browser is **not proof** that
  this user's required challenge and Daybreak entitlement succeed.
- P's separate [`openai` ChatGPT OAuth][chatgpt-oauth] registers a dynamic client,
  retains its issued client ID, targets resource `https://api.openai.com/v1`
  and requires `chatgpt.tokens.use.direct`. It is a different grant and endpoint
  from `openai-codex`. Neither a paid API key nor a copied native login can be
  assumed interchangeable with the user's subscription binding.
- P [`openai-codex-responses`][pi-transport] uses ChatGPT's Codex Responses path,
  extracts account identity from the bearer token, sets Authorization and
  `chatgpt-account-id`, supports WebSocket/SSE, and uses transport-specific beta
  headers. Its inspected request builder has no explicit Daybreak/cyber program
  field. This is a bounded finding, not a claim that an extension cannot add
  supported behavior. In particular, pointing this adapter at a proxy with a
  plain gateway API key is not automatically valid: account extraction expects
  an upstream JWT. Select and verify the gateway-facing adapter explicitly.

## The existing codex-lb reference

Canonical configuration default at
`dda57166bd8bb6d85a74decdd05a8810933bdecc`
[`aitherdev/config.nix`][configuration] defines a personal
`ghcr.io/soju06/codex-lb:1.21.0` image pinned to digest
`sha256:f8f24d08d7cb4b993e64a52ed87b8eb769788a60df8e921665e817523d0ab945`.
It also separately defines the provider labelled “Snajpa codex-lb”. The public
upstream `v1.21.0` tag resolves to
`8a20de0b5abf6bb6c65c12d47b22956d167baee1` (L below). No source/image
equivalence or deployed-state proof was attempted.

The source definition maps local ports 2455/1455 and configures nginx to reject
`/v1/` and `/backend-api/codex/` paths while forwarding other paths. This
describes that nginx entry point; it does **not** establish that local workers
cannot reach an internal API. No listener, network or service was probed.

L's [OAuth implementation][lb-oauth] constructs browser PKCE authorization,
adds offline access, and exchanges credentials. Its [settings][lb-settings]
use the same static Codex client ID, localhost callback and ChatGPT backend
family as P's Codex adapter. [OAuth service][lb-login] stores encrypted token
material; [refresh claims][lb-refresh] coordinate its own replicas. These are
source capabilities, not proof of compatibility with another grant owner.

L is an inference proxy, not a demonstrated access-token-only broker. Its
[proxy code][lb-proxy] strips inbound Authorization/account routing and rebuilds
upstream credentials/headers, including client identity normalization. It is
therefore not a transparent tunnel. The [Responses spec][lb-responses] covers
streaming/WebSocket continuity and security-work-authorized account routing.
That routing flag and generic API compatibility do not prove Daybreak access.
No explicit end-to-end Daybreak guarantee was established in the inspected
source. Existing credential-export shapes include refresh tokens; exporting
them does not create a safe broker contract.

Reuse remains optional. The inspected project is MIT-licensed and publishes
versioned source/specs; this is not a security or maintenance endorsement.
The gateway becomes a credential holder and protocol dependency, requiring a
pinned package, retained encryption/database recovery and relevant upgrade
checks. No ecosystem search, installation or new gateway implementation is
proposed by this evidence.

## Daybreak and coexistence constraints

The user's required route is subscription-backed Daybreak with a hardware key.
Keep that as an acceptance requirement. Hardware-key authentication, OAuth
grant issuance/renewal, account entitlement, model discovery and request
program selection are separate checks. Successful ordinary chat proves only
ordinary chat. A model alias in a catalog does not prove the rest.

N [`tui/daybreak.rs`][daybreak] selects per-turn programs using account
eligibility and `available_access_programs` model metadata. Native feature
checks also distinguish API-key program forwarding. N's [access tests][access]
exercise account-bound `/accounts/verified_access` requests and entitlement
context on eligible plugin calls. This establishes more than a model-name
substitution; it does not say every inference requires that plugin call.
The fixed native source also has an API-key path under explicit support flags;
that does not establish access for this user or relax the requested subscription
route. Hardware-key success and gateway/Pi Daybreak parity remain unproved.

Legacy Codex remains writable under its existing auth authority. **Do not copy
its login into Pi or codex-lb and let both renew it.** File locking in Pi cannot
coordinate native Codex's refresh, and gateway database claims cannot coordinate
either independent writer. One rotating grant needs one cooperating renewal
authority. A separate supported login/grant for Pi is the least coupled
transition; verify that its issuance and refresh do not invalidate legacy use.
If one grant across both is required, use a supported external-auth integration
to the common owner and prove both clients' refresh/restart behavior first.
No such installed integration was verified here. Preserve client ID, scopes,
account/workspace identity and issuance provenance; never reinterpret token
formats or silently fall back to a different account.

## Small acceptance path, not performed

1. With a later explicit test assignment, fix one account/profile, exact
   subscription model/program, client/grant path and pinned adapter/gateway.
   Record only nonsecret identity/version evidence. Complete the upstream
   browser/hardware-key flow through the intended callback path; verify the
   actual account/workspace and entitlement. A device-code flow is not assumed
   equivalent to the required browser challenge.
2. In two disposable Pi session workers, exercise concurrent expiry/refresh and
   a worker restart. Prove one successful persisted rotation, continued use by
   both workers, preserved profile selection and unaffected legacy Codex.
   Use mocks for race/crash cases before any authorized live check. Never test
   this by cloning a live refresh token.
3. Compare the verified direct route with the proposed gateway/broker route:
   one tiny benign request on the **exact Daybreak binding**, then one minimal
   continuation/tool round trip. Verify model/access-program and account
   routing, required headers and Responses behavior, WebSocket continuity and
   SSE policy, error/entitlement visibility and shared quota accounting.
   Do not fabricate entitlement metadata or client claims to make it pass.
4. With fixtures, test expired credentials, renewal failure, gateway/broker
   outage, cancellation and partial stream/reconnect. Confirm bounded retries,
   no cross-profile fallback, no duplicated tool effects and no secrets in
   logs. A failure of the Daybreak route leaves it unavailable and the proven
   legacy route intact; it does not trigger additional proxy research by default.

Research stayed within the six-active-minute cap and stopped at these seams.
Only public pinned source and committed configuration were inspected. No live
auth files, credentials, login/hardware-key prompts, model requests, runtime
probes, builds, services, deployment or lifecycle actions occurred. Source and
reference checks are evidence checks, not runtime acceptance. No automatic
independent review is triggered by this planning artifact.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[store]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts#L84
[refresh]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/resolve.ts#L106
[codex-oauth]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/oauth/openai-codex.ts#L359
[chatgpt-oauth]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/oauth/openai-chatgpt.ts#L15
[pi-transport]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/api/openai-codex-responses.ts#L541
[configuration]: https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/dda57166bd8bb6d85a74decdd05a8810933bdecc/cluster/cz.vpsfree/machines/aitherdev/config.nix#L59
[lb-oauth]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/app/core/clients/oauth.py#L65
[lb-settings]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/app/core/config/settings.py#L157
[lb-login]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/app/modules/oauth/service.py#L653
[lb-refresh]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/app/modules/accounts/refresh_claims.py#L211
[lb-proxy]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/app/core/clients/proxy.py#L621
[lb-responses]: https://github.com/Soju06/codex-lb/blob/8a20de0b5abf6bb6c65c12d47b22956d167baee1/openspec/specs/responses-api-compat/spec.md#L1307
[daybreak]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tui/src/daybreak.rs#L8
[access]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/tests/suite/daybreak_access.rs#L48
