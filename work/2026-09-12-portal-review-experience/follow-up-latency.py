#!/usr/bin/env python3
"""Bounded post-deployment acceptance; never print or persist authentication data.

Run only after review and deployment. History/comparison GETs write the portal's
normal private review descriptors/cache; this script never changes Git refs,
working files, manifests, conversations, queues, or service state.
"""
import argparse
import base64
import hashlib
import http.client
import json
import re
import signal
import socket
import ssl
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True)
parser.add_argument('--samples', type=int, default=5, choices=range(3, 8))
parser.add_argument('--require-improvement', action='store_true')
args = parser.parse_args()
BASE = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
SLUG = '2026-09-12-portal-review-experience'
WORKSPACE = '/home/aither/workspace/ai/vpsfree.cz'
SERVICE = 'workspace-portal@vpsfree-cz.service'
REPOSITORIES = ('codex-web', 'dev-workspace', 'vpsfree-dev-workspace', 'workspace')
BASELINE_DIRECT_MS = 615.8
API = '/api/sessions/' + SLUG + '/repository-'
MAX_RESPONSE = 16 * 1024 * 1024
started = time.monotonic()
deadline = started + 120
observations = []
heads = {}
result = {
    'baselineDirectStateMedianMs': BASELINE_DIRECT_MS,
    'baselineNote': 'Before changes, direct repository-state samples were 618.6, 615.8, 577.7 ms. Cold-cache status is not asserted for this run.',
    'observations': observations,
    'heads': heads,
}

def remaining():
    budget = deadline - time.monotonic()
    if budget <= 0:
        raise TimeoutError('measurement deadline')
    return min(10, budget)

def review_id(name):
    return hashlib.sha256(name.encode()).hexdigest()[:32]

def query(values):
    return urllib.parse.urlencode(values, doseq=True)

class UnixHTTP(http.client.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect(portal_socket)

def request(transport, operation, path):
    sample_start = time.monotonic()
    if transport == 'direct':
        client = UnixHTTP(urllib.parse.urlsplit(BASE).hostname, timeout=remaining())
        try:
            client.request('GET', path)
            response = client.getresponse()
            status = response.status
            data = response.read(MAX_RESPONSE + 1)
        finally:
            client.close()
    else:
        # Credentials stay in this process and are never included in a URL,
        # command argument, output object, exception text, or temporary file.
        message = urllib.request.Request(BASE + path, headers={'Authorization': authorization})
        try:
            response = urllib.request.urlopen(message, context=tls, timeout=remaining())
        except urllib.error.HTTPError as error:
            response = error
        with response:
            status = response.status
            data = response.read(MAX_RESPONSE + 1)
    observations.append({'transport': transport, 'operation': operation, 'status': status,
                         'ms': round((time.monotonic() - sample_start) * 1000, 2), 'bytes': len(data)})
    if len(data) > MAX_RESPONSE:
        raise ValueError('response cap exceeded')
    if status != 200:
        raise RuntimeError('unexpected HTTP status')
    return json.loads(data)

def measure(transport):
    for _ in range(3):
        request(transport, 'health', '/healthz')
    for _ in range(args.samples):
        payload = request(transport, 'registered-state', API + 'state?' + query({'repository': review_id('dev-workspace')}))
        if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', payload.get('head', '')):
            raise ValueError('invalid state payload')
    for _ in range(3):
        payload = request(transport, 'four-repository-states', API + 'states?' + query({'repository': [review_id(name) for name in REPOSITORIES]}))
        rows = payload.get('repositories', [])
        if len(rows) != len(REPOSITORIES):
            raise ValueError('incomplete states batch')
        for name in REPOSITORIES:
            row = next((item for item in rows if item.get('repository') == review_id(name)), {})
            if 'error' in row or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', row.get('head', '')):
                raise ValueError('repository state unavailable')
            heads[name] = row['head']
    payload = request(transport, 'four-initial-histories', API + 'histories?' + query({'repository': [review_id(name) for name in REPOSITORIES]}))
    rows = payload.get('repositories', [])
    if len(rows) != len(REPOSITORIES) or any('error' in row for row in rows):
        raise ValueError('repository history unavailable')
    selected = next(item for item in rows if item.get('repository') == review_id('dev-workspace'))
    if not re.fullmatch(r'[0-9a-f]{32}', selected.get('review', '')):
        raise ValueError('durable review missing')
    comparison_query = {'repository': review_id('dev-workspace'), 'review': selected['review']}
    branch = request(transport, 'branch-with-first-preview', API + 'comparison?' + query(comparison_query))
    if branch.get('review') != selected['review'] or branch.get('pair', {}).get('head') != selected.get('pair', {}).get('head'):
        raise ValueError('comparison revisions changed')
    if branch.get('files') and not branch.get('preview'):
        raise ValueError('initial branch preview unavailable')
    commits = selected.get('history', {}).get('commits', [])
    if not commits:
        raise ValueError('fixture feature commits missing')
    comparison_query['commit'] = commits[0]['sha']
    for index in range(3):
        commit = request(transport, 'commit-first-open' if index == 0 else 'commit-repeat-open', API + 'comparison?' + query(comparison_query))
        if commit.get('commit', {}).get('sha') != commits[0]['sha'] or commit.get('historyHead') != selected['pair']['head']:
            raise ValueError('commit comparison identity changed')
        if commit.get('files') and not commit.get('preview'):
            raise ValueError('initial commit preview unavailable')
    files = branch.get('files', [])[:4]
    if files:
        payload = request(transport, 'visible-file-batch', API + 'files?' + query({'repository': review_id('dev-workspace'), 'snapshot': branch['snapshot'], 'file': [item['id'] for item in files]}))
        rows = payload.get('files', [])
        if len(rows) != len(files) or any('error' in row or 'content' not in row for row in rows):
            raise ValueError('file batch unavailable')

def expire_measurement(_signal, _frame):
    raise TimeoutError('measurement deadline')

signal.signal(signal.SIGALRM, expire_measurement)
signal.setitimer(signal.ITIMER_REAL, 120)
exit_status = 0
try:
    pid_text = subprocess.run(['systemctl', '--user', 'show', SERVICE, '-p', 'MainPID', '--value'],
                              capture_output=True, text=True, check=True, timeout=remaining()).stdout.strip()
    if not pid_text.isdecimal() or int(pid_text) <= 1:
        raise ValueError('portal service is not running')
    command = Path('/proc/' + pid_text + '/cmdline').read_bytes().decode().split('\0')
    if '--workspace' not in command or command[command.index('--workspace') + 1] != WORKSPACE:
        raise ValueError('service workspace mismatch')
    portal_socket = command[command.index('--unix-socket') + 1]
    if not Path(portal_socket).is_socket():
        raise ValueError('portal socket missing')
    result['portalExecutable'] = command[0]
    result['portalPID'] = int(pid_text)
    tls = ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
    password = Path('/var/lib/dev-workspaces/password/password').read_text().strip()
    authorization = 'Basic ' + base64.b64encode(('aither:' + password).encode()).decode()
    del password
    for transport in ('direct', 'https'):
        measure(transport)
    grouped = {}
    for item in observations:
        grouped.setdefault((item['transport'], item['operation']), []).append(item['ms'])
    result['summaries'] = [{'transport': transport, 'operation': operation, 'samples': len(values),
                            'medianMs': round(statistics.median(values), 2), 'minMs': min(values), 'maxMs': max(values)}
                           for (transport, operation), values in grouped.items()]
    direct_median = statistics.median(grouped[('direct', 'registered-state')])
    improvement = 100 * (1 - direct_median / BASELINE_DIRECT_MS)
    result['directMetadataImprovementPercent'] = round(improvement, 2)
    result['meets75PercentImprovement'] = improvement >= 75
    result['passed'] = True
    if args.require_improvement and improvement < 75:
        result['passed'] = False
        exit_status = 1
except Exception as error:
    # Do not stringify exceptions: HTTP library exceptions may include request
    # metadata. The error class and completed bounded observations suffice.
    result['passed'] = False
    result['failureClass'] = type(error).__name__
    exit_status = 1
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    result['elapsedSeconds'] = round(time.monotonic() - started, 2)
    encoded = json.dumps(result, indent=2) + '\n'
    output = Path(args.output)
    with output.open('x') as stream:
        stream.write(encoded)
    print(encoded, end='')
sys.exit(exit_status)
