require 'digest'
require 'json'
require 'open3'
root = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
Dir.chdir('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories')
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'frozen evidence digest mismatch' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
ids = JSON.parse(File.read("#{root}/assessment/packages.json")).fetch('groups').fetch('implementer0')
ids -= ['CVE-2026-74753'] if ARGV.include?('--skip-held-74753')
Dir.mkdir('.state/implementer0') unless Dir.exist?('.state/implementer0')
File.chmod(0o700, '.state/implementer0')
rows = ids.map do |cve|
  output = ".state/implementer0/#{cve}.evaluate.log"
  ok = File.open(output, File::WRONLY | File::CREAT | File::TRUNC, 0o600) do |f|
    system('bin/security-advisory', 'evaluate', cve, out: f, err: f)
  end
  raise "evaluation failed for #{cve}; see restricted #{output}" unless ok
  doc = JSON.parse(File.read("advisories/#{cve}/evaluation.json"))
  { 'cve' => cve, 'schema_version' => doc.fetch('schema_version'),
    'completeness' => doc.fetch('completeness'),
    'states' => doc.fetch('nodes').map { |n| n.slice('node_id', 'node_role', 'state', 'reason', 'kernel_release', 'affected_since', 'mitigated_since') } }
end
raise 'shared snapshot changed during evaluation' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
File.write("#{root}/assessment/implementer0/evaluation-summary#{ARGV.include?('--skip-held-74753') ? '-19' : ''}.json", JSON.pretty_generate({ 'evidence_sha256' => expected, 'rows' => rows }) + "\n")
rows.each { |r| puts "#{r['cve']} #{r['completeness']['states']}" }
