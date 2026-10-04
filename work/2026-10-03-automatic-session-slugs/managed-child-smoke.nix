{
  runtimeSource,
  packageRoot,
  fixtureBinary,
  manifestFile,
}:
let
  # All inputs are explicit frozen store paths. This wrapper neither selects an
  # installed profile nor rebuilds a different runtime package as the candidate.
  immutable = value:
    assert builtins.isString value && builtins.substring 0 11 value == "/nix/store/";
    builtins.storePath value;
  source = immutable runtimeSource;
  candidate = immutable packageRoot;
  fixture = immutable fixtureBinary;
  manifest = immutable manifestFile;
  lock = builtins.fromJSON (builtins.readFile (source + "/flake.lock"));
  locked = lock.nodes.${lock.nodes.root.inputs.nixpkgs}.locked;
  nixpkgs = builtins.fetchTree {
    inherit (locked) type owner repo rev narHash;
  };
  pkgs = import nixpkgs.outPath { system = "x86_64-linux"; };
  counter = pkgs.writeShellScriptBin "managed-naming-smoke-counter" ''
    exec ${pkgs.nftables}/bin/nft -j list counter inet managed_naming_smoke denied
  '';
  rules = pkgs.writeText "managed-naming-smoke.nft" ''
    table inet managed_naming_smoke {
      counter denied { }
      chain output {
        type filter hook output priority 0; policy accept;
        meta skuid 1000 tcp dport 39991 counter name denied drop
        meta skuid 1000 oifname "lo" accept
        meta skuid 1000 counter name denied drop
      }
    }
  '';
in
pkgs.testers.runNixOSTest {
  name = "managed-session-naming-child";
  nodes.machine = {
    users.users.developer = {
      isNormalUser = true;
      uid = 1000;
    };
    i18n.defaultLocale = "en_US.UTF-8";
    environment.systemPackages = [
      pkgs.coreutils
      pkgs.iproute2
      pkgs.nftables
      pkgs.systemd
      counter
    ];
    security.sudo.extraRules = [{
      users = [ "developer" ];
      commands = [{
        command = "/run/current-system/sw/bin/managed-naming-smoke-counter";
        options = [ "NOPASSWD" ];
      }];
    }];
    # Keep the actual candidate and fixture closures available inside the VM.
    # No host module, workspace registration, auth, home or profile is mounted.
    system.extraDependencies = [ source candidate fixture manifest ];
    system.stateVersion = "26.05";
  };
  testScript = ''
    import shlex

    machine.start()
    machine.wait_for_unit("multi-user.target")
    machine.succeed("test $(id -u developer) = 1000")
    machine.succeed("test -f /sys/fs/cgroup/cgroup.controllers")
    machine.succeed("loginctl enable-linger developer")
    machine.succeed("systemctl start user@1000.service")
    machine.wait_for_unit("user@1000.service")
    machine.wait_until_succeeds("test -S /run/user/1000/bus")
    # Install confinement before running any developer/native process. Both IP
    # families use the same UID-scoped chain and one monotonic named counter.
    machine.succeed("nft --check -f ${rules}")
    machine.succeed("nft -f ${rules}")
    machine.succeed("nft list counter inet managed_naming_smoke denied")

    argv = [
        "env", "-i",
        "PATH=/run/current-system/sw/bin", "HOME=/home/developer",
        "USER=developer", "LOGNAME=developer", "LANG=C.UTF-8",
        "XDG_RUNTIME_DIR=/run/user/1000",
        "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus",
        "MANAGED_NAMING_SMOKE_VM=disposable-nixos-user-manager-v1",
        "MANAGED_NAMING_SMOKE_SOURCE=${source}",
        "MANAGED_NAMING_SMOKE_PACKAGE=${candidate}",
        "MANAGED_NAMING_SMOKE_BINARY=${fixture}",
        "MANAGED_NAMING_SMOKE_MANIFEST=${manifest}",
        "${fixture}", "-test.v", "-test.timeout=20m",
        "-test.run=^(TestManagedNamingRuntimeIntegration|TestNativeNamingRuntimeHTTPFailure)$",
    ]
    with subtest("reviewed native child and real user-manager lifetime"):
        machine.succeed(
            "runuser -u developer -- " + shlex.join(argv), timeout=1250
        )
    # A failed Go assertion remains a VM failure. Emergency cleanup is confined
    # to its recorded units; VM destruction is the final boundary on driver loss.
  '';
}
