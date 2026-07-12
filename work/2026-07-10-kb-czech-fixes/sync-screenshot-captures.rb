#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'open3'
require 'yaml'

ROOT = File.expand_path(__dir__)
CAPTURE_REPOSITORY = File.expand_path(ARGV.fetch(0))
LANGUAGE = ARGV.fetch(1, 'cs')
CAPTURE_MANIFEST = File.join(CAPTURE_REPOSITORY, 'captures.json')
KB_MANIFEST = File.join(
  ROOT,
  LANGUAGE == 'cs' ? 'screenshot-manifest.yml' : "screenshot-manifest-#{LANGUAGE}.yml"
)

abort 'language must be cs or en' unless %w[cs en].include?(LANGUAGE)

inventory = JSON.parse(File.read(CAPTURE_MANIFEST))
raise 'capture schema 5 is required' unless inventory.fetch('schema') == 5

assets = inventory.fetch('assets').map do |capture|
  variant = capture.fetch('variants').fetch(LANGUAGE)

  source = File.join(CAPTURE_REPOSITORY, variant.fetch('output'))
  local_file = variant.fetch('output')
  target = File.join(ROOT, local_file)
  FileUtils.mkdir_p(File.dirname(target))
  FileUtils.cp(source, target)

  {
    'id' => capture.fetch('id'),
    'legacy_media' => variant.dig('legacy', 'media_id'),
    'legacy_media_aliases' => variant.fetch('legacy_aliases', []).map do |legacy|
      legacy.fetch('media_id')
    end,
    'media_id' => variant.dig('wiki', 'media_id'),
    'source_pages' => variant.dig('wiki', 'source_pages'),
    'local_file' => local_file,
    'sha256' => variant.fetch('sha256'),
    'dimensions' => variant.fetch('dimensions'),
    'capture' => variant.fetch('capture'),
    'review_status' => variant.fetch('review_status')
  }
end

raise "expected 59 captures, got #{assets.length}" unless assets.length == 59

expected_files = assets.map { |asset| File.join(ROOT, asset.fetch('local_file')) }
Dir.glob(File.join(ROOT, 'screenshots', LANGUAGE, '**', '*.png')).each do |file|
  FileUtils.rm(file) unless expected_files.include?(file)
end

capture_commit, status = Open3.capture2('git', '-C', CAPTURE_REPOSITORY, 'rev-parse', 'HEAD')
raise 'unable to read capture repository revision' unless status.success?

manifest = {
  'schema' => 5,
  'wiki' => LANGUAGE == 'cs' ? 'cz' : 'org',
  'capture_repository' => 'git@github.com:vpsfreecz/vpsadmin-kb-captures.git',
  'capture_commit' => capture_commit.strip,
  'assets' => assets
}

File.write(KB_MANIFEST, YAML.dump(manifest))
warn "Synchronized #{assets.length} capture assets"
