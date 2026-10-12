# DDNS exception: nil API user in the account-state check

Implementation update: the fix and channel pin are now merged. See
`verification.md` for final commits and passing request-level checks. The
investigation below records the evidence and proposal before implementation.

The exception is a vpsAdmin API bug. A DDNS request authenticates with a record
token and does not need a logged-in API user. When the record belongs to a
user-owned DNS zone, the account-state helper assumes `current_user` exists
and calls `current_user.role`, raising the reported exception.

## Evidence and request path

The attached email is dated 2026-09-14 21:00:05 +0200. It reports:

- `NoMethodError: undefined method 'role' for nil`.
- Action: `VpsAdmin::API::Resources::DnsRecord::DynamicUpdate`, API 7.0.
- `User: nil`, method `GET`, host `ipv6.ddns.vpsfree.cz`.
- Failure: `api/lib/vpsadmin/api/lifetimes.rb:624`.
- Deployed revision: `014fbc78422f3660b295add7a50f35cc7acdf0c8`, also the
  freshly fetched `origin/master` during this investigation.

At that revision:

1. `api/lib/vpsadmin/api/resources/dns_record.rb:197` defines DynamicUpdate;
   line 201 explicitly sets `auth false`.
2. `api/lib/vpsadmin/api/operations/dns_zone/dynamic_update.rb:12` finds an
   A/AAAA record through its update token. Line 17 invokes the action's block.
   The trace reached that block, so the token lookup succeeded.
3. `api/lib/vpsadmin/api/resources/dns_record.rb:214` calls
   `object_state_check!(record.dns_zone.user)` when `dns_zone.user_id` is set.
4. The helper at `api/lib/vpsadmin/api/lifetimes.rb:624` evaluates
   `next if current_user.role == :admin`. The email confirms `current_user`
   is nil. This is the nil receiver in the exception; it is not evidence of
   a missing DNS zone owner.

The exception happens before parsing the client IP, changing the record's
content, or firing the DNS update transaction chain. It also precedes the
unchanged-address shortcut, so a periodic refresh can fail even when the
address has not changed. This trace does not implicate DNS propagation or
the supplied IP address.

## Scope, origin, and test gap

The failing path applies to token-only DDNS updates in user-owned zones, for
both A and AAAA records. It does not depend on whether the owner is active:
the crash happens before reading the owner's state. Ownerless system zones
skip this helper. The email alone does not establish the affected owner's
actual account state or record type.

Commit `4e9a4a66bd1d7428d8f95977b9e529ed20fc708d`, dated 2024-08-13,
introduced the DDNS lifetime check and the operation's yield callback.
The helper's assumption about an authenticated caller predates that change.
The incompatible call has remained in place; this is a longstanding bug.

This is also the normal member workflow, not merely a special configuration:
`api/lib/vpsadmin/api/resources/dns_zone.rb:122` selects CreateUser for
non-administrators. `api/models/dns_record.rb:66` generates the token-only
URL for the same DynamicUpdate action. The configuration repository declares
`ipv4.ddns.vpsfree.cz` and `ipv6.ddns.vpsfree.cz` as aliases of the production
API in `cluster/cz.vpsfree/vpsadmin/common/frontend.nix:167`.

Consequently, normal generated DDNS URL requests for member-owned zones fail
in the deployed revision from the email. DDNS for ownerless system zones
does not encounter this exception, even if individual records have a user
assigned. Ordinary authenticated DNS-record edits use a separate action.

The operator confirmed that DDNS is primarily used with user-owned zones.
This therefore affects the primary production use case. The system-zone
exception explains the test coverage gap; it does not justify describing the
bug as low-impact or suggesting that most actual DDNS updates are unaffected.

The two-year interval describes source history. It does not prove two years
of continuous production failure or establish the exact number of members
using DDNS.
Production inspection was unavailable: the public WebUI hostname did not have
a trusted SSH host identity locally, and SSH to the known internal API host
`api1.int.vpsfree.cz` refused authentication. No database rows or request logs
were retrieved. Do not infer that most production DDNS updates are unaffected.

`api/spec/api/resources/dns_record_spec.rb:1576` currently covers a successful
anonymous DDNS request and an unknown token. Its successful record belongs to
`seed[:system_zone]`, which has no owner and skips the failing helper. The
operation specs call the operation directly without the action's lifetime
callback, so they do not exercise this failure either.

## Recommended fix

In `api/lib/vpsadmin/api/lifetimes.rb:624`:

```diff
-          next if current_user.role == :admin
+          next if current_user&.role == :admin
```

An anonymous caller then proceeds through the existing owner-state check.
Active owners pass; suspended and other non-active owners receive the existing
API error. Authenticated administrators retain their existing exception.
Keep the lifetime check in the DDNS action: skipping it for anonymous requests
would let record tokens bypass account restrictions.

The change requires no token regeneration, database migration, client change,
or node update. Deploy the API change to all serving instances; old instances
continue to fail during a rolling deployment. Rollback requires no data
conversion but restores the bug.

## Verification and implementation acceptance

`ruby work/2026-09-14-ddns-exception/reproduce.rb` loads the complete lifetime
helper source directly from the deployed Git revision. It uses synthetic
objects and applies the proposed one-line change only in memory.

All 43 assertions passed. The original helper reproduced `nil.role` for
anonymous callers with each of the five owner states. The proposed helper
allowed active owners and rejected every non-active state, preserving custom
and default error messages. Regular user, support, and administrator behavior
remained unchanged. A multiple-object check also retained its rejection.
See `reproduction.txt` for the output.

Before accepting an implementation, extend the existing HTTP request specs:

- Valid token, no API authentication, active user-owned zone: A and AAAA
  updates succeed, including unchanged-address refreshes.
- Valid token, suspended or otherwise non-active owner: normal API failure,
  no content change and no queued update transaction.
- Keep system-zone and invalid-token coverage, and cover administrator versus
  ordinary-user behavior for the shared helper.

This investigation did not run the database-backed suite or a live DDNS
request. No project code was edited, committed, pushed, or deployed.
