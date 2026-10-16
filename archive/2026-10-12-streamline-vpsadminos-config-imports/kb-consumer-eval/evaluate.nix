let
  vpsadminos = builtins.getFlake (toString ../../../worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos);
  fixtures = import ../../../worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/tests/fixtures/nixos-container-releases.nix { inherit vpsadminos; };
  userdata = (import ./userdata-flake.nix).outputs {
    self = {}; inherit vpsadminos; nixpkgs = fixtures."24.11";
  };
  # The snippet extends an existing guest configuration. Preserve its installation
  # stateVersion in the fixture without changing the downloaded candidate text.
  guest2511 = fixtures."25.11";
  impermanence = (import ./impermanence-flake.nix).outputs {
    inherit vpsadminos;
    impermanence = vpsadminos.inputs.impermanence;
    nixpkgs = guest2511 // {
      lib = guest2511.lib // {
        nixosSystem = args: guest2511.lib.nixosSystem (args // {
          modules = args.modules ++ [{ system.stateVersion = "25.11"; }];
        });
      };
    };
  };
  a = userdata.nixosConfigurations.vps.config;
  b = impermanence.nixosConfigurations.vps.config;
  lib = guest2511.lib;
  stateBinding = lib.findFirst (mount:
    (mount.enable or true) && mount.where == "/var/lib/nixos"
    && mount.type == "none"
    && builtins.elem "bind" (lib.splitString "," mount.options)
  ) (throw "KB impermanence consumer has no allocation-state directory bind") b.systemd.mounts;
  activation = b.system.activationScripts;
  position = marker:
    let
      numbered = lib.imap0 (index: line: { inherit index line; })
        (lib.splitString "\n" activation.script);
    in (lib.findFirst (entry: lib.hasInfix marker entry.line) { index = -1; } numbered).index;
  activationOrder = {
    specialfs = position "#### Activation script snippet specialfs:";
    mountsSource = position (builtins.unsafeDiscardStringContext "source ${b.system.build.earlyMountScript}");
    users = position "#### Activation script snippet users:";
  };
in
assert a.system.nixos.release == "24.11";
assert a.system.stateVersion == "24.11";
assert b.system.nixos.release == "25.11";
assert b.system.stateVersion == "25.11";
assert a.boot.isContainer && b.boot.isContainer;
assert stateBinding.what == "/persistent/var/lib/nixos";
assert b.boot.specialFileSystems."/var/lib/nixos".device == stateBinding.what;
assert builtins.elem "specialfs" activation.users.deps;
assert !activation.specialfs.supportsDryActivation;
assert lib.hasInfix "vpsadminosMountPersistedState" activation.specialfs.text;
assert activationOrder.specialfs >= 0;
assert activationOrder.mountsSource >= 0 && activationOrder.users >= 0;
assert activationOrder.specialfs < activationOrder.mountsSource;
assert activationOrder.mountsSource < activationOrder.users;
{
  userdata = a.system.build.toplevel.drvPath;
  impermanence = b.system.build.toplevel.drvPath;
  earlyPersistentState = stateBinding.what;
  persistedStateActivation = {
    binding = { inherit (stateBinding) what where type options; };
    dependencies = activation.specialfs.deps;
    usersDependencies = activation.users.deps;
    order = activationOrder;
    snippet = activation.specialfs.text;
    earlyMountScript = b.system.build.earlyMountScript.text;
  };
}
