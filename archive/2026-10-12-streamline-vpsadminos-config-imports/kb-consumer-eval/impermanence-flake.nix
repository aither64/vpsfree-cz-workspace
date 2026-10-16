{
  inputs = {
    vpsadminos.url = "github:vpsfreecz/vpsadminos";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    impermanence.url = "github:nix-community/impermanence";
  };

  outputs = { nixpkgs, vpsadminos, impermanence, ... }: {
    nixosConfigurations.vps = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        vpsadminos.nixosModules.containerStable
        impermanence.nixosModules.impermanence
        ./configuration.nix
      ];
    };
  };
}
