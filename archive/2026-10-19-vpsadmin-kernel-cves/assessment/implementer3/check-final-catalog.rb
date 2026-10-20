require 'json'
require 'digest'
base=File.expand_path('../..',__dir__)
repo=JSON.parse(File.read(File.join(base,'assessment/packages.json'))).fetch('worktree')
require File.join(repo,'lib/security_advisories')
rows=Dir.glob(File.join(repo,'advisories','CVE-*','advisory.yml')).sort.map do |p|
 a=SecurityAdvisories::Advisory.load(File.basename(File.dirname(p)),root:repo)
 {'cve'=>a.cve,'schema'=>a.data.fetch('schema_version'),'dossier_digest'=>a.digest}
end
raise 'unexpected catalog count' unless rows.length==111
raise 'unexpected schema2 set' unless rows.select { |r| r['schema']==2 }.map { |r| r['cve'] }==['CVE-2026-74753']
p=File.join(__dir__,'final-acceptance-result.json');x=JSON.parse(File.read(p));x['all_dossiers_loaded']=rows.length;x['all_dossier_schema_counts']=rows.group_by { |r| r['schema'] }.transform_values(&:length);x['all_dossier_catalog_sha256']=Digest::SHA256.hexdigest(JSON.generate(rows));x['frozen_head']=IO.popen(['git','-C',repo,'rev-parse','HEAD'], &:read).strip;File.write(p,JSON.pretty_generate(x)+"\n");puts JSON.generate(x.slice('all_dossiers_loaded','all_dossier_schema_counts','all_dossier_catalog_sha256','errors'))
