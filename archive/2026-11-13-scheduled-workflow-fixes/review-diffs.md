# Complete final diffs

## vpsfree-cz-configuration

~~~~diff
diff --git a/.github/workflows/daily-update.yml b/.github/workflows/daily-update.yml
index 7924a25e..b64c840f 100644
--- a/.github/workflows/daily-update.yml
+++ b/.github/workflows/daily-update.yml
@@ -34,8 +34,10 @@ jobs:
 
       - name: Install git hooks
         run: |
-          nix develop -c bundle exec overcommit --install
-          nix develop -c bundle exec overcommit --sign pre-commit
+          # Input updates can change Ruby; keep native gems and hooks on the
+          # original shell for this entire run.
+          nix develop --profile "$RUNNER_TEMP/daily-update-dev-shell" -c bundle exec overcommit --install
+          nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c bundle exec overcommit --sign pre-commit
 
       - name: Restore confctl cache
         uses: actions/cache/restore@v6
@@ -49,7 +51,7 @@ jobs:
         run: |
           set -euo pipefail
 
-          nix develop -c bash <<'EOF'
+          nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c bash <<'EOF'
             set -euo pipefail
 
             sudo mkdir "/nix/var/nix/gcroots/per-user/$USER"
@@ -65,7 +67,7 @@ jobs:
         run: |
           set -euo pipefail
 
-          nix develop -c bash <<'EOF'
+          nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c bash <<'EOF'
             set -euo pipefail
 
             codex_version_expr='let flake = builtins.getFlake (toString ./.); in flake.inputs.llm-agents.packages.x86_64-linux.codex.version'
@@ -97,7 +99,7 @@ jobs:
         run: |
           set -e
 
-          nix develop -c bash <<'EOF'
+          nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c bash <<'EOF'
             set -euo pipefail
 
             commit_update() {
@@ -178,7 +180,7 @@ jobs:
         run: |
           set -euo pipefail
 
-          nix develop -c bash <<'EOF'
+          nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c bash <<'EOF'
             set -euo pipefail
             git show HEAD:flake.lock > "$RUNNER_TEMP/flake-update-final.lock"
             nix shell "$CONFCTL_FLAKE" -c confctl inputs check-update \
~~~~

## vpsadminos-org-configuration

~~~~diff
diff --git a/.github/workflows/daily-update.yml b/.github/workflows/daily-update.yml
index 468673b..15c6161 100644
--- a/.github/workflows/daily-update.yml
+++ b/.github/workflows/daily-update.yml
@@ -35,6 +35,7 @@ jobs:
         run: |
           nix develop -c bundle exec overcommit --install
           nix develop -c bundle exec overcommit --sign
+          nix develop -c bundle exec overcommit --sign pre-commit
 
       - name: Restore confctl cache
         uses: actions/cache/restore@v6
~~~~

## vpsfree-irc-bot

~~~~diff
diff --git a/.github/workflows/daily-update.yml b/.github/workflows/daily-update.yml
index 6a1ff24..55872d3 100644
--- a/.github/workflows/daily-update.yml
+++ b/.github/workflows/daily-update.yml
@@ -10,7 +10,7 @@ jobs:
   update:
     runs-on: ubuntu-latest
     steps:
-      - uses: actions/checkout@v6
+      - uses: actions/checkout@v7
         with:
           fetch-depth: 0
 
@@ -22,23 +22,34 @@ jobs:
           git config user.email "github-actions[bot]@users.noreply.github.com"
 
       - name: Update package dependencies
+        id: update
         run: |
           # Until [bundix#68](https://github.com/nix-community/bundix/pull/68) is resolved
-          nix develop -c bash -lc '
+          nix develop -c bash -euo pipefail <<'BASH'
+            # Avoid activating the old bundle while replacing its lock or running Bundix's Ruby.
+            unset RUBYOPT
             bundle config set --local force_ruby_platform true
             rm -f gemset.nix Gemfile.lock
             bundle lock --add-platform ruby
             BUNDLE_FORCE_RUBY_PLATFORM=true bundix -l
-          '
-
-          git add gemset.nix Gemfile.lock
-          git diff --cached --quiet && exit 0
-
-          msg="$(mktemp)"
-          trap 'rm -f "$msg"' EXIT
-          printf 'Update dependencies\n' > "$msg"
-          git commit -F "$msg"
+            NIX_ENFORCE_PURITY=0 bundle install
+            bundle exec overcommit --install
+            bundle exec overcommit --sign
+
+            git add gemset.nix Gemfile.lock
+            if git diff --cached --quiet; then
+              echo "committed=false" >> "$GITHUB_OUTPUT"
+              exit 0
+            fi
+
+            msg="$(mktemp)"
+            trap 'rm -f "$msg"' EXIT
+            printf 'Update dependencies\n' > "$msg"
+            git commit -F "$msg"
+            echo "committed=true" >> "$GITHUB_OUTPUT"
+          BASH
 
       - name: Push updates
+        if: steps.update.outputs.committed == 'true'
         run: |
           git push origin HEAD:master
diff --git a/README.md b/README.md
index 07ba1ee..bf3ec0c 100644
--- a/README.md
+++ b/README.md
@@ -83,17 +83,26 @@ each channel. An absent or empty list preserves the existing announcement
 format and routing behavior.
 
 ## Bundix
-Until [bundix#68](https://github.com/nix-community/bundix/pull/68) is resolved, use:
 
-     nix develop -c bash -lc '
-       bundle config set --local force_ruby_platform true
-       rm -f gemset.nix Gemfile.lock
-       bundle lock --add-platform ruby
-       BUNDLE_FORCE_RUBY_PLATFORM=true bundix -l
-     '
-
-Our issue is with nokogiri, which uses platform-specific gems that bundler has
-problems with.
+Until [bundix#68](https://github.com/nix-community/bundix/pull/68) is resolved,
+generate Nokogiri's source-gem dependencies with:
+
+```bash
+nix develop -c bash -euo pipefail <<'BASH'
+  unset RUBYOPT
+  bundle config set --local force_ruby_platform true
+  rm -f gemset.nix Gemfile.lock
+  bundle lock --add-platform ruby
+  BUNDLE_FORCE_RUBY_PLATFORM=true bundix -l
+  NIX_ENFORCE_PURITY=0 bundle install
+BASH
+```
+
+The development shell preloads `bundler/setup` through `RUBYOPT`. Clear it while
+replacing the lock and running Bundix, which uses its own Ruby bundle. Forcing
+the Ruby platform avoids Nokogiri's platform-specific gem resolution problem.
+Install the refreshed bundle with the bot's Ruby before running checks or
+committing; native dependencies need `NIX_ENFORCE_PURITY=0`.
 
 ## Automated flake updates
 
~~~~

## vpsadmin

~~~~diff
diff --git a/api/spec/migrations/20260707140000_add_sysconfig_localized_spec.rb b/api/spec/migrations/20260707140000_add_sysconfig_localized_spec.rb
index 75853aa73..df550095a 100644
--- a/api/spec/migrations/20260707140000_add_sysconfig_localized_spec.rb
+++ b/api/spec/migrations/20260707140000_add_sysconfig_localized_spec.rb
@@ -46,7 +46,7 @@ RSpec.describe AddSysconfigLocalized do
     migrate_up!
 
     expect(column_exists?(:sysconfig, :localized)).to be(true)
-    expect(column(:sysconfig, :localized).default).to be(false)
+    expect(column(:sysconfig, :localized).default).to eq('0')
 
     noticeboard = find_row(:sysconfig, category: 'webui', name: 'noticeboard')
     expect(boolish(noticeboard.fetch('localized'))).to be(true)
diff --git a/api/spec/migrations/20260713120100_add_node_kernel_history_spec.rb b/api/spec/migrations/20260713120100_add_node_kernel_history_spec.rb
index 1c5ee20a0..365eaf405 100644
--- a/api/spec/migrations/20260713120100_add_node_kernel_history_spec.rb
+++ b/api/spec/migrations/20260713120100_add_node_kernel_history_spec.rb
@@ -29,7 +29,7 @@ RSpec.describe AddNodeKernelHistory do
     expect(table_exists?(:node_kernel_events)).to be(true)
     expect(column(:node_kernel_events, :reported_release).null).to be(false)
     expect(column(:node_kernel_events, :observed_before).null).to be(false)
-    expect(column(:node_kernel_events, :current).default).to be(false)
+    expect(column(:node_kernel_events, :current).default).to eq('0')
     expect(column_exists?(:node_kernel_events, :source_status_id)).to be(true)
     expect(column_exists?(:node_kernel_events, :evidence)).to be(false)
     expect(index_exists?(:node_kernel_events, %i[node_id observed_before])).to be(true)
diff --git a/api/spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb b/api/spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb
index 3d971af10..5de9d3ccb 100644
--- a/api/spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb
+++ b/api/spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb
@@ -67,7 +67,7 @@ RSpec.describe AddNodeKernelEvidence do
       %w[node_kernel_evidence_id generation component]
     )
     expect(software_index.unique).to be(true)
-    expect(column(:node_software_versions, :revision_dirty).default).to be(false)
+    expect(column(:node_software_versions, :revision_dirty).default).to eq('0')
     expect(column(:node_software_versions, :revision_dirty).null).to be(false)
   end
 
diff --git a/api/spec/migrations/20260716120000_add_node_system_states_spec.rb b/api/spec/migrations/20260716120000_add_node_system_states_spec.rb
index 06182012c..6d2b4caca 100644
--- a/api/spec/migrations/20260716120000_add_node_system_states_spec.rb
+++ b/api/spec/migrations/20260716120000_add_node_system_states_spec.rb
@@ -32,7 +32,7 @@ RSpec.describe AddNodeSystemStates do
     expect(column(:node_system_states, :cpus).null).to be(true)
     expect(column(:node_system_states, :first_observed_at).null).to be(false)
     expect(column(:node_system_states, :last_observed_at).null).to be(false)
-    expect(column(:node_system_states, :current).default).to be(false)
+    expect(column(:node_system_states, :current).default).to eq('0')
     expect(index_exists?(:node_system_states, %i[node_id first_observed_at])).to be(true)
     expect(index_exists?(:node_system_states, %i[node_id current])).to be(true)
   end
diff --git a/api/spec/migrations/20260716120100_make_node_capacity_reported_spec.rb b/api/spec/migrations/20260716120100_make_node_capacity_reported_spec.rb
index 5f166fe5c..731d294a0 100644
--- a/api/spec/migrations/20260716120100_make_node_capacity_reported_spec.rb
+++ b/api/spec/migrations/20260716120100_make_node_capacity_reported_spec.rb
@@ -18,9 +18,9 @@ RSpec.describe MakeNodeCapacityReported do
   it 'defaults the legacy rollback cache for capacity-optional registration' do
     migrate_up!
 
-    expect(column(:nodes, :cpus).default).to eq(0)
-    expect(column(:nodes, :total_memory).default).to eq(0)
-    expect(column(:nodes, :total_swap).default).to eq(0)
+    expect(column(:nodes, :cpus).default).to eq('0')
+    expect(column(:nodes, :total_memory).default).to eq('0')
+    expect(column(:nodes, :total_swap).default).to eq('0')
   end
 
   it 'removes the cache defaults on rollback' do
diff --git a/api/spec/migrations/20260818115900_add_authentication_generation_spec.rb b/api/spec/migrations/20260818115900_add_authentication_generation_spec.rb
index d714ef437..aae9c8f63 100644
--- a/api/spec/migrations/20260818115900_add_authentication_generation_spec.rb
+++ b/api/spec/migrations/20260818115900_add_authentication_generation_spec.rb
@@ -17,7 +17,7 @@ RSpec.describe AddAuthenticationGeneration do
     expect(column(:users, :authentication_generation)).to have_attributes(
       type: :integer,
       null: false,
-      default: 0
+      default: '0'
     )
   end
 
diff --git a/api/spec/migrations/20260818120000_add_password_recovery_spec.rb b/api/spec/migrations/20260818120000_add_password_recovery_spec.rb
index a6fae6941..c06bfce25 100644
--- a/api/spec/migrations/20260818120000_add_password_recovery_spec.rb
+++ b/api/spec/migrations/20260818120000_add_password_recovery_spec.rb
@@ -25,7 +25,7 @@ RSpec.describe AddPasswordRecovery do
     expect(column(:oauth2_clients, :authorization_start_requires_user_action)).to have_attributes(
       type: :boolean,
       null: false,
-      default: false
+      default: '0'
     )
     expect(index_exists?(:users, [:email])).to be(true)
     expect(table_exists?(:password_recovery_submissions)).to be(true)
diff --git a/api/spec/migrations/20260821120000_add_password_event_counters_spec.rb b/api/spec/migrations/20260821120000_add_password_event_counters_spec.rb
index 640177bab..2772ac85c 100644
--- a/api/spec/migrations/20260821120000_add_password_event_counters_spec.rb
+++ b/api/spec/migrations/20260821120000_add_password_event_counters_spec.rb
@@ -17,7 +17,7 @@ RSpec.describe AddPasswordEventCounters do
     expect(column(:password_event_counters, :event_count)).to have_attributes(
       type: :integer,
       null: false,
-      default: 0,
+      default: '0',
       unsigned?: true
     )
     expect(column_exists?(:password_event_counters, :last_occurred_at)).to be(true)
diff --git a/api/spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb b/api/spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb
index a6785b1f4..7a2a8c69c 100644
--- a/api/spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb
+++ b/api/spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb
@@ -11,7 +11,7 @@ RSpec.describe AddIpReleaseCampaigns do
     insert_row(:ip_release_attempt_addresses, membership)
     expect { insert_row(:ip_release_attempt_addresses, membership) }.to raise_error(ActiveRecord::RecordNotUnique)
     insert_row(:ip_release_attempt_addresses, membership.merge(ip_release_attempt_id: 2))
-    expect(column(:ip_release_campaigns, :allow_keep).default).to be(true)
+    expect(column(:ip_release_campaigns, :allow_keep).default).to eq('1')
     attrs = {
       ip_release_request_id: 1, ip_address_id: 10, active_ip_address_id: 10,
       network_id: 1, address: '192.0.2.10', prefix: 32, size: 1,
~~~~

## haveapi

~~~~diff
diff --git a/clients/python/CONTRIBUTING.md b/clients/python/CONTRIBUTING.md
index a8062c85..37f22f0f 100644
--- a/clients/python/CONTRIBUTING.md
+++ b/clients/python/CONTRIBUTING.md
@@ -30,15 +30,18 @@ through 3.15. Each checkout resolves compatible development dependencies into
 its local lock; package dependencies keep compatible runtime ranges for
 consumers. Separate checkouts can resolve different versions.
 
-Ruff is pinned to 0.17.2 to match the native executable in the locked Nixpkgs.
+The exact Ruff development pin matches the native executable in locked Nixpkgs.
 `run_ruff.py` selects `HAVEAPI_RUFF` in Nix and checks that its version matches
 the installed locked Python distribution. Elsewhere it runs the locked Ruff
 executable. This avoids invoking PyPI's generic Linux ELF on NixOS and preserves
 formatter parity with CI. The `python-ruff-parity` flake check requires exactly
 one exact Ruff dev pin matching the selected Nix package and its executable.
-The Nixpkgs updater runs this check through `nix flake check` before committing
-an input update. Keep the Nix input and Ruff pin in sync, then run `uv sync`
-to refresh the local environment.
+The Nixpkgs updater reads Ruff's version from the newly locked Nixpkgs and
+updates the development pin. It runs `nix flake check`, then enters the newly
+locked `client-python` shell, runs `uv sync`, and checks Python formatting and
+lint with `run_ruff.py` before committing the pin and `flake.lock` together.
+The updater does not reformat Python source. For manual input changes, keep the
+Nix input and Ruff pin in sync, then run `uv sync` to refresh the local environment.
 Mypy and pytest run from the uv environment.
 
 The build requirement `uv_build>=0.13.0,<0.14` admits the locked Nix uv's native
diff --git a/doc/agent-instructions/development.md b/doc/agent-instructions/development.md
index 596c43ef..96656b05 100644
--- a/doc/agent-instructions/development.md
+++ b/doc/agent-instructions/development.md
@@ -86,8 +86,16 @@ repository root unless explicitly stated otherwise.
   `.github/workflows/update-nixpkgs.yml`, then run `./utils/update-nixpkgs.sh`
   and review its generated commit.
   The helper uses confctl's forward-only guard; a rejection or unavailable
-  ancestry evidence stops the update. The workflow saves the original lock
-  outside the checkout and checks the final lock again before its ordinary
+  ancestry evidence stops the update. It requires Python 3.11 or newer with
+  `tomllib`, reads Ruff's version from the newly locked host Nixpkgs, and updates
+  the exact Python development pin before running `nix flake check`. It requires
+  both `flake.lock` and `clients/python/pyproject.toml` to be clean and an empty
+  staging area; only the checked lock/pin pair enters its generated commit.
+  Before staging, it enters the newly locked `client-python` shell, runs
+  `uv sync`, and checks Python formatting and lint with `run_ruff.py`.
+  Failure stops the update before staging or committing. The updater does not
+  reformat source or track the local `uv.lock`. The workflow saves the original
+  lock outside the checkout and checks the final lock again before its ordinary
   non-force push. If the target branch advances, rerun from its new baseline;
   do not rebase an old generated lock update. The commit subject must be
   `flake: nixpkgs <oldrev11> -> <newrev11>`.
diff --git a/utils/sync-ruff.py b/utils/sync-ruff.py
new file mode 100644
index 00000000..a2201edf
--- /dev/null
+++ b/utils/sync-ruff.py
@@ -0,0 +1,60 @@
+"""Keep the exact Python Ruff dev pin aligned with the selected Nix package."""
+
+from __future__ import annotations
+
+import re
+import sys
+import tomllib
+from pathlib import Path
+
+
+def sync_ruff(path: Path, version: str) -> None:
+    if re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version) is None:
+        raise ValueError(f"invalid Nix Ruff version: {version!r}")
+
+    text = path.read_bytes().decode("utf-8")
+    document = tomllib.loads(text)
+    groups = document.get("dependency-groups", {})
+    if not isinstance(groups, dict) or not isinstance(groups.get("dev"), list):
+        raise ValueError("expected a dev dependency group")
+    requirements = groups["dev"]
+    ruff = [
+        (index, requirement)
+        for index, requirement in enumerate(requirements)
+        if isinstance(requirement, str)
+        and re.match(r"\s*ruff(?:[^A-Za-z0-9._-]|$)", requirement, re.IGNORECASE)
+    ]
+    if len(ruff) != 1:
+        raise ValueError("expected exactly one Ruff dev requirement")
+    index, requirement = ruff[0]
+    pin = re.fullmatch(
+        r"\s*ruff\s*==\s*([0-9]+\.[0-9]+\.[0-9]+)\s*", requirement, re.IGNORECASE
+    )
+    if pin is None:
+        raise ValueError("expected an exact Ruff dev pin (ruff==X.Y.Z)")
+    if pin[1] == version:
+        return
+
+    requirements[index] = (
+        requirement[: pin.start(1)] + version + requirement[pin.end(1) :]
+    )
+    candidates = []
+    for match in re.finditer(r"(['\"])" + re.escape(requirement) + r"\1", text):
+        start = match.start() + 1 + pin.start(1)
+        end = match.start() + 1 + pin.end(1)
+        updated = text[:start] + version + text[end:]
+        if tomllib.loads(updated) == document:
+            candidates.append(updated)
+    if len(candidates) != 1:
+        raise ValueError(
+            "could not identify one Ruff dev pin without changing other TOML"
+        )
+    path.write_bytes(candidates[0].encode("utf-8"))
+    print(f"Python Ruff: {pin[1]} -> {version}")
+
+
+if __name__ == "__main__":
+    try:
+        sync_ruff(Path("clients/python/pyproject.toml"), sys.argv[1])
+    except (IndexError, OSError, UnicodeError, ValueError) as error:
+        sys.exit(f"error: {error}")
diff --git a/utils/test_update_nixpkgs.py b/utils/test_update_nixpkgs.py
new file mode 100644
index 00000000..1dd1d1e7
--- /dev/null
+++ b/utils/test_update_nixpkgs.py
@@ -0,0 +1,264 @@
+"""Exercise pin synchronization and updater Git boundaries without remote writes."""
+
+from __future__ import annotations
+
+import json
+import os
+import subprocess
+import sys
+import tempfile
+import unittest
+from pathlib import Path
+
+UTILS = Path(__file__).resolve().parent
+OLD_REV = "a" * 40
+NEW_REV = "b" * 40
+PROJECT = b'[dependency-groups]\ndev = ["ruff==1.2.3", "pytest>=9"]\n'
+NIX = """#!/usr/bin/env python3
+import json
+import os
+import pathlib
+import sys
+import tomllib
+
+args = sys.argv[1:]
+with open('nix-calls', 'a') as log:
+    log.write(' '.join(args) + '\\n')
+lock = pathlib.Path('flake.lock')
+if args[:1] == ['shell'] and args[-1:] == ['nixpkgs']:
+    if 'ls' in args:
+        rev = json.loads(lock.read_text())['rev']
+        print(json.dumps([{'input': 'nixpkgs', 'rev': rev}]))
+    else:
+        assert '--forward-only' in args
+        if os.environ.get('UPDATE_EXIT'):
+            sys.exit(int(os.environ['UPDATE_EXIT']))
+        lock.write_text(json.dumps({'rev': os.environ['NEW_REV']}))
+elif args[:1] == ['eval']:
+    assert 'builtins.currentSystem' in args[-1]
+    assert 'inputs.nixpkgs.legacyPackages' in args[-1]
+    print(os.environ.get('RUFF_VERSION', '1.2.4'))
+elif args == ['flake', 'check']:
+    project = pathlib.Path('clients/python/pyproject.toml')
+    requirements = tomllib.loads(project.read_text())['dependency-groups']['dev']
+    assert 'ruff==' + os.environ.get('RUFF_VERSION', '1.2.4') in requirements
+    sys.exit(int(os.environ.get('CHECK_EXIT', '0')))
+elif args[:3] == ['develop', '.#client-python', '-c']:
+    os.execvp(args[3], args[3:])
+else:
+    sys.exit('unexpected Nix invocation: ' + repr(args))
+"""
+UV = """#!/usr/bin/env python3
+import os
+import pathlib
+import sys
+
+args = sys.argv[1:]
+with open('../../uv-calls', 'a') as log:
+    log.write(' '.join(args) + '\\n')
+if args == ['sync']:
+    pathlib.Path('uv.lock').write_text('fixture local lock')
+    sys.exit(int(os.environ.get('UV_SYNC_EXIT', '0')))
+assert args[:4] == ['run', '--locked', 'python', 'utils/run_ruff.py']
+if args[4:] == ['format', '--check', '.']:
+    sys.exit(int(os.environ.get('RUFF_FORMAT_EXIT', '0')))
+if args[4:] == ['check', '.']:
+    sys.exit(int(os.environ.get('RUFF_CHECK_EXIT', '0')))
+sys.exit('unexpected uv invocation: ' + repr(args))
+"""
+
+
+class UpdateNixpkgsTest(unittest.TestCase):
+    def setUp(self) -> None:
+        temporary = tempfile.TemporaryDirectory(prefix="haveapi-update-test-")
+        self.addCleanup(temporary.cleanup)
+        self.root = Path(temporary.name)
+        self.project = self.root / "clients/python/pyproject.toml"
+        self.project.parent.mkdir(parents=True)
+        self.project.write_bytes(PROJECT)
+        (self.root / "flake.lock").write_text(json.dumps({"rev": OLD_REV}))
+        (self.root / "utils").mkdir()
+        for name in ("update-nixpkgs.sh", "sync-ruff.py"):
+            (self.root / "utils" / name).write_bytes((UTILS / name).read_bytes())
+        (self.root / "utils/update-nixpkgs.sh").chmod(0o755)
+        (self.root / "bin").mkdir()
+        nix = self.root / "bin/nix"
+        nix.write_text(NIX)
+        nix.chmod(0o755)
+        uv = self.root / "bin/uv"
+        uv.write_text(UV)
+        uv.chmod(0o755)
+        self.env = dict(
+            os.environ,
+            PATH=str(nix.parent) + os.pathsep + os.environ["PATH"],
+            CONFCTL_FLAKE="fixture-pinned-confctl",
+            NEW_REV=NEW_REV,
+        )
+        self.git("init", "--initial-branch=fixture")
+        self.git("config", "user.name", "Updater Fixture")
+        self.git("config", "user.email", "fixture@example.invalid")
+        self.git("add", "flake.lock", "clients", "utils")
+        message = self.root / "message"
+        message.write_text("Initialize updater fixture\n")
+        self.git("commit", "-F", str(message))
+        self.head = self.git("rev-parse", "HEAD").stdout
+
+    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
+        return subprocess.run(
+            ["git", *args],
+            cwd=self.root,
+            env=self.env,
+            check=True,
+            capture_output=True,
+            text=True,
+        )
+
+    def update(self, **env: str) -> subprocess.CompletedProcess[str]:
+        return subprocess.run(
+            ["./utils/update-nixpkgs.sh"],
+            cwd=self.root,
+            env=dict(self.env, **env),
+            capture_output=True,
+            text=True,
+        )
+
+    def sync(self, version: str) -> subprocess.CompletedProcess[str]:
+        return subprocess.run(
+            [sys.executable, "utils/sync-ruff.py", version],
+            cwd=self.root,
+            capture_output=True,
+            text=True,
+        )
+
+    def assert_no_commit(self) -> None:
+        self.assertEqual(self.git("rev-parse", "HEAD").stdout, self.head)
+
+    def test_replacement_preserves_unrelated_toml_bytes(self) -> None:
+        source = (
+            b"# ruff==1.2.3\r\n[dependency-groups]\r\n"
+            b"dev = [\"pytest>=9\", 'RuFf == 1.2.3'] # comment\r\n"
+            b'other = ["RuFf == 1.2.3"]\r\n'
+        )
+        self.project.write_bytes(source)
+        result = self.sync("1.2.4")
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertEqual(
+            self.project.read_bytes(), source.replace(b"1.2.3'", b"1.2.4'", 1)
+        )
+
+    def test_same_pin_does_not_write(self) -> None:
+        before = self.project.stat().st_mtime_ns
+        self.assertEqual(self.sync("1.2.3").returncode, 0)
+        self.assertEqual(self.project.read_bytes(), PROJECT)
+        self.assertEqual(self.project.stat().st_mtime_ns, before)
+
+    def test_invalid_requirements_fail_without_writing(self) -> None:
+        for requirements in (
+            "[]",
+            '["pytest>=9"]',
+            '["ruff==1.2.3", "Ruff==1.2.3"]',
+            '["ruff>=1.2.3"]',
+            '["ruff[extra]==1.2.3"]',
+            '["ruff==1.2"]',
+        ):
+            with self.subTest(requirements=requirements):
+                source = f"[dependency-groups]\ndev = {requirements}\n".encode()
+                self.project.write_bytes(source)
+                self.assertNotEqual(self.sync("1.2.4").returncode, 0)
+                self.assertEqual(self.project.read_bytes(), source)
+
+    def test_invalid_versions_fail_without_writing(self) -> None:
+        for version in ("", "1.2", "1.2.4rc1", "1.2.4\n", "unexpected"):
+            with self.subTest(version=version):
+                self.assertNotEqual(self.sync(version).returncode, 0)
+                self.assertEqual(self.project.read_bytes(), PROJECT)
+
+    def test_update_commits_only_checked_lock_and_pin(self) -> None:
+        (self.root / "unrelated").write_text("untracked local content")
+        result = self.update()
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertEqual(
+            self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout,
+            "clients/python/pyproject.toml\nflake.lock\n",
+        )
+        self.assertEqual(
+            self.git("log", "-1", "--format=%s").stdout.strip(),
+            f"flake: nixpkgs {OLD_REV[:11]} -> {NEW_REV[:11]}",
+        )
+        self.assertEqual(self.project.read_bytes(), PROJECT.replace(b"1.2.3", b"1.2.4"))
+        self.assertEqual(
+            (self.root / "uv-calls").read_text().splitlines(),
+            [
+                "sync",
+                "run --locked python utils/run_ruff.py format --check .",
+                "run --locked python utils/run_ruff.py check .",
+            ],
+        )
+
+    def test_unchanged_ruff_commits_only_lock(self) -> None:
+        result = self.update(RUFF_VERSION="1.2.3")
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertEqual(self.project.read_bytes(), PROJECT)
+        self.assertEqual(
+            self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout,
+            "flake.lock\n",
+        )
+
+    def test_no_input_update_skips_version_and_checks(self) -> None:
+        result = self.update(NEW_REV=OLD_REV)
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assert_no_commit()
+        self.assertNotIn("eval", (self.root / "nix-calls").read_text())
+        self.assertNotIn("flake check", (self.root / "nix-calls").read_text())
+        self.assertEqual(self.project.read_bytes(), PROJECT)
+        self.assertFalse((self.root / "uv-calls").exists())
+
+    def test_dirty_inputs_and_unrelated_index_reject_before_nix(self) -> None:
+        for name in ("flake.lock", "clients/python/pyproject.toml", "unrelated"):
+            path = self.root / name
+            original = path.read_bytes() if path.exists() else None
+            path.write_text("pre-existing content")
+            if name != "unrelated":
+                self.assertNotEqual(self.update().returncode, 0)
+            self.git("add", name)
+            self.assertNotEqual(self.update().returncode, 0)
+            self.assert_no_commit()
+            self.assertFalse((self.root / "nix-calls").exists())
+            self.git("restore", "--staged", name)
+            if original is None:
+                path.unlink()
+            else:
+                path.write_bytes(original)
+
+    def test_failed_check_leaves_no_commit_or_staging(self) -> None:
+        result = self.update(CHECK_EXIT="1")
+        self.assertNotEqual(result.returncode, 0)
+        self.assert_no_commit()
+        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout, "")
+        self.assertEqual(self.project.read_bytes(), PROJECT.replace(b"1.2.3", b"1.2.4"))
+
+    def test_failed_guard_does_not_reach_sync_or_check(self) -> None:
+        self.assertNotEqual(self.update(UPDATE_EXIT="1").returncode, 0)
+        self.assert_no_commit()
+        self.assertEqual(self.project.read_bytes(), PROJECT)
+        self.assertNotIn("eval", (self.root / "nix-calls").read_text())
+        self.assertNotIn("flake check", (self.root / "nix-calls").read_text())
+
+    def assert_python_failure(self, calls: int, **env: str) -> None:
+        self.assertNotEqual(self.update(**env).returncode, 0)
+        self.assert_no_commit()
+        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout, "")
+        self.assertEqual(len((self.root / "uv-calls").read_text().splitlines()), calls)
+
+    def test_failed_uv_sync_leaves_no_commit_or_staging(self) -> None:
+        self.assert_python_failure(1, UV_SYNC_EXIT="1")
+
+    def test_failed_format_leaves_no_commit_or_staging(self) -> None:
+        self.assert_python_failure(2, RUFF_FORMAT_EXIT="1")
+
+    def test_failed_lint_leaves_no_commit_or_staging(self) -> None:
+        self.assert_python_failure(3, RUFF_CHECK_EXIT="1")
+
+
+if __name__ == "__main__":
+    unittest.main()
diff --git a/utils/update-nixpkgs.sh b/utils/update-nixpkgs.sh
index 2526e528..80591524 100755
--- a/utils/update-nixpkgs.sh
+++ b/utils/update-nixpkgs.sh
@@ -17,12 +17,25 @@ short_rev() {
 need_cmd git
 need_cmd jq
 need_cmd nix
+need_cmd python3
+
+if ! python3 -c 'import tomllib' 2>/dev/null; then
+  echo "error: Python 3.11 or newer with tomllib is required" >&2
+  exit 1
+fi
 
 repo_root=$(git rev-parse --show-toplevel)
 cd "$repo_root"
 
-if ! git diff --quiet -- flake.lock || ! git diff --cached --quiet -- flake.lock; then
-  echo "error: flake.lock has uncommitted changes" >&2
+ruff_project=clients/python/pyproject.toml
+if ! git diff --quiet -- flake.lock "$ruff_project" ||
+   ! git diff --cached --quiet -- flake.lock "$ruff_project"; then
+  echo "error: flake.lock or $ruff_project has uncommitted changes" >&2
+  exit 1
+fi
+
+if ! git diff --cached --quiet; then
+  echo "error: staging area must be empty before updating nixpkgs" >&2
   exit 1
 fi
 
@@ -39,9 +52,21 @@ if [ "$old_rev" = "$new_rev" ]; then
   exit 0
 fi
 
+ruff_version=$(nix eval --impure --raw --expr \
+  '(builtins.getFlake (toString ./.)).inputs.nixpkgs.legacyPackages.${builtins.currentSystem}.ruff.version')
+python3 utils/sync-ruff.py "$ruff_version"
+
 nix flake check
 
-git add flake.lock
+nix develop .#client-python -c bash <<'EOF'
+set -euo pipefail
+cd clients/python
+uv sync
+uv run --locked python utils/run_ruff.py format --check .
+uv run --locked python utils/run_ruff.py check .
+EOF
+
+git add flake.lock "$ruff_project"
 
 if git diff --cached --quiet -- flake.lock; then
   echo "flake.lock did not change"
~~~~

## vpsfree-kb-contracts

~~~~diff
diff --git a/tests/suite/kb/firewall.nix b/tests/suite/kb/firewall.nix
index 28ab29d..5162d0f 100644
--- a/tests/suite/kb/firewall.nix
+++ b/tests/suite/kb/firewall.nix
@@ -188,6 +188,38 @@ import ../../make-test.nix (
         end
       end
 
+      def wait_for_listeners(ct)
+        command = <<~SH
+          set -eu
+          listeners=$(ss -H -lnt)
+          for port in 22 80 81 443; do
+            printf '%s\\n' "$listeners" | grep -Eq ":$port[[:space:]]" || exit 1
+          done
+          printf '%s\\n' "$listeners"
+        SH
+        machine.wait_until_succeeds(
+          "osctl ct exec #{Shellwords.escape(ct)} " \
+          "bash -lc #{Shellwords.escape(command)}",
+          timeout: 120
+        )
+      rescue StandardError
+        diagnostics = <<~SH
+          ss -lntp
+          systemctl --no-pager --full --lines=10 status 'ssh*' 'kb-firewall-listener*' || true
+          journalctl --no-pager --lines=80 --unit='ssh*' --unit='kb-firewall-listener*'
+        SH
+        begin
+          machine.execute(
+            "osctl ct exec #{Shellwords.escape(ct)} " \
+            "bash -lc #{Shellwords.escape(diagnostics)}",
+            timeout: 30
+          )
+        rescue StandardError => e
+          warn "Unable to collect listener diagnostics for #{ct}: #{e.message}"
+        end
+        raise
+      end
+
       def prepare_systemd_listeners(ct, ssh_service:)
         write_container_file(
           ct,
@@ -196,11 +228,11 @@ import ../../make-test.nix (
         )
         in_container(
           ct,
-          "systemctl daemon-reload; systemctl enable --now #{ssh_service}; " \
+          "set -eu; systemctl daemon-reload; systemctl enable --now #{ssh_service}; " \
           'systemctl enable --now kb-firewall-listener@80.service ' \
-          'kb-firewall-listener@81.service kb-firewall-listener@443.service; ' \
-          "ss -lnt | grep -E ':(22|80|81|443)[[:space:]]'"
+          'kb-firewall-listener@81.service kb-firewall-listener@443.service'
         )
+        wait_for_listeners(ct)
       end
 
       def begin_established_connection(address, family)
@@ -298,11 +330,7 @@ import ../../make-test.nix (
           timeout: 300
         )
         machine.wait_until_container_online(ct, timeout: 300)
-        in_container(
-          ct,
-          "until ss -lnt | grep -Eq ':(22|80|443)[[:space:]]'; do sleep 1; done",
-          timeout: 120
-        )
+        wait_for_listeners(ct)
       end
 
       def cleanup_container(ct)
~~~~
