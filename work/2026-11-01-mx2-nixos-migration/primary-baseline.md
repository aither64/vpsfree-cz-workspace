# Primary and old mx2 baseline

Bounded read-only evidence collected 2026-11-02, approximately 15:30–15:38 UTC,
by implementer1. This is session evidence, not an operating procedure or a
production acceptance result.

## Authority and boundaries

- `dev-session current` from the session directory returned
  `2026-11-01-mx2-nixos-migration`; both `DEV_SESSION_*` identity variables were
  absent. The trusted thread binding names this slug and
  `/home/aither/workspace/ai/vpsfree.cz`.
- Live same-session roster: implementer1 is `workspace_write`,
  `gpt-6.1-sol` / `xhigh`; retained settings were preserved. Evidence-file writing
  was assigned explicitly; no source edits or Git mutations were performed.
- User-provided facts, not remotely verified: primary runs Debian 13 outside
  the configuration repository; old mx2 runs CentOS 6.
- SSH used the existing effective user `aither`, port 22, without a proxy or
  target override. BatchMode and strict existing host verification were enabled;
  host-key updates, forwarding, connection sharing and local commands were
  disabled; connect timeout was five seconds. No passwords, private-key contents,
  credentials or mail contents were read. No new host trust was accepted.
- No deployment, service/configuration change, package installation, mail
  submission, scan or historical candidate connection occurred. The later
  banner/EHLO/STARTTLS probe was explicitly authorized; it sent no MAIL, RCPT,
  DATA or AUTH command.

## DNS observations: internal and public views differ

Queries used `dig` with bounded timeouts for the three assigned domains and
their resulting primary A/AAAA names. These are resolver observations, not a
complete authoritative DNS audit.

| Domain | Configured resolver `172.16.9.90` | Public recursive resolver `1.1.1.1` |
| --- | --- | --- |
| `vpsfree.cz` | NOERROR, no MX answer; authoritative response | MX 10 `prasiatko-mail.vpsfree.cz`, MX 15 `mx2.vpsfree.cz` |
| `lists.vpsfree.cz` | MX 10 `mx1.vpsfree.cz`; authoritative response | MX 10 `prasiatko-mail.vpsfree.cz`, MX 15 `mx2.vpsfree.cz` |
| `vpsfree.org` | MX 10 `prasiatko-mail.vpsfree.cz`, MX 15 `mx2.vpsfree.cz`; recursive response | Same primary and backup |

The internal authoritative response identifies
`ns1.int.prg.vpsfree.cz` in the `vpsfree.cz` SOA. It returns NXDOMAIN for both
A and AAAA of `prasiatko-mail.vpsfree.cz`. Public recursive results resolve that
primary normally:

| Name and view | A | AAAA |
| --- | --- | --- |
| `mx1.vpsfree.cz`, configured resolver | `37.205.15.53` | `2a01:430:17:1::33` |
| `prasiatko-mail.vpsfree.cz`, public recursive resolver | `37.205.15.53` | `2a03:3b40:fe:1c3::1` |

The inherited `prasiatko-mail.vpsfree.cz` name remains the primary in the
observed public MX records. Its initial local resolution failure does **not**
prove stale or broken public routing. The shared IPv4 address and SMTP identity
below corroborate a relationship to internal `mx1`; the differing IPv6 addresses
prevent treating the endpoints or their network paths as interchangeable.
Public primary and IPv6 SMTP behavior were not probed.

## SSH access results

| Target | Observed result | Limit |
| --- | --- | --- |
| `prasiatko-mail.vpsfree.cz` | Exit 255: hostname could not be resolved through the configured resolver | No remote command ran; no IP override attempted |
| `mx2.vpsfree.cz` | Resolved to `37.205.11.114`; TCP22 connected; SSH 10.5p1 refused negotiation because server offered only `ssh-rsa,ssh-dss` host keys | No remote command ran |
| DNS-identified `mx1.vpsfree.cz` | Exit 255: no known RSA host key; strict checking rejected it | No remote command ran; no trust added |

For the narrowly authorized old-mx2 RSA retry, `ssh-keygen -F mx2.vpsfree.cz`
found no exact-host entry in either `/home/aither/.ssh/known_hosts` or
`/etc/ssh/ssh_known_hosts`; `known_hosts2` was absent. The trust prerequisite
therefore failed and no legacy-algorithm retry was performed. Neither
`HostKeyAlgorithms` nor `PubkeyAcceptedAlgorithms` was relaxed.

The fixed remote allowlist was prepared but never executed successfully:
`/etc/os-release`, MTA executable/version, selected Postfix domain/recipient,
transport, trust, TLS, restriction, milter, queue-path and delay/lifetime
parameters, TCP25 listeners and relevant service state. There are no live
configuration or map-content findings to infer from these failures.

## Single authorized SMTP observation on internal mx1

One Python standard-library SMTP connection to `mx1.vpsfree.cz:25` observed:

```text
220 prasiatko.vpsfree.cz ESMTP Postfix (Debian/GNU)
250-prasiatko.vpsfree.cz
PIPELINING, SIZE 104857600, VRFY, ETRN, STARTTLS,
AUTH PLAIN LOGIN, AUTH=PLAIN LOGIN, ENHANCEDSTATUSCODES,
8BITMIME, DSN, CHUNKING
```

EHLO used `verification.invalid`. One STARTTLS handshake with the default
system-verifying Python SSL context failed verification code 18,
`self-signed certificate`. No verification override or second handshake was
used. QUIT was unavailable after the aborted TLS handshake; the local socket
was closed. Certificate subject, issuer, validity, negotiated TLS version/cipher
and the connected address family were not captured. The banner identifies
Postfix/Debian branding, not the exact Postfix or Debian version.

STARTTLS advertisement proves that this observed listener offers STARTTLS; the
failed verification does not establish its full TLS policy or what the candidate
will negotiate. Advertised AUTH and VRFY do not establish permission or behavior;
neither was invoked.

## Policy comparison and remaining limits

Candidate facts below refer only to the pre-verification source snapshot
`e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c` and its existing
[evaluated configuration evidence](evaluated-mail-config.md). They are generated
configuration, not service observations or the result of later candidate fixes.

| Concern | Old mx2 / actual primary | Candidate snapshot |
| --- | --- | --- |
| Relay domains and routing | No live domain policy obtained; public DNS names do not establish SMTP acceptance | Empty `relay_domains`; transport-map path configured |
| Recipient validation | No RCPT probes or recipient-map access; valid/invalid recipient handling unknown | Restriction list contains `reject_unlisted_recipient`; actual primary recipient semantics remain unknown |
| TLS | Old mx2 unknown; internal mx1 advertises STARTTLS, default verification fails self-signed certificate | Inbound `smtpd_tls_security_level = none`; outbound `smtp_tls_security_level = may` |
| Filtering | Old/primary greylisting, DNSBL, milter and failure policy unknown | Postgrey, two DNSBL checks and localhost milter configured; `milter_default_action = accept` |
| Trust | Actual allowed senders/networks, SASL policy and candidate-origin acceptance unknown | `mynetworks_style = host`; recipient restrictions begin with network/SASL permits |
| Queue and recovery | Queue path, contents, lifetimes and spool compatibility uninspected | Queue path `/var/lib/postfix/queue`; runtime durability belongs to isolated tests |

Isolated verification can continue with explicit fixtures. It cannot certify
equivalence to unknown old/primary policies or acceptance from the future mx2
network identity. Later no-DATA consultation of the primary is possible in
principle using greeting/EHLO/STARTTLS and separately authorized MAIL/RCPT/RSET
checks, but this package did not test recipient consultation or the public
primary path. A valid test recipient and trust/TLS expectations remain future
acceptance inputs, not blockers for the isolated package.

No further access or dependency exploration is needed for this evidence package.
Lead and architect0 received the stable results and the correction of the initial
local-DNS stale-name inference. Lead owns linking this artifact from shared state.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/
