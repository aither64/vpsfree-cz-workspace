# Dedicated DNSBL source address correction

Old: `9738dfbc66bd06b75670d8efd93c684a174acbee`. New: `1bea06a507cf6d3c738740a778cb8328d1f49e92`.

```diff
diff --git a/tests/mx2.nix b/tests/mx2.nix
index c652ae2c..a1f278ca 100644
--- a/tests/mx2.nix
+++ b/tests/mx2.nix
@@ -87,7 +87,8 @@ pkgs.testers.runNixOSTest {
         receiver
         (network "192.168.1.10" "fd42:6d78:32::10")
       ];
-      networking.interfaces.eth1.ipv4.addresses = lib.mkForce [
+      # Override the network helper's priority 20 with both intended sources.
+      networking.interfaces.eth1.ipv4.addresses = lib.mkOverride 10 [
         {
           address = "192.168.1.10";
           prefixLength = 24;
diff --git a/tests/mx2.py b/tests/mx2.py
index 7fcf08c7..39141a42 100644
--- a/tests/mx2.py
+++ b/tests/mx2.py
@@ -191,6 +191,7 @@ with subtest("fresh Postgrey tuple, retry and policy-state restart persistence")
     assert smtp("grey@vpsfree.cz", "grey", probe=True)["code"] == 250
 
 with subtest("original DNSBL rejects a listed external source"):
+    sender.succeed("ip -4 -o address show dev eth1 | grep -F 'inet 192.168.1.11/24 '")
 
     def listed():
         response = smtp(
```

```diff
1:  36ae6529 = 1:  36ae6529 cluster: configure mx2 backup mail relay
2:  91595bef = 2:  91595bef internal-dns: align mail records with public DNS
3:  9738dfbc ! 3:  1bea06a5 tests: verify mx2 relay and queue behavior in isolated VMs
    @@ tests/mx2.nix (new)
     +        receiver
     +        (network "192.168.1.10" "fd42:6d78:32::10")
     +      ];
    -+      networking.interfaces.eth1.ipv4.addresses = lib.mkForce [
    ++      # Override the network helper's priority 20 with both intended sources.
    ++      networking.interfaces.eth1.ipv4.addresses = lib.mkOverride 10 [
     +        {
     +          address = "192.168.1.10";
     +          prefixLength = 24;
    @@ tests/mx2.py (new)
     +    assert smtp("grey@vpsfree.cz", "grey", probe=True)["code"] == 250
     +
     +with subtest("original DNSBL rejects a listed external source"):
    ++    sender.succeed("ip -4 -o address show dev eth1 | grep -F 'inet 192.168.1.11/24 '")
     +
     +    def listed():
     +        response = smtp(
```
