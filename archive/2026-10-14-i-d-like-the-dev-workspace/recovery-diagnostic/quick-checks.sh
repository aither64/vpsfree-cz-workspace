#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
source ../runtime-dev-env.sh
test "$(command -v ruby)" = /nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9/bin/ruby
ruby --version
ruby -c raise-observer.rb
ruby -c check-observer.rb
ruby check-observer.rb
python3 check-static.py
bash -n quick-checks.sh run-diagnostic.sh
