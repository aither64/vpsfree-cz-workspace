#!/usr/bin/env ruby
# Isolated acceptance fixture: delay the real CLI before it writes a binding.
require 'json'

configuration = JSON.parse(File.read(ENV.fetch('CREATION_ACCEPT_CONFIG')))
command = ARGV.fetch(0)
destination = case command
              when 'start' then ARGV.fetch(1)
              when 'fork' then ARGV.fetch(2)
              else abort('acceptance gate only permits start and fork')
              end
abort('destination is outside the fixture') unless configuration.fetch('slugs').include?(destination)
if command == 'fork'
  abort('source is outside the fixture') unless configuration.fetch('slugs').include?(ARGV.fetch(1))
end
root = configuration.fetch('root')
abort('fixture marker is missing') unless File.file?(File.join(root, 'creation-acceptance-fixture'))
gates = File.join(root, 'gates')
File.open(File.join(gates, "#{destination}.count"), File::RDWR | File::CREAT, 0o600) do |file|
  file.flock(File::LOCK_EX)
  count = file.read.to_i + 1
  file.rewind
  file.truncate(0)
  file.write(count.to_s)
  file.flush
  file.fsync
end
File.write(File.join(gates, "#{destination}.entered"), Process.pid.to_s, mode: 'w', perm: 0o600)
deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + configuration.fetch('gate_seconds')
while File.exist?(File.join(gates, "#{destination}.hold"))
  abort('acceptance gate timed out before CLI initialization') if Process.clock_gettime(Process::CLOCK_MONOTONIC) >= deadline
  sleep 0.1
end
failure = File.join(gates, "#{destination}.fail-once")
if File.exist?(failure)
  File.unlink(failure)
  abort('acceptance gate injected one failure before CLI initialization')
end
# fd 3, when present, is the portal's shared package-transition lock.
exec(*configuration.fetch('cli'), *ARGV, close_others: false)
