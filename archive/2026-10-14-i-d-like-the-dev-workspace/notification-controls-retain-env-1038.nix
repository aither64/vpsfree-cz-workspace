let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/vpsfree-cz-configuration?rev=2dfbf7ade3bfc9a7c60dd827959319c63b93c154";
 p = f.inputs.nixpkgs.legacyPackages.x86_64-linux;
 c = f.inputs.confctl.packages.x86_64-linux.confctl;
 h = builtins.storePath "/nix/store/g2bnifmisaznv1p14wpjxdycmw7cd0fl-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/bin/workspace-confctl-adapter";
in p.writeShellScriptBin "workspace-confctl-environment" ''
 export GEM_HOME="${c.deps}/${c.ruby.gemPath}"
 export GEM_PATH="$GEM_HOME"
 export RUBYLIB="${c.src}/lib"
 export PATH="${p.lib.makeBinPath [p.git p.openssh p.nix]}:$PATH"
 exec ${c.ruby}/bin/ruby ${h} --pinned
''
