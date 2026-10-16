
                systemctl --failed --plain --no-legend --no-pager | head -n 8 |
                  while read -r unit rest; do
                    printf '\n--- failed unit %s ---\n' "$unit"
                    systemctl status "$unit" --no-pager --full --lines=40
                    systemctl show "$unit" -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus
                    journalctl -b -u "$unit" --no-pager -n 40 -o short-iso-precise
                  done
