require 'json'
require 'open3'
require 'fileutils'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos-benchmark/.github/workflows/scripts/prebuild_benchmark'

product = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos'
root = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-17-impermanence-test-failures/benchmark-child-env-smoke'
FileUtils.mkdir_p(root)
raise 'Unexpected product revision' unless `git -C #{product} rev-parse HEAD`.strip == PrebuildBenchmark::PRODUCT_SHA

original_cleanup = ENV.keys.grep(/\A(?:BUNDLE_|RUBY|GEM_)/).to_h { |name| [name, nil] }
old_output, old_status = Open3.capture2e(original_cleanup, './test-runner.sh', '--help', chdir: product)
File.write(File.join(root, 'old-cli.log'), old_output)
unless old_status.exitstatus == 1 && old_output.include?('geminabox') && old_output.include?('Bundler::GemNotFound')
  raise "Expected original CI failure, got #{old_status.inspect}: #{old_output}"
end

run = PrebuildBenchmark::Run.new(product, root)
run.send(:smoke_cli)
receipt = {
  product_sha: PrebuildBenchmark::PRODUCT_SHA,
  ruby: RUBY_VERSION,
  bundler: Bundler::VERSION,
  old_exit_status: old_status.exitstatus,
  fixed_exit_status: run.instance_variable_get(:@report).fetch('cli_smoke').fetch('exit_status'),
  inherited_bundler_setup: ENV.fetch('BUNDLER_SETUP'),
  inherited_original_keys: ENV.keys.grep(/\ABUNDLER_ORIG_/).sort,
  fixed_bundler_setup: PrebuildBenchmark.cli_environment['BUNDLER_SETUP'],
  fixed_original_keys: PrebuildBenchmark.cli_environment.keys.grep(/\ABUNDLER_ORIG_/),
  child_command: ['./test-runner.sh', '--help']
}
File.write(File.join(root, 'receipt.json'), JSON.pretty_generate(receipt))
puts JSON.pretty_generate(receipt)
