#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'digest'
require 'json'
require 'yaml'

ROOT = File.expand_path(__dir__)

REPLACEMENTS = {
  'domu' => [
    ['User namespaces', 'Uživatelské jmenné prostory', 1]
  ],
  'informace:novacci' => [
    ['**Members**', '**Členové**', 1]
  ],
  'informace:platby' => [
    ['sekce Admin Členů', 'sekce Členové', 1],
    [
      '**Edit profile** -> **Payment instructions**',
      '**Upravit profil** -> **Pokyny k platbě**',
      1
    ]
  ],
  'informace:vymena_ip' => [
    ['"Interface addresses"', '„Adresy rozhraní“', 2],
    ['"Routed addresses"', '„Routované adresy“', 1]
  ],
  'navody:distribuce:nixos:impermanence' => [
    [
      '**Boot VPS from template (rescue mode)**',
      '**Spustit VPS ze šablony (nouzový režim)**',
      1
    ],
    ['**Features**', '**Funkce**', 1]
  ],
  'navody:server:primarni_dns' => [
    ['**Primary zones**', '**Primární zóny**', 1],
    [
      '**View DNSKEY and DS records**',
      '**Zobrazit záznamy DNSKEY a DS**',
      1
    ],
    ['**Secondary servers**', '**Sekundární servery**', 1]
  ],
  'navody:server:sekundarni_dns' => [
    ['DNS -> Secondary zones', 'DNS -> Sekundární zóny', 1],
    ['"Primary servers"', '„Primární servery“', 1],
    ['DNS -> TSIG keys', 'DNS -> TSIG klíče', 1]
  ],
  'navody:server:ssh' => [
    [
      'Edit profile → Public keys → vpravo v panelu Add public key',
      'Upravit profil → Veřejné klíče → vpravo v panelu Přidat veřejný klíč',
      1
    ]
  ],
  'navody:vps:api' => [
    [
      'chybou "Resource is locked".',
      'chybou „Zdroj je uzamčen. Zkuste to prosím později.“',
      1
    ]
  ],
  'navody:vps:datasety' => [
    ['//Create dataset//', '//Vytvořit dataset//', 2],
    ['//Parent//', '//Rodičovský dataset//', 1],
    ['//Auto mount//', '//Automatický mount//', 1],
    ['//Quota//', '//Kvóta včetně potomků (quota)//', 2],
    ['//Used space//', '//Použité místo//', 2],
    [
      '//Referenced space//',
      '//Referencovaný prostor (referenced)//',
      2
    ],
    ['//Available space//', '//Dostupné místo//', 2],
    ['//Reference quota//', '//Kvóta datasetu (refquota)//', 1],
    [
      "Mount lze dočasně odpojit tlačítkem \"Disable/Enable\". Toto nastavení je\n" \
      'perzistentní mezi restarty VPS.',
      "Mount lze dočasně vypnout a znovu zapnout. Toto nastavení je\n" \
      'perzistentní mezi restarty VPS.',
      1
    ]
  ],
  'navody:vps:exporty' => [
    ['//Exports//', '//Exporty//', 2],
    ['//Export dataset//', '//Export datasetu//', 1],
    [
      '//Backups// -> //VPS backups//, popř. //NAS backups//',
      '//Zálohy// -> //Zálohy VPS//, popř. //Zálohy NAS//',
      1
    ],
    ['//All VPS//', '//Všechny VPS//', 1]
  ],
  'navody:vps:ip_adresy' => [
    [
      'Networking -> Routable addresses',
      'Sítě -> Routované adresy',
      1
    ],
    ['"Manage host addresses"', '„Spravovat adresy hostitelů“', 1],
    ['"Add host addresses"', '„Přidat adresy hostitelů“', 1]
  ],
  'navody:vps:konzole' => [],
  'navody:vps:kvm-openrc' => [],
  'navody:vps:metriky' => [
    [
      '**Edit profile** -> **Metrics access tokens**',
      '**Upravit profil** -> **Přístupové tokeny k metrikám**',
      1
    ]
  ],
  'navody:vps:obnova_webu_zo_zalohy' => [
    [
      '//VPS > New VPS//" v "//Location//" vyberieme "//Playground//" a klikneme na "//next//',
      '//VPS > Nové VPS//" v "//Lokace//" vyberieme "//Playground//" a klikneme na "//Další//',
      1
    ],
    [
      '//Backups > VPS Backups//',
      '//Zálohy > Zálohy VPS//',
      1
    ]
  ],
  'navody:vps:oprava' => [
    [
      "Mount se vytvoří následovně: Detail záchranné VPS -> Create mount ->\n" \
      'vybrat dataset rozbité VPS.',
      "Mount vytvoříme v detailu záchranné VPS akcí **Mount**, kde vybereme\n" \
      'dataset rozbité VPS.',
      1
    ]
  ],
  'navody:vps:playgroundvps' => [
    ['"New VPS"', '„Nové VPS“', 1],
    ['**Clone VPS**', '**Klonovat VPS**', 1],
    ['v transaction logu', 'v sekci **Transakce**', 1],
    ['Funkce swap VPS', 'Funkce **Prohodit VPS**', 1],
    ['Swap VPS lze', '**Prohodit VPS** lze', 1]
  ],
  'navody:vps:plny_disk' => [
    ['menu Backups -> NAS', 'menu Zálohy -> NAS', 1]
  ],
  'navody:vps:prenosy' => [
    [
      'Networking -> List monthly traffic',
      'Sítě -> Seznam měsíčního provozu',
      1
    ],
    ['Networking -> Live monitor', 'Sítě -> Live monitor', 1]
  ],
  'navody:vps:prostredi' => [
    [
      "Edit profile →\nCluster resources",
      "Upravit profil →\nProstředky clusteru",
      1
    ],
    [
      "Edit profile → Environment\nconfigs",
      'Upravit profil → Konfigurace prostředí',
      1
    ]
  ],
  'navody:vps:rdns' => [
    ['"Interface addresses"', '„Adresy rozhraní“', 1]
  ],
  'navody:vps:sprava' => [
    [
      'Edit profile → Public keys → vpravo v panelu Add public key',
      'Upravit profil → Veřejné klíče → vpravo v panelu Přidat veřejný klíč',
      1
    ],
    ['===== Features =====', '===== Funkce =====', 1],
    ['Features lze', 'Funkce lze', 1],
    ['buď environment, lokaci', 'buď prostředí, lokaci', 1]
  ],
  'navody:vps:start_menu' => [
    ['====== Start Menu ======', '====== Start menu ======', 1]
  ],
  'navody:vps:userdata' => [
    ['**Edit profile**', '**Upravit profil**', 1],
    ['**Deploy to VPS**', '**Nasadit do VPS**', 1]
  ],
  'navody:vps:userns' => [
    ['====== User namespace =======', '====== Uživatelské jmenné prostory =======', 1],
    ['User namespace je', 'Uživatelský jmenný prostor je', 1],
    [
      "rootem v jeho user namespace. Každé naše\nVPS běží v jednom user namespace. Nastavování user namespace je",
      "rootem ve svém uživatelském jmenném prostoru. Každá naše\nVPS běží v jednom uživatelském jmenném prostoru. Nastavování uživatelských jmenných prostorů je",
      1
    ],
    [
      'VPS jsou od námi vytvořených user namespace abstrahovány',
      'VPS jsou od námi vytvořených uživatelských jmenných prostorů abstrahovány',
      1
    ],
    ['**ID within VPS**', '**ID uvnitř VPS**', 1],
    [
      '**ID within namespace**',
      '**ID v rámci jmenného prostoru**',
      2
    ],
    ['**ID count**', '**ID počet**', 1],
    ['Type', 'Typ', 4],
    ['ID within VPS', 'ID uvnitř VPS', 4],
    [
      'ID within namespace',
      'ID v rámci jmenného prostoru',
      4
    ],
    ['ID count', 'ID počet', 4],
    [
      'z našeho user namespace.',
      'z našeho uživatelského jmenného prostoru.',
      1
    ],
    [
      '**IDs within VPS**',
      '**ID uvnitř VPS**',
      1
    ]
  ],
  'navody:vps:uzivatele' => [
    ['Edit profile -> Passkeys', 'Upravit profil -> Přístupové klíče', 1],
    ['vpsAdmin -> Edit profile', 'vpsAdmin -> Upravit profil', 7],
    ['role account management', 'role Vedení účtu', 1],
    ['role system administrator', 'role Správce systému', 1],
    [
      'Advanced e-mail configuration',
      'Pokročilá konfigurace e-mailu',
      1
    ],
    ['TOTP devices', 'TOTP zařízení', 1],
    ['"Session control"', '„Nastavení relací“', 1],
    ['**Enable single sign-on**', '**Povolit jednotné přihlášení**', 1],
    [
      '**Preferred session length**',
      '**Doba nečinnosti před odhlášením**',
      1
    ],
    ['**Logout all**', '**Odhlašovat všude**', 1],
    ['-> Sessions', '-> Relace', 1],
    [
      'všechny aktivní přihlášení dané aplikace',
      'všechny aktivní relace dané aplikace',
      1
    ],
    [
      'vpsAdmin loguje všechny přihlášení a pamatuje si',
      'vpsAdmin loguje všechny relace a pamatuje si',
      1
    ],
    [
      "daném sezení vykonány. Světle zeleně jsou zvýrazněny přihlášení, které jsou stále aktivní.\n" \
      "Aktuální přihlášení, ze kterého se na log koukáme, je zvýrazněno tmavě zeleně. Kliknutím\n" \
      'na ikonku koše můžeme vybrané aktivní přihlášení ukončit.',
      "dané relaci vykonány. Světle zeleně jsou zvýrazněny relace, které jsou stále aktivní.\n" \
      "Aktuální relace, ze které se na log díváme, je zvýrazněna tmavě zeleně. Kliknutím\n" \
      'na ikonku koše můžeme vybranou aktivní relaci ukončit.',
      1
    ]
  ],
  'navody:vps:vpsadmin' => [
    ['„transaction chain“', '„řetězec transakcí“', 1],
    ['jedním chainem', 'jedním řetězcem', 1],
    [
      "transaction\nlogu v pravém panelu",
      'sekci **Transakce** v pravém panelu',
      1
    ],
    ['deseti posledních chainů', 'deseti posledních řetězců', 1],
    ['ID chainu', 'ID řetězce', 1],
    ['se chain', 'se řetězec', 1],
    ['Chainy se', 'Řetězce se', 1],
    ['když chain doběhne', 'když řetězec doběhne', 1],
    ['dokončení chainu', 'dokončení řetězce', 1],
    [
      "Pokud na vás vyskočí chybová hláška: „Resource is locked. Please try\n" \
      'again.“ znamená to, že objekt, se kterým chcete něco udělat, je uzamčen',
      'Pokud na vás vyskočí chybová hláška: „Zdroj je uzamčen. Zkuste to prosím později.“ ' \
      'Znamená to, že objekt, se kterým chcete něco udělat, je uzamčen',
      1
    ],
    [
      "„Resource is locked. Please try\nagain.“",
      '„Zdroj je uzamčen. Zkuste to prosím později.“',
      1
    ]
  ],
  'navody:vps:vpsadminos:oprava' => [
    [
      '**Boot from VPS template**',
      '**Spustit VPS ze šablony (nouzový režim)**',
      1
    ]
  ],
  'navody:vps:zalohy' => [
    ['menu Backups', 'menu Zálohy', 2]
  ]
}.freeze

metadata = JSON.parse(
  File.read(File.join(ROOT, 'kb-source', 'page-metadata.json'))
)
manifest = YAML.safe_load_file(File.join(ROOT, 'screenshot-manifest.yml'))
media_by_page = Hash.new { |hash, key| hash[key] = [] }
manifest.fetch('assets').each do |asset|
  asset.fetch('source_pages').each { |page| media_by_page[page] << asset }
end

abort "expected 30 replacement pages, got #{REPLACEMENTS.length}" unless REPLACEMENTS.length == 30

drafts = []

REPLACEMENTS.each do |page, replacements|
  source_path = File.join(ROOT, 'kb-source', *page.split(':')) + '.txt'
  text = File.read(source_path)

  replacements.each do |old_text, new_text, expected_count|
    count = text.scan(old_text).length
    unless count == expected_count
      abort "#{page}: expected #{expected_count} occurrences of #{old_text.inspect}, got #{count}"
    end

    text = text.gsub(old_text, new_text)
  end

  media_by_page[page].each do |asset|
    legacy = asset.fetch('legacy_media')
    basename = legacy.split(':').last
    replaced = 0

    text = text.gsub(/\{\{[^}]+\}\}/) do |media_ref|
      target = media_ref[/\{\{\s*([^?\s|}]+)/, 1]
      next media_ref unless target

      normalized = target.delete_prefix(':')
      next media_ref unless normalized == legacy || normalized == basename

      replaced += 1
      media_ref.sub(target, ":#{asset.fetch('media_id')}")
    end

    abort "#{page}: did not replace media reference #{legacy}" if replaced.zero?
  end

  revision = metadata.fetch(page).fetch('revision')

  preview_path = File.join(ROOT, 'kb-candidates', *page.split(':')) + '.txt'
  FileUtils.mkdir_p(File.dirname(preview_path))
  File.write(preview_path, text)

  drafts << {
    'id' => page,
    'source_revision' => revision,
    'source_sha256' => Digest::SHA256.file(source_path).hexdigest,
    'file' => preview_path.delete_prefix("#{ROOT}/"),
    'sha256' => Digest::SHA256.file(preview_path).hexdigest,
    'screenshot_count' => media_by_page[page].length
  }
end

media = manifest.fetch('assets').map do |asset|
  {
    'id' => asset.fetch('media_id'),
    'file' => asset.fetch('local_file'),
    'sha256' => asset.fetch('sha256'),
    'policy' => 'create'
  }
end

release = { 'schema' => 1, 'wiki' => 'cz', 'pages' => drafts, 'media' => media }
File.write(File.join(ROOT, 'kb-release.yml'), YAML.dump(release))

puts "wrote release with #{drafts.length} pages and #{media.length} media objects"
