#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'
require 'fileutils'
require 'json'
require 'yaml'

ROOT = File.expand_path(__dir__)

metadata = JSON.parse(
  File.read(File.join(ROOT, 'kb-source-en', 'page-metadata.json'))
)
inventory = YAML.safe_load_file(File.join(ROOT, 'screenshot-manifest-en.yml'))
abort 'English screenshot manifest is required' unless inventory.fetch('wiki') == 'org'

media_by_page = Hash.new { |hash, key| hash[key] = [] }
inventory.fetch('assets').each do |asset|
  asset.fetch('source_pages').each { |page| media_by_page[page] << asset }
end

abort "expected 14 English pages, got #{media_by_page.length}" unless media_by_page.length == 14

counterparts = Dir.glob(File.join(ROOT, 'kb-candidates', '**', '*.txt')).filter_map do |path|
  content = File.read(path)
  english_id = content[/<page>\s*([^<]+?)\s*<\/page>/, 1]
  relative = path.delete_prefix("#{File.join(ROOT, 'kb-candidates')}/").delete_suffix('.txt')
  [english_id, relative.tr('/', ':')] if english_id
end.to_h

replacement_count = 0
pages = media_by_page.keys.sort.map do |page|
  source_path = File.join(ROOT, 'kb-source-en', *page.split(':')) + '.txt'
  source = File.read(source_path)
  candidate = source.dup

  media_by_page.fetch(page).each do |asset|
    legacy_ids = [asset.fetch('legacy_media'), *asset.fetch('legacy_media_aliases', [])].compact
    basenames = legacy_ids.map { |legacy| legacy.split(':').last }
    replaced = 0

    candidate = candidate.gsub(/\{\{[^}]+\}\}/) do |media_ref|
      target = media_ref[/\{\{\s*([^?\s|}]+)/, 1]
      next media_ref unless target

      normalized = target.delete_prefix(':')
      next media_ref unless legacy_ids.include?(normalized) || basenames.include?(normalized)

      replaced += 1
      media_ref.sub(target, ":#{asset.fetch('media_id')}")
    end

    unless replaced == 1
      abort "#{page}: expected one reference to #{legacy_ids.join(', ')}, got #{replaced}"
    end
    replacement_count += replaced
  end

  unexpected_changes = candidate.lines.zip(source.lines).count do |new_line, old_line|
    next false if new_line == old_line

    old_without_media = old_line&.gsub(/\{\{[^}]+\}\}/, '{{MEDIA}}')
    new_without_media = new_line&.gsub(/\{\{[^}]+\}\}/, '{{MEDIA}}')
    old_without_media != new_without_media
  end
  abort "#{page}: changes extend beyond media references" unless unexpected_changes.zero?

  preview_path = File.join(ROOT, 'kb-candidates-en', *page.split(':')) + '.txt'
  FileUtils.mkdir_p(File.dirname(preview_path))
  File.write(preview_path, candidate)

  info = metadata.fetch(page)
  revision = info['revision'] || info['rev'] || info['lastModified']
  abort "#{page}: source revision is missing" unless revision

  {
    'id' => page,
    'source_revision' => revision,
    'source_sha256' => Digest::SHA256.file(source_path).hexdigest,
    'file' => preview_path.delete_prefix("#{ROOT}/"),
    'sha256' => Digest::SHA256.file(preview_path).hexdigest,
    'screenshot_count' => media_by_page.fetch(page).length,
    'language_counterpart' => counterparts.fetch(page)
  }
end

abort "expected 54 English media replacements, got #{replacement_count}" unless replacement_count == 54

media = inventory.fetch('assets').map do |asset|
  {
    'id' => asset.fetch('media_id'),
    'file' => asset.fetch('local_file'),
    'sha256' => asset.fetch('sha256'),
    'policy' => 'create'
  }
end

abort "expected 59 English media objects, got #{media.length}" unless media.length == 59

release = {
  'schema' => 2,
  'wiki' => 'org',
  'production_summary' => 'Replace outdated vpsAdmin screenshots',
  'pages' => pages,
  'media' => media
}
File.write(File.join(ROOT, 'kb-release-en.yml'), YAML.dump(release))

puts "wrote English release with #{pages.length} pages and #{media.length} media objects"
