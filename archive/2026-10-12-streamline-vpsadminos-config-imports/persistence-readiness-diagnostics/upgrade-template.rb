# Static template: all conditional bodies included; Nix values are placeholders.

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
        snapshot = lambda do |challenge|
          accounts = challenge ? %w[preservation-test a-preservation-test] : %w[preservation-test]
          ids = accounts.to_h do |account|
            live = exec_guest.call("id -u #{account}; id -g #{account}").split.map(&:to_i)
            saved = JSON.parse(exec_guest.call("jq -n --slurpfile u /var/lib/nixos/uid-map --slurpfile g /var/lib/nixos/gid-map --arg name #{account} '[$u[0][$name], $g[0][$name]]'"))
            backing = JSON.parse(exec_guest.call("jq -n --slurpfile u /fixture/source/var/lib/nixos/uid-map --slurpfile g /fixture/source/var/lib/nixos/gid-map --arg name #{account} '[$u[0][$name], $g[0][$name]]'"))
            expect(live).to eq(saved), "live IDs differ from allocation maps for #{account}"
            expect(saved).to eq(backing), "visible and backing maps differ for #{account}"
            [account, live]
          end
          %w[/var/lib/nixos /var/log].each do |target|
            exec_guest.call("mountpoint -q #{target} && test /fixture/source#{target} -ef #{target}")
            expect(exec_guest.call("awk '$5 == \"#{target}\" {n++} END {print n+0}' /proc/self/mountinfo")).to eq('1')
          end
          exec_guest.call('test /fixture/source/var/lib/preservation-test/payload -ef /var/lib/preservation-test/payload && test /fixture/source/etc/machine-id -ef /etc/machine-id')
          {
            'ids' => ids,
            'mount_options' => %w[/var/lib/nixos /var/log].to_h { |target| [target, exec_guest.call("findmnt -n -o OPTIONS --mountpoint #{target}")] },
            'machine_id' => exec_guest.call('cat /etc/machine-id'),
            'payload' => exec_guest.call('sha256sum /var/lib/preservation-test/payload').split.first,
            'owner' => exec_guest.call("stat -c '%u:%g' /var/lib/preservation-test/payload"),
            'metadata' => exec_guest.call("stat -c '%u:%g:%a:%i' /fixture/source/var/lib/nixos")
          }
        end

        describe '/fixture/source /fixture/source' do
          it 'retains dynamic accounts, maps, data and bind identity' do
            puts 'Old compatibility source: /fixture/source (/fixture/source)'
            puts 'Candidate compatibility source: /fixture/source'
            puts 'Guest release /fixture/source; stateVersion 22.11'
            
                  puts 'Fresh candidate generations /fixture/source -> /fixture/source'
                

                  puts 'Prepared old-to-new generations /fixture/source -> /fixture/source -> /fixture/source'
                
            machine.all_succeed(
              "osctl ct new --skip-image --distribution nixos --version /fixture/source --arch x86_64 #{ct}",
              "osctl ct unset start-menu #{ct}",
              "osctl ct dataset new #{ct} nix",
              # Shared closures are read-only; the host overlay store cannot be
              # ID-mapped. Container datasets keep their native mappings.
              "osctl ct mounts new --fs /nix/store --type bind --opts bind,ro,create=dir --mountpoint /nix/store --no-map-ids #{ct}",
            )
            rootfs = machine.osctl_json("ct show #{ct}").fetch('rootfs')
            nix_root = machine.osctl_json("ct mounts ls #{ct}").find { |mount| mount.fetch('mountpoint') == '/nix' }.fetch('fs')
            machine.all_succeed(
              "mkdir -p #{nix_root}/var/nix/profiles #{rootfs}/sbin #{rootfs}/etc #{rootfs}/var",
              "ln -s /fixture/source #{nix_root}/var/nix/profiles/system",
              "ln -s /fixture/source/init #{rootfs}/sbin/init",
            )
                          machine.all_succeed(
                # The CLI mounts subdatasets; '/' denotes root only in image
                # configuration. Bind this container's queried private root.
                "osctl ct mounts new --fs #{rootfs} --type bind --opts bind,create=dir,rw --mountpoint /persistent #{ct}",
                "osctl ct set impermanence #{ct}",
              )

                          # Provision the old configuration's declared backing sources;
              # this is setup, before any accounts or data exist.
              machine.all_succeed(
                "mkdir -p #{rootfs}/backing/var/lib/nixos #{rootfs}/backing/var/lib/preservation-test #{rootfs}/backing/var/log #{rootfs}/backing/etc",
                "touch #{rootfs}/backing/etc/machine-id",
              )

                          machine.succeeds("mkdir -p #{rootfs}/var/lib/nixos/usr")

                          machine.fails("test -e #{rootfs}/var/lib/nixos")

            machine.succeeds("osctl ct start #{ct}")
            wait_for_guest_ready.call('initial boot')
            expect(exec_guest.call('nixos-version')).to start_with('/fixture/source')
            exec_guest.call('nix-store --load-db < /fixture/source/registration')
                          # The old boot has already mounted state. A normal old live
              # switch establishes healthy persisted maps; no ID/map repair.
              switch.call('/fixture/source')

            exec_guest.call("printf '%s\\n' persistence-upgrade-payload > /var/lib/preservation-test/payload && chown preservation-test:preservation-test /var/lib/preservation-test/payload")
            original = snapshot.call(false)
            expect(original.fetch('payload')).to eq(Digest::SHA256.hexdigest("persistence-upgrade-payload\n"))
            expect(original.fetch('owner')).to eq(original.fetch('ids').fetch('preservation-test').join(':'))
            expect(original.fetch('machine_id')).to match(/\A[0-9a-f]{32}\z/)

            switch.call('/fixture/source')
            healthy = snapshot.call(true)
            expect(healthy.reject { |key, _| key == 'ids' }).to eq(original.reject { |key, _| key == 'ids' })
            expect(healthy.fetch('ids').fetch('preservation-test')).to eq(original.fetch('ids').fetch('preservation-test'))
            expect(healthy.fetch('ids').fetch('a-preservation-test')).not_to eq(healthy.fetch('ids').fetch('preservation-test'))
                          # Keep this old guest running: an old restart is the known defect.
              # Only the raw compatibility source changes in this generation.
              switch.call('/fixture/source')
              expect(snapshot.call(true)).to eq(healthy)

            switch.call('/fixture/source')
            expect(snapshot.call(true)).to eq(healthy)
            machine.succeeds("osctl ct restart #{ct}")
            wait_for_guest_ready.call('restart')
            expect(exec_guest.call('readlink /run/current-system')).to eq('/fixture/source')
            expect(snapshot.call(true)).to eq(healthy)
                          exec_guest.call('test /persistent/backing -ef /guest-backing')
              expect(exec_guest.call("findmnt -n -o OPTIONS --mountpoint /guest-backing")).to include('rw')

                          exec_guest.call('test /persistent/var/lib/nixos/usr -ef /usr')
              expect(exec_guest.call("awk '$5 == \"/usr\" {n++} END {print n+0}' /proc/self/mountinfo")).to eq('1')

                          saved_files = exec_guest.call('sha256sum /etc/passwd /etc/group /var/lib/nixos/uid-map /var/lib/nixos/gid-map /var/lib/preservation-test/payload')
              # Positive execution control uses the complete generated activation
              # and real allocator; trace markers do not replace it.
              positive = "/root/persistence-#{ct}-positive.log"
              machine.succeeds("osctl ct exec #{ct} bash -c #{Shellwords.escape('echo TRACE_BEGIN; bash -x /fixture/source/activate; rc=$?; echo TRACE_END:$rc; exit $rc')} > #{positive} 2>&1")
              trace = machine.succeeds("cat #{positive}")[1]
              expect(trace).to include('TRACE_BEGIN', 'TRACE_END:0')
              expect(trace).to match(/^\+.*perl.*-update-users-groups\.pl/)
              failures = JSON.parse('/fixture/source')
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
                end
                # Each preparation must succeed; no artificial allocator marker.
                command = "set -e; #{preparation}; set +e; echo TRACE_BEGIN; bash -x #{generation}/activate; rc=$?; echo TRACE_END:$rc; exit $rc"
                log = "/root/persistence-#{ct}-#{failure}.log"
                machine.fails("osctl ct exec #{ct} unshare --mount --propagation private bash -c #{Shellwords.escape(command)} > #{log} 2>&1")
                trace = machine.succeeds("cat #{log}")[1]
                expect(trace).to include('TRACE_BEGIN', 'TRACE_END:1', 'refusing user allocation')
                expect(trace).to match(/^\++ source .*mounts/)
                expect(trace).to match(/^\++ exit 1$/)
                expect(trace).not_to match(/^\+.*perl.*-update-users-groups\.pl/)
                expect(exec_guest.call('sha256sum /etc/passwd /etc/group /var/lib/nixos/uid-map /var/lib/nixos/gid-map /var/lib/preservation-test/payload')).to eq(saved_files)
                expect(snapshot.call(true)).to eq(healthy)
                exec_guest.call('test ! -e /persistent/required/absent-state && test ! -e /run/wrong-backing/absent-state') if failure == 'wrong-backing'
              end

            machine.succeeds("osctl ct del -f --prune #{ct}")
          end
        end
