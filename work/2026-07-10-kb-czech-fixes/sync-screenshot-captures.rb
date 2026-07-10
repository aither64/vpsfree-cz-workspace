#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'yaml'

ROOT = File.expand_path(__dir__)
CAPTURE_REPOSITORY = File.expand_path(ARGV.fetch(0))
CAPTURE_MANIFEST = File.join(CAPTURE_REPOSITORY, 'captures.json')
KB_MANIFEST = File.join(ROOT, 'screenshot-manifest.yml')

captures = JSON.parse(File.read(CAPTURE_MANIFEST)).fetch('assets')
by_legacy_media = captures.to_h { |asset| [asset.dig('legacy', 'media_id'), asset] }
manifest = YAML.safe_load_file(KB_MANIFEST)

manifest.fetch('assets').each do |asset|
  capture = by_legacy_media.fetch(asset.fetch('legacy_media'))
  unless capture.dig('wiki', 'draft_media_id') == asset.fetch('draft_media')
    raise "Draft media mismatch for #{asset.fetch('legacy_media')}"
  end
  unless capture.fetch('output') == asset.fetch('local_file')
    raise "Local output mismatch for #{asset.fetch('legacy_media')}"
  end

  source = File.join(CAPTURE_REPOSITORY, capture.fetch('output'))
  target = File.join(ROOT, asset.fetch('local_file'))
  FileUtils.mkdir_p(File.dirname(target))
  FileUtils.cp(source, target)

  asset['capture'] = capture.fetch('capture')
  asset['dimensions'] = capture.fetch('dimensions')
  asset['sha256'] = capture.fetch('sha256')
  asset['review_status'] = capture.fetch('review_status')
end

unexpected = by_legacy_media.keys - manifest.fetch('assets').map { |asset| asset.fetch('legacy_media') }
raise "Capture assets missing from KB manifest: #{unexpected.join(', ')}" unless unexpected.empty?

File.write(KB_MANIFEST, YAML.dump(manifest))
warn "Synchronized #{captures.length} capture assets"
