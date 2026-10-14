# frozen_string_literal: true
require 'json'
require 'fileutils'
require File.join(ENV.fetch('INTEGRATION_BENCHMARK_SOURCE'), 'test/integration_test')
IntegrationTest.prepend(Module.new do
  def teardown
    reports = Dir[File.join(@engine.store.root, 'integrations', '*.json')].map do |path|
      value = JSON.parse(File.read(path))
      {'runId' => value['id'], 'phase' => value['phase'], 'phaseSeconds' => value['phaseSeconds'],
       'queueSeconds' => value['queueSeconds'], 'verificationSeconds' => value['verificationSeconds'],
       'preparationSeconds' => value['preparationSeconds'], 'heads' => value['operations'].transform_values { |o| o.dig('snapshot','operation','featureHead') }}
    end
    File.write(ENV.fetch('INTEGRATION_BENCHMARK_OUTPUT'), JSON.pretty_generate(reports)+"\n")
    super
  end
end)
