# frozen_string_literal: true

# One operation only. Load through RUBYOPT on the selected dev-session wrapper.
if ARGV.include?('074406d2-822a-4079-9ef4-931a802da234') && ARGV.include?('integration-resume')
  require '/nix/store/7gr1y56cc22yk6ciy01l4gwk21kpvxs2-dev-workspace-0.2.0/libexec/workspace-integration'

  module PortalPreparationRecovery
    def advance(value)
      operation = value.fetch('operations').fetch('workspace')
      original_head = 'f73b89d95ad46ff47050dab7f7e4b125538a4e38'
      if value['id'] == '074406d2-822a-4079-9ef4-931a802da234' &&
         value['phase'] == 'prepare' && operation['expectedHead'] == original_head
        unless engine.package == '/nix/store/7gr1y56cc22yk6ciy01l4gwk21kpvxs2-dev-workspace-0.2.0' &&
               engine.workspace == '/home/aither/workspace/ai/vpsfree.cz' &&
               owner['id'] == '420aa210-6d7a-4f07-afe3-ca49aea0ac94' &&
               owner['slug'] == '2026-10-15-portal-performance-fix' &&
               value['ownerId'] == owner['id'] && value.fetch('jobs').empty? &&
               !operation['snapshot'] && !operation['approvalId'] &&
               !value.fetch('steps').fetch('prepare-workspace', {}).key?('result')
          raise WorkspaceCoordination::Error.new('recovery preconditions do not match this unsubmitted run', 5)
        end
        item = value.fetch('request').fetch('repositories').find { |entry| entry['repository'] == 'workspace' }
        unless item && item['head'] == original_head && item['base'] == '453932593b64a284606c6f34e78d63cc8dfa534b' &&
               item['target'] == 'refs/heads/master'
          raise WorkspaceCoordination::Error.new('recovery review range changed', 5)
        end
        engine.current_generation!
        # The ordinary resume already holds the integration lock. This invokes
        # its installed pin recipe, proof, owner admission and leased publication.
        # Keep the original request, review, snapshots and approval identities.
        operation['expectedHead'] = refresh(value, item)
        save(value)
        # Stop before verification/preparation/submission so the lead can capture
        # the exact refreshed comparison and inspect its native proof.
        raise WorkspaceCoordination::Error.new('certified refresh saved; capture comparison and resume without recovery loader', 75)
      end
      raise WorkspaceCoordination::Error.new('recovery loader refuses changed or already-refreshed state; use ordinary resume after inspection', 75)
    end
  end

  WorkspaceCoordination::Integration.prepend(PortalPreparationRecovery)
end
