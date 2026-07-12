#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'
require 'fileutils'
require 'json'
require 'yaml'

ROOT = File.expand_path('../..', __dir__)
CAPTURE_ROOT = File.join(
  ROOT,
  'worktrees/2026-07-12-vpsadmin-kb-contract/vpsadmin-kb-captures'
)
CONTRACT = File.join(CAPTURE_ROOT, 'contract/navigation.yml')
OUTPUT = File.join(__dir__, 'kb-sources')
WIKIS = { 'cs' => 'cz', 'en' => 'org' }.freeze

load File.join(ROOT, 'bin/kb-page')

contract = YAML.safe_load_file(CONTRACT)
index = {}

WIKIS.each do |language, wiki|
  wiki_config = KbPage.wiki_config(wiki)
  client = KbPage::JsonRpcClient.new(
    base_url: wiki_config.fetch(:url),
    token_path: wiki_config.fetch(:token_path)
  )
  page_ids = contract.fetch('paths').flat_map do |path|
    path.fetch('pages').fetch(language)
  end.uniq.sort

  index[language] = page_ids.map do |page_id|
    info = client.call('core.getPageInfo', page: page_id)
    output = client.call('core.getPage', page: page_id)
    revision = info['revision'] || info['rev'] || info['lastModified']
    raise "#{wiki}:#{page_id}: source revision is missing" unless revision

    relative = File.join(language, *page_id.split(':')) + '.txt'
    destination = File.join(OUTPUT, relative)
    FileUtils.mkdir_p(File.dirname(destination))
    File.write(destination, output)

    {
      'id' => page_id,
      'file' => relative,
      'revision' => revision,
      'sha256' => Digest::SHA256.hexdigest(output)
    }
  end
end

FileUtils.mkdir_p(OUTPUT)
File.write(File.join(OUTPUT, 'index.json'), "#{JSON.pretty_generate(index)}\n")
puts "Fetched #{index.fetch('cs').length} Czech and #{index.fetch('en').length} English pages"
