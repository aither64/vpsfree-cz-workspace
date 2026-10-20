#!/usr/bin/env ruby
require 'json'
require 'time'
require 'digest'
base=File.expand_path('../..',__dir__)
pkg=JSON.parse(File.read(File.join(base,'assessment/packages.json')))
approved=JSON.parse(File.read(File.join(base,'approved-cves.json'))).fetch('cves')
errors=[]; roots={}; rows=[]; hashes={}
pkg.fetch('groups').each do |owner,ids|
 path=File.join(base,'assessment',owner,'requirements.json')
 x=JSON.parse(File.read(path));hashes[owner]=Digest::SHA256.file(path).hexdigest
 roots[owner]=x.is_a?(Array) ? 'array' : x.is_a?(Hash) && x['rows'].is_a?(Array) ? 'object.rows' : 'unsupported'
 rr=case roots[owner];when 'array' then x;when 'object.rows' then x.fetch('rows');else errors<<{'owner'=>owner,'root'=>'unsupported'};next;end
 actual=rr.filter_map { |r| r['cve'] if r.is_a?(Hash) }
 errors<<{'owner'=>owner,'ownership'=>'missing/extra/duplicate/nonobject rows'} unless actual.sort==ids.sort && actual.uniq.length==rr.length
 rr.each do |r|
  unless r.is_a?(Hash);errors<<{'owner'=>owner,'row'=>'not object'};next;end
  c=r['cve'];fields=%w[cve required_options required_sysctls history_required_since affected_node_roles source_prerequisites unmodeled_prerequisites]
  fields.each { |k| errors<<{'cve'=>c,'missing'=>k} unless r.key?(k) }
  options=r['required_options']; sysctls=r['required_sysctls']
  errors<<{'cve'=>c,'shape'=>'required_options'} unless options.is_a?(Hash) && options.all? { |k,v| k.match?(/\ACONFIG_[A-Z0-9_]+\z/) && %w[enabled disabled y m n].include?(v) }
  errors<<{'cve'=>c,'shape'=>'required_sysctls'} unless sysctls.is_a?(Hash) && sysctls.all? { |k,v| k.match?(/\A[a-zA-Z0-9_.-]+\z/) && v.is_a?(Array) && !v.empty? && v.all? { |a| a.is_a?(String) } && v.uniq.length==v.length }
  %w[affected_node_roles source_prerequisites unmodeled_prerequisites].each { |k| errors<<{'cve'=>c,'shape'=>k} unless r[k].is_a?(Array) && r[k].all? { |v| v.is_a?(String) } }
  begin;Time.iso8601(r.fetch('history_required_since'));rescue ArgumentError,TypeError,KeyError;errors<<{'cve'=>c,'shape'=>'history_required_since'};end
  rows<<r.merge('_owner'=>owner)
 end
end
actual=rows.map { |r| r['cve'] }
errors<<{'partition'=>'not exactapproved60 once'} unless actual.sort==approved.sort && actual.uniq.length==60
options={};sysctls={}
rows.each do |r|
 (r['required_options']||{}).each { |k,v| (options[k]||=[])<<{'cve'=>r['cve'],'owner'=>r['_owner'],'value'=>v} }
 (r['required_sysctls']||{}).each { |k,v| (sysctls[k]||=[])<<{'cve'=>r['cve'],'owner'=>r['_owner'],'accepted_values'=>v} }
end
result={'mode'=>'ledgers_only','root_containers'=>roots,'rows'=>rows.length,'owner_counts'=>rows.group_by { |r| r['_owner'] }.transform_values(&:length),'errors'=>errors,'ledger_sha256'=>hashes,'option_names'=>options.keys.sort,'option_requirements'=>options.sort.to_h,'sysctl_names'=>sysctls.keys.sort,'sysctl_requirements'=>sysctls.sort.to_h,'earliest_history_required_since'=>rows.filter_map { |r| Time.iso8601(r['history_required_since']) rescue nil }.min&.utc&.iso8601,'history_scopes'=>rows.group_by { |r| r['history_required_since'] }.transform_values { |rs| rs.map { |r| r['cve'] } },'actual_declarations_gate'=>'pending; not checked in this ledger-only pass','collection_released'=>false,'limits'=>'Structural and ownership check only. Different values retained per CVE; architect reconciles semantics and source citations. No API, runtime classification or Node collection.'}
File.write(File.join(__dir__,'ledger-union-result.json'),JSON.pretty_generate(result)+"\n")
puts JSON.generate(result.reject { |k,_| %w[option_requirements sysctl_requirements history_scopes].include?(k) })
