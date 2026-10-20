# frozen_string_literal: true

RSpec.describe SecurityAdvisories::Advisory do
  include AdvisoryFixture

  it 'rejects non ascii cve dash' do
    expect do
      described_class.normalize_cve('CVE-2026–23111')
    end.to raise_error(SecurityAdvisories::Error)
  end

  it 'rejects malformed nested mitigation acceptance rules' do
    advisory = fixture_advisory
    advisory.platform['accepted_ebpf_programs'] = [{
      'name' => 'guard',
      'revision' => 'revision',
      'digest' => 'digest',
      'hooks' => ['lsm/file_open', false]
    }]

    error = nil
    expect do
      advisory.validate!
    end.to raise_error(SecurityAdvisories::Error) { |raised_error| error = raised_error }
    expect(error.message).to include('accepted_ebpf_programs[0] is incomplete')
  end

  it 'requires livepatch kernel and vpsAdminOS identities' do
    advisory = fixture_advisory
    advisory.platform['accepted_livepatches'] = [{
      'id' => 'livepatch_2',
      'patch_version' => '2',
      'kernel_version' => '6.12.95',
      'kernel_source_revision' => 'a' * 40,
      'vpsadminos_revision' => 'b' * 40
    }]
    expect { advisory.validate! }.not_to raise_error

    advisory.platform['accepted_livepatches'][0].delete('kernel_version')
    expect do
      advisory.validate!
    end.to raise_error(SecurityAdvisories::Error, /accepted_livepatches\[0\]/)
  end

  it 'rejects malformed required sysctl contracts' do
    [
      { 'not a sysctl' => ['0'] },
      { 'kernel.dmesg_restrict' => [] },
      { 'kernel.dmesg_restrict' => %w[1 1] },
      { 'kernel.dmesg_restrict' => [1] }
    ].each do |requirements|
      advisory = fixture_advisory(required_sysctls: requirements)

      expect do
        advisory.validate!
      end.to raise_error(
        SecurityAdvisories::Error,
        /platform.required_sysctls/
      )
    end
  end

  it 'requires schema 2 even for an empty introduction rule list' do
    advisory = fixture_advisory
    advisory.platform['affected_livepatches'] = []

    expect { advisory.validate! }.to raise_error(SecurityAdvisories::Error, /requires schema_version 2/)

    advisory.data['schema_version'] = 2
    expect { advisory.validate! }.not_to raise_error
  end

  it 'validates introduction tuples with the protection identity contract' do
    advisory = fixture_advisory
    advisory.data['schema_version'] = 2
    rule = {
      'id' => 'livepatch_2', 'patch_version' => '2', 'kernel_version' => '6.12.95',
      'kernel_source_revision' => 'a' * 40, 'vpsadminos_revision' => 'b' * 40
    }
    advisory.platform['affected_livepatches'] = [rule]
    expect { advisory.validate! }.not_to raise_error

    rule.each_key do |key|
      advisory.platform['affected_livepatches'] = [rule.reject { |name, _value| name == key }]
      expect { advisory.validate! }.to raise_error(SecurityAdvisories::Error, /affected_livepatches\[0\]/)
    end
    advisory.platform['affected_livepatches'] = { 'id' => 'livepatch_2' }
    expect { advisory.validate! }.to raise_error(SecurityAdvisories::Error, /affected_livepatches must be an array/)
  end

  it 'rejects unsupported dossier versions' do
    advisory = fixture_advisory
    advisory.data['schema_version'] = 3
    expect { advisory.validate! }.to raise_error(SecurityAdvisories::Error, /schema_version must be 1 or 2/)
  end

  it 'accepts an explicitly reviewed empty affected-role set in schema 1' do
    advisory = fixture_advisory
    advisory.platform['affected_node_roles'] = []

    expect { advisory.validate! }.not_to raise_error
    expect(advisory.data.fetch('schema_version')).to eq(1)
    schema = JSON.parse(File.read(File.join(SecurityAdvisories::ROOT, 'schema/advisory.schema.json')))
    platform_schema = schema.fetch('properties').fetch('platform')
    role_schema = platform_schema.fetch('properties').fetch('affected_node_roles')
    expect(platform_schema.fetch('required')).to include('affected_node_roles')
    expect(role_schema.fetch('type')).to eq('array')
    expect(role_schema.fetch('minItems', 0)).to eq(0)
    expect(role_schema.fetch('items')).to eq('type' => 'string')
  end

  it 'still requires an affected-role array when no role is applicable' do
    advisory = fixture_advisory
    [nil, 'none', {}].each do |invalid|
      advisory.platform['affected_node_roles'] = invalid
      expect { advisory.validate! }.to raise_error(SecurityAdvisories::Error, /affected_node_roles must be an array/)
    end
  end

  it 'rejects inverted global version bounds' do
    advisory = fixture_advisory
    advisory.data['affected_from'] = '7.1.0'
    advisory.data['fixed_from'] = '6.4.0'

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /affected_from must be older than fixed_from/
    )
  end

  it 'rejects cross-branch and inverted stable ranges' do
    advisory = fixture_advisory
    advisory.version_rules['6.12']['affected_from'] = '6.13.0'

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /version_rules\.6\.12\.affected_from is invalid/
    )

    advisory.version_rules['6.12']['affected_from'] = '6.12.96'

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /version_rules\.6\.12 has an inverted affected range/
    )
  end

  it 'requires an explicit fixed bound or open-ended null' do
    advisory = fixture_advisory
    advisory.version_rules['6.12'].delete('fixed_in')

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /version_rules\.6\.12\.fixed_in is invalid/
    )

    advisory.version_rules['6.12']['fixed_in'] = nil
    expect { advisory.validate! }.not_to raise_error
  end

  it 'rejects noncanonical stable branch keys' do
    advisory = fixture_advisory
    rule = advisory.version_rules.delete('6.12')
    advisory.version_rules[6.12] = rule

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /version_rules\.6\.12 has an invalid branch/
    )

    advisory.version_rules.delete(6.12)
    rule['affected_from'] = '06.12.0'
    rule['fixed_in'] = '06.12.95'
    advisory.version_rules['06.12'] = rule

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /version_rules\.06\.12 has an invalid branch/
    )
  end

  it 'requires summaries to be short titles' do
    advisory = fixture_advisory
    advisory.texts.fetch('en')['summary'] = 'This is a complete explanatory sentence.'

    expect do
      advisory.validate!
    end.to raise_error(
      SecurityAdvisories::Error,
      /texts\.en\.summary must be a short single-line title/
    )
  end

  it 'accepts only short bilingual per-Node notes' do
    advisory = fixture_advisory
    advisory.data['node_notes'] = {
      '1' => {
        'en' => 'Mitigated by live patch',
        'cs' => 'Ošetřeno live patchem'
      }
    }
    expect { advisory.validate! }.not_to raise_error

    advisory.data['node_notes']['1'].delete('cs')
    expect do
      advisory.validate!
    end.to raise_error(SecurityAdvisories::Error, /must contain exactly en and cs/)

    advisory.data['node_notes']['1']['cs'] = "První řádek\ndruhý řádek"
    expect do
      advisory.validate!
    end.to raise_error(SecurityAdvisories::Error, /must be a short single-line note/)
  end
end
