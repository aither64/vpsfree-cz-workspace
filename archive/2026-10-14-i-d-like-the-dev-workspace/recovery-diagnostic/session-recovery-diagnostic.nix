{
  pkgs,
  self,
  devWorkspace,
  probe,
  collector,
}:
pkgs.testers.runNixOSTest {
  name = "dev-workspace-session-recovery-diagnostic";
  nodes.machine = {
    imports = [ self.nixosModules.host ];
    users.users.developer = {
      isNormalUser = true;
      uid = 1000;
      linger = true;
    };
    services.dev-workspaces = {
      enable = true;
      owner = "developer";
      hostName = "workspace.example.test";
      wildcardHost = "*.workspace.example.test";
      codexProviders = [
        {
          id = "pool";
          label = "Disposable provider";
          baseURL = "http://127.0.0.1:2455/v1";
          tokenFile = "/home/developer/provider.token";
        }
        {
          id = "pooltwo";
          label = "Second disposable provider";
          baseURL = "http://127.0.0.1:2455/v1";
          tokenFile = "/home/developer/provider.token";
        }
      ];
    };
    systemd.services.provider-fixture = {
      wantedBy = [ "multi-user.target" ];
      serviceConfig.ExecStart = "${pkgs.python3}/bin/python3 ${pkgs.writeText "provider-fixture.py" ''
        import http.server
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                payload = {
                    "/v1/models": b'{"data":[{"id":"gpt-6.1-sol"}]}',
                    "/v1/usage": b'{"limits":[],"upstream_limits":[]}',
                }.get(self.path)
                if payload is None or self.headers.get("Authorization") != "Bearer synthetic-only":
                    self.send_error(403)
                    return
                self.send_response(200)
                self.end_headers()
                self.wfile.write(payload)
        http.server.HTTPServer(("127.0.0.1", 2455), Handler).serve_forever()
      ''}";
    };
    environment.systemPackages = [ pkgs.git ];
    # Register the user-profile closure in the VM's own Nix database.
    virtualisation.additionalPaths = [ devWorkspace probe collector ];
    system.stateVersion = "26.05";
  };
  testScript = ''
    import json
    import re
    import shlex

    machine.start(allow_reboot=True)
    machine.wait_for_unit("user@1000.service")
    package = "${devWorkspace}"
    user_prefix = "runuser -u developer -- env XDG_RUNTIME_DIR=/run/user/1000 "

    def user(command):
        return machine.succeed(user_prefix + "sh -c " + shlex.quote(command))

    def assert_services():
        machine.wait_for_unit("user@1000.service")
        for unit in ["workspace-tmux@fixture", "workspace-codex@fixture",
                     "workspace-portal@fixture", "workspace-router"]:
            machine.wait_until_succeeds(user_prefix + "systemctl --user is-active " + unit)
            assert user("systemctl --user is-enabled " + unit).strip() == "enabled"
        after = user("systemctl --user show workspace-portal@fixture -p After --value")
        assert "workspace-tmux@fixture.service" in after
        assert "workspace-codex@fixture.service" in after
        for socket in ["app-server.sock", "tmux.sock"]:
            machine.wait_until_succeeds(user_prefix + "test -S "
                                       "/run/user/1000/dev-workspaces/fixture/" + socket)

    with subtest("install private user profile and enable real application units"):
        user("mkdir -p ~/.local/state/dev-workspaces ~/workspace/repos "
             "~/workspace/work ~/workspace/worktrees")
        user("umask 077; printf synthetic-only > ~/provider.token")
        user("nix-env --profile ~/.local/state/dev-workspaces/profile --set " + package)
        user("git -C ~/workspace init --initial-branch=master")
        user(package + "/bin/workspace-host register fixture /home/developer/workspace "
             "--hostname fixture.workspace.example.test")
        assert_services()

    state_path = "/home/developer/.local/state/dev-workspaces/providers/fixture/state.json"
    host = package + "/bin/workspace-host"
    worker = "workspace-codex-provider@fixture.service"
    codex_unit = "workspace-codex@fixture.service"

    # Confined to this worker instance; the original service policy is retained.
    dropin = "/home/developer/.config/systemd/user/" + worker + ".d/diagnostic.conf"
    user("mkdir -p " + shlex.quote(dropin.rsplit("/", 1)[0]))
    user("printf '%s\\n' '[Service]' 'Environment=RUBYOPT=-r${probe}' > " + shlex.quote(dropin))
    user("systemctl --user daemon-reload")
    diagnostic_start = machine.succeed("date +%s").strip()
    assert diagnostic_start.isdigit()

    def print_observer_outcome(trace):
        active = set(re.findall(r"DW_PROVIDER_RAISE active pid=([0-9]+)(?=\s|$)", trace))
        raises = re.findall(r"DW_PROVIDER_RAISE pid=([0-9]+) seq=[0-9]+", trace)
        disabled = len(re.findall(r"DW_PROVIDER_RAISE disabled pid=[0-9]+", trace))
        truncated = len(re.findall(r"DW_PROVIDER_RAISE truncated pid=[0-9]+", trace))
        if not active or any(pid not in active for pid in raises):
            coverage = "missing-active-inconclusive"
        elif disabled or truncated:
            coverage = "observed-partial-inconclusive"
        else:
            coverage = "observed-with-raises" if raises else "observed-no-raises"
        print("DIAGNOSTIC_OBSERVER_RESULT=" + json.dumps({
            "coverage": coverage, "activePids": sorted(int(pid) for pid in active),
            "raiseCount": len(raises), "disabledCount": disabled, "truncationCount": truncated,
        }, sort_keys=True))

    def collect_diagnostics():
        # Separate from the observer: only these two fixture units, <=64 KiB total.
        commands = [
            "journalctl --user --no-pager --output=short-monotonic --since=@" + diagnostic_start
            + " --unit=" + worker + " --unit=" + codex_unit + " | tail -c 65536",
            "systemctl --user show " + worker + " " + codex_unit
            + " --property=ActiveState,SubState,MainPID,Result,ExecMainStatus,NRestarts",
            "${pkgs.python3}/bin/python3 ${collector}",
        ]
        for index, command in enumerate(commands):
            # A collection failure must not replace the original assertion failure.
            try:
                status, output = machine.execute(user_prefix + "sh -c " + shlex.quote(command))
                print(output)
                print("DIAGNOSTIC_COLLECTION_STATUS=" + str(status))
                if index == 0:
                    print_observer_outcome(output)
            except Exception:
                print("DIAGNOSTIC_COLLECTION_UNAVAILABLE")
                if index == 0:
                    print_observer_outcome("")

    def wait_phase(phase):
        command = "${pkgs.python3}/bin/python3 -c " + shlex.quote(
            "import json; d=json.load(open(" + repr(state_path) + ")); o=d['operation']; "
            "terminal=o['phase'] in ['failed','canceled']; "
            "assert o['phase'] == " + repr(phase) + " or terminal; "
            "print('DIAGNOSTIC_UNEXPECTED_TERMINAL' if terminal else 'DIAGNOSTIC_EXPECTED_PHASE')")
        output = machine.wait_until_succeeds(user_prefix + "sh -c " + shlex.quote(command))
        # Return terminal failure to Python rather than retrying a nonzero shell exit.
        assert "DIAGNOSTIC_UNEXPECTED_TERMINAL" not in output, "provider reached an unexpected terminal phase"
        return json.loads(user(host + " provider status fixture"))

    try:
        with subtest("foreign cgroup processes block the real worker until removed"):
            foreign_pid = machine.succeed("${pkgs.python3}/bin/python3 -c " + shlex.quote(
                "import subprocess; p=subprocess.Popen(['sleep','300'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=True); print(p.pid)")).strip()
            group = user("systemctl --user show " + codex_unit + " -p ControlGroup --value").strip()
            machine.succeed("echo " + foreign_pid + " > " + shlex.quote("/sys/fs/cgroup" + group + "/cgroup.procs"))
            user(host + " provider request fixture pool aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa")
            blocked = "${pkgs.python3}/bin/python3 -c " + shlex.quote(
                "import json; d=json.load(open(" + repr(state_path) + ")); o=d['operation']; "
                "terminal=o['phase'] in ['failed','canceled']; "
                "assert terminal or (d['operation']['phase']=='waiting' and d['operation']['blockers']); "
                "print('DIAGNOSTIC_UNEXPECTED_TERMINAL' if terminal else 'DIAGNOSTIC_EXPECTED_BLOCKERS')")
            output = machine.wait_until_succeeds(user_prefix + "sh -c " + shlex.quote(blocked))
            assert "DIAGNOSTIC_UNEXPECTED_TERMINAL" not in output, "provider reached an unexpected terminal phase"
            machine.succeed("kill " + foreign_pid)
            assert wait_phase("applied")["active"] == "pool"
            assert_services()

    except Exception:
        collect_diagnostics()
        raise

    # Coverage only after original assertions; no readiness/timing fence added.
    # Diagnostic collection cannot change the already-passed product assertion.
    try:
        command = ("journalctl --user --no-pager --output=cat --since=@" + diagnostic_start
                   + " --unit=" + worker + " --grep='^DW_PROVIDER_RAISE ' | tail -c 65536")
        status, output = machine.execute(user_prefix + "sh -c " + shlex.quote(command))
        print(output)
        print_observer_outcome(output if status == 0 else "")
    except Exception:
        print_observer_outcome("")
  '';
}
