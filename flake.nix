{
  description = "vpsFree.cz development workspace policy and records";

  inputs = {
    nixpkgs.follows = "vpsfree-dev-workspace/nixpkgs";
    vpsfree-dev-workspace = {
      url = "github:vpsfreecz/dev-workspace/0ff827df13e82dfab4b536ff29979280f264e8f5";
      inputs.dev-workspace.url = "github:aither64/dev-workspace/66262519d497073d9bb0dccc2252cdec4528f389";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      vpsfree-dev-workspace,
      ...
    }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      teamConfig = import ./config/agent-teams.nix;
      siteConfig = {
        kb = {
          cz = {
            url = "https://kb.vpsfree.cz";
            tokenPath = "/home/aither/.codex/codex-kb-vpsfree-cz-aither-key";
            stagingUrl = "http://kb-cs.aitherdev.int.vpsfree.cz";
            stagingPasswordPath = "/home/aither/.codex/codex-kb-staging-cz-aither-password";
          };
          org = {
            url = "https://kb.vpsfree.org";
            tokenPath = "/home/aither/.codex/codex-kb-vpsfree-org-aither-key";
            stagingUrl = "http://kb-en.aitherdev.int.vpsfree.cz";
            stagingPasswordPath = "/home/aither/.codex/codex-kb-staging-org-aither-password";
          };
          stagingUsername = "aither";
          stageContainerctl = "/run/current-system/sw/bin/kb-staging-containerctl";
        };
        clusterDefaults = {
          vpsadmin = ./config/vpsadmin-devcluster.json;
          vpsadminos = ./config/vpsadminos-devcluster.json;
        };
      };
      package = vpsfree-dev-workspace.lib.mkPackage {
        inherit pkgs siteConfig teamConfig;
      };
    in
    {
      packages.${system} = {
        default = package;
        vpsfree-dev-workspace = package;
      };
      apps.${system}.workspace-host = {
        type = "app";
        program = "${package}/bin/workspace-host";
      };
      checks.${system} = {
        deployment-contract =
          pkgs.runCommand "dev-workspace-deployment-contract-tests"
            {
              nativeBuildInputs = [ pkgs.ruby ];
            }
            ''
              cp -R ${self} source
              chmod -R u+w source
              patchShebangs source/bin
              ruby source/test/deployment_contract_test.rb
              touch "$out"
            '';
        agent-instructions =
          pkgs.runCommand "workspace-agent-instructions-tests"
            {
              nativeBuildInputs = [ pkgs.ruby ];
            }
            ''
              ruby ${self}/test/agent_instructions_test.rb
              touch "$out"
            '';
        agent-team-policy = pkgs.runCommand "workspace-agent-team-policy-tests" {
          nativeBuildInputs = [ pkgs.jq ];
        } ''
          catalog=${package}/share/dev-workspace/agent-teams.json
          metadata=${package}/share/dev-workspace/package.json
          test -f "$catalog"
          ${pkgs.jq}/bin/jq -e '
            .schema_version == 4 and
            .default_team == "lead_reviewed" and
            .default_development_team == "lead_reviewed" and
            .capacity.required_native_child_threads == 4 and
            .work_policy.design.default == "xhigh" and
            .work_policy.design.simple == "high" and
            .work_policy.design.allowed == ["high", "xhigh"] and
            .work_policy.design.simple_requires_reason == true and
            .work_policy.design.followup == "retain" and
            .work_policy.implementation.default == "xhigh" and
            .work_policy.implementation.simple == "high" and
            .work_policy.implementation.allowed == ["high", "xhigh"] and
            .work_policy.implementation.simple_requires_reason == true and
            .work_policy.implementation.followup == "retain" and
            .teams.solo.max_open_agents == 0 and
            .teams.solo.design_owner == "team_lead" and
            (.teams.solo.roles | keys) == ["team_lead"] and
            .teams.solo.roles.team_lead.access == "workspace_write" and
            .teams.solo.roles.team_lead.effort == "high" and
            .teams.solo.roles.team_lead.allowed_efforts == ["high", "xhigh"] and
            .teams.solo.roles.team_lead.model == "gpt-6.1-sol" and
            .teams.solo.roles.team_lead.purpose == "lead" and
            (.teams.solo.roles.team_lead.instructions | contains("Investigate, design and edit application code yourself without automatic specialists")) and
            (.teams.solo.roles.team_lead.instructions | contains("At the end of every turn")) and
            .teams.delegated.max_open_agents == 3 and
            .teams.delegated.design_owner == "designer" and
            (.teams.delegated.roles | keys | sort) == (["designer", "implementer", "reviewer", "team_lead"] | sort) and
            .teams.delegated.roles.team_lead.access == "workspace_write" and
            .teams.delegated.roles.team_lead.allowed_efforts == ["high", "xhigh"] and
            .teams.delegated.roles.team_lead.model == "gpt-6.1-sol" and
            .teams.delegated.roles.team_lead.effort == "high" and
            (.teams.delegated.roles.team_lead.instructions | contains("At the end of every turn")) and
            (.teams.delegated.roles.team_lead.instructions | contains("do not take over delegated application edits")) and
            (.teams.delegated.roles.team_lead.instructions | contains("complete base-to-head commit series")) and
            .teams.delegated.roles.designer.model == "gpt-6-astra" and
            .teams.delegated.roles.designer.purpose == "design" and
            .teams.delegated.roles.designer.access == "workspace_write" and
            .teams.delegated.roles.designer.effort == "xhigh" and
            .teams.delegated.roles.designer.allowed_efforts == ["high", "xhigh"] and
            .teams.delegated.roles.designer.lifetime == "session" and
            (.teams.delegated.roles.designer.instructions | contains("work/<slug>/design.md")) and
            (.teams.delegated.roles.designer.instructions | contains("application implementation belongs to implementers")) and
            .teams.delegated.roles.implementer.model == "gpt-6.1-sol" and
            .teams.delegated.roles.implementer.access == "workspace_write" and
            .teams.delegated.roles.implementer.effort == "xhigh" and
            .teams.delegated.roles.implementer.allowed_efforts == ["high", "xhigh"] and
            .teams.delegated.roles.implementer.lifetime == "session" and
            (.teams.delegated.roles.implementer.instructions | contains("Refer consequential design deviations through the lead")) and
            .teams.delegated.roles.reviewer.model == "gpt-6.1-sol" and
            .teams.delegated.roles.reviewer.access == "read_only" and
            .teams.delegated.roles.reviewer.effort == "xhigh" and
            .teams.delegated.roles.reviewer.allowed_efforts == ["xhigh"] and
            .teams.delegated.roles.reviewer.lifetime == "session" and
            .teams.delegated.roles.reviewer.fresh_context == true and
            (.teams.delegated.roles.reviewer.instructions | contains("complete base-to-head history")) and
            (.teams.delegated.roles.reviewer.instructions | contains("Earlier review is allowed only on an explicit user request")) and
            (.teams.delegated.roles.reviewer.instructions | contains("after all intended changes are committed and quick checks pass")) and
            .teams.lead_designed.roles.team_lead.model == "gpt-6.1-sol" and
            .teams.lead_designed.roles.team_lead.effort == "xhigh" and
            .teams.lead_designed.design_owner == "team_lead" and
            .teams.lead_designed.max_open_agents == 2 and
            (.teams.lead_designed.roles | keys | sort) == (["implementer", "reviewer", "team_lead"] | sort) and
            .teams.lead_designed.roles.team_lead.access == "workspace_write" and
            .teams.lead_designed.roles.team_lead.allowed_efforts == ["high", "xhigh"] and
            (.teams.lead_designed.roles.team_lead.instructions | contains("Own substantive technical design and write work/<slug>/design.md")) and
            .teams.lead_designed.roles.implementer.model == "gpt-6.1-sol" and
            .teams.lead_designed.roles.reviewer.model == "gpt-6.1-sol" and
            .teams.lead_reviewed.mode == "development" and
            .teams.lead_reviewed.design_owner == "team_lead" and
            .teams.lead_reviewed.max_open_agents == 1 and
            (.teams.lead_reviewed.roles | keys) == ["reviewer", "team_lead"] and
            .teams.lead_reviewed.roles.team_lead.model == "gpt-6.1-sol" and
            .teams.lead_reviewed.roles.team_lead.effort == "xhigh" and
            .teams.lead_reviewed.roles.team_lead.allowed_efforts == ["high", "xhigh"] and
            .teams.lead_reviewed.roles.team_lead.access == "workspace_write" and
            (.teams.lead_reviewed.roles.team_lead.instructions | contains("Investigate, design and edit application code yourself")) and
            (.teams.lead_reviewed.roles.team_lead.instructions | contains("ready retained review-purpose member")) and
            .teams.lead_reviewed.roles.reviewer.model == "gpt-6-astra" and
            .teams.lead_reviewed.roles.reviewer.effort == "xhigh" and
            .teams.lead_reviewed.roles.reviewer.allowed_efforts == ["xhigh"] and
            .teams.lead_reviewed.roles.reviewer.access == "read_only" and
            .teams.lead_reviewed.roles.reviewer.purpose == "review" and
            .teams.lead_reviewed.roles.reviewer.fresh_context == true and
            .teams.lead_reviewed.roles.reviewer.lifetime == "session" and
            ([.teams[].roles.team_lead.instructions] | unique | length) == 4 and
            ([.teams[].roles.team_lead.instructions] | all(
              contains("all intended changes are committed, and quick checks pass, before long integration tests") and
              contains("Completed substantive documentation and configuration deliverables are included") and
              contains("Routine planning, investigation, findings, session tracking and evidence alone never trigger automatic review") and
              contains("Earlier review requires an explicit user request, is advisory, and does not replace final review") and
              contains("Adding, replacing or reconfiguring team members requires explicit user direction")
            )) and
            ([.teams.delegated, .teams.lead_designed] | all(
              .roles.implementer.instructions | contains("architect-owned or lead-owned design and verification brief for substantive work")
            )) and
            .utilities.verification_watcher.model == "gpt-6-luna" and
            .utilities.verification_watcher.effort == "low" and
            .utilities.verification_watcher.behavior == "verification_watcher" and
            .utilities.verification_watcher.lifetime == "operation" and
            .utilities.verification_watcher.required_for == [
              "long_check", "uncertain_check", "workflow_wait", "ci_wait", "deployment_wait"
            ] and
            ([.teams[].roles | keys[]] | index("verification_watcher") | not) and
            ([.teams[].roles[].model] | all(. == "gpt-6.1-sol" or . == "gpt-6-astra")) and
            ([.. | strings] | all(contains("gpt-5.6-") | not))
          ' "$catalog" >/dev/null
          ${pkgs.jq}/bin/jq -e '
            .agent_teams.managed == true and
            .agent_teams.catalog.schema_version == 4 and
            .agent_teams.native_capacity.config_key == "agents.max_concurrent_threads_per_session" and
            .agent_teams.native_capacity.required_value == 4
          ' "$metadata" >/dev/null
          ${pkgs.jq}/bin/jq -r '.agent_teams.native_role_configs[].path' "$metadata" |
            while IFS= read -r path; do
              config=${package}/$path
              test -f "$config"
              if grep -Eq "^(model|model_reasoning_effort|sandbox_mode) =" "$config"; then
                echo "native role configuration overrides runtime settings" >&2
                exit 1
              fi
            done
          touch "$out"
        '';
        cluster-provider-composition = pkgs.runCommand
          "workspace-cluster-provider-composition-tests"
          {
            nativeBuildInputs = [ pkgs.jq ];
          }
          ''
            workspace=${self}/.dev-workspace.json
            catalog=${package}/share/dev-workspace/extensions.json
            expected=$(${pkgs.jq}/bin/jq -c \
              '.developmentClusterProviders | sort' "$workspace")
            actual=$(${pkgs.jq}/bin/jq -c \
              '[.clusterProviders[].id] | sort' "$catalog")
            test "$expected" = "$actual"
            for provider in $(${pkgs.jq}/bin/jq -r \
              '.developmentClusterProviders[]' "$workspace"); do
              command=$(${pkgs.jq}/bin/jq -er \
                --arg provider "$provider" \
                '.clusterProviders[] | select(.id == $provider) | .command' \
                "$catalog")
              test -x "$command"
              test -x ${package}/libexec/workspace-portal/"$provider"-devcluster
            done
            touch "$out"
          '';
      };
    };
}
