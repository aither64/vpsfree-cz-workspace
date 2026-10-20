require 'json'
require 'digest'
require 'time'
require 'yaml'
repo = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories'
require File.join(repo, 'lib/security_advisories')
out = File.dirname(__FILE__)
begin
  token_path = ENV.fetch('VPSADMIN_TOKEN_FILE', SecurityAdvisories::Config.default_path)
  stat = File.stat(token_path)
  mode = stat.mode & 0777
  raise 'unsafe_token_permissions' unless mode & 0077 == 0 && stat.uid == Process.uid
  config = SecurityAdvisories::Config.load
  client = SecurityAdvisories::APIClient.new(api_url: config.api_url, token: config.token)
  pages = []
  lists = {}
  {'security_advisories' => 'security_advisory', 'security_advisory_cves' => 'security_advisory_cve'}.each do |resource, scope|
    cursor = nil
    rows = []
    loop do
      query = {'limit' => 100}
      query['from_id'] = cursor if cursor
      response = client.get(resource, scope => query)
      page = response.fetch('response').fetch(resource)
      raise 'invalid_page' unless page.is_a?(Array)
      pages << {'resource' => resource, 'from_id' => cursor, 'count' => page.length}
      raise 'pagination_repeated_ids' unless (rows.map { |r| r.fetch('id') } & page.map { |r| r.fetch('id') }).empty?
      rows.concat(page)
      break if page.empty?
      cursor = resource == 'security_advisories' ? page.map { |r| r.fetch('id') }.min : page.map { |r| r.fetch('id') }.max
    end
    lists[resource] = rows
  end
  client.options('security_advisories')
  client.options('security_advisory_cves')
  advisories = lists['security_advisories'].map { |r| r.slice('id','external_id','state','content_revision') }
  links = lists['security_advisory_cves'].map do |r|
    advisory = r['security_advisory']; advisory = advisory['id'] if advisory.is_a?(Hash)
    {'id'=>r['id'], 'cve'=>r.fetch('cve_id'), 'advisory_id'=>advisory}
  end
  approved_path = File.join(out,'../approved-cves.json')
  approved = JSON.parse(File.read(approved_path)).fetch('cves')
  raise 'approved_set_not60unique' unless approved.length == 60 && approved.uniq.length == 60
  matches = links.select { |r| approved.include?(r['cve']) }
  external_matches = advisories.select { |r| approved.any? { |c| r['external_id'].to_s.include?(c) } }
  local = Dir.glob(File.join(repo,'advisories','*')).select { |p| File.directory?(p) }.map do |p|
    subpath = File.join(p,'submission.yml'); sub = File.exist?(subpath) ? YAML.safe_load_file(subpath) : {}
    {'cve'=>File.basename(p), 'advisory_id'=>sub['advisory_id'], 'remote_content_revision'=>sub['remote_content_revision']}
  end
  result = {'collected_at'=>Time.now.utc.iso8601,'api_url'=>config.api_url,'approved_sha256'=>Digest::SHA256.file(approved_path).hexdigest,'approved_count'=>approved.length,'token_file'=>{'exists'=>true,'mode'=>format('%04o',mode),'owned_by_current_user'=>true},'read_actions_succeeded'=>['security_advisory#index','security_advisory_cve#index'],'read_options_succeeded'=>['security_advisories','security_advisory_cves'],'pagination'=>pages,'advisory_count'=>advisories.length,'association_count'=>links.length,'state_counts'=>advisories.group_by { |r| r['state'] }.transform_values(&:length),'advisories'=>advisories,'associations'=>links,'approved_matches'=>matches,'approved_external_id_matches'=>external_matches,'local_submissions'=>local,'approved_local_matches'=>local.select { |r| approved.include?(r['cve']) },'limits'=>['Read-only index inventory; server authorization limits visible records. No Node resources requested. No remote mutation, adopt or synchronization.']}
  File.write(File.join(out,'inventory.json'), JSON.pretty_generate(result)+"\n")
  puts JSON.generate(result.slice('collected_at','approved_count','advisory_count','association_count','state_counts','approved_matches','approved_external_id_matches','approved_local_matches','token_file'))
rescue StandardError => e
  failure = {'error_class'=>e.class.name,'http_status'=>(e.respond_to?(:status) ? e.status : nil),'stage'=>'read_only_inventory','details_suppressed'=>true,'local_guard'=>(['pagination_repeated_ids','invalid_page','unsafe_token_permissions'].include?(e.message) ? e.message : nil)}
  File.write(File.join(out,'failure.json'),JSON.pretty_generate(failure)+"\n")
  puts JSON.generate(failure)
  exit 1
end
