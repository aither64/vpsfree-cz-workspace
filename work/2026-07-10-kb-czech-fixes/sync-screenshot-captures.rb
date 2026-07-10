#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'open3'
require 'yaml'

ROOT = File.expand_path(__dir__)
CAPTURE_REPOSITORY = File.expand_path(ARGV.fetch(0))
CAPTURE_MANIFEST = File.join(CAPTURE_REPOSITORY, 'captures.json')
KB_MANIFEST = File.join(ROOT, 'screenshot-manifest.yml')

inventory = JSON.parse(File.read(CAPTURE_MANIFEST))
raise 'capture schema 3 is required' unless inventory.fetch('schema') == 3

assets = inventory.fetch('assets').map do |capture|
  raise "only Czech captures are expected: #{capture.fetch('id')}" unless capture.fetch('language') == 'cs'

  source = File.join(CAPTURE_REPOSITORY, capture.fetch('output'))
  local_file = capture.fetch('output')
  target = File.join(ROOT, local_file)
  FileUtils.mkdir_p(File.dirname(target))
  FileUtils.cp(source, target)

  {
    'id' => capture.fetch('id'),
    'legacy_media' => capture.dig('legacy', 'media_id'),
    'media_id' => capture.dig('wiki', 'media_id'),
    'source_pages' => capture.dig('wiki', 'source_pages'),
    'local_file' => local_file,
    'sha256' => capture.fetch('sha256'),
    'dimensions' => capture.fetch('dimensions'),
    'capture' => capture.fetch('capture'),
    'review_status' => capture.fetch('review_status')
  }
end

raise "expected 60 captures, got #{assets.length}" unless assets.length == 60

capture_commit, status = Open3.capture2('git', '-C', CAPTURE_REPOSITORY, 'rev-parse', 'HEAD')
raise 'unable to read capture repository revision' unless status.success?

manifest = {
  'schema' => 3,
  'wiki' => 'cz',
  'capture_repository' => 'git@github.com:vpsfreecz/vpsadmin-kb-captures.git',
  'capture_commit' => capture_commit.strip,
  'assets' => assets
}

File.write(KB_MANIFEST, YAML.dump(manifest))
warn "Synchronized #{assets.length} capture assets"
