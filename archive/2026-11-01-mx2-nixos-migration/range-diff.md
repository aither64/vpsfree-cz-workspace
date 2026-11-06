# Original to refreshed mx2 series

```diff
1:  be8435d1 ! 1:  e4c1ac0c cluster: add mx2.vpsfree.cz
    @@ Metadata
      ## Commit message ##
         cluster: add mx2.vpsfree.cz

    +    Restore the NixOS backup MX container definition with its SMTP transport,
    +    Postgrey policy, administrator key and vpsAdmin placement metadata.
    +
    +    Select current flake channels while preserving the imported mail policy,
    +    network identity and persistent-state version.
    +
      ## cluster/cluster.nix ##
     @@
        ./cz.vpsfree/containers/int.utils/module.nix
    @@ cluster/cluster.nix

      ## cluster/cz.vpsfree/containers/mx2/config.nix (new) ##
     @@
    -+{ pkgs, lib, config, confData, ... }:
    ++{
    ++  pkgs,
    ++  lib,
    ++  config,
    ++  confData,
    ++  ...
    ++}:
     +{
     +  imports = [
     +    ../../../../environments/base.nix
    @@ cluster/cz.vpsfree/containers/mx2/module.nix (new)
     +{
     +  cluster."cz.vpsfree/containers/mx2" = {
     +    spin = "nixos";
    -+    swpins.channels = [ "nixos-stable" "os-staging" ];
    ++    inputs.channels = [
    ++      "nixos-stable"
    ++      "os-staging"
    ++    ];
     +    container.id = 27627;
    -+    host = { name = "mx2"; domain = "vpsfree.cz"; target = "172.19.9.22"; };
    ++    host = {
    ++      name = "mx2";
    ++      domain = "vpsfree.cz";
    ++      target = "172.19.9.22";
    ++    };
     +    addresses = {
    -+      v4 = [ { address = "37.205.11.114"; prefix = 32; } ];
    -+      v6 = [ { address = "2a03:3b40:100::1:95"; prefix = 128; } ];
    ++      v4 = [
    ++        {
    ++          address = "37.205.11.114";
    ++          prefix = 32;
    ++        }
    ++      ];
    ++      v6 = [
    ++        {
    ++          address = "2a03:3b40:100::1:95";
    ++          prefix = 128;
    ++        }
    ++      ];
     +    };
    -+    tags = [ "mx" "auto-update" ];
    ++    tags = [
    ++      "mx"
    ++      "auto-update"
    ++    ];
     +  };
     +}

2:  40411d67 < -:  -------- environments/deploy: use cache.vpsadminos.org
```
