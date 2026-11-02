# Exporter metadata source correction

Verified predecessor: `8d4e03d53699d80f46030b0ee6eb213151b8ae30`. Current candidate: `1e3afc478fb72b54a25a0147910463f060fee88f`.

```diff
diff --git a/cluster/cz.vpsfree/containers/mx2/module.nix b/cluster/cz.vpsfree/containers/mx2/module.nix
index f80d90e6..f19a4b3d 100644
--- a/cluster/cz.vpsfree/containers/mx2/module.nix
+++ b/cluster/cz.vpsfree/containers/mx2/module.nix
@@ -26,6 +26,7 @@
         }
       ];
     };
+    services.node-exporter = { };
     tags = [
       "mx"
       "auto-update"
```

```diff
1:  36ae6529 ! 1:  9c6e3613 cluster: configure mx2 backup mail relay
    @@ Commit message
         match the primary message limit while preserving transport, filtering,
         trust, queue paths and the imported persistent-state version.
     
    +    Declare the existing node exporter in the service inventory so both
    +    monitor configurations can construct the mx2 scrape target.
    +
      ## cluster/cluster.nix ##
     @@
        ./cz.vpsfree/containers/int.utils/module.nix
    @@ cluster/cz.vpsfree/containers/mx2/module.nix (new)
     +        }
     +      ];
     +    };
    ++    services.node-exporter = { };
     +    tags = [
     +      "mx"
     +      "auto-update"
2:  91595bef = 2:  a5848319 internal-dns: align mail records with public DNS
3:  8d4e03d5 = 3:  1e3afc47 tests: verify mx2 relay and queue behavior in isolated VMs
```
