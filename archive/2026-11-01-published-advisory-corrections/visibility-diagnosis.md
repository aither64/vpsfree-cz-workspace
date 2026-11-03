# Advisory visibility diagnosis

Read-only reproduction at running API/legacy source `49f5a29e5a7d85559d06d31496acb5c08895bcda` on the exact same-session development cluster. No source, fixture or configuration changes. The three synthetic advisories remain draft1, published2 and retracted3; API49f5 source is clean. Credentials and response bodies are private and not included here.

## Observed API behavior

| Reader | Original list | Draft1 | Published2 | Retracted3 |
| --- | --- | --- | --- | --- |
| Anonymous | IDs3,2 | 404 | 200 | 200 |
| Ordinary seeded member | IDs3,2 | 404 | 200 | 200 |
| Administrator | IDs3,2,1 | 200 | 200 | 200 |

Routes: `/v7.0/security_advisories` and `/v7.0/security_advisories/:id`. Anonymous/member nested `/security_advisories/1/node_statuses` returns an empty list; `/3/node_statuses` returns the retracted assessment row3. CVE detail `/security_advisory_cves/1` is 404 for anonymous/member; `/3` returns200. Admin sees all existing originals and child rows.

Correctly wrapped anonymous list filters with `_meta[count]=true` confirm draft→empty/count0, published→ID2/count1, retracted→ID3/count1. Earlier diagnostic flat query parameters were ignored by HaveAPI and are not filter evidence. The unfiltered/detail results from that matrix remain valid.

Update and outage-link lists are empty in this preview, so they establish route accessibility but not populated-child visibility. No new update/outage fixture was created during reproduction; populated cases belong in focused regressions.

## Observed legacy behavior

Fresh cookie-free HTTPS requests show IDs2+3 in `?page=security_advisory&action=list`; state=draft is empty; state=retracted shows3. Direct show?id=1 returns a PHP200 error page without the draft marker; show?id=2 and3 return200 and render their own marker. No anonymous logout form was present. A fresh pinned Luna/low normal-CA browser observation passed in82seconds across21read-only pages: anonymous and ordinary-member lists/details show2+3, draft filter/detail contains no draft marker; administrator list/details and filters expose all three states correctly. Current member/admin identities were checked through the normal OAuth login/logout-form account marker. No TLS bypass or advisory write. Exact role/route/status/ID results are retained in `legacy-roles-result.json`.

The user-reported public draft exposure is not reproduced in these fresh anonymous API/PHP requests. This does not waive the requested admin-only draft boundary or cache/logout regressions. Retracted exposure is confirmed.

## Root cause and shortest fix

`api/models/security_advisory.rb` implements `visible_to(nil/nonadmin)` as published **or retracted**. Original list/detail, original pagination cursor, node-assessment list, CVE list/detail, update list/detail, affected-user/VPS lists, and outage-advisory link list/detail already consume that shared scope. The shortest server-authoritative correction is published-only for non-admins, retaining unrestricted admin access and scoped not-found/empty behavior.

Existing resource example “shows only published advisories to public readers” creates draft+published only, so it does not catch retracted exposure. Extend meaningful state/role tests through list/count/filter/cursor/detail and populated child/related/include paths rather than adding UI-only filtering.

Legacy list/detail rely on API results; administrative mutation routes already call `isAdmin()`. `Outage#index` also accepts a security-advisory filter and joins links without its own explicit advisory scope: the architect should settle the bounded resource-resolution/include/filter exposure contract before edits. No general authorization framework or broader audit is proposed.

Private evidence: `/tmp/2026-11-01-published-advisory-corrections-visibility/` contains the sanitized API matrix, wrapped filter/count results and private raw responses. The bounded read-only observer finished with exit0 and closed its browser; no verification utility remains active. Cluster guests intentionally stay running. Source and fixture state remain unchanged pending the architect brief.
