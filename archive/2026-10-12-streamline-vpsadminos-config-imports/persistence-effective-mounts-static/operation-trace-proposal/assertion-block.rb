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
