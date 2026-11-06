# Keep SMTP probe commands synchronized after STARTTLS

Piping EHLO, MAIL, RCPT, RSET and QUIT together into `openssl s_client -starttls smtp`
can trigger Postfix `554 5.5.0 Error: SMTP protocol synchronization`. OpenSSL
negotiates TLS, but does not wait for each SMTP reply on behalf of its stdin
producer. The error is not a relay-policy result; successful certificate
verification still proves the completed TLS connection.

Use a reply-aware client such as Python `smtplib` for the remaining SMTP dialogue.
After STARTTLS, issue EHLO again before MAIL/RCPT; never send DATA for a relay
rejection probe. Use the default TLS trust store and verify the intended DNS name.
When connecting to a literal IP, the inspected Python SMTP.connect updates `_host`;
set the intended verification name after connect before calling starttls. Assert
the connected peer when exact address-family coverage matters.

In the mx2 migration, the corrected client passed against public IPv4 with trusted
TLS and `554 5.7.1 Relay access denied`, without DATA. The user then proved
external IPv6 TLS and relay denial with the corrected client; the earlier
synchronization error itself did not prove IPv6 RCPT denial.
See `work/2026-11-01-mx2-nixos-migration/public-profile-preparation.md` for evidence.
