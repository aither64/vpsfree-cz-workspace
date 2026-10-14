sed -i "/^}$/i\  users.groups.a-preservation-test = {};\n  users.users.a-preservation-test = { isSystemUser = true; group = \"a-preservation-test\"; };" /etc/nixos/preservation-test.nix
