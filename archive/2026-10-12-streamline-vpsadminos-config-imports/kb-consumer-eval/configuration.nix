{ ... }:
{
  environment.persistence."/persistent" = {
    hideMounts = true;
    directories = [
      "/etc/nixos"
      "/var/log"
      "/var/lib/nixos"
    ];
    files = [
      "/etc/machine-id"
    ];
  };
}
