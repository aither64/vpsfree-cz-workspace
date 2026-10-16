cat > /etc/nixos/preservation-test.nix <<"EOF"
{ ... }:
{
  users.groups.preservation-test = {};
  users.users.preservation-test = {
    isSystemUser = true;
    group = "preservation-test";
  };
  environment.persistence."/persistent".directories = [
    "/var/lib/preservation-test"
  ];
}
EOF
sed -i "/^{$/a\  imports = [ ./preservation-test.nix ];" /etc/nixos/configuration.nix
