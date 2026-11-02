# Verification phase range comparisons

## Reviewed import to complete final series

```diff
1:  e4c1ac0c ! 1:  36ae6529 cluster: add mx2.vpsfree.cz
    @@ Metadata
     Author: Jakub Skokan <jakub.skokan@havefun.cz>
     
      ## Commit message ##
    -    cluster: add mx2.vpsfree.cz
    +    cluster: configure mx2 backup mail relay
     
    -    Restore the NixOS backup MX container definition with its SMTP transport,
    -    Postgrey policy, administrator key and vpsAdmin placement metadata.
    +    Restore the NixOS backup MX container with its administrator key and
    +    vpsAdmin placement. Share its mail module with isolated verification.
     
    -    Select current flake channels while preserving the imported mail policy,
    -    network identity and persistent-state version.
    +    Authorize only the three backup relay domains, exclude implicit subdomain
    +    relay and separate relay authorization from greylisting. Open TCP25 and
    +    match the primary message limit while preserving transport, filtering,
    +    trust, queue paths and the imported persistent-state version.
     
      ## cluster/cluster.nix ##
     @@
    @@ cluster/cz.vpsfree/containers/mx2/config.nix (new)
     +  imports = [
     +    ../../../../environments/base.nix
     +    ../../../../profiles/ct.nix
    ++    ../../../../configs/mx2.nix
     +  ];
     +
    -+  services.postfix = {
    -+    enable = true;
    -+
    -+    config = {
    -+      smtpd_recipient_restrictions = [
    -+        "permit_mynetworks"
    -+        "permit_sasl_authenticated"
    -+        "reject_unauth_pipelining"
    -+        "reject_non_fqdn_recipient"
    -+        "reject_unknown_recipient_domain"
    -+        "reject_unauth_destination"
    -+        "reject_unlisted_recipient"
    -+        "check_policy_service unix:${config.services.postgrey.socket.path}"
    -+        "reject_rbl_client zen.spamhaus.org=127.0.0.[2..11]"
    -+        "reject_rbl_client b.barracudacentral.org=127.0.0.2"
    -+      ];
    -+
    -+      smtpd_milters = "inet:localhost:11332";
    -+
    -+      milter_default_action = "accept";
    -+    };
    -+
    -+    transport = ''
    -+      vpsfree.cz              smtp:prasiatko-mail.vpsfree.cz
    -+      lists.vpsfree.cz        smtp:prasiatko-mail.vpsfree.cz
    -+      vpsfree.org             smtp:prasiatko-mail.vpsfree.cz
    -+    '';
    -+  };
    -+
    -+  services.postgrey.enable = true;
    -+
     +  users.users.root.openssh.authorizedKeys.keys = with confData.sshKeys; [ toms ];
     +
     +  system.stateVersion = "25.05";
    @@ cluster/cz.vpsfree/containers/mx2/module.nix (new)
     +      "auto-update"
     +    ];
     +  };
    ++}
    +
    + ## configs/mx2.nix (new) ##
    +@@
    ++{ config, ... }:
    ++{
    ++  networking.firewall.allowedTCPPorts = [ 25 ];
    ++
    ++  services.postfix = {
    ++    enable = true;
    ++    settings.main = {
    ++      relay_domains = [
    ++        "vpsfree.cz"
    ++        "lists.vpsfree.cz"
    ++        "vpsfree.org"
    ++      ];
    ++      # Keep Postfix defaults except implicit relay permission for subdomains.
    ++      parent_domain_matches_subdomains = [
    ++        "debug_peer_list"
    ++        "fast_flush_domains"
    ++        "mynetworks"
    ++        "permit_mx_backup_networks"
    ++        "qmqpd_authorized_clients"
    ++        "smtpd_access_maps"
    ++      ];
    ++      smtpd_relay_restrictions = [
    ++        "permit_mynetworks"
    ++        "permit_sasl_authenticated"
    ++        "reject_unauth_destination"
    ++      ];
    ++      smtpd_recipient_restrictions = [
    ++        "permit_mynetworks"
    ++        "permit_sasl_authenticated"
    ++        "reject_unauth_pipelining"
    ++        "reject_non_fqdn_recipient"
    ++        "reject_unknown_recipient_domain"
    ++        "reject_unlisted_recipient"
    ++        "check_policy_service unix:${config.services.postgrey.socket.path}"
    ++        "reject_rbl_client zen.spamhaus.org=127.0.0.[2..11]"
    ++        "reject_rbl_client b.barracudacentral.org=127.0.0.2"
    ++      ];
    ++      # Match the primary's advertised 100 MiB limit before accepting a queue item.
    ++      message_size_limit = 104857600;
    ++      smtpd_milters = "inet:localhost:11332";
    ++      milter_default_action = "accept";
    ++    };
    ++    transport = ''
    ++      vpsfree.cz              smtp:prasiatko-mail.vpsfree.cz
    ++      lists.vpsfree.cz        smtp:prasiatko-mail.vpsfree.cz
    ++      vpsfree.org             smtp:prasiatko-mail.vpsfree.cz
    ++    '';
    ++  };
    ++  services.postgrey.enable = true;
     +}
     
      ## data/ssh-keys.nix ##
-:  -------- > 2:  91595bef internal-dns: align mail records with public DNS
-:  -------- > 3:  f3789413 tests: verify mx2 relay and queue behavior in isolated VMs
```

## Consolidation of complete working series

```diff
1:  e4c1ac0c ! 1:  36ae6529 cluster: add mx2.vpsfree.cz
    @@ Metadata
     Author: Jakub Skokan <jakub.skokan@havefun.cz>
     
      ## Commit message ##
    -    cluster: add mx2.vpsfree.cz
    +    cluster: configure mx2 backup mail relay
     
    -    Restore the NixOS backup MX container definition with its SMTP transport,
    -    Postgrey policy, administrator key and vpsAdmin placement metadata.
    +    Restore the NixOS backup MX container with its administrator key and
    +    vpsAdmin placement. Share its mail module with isolated verification.
     
    -    Select current flake channels while preserving the imported mail policy,
    -    network identity and persistent-state version.
    +    Authorize only the three backup relay domains, exclude implicit subdomain
    +    relay and separate relay authorization from greylisting. Open TCP25 and
    +    match the primary message limit while preserving transport, filtering,
    +    trust, queue paths and the imported persistent-state version.
     
      ## cluster/cluster.nix ##
     @@
    @@ cluster/cz.vpsfree/containers/mx2/config.nix (new)
     +  imports = [
     +    ../../../../environments/base.nix
     +    ../../../../profiles/ct.nix
    ++    ../../../../configs/mx2.nix
     +  ];
     +
    -+  services.postfix = {
    -+    enable = true;
    -+
    -+    config = {
    -+      smtpd_recipient_restrictions = [
    -+        "permit_mynetworks"
    -+        "permit_sasl_authenticated"
    -+        "reject_unauth_pipelining"
    -+        "reject_non_fqdn_recipient"
    -+        "reject_unknown_recipient_domain"
    -+        "reject_unauth_destination"
    -+        "reject_unlisted_recipient"
    -+        "check_policy_service unix:${config.services.postgrey.socket.path}"
    -+        "reject_rbl_client zen.spamhaus.org=127.0.0.[2..11]"
    -+        "reject_rbl_client b.barracudacentral.org=127.0.0.2"
    -+      ];
    -+
    -+      smtpd_milters = "inet:localhost:11332";
    -+
    -+      milter_default_action = "accept";
    -+    };
    -+
    -+    transport = ''
    -+      vpsfree.cz              smtp:prasiatko-mail.vpsfree.cz
    -+      lists.vpsfree.cz        smtp:prasiatko-mail.vpsfree.cz
    -+      vpsfree.org             smtp:prasiatko-mail.vpsfree.cz
    -+    '';
    -+  };
    -+
    -+  services.postgrey.enable = true;
    -+
     +  users.users.root.openssh.authorizedKeys.keys = with confData.sshKeys; [ toms ];
     +
     +  system.stateVersion = "25.05";
    @@ cluster/cz.vpsfree/containers/mx2/module.nix (new)
     +      "auto-update"
     +    ];
     +  };
    ++}
    +
    + ## configs/mx2.nix (new) ##
    +@@
    ++{ config, ... }:
    ++{
    ++  networking.firewall.allowedTCPPorts = [ 25 ];
    ++
    ++  services.postfix = {
    ++    enable = true;
    ++    settings.main = {
    ++      relay_domains = [
    ++        "vpsfree.cz"
    ++        "lists.vpsfree.cz"
    ++        "vpsfree.org"
    ++      ];
    ++      # Keep Postfix defaults except implicit relay permission for subdomains.
    ++      parent_domain_matches_subdomains = [
    ++        "debug_peer_list"
    ++        "fast_flush_domains"
    ++        "mynetworks"
    ++        "permit_mx_backup_networks"
    ++        "qmqpd_authorized_clients"
    ++        "smtpd_access_maps"
    ++      ];
    ++      smtpd_relay_restrictions = [
    ++        "permit_mynetworks"
    ++        "permit_sasl_authenticated"
    ++        "reject_unauth_destination"
    ++      ];
    ++      smtpd_recipient_restrictions = [
    ++        "permit_mynetworks"
    ++        "permit_sasl_authenticated"
    ++        "reject_unauth_pipelining"
    ++        "reject_non_fqdn_recipient"
    ++        "reject_unknown_recipient_domain"
    ++        "reject_unlisted_recipient"
    ++        "check_policy_service unix:${config.services.postgrey.socket.path}"
    ++        "reject_rbl_client zen.spamhaus.org=127.0.0.[2..11]"
    ++        "reject_rbl_client b.barracudacentral.org=127.0.0.2"
    ++      ];
    ++      # Match the primary's advertised 100 MiB limit before accepting a queue item.
    ++      message_size_limit = 104857600;
    ++      smtpd_milters = "inet:localhost:11332";
    ++      milter_default_action = "accept";
    ++    };
    ++    transport = ''
    ++      vpsfree.cz              smtp:prasiatko-mail.vpsfree.cz
    ++      lists.vpsfree.cz        smtp:prasiatko-mail.vpsfree.cz
    ++      vpsfree.org             smtp:prasiatko-mail.vpsfree.cz
    ++    '';
    ++  };
    ++  services.postgrey.enable = true;
     +}
     
      ## data/ssh-keys.nix ##
2:  655851e5 = 2:  91595bef internal-dns: align mail records with public DNS
3:  29bea055 < -:  -------- fixup! cluster: add mx2.vpsfree.cz
4:  13e0ad18 = 3:  f3789413 tests: verify mx2 relay and queue behavior in isolated VMs
```
