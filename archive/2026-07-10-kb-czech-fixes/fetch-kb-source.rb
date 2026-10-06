#!/usr/bin/env ruby
# frozen_string_literal: true

require 'base64'
require 'fileutils'
require 'json'

load File.expand_path('../../bin/kb-page', __dir__)

ROOT = File.expand_path(__dir__)

PAGES = %w[
  domu
  informace:novacci
  informace:platby
  informace:vymena_ip
  navody:distribuce:nixos:impermanence
  navody:server:primarni_dns
  navody:server:sekundarni_dns
  navody:server:ssh
  navody:vps:api
  navody:vps:datasety
  navody:vps:exporty
  navody:vps:ip_adresy
  navody:vps:konzole
  navody:vps:kvm-openrc
  navody:vps:metriky
  navody:vps:obnova_webu_zo_zalohy
  navody:vps:oprava
  navody:vps:playgroundvps
  navody:vps:plny_disk
  navody:vps:prenosy
  navody:vps:prostredi
  navody:vps:rdns
  navody:vps:sprava
  navody:vps:start_menu
  navody:vps:userdata
  navody:vps:userns
  navody:vps:uzivatele
  navody:vps:vpsadmin
  navody:vps:vpsadminos:oprava
  navody:vps:zalohy
].freeze

MEDIA = %w[
  informace:members.png
  informace:vps1.png
  informace:detailsvps.png
  navody:vps:ssh-connection.png
  informace:details2.png
  navody:vps:deploy-public-key.png
  navody:vps:vps-transfers.png
  navody:server:add_ssh_key.png
  navody:server:deploy_ssh_key.png
  navody:vps:dataset_vps.png
  navody:vps:dataset_create.png
  navody:vps:mounts.png
  navody:vps:mounts_detail.png
  navody:vps:vpsadminos:nasexport.png
  navody:vps:vpsadminos:backupexport.png
  navody:vps:vpsadminos:detailexportu1v2.png
  navody:vps:vpsadminos:detailexportu2v2.png
  navody:vps:ip_adresy.png
  navody:vps:vpsadminos:routedadresses.png
  navody:vps:vpsadminos:interfaceaddresses.png
  navody:vps:console-1-web.png
  navody:vps:console-2-web.png
  navody:vps:features.jpg
  navody:vps:datasets.jpg
  navody:vps:vpsfree_playground.jpg
  navody:vps:vspfree_zalohy.jpg
  navody:vps:vpsfree_mounting.jpg
  navody:vps:pgnd_create.png
  navody:vps:clone_vps.png
  navody:vps:swap_vps2.png
  navody:vps:swap_preview2.png
  navody:vps:datove_prenosy.png
  navody:vps:net_monitor_web.png
  navody:vps:net_monitor_cli.png
  navody:vps:cluster_resources_detail.png
  navody:vps:cluster_resources.png
  navody:vps:env_config.png
  navody:vps:reverzni_dns.png
  navody:vps:create_vps.png
  navody:vps:root_passwd.png
  navody:vps:distro_reinstall.png
  navody:vps:resources.png
  navody:vps:hostname.png
  navody:vps:vps_features.png
  navody:vps:outage_windows.png
  navody:vps:vps_details_start_menu.png
  navody:vps:vps_console_start_menu.png
  navody:vps:vps_console_start_menu_nixos.png
  navody:vps:vps_console_start_menu_generations.png
  manuals:vps:vps_userns_map.png
  navody:vps:user_mail_roles.png
  navody:vps:user_mail_templates.png
  navody:vps:2fa_status.png
  navody:vps:totp_device_confirm.png
  navody:vps:totp_device_list.png
  navody:vps:user-session-control.png
  navody:vps:user-session-log.png
  navody:vps:vpsadminos:vps-details-boot.png
  navody:vps:vpsadminos:vps-console-boot.png
  navody:vps:backups.png
].freeze

abort "expected 30 pages, got #{PAGES.length}" unless PAGES.length == 30
abort "expected 60 media IDs, got #{MEDIA.length}" unless MEDIA.length == 60

def local_path(root, id, suffix: nil)
  parts = id.split(':')
  filename = suffix ? "#{parts.pop}#{suffix}" : parts.pop
  File.join(root, *parts, filename)
end

wiki = KbPage.wiki_config('cz')
client = KbPage::JsonRpcClient.new(
  base_url: wiki.fetch(:url),
  token_path: wiki.fetch(:token_path)
)

page_metadata = PAGES.to_h do |page|
  info = client.call('core.getPageInfo', page:)
  source = client.call('core.getPage', page:)
  source_path = local_path(File.join(ROOT, 'kb-source'), page, suffix: '.txt')
  FileUtils.mkdir_p(File.dirname(source_path))
  File.write(source_path, source)
  [page, info]
end

File.write(
  File.join(ROOT, 'kb-source', 'page-metadata.json'),
  "#{JSON.pretty_generate(page_metadata)}\n"
)

media_metadata = MEDIA.to_h do |media|
  info = client.call('core.getMediaInfo', media:, hash: true)
  encoded = client.call('core.getMedia', media:)
  target = local_path(File.join(ROOT, 'legacy-media'), media)
  FileUtils.mkdir_p(File.dirname(target))
  File.binwrite(target, Base64.strict_decode64(encoded))
  [media, info]
end

File.write(
  File.join(ROOT, 'legacy-media', 'media-metadata.json'),
  "#{JSON.pretty_generate(media_metadata)}\n"
)

puts "fetched #{PAGES.length} pages and #{MEDIA.length} media files"
