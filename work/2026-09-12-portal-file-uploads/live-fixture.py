"""Owned fixture helpers adapted from the existing packaged creation acceptance.
No actions on import; all runtime paths belong to one fresh private fixture.
"""
import argparse


import datetime as dt


import hashlib


import http.client


import http.server


import json


import os


from pathlib import Path


import re


import select


import shlex


import shutil


import signal


import socket


import socketserver


import ssl


import subprocess


import tempfile


import threading


import time


import urllib.parse


import uuid


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def until(test, seconds=120, interval=1, label='condition'):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        value = test()
        if value:
            return value
        time.sleep(interval)
    raise TimeoutError(f'{label} did not finish within {seconds}s')


class UnixHTTP(http.client.HTTPConnection):
    def __init__(self, path, timeout=20):
        super().__init__('localhost', timeout=timeout)
        self.socket_path = str(path)

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect(self.socket_path)


class Fixture:
    def __init__(self, resume_root=None, allow_package_change=False):
        self.package = Path(os.environ['ACCEPT_PACKAGE']).resolve(strict=True)
        self.previous = Path(os.environ.get('ACCEPT_PREVIOUS', '/nix/store/aamx7bqmg406w3zrfnvpd60knhrgps4s-dev-workspace-0.2.0')).resolve(strict=True)
        self.codex = Path(os.environ.get('ACCEPT_CODEX', str(self.package / 'libexec/codex/bin/codex'))).resolve(strict=True)
        self.authenticated_socket = Path(os.environ['ACCEPT_CODEX_SOCKET'])
        require(self.authenticated_socket.is_socket(), 'ACCEPT_CODEX_SOCKET must be the selected authenticated Unix socket')
        for package in (self.package, self.previous):
            require(str(package).startswith('/nix/store/'), 'acceptance requires immutable packaged outputs')
            require((package / 'bin/workspace-portal').is_file(), 'workspace-portal is missing from a package')
        self.tmux = self.executable('ACCEPT_TMUX', 'tmux')
        self.ruby = self.executable('ACCEPT_RUBY', 'ruby')
        self.openssl = self.executable('ACCEPT_OPENSSL', 'openssl')
        self.root = Path(resume_root).resolve(strict=True) if resume_root else Path(tempfile.mkdtemp(prefix='upload-live.'))
        self.workspace = self.root / 'workspace'
        self.codex_socket = self.root / 'codex.sock'
        self.portal = None
        self.browser = None
        self.proxy = None
        self.codex_relay = None
        self.upstreams = set()
        self.upstream_lock = threading.Lock()
        self.events = []
        self.results = {'fixture': str(self.root), 'package': str(self.package), 'previous': str(self.previous), 'codex': str(self.codex), 'checks': [], 'threads': {}}
        if resume_root:
            require((self.root / 'upload-acceptance-fixture').is_file(), 'resume path is not an acceptance fixture')
            recorded = json.loads((self.root / 'results.json').read_text())
            identity_keys = ('fixture', 'previous', 'codex') if allow_package_change else ('fixture', 'package', 'previous', 'codex')
            require(all(recorded[key] == self.results[key] for key in identity_keys), 'resume would change the accepted package or fixture')
            require(len(set(recorded['threads'].values())) <= 4, 'resume exceeds the fixture thread budget')
            self.results = recorded
            if allow_package_change:
                self.results['reconciliationPackage'] = str(self.package)
        self.environment = {k: v for k, v in os.environ.items() if not k.startswith(('DEV_SESSION_', 'DEV_WORKSPACE_')) and k not in ('TMUX', 'TMUX_PANE', 'CODEX_THREAD_ID')}
        self.environment['CREATION_ACCEPT_CONFIG'] = str(self.root / 'gate.json')
        self.environment['DEV_WORKSPACES_STATE'] = str(self.root / 'state')
        if (self.root / 'codex-metadata').is_dir():
            self.environment['CODEX_HOME'] = str(self.root / 'codex-metadata')
        self.date = dt.date.today().isoformat()
        self.names = ['upload-source', 'upload-fork']
        self.slugs = [f'{self.date}-{name}' for name in self.names]
        if resume_root:
            require(json.loads((self.root / 'gate.json').read_text())['slugs'] == self.slugs, 'resume would change fixture slugs')
        self.version = ''
    @staticmethod
    def executable(variable, fallback):
        result = os.environ.get(variable) or shutil.which(fallback)
        require(result and Path(result).is_file(), f'{fallback} must be supplied by the Nix environment')
        return str(Path(result).resolve())
    def command(self, arguments, label, timeout=120):
        result = subprocess.run([str(x) for x in arguments], cwd=self.workspace, env=self.environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        (self.root / f'{label}.stderr').write_bytes(result.stderr)
        require(result.returncode == 0, f'{label} failed; see its private stderr log')
        return result.stdout
    def record(self, name, **values):
        self.results['checks'].append({'check': name, **values})
        (self.root / 'results.json').write_text(json.dumps(self.results, indent=2) + '\n')
        print(name, flush=True)
    def prepare(self):
        for directory in ('workspace', 'workspace/work', 'workspace/worktrees', 'workspace/repos', 'authority', 'state', 'gates', 'screenshots'):
            (self.root / directory).mkdir(mode=0o700, parents=True, exist_ok=True)
        (self.root / 'upload-acceptance-fixture').touch(mode=0o600)
        (self.root / 'transition.lock').touch(mode=0o600)
        (self.workspace / 'AGENTS.md').write_text('This is a disposable acceptance fixture. Use request_user_input only when explicitly requested. Do not use other tools, edit files, create repositories, or run lifecycle commands. Respond only to the fixed test requests. Keep all conversations open.\n')
        for args in (['git', 'init', '-b', 'master'], ['git', 'config', 'user.name', 'Creation acceptance'], ['git', 'config', 'user.email', 'creation-acceptance@invalid'], ['git', 'add', 'AGENTS.md'], ['git', 'commit', '-m', 'Initialize isolated acceptance fixture']):
            self.command(args, 'git-' + args[1])
        gate = Path(__file__).with_name('upload-session-gate.rb').read_text()
        (self.root / 'session-gate').write_text('#!' + self.ruby + '\n' + gate.split('\n', 1)[1])
        (self.root / 'session-gate').chmod(0o700)
        raw_version = self.command([self.codex, '--version'], 'codex-version').decode().strip()
        self.version = raw_version.split()[-1]
        require(re.fullmatch(r'\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.]+)?', self.version), 'unexpected Codex version output')
        expected_version = os.environ.get('ACCEPT_CODEX_VERSION')
        require(not expected_version or expected_version == self.version, 'selected Codex version differs from the authenticated socket contract')
        self.results['codexVersion'] = self.version
        self.defaults = json.loads(self.command([self.package / 'bin/workspace-portal', 'thread', 'defaults'], 'defaults'))
        self.command([self.openssl, 'req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-keyout', self.root / 'tls.key', '-out', self.root / 'tls.crt', '-days', '1', '-subj', '/CN=127.0.0.1', '-addext', 'subjectAltName=IP:127.0.0.1'], 'certificate', timeout=30)
        self.start_codex_relay()
        self.start_proxy()
        self.start(self.package)
        self.record('fixture prepared', codexVersion=self.version, base=self.base)
    def start_codex_relay(self):
        fixture = self

        class Relay(socketserver.BaseRequestHandler):
            def handle(self):
                upstream = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                try:
                    upstream.connect(str(fixture.authenticated_socket))
                    peers = {self.request: upstream, upstream: self.request}
                    while True:
                        readable, _, _ = select.select(list(peers), [], [], 1)
                        for source in readable:
                            data = source.recv(65536)
                            if not data:
                                return
                            peers[source].sendall(data)
                except (OSError, ValueError):
                    pass
                finally:
                    upstream.close()

        self.codex_relay = socketserver.ThreadingUnixStreamServer(str(self.codex_socket), Relay)
        self.codex_relay.daemon_threads = True
        self.codex_socket.chmod(0o600)
        threading.Thread(target=self.codex_relay.serve_forever, daemon=True).start()
    def start_proxy(self):
        fixture = self

        class Proxy(http.server.BaseHTTPRequestHandler):
            protocol_version = 'HTTP/1.0'

            def log_message(self, *_):
                pass

            def do_GET(self):
                self.forward()

            def do_POST(self):
                self.forward()

            def forward(self):
                started = time.monotonic()
                connection = UnixHTTP(fixture.root / 'portal.sock', timeout=150)
                try:
                    length = int(self.headers.get('Content-Length', '0'))
                    require(0 <= length <= 2 * 1024 * 1024, 'proxy request exceeds fixture bound')
                    body = self.rfile.read(length) if length else None
                    headers = {k: v for k, v in self.headers.items() if k.lower() not in ('connection', 'transfer-encoding')}
                    connection.request(self.command, self.path, body=body, headers=headers)
                    with fixture.upstream_lock:
                        fixture.upstreams.add(connection)
                    response = connection.getresponse()
                    fixture.events.append({'method': self.command, 'path': self.path, 'status': response.status, 'started': started, 'headersSeconds': time.monotonic() - started})
                    self.send_response(response.status)
                    for key, value in response.getheaders():
                        if key.lower() not in ('connection', 'transfer-encoding'):
                            self.send_header(key, value)
                    self.end_headers()
                    self.wfile.flush()
                    while chunk := response.read1(65536):
                        self.wfile.write(chunk)
                        self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, socket.timeout):
                    pass
                except (OSError, http.client.HTTPException):
                    if not self.wfile.closed:
                        try:
                            self.send_error(502)
                        except OSError:
                            pass
                finally:
                    with fixture.upstream_lock:
                        fixture.upstreams.discard(connection)
                    connection.close()

        self.proxy = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Proxy)
        self.proxy.daemon_threads = True
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(self.root / 'tls.crt', self.root / 'tls.key')
        self.proxy.socket = context.wrap_socket(self.proxy.socket, server_side=True)
        self.base = f'https://127.0.0.1:{self.proxy.server_port}'
        threading.Thread(target=self.proxy.serve_forever, daemon=True).start()
    def cli(self, package):
        token = self.command([self.ruby, '-r', package / 'libexec/workspace-profile-identity.rb', '-e', 'print DevWorkspaceProfileIdentity.token(ARGV.fetch(0))', self.root / 'profile'], 'profile-token').decode()
        require(re.fullmatch('[0-9a-f]{64}', token), 'fixture profile token is missing')
        options = {'workspace': self.workspace, 'tmux-socket': self.root / 'tmux.sock', 'authority-dir': self.root / 'authority', 'codex-socket': self.codex_socket, 'codex-version': self.version, 'codex-command': self.codex, 'portal-command': package / 'bin/workspace-portal', 'portal-base-url': self.base, 'transition-lock': self.root / 'transition.lock', 'host-profile': self.root / 'profile', 'expected-host-generation': package, 'expected-host-profile-token': token}
        return [str(package / 'libexec/workspace-portal/dev-session')] + [str(part) for key, value in options.items() for part in ('--' + key, value)] + ['--require-runtime']
    def start(self, package):
        require(self.portal is None, 'fixture portal must stop before changing its profile')
        profile = self.root / 'profile'
        profile.unlink(missing_ok=True)
        profile.symlink_to(package)
        configuration = {'root': str(self.root), 'slugs': self.slugs, 'gate_seconds': 240, 'cli': self.cli(package)}
        (self.root / 'gate.json').write_text(json.dumps(configuration))
        options = {'workspace': self.workspace, 'base-url': self.base, 'unix-socket': self.root / 'portal.sock', 'dev-session': self.root / 'session-gate', 'authority-dir': self.root / 'authority', 'user-state-root': self.root / 'state', 'host-profile': profile, 'transition-lock': self.root / 'transition.lock', 'codex-socket': self.codex_socket, 'codex-version': self.version, 'tmux': self.tmux}
        args = [str(package / 'bin/workspace-portal'), 'serve'] + [str(part) for key, value in options.items() for part in ('--' + key, value)]
        log = open(self.root / f'portal-{len(self.results["checks"])}.log', 'ab')
        self.portal = subprocess.Popen(args, cwd=self.workspace, env=self.environment, stdout=log, stderr=log, start_new_session=True)
        log.close()

        def alive():
            require(self.portal.poll() is None, 'packaged portal stopped during startup; see private log')
            try:
                return self.http('/')[0] == 200
            except (OSError, http.client.HTTPException):
                return False
        until(alive, seconds=30, interval=.1, label='portal startup')
    def stop(self):
        if self.portal:
            # Close this proxy's SSE readers so graceful HTTP shutdown need not
            # wait for an idle browser stream. No shared App Server socket is closed.
            with self.upstream_lock:
                connections = list(self.upstreams)
            for connection in connections:
                try:
                    if connection.sock:
                        connection.sock.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass
            self.portal.send_signal(signal.SIGTERM)
            try:
                self.portal.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(self.portal.pid, signal.SIGKILL)
                self.portal.wait(timeout=5)
                raise TimeoutError('fixture portal failed to stop within 15s')
            finally:
                self.portal = None
    def http(self, path, body=None, form=False, timeout=20):
        connection = UnixHTTP(self.root / 'portal.sock', timeout)
        headers = {'Origin': self.base}
        if body is not None:
            headers['Content-Type'] = 'application/x-www-form-urlencoded' if form else 'application/json'
            body = urllib.parse.urlencode(body) if form else json.dumps(body)
        started = time.monotonic()
        try:
            connection.request('GET' if body is None else 'POST', path, body, headers)
            response = connection.getresponse()
            data = response.read()
            return response.status, data, dict(response.getheaders()), time.monotonic() - started
        finally:
            connection.close()
    def get_json(self, path):
        status, body, _, _ = self.http(path)
        require(status == 200, f'GET {path} returned {status}')
        return json.loads(body)
    def status(self, slug):
        return self.get_json(f'/api/sessions/{slug}/creation')
    def receipt(self, slug):
        paths = list((self.root / 'state').rglob(f'creations/{slug}.json'))
        require(len(paths) == 1, 'expected exactly one private creation receipt')
        return json.loads(paths[0].read_bytes()), paths[0]
    def manifest(self, slug):
        return json.loads(self.command([self.ruby, '-ryaml', '-rjson', '-e', 'print JSON.generate(YAML.safe_load(File.read(ARGV.fetch(0)), permitted_classes: [], aliases: false))', self.workspace / 'work' / slug / 'portal.yml'], 'manifest-' + slug))
    def transcript(self, slug):
        return self.get_json(f'/codex/conversations/{slug}/thread')
    def idle(self, slug):
        return until(lambda: (value if (value := self.transcript(slug))['status'] != 'active' else None), seconds=180, label=f'{slug} idle')
    def ready(self, slug):
        def check():
            value = self.status(slug)
            require(value['state'] not in ('failed', 'paused', 'conflict'), 'creation stopped; inspect its private receipt')
            return value if value['state'] == 'ready' else None
        result = until(check, seconds=150, label=f'{slug} ready')
        thread = self.manifest(slug)['codex']['thread_id']
        self.results['threads'][slug] = thread
        require(len(set(self.results['threads'].values())) <= 4, 'fixture exceeded four conversation identities')
        return result
    def close(self):
        if self.browser:
            try:
                self.browser.quit()
            except Exception:
                self.results['browserCleanup'] = 'Browser close failed; inspect the private GeckoDriver log.'
        try:
            self.stop()
        finally:
            if self.proxy:
                self.proxy.shutdown()
                self.proxy.server_close()
            if self.codex_relay:
                self.codex_relay.shutdown()
                self.codex_relay.server_close()
            for slug in self.slugs:
                if (self.workspace / 'work' / slug / 'portal.yml').exists():
                    try:
                        thread = self.manifest(slug).get('codex', {}).get('thread_id')
                        if thread:
                            self.results['threads'][slug] = thread
                    except Exception:
                        self.results['cleanupInspection'] = 'Some fixture manifests need inspection before cleanup.'
            self.results['tmuxSocket'] = str(self.root / 'tmux.sock')
            self.results['cleanup'] = 'Portal, browser, HTTPS proxy and local Codex relay stopped. Fixture tmux and recorded Codex threads are retained for root-owned cleanup; no registered session was changed.'
            (self.root / 'results.json').write_text(json.dumps(self.results, indent=2) + '\n')
            (self.root / 'http-metadata.json').write_text(json.dumps(self.events, indent=2) + '\n')
            print(f'Private results: {self.root / "results.json"}', flush=True)

