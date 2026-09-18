# frozen_string_literal: true

ENV['RACK_ENV'] = 'test'
require 'spec_helper'

source = File.read('../tests/suite/supervisor/runtime-ingestion.nix')
t = Time.utc(2026, 9, 14, 12)
base = source.match(/^            evidence = \{.*?(?=^            publish = lambda)/m)&.to_s
recovery = source.match(/^            recovered = Marshal.*?(?=^            publish.call\(t \+ 270, recovered\))/m)&.to_s
raise 'Missing exact integration fixtures' unless base && recovery

scope = binding
scope.eval(base)
scope.eval(recovery)
%i[evidence recovered].each do |name|
  parsed = VpsAdmin::API::KernelEvidence::PayloadParser.call(scope.local_variable_get(name))
  raise "Rejected #{name}: #{parsed.report.errors.inspect}" unless parsed.record_events

  puts "Exact integration #{name} accepted by PayloadParser"
end
