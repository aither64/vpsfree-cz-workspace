# Session-only matching examples with synthetic traces; not mount/runtime evidence.
# Prepared and syntax-checked only while the product quick batch is active.
require 'shellwords'
require 'rspec/autorun'

RSpec.describe 'case-specific executed mount evidence' do
  def check_operation(failure, trace)
    operation = case failure
    when 'nonbind'
      ['ext4', '/dev/no-such-persistence-device', '/var/log', %w[mode=0755]]
    when 'nonbind-remount'
      ['tmpfs', 'tmpfs', '/var/log', %w[remount size=invalid]]
    when 'required-remount'
      ['tmpfs', 'tmpfs', '/required-storage', %w[remount size=invalid]]
    when 'ancestor-bind'
      ['none', '/persistent/var/lib', '/var/lib', %w[bind remount]]
    end
    if operation
      fs_type, mount_source, mount_target, required_options = operation
      lines = trace.lines
      mount_position = lines.index do |line|
        next false unless line.match?(/\A\++ mount -t /)
        argv = Shellwords.split(line.sub(/\A\++ /, ""))
        argv.length == 7 && argv.first(4) == ['mount', '-t', fs_type, '-o'] &&
          argv.last(2) == [mount_source, mount_target] &&
          (required_options - argv[4].split(',')).empty?
      end
      refusal_position = lines.index { |line| line.match?(/\A\++ printf .*refusing user allocation/) }
      expect(mount_position).not_to be_nil
      expect(refusal_position).not_to be_nil
      expect(mount_position).to be < refusal_position
    end
  end

  commands = {
    'nonbind' => 'mount -t ext4 -o x-initrd.mount,mode=0755 /dev/no-such-persistence-device /var/log',
    'nonbind-remount' => 'mount -t tmpfs -o remount,x-initrd.mount,size=invalid tmpfs /var/log',
    'required-remount' => 'mount -t tmpfs -o remount,x-initrd.mount,remount,size=invalid tmpfs /required-storage',
    'ancestor-bind' => 'mount -t none -o bind,remount /persistent/var/lib /var/lib'
  }
  refusal = "+ printf 'vpsAdminOS: persisted state unavailable; refusing user allocation\\n'\n+ exit 1\nTRACE_END:1\n"
  commands.each do |failure, command|
    it "accepts the actual #{failure} tuple before refusal at nested trace depth" do
      trace = "TRACE_BEGIN\n++ source /nix/store/example-mounts.sh\n+++ #{command}\n#{refusal}"
      expect { check_operation(failure, trace) }.not_to raise_error
    end

    it "rejects earlier root failure with #{failure} tokens only in diagnostic text" do
      trace = "TRACE_BEGIN\n++ source /nix/store/example-mounts.sh\n+ mount -t tmpfs -o remount tmpfs /\n+ echo #{Shellwords.escape(command)}\n#{refusal}"
      expect { check_operation(failure, trace) }.to raise_error(RSpec::Expectations::ExpectationNotMetError)
    end
  end

  it 'rejects the intended operation after refusal' do
    trace = "#{refusal}+++ #{commands.fetch('nonbind')}\n"
    expect { check_operation('nonbind', trace) }.to raise_error(RSpec::Expectations::ExpectationNotMetError)
  end

  it 'rejects a different target on the intended filesystem' do
    trace = "+++ #{commands.fetch('nonbind-remount').sub('/var/log', '/wrong-target')}\n#{refusal}"
    expect { check_operation('nonbind-remount', trace) }.to raise_error(RSpec::Expectations::ExpectationNotMetError)
  end

  it 'requires complete comma option tokens' do
    trace = "+++ #{commands.fetch('required-remount').sub('size=invalid', 'x-size=invalid')}\n#{refusal}"
    expect { check_operation('required-remount', trace) }.to raise_error(RSpec::Expectations::ExpectationNotMetError)
  end
end
