# Explicit inputs keep this evaluator usable in normal pure flake checks.
{
  source,
  fixtures,
  oldSource,
  impermanenceModule,
  lib,
  system,
}:
let
  rawPath =
    release:
    if release == "unstable" then "unstable/vpsadminos.nix" else "stable/vpsadminos-${release}.nix";
  raw = base: release: import (base + "/os/lib/nixos-container/${rawPath release}");
  evaluate =
    release: module: extra:
    (fixtures.${release}.lib.nixosSystem {
      inherit system;
      modules = [
        module
        {
          system.stateVersion = "22.11";
          fileSystems."/" = {
            device = "none";
            fsType = "tmpfs";
          };
        }
      ]
      ++ extra;
    }).config;
  persistence = {
    imports = [ impermanenceModule ];
    environment.persistence."/persistent" = {
      hideMounts = true;
      directories = [
        "/var/lib/nixos"
        "/var/log"
      ];
    };
  };
  bind = what: where: {
    inherit what where;
    type = "none";
    options = "bind,x-gvfs-hide";
  };
  manual = mounts: { systemd.mounts = mounts; };
  contains = needle: text: lib.hasInfix (builtins.unsafeDiscardStringContext needle) text;
  position =
    needle: text:
    (lib.findFirst (entry: contains needle entry.line) { index = -1; } (
      lib.imap0 (index: line: { inherit index line; }) (lib.splitString "\n" text)
    )).index;
  count = needle: text: builtins.length (lib.filter (contains needle) (lib.splitString "\n" text));
  before =
    first: second: text:
    position first text >= 0 && position second text >= 0 && position first text < position second text;
  check = label: condition: if condition then true else throw "Persistence check failed: ${label}";
  script = c: c.system.activationScripts.script;
  mounts = c: c.system.build.earlyMountScript.text;
  force = c: builtins.deepSeq [ (script c) (mounts c) c.system.dryActivationScript ] true;
  failure = c: !(builtins.tryEval (force c)).success;
  checkRelease =
    release:
    let
      current = extra: evaluate release (raw source release) extra;
      baseline = extra: evaluate release (raw oldSource release) extra;
      ordinary = current [ ];
      persisted = current [ persistence ];
      copied = builtins.toFile "vpsadminos-persistence-${release}.nix" (
        builtins.readFile (source + "/os/lib/nixos-container/${rawPath release}")
      );
      standalone = evaluate release (import copied) [ persistence ];
      alternative =
        base: backend:
        evaluate release (raw base release) [
          persistence
          {
            systemd.sysusers.enable = backend == "sysusers";
            services.userborn.enable = backend == "userborn";
          }
        ];
      ancestry = current [
        (manual [
          (bind "/persistent/state" "/var/lib/nixos")
          (bind "/var/lib/nixos/log" "/var/log")
        ])
      ];
      dependent = current [
        (manual [
          (bind "/persistent/state" "/var/lib/nixos")
          (bind "/var/lib/nixos/usr" "/usr")
        ])
      ];
      root = current [ (manual [ (bind "/root-state/nixos" "/var/lib/nixos") ]) ];
      declared = current [
        (manual [ (bind "/custom/backing/state" "/var/lib/nixos") ])
        {
          fileSystems."/custom/backing" = {
            device = "/host/custom";
            fsType = "none";
            options = [ "bind" ];
            neededForBoot = true;
          };
        }
      ];
      nearPrefix = current [
        (manual [ (bind "/custom/backing-other/state" "/var/lib/nixos") ])
        {
          fileSystems."/custom/backing" = {
            device = "/host/custom";
            fsType = "none";
            options = [ "bind" ];
            neededForBoot = true;
          };
        }
      ];
      nonBind = current [
        (manual [ (bind "/custom/backing/state" "/var/lib/nixos") ])
        {
          fileSystems."/custom/backing" = {
            device = "tmpfs";
            fsType = "tmpfs";
            neededForBoot = true;
          };
        }
      ];
      cycle = current [
        (manual [
          (bind "/var/log/state" "/var/lib/nixos")
          (bind "/var/lib/nixos/log" "/var/log")
        ])
      ];
      forced = current [
        persistence
        { system.activationScripts.specialfs = lib.mkForce "guest-specialfs"; }
      ];
      direct = current [
        {
          fileSystems."/var/log" = {
            device = "/direct/log";
            fsType = "none";
            options = [ "bind" ];
          };
        }
      ];
      old = baseline [ persistence ];
      upstreamSource = "source ${persisted.system.build.earlyMountScript}";
    in
    {
      actualRelease = persisted.system.nixos.release;
      legacyOrder = check "${release} global specialfs before real allocator" (
        before upstreamSource "-update-users-groups.pl" (script persisted)
        && builtins.elem "specialfs" persisted.system.activationScripts.users.deps
        && count upstreamSource (script persisted) == 1
        && count "specialMount()" (script persisted) == 1
        && force persisted
      );
      promotion = check "${release} complete promotion and units/options" (
        mounts persisted == mounts old
        &&
          lib.all
            (
              target:
              persisted.boot.specialFileSystems.${target}.options == [
                "bind"
                "x-gvfs-hide"
              ]
              && lib.any (m: m.where == target && m.options == "bind,x-gvfs-hide") persisted.systemd.mounts
            )
            [
              "/var/lib/nixos"
              "/var/log"
            ]
      );
      standalone = check "${release} copied self-contained file" (script standalone == script persisted);
      dry = check "${release} dry omits mounts and prep" (
        !contains "vpsadminosPrepareStateDirectory" persisted.system.dryActivationScript
        && !contains upstreamSource persisted.system.dryActivationScript
        && contains "-update-users-groups.pl" persisted.system.dryActivationScript
      );
      ordinary = check "${release} ordinary exact baseline equivalence" (
        script ordinary == script (baseline [ ])
        && ordinary.system.dryActivationScript == (baseline [ ]).system.dryActivationScript
        && force ordinary
      );
      alternatives = lib.genAttrs [ "sysusers" "userborn" ] (
        backend:
        let
          c = alternative source backend;
          b = alternative oldSource backend;
        in
        check "${release} ${backend} exact baseline equivalence" (
          c.system.activationScripts.users == ""
          && script c == script b
          && c.system.dryActivationScript == b.system.dryActivationScript
          && force c
        )
      );
      ancestry = check "${release} selected source ancestry" (
        before "\"/persistent/state\" \"/var/lib/nixos\"" "\"/var/lib/nixos/log\" \"/var/log\"" (
          mounts ancestry
        )
        && force ancestry
      );
      topology = check "${release} valid selected-to-ordinary topology" (
        before "\"/persistent/state\" \"/var/lib/nixos\"" "\"/var/lib/nixos/usr\" \"/usr\"" (
          mounts dependent
        )
        && force dependent
      );
      root = check "${release} root-backed source allowed" (
        force root
        && contains (lib.escapeShellArg "/root-state/nixos") root.system.activationScripts.specialfs.text
      );
      declared = check "${release} declared backing in original global order" (
        before "\"/host/custom\" \"/custom/backing\"" "\"/custom/backing/state\" \"/var/lib/nixos\"" (
          mounts declared
        )
        && contains (lib.escapeShellArgs [
          "bind"
          "/host/custom"
          "/custom/backing"
        ]) declared.system.activationScripts.specialfs.text
        && force declared
      );
      pathComponents = check "${release} backing checks respect path components" (
        !contains (lib.escapeShellArgs [
          "bind"
          "/host/custom"
          "/custom/backing"
        ]) nearPrefix.system.activationScripts.specialfs.text
        && force nearPrefix
      );
      nonBindBacking = check "${release} non-bind backing retains presence-only check" (
        contains (lib.escapeShellArgs [
          "filesystem"
          "tmpfs"
          "/custom/backing"
        ]) nonBind.system.activationScripts.specialfs.text
        && force nonBind
      );
      cycle = check "${release} upstream cycle remains an error" (failure cycle);
      mkForce = check "${release} guest mkForce retains precedence" (
        forced.system.activationScripts.specialfs == "guest-specialfs" && force forced
      );
      direct = check "${release} direct filesystems retain upstream activation" (
        script direct == script (baseline [
          {
            fileSystems."/var/log" = {
              device = "/direct/log";
              fsType = "none";
              options = [ "bind" ];
            };
          }
        ])
        && force direct
      );
    };
  shellConfig =
    mode:
    evaluate "26.05" (raw source "26.05") (
      [
        (manual [
          (bind "/fixture/backing storage/nixos" "/var/lib/nixos")
          (bind "/fixture/backing storage/log" "/var/log")
        ])
      ]
      ++ lib.optional (mode != "undeclared") {
        fileSystems."/fixture/backing storage" = {
          device = if mode == "filesystem" then "tmpfs" else "/fixture/host storage";
          fsType = if mode == "filesystem" then "tmpfs" else "none";
          options = lib.optional (mode != "filesystem") "bind";
          neededForBoot = true;
        };
      }
    );
in
{
  assertions = {
    releases = lib.genAttrs [ "25.11" "26.05" "unstable" ] checkRelease;
    latestStable = check "latest stable equals self-contained 26.05" (
      builtins.readFile (source + "/os/lib/nixos-container/stable/vpsadminos.nix")
      == builtins.readFile (source + "/os/lib/nixos-container/stable/vpsadminos-26.05.nix")
    );
  };
  shellFixtures = lib.genAttrs [ "declared" "undeclared" "filesystem" ] (
    name:
    let
      c = shellConfig name;
    in
    {
      snippet = c.system.activationScripts.specialfs.text;
      earlyMountScript = c.system.build.earlyMountScript;
    }
  );
}
