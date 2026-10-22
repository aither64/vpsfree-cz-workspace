# Evidence-only view of the pinned confctl evaluator. This does not change the
# configuration repository or recreate its module/specialArgs composition.
{
  configurationRoot ? /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-development-session/vpsfree-cz-configuration,
  configurationReference ? "git+file://${toString configurationRoot}",
  hostNames ? [
    "cz.vpsfree/containers/int.blog"
    "cz.vpsfree/containers/int.kb"
    "cz.vpsfree/containers/int.utils"
    "cz.vpsfree/containers/int.web"
    "cz.vpsfree/machines/aitherdev"
    "cz.vpsfree/vpsadmin/int.webui-dev"
    "cz.vpsfree/vpsadmin/int.webui1"
    "cz.vpsfree/vpsadmin/int.webui2"
  ],
}:
let
  flake = builtins.getFlake configurationReference;
  inputs = flake.inputs // { self = flake; };
  source = inputs.confctl + "/nix/flake/mk-confctl-outputs.nix";
  sourceText = builtins.readFile source;
  needle = "  settings = settings;\n";
  replacement = ''
    evaluatedConfigurations = builtins.listToAttrs (map (m: {
      name = m.name;
      value = (evalConfigFor m).evalConfig;
    }) machinesWithKey);
    settings = settings;
  '';
  exposedSource = builtins.toFile "php-runtime-confctl-evaluator.nix" (
    builtins.replaceStrings [ needle ] [ replacement ] sourceText
  );
  confctl = import exposedSource {
    confDir = flake.outPath;
    inherit inputs;
    channels = flake.confctl.channels;
  };
  lib = inputs.nixpkgsStable.lib;
  sourceEvidence = src:
    if builtins.isAttrs src then {
      path = toString src;
      urls = src.urls or [ ];
      outputHash = src.outputHash or null;
    } else { path = toString src; };
  packageEvidence = p: {
    name = p.name;
    version = p.version or null;
    drvPath = p.drvPath;
    packagePath = p.outPath;
    phpIni = p.phpIni or null;
    unwrappedDrvPath = (p.unwrapped or p).drvPath;
    source = sourceEvidence (p.unwrapped or p).src;
    patches = map sourceEvidence ((p.unwrapped or p).patches or [ ]);
    sessionExtension = if p ? extensions.session then {
      version = p.extensions.session.version or null;
      drvPath = p.extensions.session.drvPath;
      patches = map sourceEvidence (p.extensions.session.patches or [ ]);
    } else null;
    postBuild = p.postBuild or null;
    postBuildContext = builtins.getContext (p.postBuild or "");
  };
  perHost = host:
    let
      system = confctl.evaluatedConfigurations.${host};
      inherit (system) config;
      pools = config.services.phpfpm.pools;
      poolEvidence = serviceConfig: name: pool:
        let
          command = serviceConfig.systemd.services."phpfpm-${name}".serviceConfig.ExecStart;
        in {
          phpPackage = packageEvidence pool.phpPackage;
          inherit (pool) phpOptions settings phpEnv extraConfig;
          execStart = command;
          execStartContext = builtins.getContext command;
        };
    in {
      globalPhpOptions = config.services.phpfpm.phpOptions;
      apacheEnablePHP = config.services.httpd.enablePHP;
      pools = builtins.mapAttrs (poolEvidence config) pools;
      nestedContainers = lib.mapAttrs (_: container: {
        inherit (container) autoStart;
        pools = builtins.mapAttrs (poolEvidence container.config) container.config.services.phpfpm.pools;
        apacheEnablePHP = container.config.services.httpd.enablePHP;
      }) config.containers;
      foto = if host != "cz.vpsfree/containers/int.web" then null else {
        poolPresent = pools ? foto;
        servicePresent = config.systemd.services ? "phpfpm-foto";
        sessionCleanupPools = config.vpsfconf.phpfpmSessionCleanup.pools;
        virtualHost = let v = config.services.nginx.virtualHosts."foto.vpsfree.cz"; in {
          inherit (v) root extraConfig enableACME forceSSL;
          locations = builtins.attrNames v.locations;
        };
        user = lib.getAttrs [ "isSystemUser" "group" "description" ] config.users.users.foto;
        groupPresent = config.users.groups ? foto;
      };
    };
in
assert lib.count (line: line == "  settings = settings;") (lib.splitString "\n" sourceText) == 1;
{
  provenance = {
    configurationSource = flake.outPath;
    configurationRevision = flake.rev or flake.dirtyRev or null;
    confctlSource = toString source;
    confctlSourceSha256 = builtins.hashString "sha256" sourceText;
    nixpkgsStableSource = inputs.nixpkgsStable.outPath;
    nixpkgsStableRevision = inputs.nixpkgsStable.rev;
    inherit needle replacement;
  };
  hosts = builtins.listToAttrs (map (host: { name = host; value = perHost host; }) hostNames);
}
