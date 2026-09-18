ENV['RACK_ENV'] = 'test'
require 'bundler/setup'
require 'active_record'
require 'active_support/all'
require 'stringio'
require 'tempfile'
require_relative '../../worktrees/2026-09-14-kernel-history-fix/vpsadmin/api/spec/support/db_setup'

SpecDbSetup.establish_connection!
SpecDbSetup.ensure_database_exists!
ActiveRecord::Schema.verbose = false
source = IO.popen(['git', 'show', '014fbc78422f3660b295add7a50f35cc7acdf0c8:api/db/schema.rb'], &:read)
raise 'Unable to read upstream schema' unless $?.success?
Tempfile.create(['kernel-history-predecessor', '.rb']) do |file|
  file.write(source)
  file.flush
  load file.path
end
require_relative '../../worktrees/2026-09-14-kernel-history-fix/vpsadmin/api/db/migrate/20260914180000_add_node_kernel_event_last_confirmed_at'
require_relative '../../worktrees/2026-09-14-kernel-history-fix/vpsadmin/api/db/migrate/20260914190000_add_node_kernel_evidence_checkpoints'
AddNodeKernelEventLastConfirmedAt.new.migrate(:up)
AddNodeKernelEvidenceCheckpoints.new.migrate(:up)
pool = ActiveRecord::Base.connection_pool
%w[20260914180000 20260914190000].each { |version| pool.schema_migration.create_version(version) }
output = StringIO.new
ActiveRecord::SchemaDumper.dump(pool, output)
File.write('/tmp/kh-recovery-expected-schema.rb', output.string)
raise 'Core schema differs from the migrated upstream schema' unless output.string == File.read('db/schema.rb')
puts 'Both additive migrations on current upstream reproduce the committed core schema exactly'
