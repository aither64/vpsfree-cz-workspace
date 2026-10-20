#!/usr/bin/env ruby
# Offline snapshot/source consistency only; run after lead final-freeze notification.
require 'json'
require 'digest'
require 'stringio'
base=File.expand_path('../..',__dir__)
repo=JSON.parse(File.read(File.join(base,'assessment/packages.json'))).fetch('worktree')
require File.join(repo,'lib/security_advisories')
class NoNetworkClient
  def method_missing(*) = raise('network prohibited in mechanical acceptance')
  def respond_to_missing?(*) = true
end
approved=JSON.parse(File.read(File.join(base,'approved-cves.json'))).fetch('cves')
selection=JSON.parse(File.read(File.join(base,'research/member-selection.json'))).fetch('entries').to_h { |r| [r.fetch('cve'),r] }
dedup=File.read(File.join(base,'research/platform-evidence/dedup-cves.txt')).scan(/CVE-\d{4}-\d+/)
evidence_path=File.join(repo,'.state/evidence.json')
sha=Digest::SHA256.file(evidence_path).hexdigest
raise 'unexpected frozen snapshot SHA' unless sha=='61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
evidence=JSON.parse(File.read(evidence_path))
reconciler=SecurityAdvisories::Reconciler.new(client: NoNetworkClient.new,root:repo,output:StringIO.new)
errors=[];rows=[]
errors << 'approved ID set is not60unique' unless approved.length==60 && approved.uniq.length==60
errors << 'frozen snapshot node count is not13' unless evidence.fetch('nodes').length==13
approved.each do |c|
 begin
  a=SecurityAdvisories::Advisory.load(c,root:repo)
  ev=reconciler.load_evaluation(a) # existing validation checks schema4, CVE, dossier digest and completeness presence
  checks={'snapshot_evidence_digest'=>ev['evidence_digest']==evidence['evidence_digest'],'snapshot_node_set_digest'=>ev['node_set_digest']==evidence['node_set_digest'],'snapshot_collected_at'=>ev['collected_at']==evidence['collected_at'],'node_count13'=>ev.fetch('nodes').length==13,'exact_node_ids'=>ev['nodes'].map { |n| n['node_id'] }.sort==evidence['nodes'].map { |n| n['node_id'] }.sort,'public_dedup'=>!dedup.include?(c)}
  counts=ev['nodes'].group_by { |n| n.fetch('state') }.transform_values(&:length)
  summary=ev.fetch('completeness')
  ids=ev['nodes'].map { |n| n.fetch('node_id') }
  blocking=ev['nodes'].filter_map { |n| n['node_id'] unless %w[mitigated not_affected].include?(n['state']) }
  checks['declared_states']=summary.fetch('states')==counts
  checks['declared_expected_count']=summary.fetch('expected_node_count')==evidence['nodes'].length
  checks['declared_evaluated_count']=summary.fetch('evaluated_node_count')==ev['nodes'].length
  checks['declared_node_set_complete']=summary.fetch('node_set_complete')==(ids.length==evidence['nodes'].length && ids.uniq.length==ids.length)
  checks['declared_resolution_complete']=summary.fetch('resolution_complete')==blocking.empty?
  checks['declared_blocking_ids']=summary.fetch('blocking_node_ids').sort==blocking.sort
  texts=a.data.fetch('texts');checks['localized_presence']=%w[en cs].all? { |l| %w[summary description response].all? { |k| !texts.dig(l,k).to_s.strip.empty? } }
  rule=a.data.fetch('version_rules').fetch('6.12')
  if c=='CVE-2026-64387'
   exception=JSON.parse(File.read(File.join(base,'assessment/CVE-2026-64387-correction.json')))
   checks['documented_effective_64387']=rule['fixed_in']==exception.fetch('accepted_effective_boundaries').fetch('6.12') && a.data['fixed_from']==exception.fetch('accepted_effective_boundaries').fetch('mainline')
  else
   source=selection.fetch(c)
   checks['primary_6_12_fix_version']=rule['fixed_in']==source['first_fix_release']
   checks['primary_6_12_fix_sha']=rule['fixed_commit']==source['stable_fix_sha']
  end
  checks['74753_canonical_stable_bounds']=rule['affected_from']=='6.12.96' && rule['fixed_in']=='6.12.108' if c=='CVE-2026-74753'
  errors.concat(checks.reject { |_,v| v }.keys.map { |k| {'cve'=>c,'check'=>k} })
  rows<<{'cve'=>c,'schema_version'=>a.data['schema_version'],'dossier_digest'=>a.digest,'evaluation_file_sha256'=>Digest::SHA256.file(File.join(a.directory,'evaluation.json')).hexdigest,'state_counts'=>counts,'declared_completeness'=>ev['completeness'].reject { |k,_| k.include?('node') || k.include?('ids') },'checks'=>checks}
 rescue StandardError => e
  # Restrict diagnostics: no raw evaluation content or Node linkage in session output.
  errors<<{'cve'=>c,'validation_error_class'=>e.class.name,'validation_failed'=>true}
 end
end
result={'snapshot_sha256'=>sha,'evidence_digest'=>evidence['evidence_digest'],'node_set_digest'=>evidence['node_set_digest'],'approved_count'=>approved.length,'loaded_evaluation_count'=>rows.length,'schema_counts'=>rows.group_by { |r| r['schema_version'] }.transform_values(&:length),'errors'=>errors,'rows'=>rows,'limits'=>'Offline exact source/snapshot consistency only, not independent review, security correctness, editorial review, API duplicate refresh or publication readiness. No evaluation execution/edit, collection or remote writes.'}
File.write(File.join(__dir__,'final-acceptance-result.json'),JSON.pretty_generate(result)+"\n")
puts JSON.generate(result.reject { |k,_| k=='rows' })
