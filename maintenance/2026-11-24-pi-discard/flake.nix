{
  description = "Dated Pi preparation discard bridge for aitherdev";

  inputs.site.url = "github:aither64/vpsfree-cz-workspace/b095ac05040be226258afc16233d76969476f1f6";

  outputs =
    { site, ... }:
    let
      system = "x86_64-linux";
      pkgs = import site.inputs.nixpkgs { inherit system; };
      runtime = site.inputs.vpsfree-dev-workspace.inputs.dev-workspace;
      patchedSource =
        pkgs.runCommand "dev-workspace-pi-discard-source"
          {
            nativeBuildInputs = [ pkgs.gitMinimal ];
          }
          ''
            mkdir "$out"
            cp -a ${runtime}/. "$out/"
            chmod -R u+w "$out"
            cd "$out"
            git apply --check --binary ${./bridge.patch}
            git apply --binary ${./bridge.patch}
          '';
    in
    {
      packages.${system} = {
        # Keep the exact selected predecessor's site composition and change only
        # its runtime source. The ordinary workspace package remains epoch 3.
        default = site.packages.${system}.default.override {
          src = patchedSource;
        };

        # Separate operator artifact, not installed by the bridge or the system.
        pi-discard-grant =
          pkgs.runCommand "pi-discard-grant"
            {
              nativeBuildInputs = [ pkgs.go ];
              CGO_ENABLED = "0";
              GOENV = "off";
              GOTOOLCHAIN = "local";
              GOPROXY = "off";
              GOSUMDB = "off";
            }
            ''
              export HOME="$TMPDIR"
              mkdir -p "$out/bin"
              go build -trimpath -ldflags=-buildid= -o "$out/bin/pi-discard-grant" ${./publisher.go}
              chmod 0755 "$out/bin/pi-discard-grant"
            '';
      };
    };
}
