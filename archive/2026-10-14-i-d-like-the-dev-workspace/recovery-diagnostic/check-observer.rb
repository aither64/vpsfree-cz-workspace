# frozen_string_literal: true
require 'json'
require 'open3'
require 'rbconfig'

TEMPLATE = File.read(File.join(__dir__, 'raise-observer.rb'))
PACKAGE = '/synthetic-original-package'
OBSERVER_PATH = '/synthetic-probe/raise-observer.rb'
CANARY = 'SECRET_CANARY_argv_token_snapshot_rpc_payload'

def check(condition, label)
  raise "synthetic check failed: #{label}" unless condition
end

def run_case(body, argv: %w[run-provider-worker fixture], mode: 'workspace-host', extra_options: '', uid_guard: 1000)
  observer = TEMPLATE.gsub('@packageRoot@', PACKAGE)
  observer = observer.sub('Process.uid == 1000', "Process.uid == #{uid_guard}")
  prelude = <<~RUBY
    require 'json'
    ARGV.replace(#{argv.inspect})
    ENV['DEV_WORKSPACE_HOST_MODE'] = #{mode.inspect}
    ENV['RUBYOPT'] = #{("-r#{OBSERVER_PATH} " + extra_options).strip.inspect}
    eval(#{observer.inspect}, TOPLEVEL_BINDING, #{OBSERVER_PATH.inspect})
    error = RuntimeError.new(#{CANARY.inspect} + ' https://private.example/capability /token/private /snapshot/private')
    def check(condition)
      raise 'synthetic propagation or environment assertion' unless condition
    end
    eval(<<~'HOST', TOPLEVEL_BINDING, '#{PACKAGE}/libexec/.workspace-host-wrapped')
      def capture!(error)
        private_argv = ['#{CANARY}', '/token/private']
        raise error
      end
    HOST
  RUBY
  stdout, stderr, status = Open3.capture3({'RUBYOPT' => nil}, RbConfig.ruby, '-e', prelude + body)
  check(status.success?, 'child status')
  check(!stderr.include?(CANARY) && !stdout.include?(CANARY), 'canary omission')
  check(!stderr.match?(%r{https?://|/token/|/snapshot/|private_argv|synthetic-original-package}), 'no private payload or paths')
  lines = stderr.lines
  check(lines.all? { |line| line.start_with?('DW_PROVIDER_RAISE ') && line.bytesize <= 768 }, 'prefix and bytes')
  check(lines.grep(/ frames=/).all? { |line| line.split(' frames=').last.strip.split(',').length <= 6 }, 'six source frames')
  check(lines.length <= 64, 'process record cap')
  check(lines.count { |line| line.include?('truncated ') } <= 1, 'single truncation marker')
  [JSON.parse(stdout), lines]
end

results = []
body = <<~RUBY
  eval(<<~'PROVIDER', TOPLEVEL_BINDING, '#{PACKAGE}/libexec/workspace-codex-providers.rb')
    def provider_helper(error)
      capture!(error)
    end
    def provider_recover(error)
      begin
        provider_helper(error)
      rescue => caught
        check(caught.equal?(error))
      end
    end
    def provider_apply(error)
      begin
        provider_helper(error)
      rescue => caught
        check(caught.equal?(error))
        provider_recover(error)
      end
    end
  PROVIDER
  check(!ENV.key?('RUBYOPT'))
  provider_apply(error)
  provider_apply(Errno::ENOENT.new('#{CANARY}'))
  puts JSON.generate(ok: true)
RUBY
data, lines = run_case(body)
check(data['ok'] && lines.count { |line| line.include?('direction=forward') } == 2, 'forward observation')
check(lines.count { |line| line.include?('direction=recovery') } == 2, 'nested recovery takes precedence')
check(lines.any? { |line| line.include?('class=Errno::ENOENT errno=2') }, 'numeric errno')
check(lines.count { |line| line.include?('active ') } == 1, 'active coverage')
results << {case: 'nested-rescue-original-propagation-errno-canary', records: lines.length, maxBytes: lines.map(&:bytesize).max}

guard_body = <<~RUBY
  eval(<<~'PROVIDER', TOPLEVEL_BINDING, '#{PACKAGE}/libexec/workspace-codex-providers.rb')
    def provider_apply(error)
      capture!(error)
    rescue => caught
      check(caught.equal?(error))
    end
  PROVIDER
  provider_apply(error)
  puts JSON.generate(ok: true)
RUBY
[
  {argv: %w[run-provider-worker other]},
  {argv: %w[run-provider-worker fixture extra]},
  {argv: %w[provider fixture]},
  {mode: 'dev-session'},
  # This process cannot change UID; vary the expected UID literal in the isolated
  # probe copy to exercise rejection, leaving the fixture's exact 1000 untouched.
  {uid_guard: Process.uid + 1},
].each do |options|
  data, lines = run_case(guard_body, **options)
  check(data['ok'] && lines.empty?, 'exact worker/mode/UID guard')
end
results << {case: 'exact-argv-mode-uid-guards', variants: 5}

waiting = <<~RUBY
  eval(<<~'PROVIDER', TOPLEVEL_BINDING, '#{PACKAGE}/libexec/workspace-codex-providers.rb')
    def run_provider_worker(error)
      capture!(error)
    rescue => caught
      check(caught.equal?(error))
    end
  PROVIDER
  check(ENV['RUBYOPT'] == '-w')
  run_provider_worker(error)
  puts JSON.generate(ok: true)
RUBY
_, lines = run_case(waiting, extra_options: '-w')
check(lines.length == 1 && lines.first.include?('active '), 'waiting raises ignored')
results << {case: 'waiting-ignored-unrelated-ruby-options-retained', records: lines.length}

def repeated_body(count, repetitions)
  calls = (1..count).map { '  ' + repetitions.to_s + '.times { provider_helper(error) }' }.join("\n")
  <<~RUBY
    eval(<<~'PROVIDER', TOPLEVEL_BINDING, '#{PACKAGE}/libexec/workspace-codex-providers.rb')
      def provider_helper(error)
        capture!(error)
      rescue => caught
        check(caught.equal?(error))
      end
      def provider_apply(error)
    #{calls}
      end
    PROVIDER
    provider_apply(error)
    puts JSON.generate(ok: true)
  RUBY
end

_, lines = run_case(repeated_body(2, 5))
raises = lines.select { |line| line.include?('direction=forward') }
check(raises.length == 4, 'two per caller signature and distinct helper steps')
check(raises.map { |line| line.split(' frames=').last }.tally.values == [2, 2], 'signature occurrence bound')
check(lines.count { |line| line.include?('truncated ') } == 1, 'suppression marker')
results << {case: 'per-signature-two-provider-caller-distinct', raises: raises.length, records: lines.length}

_, lines = run_case(repeated_body(100, 3))
check(lines.length.between?(62, 64), 'global cap exercised')
check(lines.count { |line| line.include?('truncated ') } == 1, 'global truncation marker')
results << {case: '64-record-768-byte-global-cap', records: lines.length, maxBytes: lines.map(&:bytesize).max}

unknown = guard_body.sub("\nprovider_apply(error)\n", "\nprovider_apply(Class.new(RuntimeError).new('#{CANARY}'))\n")
_, lines = run_case(unknown)
check(lines.any? { |line| line.include?('class=OtherError') }, 'unknown exception classes are fixed category')
results << {case: 'unknown-class-fixed-category', records: lines.length}

failure = <<~RUBY
  target = $stderr
  sink = Object.new
  sink.define_singleton_method(:write) do |line|
    if @failed
      target.write(line)
    else
      @failed = true
      raise '#{CANARY}'
    end
  end
  $stderr = sink
  #{guard_body.sub('puts JSON.generate(ok: true)', '')}
  check(RecoveryRaiseObserver.instance_variable_get(:@disabled))
  puts JSON.generate(ok: true)
RUBY
_, lines = run_case(failure)
check(lines.length == 2 && lines.last.include?('disabled '), 'internal failure is opaque and disabled')
results << {case: 'observer-write-failure-original-exception-preserved', records: lines.length}

_, restarted = run_case(body)
check(restarted.first != run_case(body).last.first, 'per-process active PID coverage')
results << {case: 'new-worker-process-coverage', activeMarkers: 2}
puts JSON.pretty_generate(ruby: RbConfig.ruby, version: RUBY_VERSION, checks: results, status: 'PASS')
