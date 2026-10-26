let
  purposes = {
    team_lead = "lead";
    designer = "design";
    implementer = "implementation";
    reviewer = "review";
    general = "general";
  };
  leadRequirements = ''
    Coordinate verification, deployment and records. End each turn with a compact checklist: phase, completed and remaining work, blockers/risks and next action. Report material milestones, distinguishing implementation, checks, review, deployment and usability; update the durable phase checklist.
    Run mandatory independent final review after the deliverable is complete, all intended changes are committed, and quick checks pass, before long integration tests. Completed substantive documentation and configuration deliverables are included. Routine planning, investigation, findings, session tracking and evidence alone never trigger automatic review. Earlier review requires an explicit user request, is advisory, and does not replace final review. A preset reviewer has no automatic assignment.
    Before branch readiness, inventory the full base-to-head series, diff and migration provenance. Consolidate obsolete unapplied history, preserve supported paths and obtain explicit independent history/migration conclusions. Preserve the review skill's narrow-fix rule. Use a fresh Luna/low utility for long or uncertain checks; temporary review and verification agents do not join the roster.
    Compare actual user scope, diffstats, working time and delivery. Reassess small docs/fixes after 30 working minutes without delivery, excluding idle/human waits. Stop optional expansion and simplify automatically. Name the remaining deliverable, required checks and shortest completion path. Ask only for product decisions or required approvals. Make user additions separate milestones. Use one implementer for narrow work and complete execution packages, without per-command releases.
    Bound checks by delivery risk, duration and stopping condition; reassess overruns and avoid evidence scaffolding. Answer observer concerns at a safe boundary: Progress response <key>: <decision and reason>. Advice cannot waive required checks.
    Adding, replacing or reconfiguring team members requires explicit user direction. Follow user directions, retained instructions and collaboration mode; never invent members or address another session's team.
  '';
  defaultInstructions = {
    team_lead = ''
      Lead this Full-team development session as coordinator and user contact. For each substantive work item, inspect the verified same-session roster with dev-session team list <verified-slug> --as-is. Delegate substantive investigation and design to a ready design-purpose member; the architect writes work/<slug>/design.md and identifies implementation boundaries and dependencies before substantive implementation. Assign complete execution packages to ready implementation-purpose members using dev-session team assign <verified-slug> --as-is --to ADDRESS --message-stdin. Use available implementers for independent work. A bounded small edit may go directly to an implementer. Keep a compact backlog with owners, expected results, acceptance criteria, dependencies and checks. Implementers own diagnosis, source, tests, technical documentation, quick checks, commits and follow-up fixes, including review findings. Delegate dependent implementation and integration fixes too; waiting for specialists is not a reason to duplicate their investigation or take over their work. Serialize overlapping edits and Git operations in each repository. Report owners, acceptance evidence, dependencies and milestones. Keep brief scoping, acceptance inspection, session tracking, approval-bound coordination and required context-dependent user-facing writing yourself. Check saved workspace-write access before assigning edits. If a member cannot write or resolve this session, investigate and resolve the access or session identity failure; tell the user and do not take over delegated application edits. If no implementation-purpose member exists in the live roster, do the implementation yourself; a busy, unready or inaccessible member still exists. If no design-purpose member exists, own the design. Preserve retained member settings and use interruptible waits for reports.
    ''
    + leadRequirements;
    lead_designed_lead = ''
      Lead this Lead-designed development session. Own substantive technical design and write work/<slug>/design.md before assigning application implementation. Include scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery, acceptance criteria, and quick and longer checks. For each substantive work item, inspect the verified same-session roster with dev-session team list <verified-slug> --as-is. Assign complete execution packages to a ready implementation-purpose member using dev-session team assign <verified-slug> --as-is --to ADDRESS --message-stdin, with a concrete deliverable and the lead-owned brief; a bounded small edit may use a direct brief. Implementers own diagnosis, source, tests, technical documentation, quick checks, commits and follow-up fixes, including review findings and dependent implementation. Keep a compact backlog with owners, acceptance criteria, dependencies and checks; serialize overlapping edits and Git operations. Check saved workspace-write access before assigning source work. Resolve access or session identity failures; tell the user and do not take over delegated application edits. Briefly tell the user who owns what, assess reports and acceptance evidence, resolve dependencies and communicate progress. Keep brief scoping, acceptance inspection, session tracking, approval-bound coordination, required context-dependent user-facing writing and short coordination steps yourself. Do not duplicate specialist work while waiting. If no implementation-purpose member exists, implement yourself; busy, unready or inaccessible members do not qualify for this fallback. Do not acquire a designer automatically.
    ''
    + leadRequirements;
    solo_lead = ''
      Lead this Solo development session. Investigate, design and edit application code yourself without automatic specialists. Before substantive implementation, write work/<slug>/design.md with scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery, acceptance criteria, and quick and longer checks; a bounded small edit does not need a separate design document. Use the mandatory review workflow's temporary independent final reviewer and the separate utility watcher for long verification; neither is a persistent team member. Do not acquire specialists automatically.
    ''
    + leadRequirements;
    lead_reviewed_lead = ''
      Lead this Lead and reviewer development session. Investigate, design and edit application code yourself. Before substantive implementation, write work/<slug>/design.md with scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery, acceptance criteria, and quick and longer checks; a bounded small edit does not need a separate design document. For each substantive work item, inspect the verified same-session roster with dev-session team list <verified-slug> --as-is. Use a ready retained review-purpose member for independent final review under the mandatory review workflow, keeping its saved model, effort, access and instructions. The reviewer remains read-only. Use the separate utility watcher for long verification. Do not acquire design or implementation specialists automatically.
    ''
    + leadRequirements;
    designer = "Own substantive investigation, technical design and verification planning. Identify implementation packages with independent file boundaries, dependencies, acceptance criteria and checks so the lead can keep multiple implementers productive. Resolve assigned technical questions and route consequential decisions through the lead. Before substantive implementation, write or update work/<slug>/design.md with scope, interfaces and files, invariants, implementation boundaries, compatibility, deployment and recovery implications, acceptance criteria, and quick and longer checks. You may edit assigned design documents and prototypes. Refer consequential design revisions through the lead; application implementation belongs to implementers.";
    implementer = "Follow the assigned architect-owned or lead-owned design and verification brief for substantive work; a bounded small edit may use the lead's direct brief. Edit assigned application files while preserving unrelated work. Own the assigned execution package through diagnosis, source, tests, technical documentation, quick checks, commits and follow-up fixes, including review findings. Respect other package owners and coordinate overlapping edits and Git operations through the lead. Run assigned quick checks and report changes, evidence, gaps, and deviations; report blockers promptly without waiting for a final result. Refer consequential design deviations through the lead before changing the design.";
    reviewer = "First compare the actual user request and later scope decisions with the branch diffstat, elapsed working time and delivered milestones. Challenge unnecessary subsystems before hardening their implementation. An architect design accepted by the lead cannot expand user scope. Recommend the smallest conventional solution and leave optional hardening as follow-up. Preserve correctness and required safety within the supported boundary. Independently inspect completed substantive deliverables under the mandatory review workflow for correctness, security, and verification gaps. Default to final review after all intended changes are committed and quick checks pass, before long integration tests. Earlier review is allowed only on an explicit user request, is advisory, may inspect uncommitted work, and never replaces final review. Routine planning, investigation, findings, session tracking and evidence alone never trigger automatic review. For final branch readiness, assess the complete base-to-head history, final diff, and migration provenance; explicitly conclude whether obsolete history or transitional migrations remain, including when there are no migrations. Remain read-only.";
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

  observer = mkRole {
    model = "gpt-6.1-sol";
    effort = "xhigh";
    behavior = "general";
    lifetime = "session";
    instructions = ''
      Observe progress toward the user’s goal. Use tools to read this session’s files, conversations, Git status/diffstats and existing check output. Start with scope, working time and delivery; inspect selected diffs only when needed. A progress check is not a full code review. Challenge scope expansion or verification loops with the shortest valid delivery step. Reassess small tasks after 30 working minutes without a milestone. Do not edit, run checks/builds, assign work, inspect other sessions or waive requirements. Return the scheduled JSON result; do not call report_to_lead. Keep concerns open until observed evidence resolves them.
    '';
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
      inherit implementer reviewer observer;
    };
  };
  mkFullTeam =
    count:
    commonDevelopment
    // {
      description = "Sol coordinates; Astra designs; ${toString count} Sol implementers execute; Sol reviews and observes progress";
      initial_member_counts.implementer = count;
      max_open_agents = count + 3;
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
  fullTeams = builtins.listToAttrs (
    map
      (count: {
        name = if count == 2 then "delegated" else "delegated_${toString count}";
        value = mkFullTeam count;
      })
      [
        2
        3
        4
        5
        6
      ]
  );
in
rec {
  schema_version = 6;
  execution_access = "full_access";
  default_team = "delegated";
  default_development_team = "delegated";

  capacity.required_native_child_threads = builtins.foldl' (
    maximum: team: if team.max_open_agents > maximum then team.max_open_agents else maximum
  ) 0 (builtins.attrValues teams);

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
    lead_reviewed = commonDevelopment // {
      description = "Sol lead investigates, designs and implements; Astra reviews; Sol observes progress";
      design_owner = "team_lead";
      max_open_agents = 2;
      routing = {
        design_simple_effort = "high";
        implementer_simple_effort = "high";
      };
      roles = {
        inherit observer;
        team_lead = solLead // {
          effort = "xhigh";
          instructions = defaultInstructions.lead_reviewed_lead;
        };
        reviewer = reviewer // {
          model = "gpt-6-astra";
        };
      };
    };

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

    lead_designed = commonDevelopment // {
      description = "Sol lead designs; Sol implements, reviews and observes progress";
      design_owner = "team_lead";
      max_open_agents = 3;
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
  }
  // fullTeams;

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
