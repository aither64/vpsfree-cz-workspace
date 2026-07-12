#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'
require 'fileutils'
require 'json'

ROOT = __dir__
SOURCE_ROOT = File.join(ROOT, 'kb-sources')
OUTPUT_ROOT = File.join(ROOT, 'kb-candidates')

Replacement = Data.define(:language, :page, :path, :before, :body, :count)
replacements = []
add = lambda do |language, page, path, before, body = before, count = 1|
  replacements << Replacement.new(language:, page:, path:, before:, body:, count:)
end

add.call('cs', 'informace:platby', 'member.payment-instructions.open',
         '**Upravit profil** -> **Pokyny k platbě**')
%w[navody:server:ssh navody:vps:sprava].each do |page|
  add.call('cs', page, 'member.public-keys.add',
           'Upravit profil → Veřejné klíče → vpravo v panelu Přidat veřejný klíč')
end
add.call('cs', 'navody:vps:metriky', 'member.metrics-access-tokens.open',
         '**Upravit profil** -> **Přístupové tokeny k metrikám**')
add.call('cs', 'navody:vps:prostredi', 'member.cluster-resources.open',
         "Upravit profil →\nProstředky clusteru")
add.call('cs', 'navody:vps:prostredi', 'member.environment-configs.open',
         'Upravit profil → Konfigurace prostředí')
add.call('cs', 'navody:vps:uzivatele', 'member.advanced-email-configuration.open',
         'vpsAdmin -> Upravit profil -> Pokročilá konfigurace e-mailu')
add.call('cs', 'navody:vps:uzivatele', 'member.totp-devices.open',
         'vpsAdmin -> Upravit profil -> TOTP zařízení')
add.call('cs', 'navody:vps:uzivatele', 'member.passkeys.open',
         'Upravit profil -> Přístupové klíče')
add.call('cs', 'navody:vps:uzivatele', 'member.sessions.open',
         'vpsAdmin -> Upravit profil -> Relace')
add.call('cs', 'navody:vps:ip_adresy', 'networking.routable-addresses.open',
         'Sítě -> Routované adresy')
add.call('cs', 'navody:vps:prenosy', 'networking.monthly-traffic.open',
         'Sítě -> Seznam měsíčního provozu')
add.call('cs', 'navody:vps:prenosy', 'networking.live-monitor.open',
         'Sítě -> Live monitor')
add.call('cs', 'navody:server:primarni_dns', 'dns.primary-zones.open',
         '**DNS** -> **Primární zóny**')
add.call('cs', 'navody:server:sekundarni_dns', 'dns.secondary-zones.open',
         'DNS -> Sekundární zóny')
add.call('cs', 'navody:server:sekundarni_dns', 'dns.tsig-keys.open',
         'DNS -> TSIG klíče')
add.call('cs', 'navody:vps:zalohy', 'backups.vps.open', 'menu Zálohy',
         'menu Zálohy → Zálohy VPS', 2)
add.call('cs', 'navody:vps:obnova_webu_zo_zalohy', 'backups.vps.open',
         '//Zálohy > Zálohy VPS//')
add.call('cs', 'navody:vps:playgroundvps', 'vps.create.open', '„Nové VPS“')
add.call('cs', 'navody:vps:obnova_webu_zo_zalohy', 'vps.create.open',
         '//VPS > Nové VPS//')
add.call('cs', 'navody:vps:playgroundvps', 'vps.clone.open', '**Klonovat VPS**')
add.call('cs', 'navody:vps:playgroundvps', 'vps.swap.open', '**Prohodit VPS**',
         '**Prohodit VPS**', 2)
add.call('cs', 'navody:vps:datasety', 'datasets.create.open', '//Vytvořit dataset//',
         '//Vytvořit dataset//', 2)
add.call('cs', 'navody:vps:oprava', 'datasets.mount.open', '**Mount**')
add.call('cs', 'navody:distribuce:nixos:impermanence', 'vps.features.open', '**Funkce**')
%w[navody:vps:vpsadminos:oprava navody:distribuce:nixos:impermanence].each do |page|
  add.call('cs', page, 'vps.boot-rescue.open',
           '**Spustit VPS ze šablony (nouzový režim)**')
end
add.call('cs', 'navody:vps:userdata', 'userdata.deploy.open', '**Nasadit do VPS**')

add.call(
  'en',
  'information:membership_fees',
  'member.payment-instructions.open',
  "You can find member ID\nin vpsAdmin -> Edit profile at the top, or Members section. It is also sent in email payment\nreminders and can be seen in Payment instructions in member details in vpsAdmin.",
  'You can find member ID in vpsAdmin -> Edit profile -> Payment instructions. It is also sent in email payment reminders.'
)
add.call('en', 'manuals:vps:management', 'member.public-keys.add',
         'Edit profile → Public keys → Add public key')
add.call('en', 'manuals:vps:metrics', 'member.metrics-access-tokens.open',
         '**Edit profile** -> **Metrics access tokens**')
add.call('en', 'manuals:vps:environment', 'member.cluster-resources.open',
         "Edit profile →\nCluster resources")
add.call('en', 'manuals:vps:environment', 'member.environment-configs.open',
         "Edit profile → Environment\nconfigs")
add.call('en', 'manuals:vps:users', 'member.advanced-email-configuration.open',
         "vpsAdmin -> Edit profile ->\nAdvanced e-mail configuration")
add.call('en', 'manuals:vps:users', 'member.totp-devices.open',
         'vpsAdmin -> Edit profile -> TOTP devices')
add.call('en', 'manuals:vps:users', 'member.passkeys.open',
         'vpsAdmin -> Edit profile -> Passkeys')
add.call('en', 'manuals:vps:users', 'member.sessions.open',
         'vpsAdmin -> Edit profile -> Session log',
         'vpsAdmin -> Edit profile -> Sessions')
add.call('en', 'manuals:vps:ip_addresses', 'networking.routable-addresses.open',
         'Networking -> Routable addresses')
add.call('en', 'manuals:vps:traffic', 'networking.monthly-traffic.open',
         'Networking -> List monthly traffic')
add.call('en', 'manuals:vps:traffic', 'networking.live-monitor.open',
         'Networking -> Live monitor')
add.call('en', 'manuals:server:primary_dns', 'dns.primary-zones.open',
         '**DNS** -> **Primary Zones**', '**DNS** -> **Primary zones**')
add.call('en', 'manuals:server:secondary_dns', 'dns.secondary-zones.open',
         'DNS -> Secondary Zones', 'DNS -> Secondary zones')
add.call('en', 'manuals:server:secondary_dns', 'dns.tsig-keys.open',
         'DNS -> TSIG Keys', 'DNS -> TSIG keys')
add.call('en', 'manuals:vps:backups', 'backups.vps.open', 'the Backups menu',
         'the Backups -> VPS backups menu', 2)
add.call('en', 'manuals:vps:playgroundvps', 'vps.create.open',
         'section VPS, "New VPS"', 'section VPS, "New VPS"')
add.call('en', 'manuals:vps:playgroundvps', 'vps.clone.open', '**Clone VPS**')
add.call('en', 'manuals:vps:playgroundvps', 'vps.swap.open',
         "VPS can be\nswapped from details of the production VPS:",
         'Use **Swap VPS** in details of the production VPS:')
add.call('en', 'manuals:vps:repair', 'datasets.mount.open',
         'Details of the recovery VPS -> Create mount',
         'VPS details -> Mount')
add.call('en', 'manuals:vps:vpsadminos:recovery', 'vps.boot-rescue.open',
         '**Boot from VPS template**',
         '**Boot VPS from template (rescue mode)**')
add.call('en', 'manuals:distributions:nixos:impermanence', 'vps.boot-rescue.open',
         '**Boot VPS from template (rescue mode)**')
add.call('en', 'manuals:vps:userdata', 'userdata.deploy.open', '**Deploy to VPS**')

index = JSON.parse(File.read(File.join(SOURCE_ROOT, 'index.json')))
pages = index.flat_map do |language, entries|
  entries.map do |entry|
    key = [language, entry.fetch('id')]
    [key, File.read(File.join(SOURCE_ROOT, entry.fetch('file')))]
  end
end.to_h

plan = replacements.map do |replacement|
  key = [replacement.language, replacement.page]
  source = pages.fetch(key)
  actual_count = source.scan(replacement.before).length
  unless actual_count == replacement.count
    raise "#{key.join(':')}: #{replacement.path} expected #{replacement.count} matches, found #{actual_count}"
  end

  tagged = %(<vpsadmin-nav id="#{replacement.path}">#{replacement.body}</vpsadmin-nav>)
  pages[key] = source.gsub(replacement.before, tagged)
  {
    'language' => replacement.language,
    'page' => replacement.page,
    'path' => replacement.path,
    'count' => replacement.count,
    'before' => replacement.before,
    'body' => replacement.body
  }
end

exceptions = [
  {
    'language' => 'en',
    'page' => 'manuals:vps:management',
    'path' => 'vps.create.open',
    'reason' => 'The article describes creation steps but does not name the New VPS navigation control.'
  },
  {
    'language' => 'en',
    'page' => 'manuals:vps:management',
    'path' => 'vps.clone.open',
    'reason' => 'The article does not contain a Clone VPS navigation instruction.'
  },
  {
    'language' => 'en',
    'page' => 'manuals:vps:datasets',
    'path' => 'datasets.create.open',
    'reason' => 'The article discusses subdatasets but does not name the Create dataset control.'
  },
  {
    'language' => 'cs',
    'page' => 'navody:vps:sprava',
    'path' => 'vps.features.open',
    'reason' => 'Features is only the article section heading, not an in-prose navigation instruction.'
  },
  {
    'language' => 'en',
    'page' => 'manuals:vps:management',
    'path' => 'vps.features.open',
    'reason' => 'Features is only the article section heading, not an in-prose navigation instruction.'
  },
  {
    'language' => 'en',
    'page' => 'manuals:distributions:nixos:impermanence',
    'path' => 'vps.features.open',
    'reason' => 'The current English article does not mention the Features form.'
  }
]

candidate_index = { 'pages' => [], 'annotations' => plan, 'exceptions' => exceptions }
pages.sort.each do |(language, page_id), content|
  relative = File.join(language, *page_id.split(':')) + '.txt'
  destination = File.join(OUTPUT_ROOT, relative)
  FileUtils.mkdir_p(File.dirname(destination))
  File.write(destination, content)
  original = File.read(File.join(SOURCE_ROOT, relative))
  candidate_index.fetch('pages') << {
    'language' => language,
    'id' => page_id,
    'file' => relative,
    'changed' => content != original,
    'source_sha256' => Digest::SHA256.hexdigest(original),
    'candidate_sha256' => Digest::SHA256.hexdigest(content)
  }
end

FileUtils.mkdir_p(OUTPUT_ROOT)
File.write(
  File.join(OUTPUT_ROOT, 'index.json'),
  "#{JSON.pretty_generate(candidate_index)}\n"
)

cell = lambda do |value|
  value.to_s.gsub('|', '\\|').gsub("\n", ' ↵ ')
end
review = [
  '# KB navigation annotation review',
  '',
  "Changed pages: #{candidate_index.fetch('pages').count { |page| page.fetch('changed') }}",
  "Annotation tags: #{plan.sum { |item| item.fetch('count') }}",
  '',
  '| Language | Page | Semantic path | Count | Existing text | Candidate text |',
  '| --- | --- | --- | ---: | --- | --- |'
]
plan.each do |item|
  review << "| #{cell.call(item.fetch('language'))} | #{cell.call(item.fetch('page'))} " \
            "| `#{cell.call(item.fetch('path'))}` | #{item.fetch('count')} " \
            "| #{cell.call(item.fetch('before'))} | #{cell.call(item.fetch('body'))} |"
end
review.concat([
  '',
  '## Explicit exceptions',
  '',
  '| Language | Page | Semantic path | Reason |',
  '| --- | --- | --- | --- |'
])
exceptions.each do |item|
  review << "| #{cell.call(item.fetch('language'))} | #{cell.call(item.fetch('page'))} " \
            "| `#{cell.call(item.fetch('path'))}` | #{cell.call(item.fetch('reason'))} |"
end
File.write(File.join(OUTPUT_ROOT, 'review.md'), "#{review.join("\n")}\n")

puts "Prepared #{candidate_index.fetch('pages').count { |page| page.fetch('changed') }} changed pages " \
     "with #{plan.sum { |item| item.fetch('count') }} annotations"
