{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    vpsadminos.url = "github:vpsfreecz/vpsadminos/staging";
  };
  
  outputs = { self, nixpkgs, vpsadminos }: {
    # The configuration must include a system named "vps"
    nixosConfigurations.vps = nixpkgs.lib.nixosSystem {
      modules = [
        ({ config, pkgs, lib, ... }:
        {
          imports = [
            vpsadminos.nixosModules.containerStable
          ];

          environment.systemPackages = with pkgs; [
            vim
          ];

          services.openssh.enable = true;
          services.openssh.settings.PermitRootLogin = "yes";
          #users.extraUsers.root.openssh.authorizedKeys.keys =
          #  [ "..." ];

          systemd.extraConfig = ''
            DefaultTimeoutStartSec=900s
          '';

          time.timeZone = "Europe/Amsterdam";

          nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";

          system.stateVersion = "24.11";
        })
      ];
    };
  };
}
