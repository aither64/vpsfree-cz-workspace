# Try the IP release flow

The development cluster was reset and runs the final batch-release implementation
on a single node with bridge networking. Both review VPSes are running. The
existing private credentials still work.

- [Campaign 1](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=show&id=1)
- [Campaign list](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=list)
- [Create campaign](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=new)
- [Mailpit](https://mailpit.aitherdev.int.vpsfree.cz/) collects development email.
- [API](https://api.aitherdev.int.vpsfree.cz/)

Sign out and back in to refresh any browser session from before the reset.
Credentials are in the private file
`/home/aither/.local/state/ip-release-review/2026-09-09-ip-release-mechanism/access.md`.
They are not included in this portal.

| Account | Role | VPS |
| --- | --- | --- |
| `test-admin` | Administrator, English | Both member VPSes are visible |
| `test-user1` | Member, Czech | 1, `ip-review-cs` |
| `test-user2` | Member, English | 2, `ip-review-en` |

## Fresh campaign

Campaign 1 is open with user opt-outs enabled. Its planned release date is
**23 September 2026, 22:08 UTC** (24 September, 00:08 CEST). No notices have been
sent, and there are no reasons, exemptions or release attempts. It shows
**Total: 5**, **Release: 5**, **Keep: 0**.

| Address | Owner | Fixture detail |
| --- | --- | --- |
| `198.51.100.20/32` | `test-user1` | Real, completed assignment to VPS 1 |
| `198.51.100.21/32` | `test-user1` | PTR: `review-ip.example.test.` |
| `2001:db8:106::/64` | `test-user1` | Public IPv6 allocation |
| `10.106.0.20/32` | `test-user1` | Private IPv4 |
| `198.51.100.22/32` | `test-user2` | Public IPv4 |

All five are owned and currently unassigned. Their charged environment and quota
usage have been checked. Addresses `.10` and `.11` remain assigned to the two
VPSes and are outside the campaign.

The [assignment history for 198.51.100.20](https://webui.aitherdev.int.vpsfree.cz/?page=networking&action=assignments&ip_addr=198.51.100.20&ip_prefix=32&list=1)
contains assignment chain **8** and removal chain **9**. The previous fixture
had no entry because it had never been assigned. Releasing ownership does not
remove assignment history.

1. As administrator, open campaign 1 and use **Send initial notices**. Open the
   resulting messages in Mailpit. Reminders become available after initial
   notices have been sent. **Notice history** records recipients and senders.
2. Sign in separately as each member. Open
   [request 1](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=request&id=1)
   for `test-user1`, or
   [request 2](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=request&id=2)
   for `test-user2`. Members see only their own addresses and release date.
   Try saving a reason or assigning an address to a VPS.
3. Administrators can select multiple addresses and set one exemption reason.
   Rows show who granted each exemption. Removing an exemption preserves any
   separately submitted user reason.
4. **Edit campaign** changes the date or user opt-out policy. Edits do not send
   email. Administrator exemptions and VPS assignments protect addresses under
   either policy. Reminders use the current date and policy.
5. **Release eligible addresses** starts one transaction chain for the entire
   eligible batch. The early-release warning is advisory. Every selected address
   stays owned and charged until the final successful confirmation applies the
   whole batch. Refresh to inspect the campaign-level result and numbered chain
   link. The PTR on `.21` should disappear when that address is released.

A preparation failure releases nothing and records the cause. After a completed
rollback, ownership and quota remain intact and an administrator can retry.
Repeated submissions while a batch is active return that attempt. An outcome
requiring operator attention prevents another release until the chain has been
reconciled. Changing the policy or closing the campaign does not cancel an
already prepared batch.

**Close without releasing IPs** ends further campaign actions and retains
history. Remaining addresses stay owned. A closed campaign cannot be reopened.
Members have no access to notice history, release attempts or other users' IPs.

## Selection and counts

Creation selects only owned, unassigned and unused allocations. VPS assignments,
routing dependencies, export grants and active resource locks exclude an
allocation. Release rechecks current ownership and use before changing anything.
The default filter is public IPv4. Networks, locations and IP versions support
multiple selections; user ID and public/private access can also be filtered.

Campaign address pages contain 500 rows. There is no campaign allocation limit.
The header checkbox selects editable rows on the current page; the creation
preview also supports selecting all matches across pages.

The administrator list has separate **Total**, **Release** and **Keep** columns.
Details show **Total**, **To be released** and **Kept**. Each subnet counts once.
Total includes historical rows, so the other two figures need not add up to it.
Tooltips explain each count.

Allocation IDs and fixture details are in
[review-inventory.json](review-inventory.json). Implementation commits and locking
boundaries are in [commit-map.md](commit-map.md).
