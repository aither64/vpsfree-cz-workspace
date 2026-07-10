#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'
require 'json'
require 'yaml'

ROOT = File.expand_path(__dir__)
NAMESPACE = 'drafts:2026-07-10-kb-czech-fixes:media:vpsadmin'
PERMANENT_NAMESPACE = 'screenshots:vpsadmin'
VPSADMIN_COMMIT = '299147166ecb8459c712ed8a5c4dd14f673663fc'

CAPTURES = [
  %w[informace:members.png getting-started members-list],
  %w[informace:vps1.png getting-started vps-list],
  %w[informace:detailsvps.png getting-started vps-details],
  %w[navody:vps:ssh-connection.png getting-started ssh-connection],
  %w[informace:details2.png getting-started vps-action-menu],
  %w[navody:vps:deploy-public-key.png getting-started deploy-public-key],
  %w[navody:vps:vps-transfers.png traffic vps-monthly-transfers],
  %w[navody:server:add_ssh_key.png ssh-keys add-public-key],
  %w[navody:server:deploy_ssh_key.png ssh-keys deploy-public-key],
  %w[navody:vps:dataset_vps.png datasets vps-dataset-list],
  %w[navody:vps:dataset_create.png datasets create-dataset-form],
  %w[navody:vps:mounts.png datasets mount-list],
  %w[navody:vps:mounts_detail.png datasets mount-dataset-form],
  %w[navody:vps:vpsadminos:nasexport.png exports nas-export-list],
  %w[navody:vps:vpsadminos:backupexport.png exports backup-export-list],
  %w[navody:vps:vpsadminos:detailexportu1v2.png exports create-export-form],
  %w[navody:vps:vpsadminos:detailexportu2v2.png exports export-details],
  %w[navody:vps:ip_adresy.png networking ip-address-list],
  %w[navody:vps:vpsadminos:routedadresses.png networking routed-addresses],
  %w[navody:vps:vpsadminos:interfaceaddresses.png networking interface-addresses],
  %w[navody:vps:console-1-web.png console open-web-console],
  %w[navody:vps:console-2-web.png console web-console],
  %w[navody:vps:features.jpg vps-details feature-settings],
  %w[navody:vps:datasets.jpg vps-details datasets],
  %w[navody:vps:vpsfree_playground.jpg restore-backups playground-vps-list],
  %w[navody:vps:vspfree_zalohy.jpg restore-backups backup-list],
  %w[navody:vps:vpsfree_mounting.jpg restore-backups mount-backup-form],
  %w[navody:vps:pgnd_create.png playground create-vps-form],
  %w[navody:vps:clone_vps.png playground clone-vps-form],
  %w[navody:vps:swap_vps2.png playground swap-vps-action],
  %w[navody:vps:swap_preview2.png playground swap-vps-preview],
  %w[navody:vps:datove_prenosy.png traffic monthly-traffic],
  %w[navody:vps:net_monitor_web.png traffic live-monitor-web],
  %w[navody:vps:net_monitor_cli.png traffic live-monitor-cli],
  %w[navody:vps:cluster_resources_detail.png environments resource-package-detail],
  %w[navody:vps:cluster_resources.png environments cluster-resources],
  %w[navody:vps:env_config.png environments environment-configs],
  %w[navody:vps:reverzni_dns.png reverse-dns configure-reverse-record],
  %w[navody:vps:create_vps.png vps-management create-vps-form],
  %w[navody:vps:root_passwd.png vps-management set-root-password],
  %w[navody:vps:distro_reinstall.png vps-management reinstall-form],
  %w[navody:vps:resources.png vps-management resource-settings],
  %w[navody:vps:hostname.png vps-management hostname-form],
  %w[navody:vps:vps_features.png vps-management feature-settings],
  %w[navody:vps:outage_windows.png vps-management outage-windows],
  %w[navody:vps:vps_details_start_menu.png start-menu vps-action],
  %w[navody:vps:vps_console_start_menu.png start-menu main-menu],
  %w[navody:vps:vps_console_start_menu_nixos.png start-menu nixos-generation-action],
  %w[navody:vps:vps_console_start_menu_generations.png start-menu generation-list],
  %w[manuals:vps:vps_userns_map.png userns map],
  %w[navody:vps:user_mail_roles.png account email-roles],
  %w[navody:vps:user_mail_templates.png account mail-template-recipients],
  %w[navody:vps:2fa_status.png account multifactor-status],
  %w[navody:vps:totp_device_confirm.png account totp-confirm],
  %w[navody:vps:totp_device_list.png account totp-device-list],
  %w[navody:vps:user-session-control.png account session-settings],
  %w[navody:vps:user-session-log.png account session-list],
  %w[navody:vps:vpsadminos:vps-details-boot.png rescue-mode boot-form],
  %w[navody:vps:vpsadminos:vps-console-boot.png rescue-mode console],
  %w[navody:vps:backups.png backups vps-backups]
].freeze

PAGE_MEDIA = {
  'informace:novacci' => CAPTURES[0..6].map(&:first),
  'navody:server:ssh' => CAPTURES[7..8].map(&:first),
  'navody:vps:datasety' => CAPTURES[9..12].map(&:first),
  'navody:vps:exporty' => CAPTURES[13..16].map(&:first),
  'navody:vps:ip_adresy' => CAPTURES[17..19].map(&:first),
  'navody:vps:konzole' => CAPTURES[20..21].map(&:first),
  'navody:vps:kvm-openrc' => CAPTURES[22..23].map(&:first),
  'navody:vps:obnova_webu_zo_zalohy' => CAPTURES[24..26].map(&:first),
  'navody:vps:playgroundvps' => CAPTURES[27..30].map(&:first),
  'navody:vps:prenosy' => CAPTURES[31..33].map(&:first),
  'navody:vps:prostredi' => CAPTURES[34..36].map(&:first),
  'navody:vps:rdns' => [CAPTURES[37].first],
  'navody:vps:sprava' => [
    CAPTURES[38].first,
    CAPTURES[39].first,
    *CAPTURES[7..8].map(&:first),
    *CAPTURES[40..44].map(&:first),
    CAPTURES[28].first
  ],
  'navody:vps:start_menu' => CAPTURES[45..48].map(&:first),
  'navody:vps:userns' => [CAPTURES[49].first],
  'navody:vps:uzivatele' => CAPTURES[50..56].map(&:first),
  'navody:vps:vpsadminos:oprava' => CAPTURES[57..58].map(&:first),
  'navody:vps:zalohy' => [CAPTURES[59].first]
}.freeze

abort "expected 60 captures, got #{CAPTURES.length}" unless CAPTURES.length == 60
abort 'legacy media IDs are not unique' unless CAPTURES.map(&:first).uniq.length == 60

metadata = JSON.parse(
  File.read(File.join(ROOT, 'legacy-media', 'media-metadata.json'))
)

source_pages = Hash.new { |hash, key| hash[key] = [] }
PAGE_MEDIA.each do |page, media_ids|
  media_ids.each { |media| source_pages[media] << page }
end

assets = CAPTURES.map do |legacy_media, topic, view|
  legacy_path = File.join(ROOT, 'legacy-media', *legacy_media.split(':'))
  filename = "#{view}.png"
  local_file = File.join('screenshots', topic, 'cs', filename)

  {
    'legacy_media' => legacy_media,
    'legacy_revision' => metadata.fetch(legacy_media).fetch('revision'),
    'legacy_hash' => metadata.fetch(legacy_media).fetch('hash'),
    'legacy_sha256' => Digest::SHA256.file(legacy_path).hexdigest,
    'draft_media' => "#{NAMESPACE}:#{topic}:cs:#{filename}",
    'permanent_media' => "#{PERMANENT_NAMESPACE}:#{topic}:cs:#{filename}",
    'language' => 'cs',
    'topic' => topic,
    'view' => view,
    'source_pages' => source_pages.fetch(legacy_media),
    'vpsadmin_commit' => VPSADMIN_COMMIT,
    'viewport' => { 'width' => 1440, 'height' => 1100, 'device_scale_factor' => 1 },
    'capture' => nil,
    'local_file' => local_file,
    'dimensions' => nil,
    'sha256' => nil,
    'review_status' => 'pending'
  }
end

manifest = {
  'schema' => 2,
  'wiki' => 'kb.vpsfree.cz',
  'draft_namespace' => 'drafts:2026-07-10-kb-czech-fixes',
  'vpsadmin_commit' => VPSADMIN_COMMIT,
  'assets' => assets
}

File.write(File.join(ROOT, 'screenshot-manifest.yml'), YAML.dump(manifest))
puts "wrote screenshot-manifest.yml with #{assets.length} assets"
