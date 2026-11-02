# Native type-check fix source delta

Old: `53d1310dd1be1c35ea83317a620ce9f6a7fae227`. New: `9738dfbc66bd06b75670d8efd93c684a174acbee`.

```diff
diff --git a/tests/mx2.py b/tests/mx2.py
index ae40e612..7fcf08c7 100644
--- a/tests/mx2.py
+++ b/tests/mx2.py
@@ -66,7 +66,9 @@ def check_message(record, recipient, marker):
     message = email.message_from_string(record["message"])
     assert message["Message-ID"] == f"<{marker}@sender.test>", record
     assert message["Subject"] == "mx2 " + marker, record
-    assert message.get_payload().replace("\r\n", "\n") == (
+    payload = message.get_payload()
+    assert isinstance(payload, str), record
+    assert payload.replace("\r\n", "\n") == (
         f"mx2 marker: {marker}\nContent survives forwarding: abc 123 !\n"
     ), record
     return message
```

```diff
1:  36ae6529 = 1:  36ae6529 cluster: configure mx2 backup mail relay
2:  91595bef = 2:  91595bef internal-dns: align mail records with public DNS
3:  53d1310d ! 3:  9738dfbc tests: verify mx2 relay and queue behavior in isolated VMs
    @@ tests/mx2.py (new)
     +    message = email.message_from_string(record["message"])
     +    assert message["Message-ID"] == f"<{marker}@sender.test>", record
     +    assert message["Subject"] == "mx2 " + marker, record
    -+    assert message.get_payload().replace("\r\n", "\n") == (
    ++    payload = message.get_payload()
    ++    assert isinstance(payload, str), record
    ++    assert payload.replace("\r\n", "\n") == (
     +        f"mx2 marker: {marker}\nContent survives forwarding: abc 123 !\n"
     +    ), record
     +    return message
```
