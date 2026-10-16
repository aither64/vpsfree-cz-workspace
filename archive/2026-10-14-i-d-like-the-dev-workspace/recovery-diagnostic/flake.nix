{
  description = "Fixture-only diagnostic for the frozen b8a6 recovery failure";

  inputs.runtime.url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=b8a6be26a75347dcc9ec0fd1330dff886e47c93f";

  outputs = { runtime, ... }:
    let
      system = "x86_64-linux";
      pkgs = import runtime.inputs.nixpkgs { inherit system; };
      devWorkspace = runtime.packages.${system}.dev-workspace;
      expectedProduct = "/nix/store/54cv3sm4z10nal6hi4p214vds9cmjddd-dev-workspace-0.2.0";
      # Isolate fixture inputs from logs/provenance written alongside the wrapper.
      # Product source remains runtime; no diagnostic file enters that package.
      probeSource = builtins.path { path = ./raise-observer.rb; name = "recovery-raise-observer.rb"; };
      fixtureSource = builtins.path { path = ./session-recovery-diagnostic.nix; name = "session-recovery-diagnostic.nix"; };
      collectorSource = builtins.path { path = ./collect-metadata.py; name = "recovery-collect-metadata.py"; };
      probe = pkgs.replaceVars probeSource {
        packageRoot = toString devWorkspace;
      };
      diagnostic = import fixtureSource {
        inherit pkgs devWorkspace probe;
        self = runtime;
        collector = collectorSource;
      };
    in
    assert runtime.rev == "b8a6be26a75347dcc9ec0fd1330dff886e47c93f";
    assert toString devWorkspace == expectedProduct;
    {
      checks.${system}.session-recovery-diagnostic = diagnostic;
      lib.provenance = {
        runtimeRevision = runtime.rev;
        runtimeSource = toString runtime;
        runtimeLock = "${runtime}/flake.lock";
        nixpkgsRevision = runtime.inputs.nixpkgs.rev;
        product = toString devWorkspace;
        productDrv = devWorkspace.drvPath;
        originalCheckDrv = runtime.checks.${system}.session-recovery-boot.drvPath;
        diagnosticDrv = diagnostic.drvPath;
        observer = toString probe;
        ruby = "${pkgs.ruby}/bin/ruby";
      };
    };
}
