# Native reboot handling source correction

Old: `1bea06a507cf6d3c738740a778cb8328d1f49e92`. New: `795134a48cdee269bdccabb68168de2d190c6830`.

```diff
diff --git a/tests/mx2.py b/tests/mx2.py
index 39141a42..c6391061 100644
--- a/tests/mx2.py
+++ b/tests/mx2.py
@@ -97,6 +97,8 @@ def recipient_map(temporary=True):
     )
 
 
+# The native driver otherwise exits QEMU at guest reboot (-no-reboot).
+mx.start(allow_reboot=True)
 start_all()
 for machine in (sender, mx, primary):
     machine.wait_for_unit("multi-user.target", timeout=90)
```

```diff
1:  36ae6529 = 1:  36ae6529 cluster: configure mx2 backup mail relay
2:  91595bef = 2:  91595bef internal-dns: align mail records with public DNS
3:  1bea06a5 ! 3:  795134a4 tests: verify mx2 relay and queue behavior in isolated VMs
    @@ tests/mx2.py (new)
     +    )
     +
     +
    ++# The native driver otherwise exits QEMU at guest reboot (-no-reboot).
    ++mx.start(allow_reboot=True)
     +start_all()
     +for machine in (sender, mx, primary):
     +    machine.wait_for_unit("multi-user.target", timeout=90)
```
