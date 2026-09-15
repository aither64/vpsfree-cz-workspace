# Try the IP release flow

The single-node development cluster uses the bridge network and published
vpsAdmin revision `a75bb80d5`. The two member VPSes are running. The addresses below use documentation ranges and the cluster's
public-address pool.

- [WebUI](https://webui.aitherdev.int.vpsfree.cz/)
- [Mailpit](https://mailpit.aitherdev.int.vpsfree.cz/) collects development email.
- [API](https://api.aitherdev.int.vpsfree.cz/)

Credentials are in the private file
`/home/aither/.local/state/ip-release-review/2026-09-09-ip-release-mechanism/access.md`.
They are not included in this portal.

| Account | Role | VPS |
| --- | --- | --- |
| `test-admin` | Administrator, English | Both member VPSes are visible |
| `test-user1` | Member, Czech | 1, `ip-review-cs` |
| `test-user2` | Member, English | 2, `ip-review-en` |

## Prepared campaign

Open [Unassigned IP review, campaign 1](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=show&id=1)
as `test-admin`. It has not sent any notices. User opt-outs are enabled and the
planned release date is **22 September 2026, 14:44 UTC** (16:44 CEST).

The campaign contains unassigned addresses from both members in one table:

| Address | Suggested use |
| --- | --- |
| `198.51.100.20/32` | Leave eligible; its PTR is `review-ip.example.test.` |
| `198.51.100.21/32` | Save a member reason |
| `198.51.100.22/32` | Assign to VPS 1 |
| `2001:db8:106::/64` | Try an administrator exemption |
| `198.51.100.26/32` | Belongs to `test-user2`; include it in a bulk exemption |

1. Open **Cluster → IP release campaigns**. Use **Create campaign** in the
   sidebar to preview other eligible addresses, or open the prepared campaign.
   Its settings, addresses and action links are separate. The address table
   identifies each owner and includes checkboxes and **Select all**.
2. Select addresses from both members, enter one reason, and click **Set
   exemption**. The rows show the administrator's login, numeric ID and time.
   Select them again and use **Remove exemption** to undo this trial.
3. Choose **Send initial notices** in the sidebar and submit its form, then open the message for
   `test-user1@example.test` in Mailpit. It contains plain text, HTML, location
   labels and the button to open the request.
4. Use a separate browser session for `test-user1`. Follow the email button,
   sign in through **Log In** if needed, and open
   [request 1](https://webui.aitherdev.int.vpsfree.cz/?page=ip_release&action=request&id=1).
   Select `.21` and enter a reason. Use **Assign to a VPS** for `.22`.
5. In the administrator session, select the IPv6 subnet and `.26`, enter one
   exemption reason and click **Set exemption**.
   **Send reminders** sends another message containing the addresses still
   eligible under the current policy.
6. Choose **Release eligible addresses** in the sidebar and submit its form. The early-date warning is advisory.
   With the steps above, `.20` is released after its PTR cleanup succeeds;
   the assigned, retained and exempted addresses stay owned. Refresh to inspect
   the result and transaction.

Use **Notice history** to inspect initial notices and reminders, their
recipients and the administrator who queued them. Members see only their own
request and reasons; administrator identity is hidden in the member view.

**Close without releasing IPs** has a separate confirmation form. It leaves
remaining ownership intact and ends further campaign actions. Existing releases
continue. A closed campaign cannot be reopened.

To test a policy change, open **Edit campaign**, disable **Allow user opt-outs**, save, then send a
reminder or release again. A previously recorded member reason remains in the
history; the current policy determines whether it protects the address.
Administrator exemptions and VPS assignments continue to protect it.

## Additional addresses

`test-user1` also owns these unassigned allocations outside campaign 1:

- `198.51.100.23/32`, `198.51.100.24/32`, `198.51.100.25/32`
- `2001:db8:106:1::/64`, suitable for an IPv6-only campaign and email

The unassigned `198.51.100.26/32` belongs to `test-user2` and is included in
campaign 1. Sign in with this account to compare the member views. Assigned controls are `198.51.100.10/32`
on VPS 1 and `198.51.100.11/32` on VPS 2.

Campaign 2, **Release smoke validation**, records the completed automated live
check on separate addresses. Its initial notice and two reminders are already
in Mailpit. The smoke check released `.27` with PTR cleanup and
`2001:db8:106:2::/64` after a policy change; `.28` remains administrator-exempted.
Campaign 1 and its eight available member allocations were preserved.

The full allocation IDs are in [review-inventory.json](review-inventory.json).
