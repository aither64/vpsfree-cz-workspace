require 'date'
require 'digest'
require 'json'
require 'rubygems/version'
require 'time'
require 'yaml'

module SecurityAdvisories
  class Advisory
    IMPACT_KEYS = %w[vps_root node_root cross_vps node_availability].freeze
    IMPACT_VALUES = %w[not_applicable unlikely possible plausible demonstrated unknown].freeze
    REQUIRED_TEXTS = %w[summary description response].freeze
    REQUIRED_NOTE_LANGUAGES = %w[en cs].freeze
    MAX_SUMMARY_LENGTH = 80
    MAX_NODE_NOTE_LENGTH = 120
    REQUIRED_SOFTWARE_IDENTITIES =
      %w[booted current].product(%w[vpsadminos vpsadmin nixpkgs]).freeze
    OPTIONAL_SOFTWARE_IDENTITIES =
      %w[booted current].product(%w[system_configuration]).freeze

    attr_reader :cve, :data, :directory, :historical_attestations

    def self.load(cve, root: SecurityAdvisories::ROOT)
      normalized = normalize_cve(cve)
      directory = File.join(root, 'advisories', normalized)
      path = File.join(directory, 'advisory.yml')
      attestations_path = File.join(directory, 'historical-attestations.yml')
      attestations = if File.file?(attestations_path)
                       YAML.safe_load_file(attestations_path, permitted_classes: [Date, Time])
                     else
                       { 'schema_version' => 1, 'attestations' => [] }
                     end
      new(
        YAML.safe_load_file(path, permitted_classes: [Date, Time]),
        directory:,
        historical_attestations: attestations
      ).tap(&:validate!)
    rescue Errno::ENOENT
      raise Error, "advisory dossier not found for #{normalized}"
    rescue Psych::SyntaxError => e
      raise Error, "invalid YAML for #{normalized}: #{e.message}"
    end

    def self.normalize_cve(value)
      cve = value.to_s.upcase
      raise Error, "invalid CVE identifier #{value.inspect}" unless cve.match?(/\ACVE-\d{4}-\d{4,}\z/)

      cve
    end

    def initialize(data, directory:, historical_attestations: { 'schema_version' => 1, 'attestations' => [] })
      @data = data
      @directory = directory
      @cve = data['cve']
      @historical_attestations_document = historical_attestations
      @historical_attestations = if historical_attestations.is_a?(Hash)
                                   Array(historical_attestations['attestations'])
                                 else
                                   []
                                 end
    end

    def validate!
      errors = []
      errors << 'schema_version must be 1 or 2' unless [1, 2].include?(data['schema_version'])
      if platform.has_key?('affected_livepatches') && data['schema_version'] != 2
        errors << 'platform.affected_livepatches requires schema_version 2'
      end
      if platform.has_key?('affected_livepatches') && !platform['affected_livepatches'].is_a?(Array)
        errors << 'platform.affected_livepatches must be an array'
      end
      errors << 'cve is invalid' unless cve.to_s.match?(/\ACVE-\d{4}-\d{4,}\z/)
      errors << 'directory and cve differ' unless File.basename(directory) == cve
      errors << 'name is required' if data['name'].to_s.empty?
      global_affected = kernel_version(data['affected_from'])
      global_fixed = kernel_version(data['fixed_from'])
      errors << 'affected_from must be a kernel version' unless global_affected
      errors << 'fixed_from must be a kernel version' unless global_fixed
      if global_affected && global_fixed && global_affected >= global_fixed
        errors << 'affected_from must be older than fixed_from'
      end
      errors << 'version_rules must not be empty' if version_rules.empty?
      errors << 'platform.configuration_assessed must be true' unless platform['configuration_assessed'] == true
      unless @historical_attestations_document.is_a?(Hash) &&
             @historical_attestations_document['schema_version'] == 1 &&
             @historical_attestations_document['attestations'].is_a?(Array)
        errors << 'historical-attestations.yml must use schema version 1 with an attestations array'
      end

      version_rules.each do |branch, rule|
        branch_name = branch.to_s
        unless branch.is_a?(String) && branch_name.match?(/\A(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\z/)
          errors << "version_rules.#{branch} has an invalid branch"
        end
        open_ended = rule.is_a?(Hash) && rule.has_key?('fixed_in') && rule['fixed_in'].nil?
        unless rule.is_a?(Hash) &&
               (open_ended || version_in_branch?(rule['fixed_in'], branch_name))
          errors << "version_rules.#{branch}.fixed_in is invalid"
        end
        if rule.is_a?(Hash)
          rule_affected = kernel_version(rule['affected_from'])
          rule_fixed = kernel_version(rule['fixed_in'])
          unless rule_affected && version_in_branch?(rule['affected_from'], branch_name)
            errors << "version_rules.#{branch}.affected_from is invalid"
          end
          if rule_affected && rule_fixed && rule_affected >= rule_fixed
            errors << "version_rules.#{branch} has an inverted affected range"
          end
        end
        %w[introduced_commit fixed_commit].each do |commit_key|
          next unless rule.is_a?(Hash) && rule[commit_key]
          next if rule[commit_key].to_s.match?(/\A[0-9a-f]{40}\z/)

          errors << "version_rules.#{branch}.#{commit_key} is invalid"
        end
      end

      required_options = platform['required_options']
      unless required_options.is_a?(Hash) && required_options.all? do |name, value|
               name.to_s.match?(/\ACONFIG_[A-Z0-9_]+\z/) &&
               %w[enabled disabled y m n].include?(value)
             end
        errors << 'platform.required_options must map CONFIG_* names to enabled, disabled, y, m, or n'
      end
      unless SysctlEvidence.valid_requirements?(platform['required_sysctls'])
        errors << 'platform.required_sysctls must map valid names to unique accepted effective values'
      end

      %w[affected_node_roles accepted_kernel_builds accepted_livepatches accepted_ebpf_programs].each do |key|
        errors << "platform.#{key} must be an array" unless platform[key].is_a?(Array)
      end
      begin
        Time.iso8601(platform.fetch('history_required_since').to_s)
      rescue ArgumentError, KeyError
        errors << 'platform.history_required_since must be an ISO 8601 timestamp'
      end
      history_start_overrides = platform.fetch('history_start_overrides', {})
      unless history_start_overrides.is_a?(Hash)
        errors << 'platform.history_start_overrides must be a map'
        history_start_overrides = {}
      end
      history_start_overrides.each do |node_id, override|
        next if node_id.to_s.match?(/\A\d+\z/) && override.is_a?(Hash) &&
                valid_time?(override['required_since']) &&
                !override['reason'].to_s.strip.empty? &&
                !override['source'].to_s.strip.empty?

        errors << "platform.history_start_overrides.#{node_id} is incomplete"
      end

      Array(platform['accepted_kernel_builds']).each_with_index do |build, index|
        required = %w[
          reported_release booted_release kernel_source_revision
          vpsadminos_revision config_digest deployment_digest software_digest
          fix_state
        ]
        unless build.is_a?(Hash) && required.all? { |key| !build[key].to_s.empty? }
          errors << "platform.accepted_kernel_builds[#{index}] is incomplete"
          next
        end
        unless %w[affected fixed].include?(build['fix_state'])
          errors << "platform.accepted_kernel_builds[#{index}].fix_state is invalid"
        end
        %w[config_digest deployment_digest software_digest].each do |key|
          unless build[key].to_s.match?(/\A[0-9a-f]{64}\z/)
            errors << "platform.accepted_kernel_builds[#{index}].#{key} is invalid"
          end
        end
      end
      %w[accepted_livepatches affected_livepatches].each do |key|
        Array(platform[key]).each_with_index do |patch, index|
          errors << "platform.#{key}[#{index}] is incomplete" unless valid_livepatch_rule?(patch)
        end
      end
      Array(platform['accepted_ebpf_programs']).each_with_index do |program, index|
        required = %w[name revision digest]
        next if program.is_a?(Hash) &&
                required.all? { |key| !program[key].to_s.empty? } &&
                program['hooks'].is_a?(Array) && !program['hooks'].empty? &&
                program['hooks'].all? { |hook| hook.is_a?(String) && !hook.empty? } &&
                program['hooks'].uniq.length == program['hooks'].length

        errors << "platform.accepted_ebpf_programs[#{index}] is incomplete"
      end

      historical_attestations.each_with_index do |attestation, index|
        unless valid_historical_attestation?(attestation)
          errors << "historical attestations[#{index}] is incomplete"
        end
      end
      duplicates = historical_attestations.group_by do |attestation|
        [attestation['node_id'], attestation['event_id']] if attestation.is_a?(Hash)
      end.select { |key, values| key && values.length > 1 }
      errors << 'historical attestations contain duplicate node/event pairs' unless duplicates.empty?

      IMPACT_KEYS.each do |key|
        value = impact[key]
        errors << "impact.#{key} is invalid" unless IMPACT_VALUES.include?(value)
      end

      %w[en cs].each do |language|
        REQUIRED_TEXTS.each do |key|
          errors << "texts.#{language}.#{key} is required" if texts.dig(language, key).to_s.strip.empty?
        end

        summary = texts.dig(language, 'summary').to_s
        if summary.length > MAX_SUMMARY_LENGTH || summary.match?(/[\r\n]/) || summary.match?(/[.!?]\z/)
          errors << "texts.#{language}.summary must be a short single-line title"
        end
      end

      if node_notes.is_a?(Hash)
        node_notes.each do |node_id, notes|
          unless node_id.is_a?(String) && node_id.match?(/\A[1-9]\d*\z/)
            errors << "node_notes.#{node_id} has an invalid Node ID"
            next
          end
          unless notes.is_a?(Hash) && notes.keys.sort == REQUIRED_NOTE_LANGUAGES.sort
            errors << "node_notes.#{node_id} must contain exactly en and cs"
            next
          end

          REQUIRED_NOTE_LANGUAGES.each do |language|
            note = notes[language]
            next if note.is_a?(String) && !note.strip.empty? &&
                    note.length <= MAX_NODE_NOTE_LENGTH && !note.match?(/[\r\n]/)

            errors << "node_notes.#{node_id}.#{language} must be a short single-line note"
          end
        end
      else
        errors << 'node_notes must be a map'
      end

      errors << 'analysis.md is required' unless File.file?(File.join(directory, 'analysis.md'))
      raise Error, "#{cve || File.basename(directory)}: #{errors.join('; ')}" unless errors.empty?

      self
    end

    def name = data.fetch('name')
    def affected_from = data.fetch('affected_from')
    def fixed_from = data.fetch('fixed_from')
    def version_rules = data.fetch('version_rules', {})
    def platform = data.fetch('platform', {})
    def impact = data.fetch('impact', {})
    def texts = data.fetch('texts', {})
    def node_notes = data.fetch('node_notes', {})

    def digest
      analysis = File.read(File.join(directory, 'analysis.md'))
      Digest::SHA256.hexdigest(
        JSON.generate(canonical(data)) +
        JSON.generate(canonical(@historical_attestations_document)) +
        analysis
      )
    end

    def advisory_attributes
      attrs = { 'name' => name }
      texts.each do |language, values|
        REQUIRED_TEXTS.each do |key|
          attrs["#{language}_#{key}"] = values.fetch(key)
        end
      end
      attrs
    end

    protected

    def valid_livepatch_rule?(patch)
      required = %w[id patch_version kernel_version kernel_source_revision vpsadminos_revision]
      patch.is_a?(Hash) && required.all? { |key| !patch[key].to_s.empty? } &&
        (patch['patch_version'].is_a?(String) || patch['patch_version'].is_a?(Numeric)) &&
        patch['kernel_source_revision'].to_s.match?(/\A[0-9a-f]{40}\z/) &&
        patch['vpsadminos_revision'].to_s.match?(/\A[0-9a-f]{40}\z/)
    end

    def kernel_version(value)
      return unless value.to_s.match?(/\A\d+\.\d+(?:\.\d+)*(?:[-.][0-9A-Za-z._-]+)?\z/)

      Gem::Version.new(value.to_s)
    rescue ArgumentError
      nil
    end

    def version_in_branch?(value, branch)
      value.to_s.match?(/\A#{Regexp.escape(branch)}\.\d+(?:[.-].*)?\z/)
    end

    def valid_historical_attestation?(attestation)
      return false unless attestation.is_a?(Hash)
      return false unless attestation['node_id'].is_a?(Integer) && attestation['event_id'].is_a?(Integer)
      return false unless attestation['event_digest'].to_s.match?(/\A[0-9a-f]{64}\z/)
      return false if attestation['source'].to_s.strip.empty?

      evidence = attestation['security_evidence']
      kernel = evidence.is_a?(Hash) ? evidence['kernel'] : nil
      required_kernel_strings = %w[
        boot_id reported_release booted_release kernel_source_revision
        config_digest command_line
      ]
      deployment = evidence.is_a?(Hash) ? evidence['deployment'] : nil
      schema_version = evidence.is_a?(Hash) ? evidence['schema_version'] : nil
      kernel.is_a?(Hash) &&
        schema_version == 1 &&
        required_kernel_strings.all? { |key| kernel[key].is_a?(String) } &&
        !kernel['boot_id'].empty? &&
        kernel['config_digest'].match?(/\A[0-9a-f]{64}\z/) &&
        valid_time?(kernel['booted_at']) &&
        kernel['booted_params'].is_a?(Array) &&
        kernel['config_options'].is_a?(Hash) &&
        deployment.is_a?(Hash) &&
        %w[booted_system current_system].all? { |key| deployment[key].is_a?(String) } &&
        evidence['livepatches'].is_a?(Array) &&
        evidence['ebpf_programs'].is_a?(Array) &&
        evidence['loaded_modules'].is_a?(Array) &&
        SysctlEvidence.valid_map?(evidence['sysctls']) &&
        valid_software_versions?(evidence['software_versions']) &&
        evidence['errors'].is_a?(Array)
    end

    def valid_software_versions?(versions)
      return false unless versions.is_a?(Array) && versions.all?(Hash)

      by_key = versions.to_h do |version|
        [[version['generation'], version['component']], version]
      end
      allowed = REQUIRED_SOFTWARE_IDENTITIES + OPTIONAL_SOFTWARE_IDENTITIES
      return false unless by_key.length == versions.length
      return false unless (REQUIRED_SOFTWARE_IDENTITIES - by_key.keys).empty?
      return false unless (by_key.keys - allowed).empty?

      by_key.all? do |key, version|
        if OPTIONAL_SOFTWARE_IDENTITIES.include?(key)
          next version['version'].nil? &&
            version['version_source'].nil? &&
            version['revision'].is_a?(String) &&
            version['revision'].match?(/\A[0-9a-f]{40}\z/) &&
            version['revision_source'] == 'native' &&
            [true, false].include?(version['revision_dirty'])
        end

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
    end

    def valid_time?(value)
      Time.iso8601(value.to_s)
      true
    rescue ArgumentError
      false
    end

    def canonical(value)
      case value
      when Hash
        value.keys.sort.to_h { |key| [key, canonical(value[key])] }
      when Array
        value.map { |item| canonical(item) }
      when Date, Time
        value.iso8601
      else
        value
      end
    end
  end
end
