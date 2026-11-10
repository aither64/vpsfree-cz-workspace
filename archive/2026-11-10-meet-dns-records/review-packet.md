# Final review packet: meet DNS aliases

Status: committed implementation complete; quick checks passed; ready for final review.

## Request and acceptance

User requests auth.meet -> meet.vpsfree.cz., auth.test-meet ->
test-meet.vpsfree.cz., turn.meet -> jvb1.vpsfree.cz., and turn.test-meet ->
test-jvb01.vpsfree.cz., in both public/private vpsfree.cz zones, with a comparison
of private meet records. Every mapping must exist exactly, have no conflicting
owner data, resolve to the intended address and preserve unrelated records.

Only relevant private target parity is approved: replace legacy turn.meet A/AAAA,
add test-meet -> test-meet-nixos, test-meet-nixos A 37.205.13.90, and test-jvb01 A
37.205.14.250. Preserve private meet -> meet-dev A 37.205.14.113 and unrelated
legacy names. Increment serials. No wider private cleanup, new abstractions,
permanent tests, inputs or service configuration. Implementation excludes
merge/deployment; user later approved configuration/master integration after
verification and will deploy personally.

## Context and review policy

Session 2026-11-10-meet-dns-records; context [plan](plan.md), [state](state.md),
[design](design.md). Project vpsfree-cz-configuration, worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-10-meet-dns-records/vpsfree-cz-configuration.

Selected reviewer: retained reviewer0, gpt-6.1-sol/xhigh, read_only. No fallback.
Risk classified high to cover the changed public DNS contract, private TURN
IPv4/IPv6 behavior and DNS serial/rollback semantics. Lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. This is a
small data-only change; apply those concerns proportionately. Read the mandatory
review skill and all selected lane references. Review directly without nesting.

## Compatibility and documentation

Standard DNS data; no application state, database or schema migration, API/client,
CLI, Terraform, daemon protocol, Nix module interface or version/input change.
Private turn.meet changes from legacy IPv4/IPv6 to jvb1 IPv4. New aliases are
additive. Existing CNAME chains are intentional. Future DNS activation needs
normal authoritative reload/secondary propagation; old caches may persist for
one hour. Recovery after publication restores old data with a higher serial.
No deployment executed; no endpoint-service functionality claim is made.

Documentation inventory: alias mapping -> DNS maintainer/reference -> both zone
files; compatibility/recovery -> operator/current execution context -> design.md;
verification -> reviewer/session evidence -> implementation evidence and state.md.
No project prose change is useful for this small zone-data edit. Existing
reusable rollback guidance in docs/operations/newadmin-webui.md is preserved;
no instructions were moved or retired. Assess this placement justification.

## Revision and verification inventory

Base: 959e1d54cabc7ac5530dac6179acacb077a57754 (origin/master).
Final head: 0c6b844e404ba957c1d48d892479ad704d2b22f0, published SSH branch
2026-11-10-meet-dns-records. Lead independently checked remote master/feature
refs with git ls-remote; remote refs match these revisions.

Complete series: one commit, 0c6b844e dns: add meet auth and turn aliases in both
views. Intended split: one coherent static DNS-data change with required target
parity and serials. No superseded approaches, follow-up source fixes, repeated
input/dependency/generated-artifact updates or compatibility paths. A local
commit-message shortening before publication changed the hash without source
change. No migrations (none merged/released/deployed/externally consumed), no
schema/input changes and no deployment.

Changed files: configs/internal-dns/zone.vpsfree.cz. (+8/-3) and
configs/public-dns/zone.vpsfree.cz. (+5/-1), total +13/-4.

Implementer reports quick checks PASS using BIND 9.20.29 from
`nix shell --inputs-from . nixpkgs#bind`: canonical before/after public and four
substituted private templates; exact mappings/TTL/terminal addresses, owner
exclusivity, serial advance and unrelated-record preservation. git diff --check
passes. Nixfmt and commit-message hooks pass; TextWidth has a nonblocking warning
and final commit lines are <=80. Worktree clean. No applicable branch CI exists;
only scheduled/manual daily-update workflow. Detailed commands and outputs are
being preserved in [package-b-evidence.md](package-b-evidence.md); inspect this
and source before conclusions and request missing evidence if needed.

Full final diff follows (also independently inspect repository series).


```diff
diff --git a/configs/internal-dns/zone.vpsfree.cz. b/configs/internal-dns/zone.vpsfree.cz.
index 5e86e992..c976437c 100644
--- a/configs/internal-dns/zone.vpsfree.cz.
+++ b/configs/internal-dns/zone.vpsfree.cz.
@@ -1,7 +1,7 @@
 $ORIGIN vpsfree.cz.
 $TTL 1H                  ; default expiration time of all resource records without their own TTL value
 @  IN  SOA  @fqdn@. podpora.vpsfree.cz. (
-              2026110600 ; serial number of this zone file
+              2026111000 ; serial number of this zone file
               1D         ; slave refresh (1 day)
               2H         ; slave retry time in case of a problem (2 hours)
               4W         ; slave expiration time (4 weeks)
@@ -206,10 +206,10 @@ jicofo.meet                    IN   A       37.205.14.91
 jicofo.meet                    IN   AAAA    2a03:3b40:fe:40::1
 jvb1.meet                      IN   A       37.205.14.146
 jvb1.meet                      IN   AAAA    2a03:3b40:fe:59::1
-turn.meet                      IN   A       37.205.14.152
-turn.meet                      IN   AAAA    2a03:3b40:fe:76::1
+turn.meet                  300 IN   CNAME   jvb1.vpsfree.cz.
 meet-dev                       IN   A       37.205.14.113
 meet                           IN   CNAME   meet-dev.vpsfree.cz.
+auth.meet                  300 IN   CNAME   meet.vpsfree.cz.
 jitsi-videobridge.meet         IN   A       37.205.14.168
 jitsi-videobridge1.meet        IN   CNAME   jitsi-videobridge.meet.vpsfree.cz.
 jitsi-videobridge2.meet        IN   A       37.205.14.153
@@ -233,6 +233,11 @@ jvb8                           IN   A       37.205.14.219
 jvb9                           IN   A       37.205.14.231
 jvb10                          IN   A       37.205.14.250
 jvb11                          IN   A       37.205.13.90
+test-meet-nixos            300 IN   A       37.205.13.90
+test-meet                  300 IN   CNAME   test-meet-nixos.vpsfree.cz.
+test-jvb01                 300 IN   A       37.205.14.250
+auth.test-meet             300 IN   CNAME   test-meet.vpsfree.cz.
+turn.test-meet             300 IN   CNAME   test-jvb01.vpsfree.cz.
 
 ; aitherdev
 aitherdev.int                  IN   A       172.16.106.40
diff --git a/configs/public-dns/zone.vpsfree.cz. b/configs/public-dns/zone.vpsfree.cz.
index f0c531fd..9051a9e1 100644
--- a/configs/public-dns/zone.vpsfree.cz.
+++ b/configs/public-dns/zone.vpsfree.cz.
@@ -1,7 +1,7 @@
 $ORIGIN vpsfree.cz.
 $TTL 1H                  ; default expiration time of all resource records without their own TTL value
 @ IN  SOA  ns1.vpsfree.cz. hostmaster.vpsfree.cz. (
-              2026092800 ; serial number of this zone file
+              2026111000 ; serial number of this zone file
               1D         ; slave refresh (1 day)
               2H         ; slave retry time in case of a problem (2 hours)
               4W         ; slave expiration time (4 weeks)
@@ -55,6 +55,8 @@ meet					300 IN CNAME	meet-nixos.vpsfree.cz.
 meet-dev				300 IN CNAME	meet-nixos.vpsfree.cz.
 meet-dev1				300 IN CNAME	meet-nixos.vpsfree.cz.
 meet-nixos				300 IN A	37.205.14.113
+auth.meet				300 IN CNAME	meet.vpsfree.cz.
+turn.meet				300 IN CNAME	jvb1.vpsfree.cz.
 jvb1					300 IN A	37.205.14.138
 jvb2					300 IN A	37.205.14.150
 jvb3					300 IN A	37.205.14.163
@@ -69,6 +71,8 @@ jvb11					300 IN A	37.205.13.90
 test-meet-nixos         300 IN A    37.205.13.90
 test-meet               300 IN CNAME test-meet-nixos.vpsfree.cz.
 test-jvb01              300 IN A    37.205.14.250
+auth.test-meet          300 IN CNAME test-meet.vpsfree.cz.
+turn.test-meet          300 IN CNAME test-jvb01.vpsfree.cz.
 
 caladan		IN	CNAME	caladan.hawin.cz.
 tor-relay	IN	A	37.205.8.191
```
