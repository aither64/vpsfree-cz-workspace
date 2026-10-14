#!/usr/bin/env bash
set -euo pipefail
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$v_root"
case "$1" in
  ruby)
    mapfile -t changed < <(git diff --name-only -- '*.rb')
    mapfile -t added < <(git ls-files --others --exclude-standard -- '*.rb')
    for path in "${changed[@]}" "${added[@]}"; do ruby -c "$path"; done
    bundle exec rubocop --force-exclusion "${changed[@]}" "${added[@]}"
    ruby tests/ci-selection-test.rb
    ;;
  php-locales)
    cd webui
    lang/scripts/locales-update
    lang/scripts/locales-health
    ;;
  php|php-csrf)
    for path in webui/forms/cluster.forms.php webui/forms/networking.forms.php webui/lib/functions.lib.php webui/pages/page_cluster.php webui/tests/Regression/CsrfStateFormsTest.php webui/tests/Regression/NetworkAvailabilityTest.php; do
      php -l "$path"
    done
    cd webui
    if [[ $1 == php-csrf ]]; then
      vendor/bin/phpunit -c phpunit.xml.dist --filter CsrfStateFormsTest
    else
      vendor/bin/phpunit -c phpunit.xml.dist
    fi
    ;;
  php-format)
    for path in webui/forms/cluster.forms.php webui/forms/networking.forms.php webui/lib/functions.lib.php webui/pages/page_cluster.php webui/tests/Regression/CsrfStateFormsTest.php webui/tests/Regression/NetworkAvailabilityTest.php; do
      php-cs-fixer fix --dry-run --diff "$path"
    done
    ;;
  nix)
    nixfmt --check tests/suite/network/network-interface-routes-and-host-ips.nix tests/suite/network/export-lifecycle.nix tests/suite/vps/migrate-with-data-check.nix tests/suite/storage/restore-after-reinstall-with-descendants-remote.nix
    ;;
  *) exit 2 ;;
esac
