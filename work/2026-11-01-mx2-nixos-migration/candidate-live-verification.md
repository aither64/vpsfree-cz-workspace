# Candidate live verification execution contract

Prepared only. Execute after lead confirms actual switch to4pc5 and held claim
13ba611e-2f87-4036-b958-b0e056e13da7. Target only172.19.9.22/VPS27627.
No remote probe, fault, reboot or message has run under this contract.

1. Strict pinned SSH using candidate-ssh.conf. Require current/profile4pc5,
   configuration-info clean084488 and expected inputs; installed-approved key
   presence without dumping other keys; stateVersion25.05 and persistent
   tank/ct/27627; private172.19.9.22/32, no old publicIPs/globalIPv6. Require
   Postfix/Postgrey/firewall/sshd active, exporter/rsyslog absent/inactive;
   inspect actual firewall rule/source and resolver1.1.1.1. Booted-system can
   remain98n9 until the planned reboot. Check queue count0 before mail.
2. Actual candidate primary DNS, using ordinary installed host (available in
   built4pc5; oldguest lacked dig):

   ```sh
   host -W 2 -R 1 -t A prasiatko-mail.vpsfree.cz.
   host -W 2 -R 1 -t AAAA prasiatko-mail.vpsfree.cz.
   ```

   Save all A/AAAA answers and actual resolver. Require usableIPv4 route; no
   IPv6 transport claim without a usableIPv6 route. Do not hardcode new transport
   or change primary. Recheck DNS after reboot before removing fault; drift
   stops the test for reconciliation.
3. From workspace use bounded stdlib Python smtplib to candidate25, recording
   greeting/EHLO/options. Probe MAIL FROM podpora@vpsfree.cz and unrelated
   RCPT postmaster@example.org, then RSET/QUIT without DATA. example.org is the
   reserved documentation domain; require explicit relay-authorization denial,
   not DNSBL/unknown-domain/temporary-policy failure. No other recipient is used.
4. Create exactly two small fixed ASCII synthetic payloads in session data:
   unique Message-ID/marker and clearly marked subject, normal and outage.
   Both envelope sender and recipient are podpora@vpsfree.cz. Preserve exact
   bytes/hash and SMTP final reply/queueID. Native300s greylisting can cause
   a pre-DATA450; retain same source/envelope and retry after305s, at most
   one scheduled retry. Never retry unknown DATA outcome; reconcile ID/logs.
   Waits remain interruptible. No bypass, AUTH, trust expansion or deliberateDSN.
5. Send normal payload, confirm primary handoff/queue drain and user receipt.
   Require queue0 again before any outage mutation. Stop on unexpected real
   queued mail or unexpected DSN. No accepted mail may be deleted.

## Candidate-only persistent fault

Before mutation save exact rendered unit/drop-in and hashes in session. Assert
these guest files and the dedicated IPv4/IPv6 chains do not exist; collision
stops rather than overwriting. Save current rules relevant to OUTPUT. All primary
DNS addresses are recorded before rendering; substitute every observed A/AAAA.
Use ordinary installed /run/current-system/sw/bin/{iptables,ip6tables}.

Temporary /usr/local/lib/systemd/system/mx2-verification-outage.service:

```ini
[Unit]
Description=Owned mx2 verification primary SMTP outage
Requires=firewall.service
After=firewall.service
Before=postfix.service
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/run/current-system/sw/bin/iptables -w -N MX2VERIFY
ExecStart=/run/current-system/sw/bin/ip6tables -w -N MX2VERIFY
# One following rule for EACH recorded A answer:
ExecStart=/run/current-system/sw/bin/iptables -w -A MX2VERIFY -p tcp -d PRIMARY_A --dport 25 -j REJECT --reject-with tcp-reset
# One following rule for EACH recorded AAAA answer:
ExecStart=/run/current-system/sw/bin/ip6tables -w -A MX2VERIFY -p tcp -d PRIMARY_AAAA --dport 25 -j REJECT --reject-with tcp-reset
ExecStart=/run/current-system/sw/bin/iptables -w -I OUTPUT 1 -p tcp --dport 25 -m comment --comment mx2-verification-outage -j MX2VERIFY
ExecStart=/run/current-system/sw/bin/ip6tables -w -I OUTPUT 1 -p tcp --dport 25 -m comment --comment mx2-verification-outage -j MX2VERIFY
ExecStop=/run/current-system/sw/bin/iptables -w -D OUTPUT -p tcp --dport 25 -m comment --comment mx2-verification-outage -j MX2VERIFY
ExecStop=/run/current-system/sw/bin/ip6tables -w -D OUTPUT -p tcp --dport 25 -m comment --comment mx2-verification-outage -j MX2VERIFY
ExecStop=/run/current-system/sw/bin/iptables -w -F MX2VERIFY
ExecStop=/run/current-system/sw/bin/ip6tables -w -F MX2VERIFY
ExecStop=/run/current-system/sw/bin/iptables -w -X MX2VERIFY
ExecStop=/run/current-system/sw/bin/ip6tables -w -X MX2VERIFY
```

Only primary-destination TCP25 rejects in each chain; unmatched traffic returns.
No primary, DNS, SSH or host-side mutation. To prevent a boot failure from
starting Postfix without the fault, temporary owned drop-in
/usr/local/lib/systemd/system/postfix.service.d/90-mx2-verification-outage.conf:

```ini
[Unit]
Requires=mx2-verification-outage.service
After=mx2-verification-outage.service
```

Install exact files only after their absence checks, then ordinary commands:

```sh
systemctl daemon-reload
systemctl start mx2-verification-outage.service
systemctl is-active mx2-verification-outage.service
iptables -w -S MX2VERIFY
ip6tables -w -S MX2VERIFY
iptables -w -S OUTPUT
ip6tables -w -S OUTPUT
```

Inspect exact rules before accepting the second payload. On partial failure,
record actual effects and remove only proven owned partial rules/files before
continuing; never retry blindly.

## Queue persistence and restoration

After outage payload final DATA250, record accepted Postfix queueID. Require
that ID has only expected envelope/recipient; inspect only its own synthetic
Message-ID/marker through postcat and print booleans/hashes, never other bodies.
Record queue delay tied to the intended primary. Then, one at a time:

```sh
systemctl restart postfix.service
# Inspect same ID/envelope/own marker and active fault before reboot.
systemctl reboot
# Strict reconnect, same4pc5/current/profile/booted, persistence, service+fault.
# Inspect same accepted ID/envelope/marker; no new payload.
```

Reboot only the guest; bounded reconnect uses the same pinned host trust/key.
After successful persistence evidence, remove the exact checksummed Postfix
drop-in first, daemon-reload, then stop the owned fault (its ExecStop
removes exact rules). Finally remove the checksummed unit, daemon-reload and
verify unit/chain/jump absence before normal flush:

```sh
rm /usr/local/lib/systemd/system/postfix.service.d/90-mx2-verification-outage.conf
systemctl daemon-reload
systemctl stop mx2-verification-outage.service
rm /usr/local/lib/systemd/system/mx2-verification-outage.service
systemctl daemon-reload
postqueue -f
```

Verify primary handoff for that queueID, queue0, service/access/resolver health
and user receipt. Record exact removal/rule absence. On uncertain command, lost
management access, unexpected mail/DSN or failed persistence: stop submissions,
keep accepted queues/disk and same claim, reconcile exact effects. Remove only
owned faults; old98n9 rollback requires state-compatibility assessment and is
not an automatic test reset. No session cleanup, default merge or public cutover.

Native path proof after healthy boot: /usr/local/lib/systemd/system is listed
by systemd-analyze unit-paths. Directory is currently absent, but /usr is
writable on persistent candidate ZFS. Standard owned directories may be
created with install -d; no /etc override or unit-path change. Local exact
rendering and hashes are in mx2-outage-plan.json; no guest files written.
Postfix Requires/After triggers fault after reboot without an enable symlink.
