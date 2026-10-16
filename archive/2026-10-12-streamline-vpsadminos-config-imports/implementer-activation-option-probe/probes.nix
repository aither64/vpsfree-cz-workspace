let
  checkout = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  vpsadminos = builtins.getFlake (toString checkout);
  lock = builtins.fromJSON (builtins.readFile (checkout + "/flake.lock"));
  fixtures = import (checkout + "/tests/fixtures/nixos-container-releases.nix") {
    inherit vpsadminos;
  };
  lib = vpsadminos.inputs.nixpkgs.lib;
  releases = [ "25.11" "26.05" "unstable" ];
  variants = [
    "baseline"
    "usersDependency"
    "beforeString"
    "beforeText"
    "specialfsDependency"
    "normalizeApply"
  ];
  preparationName = "zProbeCriticalStorage";
  preparationMarker = "VPSADMINOS_SESSION_PREPARATION_PROBE";
  # This is an option/ordering probe only. Nothing here is executed, and this
  # harmless text does not implement production preparation or failure guards.
  preparation = {
    text = ": ${preparationMarker}\n";
    supportsDryActivation = false;
  };

  candidateModule = variant: { config, lib, ... }:
    if variant == "baseline" then { }
    else if variant == "usersDependency" then {
      system.activationScripts.users.deps = [ "specialfs" ];
    }
    else if variant == "beforeString" then {
      system.activationScripts.specialfs = lib.mkBefore preparation.text;
      system.activationScripts.users.deps = [ "specialfs" ];
    }
    else if variant == "beforeText" then {
      system.activationScripts.specialfs.text = lib.mkBefore preparation.text;
      system.activationScripts.users.deps = [ "specialfs" ];
    }
    else if variant == "specialfsDependency" then {
      system.activationScripts.${preparationName} = preparation;
      system.activationScripts.specialfs.deps = [ preparationName ];
      system.activationScripts.users.deps = [ "specialfs" ];
    }
    else if variant == "normalizeApply" then {
      # Test the architect's candidate public option declaration directly.
      # The upstream apply function is already declared in current sources;
      # duplicate-declaration rejection must be reported, not worked around.
      options.system.activationScripts = lib.mkOption {
        apply = set:
          let
            original = set.specialfs;
            normalized = if builtins.isString original then {
              text = original;
              deps = [ ];
              supportsDryActivation = false;
            } else original;
          in set // {
            specialfs = normalized // {
              deps = (normalized.deps or [ ]) ++ [ preparationName ];
            };
          };
      };
      config.system.activationScripts = {
        ${preparationName} = preparation;
        users.deps = [ "specialfs" ];
      };
    }
    else throw "Unknown session probe variant: ${variant}";

  evaluateSystem = release: variant:
    let
      guest = fixtures.${release};
      compatibility =
        if release == "unstable" then vpsadminos.nixosModules.containerUnstable
        else vpsadminos.nixosModules.containers.${release};
    in guest.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        compatibility
        vpsadminos.inputs.impermanence.nixosModules.impermanence
        {
          system.stateVersion = "25.11";
          fileSystems."/" = { device = "none"; fsType = "tmpfs"; };
          fileSystems."/persistent" = {
            device = "none";
            fsType = "tmpfs";
            neededForBoot = true;
          };
          environment.persistence."/persistent" = {
            hideMounts = true;
            directories = [ "/var/lib/nixos" "/var/log" ];
          };
          users.groups.preservation-test = { };
          users.users.preservation-test = {
            isSystemUser = true;
            group = "preservation-test";
          };
        }
        (candidateModule variant)
      ];
    };

  # lib.hasInfix builds a regexp; its needle must not carry store context.
  # These are comparisons only. Keep generated scripts and fixtures intact.
  contains = needle: text: lib.hasInfix (builtins.unsafeDiscardStringContext needle) text;
  lineMatches = needle: text:
    let
      lines = lib.splitString "\n" text;
      numbered = lib.imap1 (number: line: { inherit number line; }) lines;
    in builtins.filter (entry: contains needle entry.line) numbered;
  lineNumber = needle: text:
    let matches = lineMatches needle text;
    in if matches == [ ] then null else (builtins.head matches).number;
  count = needle: text: builtins.length (lineMatches needle text);

  evaluate = release: variant:
    let
      evaluated = evaluateSystem release variant;
      c = evaluated.config;
      scripts = c.system.activationScripts;
      baselineScripts = (evaluateSystem release "baseline").config.system.activationScripts;
      specialfsText = if builtins.isString scripts.specialfs then scripts.specialfs else scripts.specialfs.text;
      baselineSpecialfsText = if builtins.isString baselineScripts.specialfs then baselineScripts.specialfs else baselineScripts.specialfs.text;
      actual = scripts.script;
      dry = c.system.dryActivationScript;
      source = "source ${c.system.build.earlyMountScript}";
      positions = {
        preparation = lineNumber preparationMarker actual;
        specialfs = lineNumber "#### Activation script snippet specialfs:" actual;
        source = lineNumber source actual;
        users = lineNumber "#### Activation script snippet users:" actual;
        allocator = lineNumber "-update-users-groups.pl" actual;
        creator = lineNumber "#### Activation script snippet createPersistentStorageDirs:" actual;
      };
    in {
      guestRelease = c.system.nixos.release;
      stateVersion = c.system.stateVersion;
      backend = { sysusers = c.systemd.sysusers.enable; userborn = c.services.userborn.enable; };
      specialfsIsString = builtins.isString scripts.specialfs;
      specialfsDeps = if builtins.isString scripts.specialfs then [ ] else scripts.specialfs.deps;
      usersDeps = scripts.users.deps;
      inherit positions;
      upstreamMountBodyPreservedOnce =
        count "specialMount()" actual == 1
        && count source actual == 1
        && contains baselineSpecialfsText specialfsText;
      usersDependsOnSpecialfs = builtins.elem "specialfs" scripts.users.deps;
      sourceBeforeAllocator = positions.source < positions.allocator;
      preparationBeforeSource = positions.preparation != null && positions.preparation < positions.source;
      dry = {
        preparationCount = count preparationMarker dry;
        mountFunctionCount = count "specialMount()" dry;
        mountSourceCount = count source dry;
        allocatorCount = count "-update-users-groups.pl" dry;
        specialfsOmissionMarker = contains "Activation script snippet specialfs does not support dry activation." dry;
      };
      # Preserve full generated text for a successful shape's independent
      # inspection; this forces script generation, not a system build or boot.
      activationScript = actual;
      dryActivationScript = dry;
    };

  attempt = release: variant:
    let
      result = builtins.tryEval (builtins.deepSeq (evaluate release variant) (evaluate release variant));
    in {
      success = result.success;
      value = if result.success then result.value else null;
    };

  sourceFixture = release:
    let
      guest = fixtures.${release};
      node = if release == "unstable" then lock.nodes.${lock.nodes.root.inputs.nixpkgsUnstable}
        else if release == "26.05" then lock.nodes.${lock.nodes.root.inputs.nixpkgs}
        else { locked = {
          rev = "b6018f87da91d19d0ab4cf979885689b469cdd41";
          narHash = "sha256-twXPFqFsrrY5r28Zh7Homgcp2gUMBgQ6WDS98Q/3xFI=";
        }; };
    in {
      sourcePath = toString guest.outPath;
      actualRelease = guest.lib.trivial.release;
      locked = node.locked;
    };
in {
  inherit evaluate;
  matrix = {
    purpose = "Session-only activation option merging and generated-order probe; no production preparation or runtime claim";
    sourceFixtures = lib.genAttrs releases sourceFixture;
    impermanence = {
      sourcePath = toString vpsadminos.inputs.impermanence.outPath;
      locked = lock.nodes.${lock.nodes.root.inputs.impermanence}.locked;
    };
    probes = lib.genAttrs releases (release: lib.genAttrs variants (attempt release));
  };
}
