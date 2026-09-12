#!/usr/bin/env python3
"""Four-thread packaged creation acceptance. Requires an explicit --run.

No live action occurs when this module is imported or compiled. Runtime outputs,
request snapshots and subprocess logs stay in a new private /tmp fixture.
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


GOAL = 'Reply exactly READY. Do not use tools or change files. Keep this session open.'
PLAN_REQUEST = (
    'Propose a two-step plan in a <proposed_plan> block for this tiny task: '
    'compose the exact response PLAN_ACCEPTED, then return it. '
    'Do not implement yet. Do not use tools, ask questions, or change files. '
    'The plan must explicitly require no tools, no file changes, and keeping this session open.'
)
QUESTION_REQUEST = (
    'For this acceptance check, call request_user_input exactly once with one blocking '
    'two-choice question. Use question id fixture_choice, header Fixture, and question '
    'Which fixture answer should be used? The two option labels must be Alpha (Recommended) '
    'and Beta, with descriptions Select the first fixture answer. and Select the second '
    'fixture answer. Do not answer the question yourself. Do not use any other tool or '
    'change files. After I submit an answer, reply exactly QUESTION_ANSWERED and finish '
    'this turn. Keep this session open.'
)


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class QuestionUnavailable(AssertionError):
    pass


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
        self.root = Path(resume_root).resolve(strict=True) if resume_root else Path(tempfile.mkdtemp(prefix='creation-accept.'))
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
            require((self.root / 'creation-acceptance-fixture').is_file(), 'resume path is not an acceptance fixture')
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
        self.names = ['Accept_New', 'accept-fork', 'accept-plan', 'accept-conflict']
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
        (self.root / 'creation-acceptance-fixture').touch(mode=0o600)
        (self.root / 'transition.lock').touch(mode=0o600)
        (self.workspace / 'AGENTS.md').write_text('This is a disposable acceptance fixture. Use request_user_input only when explicitly requested. Do not use other tools, edit files, create repositories, or run lifecycle commands. Respond only to the fixed test requests. Keep all conversations open.\n')
        for args in (['git', 'init', '-b', 'master'], ['git', 'config', 'user.name', 'Creation acceptance'], ['git', 'config', 'user.email', 'creation-acceptance@invalid'], ['git', 'add', 'AGENTS.md'], ['git', 'commit', '-m', 'Initialize isolated acceptance fixture']):
            self.command(args, 'git-' + args[1])
        gate = Path(__file__).with_name('creation-session-gate.rb').read_text()
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
        self.start_browser()
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

    def start_browser(self):
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service
        options = Options()
        options.add_argument('-headless')
        options.binary_location = self.executable('ACCEPT_FIREFOX', 'firefox')
        options.set_capability('acceptInsecureCerts', True)
        options.set_capability('webSocketUrl', True)
        options.page_load_strategy = 'eager'
        self.browser = webdriver.Firefox(options=options, service=Service(executable_path=self.executable('ACCEPT_GECKODRIVER', 'geckodriver'), log_output=str(self.root / 'geckodriver.log')))
        self.browser.set_page_load_timeout(20)

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

    def send(self, slug, message):
        status, body, _, _ = self.http(f'/codex/conversations/{slug}/message', {'message': message, 'clientUserMessageId': str(uuid.uuid4())})
        require(status == 202, 'fixture conversation rejected its bounded request')
        return json.loads(body)

    def count(self, slug):
        path = self.root / 'gates' / f'{slug}.count'
        return int(path.read_text()) if path.exists() else 0

    def hold(self, slug):
        (self.root / 'gates' / f'{slug}.hold').touch(mode=0o600)

    def release(self, slug):
        (self.root / 'gates' / f'{slug}.hold').unlink()

    def entered(self, slug):
        until(lambda: (self.root / 'gates' / f'{slug}.entered').exists(), seconds=45, interval=.1, label='real CLI delay gate')

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

    def field(self, selector, value):
        element = self.browser.find_element('css selector', selector)
        self.browser.execute_script('arguments[0].value = arguments[1]', element, value)

    def submit(self, form, slug, endpoint, expected):
        started = time.monotonic()
        self.browser.execute_script('document.querySelector(arguments[0]).requestSubmit()', form)
        until(lambda: urllib.parse.urlparse(self.browser.current_url).path == f'/{slug}/' and self.browser.execute_script('return document.body.dataset.creation') == slug, seconds=5, interval=.05, label='destination progress navigation')
        navigation = time.monotonic() - started
        matches = [event for event in self.events if event['method'] == 'POST' and event['path'] == endpoint and event['started'] >= started]
        require(len(matches) == 1 and matches[0]['status'] == expected, 'browser creation response has wrong status')
        require(matches[0]['headersSeconds'] < .75, 'creation acceptance took 750ms or more')
        require(navigation < 2, 'browser did not reach its destination within 2s')
        require((self.root / 'gates' / f'{slug}.hold').exists(), 'navigation happened after the delay gate opened')
        code, shell, _, elapsed = self.http(f'/{slug}/')
        require(code == 200 and b'data-creation=' in shell and b'id="message-form"' not in shell and elapsed < .75, 'premanifest shell was not immediate')
        self.record('immediate ' + slug, responseSeconds=matches[0]['headersSeconds'], navigationSeconds=navigation, shellSeconds=elapsed, httpStatus=expected)

    def screenshot_shell(self, slug):
        before = self.browser.find_element('id', 'creation-elapsed').text
        started = time.monotonic()
        for label, width, height in (('desktop', 1440, 1000), ('narrow', 390, 600)):
            self.browser.browsing_context.set_viewport(context=self.browser.current_window_handle, viewport={'width': width, 'height': height})
            require(self.browser.execute_script('return innerWidth') == width, 'browser viewport differs from requested width')
            require(self.browser.execute_script('return document.documentElement.scrollWidth <= innerWidth'), 'creation shell overflows horizontally')
            self.browser.save_screenshot(str(self.root / 'screenshots' / f'{slug}-{label}.png'))
        time.sleep(max(0, 5.2 - (time.monotonic() - started)))
        require(self.browser.find_element('id', 'creation-elapsed').text != before, 'elapsed heartbeat did not advance')
        polls = [event for event in self.events if event['path'] == f'/api/sessions/{slug}/creation' and event['method'] == 'GET' and event['started'] >= started]
        require(4 <= len(polls) <= 7, 'creation status is not polling roughly once per second')
        self.browser.browsing_context.set_viewport(context=self.browser.current_window_handle, viewport={'width': 1440, 'height': 1000})
        self.record('progress heartbeat', polls=len(polls))

    def duplicate(self, slug, path, payload, form=False):
        original = self.status(slug)
        response, body, headers, elapsed = self.http(path, payload, form=form)
        require(response == (303 if form else 202) and elapsed < .75, 'matching duplicate was not immediately reused')
        repeated = self.status(slug) if form else json.loads(body)
        require((original['receiptId'], original['attempt']) == (repeated['receiptId'], repeated['attempt']), 'matching duplicate changed receipt identity')
        if form:
            require(headers.get('Location') == f'/{slug}/', 'duplicate form changed destination')
        self.entered(slug)
        require(self.count(slug) == 1, 'duplicate launched another CLI worker')
        return original

    def run(self):
        self.prepare()
        source, fork, plan, conflict = self.slugs
        self.browser.get(self.base + '/')
        self.hold(source)
        form = {'creation_date': self.date, 'name': self.names[0], 'goal': GOAL}
        for name, value in form.items():
            self.field(f'#new-session-form [name="{name}"]', value)
        self.submit('#new-session-form', source, '/sessions', 303)
        request = self.receipt(source)[0]['request']
        form.update(model=request.get('model', ''), effort=request.get('effort', ''))
        self.screenshot_shell(source)
        self.duplicate(source, '/sessions', form, form=True)
        require(self.http('/sessions', {**form, 'goal': GOAL + ' Different.'}, form=True)[0] == 409, 'different request reused the reserved name')
        message_status = self.http(f'/codex/conversations/{source}/message', {'message': GOAL, 'clientUserMessageId': str(uuid.uuid4())})[0]
        # The conversation handler masks resolver refusals as unavailable.
        require(message_status == 404, f'initializing destination message returned {message_status}, expected unavailable')
        require(self.http(f'/api/sessions/{source}/fork', {'name': 'must-not-exist', 'creationDate': self.date})[0] == 409, 'initializing destination accepted a fork')
        self.record('initializing destination rejects mutations', messageStatus=message_status, forkStatus=409)
        self.release(source)
        self.finish_new_and_remaining()

    def prepare_existing(self):
        self.version = self.command([self.codex, '--version'], 'resume-codex-version').decode().strip().split()[-1]
        require(self.version == self.results['codexVersion'], 'resume changed the selected Codex version')
        self.defaults = json.loads(self.command([self.package / 'bin/workspace-portal', 'thread', 'defaults'], 'resume-defaults'))
        if self.codex_socket.exists():
            probe = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            try:
                probe.connect(str(self.codex_socket))
            except ConnectionRefusedError:
                self.codex_socket.unlink()
            else:
                raise AssertionError('the fixture Codex relay is still running')
            finally:
                probe.close()
        self.start_codex_relay()
        self.start_proxy()
        self.start(self.package)
        self.start_browser()
        self.results['priorFailure'] = self.results.pop('failure', '')
        self.results.pop('outcome', None)
        self.results['codexSocket'] = str(self.authenticated_socket)
        self.results['ownedAppServerPid'] = int((self.root / 'owned-app-server.pid').read_text())
        self.results['codexMetadataHome'] = str(self.root / 'codex-metadata')

    def resume_initial_creation(self):
        source = self.slugs[0]
        require(not self.results['threads'], 'initial resume requires no recorded fixture thread')
        require(all(not (self.workspace / 'work' / slug).exists() for slug in self.slugs[1:]), 'resume checkpoint has later fixture destinations')
        require(not (self.root / 'gates' / f'{source}.hold').exists(), 'resume checkpoint still holds its initial CLI gate')
        self.prepare_existing()
        prior = self.status(source)
        require(prior['state'] in ('paused', 'failed'), 'initial creation does not offer explicit retry')
        count = self.count(source)
        self.browser.get(self.base + f'/{source}/')
        self.browser.find_element('id', 'creation-retry').click()
        until(lambda: self.count(source) == count + 1, seconds=30, interval=.1, label='initial receipt retry worker')
        current = self.status(source)
        require(current['receiptId'] == prior['receiptId'] and current['attempt'] == prior['attempt'] + 1, 'initial retry replaced its receipt identity')
        self.record('existing initial receipt retried after filtered lookup diagnosis', receiptId=current['receiptId'], attempt=current['attempt'])
        self.finish_new_and_remaining()

    def resume_fork_creation(self):
        source, fork, _, _ = self.slugs
        require(set(self.results['threads']) == {source}, 'fork resume requires only the original fixture thread')
        self.prepare_existing()
        self.restore_source_terminal(source)
        self.complete_source_diagnostic_and_fork(source, fork)

    def restore_source_terminal(self, source):
        require(self.transcript(source)['status'] != 'active', 'source must be idle before restoring its fixture terminal')
        authority = json.loads((self.root / 'authority' / f'{source}.json').read_text())
        panes = self.command([self.tmux, '-S', self.root / 'tmux.sock', 'list-panes', '-t', authority['tmux_session_id'], '-F', '#{pane_id} #{pane_current_command}'], 'resume-panes').decode().splitlines()
        candidates = [line.split()[0] for line in panes if line.split()[1] in ('codex', '.codex-wrapped')]
        require(len(candidates) == 1, 'source has no unique fixture Codex pane')
        self.command([self.tmux, '-S', self.root / 'tmux.sock', 'set-environment', '-g', 'CODEX_HOME', self.root / 'codex-metadata'], 'resume-tmux-home')
        native = shlex.join([str(self.codex), '--remote', 'unix://' + str(self.codex_socket), 'resume', self.results['threads'][source]])
        self.command([self.tmux, '-S', self.root / 'tmux.sock', 'respawn-pane', '-k', '-t', candidates[0], '-e', 'CODEX_HOME=' + str(self.root / 'codex-metadata'), '-c', self.workspace / 'work' / source, native], 'resume-native-client')
        def native_connected():
            pane = self.command([self.tmux, '-S', self.root / 'tmux.sock', 'capture-pane', '-p', '-t', candidates[0]], 'resume-native-screen').decode()
            return 'model:' in pane and '›' in pane and 'Connection lost' not in pane and 'Reconnect failed' not in pane
        until(native_connected, seconds=30, interval=.2, label='restored fixture terminal connection')

    def complete_source_diagnostic_and_fork(self, source, fork):
        accepted, _ = self.receipt(source)
        diagnostic = 'Reply exactly DIAGNOSTIC_READY. Do not use tools or change files. Keep this session open.'
        self.send(source, diagnostic)
        transcript = self.idle(source)
        replies = [entry for entry in transcript['entries'] if entry['kind'] == 'agentMessage' and entry.get('text', '').strip() == 'DIAGNOSTIC_READY' and entry.get('turnStatus') == 'completed']
        require(len(replies) == 1, 'single diagnostic request did not complete successfully')
        require(self.http(f'/codex/conversations/{source}/settings', {'model': accepted['model'], 'reasoningEffort': accepted['effort']})[0] == 200, 'source rejected its original accepted settings after the diagnostic turn')
        transcript = self.transcript(source)
        require((transcript['model'], transcript['reasoningEffort']) == (accepted['model'], accepted['effort']), 'source did not retain its accepted settings after the diagnostic request')
        require(len([entry for entry in transcript['entries'] if entry['kind'] == 'userMessage' and entry['text'] == GOAL]) == 1, 'diagnostic repeated the original initial request')
        self.record('same source completed one diagnostic after terminal home correction', threadId=transcript['threadId'], diagnosticTurnId=replies[0]['turnId'], model=transcript['model'], reasoningEffort=transcript['reasoningEffort'])
        prior = self.status(fork)
        require(prior['state'] in ('failed', 'paused') and self.count(fork) == 0, 'fork checkpoint already invoked its CLI')
        self.browser.get(self.base + f'/{fork}/')
        self.browser.find_element('id', 'creation-retry').click()
        self.entered(fork)
        receipt, _ = self.receipt(fork)
        require(receipt['receiptId'] == prior['receiptId'] and receipt['attempt'] == prior['attempt'] + 1, 'fork retry replaced its accepted receipt')
        self.duplicate(fork, f'/api/sessions/{source}/fork', {'name': self.names[1], 'creationDate': self.date, 'model': receipt['request'].get('model', ''), 'reasoningEffort': receipt['request'].get('effort', '')})
        self.release(fork)
        self.finish_fork_and_remaining()

    def resume_completed_plan(self):
        source, fork, plan, conflict = self.slugs
        require(set(self.results['threads']) == {source, fork, plan}, 'plan checkpoint requires exactly the three recorded conversations')
        require(not (self.workspace / 'work' / conflict).exists(), 'fourth fixture destination already exists')
        original, receipt_path = self.receipt(plan)
        require(original['state'] == 'failed' and original['error'] == 'creation completion goal changed', 'plan checkpoint does not match the diagnosed deployed receipt')
        evidence = receipt_path.with_name(f'{plan}.{original["receiptId"]}.complete.json')
        binding = Path(str(evidence) + '.request')
        evidence_hashes = {path: digest(path.read_bytes()) for path in (evidence, binding)}
        invocations = self.count(plan)
        self.prepare_existing()
        completed = self.ready(plan)
        reconciled, _ = self.receipt(plan)
        require(completed['receiptId'] == original['receiptId'] and completed['attempt'] == original['attempt'] and self.count(plan) == invocations, 'completion reconciliation reran creation or changed its receipt')
        require(reconciled['request'] == original['request'] and reconciled['goal'] == original['goal'], 'reconciliation changed the frozen accepted snapshot')
        require(all(digest(path.read_bytes()) == expected for path, expected in evidence_hashes.items()), 'reconciliation rewrote CLI binding or completion evidence')
        expected_goal = ('Implement the following approved plan from session ' + source + '.\n\n' + original['request']['planText']).strip(' \t\n\v\f\r\x00')
        require(original['request']['planSha256'] == digest(original['request']['planText']), 'accepted plan text no longer matches its captured digest')
        transcript = self.idle(plan)
        require([entry['text'] for entry in transcript['entries'] if entry['kind'] == 'userMessage'] == [expected_goal], 'plan destination lost the exact canonical implementation request')
        require(any(entry['kind'] == 'agentMessage' and entry.get('turnStatus') == 'completed' for entry in transcript['entries']), 'plan destination has no completed model response')
        require((transcript['model'], transcript['reasoningEffort']) == (original['model'], original['effort']), 'plan destination changed captured settings')
        newer = [entry for entry in self.transcript(source)['entries'] if entry['kind'] == 'plan' and entry.get('turnStatus') == 'completed']
        require(newer and digest(newer[-1]['text']) != original['request']['planSha256'], 'source no longer demonstrates the newer unaccepted plan')
        self.record('exact plan survived newer source and retry; deployed receipt reconciled without replay', receiptId=completed['receiptId'], attempt=completed['attempt'], planTurnId=original['request']['planTurnId'], planSha256=original['request']['planSha256'], goalSha256=digest(expected_goal), invocations=invocations, threadId=transcript['threadId'])
        self.passive_question(source, plan)
        self.rollback_conflict(source, conflict)

    def resume_remaining_checks(self):
        source, fork, plan, conflict = self.slugs
        require(set(self.results['threads']) == {source, fork, plan}, 'remaining checkpoint requires the same three conversations')
        require(not (self.workspace / 'work' / conflict).exists(), 'fourth fixture destination already exists')
        require(self.receipt(plan)[0]['state'] == 'ready', 'plan reconciliation has not completed')
        self.prepare_existing()
        self.restore_source_terminal(source)
        for mode in ('default', 'plan'):
            status, body, _, _ = self.http(f'/codex/conversations/{source}/settings', {'collaborationMode': mode})
            require(status == 200 and json.loads(body)['collaborationMode'] == mode, 'source did not accept the explicit live mode transition')
        self.record('live Plan mode established after stale rollout-mode refusal', threadId=self.results['threads'][source], transitions=['default', 'plan'], retryBudget=1)
        try:
            self.passive_question(source, plan)
        except QuestionUnavailable as error:
            self.record('real question unavailable after one mode-corrected retry', reason=str(error))
        self.rollback_conflict(source, conflict)

    def resume_pending_question(self, turn_id):
        source, fork, plan, conflict = self.slugs
        require(set(self.results['threads']) == {source, fork, plan}, 'question checkpoint requires the same three conversations')
        require(not (self.workspace / 'work' / conflict).exists(), 'fourth fixture destination already exists')
        self.prepare_existing()
        # This checkpoint must never send another model request or replace its
        # active native client. Only the previously observed turn can be answered.
        self.passive_question(source, plan, existing_turn=turn_id)
        self.rollback_conflict(source, conflict)

    def resume_rollback_after_question(self, turn_id):
        source, fork, plan, conflict = self.slugs
        require(set(self.results['threads']) == {source, fork, plan}, 'rollback checkpoint requires the same three conversations')
        require(not (self.workspace / 'work' / conflict).exists(), 'fourth fixture destination already exists')
        self.prepare_existing()
        transcript = self.transcript(source)
        activity = self.get_json(f'/codex/conversations/{source}/activity')
        require(transcript['threadId'] == self.results['threads'][source] and transcript['status'] == 'active', 'cleanup question is no longer active on the exact source')
        require(activity['currentTurnId'] == turn_id and activity['currentState'] == 'waiting', 'cleanup would interrupt a different fixture turn')
        require(not self.get_json(f'/codex/conversations/{source}/pending'), 'restarted portal unexpectedly recovered interactive request authority')
        self.record('real question passive observation passed; answer subcheck unverified after fixture client loss', threadId=transcript['threadId'], turnId=turn_id, observedMsMinimum=2500, waitingGrowthMsMinimum=2500, absoluteWorkingGrowthMsMaximum=1000, originalSnapshotValuesRetained=False, answerVerified=False, closedWaitVerified=False)
        require(self.http(f'/codex/conversations/{source}/interrupt', {})[0] == 202, 'ordinary fixture question interrupt failed')
        ended = self.idle(source)
        require(any(entry.get('turnId') == turn_id and entry.get('turnStatus') == 'interrupted' for entry in ended['entries']), 'fixture cleanup did not interrupt the exact question turn')
        self.record('exact stranded fixture question interrupted before rollback', threadId=transcript['threadId'], turnId=turn_id)
        self.rollback_conflict(source, conflict)

    def finish_new_and_remaining(self):
        source, fork, plan, conflict = self.slugs
        source_status = self.ready(source)
        original = self.idle(source)
        require([entry['text'] for entry in original['entries'] if entry['kind'] == 'userMessage'] == [GOAL], 'new session did not contain exactly its original request')
        require(self.manifest(source)['creation']['goal_sha256'] == digest(GOAL), 'new-session goal digest changed')
        self.record('new session completed once', receiptId=source_status['receiptId'], goalSha256=digest(GOAL), invocations=self.count(source))

        self.browser.get(self.base + f'/{source}/')
        until(lambda: self.browser.find_element('css selector', '#fork-form [name="model"]').get_attribute('value'), seconds=30, interval=.1, label='fork settings')
        self.browser.find_element('id', 'fork-open').click()
        self.field('#fork-form [name="name"]', self.names[1])
        self.field('#fork-form [name="creationDate"]', self.date)
        fork_payload = {'name': self.names[1], 'creationDate': self.date, 'model': self.browser.find_element('css selector', '#fork-form [name="model"]').get_attribute('value'), 'reasoningEffort': self.browser.find_element('css selector', '#fork-form [name="effort"]').get_attribute('value')}
        self.hold(fork)
        self.submit('#fork-form', fork, f'/api/sessions/{source}/fork', 202)
        self.duplicate(fork, f'/api/sessions/{source}/fork', fork_payload)
        self.release(fork)
        self.finish_fork_and_remaining()

    def finish_fork_and_remaining(self):
        source, fork, plan, conflict = self.slugs
        self.ready(fork)
        manifest = self.manifest(fork)
        require(manifest['codex']['thread_id'] != self.results['threads'][source] and manifest['forked_from'] == source, 'fork did not preserve distinct destination/source identities')
        require(not manifest.get('repositories') and not manifest.get('artifacts'), 'fork copied repository or artifact ownership')
        source_messages = [entry['text'] for entry in self.idle(source)['entries'] if entry['kind'] == 'userMessage']
        require([entry['text'] for entry in self.idle(fork)['entries'] if entry['kind'] == 'userMessage'] == source_messages, 'fork submitted a new initial user turn')
        receipt, receipt_path = self.receipt(fork)
        evidence = json.loads(receipt_path.with_name(f'{fork}.{receipt["receiptId"]}.complete.json').read_bytes())
        require(evidence['sourceThreadId'] == self.results['threads'][source], 'fork completion proof lost its source thread')
        require(not (self.workspace / 'worktrees/.locks' / f'{fork}.fork.json').exists(), 'ready fork retained its incomplete journal')
        self.record('fork completed without a new turn', sourceThreadId=evidence['sourceThreadId'], invocations=self.count(fork))

        require(self.http(f'/codex/conversations/{source}/settings', {'collaborationMode': 'plan'})[0] == 200, 'unable to enter Plan mode')
        self.send(source, PLAN_REQUEST)
        planned = self.idle(source)
        plans = [entry for entry in planned['entries'] if entry['kind'] == 'plan' and entry.get('turnStatus') == 'completed' and entry.get('text', '').strip()]
        require(plans, 'model did not return a completed plan within the bounded fixture request')
        captured = plans[-1]
        self.browser.get(self.base + f'/{source}/')
        until(lambda: self.browser.find_element('id', 'plan-actions').is_displayed(), seconds=30, interval=.1, label='plan action panel')
        self.browser.find_element('id', 'plan-implement-new').click()
        self.field('#plan-session-form [name="name"]', self.names[2])
        self.field('#plan-session-form [name="creationDate"]', self.date)
        self.hold(plan)
        self.submit('#plan-session-form', plan, f'/api/sessions/{source}/implement-plan', 202)
        self.entered(plan)
        accepted, _ = self.receipt(plan)
        expected_goal = f'Implement the following approved plan from session {source}.\n\n{captured["text"]}'.strip(' \t\n\v\f\r\x00')
        require(accepted['validated'] and accepted['goal'] == expected_goal and accepted['request']['planTurnId'] == captured['turnId'] and accepted['request']['planSha256'] == digest(captured['text']), 'accepted plan snapshot differs from the displayed plan')
        require((accepted['model'], accepted['effort']) == (planned['model'], planned['reasoningEffort']), 'accepted plan settings changed')
        self.duplicate(plan, f'/api/sessions/{source}/implement-plan', {'action': 'new', 'name': self.names[2], 'creationDate': self.date, 'planText': captured['text'], 'planTurnId': captured['turnId'], 'planSha256': digest(captured['text']), 'model': accepted['model'], 'reasoningEffort': accepted['effort']})
        self.send(source, PLAN_REQUEST.replace('PLAN_ACCEPTED', 'NEWER_PLAN_ONLY'))
        newer = self.idle(source)
        newer_plans = [entry for entry in newer['entries'] if entry['kind'] == 'plan' and entry.get('turnStatus') == 'completed']
        require(newer_plans and digest(newer_plans[-1]['text']) != digest(captured['text']), 'source did not publish a different completed plan')
        self.stop()
        self.start(self.package)
        paused = self.status(plan)
        require(paused['state'] == 'paused' and self.count(plan) == 1, 'restart silently resumed or lost the paused plan')
        self.browser.get(self.base + f'/{plan}/')
        until(lambda: self.browser.find_element('id', 'creation-retry').is_displayed(), seconds=10, interval=.1, label='explicit retry control')
        source_link = self.browser.find_element('id', 'creation-source')
        require(source_link.is_displayed() and source_link.get_attribute('href') == self.base + f'/{source}/', 'uppercase/underscore source link is missing after interruption')
        require(self.http(f'/{source}/')[0] == 200, 'source recovery link does not work')
        time.sleep(2.2)
        require(self.count(plan) == 1, 'read-only page polling restarted the worker')
        require(self.http(f'/api/sessions/{plan}/creation/retry', {'receiptId': '0' * 64, 'attempt': paused['attempt']})[0] == 409, 'wrong retry receipt was accepted')
        self.browser.find_element('id', 'creation-retry').click()
        until(lambda: self.count(plan) == 2, seconds=30, interval=.1, label='explicit retry worker')
        require(self.http(f'/api/sessions/{plan}/creation/retry', {'receiptId': paused['receiptId'], 'attempt': paused['attempt']})[0] == 409, 'old retry attempt was accepted')
        self.release(plan)
        completed = self.ready(plan)
        implemented = self.idle(plan)
        require([entry['text'] for entry in implemented['entries'] if entry['kind'] == 'userMessage'] == [expected_goal], 'retry did not preserve the exact accepted plan')
        require((implemented['model'], implemented['reasoningEffort']) == (accepted['model'], accepted['effort']), 'plan destination changed captured settings')
        self.record('exact plan survived newer source and retry', receiptId=completed['receiptId'], attempt=completed['attempt'], planTurnId=captured['turnId'], planSha256=digest(captured['text']), goalSha256=digest(expected_goal), invocations=self.count(plan))

        self.passive_question(source, plan)
        self.rollback_conflict(source, conflict)

    def passive_question(self, source, destination, existing_turn=None):
        require(self.transcript(source).get('collaborationMode') == 'plan', 'blocking-question fixture source left Plan mode')
        self.browser.get(self.base + f'/{destination}/')
        require(self.browser.find_element('id', 'message-form').is_displayed(), 'completed destination is unavailable before the observer check')
        deadline = time.monotonic() + 180

        def remaining():
            seconds = deadline - time.monotonic()
            require(seconds > 0, 'blocking-question fixture exceeded its single 180s model deadline')
            return seconds

        def still_on_destination():
            require(urllib.parse.urlparse(self.browser.current_url).path == f'/{destination}/', 'browser visited the source before both passive snapshots')

        sent = {'turnId': existing_turn} if existing_turn else self.send(source, QUESTION_REQUEST)

        def pending_question():
            still_on_destination()
            entries = self.get_json(f'/codex/conversations/{source}/pending')
            if not entries:
                transcript = self.transcript(source)
                finished = [entry for entry in transcript['entries'] if entry.get('turnId') == sent['turnId'] and entry.get('turnStatus') in ('completed', 'failed', 'interrupted')]
                if transcript['status'] != 'active' and finished:
                    raise QuestionUnavailable('Question turn finished without blocking input (state ' + finished[-1]['turnStatus'] + ', mode ' + transcript.get('collaborationMode', 'unknown') + ').')
                return None
            require(len(entries) == 1, 'bounded question request produced more than one pending request')
            entry = entries[0]
            require(entry['kind'] == 'userInput' and entry['isBlocking'] and entry['authorityAvailable'], 'question lacks blocking interactive authority')
            require(entry['threadId'] == self.results['threads'][source], 'pending question belongs to another thread')
            questions = entry.get('questions', [])
            require(len(questions) == 1 and questions[0]['id'] == 'fixture_choice', 'model did not return the requested single question')
            require([option['label'] for option in questions[0].get('options', [])] == ['Alpha (Recommended)', 'Beta'], 'model did not return the requested two choices')
            return entry

        prompt = until(pending_question, seconds=remaining(), label='one real blocking question')

        def waiting_snapshot():
            still_on_destination()
            value = self.get_json(f'/codex/conversations/{source}/activity')
            require(value['threadId'] == self.results['threads'][source], 'passive activity belongs to another thread')
            return value if value['currentState'] == 'waiting' else None

        first = until(waiting_snapshot, seconds=min(15, remaining()), interval=.25, label='passive observer waiting state')
        require(remaining() > 3, 'question left no time for its held waiting interval')
        time.sleep(3)
        second = waiting_snapshot()
        require(second is not None and second.get('currentTurnId') == first.get('currentTurnId'), 'passive observer lost the held blocking wait')
        require(second.get('currentTurnId') == sent['turnId'], 'question observation changed the expected turn')
        observed_ms = second['observedAtMs'] - first['observedAtMs']
        waiting_ms = second['waitingMs'] + second['openWaitingMs'] - first['waitingMs'] - first['openWaitingMs']
        working_ms = second['workingMs'] - first['workingMs']
        require(observed_ms >= 2500 and waiting_ms >= 2500, 'passive waiting time did not advance across the three-second hold')
        require(abs(working_ms) <= 1000, 'working time continued during the blocking wait')
        require(pending_question()['id'] == prompt['id'], 'passive observation answered or replaced the question')
        self.record('passive blocking-question snapshots before source navigation', threadId=prompt['threadId'], turnId=sent['turnId'], promptId=prompt['id'], observedMs=observed_ms, waitingGrowthMs=waiting_ms, workingGrowthMs=working_ms)
        (self.root / 'question-checkpoint.json').write_text(json.dumps({'turnId': sent['turnId'], 'prompt': prompt, 'first': first, 'second': second}, indent=2) + '\n')

        self.browser.get(self.base + f'/{source}/')

        def question_form():
            forms = self.browser.find_elements('css selector', '.question-approval .input-wizard')
            return forms[0] if len(forms) == 1 and forms[0].is_displayed() else None

        until(question_form, seconds=min(30, remaining()), interval=.1, label='real question UI')
        # Choosing an answer renders a replacement form. Resolve each action in
        # the current DOM so a retained Selenium element cannot become stale.
        require(self.browser.execute_script('const input = document.querySelector(\'.question-approval .input-wizard input[name="answer-choice"][value="Alpha (Recommended)"]\'); if (!input) return false; input.click(); return true;'), 'question choice disappeared')
        def submit_current_form():
            return self.browser.execute_script('const form = document.querySelector(".question-approval .input-wizard"); if (!form) return false; const buttons = [...form.querySelectorAll("button")].filter(button => button.textContent.trim() === "Submit answers" && !button.disabled); if (buttons.length !== 1) return false; buttons[0].click(); return true;')
        until(submit_current_form, seconds=min(10, remaining()), interval=.1, label='current question submit action')

        def answered():
            transcript = self.transcript(source)
            if transcript['status'] == 'active' or self.get_json(f'/codex/conversations/{source}/pending'):
                return None
            replies = [entry for entry in transcript['entries'] if entry['kind'] == 'agentMessage' and entry.get('text', '').strip() == 'QUESTION_ANSWERED']
            require(len(replies) == 1 and replies[0].get('turnId') == second.get('currentTurnId'), 'question answer did not finish the same bounded turn')
            value = self.get_json(f'/codex/conversations/{source}/activity')
            return value if value['currentState'] == 'idle' else None

        closed = until(answered, seconds=remaining(), interval=.5, label='answered question and closed wait')
        closed_wait_ms = closed['waitingMs'] - first['waitingMs']
        require(closed_wait_ms >= waiting_ms - 1000, 'answered question did not retain the observed wait as closed waiting time')
        # Idle begins its own trailing wait; openWaitingMs need not become zero.
        self.record('passive observer retained a blocking question for browser response', threadId=prompt['threadId'], observedMs=observed_ms, waitingGrowthMs=waiting_ms, workingGrowthMs=working_ms, closedWaitingGrowthMs=closed_wait_ms, finalState=closed['currentState'])

    def rollback_conflict(self, source, conflict):
        self.hold(conflict)
        original_goal = GOAL + ' This is the earlier head request.'
        form = {'creation_date': self.date, 'name': self.names[3], 'goal': original_goal}
        require(self.http('/sessions', form, form=True)[0] == 303, 'head conflict fixture was not accepted')
        self.entered(conflict)
        self.stop()
        accepted, receipt_path = self.receipt(conflict)
        binding = receipt_path.with_name(f'{conflict}.{accepted["receiptId"]}.complete.json.request')
        require(not binding.exists(), 'rollback conflict started after the CLI binding boundary')
        receipts = {slug: digest(self.receipt(slug)[1].read_bytes()) for slug in self.slugs}
        manifests = {slug: digest((self.workspace / 'work' / slug / 'portal.yml').read_bytes()) for slug in self.slugs[:3]}
        self.start(self.previous)
        for slug in self.slugs[:3]:
            require(self.http(f'/{slug}/')[0] == 200, 'previous package cannot read a completed canonical session')
            require(self.transcript(slug)['threadId'] == self.results['threads'][slug], 'rollback changed canonical conversation identity')
        self.command([self.previous / 'bin/workspace-portal', 'validate', '--workspace', self.workspace], 'previous-validate')
        source_receipt, _ = self.receipt(source)
        goal_file = self.root / 'original-goal.txt'
        goal_file.write_text(GOAL)
        replay = json.loads(self.command(self.cli(self.previous) + ['start', source, '--as-is', '--exclusive', '--no-attach', '--goal-file', goal_file, '--json', '--model', source_receipt['model'], '--effort', source_receipt['effort']], 'previous-replay', timeout=120))
        require(replay['threadId'] == self.results['threads'][source], 'previous CLI replay replaced the original thread')
        require(len([entry for entry in self.transcript(source)['entries'] if entry['kind'] == 'userMessage' and entry['text'] == GOAL]) == 1, 'previous replay duplicated the initial request')
        # The old package runs its unmodified synchronous start path. No receipt
        # flags are passed and the head-only delay wrapper is intentionally absent.
        old_goal = self.root / 'base-goal.txt'
        old_goal.write_text(GOAL + ' This session was independently created by the previous package.')
        created = json.loads(self.command(self.cli(self.previous) + ['start', conflict, '--as-is', '--exclusive', '--no-attach', '--goal-file', old_goal, '--json', '--model', self.defaults['model'], '--effort', self.defaults['reasoningEffort']], 'previous-create-conflict', timeout=150))
        self.results['threads'][conflict] = created['threadId']
        require(len(set(self.results['threads'].values())) == 4, 'fixture did not retain exactly four distinct conversations')
        self.idle(conflict)
        for slug, expected in receipts.items():
            require(digest(self.receipt(slug)[1].read_bytes()) == expected, 'previous package rewrote additive creation receipt state')
        for slug, expected in manifests.items():
            require(digest((self.workspace / 'work' / slug / 'portal.yml').read_bytes()) == expected, 'rollback/replay rewrote a ready canonical manifest')
        require(not binding.exists(), 'previous package synthesized a head receipt binding')
        self.stop()
        self.start(self.package)
        reconciled = self.status(conflict)
        require(reconciled['state'] == 'conflict' and reconciled['receiptId'] == accepted['receiptId'] and reconciled['attempt'] == accepted['attempt'], 'rollforward did not retain the conflicting request identity')
        require(reconciled['canonicalUrl'] == f'/{conflict}/', 'conflict does not expose its canonical session')
        self.browser.get(self.base + f'/{conflict}/')
        require(self.browser.find_element('id', 'message-form').is_displayed(), 'conflict shadows normal canonical controls')
        require('This session was created separately.' in self.browser.find_element('tag name', 'body').text, 'canonical conflict notice is absent')
        require(self.transcript(conflict)['threadId'] == created['threadId'], 'conflict adopted another conversation')
        require(self.http(f'/api/sessions/{conflict}/creation/retry', {'receiptId': accepted['receiptId'], 'attempt': accepted['attempt']})[0] == 409, 'rollforward retried the conflicting request')
        require(not binding.exists() and not binding.with_suffix('').exists(), 'conflict fabricated receipt completion evidence')
        for slug in self.slugs[:3]:
            require(self.status(slug)['state'] == 'ready' and self.transcript(slug)['threadId'] == self.results['threads'][slug], 'rollforward changed a completed creation')
        self.command([self.package / 'bin/workspace-portal', 'validate', '--workspace', self.workspace], 'head-validate')
        self.record('packaged head-base-head conflict and normal reads', receiptId=accepted['receiptId'], canonicalThreadId=created['threadId'], state=reconciled['state'])

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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true', help='run the explicitly authorized live acceptance against ACCEPT_PACKAGE')
    resume = parser.add_mutually_exclusive_group()
    resume.add_argument('--resume-initial', metavar='ROOT', help='retry the same initial receipt after inspecting a failed fixture with no recorded thread')
    resume.add_argument('--resume-fork', metavar='ROOT', help='restore the existing source terminal and retry its accepted fork after diagnosis')
    resume.add_argument('--resume-plan', metavar='ROOT', help='verify the repaired package against the existing completed plan, then run the remaining question and rollback checks')
    resume.add_argument('--resume-remaining', metavar='ROOT', help='establish live Plan mode for the single authorized question retry, then run fourth-thread rollback')
    resume.add_argument('--resume-question', metavar='ROOT', help='answer only an existing blocking question, then run fourth-thread rollback')
    resume.add_argument('--resume-rollback', metavar='ROOT', help='interrupt the explicitly authorized stranded fixture question, then run fourth-thread rollback')
    parser.add_argument('--question-turn', help='exact previously observed turn for --resume-question; never sends another question')
    args = parser.parse_args()
    if not args.run:
        parser.error('no live action taken; pass --run after package review and root authorization')
    os.umask(0o077)
    def terminated(_signal, _frame):
        raise TimeoutError('acceptance interrupted by its external time limit')
    signal.signal(signal.SIGTERM, terminated)
    require(not (args.resume_question or args.resume_rollback) or args.question_turn, 'question recovery requires the exact existing --question-turn')
    fixture = Fixture(args.resume_initial or args.resume_fork or args.resume_plan or args.resume_remaining or args.resume_question or args.resume_rollback, allow_package_change=bool(args.resume_plan or args.resume_remaining or args.resume_question or args.resume_rollback))
    try:
        if args.resume_initial:
            fixture.resume_initial_creation()
        elif args.resume_fork:
            fixture.resume_fork_creation()
        elif args.resume_plan:
            fixture.resume_completed_plan()
        elif args.resume_remaining:
            fixture.resume_remaining_checks()
        elif args.resume_question:
            fixture.resume_pending_question(args.question_turn)
        elif args.resume_rollback:
            fixture.resume_rollback_after_question(args.question_turn)
        else:
            fixture.run()
        fixture.results['outcome'] = ('creation and rollback passed; real question answer subcheck unverified'
                                      if any(check.get('answerVerified') is False for check in fixture.results['checks']) else 'passed')
    except BaseException as error:
        fixture.results['outcome'] = 'failed'
        fixture.results['failure'] = str(error)
        raise
    finally:
        fixture.close()


if __name__ == '__main__':
    main()
