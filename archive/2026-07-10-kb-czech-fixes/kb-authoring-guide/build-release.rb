#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'
require 'json'
require 'yaml'

root = __dir__
source_root = File.join(root, 'sources')
index = JSON.parse(File.read(File.join(source_root, 'index.json')))

releases = {
  'cs' => {
    wiki: 'cz',
    page: 'informace:jak_psat',
    preview: 'preview-cs.txt',
    summary: 'Doplnění pravidel pro dokumentaci vpsAdminu'
  },
  'en' => {
    wiki: 'org',
    page: 'information:kb',
    preview: 'preview-en.txt',
    summary: 'Expand the contribution guide and document the vpsAdmin workflow',
    counterpart: 'informace:jak_psat'
  }
}.freeze

releases.each do |language, release|
  source = index.fetch(language).find { |page| page.fetch('id') == release.fetch(:page) }
  abort "source page not found: #{language}:#{release.fetch(:page)}" unless source

  source_content = File.binread(File.join(source_root, source.fetch('file')))
  source_sha256 = Digest::SHA256.hexdigest(source_content)
  abort "source checksum drift: #{release.fetch(:page)}" unless source_sha256 == source.fetch('sha256')

  preview_path = File.join(root, release.fetch(:preview))
  preview = File.binread(preview_path)
  abort "empty preview: #{release.fetch(:page)}" if preview.empty?
  abort "unchanged preview: #{release.fetch(:page)}" if preview == source_content

  page = {
    'id' => release.fetch(:page),
    'source_revision' => source.fetch('revision'),
    'source_sha256' => source_sha256,
    'file' => release.fetch(:preview),
    'sha256' => Digest::SHA256.hexdigest(preview)
  }
  page['language_counterpart'] = release.fetch(:counterpart) if release[:counterpart]

  manifest = {
    'schema' => 2,
    'wiki' => release.fetch(:wiki),
    'production_summary' => release.fetch(:summary),
    'pages' => [page],
    'media' => []
  }
  output = File.join(root, "release-#{language}.yml")
  File.write(output, YAML.dump(manifest))
  puts "Prepared #{output}: #{release.fetch(:page)}"
end
