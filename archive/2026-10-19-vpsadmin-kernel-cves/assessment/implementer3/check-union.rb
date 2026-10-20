#!/usr/bin/env ruby
# Read-only offline declaration check; never collects production evidence.
require 'json'
require 'digest'
require 'time'
base = File.expand_path('../..', __dir__)
package_path = File.join(base,'assessment/packages.json')
packages = JSON.parse(File.read(package_path))
approved = JSON.parse(File.read(File.join(base,'approved-cves.json'))).fetch('cves')
groups = packages.fetch('groups')
assigned = groups.values.flatten
errors = []
errors << {'partition'=>'IDs differ or duplicate'} unless assigned.sort == approved.sort && assigned.uniq.length == 60 && approved.uniq.length == 60
result = {'approved_count'=>approved.length,'assigned_count'=>assigned.length,'owner_counts'=>groups.transform_values(&:length),'errors'=>errors,'mode'=>ARGV.include?('--partition-only') ? 'partition_only' : 'declarations','limits'=>'Mechanical comparison only; no inferred requirements, security classification, runtime collection or union acceptance. Architect owns acceptance.'}
unless ARGV.include?('--partition-only')
  repo = packages.fetch('worktree')
  require File.join(repo,'lib/security_advisories')
  rows = {}; missing = []; ledger_hashes = {}
  groups.each do |owner, ids|
    path = File.join(base,'assessment',owner,'requirements.json')
    unless File.file?(path)
      missing << path.delete_prefix(base+'/'); next
    end
    ledger_hashes[owner] = Digest::SHA256.file(path).hexdigest
    document = JSON.parse(File.read(path))
    ledger_rows = if document.is_a?(Array)
                    document
                  elsif document.is_a?(Hash) && document['rows'].is_a?(Array)
                    document.fetch('rows')
                  else
                    errors << {'owner'=>owner,'unsupported_ledger_container'=>true}
                    next
                  end
    actual = ledger_rows.map { |r| r.fetch('cve') }
    errors << {'owner'=>owner,'ledger_ownership'=>'missing, extra or duplicate IDs'} unless actual.sort == ids.sort && actual.uniq.length == actual.length
    ledger_rows.each do |r|
      c = r.fetch('cve'); errors << {'cve'=>c,'duplicate_ledger'=>true} if rows.key?(c)
      rows[c] = r
      %w[required_options required_sysctls history_required_since affected_node_roles source_prerequisites unmodeled_prerequisites].each do |k|
        errors << {'cve'=>c,'missing_ledger_field'=>k} unless r.key?(k)
      end
    end
  end
  declarations = {}; invalid = []; dossier_hashes = {}
  Dir.glob(File.join(repo,'advisories','CVE-*','advisory.yml')).sort.each do |path|
    c = File.basename(File.dirname(path))
    begin
      advisory = SecurityAdvisories::Advisory.load(c, root: repo)
      advisory.validate!
      declarations[c] = advisory.platform.slice('required_options','required_sysctls','history_required_since','affected_node_roles')
      dossier_hashes[c] = Digest::SHA256.file(path).hexdigest
    rescue StandardError => e
      invalid << {'cve'=>c,'error'=>e.message}
    end
  end
  absent = approved - declarations.keys
  approved.each do |c|
    next unless rows[c] && declarations[c]
    declarations[c].each do |k,v|
      expected = rows[c][k]
      # Array order carries no meaning for roles or accepted sysctl values.
      normalize = lambda do |x|
        case x
        when Hash then x.transform_values { |v2| normalize.call(v2) }
        when Array then x.map { |v2| normalize.call(v2) }.sort_by(&:to_s)
        else x
        end
      end
      errors << {'cve'=>c,'declaration_mismatch'=>k,'ledger'=>expected,'dossier'=>v} unless normalize.call(expected) == normalize.call(v)
    end
  end
  options = declarations.values.flat_map { |r| r.fetch('required_options',{}).keys }.uniq.sort
  sysctls = declarations.values.flat_map { |r| r.fetch('required_sysctls',{}).keys }.uniq.sort
  history = declarations.values.filter_map { |r| Time.iso8601(r['history_required_since']) if r['history_required_since'] }.min&.utc&.iso8601
  result.merge!('missing_ledgers'=>missing,'missing_or_invalid_approved_declarations'=>absent,'invalid_dossiers_including_existing'=>invalid,'loaded_dossier_count'=>declarations.length,'approved_loaded_count'=>(approved & declarations.keys).length,'collector_all_dossiers_option_names'=>options,'all_dossiers_sysctl_names'=>sysctls,'collector_all_dossiers_history_required_since'=>history,'approved_declarations'=>declarations.select { |c,_| approved.include?(c) },'ledger_sha256'=>ledger_hashes,'dossier_sha256'=>dossier_hashes,'ready_for_architect_reconciliation'=>errors.empty? && missing.empty? && absent.empty? && invalid.empty?)
end
filename = result['mode']=='partition_only' ? 'partition-result.json' : 'union-result.json'
File.write(File.join(__dir__,filename),JSON.pretty_generate(result)+"\n")
puts JSON.generate(result.reject { |k,_| %w[approved_declarations dossier_sha256].include?(k) })
