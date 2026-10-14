{
  schema = 1;
  recipes = { }; # The organization extension supplies workspace-pins.
  refreshes = {
    workspace = {
      name = "workspace-pins";
      parameters = {
        type = "nix_input";
        repository = "dev-workspace";
        inputPath = [
          "vpsfree-dev-workspace"
          "dev-workspace"
        ];
        urlAttribute = "inputs.dev-workspace.url";
        urlPrefix = "github:aither64/dev-workspace";
      };
    };
    vpsfree-cz-configuration = {
      name = "workspace-pins";
      parameters = {
        type = "confctl_channel";
        repository = "dev-workspace";
        inputPath = [ "devWorkspace" ];
        channel = "dev-workspace";
        role = "devWorkspace";
      };
    };
  };
}
