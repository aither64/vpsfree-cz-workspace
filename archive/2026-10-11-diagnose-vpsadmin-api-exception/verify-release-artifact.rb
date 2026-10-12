require 'bundler'
require 'json'
require 'open3'
require 'rbconfig'
require 'rubygems/package'
require 'tmpdir'

gem_path = File.expand_path(ARGV.fetch(0))
package = Gem::Package.new(gem_path)
abort 'Wrong release version' unless package.spec.version.to_s == '0.29.9'
Dir.mktmpdir('haveapi-release-artifact') do |dir|
  package.extract_files(dir)
  %w[json-schema.html protocol.md create-client.md typed-input-validation.md protocol.png].each do |name|
    abort "Missing/empty document: #{name}" unless File.size?(File.join(dir, 'doc', name))
  end
  script = <<~RUBY
    require 'haveapi'
    require 'rack/mock'
    module ReleaseAPI
      class Test < HaveAPI::Resource
        version 1
        auth false
        class Index < HaveAPI::Actions::Default::Index
          authorize { allow }
          def exec; []; end
        end
      end
    end
    server = HaveAPI::Server.new(ReleaseAPI)
    server.use_version(1)
    server.mount('/')
    request = Rack::MockRequest.new(server.app)
    result = %w[/doc/json-schema /doc/protocol.md /doc/create-client.md].to_h do |path|
      response = request.get(path, 'HTTP_HOST' => 'localhost')
      [path, { status: response.status, type: response.content_type, body: response.body }]
    end
    puts JSON.generate({ framework: HaveAPI::Server.instance_method(:mount).source_location.first,
                         version: HaveAPI::VERSION, responses: result })
  RUBY
  env = { 'GEM_HOME' => Gem.dir, 'GEM_PATH' => Gem.path.join(File::PATH_SEPARATOR),
          'RUBYLIB' => nil, 'RUBYOPT' => nil }
  stdout, stderr, status = Bundler.with_unbundled_env do
    Open3.capture3(env, RbConfig.ruby, '-I', File.join(dir, 'lib'), '-e', script,
                  '-I', File.join(Gem.loaded_specs.fetch('haveapi-client').full_gem_path, 'lib'), chdir: dir)
  end
  abort stderr unless status.success?
  result = JSON.parse(stdout)
  abort 'Loaded source framework' unless File.realpath(result.fetch('framework')) == File.join(dir, 'lib/haveapi/server.rb')
  abort 'Wrong framework version' unless result.fetch('version') == '0.29.9'
  { '/doc/json-schema' => 'Envelope', '/doc/protocol.md' => 'Protocol definition',
    '/doc/create-client.md' => 'Client definition' }.each do |path, heading|
    response = result.fetch('responses').fetch(path)
    abort "Invalid response: #{path}" unless response.fetch('status') == 200 &&
                                            response.fetch('type').include?('text/html') &&
                                            response.fetch('body').include?(heading)
    puts "#{path}: 200 text/html, expected content"
  end
  puts "Verified extracted #{File.basename(gem_path)}"
end
