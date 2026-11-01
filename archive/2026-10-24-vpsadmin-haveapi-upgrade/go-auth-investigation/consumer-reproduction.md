# Go token documentation: read-only consumer reproduction

The reported message is reproduced in the current anonymous development documentation, specifically `auth-token-go`. Go initialization, Basic and OAuth2 auth, and the public cluster-stats action render code. This identifies an observed renderer limitation; it does not establish that the published Go client lacks token support. Architect0 owns the renderer/SDK diagnosis.

## Evidence and identity

Session/current binding and saved implementer0 workspace-write roster were verified; this package stayed read-only outside its own investigation record. Canonical vpsAdmin HEAD is `9697bf28c3171d4ee3e0980160be60764ae2c4aa`. The API7.0 Go profile has only `import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client'`; no SDK snapshot/version or token-transport override. [Profile excerpt](configured-profiles.rb.txt); source api/lib/vpsadmin/api.rb SHA256 `c6b60c185b27d75d9d194cb184f77a328b44dd027717cb57d8063aabdeb26566`.

Existing [E4 runtime receipt](../devcluster/e4-runtime/receipt.md) binds the deployed API package `/nix/store/5dvc6xqgq3389ds72fw6d47yihpc3zb6-vpsadmin-api-9697bf28c3171d4ee3e0980160be60764ae2c4aa` and all five HaveAPI packages0.31.1, including Go generator0.31.1. [Packaged identities](../devcluster/e4-runtime/packaged-identities.json) are package/closure evidence, not new per-process introspection. No guest or native status query was made.

E4 retained body metadata, not a raw HTML file in its evidence directory. Therefore one authorized anonymous GET was made to `https://api.aitherdev.int.vpsfree.cz/v7.0/`, explicit English/HTML, with curl configuration disabled, empty Authorization/Cookie, strict workspace CA verification, no redirect/retry. Curl exit0/HTTP200/TLS verification0. [Request record](request.json) includes exact arguments. The [raw public body](public-body.html) was saved before assertions: 2,811,894 bytes, SHA256 `591952089773748c2c2e891f662eaf275c4ecb1349079cf1ff8eb8382fc5eaa5`. This is exactly the SHA256/size already recorded in E4 docs.json. No credentials, login, tokens, timings or member mutation were used.

## Observed panels

[Extracted Go panels](selected-go-panels.txt), [structured selection](selected-go-panels.json), [panel counts](panel-summary.json). These are emitted HTML/program observations; programs were not compiled or executed in this investigation.

| Panel | Observed output |
| --- | --- |
| init-go | Code imports the configured SDK and calls client.New with the development API base |
| auth-basic-go | Code calls SetBasicAuthentication using environment placeholders |
| auth-token-go | Exactly: “This authentication method does not match the configured Go SDK.” |
| auth-oauth2-go | Code calls SetExistingOAuth2Auth using an environment placeholder |
| example-cluster-public_stats-0-go | Code prepares Cluster.PublicStats, calls the invocation and reads output fields |

The token-auth warning occurs once. There are17 Go action panels:16 render code; `example-vps-index-0-go` separately renders “This response field is unavailable in the configured Go SDK.” No general Go rendering failure is observed. The token message also appears in all three preserved0.31.1 fixture responses from the earlier authorized role checks; this investigation did not repeat those requests.

The public Token transport description advertises HTTP header `X-HaveAPI-Auth-Token` and query parameter `_auth_token`. [Raw transport context](token-transport-context.html), [exact visible values and type limit](token-visible-values.json). These match the SDK transport names reported by architect0, but HTML does not expose saved/visible Ruby hash key classes or value types. No OPTIONS request, model/Context introspection or compatibility conclusion was added.

Exact consumer/profile/panel facts and this type-evidence gap were sent directly to architect0. No application, lock, Git, dependency, package, KB, provider, cluster or lifecycle edits; no test/build/benchmark/retry campaign or stopped upstream work resumed. Single GET is complete, no active command/writer remains. Lead owns the main session state and next decision.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/).
