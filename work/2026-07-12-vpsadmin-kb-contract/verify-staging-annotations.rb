#!/usr/bin/env ruby
# frozen_string_literal: true

require 'net/http'
require 'uri'
require 'yaml'

ROOT = __dir__
ANNOTATIONS = File.join(
  ROOT,
  '../../worktrees/2026-07-12-vpsadmin-kb-contract/vpsadmin-kb-captures/contract/kb-annotations.yml'
)
SITES = {
  'cs' => 'http://kb-cs.aitherdev.int.vpsfree.cz',
  'en' => 'http://kb-en.aitherdev.int.vpsfree.cz'
}.freeze

contract = YAML.safe_load_file(ANNOTATIONS)
bindings = contract.fetch('bindings')
pages = bindings.group_by { |binding| binding.values_at('language', 'page') }

pages.each do |(language, page_id), expected|
  path = page_id.split(':').map { |part| URI.encode_uri_component(part) }.join('/')
  uri = URI("#{SITES.fetch(language)}/#{path}")
  response = Net::HTTP.get_response(uri)
  raise "#{language}:#{page_id}: HTTP #{response.code}" unless response.is_a?(Net::HTTPSuccess)
  raise "#{language}:#{page_id}: invalid annotation warning rendered" if response.body.include?('vpsadmindoc-nav--invalid')

  expected.each do |binding|
    path_id = binding.fetch('path')
    pattern = /data-vpsadmin-doc-id="#{Regexp.escape(path_id)}"/
    actual = response.body.scan(pattern).length
    unless actual == binding.fetch('count')
      raise "#{language}:#{page_id}: #{path_id} expected #{binding.fetch('count')}, rendered #{actual}"
    end
  end
end

puts "Verified #{pages.length} staging pages and #{bindings.sum { |binding| binding.fetch('count') }} rendered annotations"
