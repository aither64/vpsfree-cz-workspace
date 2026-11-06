# Temporary SMTP reply format correction

Old: `795134a48cdee269bdccabb68168de2d190c6830`. New: `8d4e03d53699d80f46030b0ee6eb213151b8ae30`.

```diff
diff --git a/tests/mx2.py b/tests/mx2.py
index c6391061..60ca39a0 100644
--- a/tests/mx2.py
+++ b/tests/mx2.py
@@ -263,7 +263,8 @@ with subtest("primary 4xx defers accepted message until recovery"):
     item = queued(queue_id, "temporary")
     assert any(
         recipient["address"] == "temporary@vpsfree.cz"
-        and "450 4.2.0 fixture temporary rejection" in recipient.get("delay_reason", "")
+        and "450 4.2.0 " in recipient.get("delay_reason", "")
+        and "fixture temporary rejection" in recipient.get("delay_reason", "")
         for recipient in item["recipients"]
     ), item
     recipient_map(temporary=False)
```

```diff
1:  36ae6529 = 1:  36ae6529 cluster: configure mx2 backup mail relay
2:  91595bef = 2:  91595bef internal-dns: align mail records with public DNS
3:  795134a4 ! 3:  8d4e03d5 tests: verify mx2 relay and queue behavior in isolated VMs
    @@ tests/mx2.py (new)
     +    item = queued(queue_id, "temporary")
     +    assert any(
     +        recipient["address"] == "temporary@vpsfree.cz"
    -+        and "450 4.2.0 fixture temporary rejection" in recipient.get("delay_reason", "")
    ++        and "450 4.2.0 " in recipient.get("delay_reason", "")
    ++        and "fixture temporary rejection" in recipient.get("delay_reason", "")
     +        for recipient in item["recipients"]
     +    ), item
     +    recipient_map(temporary=False)
```
