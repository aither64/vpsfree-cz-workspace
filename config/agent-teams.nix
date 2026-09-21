let
  mkRole =
    {
      model,
      effort,
      behavior,
      lifetime,
      access ? "read_only",
      allowed_efforts ? [ effort ],
      fresh_context ? false,
    }:
    {
      inherit
        model
        effort
        behavior
        access
        allowed_efforts
        fresh_context
        ;
      inherit lifetime;
    };

  solLead = mkRole {
    model = "gpt-6-sol";
    effort = "high";
    allowed_efforts = [
      "high"
      "xhigh"
    ];
    behavior = "team_lead";
    lifetime = "session";
    access = "workspace_write";
  };

  solDesignLead = solLead // {
    model = "gpt-6-sol";
    effort = "xhigh";
  };

  designer = mkRole {
    model = "gpt-6-sol";
    effort = "xhigh";
    allowed_efforts = [
      "high"
      "xhigh"
    ];
    behavior = "designer";
    lifetime = "session";
  };

  implementer = mkRole {
    model = "gpt-6-sol";
    effort = "xhigh";
    allowed_efforts = [
      "high"
      "xhigh"
    ];
    behavior = "implementer";
    lifetime = "session";
    access = "workspace_write";
  };

  reviewer = mkRole {
    model = "gpt-6-sol";
    effort = "xhigh";
    behavior = "reviewer";
    lifetime = "session";
    fresh_context = true;
  };

  commonDevelopment = {
    mode = "development";
    service_policy = "non_priority";
    max_open_agents = 3;
    lifecycle = {
      startup = "on_demand";
      communication = "lead_mediated";
      reviewer_reuse = "same_change";
    };
    roles = {
      inherit implementer reviewer;
    };
  };
in
{
  schema_version = 3;
  default_team = "delegated";
  default_development_team = "delegated";

  capacity.required_native_child_threads = 4;

  work_policy = {
    design = {
      default = "xhigh";
      simple = "high";
      allowed = [
        "high"
        "xhigh"
      ];
      simple_requires_reason = true;
      followup = "retain";
    };
    implementation = {
      default = "xhigh";
      simple = "high";
      allowed = [
        "high"
        "xhigh"
      ];
      simple_requires_reason = true;
      followup = "retain";
    };
  };

  teams = {
    solo = {
      description = "Investigate and discuss without automatic specialists";
      mode = "solo";
      design_owner = "team_lead";
      service_policy = "non_priority";
      max_open_agents = 0;
      lifecycle = {
        startup = "on_demand";
        communication = "lead_mediated";
        reviewer_reuse = "same_change";
      };
      routing = { };
      roles.team_lead = solLead;
    };

    delegated = commonDevelopment // {
      description = "Sol coordinates, designs, and independently reviews";
      design_owner = "designer";
      routing = {
        design_simple_effort = "high";
        implementer_simple_effort = "high";
      };
      roles = commonDevelopment.roles // {
        team_lead = solLead;
        inherit designer;
      };
    };

    lead_designed = commonDevelopment // {
      description = "Sol coordinates, owns design, and implements";
      design_owner = "team_lead";
      routing = {
        design_simple_effort = "high";
        implementer_simple_effort = "high";
      };
      roles = commonDevelopment.roles // {
        team_lead = solDesignLead;
      };
    };
  };

  utilities.verification_watcher = {
    model = "gpt-6-luna";
    effort = "low";
    behavior = "verification_watcher";
    access = "workspace_write";
    lifetime = "operation";
    startup = "on_demand";
    max_concurrent = 1;
    required_for = [
      "long_check"
      "uncertain_check"
      "workflow_wait"
      "ci_wait"
      "deployment_wait"
    ];
  };
}
