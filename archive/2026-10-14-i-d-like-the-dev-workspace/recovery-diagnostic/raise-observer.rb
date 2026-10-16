# frozen_string_literal: true

# Temporary fixture observer. No product methods or exception handling change.
module RecoveryRaiseObserver
  PACKAGE = '@packageRoot@'
  PROVIDER = "#{PACKAGE}/libexec/workspace-codex-providers.rb"
  HOST = "#{PACKAGE}/libexec/.workspace-host-wrapped"
  SOURCES = {PROVIDER => 'provider', HOST => 'host'}.freeze
  METHODS = %w[
    provider_apply provider_recover provider_helper provider_private_server
    provider_wait_shared_server provider_process_binary provider_native_binary
    require_provider_restart_safe! provider_restore_terminals provider_write_state
    provider_state provider_directory provider_state_path provider_finish
    provider_argv provider_catalog provider_thread_environment
    atomic_private_file read_private_json_file! quiesce_sessions
    restore_quiesced_sessions capture! system! active_codex package_root
    registration_plan_for instance_runtime find_command
  ].freeze
  CLASSES = %w[
    DevWorkspaceHost::Error RuntimeError ArgumentError TypeError KeyError
    NoMethodError NameError IOError EOFError JSON::ParserError
    Errno::ENOENT Errno::EACCES Errno::EPERM Errno::ESRCH Errno::ECHILD
    Errno::EPIPE Errno::ECONNREFUSED Errno::ECONNRESET Errno::ETIMEDOUT
    Errno::ENOSPC Errno::EIO Errno::EINVAL Errno::EEXIST Errno::ENOTDIR
  ].freeze

  class << self
    def start
      return unless ARGV == %w[run-provider-worker fixture] &&
                    ENV['DEV_WORKSPACE_HOST_MODE'] == 'workspace-host' && Process.uid == 1000

      # The fixture injects one require option. Retain any unrelated Ruby options.
      option = /(?<!\S)-r#{Regexp.escape(__FILE__)}(?!\S)/
      if ENV['RUBYOPT']&.match?(option)
        remaining = ENV.fetch('RUBYOPT').sub(option, '').strip
        remaining.empty? ? ENV.delete('RUBYOPT') : ENV['RUBYOPT'] = remaining
      end
      @pid = Process.pid
      @started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
      @records = 0
      @sequence = 0
      @signatures = Hash.new(0)
      @truncated = false
      @disabled = false
      emit("active pid=#{@pid}")
      @trace = TracePoint.new(:raise) do |event|
        begin
          observe(event)
        rescue Exception # An observer failure must never replace the product exception.
          disable
        end
      end
      @trace.enable
    rescue Exception
      disable
    end

    def emit(fields)
      line = "DW_PROVIDER_RAISE #{fields}\n"
      raise 'observer bound' if line.bytesize > 768 || @records >= 64
      $stderr.write(line)
      @records += 1
    end

    def truncate
      return if @truncated
      @truncated = true
      emit("truncated pid=#{@pid}")
    end

    def disable
      @disabled = true
      @trace&.disable
      begin
        emit("disabled pid=#{Process.pid}") if @records && @records < 64
      rescue Exception
        # Even a failed diagnostic write is opaque and cannot affect propagation.
      end
    end

    def observe(event)
      return if @disabled
      # Only exact original packaged source locations can contribute names/lines.
      locations = caller_locations(0, 128).select { |frame| SOURCES.key?(frame.absolute_path || frame.path) }
      return unless locations.any? { |frame| frame.path == PROVIDER && frame.base_label == 'provider_apply' } ||
                    locations.any? { |frame| frame.path == PROVIDER && frame.base_label == 'provider_recover' }
      direction = locations.any? { |frame| frame.path == PROVIDER && frame.base_label == 'provider_recover' } ? 'recovery' : 'forward'
      error = event.raised_exception
      name = error.class.name
      name = 'OtherError' unless CLASSES.include?(name)
      frames = []
      if SOURCES.key?(event.path)
        method = METHODS.include?(event.method_id.to_s) ? event.method_id.to_s : 'other'
        frames << "#{SOURCES.fetch(event.path)}:#{event.lineno}:#{method}"
      end
      locations.each do |frame|
        method = METHODS.include?(frame.base_label) ? frame.base_label : 'other'
        frames << "#{SOURCES.fetch(frame.absolute_path || frame.path)}:#{frame.lineno}:#{method}"
      end
      frames = frames.uniq.first(6)
      # Include the provider caller as well as the immediate helper raise site.
      provider_caller = locations.find do |frame|
        frame.path == PROVIDER && %w[provider_apply provider_recover].include?(frame.base_label)
      end
      signature = [direction, name, event.path, event.lineno,
                   provider_caller&.lineno, provider_caller&.base_label]
      if @signatures[signature] >= 2
        truncate
        return
      end
      if @records >= 62
        truncate
        @disabled = true
        @trace.disable
        return
      end
      @signatures[signature] += 1
      @sequence += 1
      elapsed = ((Process.clock_gettime(Process::CLOCK_MONOTONIC) - @started) * 1000).to_i
      errno = error.is_a?(SystemCallError) ? error.errno : nil
      errno = nil unless errno.is_a?(Integer) && errno.between?(0, 65535)
      emit("pid=#{@pid} seq=#{@sequence} elapsed_ms=#{elapsed} direction=#{direction} class=#{name} errno=#{errno || '-'} frames=#{frames.join(',')}")
    end
  end
end

RecoveryRaiseObserver.start
