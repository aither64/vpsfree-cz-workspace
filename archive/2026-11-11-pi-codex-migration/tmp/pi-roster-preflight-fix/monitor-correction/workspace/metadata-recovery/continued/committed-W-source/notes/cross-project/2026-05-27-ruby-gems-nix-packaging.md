# Ruby Code Packaged As Nix Gems Must Be Rebuilt

- Date: 2026-05-27
- Project: cross-project
- Initiative: none
- Command/workflow: vpsAdminOS `make gems` / `make commit-gems`;
  vpsAdmin `rake vpsadmin:gems`
- Symptom: integration tests or deployments may keep using older Ruby code even
  after source files were changed.
- Cause: some Ruby tools are packaged for Nix as gems, so the packaged gem
  output must be refreshed for Nix builds to consume the new code.
- Fix/workaround: rebuild the gems after functional Ruby changes to packaged
  tools such as vpsAdminOS `osctl` components or vpsAdmin `nodectl` programs.
  Commit gem rebuilds separately from functional changes.
- Verification: review the generated gem-package diff and run the relevant
  integration tests using the rebuilt package.
