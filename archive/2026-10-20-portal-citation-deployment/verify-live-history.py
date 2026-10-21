import hashlib
import http.client
import json
from pathlib import Path
import socket
import time
from urllib.parse import quote

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
OUT = ROOT / 'work/2026-10-20-portal-citation-deployment'
EVIDENCE = json.loads((ROOT / 'work/2026-10-20-portal-citation-investigation/evidence.json').read_text())


class PortalConnection(http.client.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(45)
        self.sock.connect('/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock')


def read_page(cursor=''):
    connection = PortalConnection('localhost')
    try:
        path = '/api/sessions/2026-10-19-dynamic-python-api-client/thread/page'
        if cursor:
            path += '?cursor=' + quote(cursor, safe='')
        connection.request('GET', path)
        response = connection.getresponse()
        payload = response.read()
        assert response.status == 200, (response.status, payload[:200])
        return json.loads(payload)
    finally:
        connection.close()


cursor = ''
for page_number in range(40):
    page = read_page(cursor)
    assert page['threadId'] == EVIDENCE['threadId']
    found = next((entry for entry in page['entries'] if entry.get('itemId') == EVIDENCE['itemId']), None)
    if found:
        # Retry this same historical page after the passive resolver finishes.
        for attempt in range(30):
            if found.get('citations') and not found.get('citationsPending'):
                break
            time.sleep(1)
            found = next(entry for entry in read_page(cursor)['entries'] if entry.get('itemId') == EVIDENCE['itemId'])
        assert found['text'] == EVIDENCE['recordedMessage']['text'], 'recorded response changed'
        assert '\ue200cite' not in found['html'], 'raw citation token in rendered HTML'
        assert '<table>' in found['html'] and '<code>haveapi-client</code>' in found['html']
        sources = [source for span in found['citations'] for source in span.get('sources', [])]
        assert {source['url'] for source in sources} == {
            'https://pypi.org/help/',
            'https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/',
        }
        assert all(source.get('title') and source.get('number') for source in sources)
        result = {
            'result': 'passed', 'threadId': page['threadId'], 'itemId': found['itemId'],
            'pageNumber': page_number + 1, 'historicalCursor': bool(cursor),
            'rawTextUnchanged': True, 'rawTextSha256': hashlib.sha256(found['text'].encode()).hexdigest(),
            'htmlSha256': hashlib.sha256(found['html'].encode()).hexdigest(),
            'citationSources': sources, 'readOnlyRequests': True,
        }
        (OUT / 'rebase-live-history-result.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps(result))
        break
    assert page.get('hasOlder') and page.get('olderCursor'), 'original response absent from retained history'
    cursor = page['olderCursor']
else:
    raise AssertionError('original response not found in bounded page traversal')
