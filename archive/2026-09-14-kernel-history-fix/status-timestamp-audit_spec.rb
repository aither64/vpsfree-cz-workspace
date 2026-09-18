# frozen_string_literal: true

require 'spec_helper'

RSpec.describe VpsAdmin::Supervisor::Node::Status do
  let(:node) { SpecSeed.node }
  let(:supervisor) { described_class.new(nil, node) }
  let(:timestamp) { Time.utc(2026, 4, 5, 12, 0, 0) }
  let(:now) { Time.utc(2026, 4, 5, 12, 30, 0) }

  def payload(overrides = {})
    {
      'id' => node.id,
      'time' => timestamp.to_i,
      'uptime' => 3600,
      'nproc' => 42,
      'loadavg' => { '1' => 0.5, '5' => 0.25, '15' => 0.1 },
      'vpsadmin_version' => 'spec',
      'kernel' => '6.8.0',
      'cgroup_version' => NodeCurrentStatus.cgroup_versions[:cgroup_v2],
      'cpus' => 8,
      'cpu' => {
        'user' => 10.0,
        'nice' => 0.0,
        'system' => 5.0,
        'idle' => 80.0,
        'iowait' => 2.0,
        'irq' => 1.0,
        'softirq' => 1.0,
        'guest' => 0.0
      },
      'memory' => { 'total' => 8 * 1024 * 1024, 'used' => 4 * 1024 * 1024 },
      'swap' => { 'total' => 2 * 1024 * 1024, 'used' => 1 * 1024 * 1024 },
      'storage' => {
        'state' => 'online',
        'scan' => 'none',
        'scan_percent' => nil,
        'checked_at' => timestamp.to_i
      },
      'arc' => {
        'c_max' => 512 * 1024 * 1024,
        'c' => 256 * 1024 * 1024,
        'size' => 128 * 1024 * 1024,
        'hitpercent' => 95.5
      }
    }.merge(overrides)
  end

  def evidence
    config_text = "CONFIG_IPV6=y\n"
    sysctls = %w[kernel.dmesg_restrict vm.unprivileged_userfaultfd].to_h do |name|
      [
        name,
        {
          'available' => true,
          'configured' => 1,
          'effective' => '1'
        }
      ]
    end
    {
      'schema_version' => 1,
      'kernel' => {
        'boot_id' => 'boot-v2',
        'booted_at' => (timestamp - 3600).iso8601,
        'booted_release' => '6.8.0',
        'reported_release' => '6.8.0',
        'kernel_source_revision' => 'kernel-revision',
        'config_digest' => Digest::SHA256.hexdigest(config_text),
        'config_text' => config_text,
        'booted_params' => ['debug=old', 'debug=new'],
        'command_line' => 'debug=old debug=new'
      },
      'livepatches' => [],
      'ebpf_programs' => [],
      'loaded_modules' => [],
      'sysctls' => sysctls,
      'deployment' => {
        'booted_system' => '/nix/store/booted-system',
        'current_system' => '/nix/store/current-system'
      },
      'software_versions' => %w[booted current].product(
        %w[vpsadminos vpsadmin nixpkgs]
      ).map do |generation, component|
        {
          'generation' => generation,
          'component' => component,
          'version' => "#{component}-version",
          'version_source' => 'native',
          'revision' => Digest::SHA1.hexdigest("#{generation}.#{component}"),
          'revision_source' => 'native',
          'revision_dirty' => false
        }
      end,
      'errors' => []
    }
  end

  before do
    allow(Time).to receive(:now).and_return(now)
  end

  def stored_report(current)
    snapshot = current.reload.kernel_evidence
    VpsAdmin::API::KernelEvidence::SnapshotReader.call(snapshot)&.to_h
  end

  def parse_evidence(value)
    VpsAdmin::API::KernelEvidence::PayloadParser.call(value)
  end

  describe 'related status timestamp audit' do
    def audit_ingest(value, at, consumer: supervisor, overrides: {})
      consumer.send(:update_status, NodeCurrentStatus.find_or_initialize_by(node:),
                    payload(overrides.merge('security_evidence' => value, 'time' => at.to_i)))
    end

    def audit_changed(kind)
      value = evidence
      case kind
      when :software
        item = value.fetch('software_versions').find do |v|
          v['generation'] == 'current' && v['component'] == 'vpsadmin'
        end
        item['revision'] = 'f' * 40
      when :deployment
        value['deployment']['current_system'] = '/nix/store/changed-system'
      when :sysctl
        value['sysctls']['kernel.dmesg_restrict']['effective'] = '0'
      when :module
        value['loaded_modules'] = ['kvm']
      when :livepatch_application
        value['kernel']['reported_release'] = '6.8.1'
        value['livepatches'] = [{
          'id' => 'audit_patch', 'kernel_version' => '6.8.0', 'patch_version' => 1,
          'loaded' => true, 'enabled' => true, 'transition' => false,
          'applied_at' => nil, 'verified_at' => nil, 'patches' => []
        }]
      when :ebpf
        value['ebpf_programs'] = [{
          'name' => 'audit', 'description' => nil, 'sinceKernel' => nil,
          'untilKernel' => nil, 'revision' => 'audit-revision', 'digest' => 'audit-digest',
          'active' => false, 'attached_at' => nil, 'verified_at' => nil,
          'bpfPrograms' => [], 'links' => {}
        }]
      end
      parsed = VpsAdmin::API::KernelEvidence::PayloadParser.call(value)
      expect(parsed.record_events).to be(true), parsed.report.errors.map(&:reason).inspect
      value
    end

    { software: :deployment_change, deployment: :deployment_change,
      sysctl: :sysctl_change, module: :module_change, ebpf: :ebpf_change,
      livepatch_application: :livepatch_change }.each do |kind, type|
      it "uses the latest unchanged report for #{kind} after restart" do
        recent = timestamp + 20.days
        audit_ingest(evidence, timestamp)
        audit_ingest(evidence, recent)
        restarted = described_class.new(nil, Node.find(node.id))
        audit_ingest(audit_changed(kind), recent + 120, consumer: restarted)
        event = node.node_kernel_events.where(event_type: type).sole
        expect(event.observed_after).to eq(recent)
        expect(event.observed_before).to eq(recent + 120)
      end

      it "reproduces the invalid-report fallback losing recent #{kind} confirmation" do
        recent = timestamp + 20.days
        audit_ingest(evidence, timestamp)
        audit_ingest(evidence, recent)
        audit_ingest({ 'schema_version' => 999 }, recent + 30)
        restarted = described_class.new(nil, Node.find(node.id))
        audit_ingest(audit_changed(kind), recent + 120, consumer: restarted)
        event = node.node_kernel_events.where(event_type: type).sole
        expect(event.observed_after).to eq(timestamp)
        expect(event.observed_before).to eq(recent + 120)
        kernel_confirmation = kind == :livepatch_application ? recent : recent + 120
        expect(node.node_kernel_events.boot.sole.last_confirmed_at).to eq(kernel_confirmation)
        puts "AUDIT #{kind}: old lower=#{event.observed_after.utc.iso8601}, proven prior=#{recent.utc.iso8601}, upper=#{event.observed_before.utc.iso8601}"
      end
    end

    it 'retains system-state confirmations through restart and malformed security evidence' do
      recent = timestamp + 20.days
      audit_ingest(evidence, timestamp)
      audit_ingest(evidence, recent)
      audit_ingest({ 'schema_version' => 999 }, recent + 30)
      state = node.node_system_states.current.sole
      expect(state.first_observed_at).to eq(timestamp)
      expect(state.last_observed_at).to eq(recent + 30)
      restarted = described_class.new(nil, Node.find(node.id))
      audit_ingest(evidence, recent + 120, consumer: restarted, overrides: { 'cpus' => 16 })
      expect(state.reload.last_observed_at).to eq(recent + 30)
      expect(node.node_system_states.current.sole.first_observed_at).to eq(recent + 120)
    end
  end
end
