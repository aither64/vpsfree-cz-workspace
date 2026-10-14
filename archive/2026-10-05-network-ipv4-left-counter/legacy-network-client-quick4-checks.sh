#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
prefix=legacy-network-client-quick4
cd "$v_root"
mapfile -t paths < "$tracking/$prefix.paths"
case "${1-}" in
  formatter)
    for path in "${paths[@]}"; do
      php-cs-fixer fix --dry-run --diff --using-cache=no --config="$v_root/.php-cs-fixer.dist.php" "$path"
    done
    ;;
  syntax)
    for path in "${paths[@]}"; do php -l "$path"; done
    ;;
  phpunit)
    cd "$v_root/webui"
    [[ ! -e "$tracking/$prefix-phpunit.xml" ]]
    php --version
    php -r 'require "vendor/autoload.php"; printf("HaveAPI PHP client %s\n", HaveAPI\Client::VERSION);'
    vendor/bin/phpunit -c phpunit.xml.dist \
      --cache-directory "$tracking/$prefix-phpunit-cache" \
      --do-not-record-test-run-history \
      --log-junit "$tracking/$prefix-phpunit.xml"
    ;;
  locales)
    cd "$v_root/webui"
    lang/scripts/locales-health
    ;;
  *) exit 2 ;;
esac
