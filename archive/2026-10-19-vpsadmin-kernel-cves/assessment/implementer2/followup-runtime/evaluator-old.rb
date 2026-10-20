require 'time'
require 'digest'
require 'json'
require 'rubygems/version'

module SecurityAdvisories
  class Evaluator
    MAX_EVIDENCE_AGE = 15 * 60
    MAX_FUTURE_SKEW = 5 * 60
    MAX_HISTORY_HANDOFF_GAP = 30 * 60
    KERNEL_EVENT_TYPES = %w[boot reported_release_change livepatch_change].freeze
    LIVEPATCH_IDENTITY_FIELDS = %w[
      kernel_version patch_version applied_at verified_at patches
    ].freeze
    ATTESTED_EVENT_FIELDS = %w[
      id event_type booted_at booted_release reported_release effective_at
      livepatch_action observed_after observed_before source source_status_id
      confidence
    ].freeze

    def self.event_digest(event)
      value = ATTESTED_EVENT_FIELDS.to_h { |key| [key, event[key]] }
      Digest::SHA256.hexdigest(JSON.generate(canonical_value(value)))
    end

    def self.canonical_value(value)
      case value
      when Hash
        value.keys.sort.to_h { |key| [key, canonical_value(value[key])] }
      when Array
        value.map { |item| canonical_value(item) }
      else
        value
      end
    end

    def initialize(advisory, now: Time.now, evidence_time: now, kernel_configurations: {})
      @advisory = advisory
      @now = now
      @evidence_time = evidence_time
      @kernel_configurations = kernel_configurations
    end

    def evaluate(nodes)
      results = nodes.map { |node| evaluate_node(node) }
      node_ids = results.map { |node| node.fetch('node_id') }
      missing_note_nodes = @advisory.node_notes.keys.map(&:to_i) - node_ids
      unless missing_note_nodes.empty?
        raise Error,
              "dossier has notes for Nodes outside the active evaluation set: #{missing_note_nodes.sort.join(', ')}"
      end
      results.each do |result|
        notes = @advisory.node_notes[result.fetch('node_id').to_s]
        result['notes'] = notes.dup if notes
      end
      states = results.group_by { |node| node.fetch('state') }
                      .transform_values(&:length)

      {
        'schema_version' => 4,
        'cve' => @advisory.cve,
        'dossier_digest' => @advisory.digest,
        'evaluated_at' => @now.utc.iso8601,
        'completeness' => {
          'expected_node_count' => nodes.length,
          'evaluated_node_count' => results.length,
          'node_set_complete' => results.length == nodes.length && node_ids.uniq.length == node_ids.length,
          'resolution_complete' => results.all? do |node|
            %w[mitigated not_affected].include?(node['state'])
          end,
          'states' => states,
          'blocking_node_ids' => results.filter_map do |node|
            node['node_id'] unless %w[mitigated not_affected].include?(node['state'])
          end
        },
        'nodes' => results
      }
    end

    protected

    def evaluate_node(node)
      base = {
        'node_id' => node['node_id'],
        'node_name' => node['node_name'],
        'node_role' => node['node_role'],
        'evidence_revision' => node['evidence_revision']
      }

      unless Array(@advisory.platform['affected_node_roles']).include?(node['node_role'])
        return base.merge(unreachable(
                            node.dig('kernel', 'reported_release'),
                            "node role #{node['node_role']} does not host the vulnerable VPS interface"
                          ))
      end

      problems = evidence_problems(node) + coverage_problems(node) + attestation_problems(node)
      return base.merge(unknown(problems.join('; '))) unless problems.empty?

      timeline = build_timeline(node)
      return base.merge(unknown('kernel history has no baseline for the required period')) if timeline.empty?

      livepatch_state = {}
      assessments = timeline.map do |point|
        point.merge(
          'assessment' => assess_snapshot(
            point.fetch('security_evidence'),
            event_type: point.fetch('event_type'),
            livepatch_state:
          )
        )
      end
      unresolved = assessments.select { |point| point.dig('assessment', 'state') == 'unknown' }
      unless unresolved.empty?
        reasons = unresolved.map { |point| point.dig('assessment', 'reason') }.uniq
        return base.merge(unknown(reasons.join('; ')))
      end

      current = assessments.last
      current_assessment = current.fetch('assessment')
      current_release = current.dig('security_evidence', 'kernel', 'reported_release')
      common = {
        'kernel_release' => current_release,
        'config_digest' => current.dig('security_evidence', 'kernel', 'config_digest')
      }

      if current_assessment['state'] == 'affected'
        return base.merge(vulnerable(current_release, current_assessment['reason'])).merge(common)
      end

      affected = assessments.select { |point| point.dig('assessment', 'state') == 'affected' }
      if affected.empty?
        reason = current_assessment['reason'] || exact_build_reason(current_assessment)
        return base.merge(not_affected(current_release, reason)).merge(common)
      end

      last_affected_index = assessments.rindex do |point|
        point.dig('assessment', 'state') == 'affected'
      end
      transition = assessments[(last_affected_index + 1)..]&.find do |point|
        point.dig('assessment', 'state') != 'affected'
      end
      return base.merge(unknown('mitigation transition is absent from retained history')) unless transition

      base.merge(mitigated(transition, current_release, current_assessment)).merge(common)
    end

    def evidence_problems(node)
      ret = []
      observed = parse_time(node['observed_at'])
      received = parse_time(node['received_at'])
      ret << 'security evidence observation time is invalid' unless observed
      ret << 'security evidence receipt time is invalid' unless received
      if received && received < @evidence_time - MAX_EVIDENCE_AGE
        ret << 'security evidence was older than 15 minutes when collected'
      end
      if observed && received && observed > received + MAX_FUTURE_SKEW
        ret << 'security evidence observation is more than 5 minutes in the future'
      end

      ret.uniq
    end

    def coverage_problems(node)
      coverage = node.dig('kernel', 'history_coverage')
      return ['kernel history coverage is missing'] unless coverage.is_a?(Hash)

      required_since = history_required_since(node)
      started_at = parse_time(coverage['started_at'])
      observed_through = parse_time(coverage['observed_through'])
      ret = []
      ret << 'kernel history coverage start is invalid' unless started_at
      ret << 'kernel history coverage end is invalid' unless observed_through
      if required_since && started_at && started_at > required_since
        ret << "kernel history starts after required time #{required_since.utc.iso8601}"
      end
      if observed_through && observed_through < @evidence_time - MAX_EVIDENCE_AGE
        ret << 'kernel history did not cover the evidence collection window'
      end

      exact_started_at = parse_time(coverage['exact_events_started_at'])
      needs_reconstruction = required_since && (!exact_started_at || required_since < exact_started_at)
      if needs_reconstruction
        reconstruction = coverage['reconstruction']
        if reconstruction.is_a?(Hash) && reconstruction['complete'] == true
          reconstructed_from = parse_time(reconstruction['started_at'])
          reconstructed_through = parse_time(reconstruction['observed_through'])
          ret << 'kernel history reconstruction start is invalid' unless reconstructed_from
          ret << 'kernel history reconstruction end is invalid' unless reconstructed_through
          if reconstructed_from && reconstructed_from > required_since
            ret << "kernel history reconstruction starts after required time #{required_since.utc.iso8601}"
          end
          if exact_started_at && reconstructed_through &&
             reconstructed_through < exact_started_at - MAX_HISTORY_HANDOFF_GAP
            ret << 'kernel history reconstruction does not overlap exact event coverage'
          end
        else
          ret << 'kernel history reconstruction is not complete for the required period'
        end
      end

      ret
    end

    def build_timeline(node)
      required_since = history_required_since(node)
      events = Array(node.dig('kernel', 'history')).sort_by do |event|
        [event['observed_before'].to_s, event['id'].to_i]
      end
      points = events.each_with_object([]) do |event, ret|
        point = event_point(node, event)
        ret << inherit_livepatch_metadata(ret.last, point)
      end
      baseline = points.reverse.find do |point|
        observed = parse_time(point['observed_before'])
        observed && observed <= required_since
      end
      return [] unless baseline

      selected = []
      selected << baseline
      points.each do |point|
        observed = parse_time(point['observed_before'])
        selected << point if observed && observed > required_since
      end

      selected << {
        'event_type' => 'current_observation',
        'effective_at' => nil,
        'observed_after' => selected.last&.fetch('observed_before', nil),
        'observed_before' => node['observed_at'],
        'confidence' => 'exact',
        'security_evidence' => current_security_evidence(node)
      }
      selected
    end

    def inherit_livepatch_metadata(previous, current)
      return current unless previous

      internal_event_types = %w[
        ebpf_change module_change sysctl_change deployment_change
        livepatch_inventory_change
      ]
      return current unless internal_event_types.include?(current['event_type'])

      previous_evidence = previous.fetch('security_evidence')
      current_evidence = current.fetch('security_evidence')
      if @advisory.platform.has_key?('affected_livepatches')
        inventories = [previous_evidence['livepatches'], current_evidence['livepatches']]
        return current unless inventories.all? { |patches| patches.is_a?(Array) && patches.all?(Hash) }
      end
      previous_boot_id = previous_evidence.dig('kernel', 'boot_id')
      current_boot_id = current_evidence.dig('kernel', 'boot_id')
      return current unless valid_boot_id?(previous_boot_id) && previous_boot_id == current_boot_id

      previous_by_id = Array(previous_evidence['livepatches']).to_h do |patch|
        [patch['id'], patch]
      end
      livepatches = Array(current_evidence['livepatches']).map do |patch|
        previous_patch = previous_by_id[patch['id']]
        next patch unless previous_patch

        previous_patch.merge(patch) do |key, old, new|
          LIVEPATCH_IDENTITY_FIELDS.include?(key) && new.nil? ? old : new
        end
      end
      unless livepatches.any? { |patch| patch['transition'] == true }
        current_ids = livepatches.map { |patch| patch['id'] }
        livepatches.concat(previous_by_id.values.select do |patch|
          !current_ids.include?(patch['id']) && effective_livepatch_state?(patch)
        end)
      end
      current.merge(
        'security_evidence' => current_evidence.merge('livepatches' => livepatches)
      )
    end

    def effective_livepatch_state?(patch)
      patch['loaded'] == true && patch['enabled'] == true && patch['transition'] == false
    end

    def valid_boot_id?(boot_id)
      boot_id.is_a?(String) && !boot_id.empty?
    end

    def event_point(node, event)
      evidence = exact_event_evidence(node, event)
      unless evidence['kernel'].is_a?(Hash)
        evidence = {
          '_release_only' => true,
          'kernel' => {
            'booted_release' => event['booted_release'],
            'reported_release' => event['reported_release']
          }
        }
      end
      {
        'event_type' => event['event_type'],
        'livepatch_action' => event['livepatch_action'],
        'effective_at' => event['effective_at'],
        'observed_after' => event['observed_after'],
        'observed_before' => event['observed_before'],
        'confidence' => event['confidence'],
        'security_evidence' => evidence
      }
    end

    def exact_event_evidence(node, event)
      evidence = event['security_evidence']
      return evidence if evidence.is_a?(Hash) && evidence['kernel'].is_a?(Hash)

      attestation = @advisory.historical_attestations.find do |candidate|
        candidate['node_id'] == node['node_id'] && candidate['event_id'] == event['id']
      end
      return {} unless attestation
      return {} unless attestation['event_digest'] == self.class.event_digest(event)

      attestation.fetch('security_evidence').merge('_configuration_attested' => true)
    end

    def attestation_problems(node)
      events = Array(node.dig('kernel', 'history')).to_h { |event| [event['id'], event] }
      @advisory.historical_attestations.filter_map do |attestation|
        next unless attestation['node_id'] == node['node_id']

        event = events[attestation['event_id']]
        if event.nil?
          "historical attestation references missing event #{attestation['event_id']}"
        elsif attestation['event_digest'] != self.class.event_digest(event)
          "historical attestation for event #{attestation['event_id']} no longer matches retained history"
        end
      end
    end

    def current_security_evidence(node)
      livepatches = node.dig('runtime_mitigations', 'livepatches')
      {
        'schema_version' => node['report_schema_version'],
        'kernel' => node.fetch('kernel', {}).except('history', 'history_coverage'),
        'livepatches' => if @advisory.platform.has_key?('affected_livepatches')
                           livepatches
                         else
                           Array(livepatches)
                         end,
        'ebpf_programs' => Array(node.dig('runtime_mitigations', 'ebpf_programs')),
        'loaded_modules' => Array(node.dig('runtime_kernel_state', 'loaded_modules')),
        'sysctls' => node.dig('runtime_kernel_state', 'sysctls') || {},
        'deployment' => node['deployment'] || {},
        'software_versions' => Array(node['software_versions']),
        'errors' => Array(node['errors'])
      }
    end

    def assess_snapshot(evidence, event_type:, livepatch_state:)
      kernel = evidence['kernel']
      return unknown_assessment('kernel release evidence is missing') unless kernel.is_a?(Hash)

      livepatch_mitigation = active_livepatch_mitigation(
        evidence,
        kernel,
        event_type:,
        state: livepatch_state
      )

      deployment = evidence['deployment'] || {}
      build = accepted_build(evidence, kernel, deployment)
      if build && !snapshot_evidence_problems(evidence, kernel).empty?
        build = nil
      end
      if build
        build_result = {
          'state' => build.fetch('fix_state'),
          'build' => build,
          'reason' => "accepted exact build #{kernel['kernel_source_revision']} is #{build.fetch('fix_state')}"
        }
      end

      base_result = build_result || version_rule_result(kernel)
      introduction = livepatch_introduction(evidence, kernel)
      return base_result unless introduction || base_result['state'] == 'affected'

      configuration = configuration_result(evidence)
      return configuration if configuration['state'] == 'unreachable'
      if configuration['state'] == 'unknown' && evidence['_release_only'] != true
        return configuration
      end

      mitigation = livepatch_mitigation || active_ebpf_mitigation(evidence)
      if introduction
        if mitigation
          return unknown_assessment(
            'livepatch introduction and protection have no reviewed execution ordering'
          )
        end
        return introduction if introduction['state'] == 'affected' || base_result['state'] != 'affected'

        # An ambiguous introduction cannot make an already affected base safe.
        return base_result
      end
      if mitigation
        return {
          'state' => 'mitigated',
          'reason' => mitigation.fetch('description'),
          'effective_at' => mitigation['effective_at'],
          'timing' => mitigation.fetch('timing')
        }
      end

      base_result
    end

    def livepatch_introduction(evidence, kernel)
      rules = Array(@advisory.platform['affected_livepatches'])
      return nil if rules.empty?

      boot_in_scope = rules.any? do |rule|
        livepatch_release_family?(kernel['booted_release'], rule['kernel_version']) ||
          livepatch_release_family?(kernel['reported_release'], rule['kernel_version'])
      end
      patches = evidence['livepatches']
      if boot_in_scope && (evidence['_release_only'] || !patches.is_a?(Array) ||
                           evidence['schema_version'] != 1 || !valid_boot_id?(kernel['boot_id']) ||
                           kernel['booted_release'].to_s.empty? ||
                           !evidence['errors'].is_a?(Array) || !evidence['errors'].empty?)
        return unknown_assessment('livepatch introduction inventory or boot identity is unavailable')
      end
      if boot_in_scope && patches.any? do |patch|
           !patch.is_a?(Hash) || !patch['id'].is_a?(String) || patch['id'].empty?
         end
        return unknown_assessment('livepatch introduction inventory contains an unidentified module')
      end

      candidates = Array(patches).select do |patch|
        patch.is_a?(Hash) && rules.any? do |rule|
          patch['id'] == rule['id'] &&
            [kernel['booted_release'], kernel['reported_release'], patch['kernel_version']].any? do |release|
              livepatch_release_family?(release, rule['kernel_version'])
            end
        end
      end
      return nil if candidates.empty?

      results = candidates.filter_map do |patch|
        unless %w[loaded enabled transition].all? { |key| [true, false].include?(patch[key]) }
          next unknown_assessment("livepatch introduction #{patch['id']} activation fields are missing")
        end
        if patch['loaded'] == false && patch['enabled'] == true
          next unknown_assessment("livepatch introduction #{patch['id']} activation fields are inconsistent")
        end

        # An explicit absence/disabled state does not run replacement code.
        next if patch['transition'] == false && (patch['loaded'] == false || patch['enabled'] == false)

        unless effective_livepatch_state?(patch)
          next unknown_assessment("livepatch introduction #{patch['id']} activation is incomplete or transitioning")
        end

        matched = matching_livepatch_rule(rules, patch, evidence, kernel)
        unless matched && valid_boot_id?(kernel['boot_id']) && evidence['schema_version'] == 1
          next unknown_assessment("livepatch introduction #{patch['id']} source or boot identity is unverified")
        end

        errors = evidence['errors']
        unless errors.is_a?(Array) && errors.empty?
          next unknown_assessment("livepatch introduction #{patch['id']} has incomplete evidence")
        end

        {
          'state' => 'affected',
          'reason' => "reviewed live patch #{patch['id']} revision #{patch['patch_version']} " \
                      'introduces the vulnerability'
        }
      end
      results.find { |result| result['state'] == 'unknown' } || results.first
    end

    def livepatch_release_family?(release, boot_release)
      release.to_s.match?(/\A#{Regexp.escape(boot_release.to_s)}(?:\.\d+)*\z/)
    end

    def version_rule_result(kernel)
      release = kernel['reported_release'] || kernel['booted_release']
      version = kernel_version(release)
      return unknown_assessment("kernel release #{release || '(missing)'} is not parseable") unless version

      branch = version.segments.first(2).join('.')
      rule = @advisory.version_rules[branch]
      unless rule
        introduced = kernel_version(@advisory.affected_from)
        fixed = kernel_version(@advisory.fixed_from)
        unless introduced && fixed
          return unknown_assessment('the dossier has invalid global affected or fixed versions')
        end

        if version >= fixed
          return {
            'state' => 'fixed',
            'reason' => "kernel #{release} includes the upstream fix available since #{@advisory.fixed_from}"
          }
        end

        if version < introduced
          return {
            'state' => 'unaffected',
            'reason' => "kernel #{release} predates the upstream introduction in #{@advisory.affected_from}"
          }
        end

        return {
          'state' => 'affected',
          'reason' => "kernel #{release} is affected since #{@advisory.affected_from} and has no fixed branch rule"
        }
      end

      affected_from = kernel_version(rule['affected_from'])
      fixed_in = kernel_version(rule['fixed_in'])
      open_ended = rule.has_key?('fixed_in') && rule['fixed_in'].nil?
      unless affected_from && (fixed_in || open_ended)
        return unknown_assessment("version rule for kernel branch #{branch} is invalid")
      end

      if version < affected_from
        {
          'state' => 'unaffected',
          'reason' => "kernel #{release} predates the affected range starting at #{rule['affected_from']}"
        }
      elsif fixed_in && version >= fixed_in
        {
          'state' => 'fixed',
          'reason' => "kernel #{release} includes the upstream stable fix released in #{rule['fixed_in']}"
        }
      else
        {
          'state' => 'affected',
          'reason' => if fixed_in
                        "kernel #{release} is in the affected range before #{rule['fixed_in']}"
                      else
                        "kernel #{release} is in an affected stable backport range without a released fix"
                      end
        }
      end
    end

    def kernel_version(release)
      match = release.to_s.match(/\A(\d+)\.(\d+)\.(\d+(?:\.\d+)*)/)
      Gem::Version.new(match.captures.join('.')) if match
    rescue ArgumentError
      nil
    end

    def history_required_since(node)
      default = parse_time(@advisory.platform.fetch('history_required_since'))
      override = @advisory.platform.fetch('history_start_overrides', {})[node['node_id'].to_s]
      return default unless override

      parse_time(override.fetch('required_since')) || default
    end

    def accepted_build(evidence, kernel, deployment)
      vpsadminos = software_version(evidence, 'booted', 'vpsadminos')
      Array(@advisory.platform['accepted_kernel_builds']).find do |build|
        %w[
          reported_release booted_release kernel_source_revision
          config_digest
        ].all? { |key| build[key].to_s == kernel[key].to_s } &&
          build['vpsadminos_revision'].to_s == vpsadminos&.[]('revision').to_s &&
          build['deployment_digest'] == digest(deployment) &&
          build['software_digest'] == digest(evidence['software_versions'])
      end
    end

    def unaccepted_build_reason(evidence, kernel, deployment)
      vpsadminos = software_version(evidence, 'booted', 'vpsadminos')
      identity = %w[
        reported_release booted_release kernel_source_revision
        config_digest
      ].to_h { |key| [key, kernel[key] || '(missing)'] }
      identity['vpsadminos_revision'] = vpsadminos&.[]('revision') || '(missing)'
      identity['deployment_digest'] = digest(deployment)
      identity['software_digest'] = digest(evidence['software_versions'])
      "kernel build has not been reviewed: #{identity.map { |key, value| "#{key}=#{value}" }.join(', ')}"
    end

    def software_version(evidence, generation, component)
      Array(evidence['software_versions']).find do |version|
        version.is_a?(Hash) &&
          version['generation'] == generation &&
          version['component'] == component
      end
    end

    def digest(value)
      Digest::SHA256.hexdigest(JSON.generate(canonical(value)))
    end

    def canonical(value)
      self.class.canonical_value(value)
    end

    def configuration_result(evidence)
      kernel = evidence.fetch('kernel')
      sysctl_problems = SysctlEvidence.requirement_problems(
        @advisory.platform.fetch('required_sysctls', {}),
        evidence['sysctls'] || {}
      )
      return unknown_assessment(sysctl_problems.join('; ')) unless sysctl_problems.empty?

      options = configuration_options(evidence, kernel)
      unless options
        return unknown_assessment(
          "kernel configuration #{kernel['config_digest'] || '(missing)'} is absent from the evidence catalog"
        )
      end
      @advisory.platform.fetch('required_options', {}).each do |name, requirement|
        actual = options[name]
        return unknown_assessment("kernel option #{name} is missing from exact build evidence") if actual.nil?
        next if option_satisfies?(actual, requirement)

        if option_excludes_interface?(actual, requirement)
          return {
            'state' => 'unreachable',
            'reason' => "required kernel interface #{name}=#{requirement} is deployed as #{actual}"
          }
        end

        return unknown_assessment(
          "kernel option #{name}=#{actual} does not satisfy exact requirement #{requirement}; " \
          'interface reachability is not disproved'
        )
      end
      { 'state' => 'verified' }
    end

    def configuration_options(evidence, kernel)
      catalog_entry = @kernel_configurations[kernel['config_digest']]
      if catalog_entry.is_a?(Hash) && catalog_entry['options'].is_a?(Hash)
        return catalog_entry['options']
      end

      if evidence['_configuration_attested'] && kernel['config_options'].is_a?(Hash)
        return kernel['config_options']
      end

      nil
    end

    def snapshot_evidence_problems(evidence, kernel)
      return ['evidence schema 1 is required for assessment'] unless evidence['schema_version'] == 1

      checks = {
        'kernel boot ID' => kernel['boot_id'].is_a?(String),
        'kernel boot time' => parse_time(kernel['booted_at']),
        'booted kernel parameters' => kernel['booted_params'].is_a?(Array),
        'running kernel command line' => kernel['command_line'].is_a?(String),
        'live patch inventory' => evidence['livepatches'].is_a?(Array),
        'eBPF mitigation inventory' => evidence['ebpf_programs'].is_a?(Array),
        'loaded module inventory' => evidence['loaded_modules'].is_a?(Array),
        'declared and effective sysctls' => SysctlEvidence.valid_map?(evidence['sysctls']),
        'booted system closure' => evidence.dig('deployment', 'booted_system').is_a?(String),
        'current system closure' => evidence.dig('deployment', 'current_system').is_a?(String)
      }
      %w[booted current].product(%w[vpsadminos vpsadmin nixpkgs]).each do |generation, component|
        version = software_version(evidence, generation, component)
        checks["#{generation} #{component} identity"] =
          version.is_a?(Hash) &&
          (version['version'].nil? || (
            version['version'].is_a?(String) &&
            !version['version'].empty? &&
            version['version_source'] == 'native'
          )) &&
          version['revision'].is_a?(String) &&
          version['revision'].match?(/\A[0-9a-f]{40}\z/) &&
          %w[native confctl].include?(version['revision_source']) &&
          version['revision_dirty'] == false
      end
      %w[booted current].each do |generation|
        version = software_version(evidence, generation, 'system_configuration')
        next if version.nil?

        checks["#{generation} vpsFree.cz configuration identity"] =
          version['version'].nil? &&
          version['version_source'].nil? &&
          version['revision'].is_a?(String) &&
          version['revision'].match?(/\A[0-9a-f]{40}\z/) &&
          version['revision_source'] == 'native' &&
          [true, false].include?(version['revision_dirty'])
      end
      problems = checks.filter_map { |component, complete| "#{component} evidence is missing" unless complete }
      problems.concat(
        SysctlEvidence.requirement_problems(
          @advisory.platform.fetch('required_sysctls', {}),
          evidence['sysctls']
        )
      )
      errors = evidence['errors']
      if errors && !errors.is_a?(Array)
        problems << 'reported evidence errors are malformed'
      elsif errors&.any?
        problems.concat(errors.map do |error|
          "reported evidence error #{error['component']}: #{error['reason']}"
        end)
      end
      problems
    end

    def option_satisfies?(actual, requirement)
      case requirement
      when 'enabled'
        %w[y m].include?(actual)
      when 'disabled'
        actual == 'n'
      else
        actual == requirement
      end
    end

    def option_excludes_interface?(actual, requirement)
      (requirement == 'enabled' && actual == 'n') ||
        (requirement == 'disabled' && %w[y m].include?(actual))
    end

    def active_livepatch_mitigation(evidence, kernel, event_type:, state:)
      boot_id = kernel['boot_id']
      unless valid_boot_id?(boot_id)
        state.replace(boot_id: nil, reviewed: {}, protected: [])
        return nil
      end

      reset = state.empty? || event_type == 'boot' || event_type == 'livepatch_change' ||
              state[:boot_id] != boot_id
      state.replace(boot_id:, reviewed: {}, protected: []) if reset

      previous_reviewed = state.fetch(:reviewed)
      previous_protected = state.fetch(:protected)
      patches = Array(evidence['livepatches']).grep(Hash)
      reviewed = patches.each_with_object({}) do |patch, ret|
        next unless patch['loaded'] == true

        key = livepatch_key(patch)
        next unless key

        accepted = accepted_livepatch(patch, evidence, kernel)
        ret[key] = accepted || previous_reviewed[key] if accepted || previous_reviewed[key]
      end

      transitioning = patches.select do |patch|
        patch['loaded'] == true && patch['transition'] == true
      end
      transitioning_patch = transitioning.one? ? transitioning.first : nil
      transitioning_key = livepatch_key(transitioning_patch) if transitioning_patch
      counterpart = case transitioning_patch&.fetch('enabled', nil)
                    when true
                      patches.find do |patch|
                        key = livepatch_key(patch)
                        key && key != transitioning_key && reviewed[key] && patch['loaded'] == true
                      end
                    when false
                      patches.find do |patch|
                        key = livepatch_key(patch)
                        key && key != transitioning_key && reviewed[key] &&
                          effective_livepatch_state?(patch)
                      end
                    end

      state[:reviewed] = reviewed
      counterpart_key = livepatch_key(counterpart) if counterpart
      previously_protected = case transitioning_patch&.fetch('enabled', nil)
                             when true
                               counterpart_key if previous_protected.include?(counterpart_key)
                             when false
                               [transitioning_key, counterpart_key].compact.find do |key|
                                 previous_protected.include?(key)
                               end
                             end
      if transitioning_patch && reviewed[transitioning_key] && counterpart && previously_protected
        state[:protected] = [transitioning_key, counterpart_key]
        protected_patch = patches.find { |patch| livepatch_key(patch) == previously_protected }
        return livepatch_mitigation(protected_patch)
      end
      unless transitioning.empty?
        state[:protected] = []
        return nil
      end

      stable = patches.find do |patch|
        key = livepatch_key(patch)
        key && reviewed[key] && effective_livepatch_state?(patch)
      end
      if stable
        key = livepatch_key(stable)
        state[:protected] = [key]
        return livepatch_mitigation(stable)
      end

      state[:protected] = []
      nil
    end

    def accepted_livepatch(patch, evidence, kernel)
      matching_livepatch_rule(Array(@advisory.platform['accepted_livepatches']), patch, evidence, kernel)
    end

    def matching_livepatch_rule(rules, patch, evidence, kernel)
      vpsadminos_versions = %w[booted current].map do |generation|
        software_version(evidence, generation, 'vpsadminos')
      end
      rules.find do |accepted|
        patch['id'] == accepted['id'] &&
          patch['patch_version'].to_s == accepted['patch_version'].to_s &&
          patch['kernel_version'].to_s == accepted['kernel_version'].to_s &&
          kernel['booted_release'].to_s == accepted['kernel_version'].to_s &&
          livepatch_kernel_identity_matches?(accepted, kernel, vpsadminos_versions)
      end
    end

    def livepatch_key(patch)
      return unless patch.is_a?(Hash)

      values = patch.values_at('id', 'patch_version', 'kernel_version')
      values if values.none? { |value| value.to_s.empty? }
    end

    def livepatch_mitigation(patch)
      {
        'description' => "reviewed live patch #{patch['id']} revision #{patch['patch_version']}",
        'timing' => 'observed'
      }
    end

    def active_ebpf_mitigation(evidence)
      Array(@advisory.platform['accepted_ebpf_programs']).each do |accepted|
        program = Array(evidence['ebpf_programs']).find do |candidate|
          candidate['name'] == accepted['name'] &&
            candidate['revision'].to_s == accepted['revision'].to_s &&
            candidate['digest'].to_s == accepted['digest'].to_s
        end
        next unless program && program['active']

        links = program.fetch('links', {})
        next unless Array(accepted['hooks']).sort == links.keys.sort
        next unless links.values.all? { |attached| attached == true }
        next unless parse_time(program['attached_at']) && parse_time(program['verified_at'])

        return {
          'description' => "reviewed eBPF mitigation #{program['name']} revision #{program['revision']}",
          'effective_at' => program['attached_at'],
          'timing' => 'exact'
        }
      end
      nil
    end

    def livepatch_kernel_identity_matches?(accepted, kernel, vpsadminos_versions)
      vpsadminos_matches = vpsadminos_versions.compact.any? do |version|
        version['revision'].to_s == accepted['vpsadminos_revision'].to_s &&
          %w[native confctl].include?(version['revision_source']) &&
          version['revision_dirty'] == false
      end
      return false unless vpsadminos_matches

      source_revision = kernel['kernel_source_revision']
      source_revision.to_s.empty? ||
        source_revision.to_s == accepted['kernel_source_revision'].to_s
    end

    def unknown_assessment(reason)
      { 'state' => 'unknown', 'reason' => reason }
    end

    def unknown(reason)
      {
        'state' => 'unknown',
        'reason' => reason
      }
    end

    def vulnerable(release, reason = nil)
      fixed = fixed_for(release)
      details = reason || "kernel #{release} is affected"
      details = "#{details}; fixed in #{fixed}" if fixed && !details.include?(fixed)
      {
        'state' => 'vulnerable',
        'reason' => details
      }
    end

    def mitigated(transition, release, current_assessment)
      observed_timing = transition.dig('assessment', 'timing') == 'observed'
      exact = unless observed_timing
                transition.dig('assessment', 'effective_at') || transition['effective_at']
              end
      vulnerable_until = exact || transition['observed_after']
      mitigated_since = exact || transition['observed_before']
      transition_assessment = transition.fetch('assessment')
      reason = transition_assessment['reason'] || current_assessment['reason'] ||
               "kernel #{release} is fixed"
      reason += observation_interval_reason(transition)
      {
        'state' => 'mitigated',
        'vulnerable_until' => vulnerable_until,
        'mitigated_since' => mitigated_since,
        'reason' => reason
      }
    end

    def not_affected(release, reason)
      {
        'state' => 'not_affected',
        'reason' => reason || "kernel #{release} is fixed"
      }
    end

    def unreachable(release, reason)
      {
        'state' => 'not_affected',
        'reason' => "kernel #{release || '(unknown)'} is outside this VPS attack surface: #{reason}"
      }
    end

    def exact_build_reason(assessment)
      assessment['reason'] || 'the current exact build contains the reviewed fix'
    end

    def fixed_for(release)
      match = release.to_s.match(/\A(\d+)\.(\d+)/)
      return unless match

      @advisory.version_rules.dig(match.captures.join('.'), 'fixed_in')
    end

    def observation_interval_reason(event)
      return '' unless event['observed_after']

      return '' if event.dig('assessment', 'timing') != 'observed' &&
                   (event['effective_at'] || event.dig('assessment', 'effective_at'))

      "; the change happened after #{event['observed_after']} " \
        "and was confirmed by #{event['observed_before']}"
    end

    def parse_time(value)
      Time.iso8601(value) if value
    rescue ArgumentError, TypeError
      nil
    end
  end
end
