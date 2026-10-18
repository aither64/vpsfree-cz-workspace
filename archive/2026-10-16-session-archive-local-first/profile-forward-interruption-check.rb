require 'tmpdir'
require 'rbconfig'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/workspace/docs/maintenance/recover-archive-profile-2026-10-16'

def await_condition
  deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + 10
  until yield
    raise 'disposable interruption check deadline' if Process.clock_gettime(Process::CLOCK_MONOTONIC) > deadline
    sleep 0.01
  end
end

def available?(path)
  File.open(path, File::RDWR) { |file| file.flock(File::LOCK_EX | File::LOCK_NB) }
end

%w[TERM KILL].each do |signal|
  Dir.mktmpdir('archive-profile-interruption-') do |directory|
    path = File.join(directory, 'worker.lock'); File.write(path, '')
    ready = File.join(directory, 'ready'); release = File.join(directory, 'release')
    stub = File.join(directory, 'activation.rb')
    File.write(stub, "File.write(ARGV[0], Process.pid.to_s); sleep 0.01 until File.exist?(ARGV[1])\n")
    wrapper = File.join(directory, 'wrapper'); File.write(wrapper, "exec \"$@\"\n")
    parent = fork do
      File.open(path, File::RDWR) do |lock|
        raise 'fixture lock' unless lock.flock(File::LOCK_EX | File::LOCK_NB)
        File.open(File.join(directory, 'output'), 'w') do |output|
          command = ['/run/current-system/sw/bin/bash', wrapper, '/run/current-system/sw/bin/bash', wrapper,
                     RbConfig.ruby, stub, ready, release]
          status = ArchiveProfileRecovery.activation_with_lock(lock, output, command)
          exit! status.success? ? 0 : 1
        end
      end
    end
    begin
      await_condition { File.exist?(ready) }
      Process.kill(signal, parent)
      Process.wait(parent) if signal == 'KILL'
      2.times do |executor|
        raise "#{signal}: executor #{executor} acquired live activation lock" if available?(path)
      end
      raise 'TERM did not defer cancellation' if signal == 'TERM' && Process.waitpid(parent, Process::WNOHANG)
      File.write(release, '')
      if signal == 'TERM'
        _, result = Process.wait2(parent)
        raise 'TERM completion failed' unless result.success?
      end
      await_condition { available?(path) }
      puts "#{signal}: recovery and reconciliation excluded through two exec wrappers until activation ended"
    ensure
      File.write(release, '')
      begin
        Process.wait(parent)
      rescue Errno::ECHILD
      end
    end
  end
end
