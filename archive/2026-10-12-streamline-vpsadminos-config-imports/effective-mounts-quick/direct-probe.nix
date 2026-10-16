let
  source = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  flake = builtins.getFlake ("git+file://" + toString source);
  fixtures = import (source + "/tests/fixtures/nixos-container-persistence.nix") { system = "x86_64-linux"; };
  original = builtins.readFile (source + "/tests/nixos-container-persistence-eval.nix");
  instrumented = builtins.replaceStrings [
    ''check = label: condition: if condition then true else throw "Persistence check failed: ''
    ''      ancestors = check''
  ] [
    ''check = label: condition: if true then condition else throw "Persistence check failed: ''
    ''      directDebug = {
        direct = adapted direct;
        state = adapted directState;
        nonbind = adapted directNonBind;
        recursive = adapted rbind;
        source = contains (lib.escapeShellArg "/direct/log") direct.system.activationScripts.specialfs.text;
        nonbindOptions = contains (lib.escapeShellArg "defaults,mode=0755") directNonBind.system.activationScripts.specialfs.text;
        rbindOptions = contains (lib.escapeShellArg "rbind,ro") rbind.system.activationScripts.specialfs.text;
        actualNonbindOptions = directNonBind.boot.specialFileSystems."/var/log".options;
        actualRbindOptions = rbind.boot.specialFileSystems."/var".options;
        nonbindSnippet = directNonBind.system.activationScripts.specialfs.text;
        rbindSnippet = rbind.system.activationScripts.specialfs.text;
      };
      ancestors = check''
  ] original;
  result = import (builtins.toFile "direct-diagnostic.nix" instrumented) {
    inherit source;
    system = "x86_64-linux";
    inherit (flake.inputs.nixpkgs) lib;
    inherit (fixtures) oldSource impermanenceModule;
    fixtures = fixtures.releases;
  };
in
builtins.mapAttrs (_: value: value.directDebug) result.assertions.releases
