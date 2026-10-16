let f = builtins.getFlake "git+file:///home/aither/.local/state/dev-workspaces/coordination/sources/40172e5fbef65c60e89b5977bae023e724572e9e/checkout?rev=40172e5fbef65c60e89b5977bae023e724572e9e";
 p = f.inputs.nixpkgs.legacyPackages.x86_64-linux;
 c = f.inputs.confctl.packages.x86_64-linux.confctl;
 h = builtins.storePath "/nix/store/irchsvsygv6gw2xckmx1w8n63ya4an4m-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/bin/workspace-confctl-adapter";
in p.writeShellScriptBin "workspace-confctl-environment" ''
 export GEM_HOME="${c.deps}/${c.ruby.gemPath}"
 export GEM_PATH="$GEM_HOME"
 export RUBYLIB="${c.src}/lib"
 export PATH="${p.lib.makeBinPath [p.git p.openssh p.nix]}:$PATH"
 exec ${c.ruby}/bin/ruby ${h} --pinned
''
