# Evaluated only on the selected Runner, at its ordinary locked seed boundary.
RETAINED_SEED_GUARD = proc do |requested_slug, goal_file, accepted, expected, frozen|
  raise DevSession::Error, 'retained seed scope changed' unless accepted &&
    @workspace == expected.fetch('workspace') && requested_slug == expected.fetch('slug') &&
    Digest::SHA256.hexdigest(read_goal(goal_file)) == expected.fetch('goalSha256')
  stat = File.stat(File.join(@workspace, 'work', requested_slug))
  raise DevSession::Error, 'tracking directory changed' unless
    [stat.dev, stat.ino] == [frozen.fetch('trackingDevice'), frozen.fetch('trackingInode')]
  frozen.fetch('files').each do |path, ref|
    File.open(path, File::RDONLY | File::NOFOLLOW) do |file|
      actual, current = file.stat, File.lstat(path)
      unless actual.file? && !current.symlink? && [actual.dev, actual.ino] == [current.dev, current.ino] &&
             actual.size <= DevSession::TRACKING_MAX_SIZE &&
             Digest::SHA256.hexdigest(file.read(DevSession::TRACKING_MAX_SIZE + 1)) == ref.fetch('sha256')
        raise DevSession::Error, "frozen retained input changed: #{path}"
      end
    end
  end
  manifest = YAML.safe_load(File.read(File.join(@workspace, 'work', requested_slug, 'portal.yml')))
  unless manifest.dig('codex', 'thread_id') == expected.fetch('threadId') &&
         manifest.dig('creation', 'initial_goal_attempted') == true &&
         manifest.dig('creation', 'initial_goal_sent') == false &&
         manifest.dig('creation', 'goal_sha256') == expected.fetch('goalSha256')
    raise DevSession::Error, 'retained root or initial-goal state changed'
  end
  # Both developed tracking files are already seeded and are left byte-identical.
  nil
end
