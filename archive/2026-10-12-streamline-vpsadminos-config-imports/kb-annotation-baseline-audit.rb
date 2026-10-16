require 'json'
require 'yaml'
require 'open3'
require 'digest'
require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsfree-kb-contracts/tools/kb_navigation_discovery'

SESSION = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports'
BASE = 'ce2c8cd9358c3636e5d39343e595df813a0b197f'
TAG = /<vpsadmin-nav\s+id="([a-z][a-z0-9.-]*)">(.*?)<\/vpsadmin-nav>/m

def git_yaml(path)
  text, status = Open3.capture2('git', 'show', "#{BASE}:#{path}")
  raise 'git source read failed' unless status.success?
  YAML.safe_load(text)
end

def counts(pages, root)
  actual = Hash.new(0)
  pages.each do |page|
    semantic = KbNavigationDiscovery.semantic_content(File.read("#{root}/#{page.fetch('file')}"))
    tags = semantic.scan(TAG)
    raise 'malformed annotation tags' unless semantic.scan('<vpsadmin-nav').length == tags.length && semantic.scan('</vpsadmin-nav>').length == tags.length
    tags.each do |path, body|
      raise 'empty annotation tag' if body.strip.empty?
      actual[[page.fetch('language'), page.fetch('id'), path]] += 1
    end
  end
  actual
end

def count_drift(actual, annotations)
  expected = annotations.fetch('bindings').to_h { |entry| [entry.values_at('language', 'page', 'path'), entry.fetch('count')] }
  (expected.keys | actual.keys).sort.filter_map do |key|
    next if expected.fetch(key, 0) == actual.fetch(key, 0)
    { key: key, expected: expected.fetch(key, 0), actual: actual.fetch(key, 0) }
  end
end

def inventory_drift(pages, root, inventory)
  discoveries = pages.flat_map do |page|
    KbNavigationDiscovery.discover(language: page.fetch('language'), page: page.fetch('id'), content: File.read("#{root}/#{page.fetch('file')}"))
  end
  actual = discoveries.to_h { |entry| [entry.fetch('id'), entry] }
  expected = inventory.fetch('discoveries').to_h { |entry| [entry.fetch('id'), entry] }
  issues = []
  (actual.keys - expected.keys).sort.each { |id| issues << { kind: 'unclassified', actual: actual.fetch(id) } }
  (expected.keys - actual.keys).sort.each { |id| issues << { kind: 'stale', expected: expected.fetch(id) } }
  (actual.keys & expected.keys).sort.each do |id|
    a = actual.fetch(id); e = expected.fetch(id)
    next if a.values_at('language', 'page', 'paragraph', 'text') == e.values_at('language', 'page', 'paragraph', 'text') &&
      (e.key?('reason') ? a.fetch('paths', []).empty? && !e.fetch('reason').strip.empty? : a.fetch('paths', []).sort == e.fetch('paths', []).sort && !e.fetch('paths', []).empty?)
    issues << { kind: 'content_or_classification_drift', actual: a, expected: e }
  end
  { discoveries: discoveries.length, issues: issues }
end

source_index = JSON.parse(File.read("#{SESSION}/kb-source/index.json"))
source_pages = source_index.flat_map { |language, entries| entries.map { |entry| entry.merge('language' => language) } }
corpus_pages = JSON.parse(File.read("#{SESSION}/kb-annotation-corpus/index.json")).fetch('pages')
candidate_pages = JSON.parse(File.read("#{SESSION}/kb-candidate/index.json")).fetch('pages')
changed_keys = candidate_pages.map { |entry| entry.values_at('language', 'id') }
current_annotations = YAML.safe_load_file('contract/kb-annotations.yml')
current_inventory = YAML.safe_load_file('contract/kb-navigation-inventory.yml')
baseline_annotations = git_yaml('contract/kb-annotations.yml')
baseline_inventory = git_yaml('contract/kb-navigation-inventory.yml')
baseline_counts = counts(source_pages, "#{SESSION}/kb-source")
final_counts = counts(corpus_pages, "#{SESSION}/kb-annotation-corpus")
expected_ids = current_inventory.fetch('page_ids').flat_map { |language, ids| ids.map { |id| [language, id] } }.sort
raise 'full identity sets differ' unless [source_pages, corpus_pages].all? { |pages| pages.map { |p| p.values_at('language', 'id') }.sort == expected_ids }
raise 'duplicate page identity' unless source_pages.map { |p| p.values_at('language', 'id') }.uniq.length == 191 && corpus_pages.map { |p| p.values_at('language', 'id') }.uniq.length == 191
raise 'duplicate page file' unless [source_pages, corpus_pages].all? { |pages| pages.map { |p| p.fetch('file') }.uniq.length == 191 }
corpus_pages.each do |p|
  original = if changed_keys.include?(p.values_at('language', 'id'))
    candidate = candidate_pages.find { |q| q.values_at('language', 'id') == p.values_at('language', 'id') }
    "#{SESSION}/kb-candidate/#{candidate.fetch('file')}"
  else
    "#{SESSION}/kb-source/#{p.fetch('file')}"
  end
  raise 'corpus content mismatch' unless File.binread(original) == File.binread("#{SESSION}/kb-annotation-corpus/#{p.fetch('file')}")
end
changed_expectations = current_annotations.fetch('bindings').select { |b| changed_keys.include?(b.values_at('language', 'page')) }
changed_actual = final_counts.select { |key, _| changed_keys.include?(key.take(2)) }
evidence = {
  baseline_commit: BASE,
  source_pages: source_pages.group_by { |p| p.fetch('language') }.transform_values(&:length),
  full_corpus_identities_and_scoped_overrides: true,
  baseline_count_drift: count_drift(baseline_counts, baseline_annotations),
  final_count_drift: count_drift(final_counts, current_annotations),
  six_candidate_count_drift: count_drift(changed_actual, { 'bindings' => changed_expectations }),
  six_candidate_counts: changed_keys.sort.map { |key| { page: key, actual: changed_actual.filter_map { |k, count| { path: k.last, count: count } if k.take(2) == key }.sort_by { |e| e.fetch(:path) } } },
  baseline_inventory: inventory_drift(source_pages, "#{SESSION}/kb-source", baseline_inventory),
  final_inventory: inventory_drift(corpus_pages, "#{SESSION}/kb-annotation-corpus", current_inventory)
}
File.write("#{SESSION}/kb-annotation-baseline-evidence.json", JSON.pretty_generate(evidence) + "\n")
puts JSON.pretty_generate(evidence.reject { |k, _| [:baseline_inventory, :final_inventory, :six_candidate_counts].include?(k) }.merge(
  baseline_discovery_issues: evidence.fetch(:baseline_inventory).fetch(:issues).length,
  final_discovery_issues: evidence.fetch(:final_inventory).fetch(:issues).length,
  final_candidate_discovery_issues: evidence.fetch(:final_inventory).fetch(:issues).count { |issue| changed_keys.include?((issue[:actual] || issue[:expected]).values_at('language', 'page')) }
))
