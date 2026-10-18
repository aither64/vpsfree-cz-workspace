require 'tmpdir'
require 'fileutils'
require 'json'
require 'digest'
require File.join(ARGV.fetch(0), 'libexec/workspace-coordination')

Dir.mktmpdir('integration-upgrade-predecessor-') do |temporary|
  store = WorkspaceCoordination::Store.new(File.join(temporary, 'state'))
  package = File.join(temporary, 'candidate')
  shared = File.join(package, 'share/dev-workspace')
  FileUtils.mkdir_p(shared)
  FileUtils.cp(File.join(ARGV.fetch(1), 'nix/coordination-contract.json'), File.join(shared, 'coordination-contract.json'))
  FileUtils.cp(File.join(ARGV.fetch(1), 'nix/integration-contract.json'), File.join(shared, 'integration-contract.json'))
  File.write(File.join(shared, 'coordination.json'), JSON.generate('schema' => 1, 'adapters' => {}, 'machines' => {}, 'repositories' => {}, 'profileMachine' => nil))
  metadata = File.join(shared, 'package.json')
  File.write(metadata, JSON.generate('integration' => {'journalSchema' => 1, 'certificationSchema' => 1}))
  WorkspaceCoordination.atomic(File.join(store.root, 'ledger.json'), store.empty)
  journal = File.join(store.root, 'integrations', '12345678-1234-1234-1234-123456789abc.json')
  WorkspaceCoordination.atomic(journal, {'schema' => 1, 'id' => '12345678-1234-1234-1234-123456789abc', 'phase' => 'prepare'})
  before = File.binread(journal)
  store.require_compatible!(package)
  raise 'manual journal changed' unless File.binread(journal) == before
  File.write(metadata, JSON.generate('integration' => {'journalSchema' => 2, 'certificationSchema' => 1}))
  begin
    store.require_compatible!(package)
    raise 'negative control did not exercise predecessor capability guard'
  rescue WorkspaceCoordination::Error => error
    raise unless error.message.include?('candidate cannot resume pending integration journals')
  end
  puts JSON.generate('predecessor' => ARGV.fetch(0), 'sourceSha256' => Digest::SHA256.file(File.join(ARGV.fetch(0), 'libexec/workspace-coordination.rb')).hexdigest, 'pendingManualUpgrade' => 'accepted', 'journalUnchanged' => true, 'oldMetadata2NegativeControl' => 'refused')
end
