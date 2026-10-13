let
  targets = {
    vpsadminos = "staging";
    security-advisories = "2026-07-13-security-advisory-automation";
    ruby-lxc = "vpsfree";
    linux = "vpsadminos-6.12";
    zfs = "vpsadminos-release-next";
  };
in
{
  schema = 1;
  adapters = { }; # The extension installs the immutable confctl adapter.
  machines.aitherdev = {
    id = "vpsfree:aitherdev";
    aliases = [
      "aitherdev.int.vpsfree.cz"
      "cz.vpsfree/machines/aitherdev"
    ];
    adapter = "confctl";
    configurationRepository = "vpsfree-cz-configuration";
    selector = "cz.vpsfree/machines/aitherdev";
  };
  profileMachine = "vpsfree:aitherdev";
  repositories =
    builtins.listToAttrs (
      map
        (project: {
          name = project;
          value = {
            remote = "git@github.com:vpsfreecz/${project}.git";
            defaultTarget = "refs/heads/${targets.${project} or "master"}";
          };
        })
        [
          "vpsadminos"
          "vpsadmin"
          "security-advisories"
          "vpsfree-kb-contracts"
          "ruby-lxc"
          "haveapi"
          "vpsf-status"
          "vpsadmin-go-client"
          "confctl"
          "vpsfree-cz-configuration"
          "vpsadminos-org-configuration"
          "vpsfree-irc-bot"
          "vpsfree-mail-templates"
          "terraform-provider-vpsadmin"
          "web"
          "ssh-exporter"
          "syslog-exporter"
          "vpsfree-client"
          "vpsfree-maintenance-tasks"
          "linux"
          "zfs"
        ]
    )
    // {
      workspace = {
        remote = "git@github.com:aither64/vpsfree-cz-workspace.git";
        defaultTarget = "refs/heads/master";
      };
      dev-workspace = {
        remote = "git@github.com:aither64/dev-workspace.git";
        defaultTarget = "refs/heads/master";
        inputPaths.workspace = [
          [
            "vpsfree-dev-workspace"
            "dev-workspace"
          ]
        ];
      };
      vpsfree-dev-workspace = {
        remote = "git@github.com:vpsfreecz/dev-workspace.git";
        defaultTarget = "refs/heads/master";
        inputPaths.workspace = [ [ "vpsfree-dev-workspace" ] ];
      };
      codex-web = {
        remote = "git@github.com:aither64/codex-web.git";
        defaultTarget = "refs/heads/master";
        inputPaths.workspace = [
          [
            "vpsfree-dev-workspace"
            "dev-workspace"
            "codex-web"
          ]
        ];
      };
    };
}
