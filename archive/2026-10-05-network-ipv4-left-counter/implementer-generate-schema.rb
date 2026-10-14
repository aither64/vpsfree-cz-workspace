ENV['RACK_ENV'] = 'test'
require 'active_record'
require File.expand_path('spec/support/db_setup', Dir.pwd)

SpecDbSetup.establish_connection!(db_name_suffix: 'network_enabled_schema')
SpecDbSetup.ensure_database_exists!
SpecDbSetup.load_schema!
ActiveRecord::MigrationContext.new('db/migrate').run(:up, 20261006120000)
File.open('db/schema.rb', 'w') do |stream|
  ActiveRecord::SchemaDumper.dump(ActiveRecord::Base.connection_pool, stream)
end
