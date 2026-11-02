# Review remediation source delta

Reviewed predecessor: `f3789413a53bcd12e2352940a0ec3e88009c5d9f`.
Current candidate: `53d1310dd1be1c35ea83317a620ce9f6a7fae227`.

```diff
diff --git a/tests/mx2.py b/tests/mx2.py
index 4ffc4cb9..ae40e612 100644
--- a/tests/mx2.py
+++ b/tests/mx2.py
@@ -162,12 +162,17 @@ with subtest("relay denial is independent of greylisting and never queues DATA")
             mx.succeed("dig +short +time=2 +tries=1 " + domain).strip()
             == "192.168.1.30"
         )
-    for recipient in (
-        "user@unrelated.test",
-        "user@arbitrary.vpsfree.cz",
-        "bad@@vpsfree.cz",
-        "user@unavailable.invalid",
+    for source, host in (
+        ("192.168.1.10", "192.168.1.20"),
+        ("fd42:6d78:32::10", "fd42:6d78:32::20"),
     ):
+        for recipient in ("user@unrelated.test", "user@arbitrary.vpsfree.cz"):
+            response = smtp(recipient, "deny", source=source, host=host, probe=True)
+            assert response["stage"] == "rcpt" and 500 <= response["code"] < 600, (
+                response
+            )
+            assert queue() == []
+    for recipient in ("bad@@vpsfree.cz", "user@unavailable.invalid"):
         response = smtp(recipient, "deny", probe=True)
         assert response["stage"] == "rcpt" and 500 <= response["code"] < 600, response
     assert queue() == []
@@ -250,7 +255,12 @@ with subtest("primary 4xx defers accepted message until recovery"):
             i["queue_id"] == queue_id and i["queue_name"] == "deferred" for i in queue()
         )
     )
-    queued(queue_id, "temporary")
+    item = queued(queue_id, "temporary")
+    assert any(
+        recipient["address"] == "temporary@vpsfree.cz"
+        and "450 4.2.0 fixture temporary rejection" in recipient.get("delay_reason", "")
+        for recipient in item["recipients"]
+    ), item
     recipient_map(temporary=False)
     mx.succeed("postqueue -f")
     check_message(delivered(primary, "temporary"), "temporary@vpsfree.cz", "temporary")
```

## Owning commit history

```diff
1:  36ae6529 = 1:  36ae6529 cluster: configure mx2 backup mail relay
2:  91595bef = 2:  91595bef internal-dns: align mail records with public DNS
3:  f3789413 ! 3:  53d1310d tests: verify mx2 relay and queue behavior in isolated VMs
    @@ Metadata
      ## Commit message ##
         tests: verify mx2 relay and queue behavior in isolated VMs
     
    -    Exercise the shared production mail policy with a controlled SMTP sender,
    -    primary receiver and local DNS. Verify domain isolation, envelopes and
    -    content, greylisting and DNSBLs, missing-milter behavior, durable outage
    -    queues, SMTP errors, and opportunistic TLS with IPv4 and IPv6 clients.
    +    Exercise the shared production mail policy with controlled SMTP sender,
    +    primary receiver and local DNS. Verify domain isolation on IPv4 and IPv6,
    +    envelopes and content, greylisting, DNSBLs and missing-milter behavior.
     
    -    Keep the fixture network isolated and document its timing differences,
    -    production acceptance limits and queue recovery requirements.
    +    Check durable outage queues, recipient-bound SMTP error responses and
    +    opportunistic TLS. Keep the fixture isolated and document its timing
    +    differences, production acceptance limits and queue recovery requirements.
     
      ## README.md ##
     @@ README.md: confctl deploy "cz.vpsfree/nodes/stg/*" dry-activate
    @@ tests/mx2.py (new)
     +            mx.succeed("dig +short +time=2 +tries=1 " + domain).strip()
     +            == "192.168.1.30"
     +        )
    -+    for recipient in (
    -+        "user@unrelated.test",
    -+        "user@arbitrary.vpsfree.cz",
    -+        "bad@@vpsfree.cz",
    -+        "user@unavailable.invalid",
    ++    for source, host in (
    ++        ("192.168.1.10", "192.168.1.20"),
    ++        ("fd42:6d78:32::10", "fd42:6d78:32::20"),
     +    ):
    ++        for recipient in ("user@unrelated.test", "user@arbitrary.vpsfree.cz"):
    ++            response = smtp(recipient, "deny", source=source, host=host, probe=True)
    ++            assert response["stage"] == "rcpt" and 500 <= response["code"] < 600, (
    ++                response
    ++            )
    ++            assert queue() == []
    ++    for recipient in ("bad@@vpsfree.cz", "user@unavailable.invalid"):
     +        response = smtp(recipient, "deny", probe=True)
     +        assert response["stage"] == "rcpt" and 500 <= response["code"] < 600, response
     +    assert queue() == []
    @@ tests/mx2.py (new)
     +            i["queue_id"] == queue_id and i["queue_name"] == "deferred" for i in queue()
     +        )
     +    )
    -+    queued(queue_id, "temporary")
    ++    item = queued(queue_id, "temporary")
    ++    assert any(
    ++        recipient["address"] == "temporary@vpsfree.cz"
    ++        and "450 4.2.0 fixture temporary rejection" in recipient.get("delay_reason", "")
    ++        for recipient in item["recipients"]
    ++    ), item
     +    recipient_map(temporary=False)
     +    mx.succeed("postqueue -f")
     +    check_message(delivered(primary, "temporary"), "temporary@vpsfree.cz", "temporary")
```
