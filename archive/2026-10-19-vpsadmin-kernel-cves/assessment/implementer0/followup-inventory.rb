require 'json'
require 'digest'
require 'fileutils'
require File.join(Dir.pwd, 'lib/security_advisories')

session = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
snapshot = JSON.parse(File.read('.state/evidence.json'))
raise 'changed frozen evidence' unless Digest::SHA256.file('.state/evidence.json').hexdigest ==
                                       '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
advisory = SecurityAdvisories::Advisory.load('CVE-2026-74753')
evaluator = SecurityAdvisories::Evaluator.new(
  advisory, evidence_time: Time.iso8601(snapshot.fetch('collected_at')),
  kernel_configurations: snapshot.fetch('kernel_configurations')
)
raw = []
summary = snapshot.fetch('nodes').filter_map do |node|
  next unless node['node_role'] == 'node'

  state = {}
  points = evaluator.send(:build_timeline, node).map do |point|
    point.merge('assessment' => evaluator.send(
      :assess_snapshot, point.fetch('security_evidence'),
      event_type: point.fetch('event_type'), livepatch_state: state
    ))
  end
  raw << { 'node_id' => node['node_id'], 'points' => points }
  unknowns = points.select { |point| point.dig('assessment', 'state') == 'unknown' }
  last_unsafe = points.rindex { |point| %w[affected unknown].include?(point.dig('assessment', 'state')) }
  suffix = last_unsafe ? points[(last_unsafe + 1)..] : []
  fixed_boot = suffix.find do |point|
    point['event_type'] == 'boot' && point.dig('assessment', 'state') == 'fixed'
  end
  {
    'node_id' => node['node_id'],
    'timeline_points' => points.length,
    'historical_states' => points.group_by { |p| p.dig('assessment', 'state') }.transform_values(&:length),
    'unknown_categories' => unknowns.group_by { |p| p.dig('assessment', 'reason') }.transform_values(&:length),
    'last_unsafe_observed_before' => last_unsafe && points[last_unsafe]['observed_before'],
    'subsequent_fixed_boot' => fixed_boot&.slice('event_type', 'effective_at', 'observed_after', 'observed_before', 'confidence'),
    'fixed_boot_release' => fixed_boot&.dig('security_evidence', 'kernel', 'booted_release'),
    'current_assessment' => points.last.fetch('assessment'),
    'global_guards' => evaluator.send(:evidence_problems, node) +
                       evaluator.send(:coverage_problems, node) + evaluator.send(:attestation_problems, node)
  }
end
FileUtils.mkdir_p('.state/implementer0', mode: 0o700)
File.write('.state/implementer0/followup-perf-timeline.json', JSON.pretty_generate(raw) + "\n", mode: 'w', perm: 0o600)
File.write(File.join(session, 'assessment/implementer0/followup-perf-history.json'), JSON.pretty_generate(summary) + "\n")
puts JSON.pretty_generate(summary)
