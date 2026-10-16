#!/usr/bin/env bash
# Static text rewrite only: no callbacks, mount doubles or allocator.
set -euo pipefail
fixture_source='/fixture-case/backing storage/nixos'
fixture_backing='/fixture-case/backing storage'
fixture_host='/fixture-case/host storage'
fixture_bridge=/fixture-case/bridge
fixture_dependency=/fixture-case/dependency
fixture_case_root=/fixture-case
fixture_target=/fixture-case/state_target
fixture_log_target=/fixture-case/log_target
configured_target=$1
  rewrite() {
    sed -e "s|/fixture/backing storage/nixos|$fixture_source|g" \
      -e "s|/fixture/bridge/state|$fixture_source|g" \
      -e "s|/fixture/backing storage|$fixture_backing|g" \
      -e "s|/fixture/host storage|$fixture_host|g" \
      -e "s|/fixture/bridge|$fixture_bridge|g" \
      -e "s|/fixture/dependency|$fixture_dependency|g" \
      -e "s|/fixture/device-file|$fixture_source|g" \
      -e "s|/fixture/unrelated|$fixture_case_root/unrelated|g" \
      -e "s|\"$configured_target\"|\"$fixture_target\"|g" \
      -e "s|'$configured_target'|'$fixture_target'|g" \
      -e "s|= $configured_target ]|= '$fixture_target' ]|g" \
      -e "s|\"/var/log\"|\"$fixture_log_target\"|g" \
      -e "s|'/var/log'|'$fixture_log_target'|g" \
      -e "s|= /var/log ]|= '$fixture_log_target' ]|g" "$1"
  }
rewrite "$2"
