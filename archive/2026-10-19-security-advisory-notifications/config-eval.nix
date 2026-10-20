let
  flake = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-cz-configuration";
  confDir = flake.outPath;
  inputs = flake.inputs;
  confctlSrc = inputs.confctl.outPath;
  system = "x86_64-linux";
  machineName = "cz.vpsfree/containers/int.vpsfbot";
  machine = flake.confctl.machines.${machineName};
  plan = flake.confctl.buildPlan.${machineName};
  corePkgs = import inputs.nixpkgs { inherit system; };
  coreLib = corePkgs.lib;
  confLib = import (confctlSrc + "/nix/lib") {
    inherit confDir corePkgs coreLib;
  };
  flakeInputs = coreLib.filterAttrs (name: _: name != "self") inputs;
  confData = import (confDir + "/data/default.nix") { lib = coreLib; };
  configurationRevision =
    if flake ? rev then flake.rev
    else if flake ? dirtyRev then coreLib.removeSuffix "-dirty" flake.dirtyRev
    else null;
  configurationInfo = if configurationRevision == null then null else {
    schemaVersion = 1;
    revision = configurationRevision;
    revisionDirty = !(flake ? rev) && flake ? dirtyRev;
  };
  confMachine = machine.metaConfig // { name = machine.clusterName; };
  moduleArgs = {
    inherit confDir confLib configurationInfo flakeInputs confData confMachine;
    inputs = plan.inputs;
    inputsInfo = plan.inputsInfo;
  };
  nixpkgs = inputs.${plan.inputsInfo.nixpkgs.input};
  evaluated = nixpkgs.lib.nixosSystem {
    inherit system;
    specialArgs = moduleArgs;
    modules = [
      ({ ... }: { _module.args = moduleArgs; })
      (confctlSrc + "/nix/modules/cluster")
    ]
    ++ (import (confDir + "/cluster/module-list.nix"))
    ++ [ (confDir + "/cluster/${machine.clusterName}/config.nix") ]
    ++ (map (name: confctlSrc + "/nix/modules/confctl/${name}.nix") [
      "generations"
      "cli"
      "nix"
      "inputs-info"
      "configuration-info"
    ])
    ++ (import (confctlSrc + "/nix/modules/system-list.nix")).nixos
    ++ (import (confDir + "/modules/module-list.nix")).nixos
    ++ machine.extraModules;
  };
  instance = evaluated.config.services.vpsfree-irc-bot.instances.libera;
  generatedSettings = {
    state_dir = "${evaluated.config.services.vpsfree-irc-bot.stateDir}/libera";
  } // instance.settings;
  settingsFile = evaluated.pkgs.writeText "vpsfree-irc-bot-libera.json" (
    builtins.toJSON generatedSettings
  );
  execStart = evaluated.config.systemd.services.vpsfree-irc-bot-libera.serviceConfig.ExecStart;
  packageDefinition = import (confDir + "/packages/vpsfree-irc-bot/default.nix") {
    bundlerEnv = args: args;
    fetchFromGitHub = args: args;
    lib = coreLib;
  };
in
assert instance.settings.security_advisories == {
  mode = "summary";
  summary_interval = 3600;
  channels = [ "#vpsfree" ];
};
# hasInfix uses a regex; discard context only from the assertion's needle.
assert coreLib.hasInfix (builtins.unsafeDiscardStringContext "--config ${settingsFile}") execStart;
{
  machine = machineName;
  advisorySettings = instance.settings.security_advisories;
  generatedAdvisorySettings = (builtins.fromJSON settingsFile.text).security_advisories;
  generatedSettingsPath = toString settingsFile;
  packagePath = toString instance.package;
  packageDerivation = instance.package.drvPath;
  source = packageDefinition.gemdir;
  inherit execStart;
  extraConfigFiles = instance.extraConfigFiles;
}
