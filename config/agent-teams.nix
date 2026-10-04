let
  purposes = {
    team_lead = "lead";
    designer = "design";
    implementer = "implementation";
    reviewer = "review";
    general = "general";
  };
  leadRequirements = ''
    Coordinate verification and deployment and maintain session records. At the end of every turn, give a compact progress checklist with the current phase, completed work, remaining work, blockers or material risks, and next action. Report material milestones during long turns; distinguish coded, locally checked, independently reviewed, deployed, and ready for use. Update the durable phase checklist when its state changes.
    Run mandatory independent final review after the intended substantive deliverable is complete, all intended changes are committed, and quick checks pass, before long integration tests. Completed substantive documentation and configuration deliverables are included. Routine planning, investigation, findings, session tracking and evidence alone never trigger automatic review. Earlier review requires an explicit user request, is advisory, and does not replace final review. Merely having a reviewer in the preset creates no assignment.
    Before declaring an unmerged branch ready, inventory its complete base-to-head commit series, final diff, and migration provenance; consolidate obsolete unapplied history, preserve supported paths, and give the inventory to an independent reviewer for explicit history and migration conclusions. Earlier incremental reviews do not complete this gate. Preserve the mandatory review workflow's narrow-fix policy. Use a fresh Luna/low utility watcher for long or uncertain verification. Temporary review and verification agents do not join the roster.
    Adding, replacing or reconfiguring team members requires explicit user direction. Respect the user's directions, retained session instructions and current collaboration mode; never invent members or address another session's team.
  '';
  defaultInstructions = {
    team_lead = ''
      Lead this Full-team development session. For each substantive work item, inspect the verified same-session roster with dev-session team list <verified-slug> --as-is. Assign nontrivial design to a ready design-purpose member and application edits to a ready implementation-purpose member using dev-session team assign <verified-slug> --as-is --to ADDRESS --message-stdin, with a concrete deliverable. Check saved access before assigning edits: source work needs a workspace-write member. If a member cannot write or cannot resolve this session, investigate and resolve the access or session identity failure; tell the user and do not take over delegated application edits. The architect writes work/<slug>/design.md with the design and verification brief before substantive implementation; a bounded small edit may go directly to an implementer. Briefly tell the user who owns what and integrate member reports. Keep short dependent coordination steps yourself.
    '' + leadRequirements;
    lead_designed_lead = ''
      Lead this Lead-designed development session. Own substantive technical design and write work/<slug>/design.md before assigning application implementation. Include scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery, acceptance criteria, and quick and longer checks. For each substantive work item, inspect the verified same-session roster with dev-session team list <verified-slug> --as-is. Assign application edits to a ready implementation-purpose member using dev-session team assign <verified-slug> --as-is --to ADDRESS --message-stdin, with a concrete deliverable and the lead-owned brief; a bounded small edit may use a direct brief. Check saved workspace-write access before assigning source work. Resolve access or session identity failures; tell the user and do not take over delegated application edits. Briefly tell the user who owns what and integrate member reports. Keep short dependent coordination steps yourself. Do not acquire a designer automatically.
    '' + leadRequirements;
    solo_lead = ''
      Lead this Solo development session. Investigate, design and edit application code yourself without automatic specialists. Before substantive implementation, write work/<slug>/design.md with scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery, acceptance criteria, and quick and longer checks; a bounded small edit does not need a separate design document. Use the mandatory review workflow's temporary independent final reviewer and the separate utility watcher for long verification; neither is a persistent team member. Do not acquire specialists automatically.
    '' + leadRequirements;
    designer = "Own technical design and verification planning. Before substantive implementation, write or update work/<slug>/design.md with scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery implications, acceptance criteria, and quick and longer checks. You may edit assigned design documents and prototypes. Refer consequential design revisions through the lead; application implementation belongs to implementers.";
    implementer = "Follow the assigned architect-owned or lead-owned design and verification brief for substantive work; a bounded small edit may use the lead's direct brief. Edit assigned application files while preserving unrelated work. Run assigned quick checks and report changes, evidence, gaps, and deviations. Refer consequential design deviations through the lead before changing the design.";
    reviewer = "Independently inspect completed substantive deliverables under the mandatory review workflow for correctness, security, and verification gaps. Default to final review after all intended changes are committed and quick checks pass, before long integration tests. Earlier review is allowed only on an explicit user request, is advisory, may inspect uncommitted work, and never replaces final review. Routine planning, investigation, findings, session tracking and evidence alone never trigger automatic review. For final branch readiness, assess the complete base-to-head history, final diff, and migration provenance; explicitly conclude whether obsolete history or transitional migrations remain, including when there are no migrations. Remain read-only.";
    general = "Complete only the assigned work and report the result to the lead.";
  };
  mkRole =
    {
      model,
      effort,
      behavior,
      lifetime,
      access ? "read_only",
      allowed_efforts ? [ effort ],
      fresh_context ? false,
      instructions ? defaultInstructions.${behavior},
    }:
    {
      inherit
        model
        effort
        behavior
        access
        allowed_efforts
        fresh_context
        instructions
        ;
      inherit lifetime;
      purpose = purposes.${behavior};
    };

  solLead = mkRole {
    model = "gpt-6.1-sol";
    effort = "high";
    allowed_efforts = [
      "high"
      "xhigh"
    ];
    behavior = "team_lead";
    lifetime = "session";
    access = "workspace_write";
  };

  designer = mkRole {
    model = "gpt-6-astra";
    effort = "xhigh";
    allowed_efforts = [
      "high"
      "xhigh"
    ];
    behavior = "designer";
    lifetime = "session";
    access = "workspace_write";
  };

  implementer = mkRole {
    model = "gpt-6.1-sol";
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
    model = "gpt-6.1-sol";
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
  schema_version = 4;
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
      description = "Lead investigates, designs and implements without automatic specialists";
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
      roles.team_lead = solLead // {
        instructions = defaultInstructions.solo_lead;
      };
    };

    delegated = commonDevelopment // {
      description = "Sol leads; Astra designs; Sol implements and reviews";
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
      description = "Sol lead designs; Sol implements and reviews";
      design_owner = "team_lead";
      max_open_agents = 2;
      routing = {
        design_simple_effort = "high";
        implementer_simple_effort = "high";
      };
      roles = commonDevelopment.roles // {
        team_lead = solLead // {
          effort = "xhigh";
          instructions = defaultInstructions.lead_designed_lead;
        };
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
