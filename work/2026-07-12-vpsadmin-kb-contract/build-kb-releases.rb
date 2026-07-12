#!/usr/bin/env ruby
# frozen_string_literal: true

require 'json'
require 'yaml'

ROOT = __dir__
source_index = JSON.parse(File.read(File.join(ROOT, 'kb-sources/index.json')))
candidate_index = JSON.parse(File.read(File.join(ROOT, 'kb-candidates/index.json')))
source_by_key = source_index.flat_map do |language, pages|
  pages.map { |page| [[language, page.fetch('id')], page] }
end.to_h

czech_counterparts = candidate_index.fetch('pages').filter_map do |page|
  next unless page.fetch('language') == 'cs'

  content = File.read(File.join(ROOT, 'kb-candidates', page.fetch('file')))
  english_id = content[/<page>\s*([^<]+?)\s*<\/page>/, 1]
  [english_id, page.fetch('id')] if english_id
end.to_h

settings = {
  'cs' => {
    'wiki' => 'cz',
    'summary' => 'Označení navigačních cest a aktualizace názvů ve vpsAdminu'
  },
  'en' => {
    'wiki' => 'org',
    'summary' => 'Annotate vpsAdmin navigation paths and update interface labels'
  }
}

settings.each do |language, setting|
  pages = candidate_index.fetch('pages').select do |page|
    page.fetch('language') == language && page.fetch('changed')
  end.map do |page|
    source = source_by_key.fetch([language, page.fetch('id')])
    entry = {
      'id' => page.fetch('id'),
      'source_revision' => source.fetch('revision'),
      'source_sha256' => source.fetch('sha256'),
      'file' => File.join('kb-candidates', page.fetch('file')),
      'sha256' => page.fetch('candidate_sha256')
    }
    if language == 'en'
      entry['language_counterpart'] = czech_counterparts.fetch(page.fetch('id'))
    end
    entry
  end

  release = {
    'schema' => 2,
    'wiki' => setting.fetch('wiki'),
    'production_summary' => setting.fetch('summary'),
    'pages' => pages,
    'media' => []
  }
  output = File.join(ROOT, "kb-release-#{language}.yml")
  File.write(output, YAML.dump(release))
  puts "Prepared #{output} with #{pages.length} pages"
end
