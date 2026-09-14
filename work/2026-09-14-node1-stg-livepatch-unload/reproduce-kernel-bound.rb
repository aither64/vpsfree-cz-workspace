# Read-only diagnostic: run the real recorder's boundary-selection method with
# in-memory report, stable-event, and persistence adapters. No database is used.
require 'json'
require 'time'

ROOT = File.expand_path('../..', __dir__)
REVISION = '791ab3aa89e2f613979da6090b89785c78245db5'
SOURCE = 'api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb'

module VpsAdmin
  module API
    module Operations
      class Base; end
      module Node; end
    end
    module KernelEvidence
      class SnapshotReader
        def self.call(snapshot) = snapshot
      end
    end
  end
end

# The selected method needs neither dependency, nor ActiveSupport beyond minutes.
$LOADED_FEATURES << 'vpsadmin/api/operations/base.rb'
$LOADED_FEATURES << 'vpsadmin/api/kernel_evidence/boot_time_confidence.rb'
class Integer
  def minutes = self * 60
end

source = IO.popen(
  ['git', "--git-dir=#{ROOT}/repos/vpsadmin.git", 'show', "#{REVISION}:#{SOURCE}"], &:read
)
raise 'cannot read pinned recorder source' unless $?.success?
eval(source, TOPLEVEL_BINDING, "#{REVISION}:#{SOURCE}")

KernelReport = Data.define(:reported_release)
Patch = Data.define(:id, :loaded, :enabled, :transition)
Report = Data.define(:kernel, :livepatches, :errors)
StableEvent = Data.define(:observed_before, :kernel_evidence)

class DiagnosticRecorder < VpsAdmin::API::Operations::Node::RecordKernelEvidence
  attr_accessor :stable_event
  attr_reader :events

  def initialize(stable_event)
    @stable_event = stable_event
    @events = []
  end

  def observe(previous, current, previous_time, current_time)
    send(
      :record_kernel_release_changes,
      node: nil,
      report: current,
      previous_report: previous,
      previous_observed_at: previous_time,
      observed_at: current_time
    )
  end

  protected

  def stable_kernel_event(_node) = stable_event
  def create_event!(**attributes) = @events << attributes
end

def report(release, patches)
  Report.new(kernel: KernelReport.new(reported_release: release), livepatches: patches, errors: [])
end

old_event_time = Time.iso8601('2026-08-22T17:33:29+02:00')
recent_time = Time.iso8601('2026-09-13T19:58:20+02:00')
transition_time = Time.iso8601('2026-09-13T19:59:50+02:00')
new_time = Time.iso8601('2026-09-13T20:00:36+02:00')
applied = report('6.12.95.6', [Patch.new(id: 'livepatch_6', loaded: true, enabled: true, transition: false)])
unpatching = report('6.12.95.6', [Patch.new(id: 'livepatch_6', loaded: true, enabled: false, transition: true)])
removed = report('6.12.95', [])

outputs = []
[:direct_removal, :removal_after_transition, :release_only, :application_control].each do |scenario|
  baseline = scenario == :application_control ? removed : applied
  baseline = report('6.12.95', []) if scenario == :release_only
  recorder = DiagnosticRecorder.new(StableEvent.new(observed_before: old_event_time, kernel_evidence: baseline))

  # A recent identical report produces no event, leaving the event timestamp old.
  recorder.observe(baseline, baseline, recent_time - 30, recent_time)
  raise 'unchanged report unexpectedly created an event' unless recorder.events.empty?

  if scenario == :removal_after_transition
    recorder.observe(applied, unpatching, recent_time, transition_time)
    recorder.observe(unpatching, removed, transition_time, new_time)
  elsif scenario == :application_control
    recorder.observe(removed, applied, recent_time, new_time)
  elsif scenario == :release_only
    recorder.observe(baseline, report('6.12.95.6', []), recent_time, new_time)
  else
    recorder.observe(applied, removed, recent_time, new_time)
  end

  event = recorder.events.last
  lower_bound = event.fetch(:previous_observed_at)
  expected_current_behavior = scenario == :application_control ? recent_time : old_event_time
  raise 'pinned behavior differs from diagnosis' unless lower_bound == expected_current_behavior
  outputs << {
    scenario:,
    event_type: event.fetch(:event_type),
    livepatch_action: event[:livepatch_action],
    latest_confirmed_previous_state: recent_time.iso8601,
    actual_observed_after: lower_bound.iso8601,
    actual_observed_before: event.fetch(:observed_at).iso8601,
    stale_lower_bound: lower_bound < recent_time
  }
end

puts JSON.pretty_generate({ revision: REVISION, scope: 'real selection logic; mocked persistence', scenarios: outputs })
