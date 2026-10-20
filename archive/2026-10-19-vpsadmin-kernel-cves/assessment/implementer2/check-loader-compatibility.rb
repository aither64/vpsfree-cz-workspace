require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'digest'
root = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/spec/fixtures'
path = File.join(__dir__, 'advisory-schema1-loader.rb')
old_source = File.read(path)
eval(old_source.sub('class Advisory', 'class RetainedSchema1Advisory'), TOPLEVEL_BINDING, path)
base = SecurityAdvisories::Advisory.load('CVE-2026-46242', root:)
SecurityAdvisories::RetainedSchema1Advisory.new(base.data, directory: base.directory).validate!
base.data['schema_version'] = 2
base.platform['affected_livepatches'] = []
base.validate!
rejection = begin
  SecurityAdvisories::RetainedSchema1Advisory.new(base.data, directory: base.directory).validate!
  raise 'Retained old loader accepted schema2 unexpectedly'
rescue SecurityAdvisories::Error => e
  raise unless e.message.include?('schema_version must be 1')
  'schema_version must be 1'
end
receipt = {
  old_loader_revision: '69027fd51efc5c7eb0a4711947b4f9d08190940e',
  old_loader_sha256: Digest::SHA256.file(path).hexdigest,
  schema1_old_and_new_loader: 'PASS', schema2_new_loader: 'PASS',
  schema2_old_loader_rejection: rejection,
  limits: 'Exact retained loader copied read-only; only class name isolated to run alongside current loader. No Git state or production evidence mutated.'
}
File.write(File.join(__dir__, 'loader-compatibility.json'), JSON.pretty_generate(receipt) + "\n")
puts JSON.pretty_generate(receipt)
