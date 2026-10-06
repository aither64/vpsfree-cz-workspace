#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'yaml'

load File.expand_path('../../bin/kb-page', __dir__)

ROOT = File.expand_path(__dir__)

inventory = YAML.safe_load_file(File.join(ROOT, 'screenshot-manifest-en.yml'))
abort 'English screenshot manifest is required' unless inventory.fetch('wiki') == 'org'

pages = inventory.fetch('assets').flat_map { |asset| asset.fetch('source_pages') }.uniq.sort
abort "expected 14 English pages, got #{pages.length}" unless pages.length == 14

wiki = KbPage.wiki_config('org')
client = KbPage::JsonRpcClient.new(
  base_url: wiki.fetch(:url),
  token_path: wiki.fetch(:token_path)
)

metadata = pages.to_h do |page|
  info = client.call('core.getPageInfo', page: page)
  source = client.call('core.getPage', page: page)
  source_path = File.join(ROOT, 'kb-source-en', *page.split(':')) + '.txt'
  FileUtils.mkdir_p(File.dirname(source_path))
  File.write(source_path, source)
  [page, info]
end

File.write(
  File.join(ROOT, 'kb-source-en', 'page-metadata.json'),
  "#{JSON.pretty_generate(metadata)}\n"
)

puts "fetched #{pages.length} English pages"
