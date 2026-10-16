let
  project = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos";
  fixtures = import /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/tests/fixtures/nixos-container-releases.nix { vpsadminos = project; };
  lib = project.inputs.nixpkgs.lib;
  baseline = /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-v2-raw-baseline/os/lib/nixos-container;
  contains = needle: haystack: lib.hasInfix (builtins.unsafeDiscardStringContext needle) haystack;
  position = needle: text: (lib.findFirst (entry: contains needle entry.line) { index = -1; } (lib.imap0 (index: line: { inherit index line; }) (lib.splitString "\n" text))).index;
  test = release:
    let
      path = if release == "unstable" then "/unstable/vpsadminos.nix" else "/stable/vpsadminos-${release}.nix";
      evaluate = extra: (fixtures.${release}.lib.nixosSystem {
        system = "x86_64-linux";
        modules = [
          (import (baseline + path))
          project.inputs.impermanence.nixosModules.impermanence
          {
            system.stateVersion = "22.11";
            fileSystems."/" = { device = "none"; fsType = "tmpfs"; };
            environment.persistence."/persistent".directories = [ "/var/lib/nixos" "/var/log" ];
          }
        ] ++ extra;
      }).config;
      original = evaluate [];
      bridge = {
        system.activationScripts.specialfs = lib.mkOverride 90 {
          text = original.system.activationScripts.specialfs;
          supportsDryActivation = false;
        };
        system.activationScripts.users.deps = [ "specialfs" ];
      };
      revised = evaluate [ bridge ];
      custom = evaluate [ bridge { system.activationScripts.specialfs = lib.mkForce "printf 'guest-owned specialfs\\n'"; } ];
      source = "source ${revised.system.build.earlyMountScript}";
      normal = revised.system.activationScripts.script;
      sourcePosition = position source normal;
      userPosition = position "-update-users-groups.pl" normal;
      result = {
        actualRelease = revised.system.nixos.release;
        structuredValueAccepted = builtins.isAttrs revised.system.activationScripts.specialfs;
        originalBodyPreserved = revised.system.activationScripts.specialfs.text == original.system.activationScripts.specialfs;
        globalMountsPreserved = revised.system.build.earlyMountScript == original.system.build.earlyMountScript;
        mountScriptSourcedOnce = builtins.length (lib.filter (contains source) (lib.splitString "\n" normal)) == 1;
        specialfsBeforeUsers = sourcePosition >= 0 && userPosition >= 0 && sourcePosition < userPosition;
        dryHasNoMountBody = !(contains "specialMount()" revised.system.dryActivationScript) && !(contains source revised.system.dryActivationScript);
        guestForceRemainsEffective = custom.system.activationScripts.specialfs == "printf 'guest-owned specialfs\\n'" && contains "guest-owned specialfs" custom.system.activationScripts.script;
      };
    in builtins.deepSeq result result;
in lib.genAttrs [ "25.11" "26.05" "unstable" ] test
