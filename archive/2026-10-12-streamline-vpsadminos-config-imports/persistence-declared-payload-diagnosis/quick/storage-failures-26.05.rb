require 'json'
require 'digest'
require 'shellwords'

machine.start unless machine.running?
machine.wait_for_osctl_pool('tank')
machine.wait_until_online
ct = get_container_id
exec_guest = lambda do |command|
  machine.succeeds("osctl ct exec #{ct} bash -c #{Shellwords.escape(command)}")[1].strip
end
wait_for_guest_ready = lambda do |phase|
  begin
    machine.wait_until_succeeds("osctl ct exec #{ct} systemctl is-system-running --wait", timeout: 180)
  rescue StandardError => readiness_error
    # Keep the failed guest's evidence without accepting degraded or
    # allowing a diagnostic error to replace the readiness failure.
    [
      'systemctl --failed --plain --no-pager',
      'journalctl -b --no-pager -n 160 -o short-iso-precise',
      <<~'GUEST',
        systemctl --failed --plain --no-legend --no-pager | head -n 8 |
          while read -r unit rest; do
            printf '\n--- failed unit %s ---\n' "$unit"
            systemctl status "$unit" --no-pager --full --lines=40
            systemctl show "$unit" -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus
            journalctl -b -u "$unit" --no-pager -n 40 -o short-iso-precise
          done
      GUEST
    ].each do |diagnostic|
      begin
        command = "timeout -k 2 20 osctl ct exec #{ct} bash -c #{Shellwords.escape(diagnostic)}"
        status, output = machine.execute("{ #{command}; } 2>&1 | head -c 32768", timeout: 25)
        warn "NixOS guest #{ct} #{phase} readiness diagnostic (#{status}): #{diagnostic}\n#{output}"
      rescue StandardError => diagnostic_error
        warn "NixOS guest #{ct} #{phase} readiness diagnostic unavailable: #{diagnostic_error.class}: #{diagnostic_error.message}"
      end
    end
    raise readiness_error
  end
end
switch = lambda do |generation|
  exec_guest.call("nix-env -p /nix/var/nix/profiles/system --set #{generation} && #{generation}/bin/switch-to-configuration switch")
  expect(exec_guest.call('readlink /run/current-system')).to eq(generation)
end
layout = JSON.parse('{"absentExactMounts":[],"logBacking":"/persistent/var/log","mounts":[{"source":"/persistent/var/lib/nixos","target":"/var/lib/nixos"},{"source":"/persistent/var/log","target":"/var/log"}]}')
snapshot = lambda do |challenge|
  accounts = challenge ? %w[preservation-test a-preservation-test] : %w[preservation-test]
  ids = accounts.to_h do |account|
    live = exec_guest.call("id -u #{account}; id -g #{account}").split.map(&:to_i)
    saved = JSON.parse(exec_guest.call("jq -n --slurpfile u /var/lib/nixos/uid-map --slurpfile g /var/lib/nixos/gid-map --arg name #{account} '[$u[0][$name], $g[0][$name]]'"))
    backing = JSON.parse(exec_guest.call("jq -n --slurpfile u /persistent/var/lib/nixos/uid-map --slurpfile g /persistent/var/lib/nixos/gid-map --arg name #{account} '[$u[0][$name], $g[0][$name]]'"))
    expect(live).to eq(saved), "live IDs differ from allocation maps for #{account}"
    expect(saved).to eq(backing), "visible and backing maps differ for #{account}"
    [account, live]
  end
  exec_guest.call('test /persistent/var/lib/nixos -ef /var/lib/nixos')
  layout.fetch('mounts').each do |pair|
    target = pair.fetch('target')
    exec_guest.call("mountpoint -q #{target} && test #{pair.fetch('source')} -ef #{target}")
    expect(exec_guest.call("awk '$5 == \"#{target}\" {n++} END {print n+0}' /proc/self/mountinfo")).to eq('1')
  end
  layout.fetch('absentExactMounts').each do |target|
    expect(exec_guest.call("awk '$5 == \"#{target}\" {n++} END {print n+0}' /proc/self/mountinfo")).to eq('0')
  end
  exec_guest.call("test #{layout.fetch('logBacking')} -ef /var/log") if layout.fetch('logBacking')
  exec_guest.call('test /persistent/var/lib/preservation-test/payload -ef /var/lib/preservation-test/payload && test /persistent/etc/machine-id -ef /etc/machine-id')
  {
    'ids' => ids,
    'mount_options' => layout.fetch('mounts').to_h { |pair| target = pair.fetch('target'); [target, exec_guest.call("findmnt -n -o OPTIONS --mountpoint #{target}")] },
    'machine_id' => exec_guest.call('cat /etc/machine-id'),
    'payload' => exec_guest.call('sha256sum /var/lib/preservation-test/payload').split.first,
    'owner' => exec_guest.call("stat -c '%u:%g' /var/lib/preservation-test/payload"),
    'metadata' => exec_guest.call("stat -c '%u:%g:%a:%i' /persistent/var/lib/nixos"),
    
    'payload_directory' => exec_guest.call("stat -c '%u:%g:%a:%i' /var/lib/preservation-test")
  }
end

describe 'storage-failures-26.05 old-to-new persistence adoption' do
  it 'retains dynamic accounts, maps, data and bind identity' do
    puts 'Old compatibility source: 1150e37b1cc997b1728f2fda806a3433ef55b798 (sha256-PdZ1g1KtuxL/3T1E01jKhj3Npmkd4G8EJIzS0OSiaMA=)'
    puts 'Candidate compatibility source: /nix/store/j6fxv9cnyfxqrf485jwjcb9j6ncw6js5-vpsadminos'
    puts 'Guest release 26.05; stateVersion 22.11'
    puts 'Prepared old-to-new generations /nix/store/v6h99xqq1j7hkpnhxi9i1zhch0ixv11h-nixos-system-persistence-fixture-26.05pre-git -> /nix/store/h8w8sqm15xx6siccmzkqjkwmd0db24iw-nixos-system-persistence-fixture-26.05pre-git -> /nix/store/jyinbn06b2csaydgh795lv7fflliivf1-nixos-system-persistence-fixture-26.05pre-git'

    machine.all_succeed(
      "osctl ct new --skip-image --distribution nixos --version 26.05 --arch x86_64 #{ct}",
      "osctl ct unset start-menu #{ct}",
      "osctl ct dataset new #{ct} nix",
    )
    rootfs = machine.osctl_json("ct show #{ct}").fetch('rootfs')
    nix_root = machine.osctl_json("ct mounts ls #{ct}").find { |mount| mount.fetch('mountpoint') == '/nix' }.fetch('fs')
    # Use the declarative NixOS container's stopped-store copy contract.
    # Native mapping exposes these root-owned copies as guest root.
    machine.succeeds(<<~SHELL)
      set -e
      # The fresh dataset root is 0750; /nix needs non-root traversal.
      chmod 0755 "#{nix_root}"
      mkdir -p "#{nix_root}/store"
      while IFS= read -r store_path; do
        cp -a "$store_path" "#{nix_root}/store/"
      done < /nix/store/k1sy9c6nk9rak3miif0aj4macdslpqvw-closure-info/store-paths
      cp /nix/store/k1sy9c6nk9rak3miif0aj4macdslpqvw-closure-info/registration "#{nix_root}/nix-path-registration"
    SHELL
    machine.all_succeed(
      "mkdir -p #{nix_root}/var/nix/profiles #{rootfs}/sbin #{rootfs}/etc #{rootfs}/var",
      "ln -s /nix/store/v6h99xqq1j7hkpnhxi9i1zhch0ixv11h-nixos-system-persistence-fixture-26.05pre-git #{nix_root}/var/nix/profiles/system",
      "ln -s /nix/store/v6h99xqq1j7hkpnhxi9i1zhch0ixv11h-nixos-system-persistence-fixture-26.05pre-git/init #{rootfs}/sbin/init",
    )
    machine.all_succeed(
  # The CLI mounts subdatasets; '/' denotes root only in image
  # configuration. Bind this container's queried private root.
  "osctl ct mounts new --fs #{rootfs} --type bind --opts bind,create=dir,rw --mountpoint /persistent #{ct}",
  "osctl ct set impermanence #{ct}",
)

    
    
    
    
    expected_source_metadata = nil
    # Provision custom source metadata before any guest accounts/data.
machine.succeeds("install -d -m 710 -o 42 -g 43 #{rootfs}/var/lib/nixos")
expected_source_metadata = machine.succeeds("stat -c '%u:%g:%a:%i' #{rootfs}/var/lib/nixos")[1].strip

    machine.succeeds("osctl ct start #{ct}")
    wait_for_guest_ready.call('initial boot')
    expect(exec_guest.call('nixos-version')).to start_with('26.05')
    exec_guest.call('nix-store --load-db < /nix/nix-path-registration')
    # The old boot has already mounted state. A normal old live
# switch establishes healthy persisted maps; no ID/map repair.
switch.call('/nix/store/v6h99xqq1j7hkpnhxi9i1zhch0ixv11h-nixos-system-persistence-fixture-26.05pre-git')

    
    exec_guest.call("printf '%s\\n' persistence-upgrade-payload > /var/lib/preservation-test/payload && chown preservation-test:preservation-test /var/lib/preservation-test/payload")
    original = snapshot.call(false)
    expect(original.fetch('payload')).to eq(Digest::SHA256.hexdigest("persistence-upgrade-payload\n"))
    expect(original.fetch('owner')).to eq(original.fetch('ids').fetch('preservation-test').join(':'))
    expect(original.fetch('machine_id')).to match(/\A[0-9a-f]{32}\z/)
    expect(original.fetch('metadata').split(':').first(3).join(':')).to eq('42:43:710')
    expect(original.fetch('metadata')).to eq(expected_source_metadata) if expected_source_metadata
    
    expect(original.fetch('payload_directory').split(':').first(3).join(':')).to eq(original.fetch('ids').fetch('preservation-test').join(':') + ':750')

    switch.call('/nix/store/h8w8sqm15xx6siccmzkqjkwmd0db24iw-nixos-system-persistence-fixture-26.05pre-git')
    healthy = snapshot.call(true)
    expect(healthy.reject { |key, _| key == 'ids' }).to eq(original.reject { |key, _| key == 'ids' })
    expect(healthy.fetch('ids').fetch('preservation-test')).to eq(original.fetch('ids').fetch('preservation-test'))
    expect(healthy.fetch('ids').fetch('a-preservation-test')).not_to eq(healthy.fetch('ids').fetch('preservation-test'))
    # Keep this old guest running: an old restart is the known defect.
# Only the raw compatibility source changes in this generation.
switch.call('/nix/store/jyinbn06b2csaydgh795lv7fflliivf1-nixos-system-persistence-fixture-26.05pre-git')
expect(snapshot.call(true)).to eq(healthy)

    switch.call('/nix/store/jyinbn06b2csaydgh795lv7fflliivf1-nixos-system-persistence-fixture-26.05pre-git')
    expect(snapshot.call(true)).to eq(healthy)
    machine.succeeds("osctl ct restart #{ct}")
    wait_for_guest_ready.call('restart')
    expect(exec_guest.call('readlink /run/current-system')).to eq('/nix/store/jyinbn06b2csaydgh795lv7fflliivf1-nixos-system-persistence-fixture-26.05pre-git')
    expect(snapshot.call(true)).to eq(healthy)
    
    
    saved_files = exec_guest.call('sha256sum /etc/passwd /etc/group /var/lib/nixos/uid-map /var/lib/nixos/gid-map /var/lib/preservation-test/payload')
# Positive execution control uses the complete generated activation
# and real allocator; trace markers do not replace it.
positive = "/root/persistence-#{ct}-positive.log"
machine.succeeds("osctl ct exec #{ct} bash -c #{Shellwords.escape('echo TRACE_BEGIN; bash -x /nix/store/jyinbn06b2csaydgh795lv7fflliivf1-nixos-system-persistence-fixture-26.05pre-git/activate; rc=$?; echo TRACE_END:$rc; exit $rc')} > #{positive} 2>&1")
trace = machine.succeeds("cat #{positive}")[1]
expect(trace).to include('TRACE_BEGIN', 'TRACE_END:0')
expect(trace).to match(/^\+.*perl.*-update-users-groups\.pl/)
failures = JSON.parse('{"ancestor-bind":"/nix/store/g173xi26n3r1m5wxlrg6j3g7x5fwyj3n-nixos-system-persistence-fixture-26.05pre-git","ancestor-conflict":"/nix/store/g36xs88xxi7kaqc7gjnbvvicgbhfvfw2-nixos-system-persistence-fixture-26.05pre-git","bind":"/nix/store/029gik57whq04lpliy11zzrxy7mii111-nixos-system-persistence-fixture-26.05pre-git","conflict":"/nix/store/dpzflznh736ala2dy8d9cskv8pwpazq4-nixos-system-persistence-fixture-26.05pre-git","missing":"/nix/store/v3r5indim8y5kbsxlv09jqpgf9jhqagj-nixos-system-persistence-fixture-26.05pre-git","nonbind":"/nix/store/vksfw8q7c8fapx24g3am6lzrql37mg4v-nixos-system-persistence-fixture-26.05pre-git","nonbind-positive":"/nix/store/7igzhii2m76mdnarqz6q55v95zg4fybz-nixos-system-persistence-fixture-26.05pre-git","nonbind-remount":"/nix/store/k8j2vnb306bmpq2f0iwb9mx4c6v53vn2-nixos-system-persistence-fixture-26.05pre-git","required-remount":"/nix/store/j1d02crqdc97dh96293nbcfarmzsvb2r-nixos-system-persistence-fixture-26.05pre-git","wrong-backing":"/nix/store/v3r5indim8y5kbsxlv09jqpgf9jhqagj-nixos-system-persistence-fixture-26.05pre-git"}')
# Visibility/order control: this log tmpfs is private to this
# activation; durable allocation state stays on its healthy bind.
nonbind = failures.delete('nonbind-positive')
nonbind_log = "/root/persistence-#{ct}-nonbind-positive.log"
command = "set -e; umount /var/log; echo TRACE_BEGIN; bash -x #{nonbind}/activate; rc=$?; echo TRACE_END:$rc; exit $rc"
machine.succeeds("osctl ct exec #{ct} unshare --mount --propagation private bash -c #{Shellwords.escape(command)} > #{nonbind_log} 2>&1")
trace = machine.succeeds("cat #{nonbind_log}")[1]
expect(trace).to include('TRACE_BEGIN', 'TRACE_END:0')
mount_position = trace.index(/^\++ mount -t tmpfs .* \/var\/log$/)
allocator_position = trace.index(/^\+.*perl.*-update-users-groups\.pl/)
expect(mount_position).not_to be_nil
expect(allocator_position).not_to be_nil
expect(mount_position).to be < allocator_position
expect(snapshot.call(true)).to eq(healthy)
failures.each do |failure, generation|
  # Isolate real mount faults without changing the live guest's
  # configured storage, maps or mounted destinations.
  preparation = case failure
  when 'missing'
    'test ! -e /persistent/required'
  when 'bind'
    'umount /var/lib/nixos'
  when 'conflict'
    'umount /var/lib/nixos; mkdir -p /run/wrong-state; mount --bind /run/wrong-state /var/lib/nixos'
  when 'wrong-backing'
    'mkdir -p /persistent/required /required-storage /run/wrong-backing; mount --bind /run/wrong-backing /required-storage; test ! -e /required-storage/absent-state'
  when 'ancestor-bind'
    'umount /var/lib/nixos; umount /var/lib/preservation-test; ! mountpoint -q /var/lib'
  when 'ancestor-conflict'
    'umount /var/lib/nixos; umount /var/lib/preservation-test; mkdir -p /run/wrong-ancestor; mount --bind /run/wrong-ancestor /var/lib'
  when 'nonbind'
    'umount /var/log; test ! -e /dev/no-such-persistence-device'
  when 'nonbind-remount'
    'umount /var/log; mount -t tmpfs tmpfs /var/log'
  when 'required-remount'
    'mkdir -p /required-storage; mount -t tmpfs tmpfs /required-storage; test ! -e /required-storage/absent-state'
  end
  # Each preparation must succeed; no artificial allocator marker.
  after_failure = failure == 'required-remount' ? 'mountpoint -q /required-storage && test ! -e /required-storage/absent-state && echo REQUIRED_STILL_PRESENT' : 'true'
  command = "set -e; #{preparation}; set +e; echo TRACE_BEGIN; bash -x #{generation}/activate; rc=$?; echo TRACE_END:$rc; #{after_failure}; exit $rc"
  log = "/root/persistence-#{ct}-#{failure}.log"
  machine.fails("osctl ct exec #{ct} unshare --mount --propagation private bash -c #{Shellwords.escape(command)} > #{log} 2>&1")
  trace = machine.succeeds("cat #{log}")[1]
  expect(trace).to include('TRACE_BEGIN', 'TRACE_END:1', 'refusing user allocation')
  expect(trace).to match(/^\++ source .*mounts/)
  expect(trace).to match(/^\++ exit 1$/)
  expect(trace).not_to match(/^\+.*perl.*-update-users-groups\.pl/)
  operation = case failure
  when 'nonbind'
    ['ext4', '/dev/no-such-persistence-device', '/var/log', %w[mode=0755]]
  when 'nonbind-remount'
    ['tmpfs', 'tmpfs', '/var/log', %w[remount size=invalid]]
  when 'required-remount'
    ['tmpfs', 'tmpfs', '/required-storage', %w[remount size=invalid]]
  when 'ancestor-bind'
    ['none', '/persistent/var/lib', '/var/lib', %w[bind remount]]
  end
  if operation
    fs_type, mount_source, mount_target, required_options = operation
    lines = trace.lines
    mount_position = lines.index do |line|
      next false unless line.match?(/\A\++ mount -t /)
      argv = Shellwords.split(line.sub(/\A\++ /, ""))
      argv.length == 7 && argv.first(4) == ['mount', '-t', fs_type, '-o'] &&
        argv.last(2) == [mount_source, mount_target] &&
        (required_options - argv[4].split(',')).empty?
    end
    refusal_position = lines.index { |line| line.match?(/\A\++ printf .*refusing user allocation/) }
    expect(mount_position).not_to be_nil
    expect(refusal_position).not_to be_nil
    expect(mount_position).to be < refusal_position
  end
  expect(trace).to include('REQUIRED_STILL_PRESENT') if failure == 'required-remount'
  expect(exec_guest.call('sha256sum /etc/passwd /etc/group /var/lib/nixos/uid-map /var/lib/nixos/gid-map /var/lib/preservation-test/payload')).to eq(saved_files)
  expect(snapshot.call(true)).to eq(healthy)
  exec_guest.call('test ! -e /persistent/required/absent-state && test ! -e /run/wrong-backing/absent-state') if failure == 'wrong-backing'
end

    machine.succeeds("osctl ct del -f --prune #{ct}")
  end
end
