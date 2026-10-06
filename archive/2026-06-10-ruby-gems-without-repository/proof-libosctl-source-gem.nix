let
  root = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-10-ruby-gems-without-repository/vpsadminos;
  flake = builtins.getFlake ("path:" + toString root);
  system = "x86_64-linux";
  pkgs = import flake.inputs.nixpkgs {
    inherit system;
    overlays = import (root + "/os/overlays");
  };
in
pkgs.buildRubyGem {
  gemName = "libosctl";
  version = "26.05.0";
  ruby = pkgs.ruby_vpsadminos;
  src = root;
  dontBuild = false;
  nativeBuildInputs = [ pkgs.gitMinimal ];
  unpackPhase = ''
    runHook preUnpack
    cp -a "$src" source
    chmod -R u+w source
    sourceRoot=source/libosctl
    cd "$sourceRoot"
    runHook postUnpack
  '';
  preBuild = ''
    git init
    git add .
  '';
}
