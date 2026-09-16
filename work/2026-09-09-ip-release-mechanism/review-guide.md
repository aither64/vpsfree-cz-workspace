# Try the IP release flow

The single-node development cluster uses the bridge network. The API runs
vpsAdmin `58a9b71ea` with the matching WebUI and notification templates. Campaign addresses use 500-row pages.

- [Campaign list](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=list)
- [Create campaign](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=new)
- [Mailpit](https://mailpit.aitherdev.int.vpsfree.cz/) collects development email.
- [API](https://api.aitherdev.int.vpsfree.cz/)

Sign out and in once to refresh an existing WebUI session after the API update. Login refreshes its cached API description.

Credentials remain in the private file
`/home/aither/.local/state/ip-release-review/2026-09-09-ip-release-mechanism/access.md`.
They are not included in this portal.

| Account | Role | VPS |
| --- | --- | --- |
| `test-admin` | Administrator, English | Both member VPSes are visible |
| `test-user1` | Member, Czech | 1, `ip-review-cs` |
| `test-user2` | Member, English | 2, `ip-review-en` |

## Review campaign

Open [campaign 3](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=show&id=3)
as `test-admin`. User opt-outs are enabled; the planned release date is
**22 September 2026, 17:38 UTC** (19:38 CEST). It contains:

| Address | Owner |
| --- | --- |
| `198.51.100.23/32` | `test-user1` |
| `2001:db8:106:1::/64` | `test-user1` |
| `10.106.0.20/32` | `test-user1`, private IPv4 |
| `10.106.0.22/32` | `test-user2`, private IPv4 |

Both members have received an initial notice. The saved reason for
`198.51.100.23/32` is preserved: the campaign currently shows **Total: 4**,
**To be released: 3**, **Kept: 1**.

1. Review the separate navigation and campaign sections in the sidebar.
   **Send initial notices** appears while eligible members remain without an
   initial notice. **Send reminders** appears for previously notified members
   with eligible addresses.
2. Select addresses from both members, enter one exemption reason and click
   **Set exemption**. Rows identify the administrator by login and numeric ID.
   Select them again and use **Remove exemption** to undo the trial.
3. Send an initial notice or reminder, then open the messages in Mailpit.
   Subjects and text/HTML bodies use singular or plural wording for the actual
   address list. Locations appear in parentheses, and the button opens the
   member request.
4. In separate browser sessions, sign in as each member and open
   [request 4](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=request&id=4)
   for `test-user1` or
   [request 5](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=request&id=5)
   for `test-user2`. Each member sees their own addresses, release date and
   retention controls. Try saving a reason or assigning an address to a VPS.
5. As administrator, try a reminder or change the policy through **Edit
   campaign**. Disabling user opt-outs leaves saved reasons visible but changes
   whether they protect the addresses. Assignments and administrator exemptions
   still protect them.
6. Use **Release eligible addresses** to trigger release. The date warning is
   advisory. Refresh to inspect the result and any cleanup transaction.

**Notice history** records initial notices and reminders. Administrators can
inspect recipients and who sent them. Members have no notice-history access;
their sidebar links to Networking and their own request list, including closed
requests.
**Close without releasing IPs** ends campaign actions without changing remaining
ownership. Existing releases continue. A closed campaign cannot be reopened.

The admin campaign list and details show **Total**, **To be released** and
**Kept**. Kept includes addresses in use, administrator exemptions and reasons
honored under the current policy. Total also includes historical rows, so the
figures need not add up. Each subnet counts once. Hover over a count for its
explanation. Members do not see these campaign totals.

Use the checkbox in the first table header to select editable addresses on the
current page. It has no visible label; its tooltip explains the scope.

## Creation and filters

The preview includes only user-owned addresses that are unassigned and unused.
Assigned host addresses, routing dependencies, export grants and active resource
locks exclude an allocation. The release action checks eligibility again.

The default filter is public IPv4. Networks, locations and IP versions allow
multiple selections; user ID and public/private access can also be filtered.
There is no campaign allocation limit. **Select all matches** and **Clear
selection** apply across the entire preview, with 500 addresses per page.

`10.106.0.21/32` is a spare private address owned by `test-user1` and outside
campaign 3. Select private access and user ID `2` to preview it. Public addresses
`198.51.100.24/32` and `198.51.100.25/32` also remain available for another campaign.

## Preserved campaigns

Campaign 1 retains its notices and the user's saved reasons. It contains `.20`,
`.21`, `.22`, `2001:db8:106::/64` and the second member's `.26`. The PTR on `.20`
is `review-ip.example.test.`.

Campaign 2 retains the earlier release validation: `.27` and
`2001:db8:106:2::/64` were released, the PTR on `.27` was removed, and `.28`
remains administrator-exempted. Assigned controls are `.10` on VPS 1 and `.11`
on VPS 2. The update preserved both VPSes and all existing campaign records.

Allocation IDs and the campaign inventory are in
[review-inventory.json](review-inventory.json).
