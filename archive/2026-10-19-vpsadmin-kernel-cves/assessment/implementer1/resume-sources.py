import concurrent.futures, datetime, hashlib, json, pathlib, urllib.request

P = pathlib.Path('assessment/implementer1')
ids = json.load(open('assessment/packages.json'))['groups']['implementer1']
rs = {r['cve']: r for r in json.load(open('research/cve-evidence/range-records.json'))}

def get(c):
    r = rs[c]
    p = P / 'primary' / c
    p.mkdir(parents=True, exist_ok=True)
    record = pathlib.Path('research/cve-evidence/records') / (c + '.json')
    (p / 'record.json').write_bytes(record.read_bytes())
    dest = p / 'stable-fix.patch'
    sha = r['fixes'][0]['sha']
    url = 'https://github.com/gregkh/linux/commit/' + sha + '.patch'
    method = 'existing local object snapshot'
    if not dest.exists():
        req = urllib.request.Request(url, headers={'User-Agent': 'vpsFree-security-assessment/1.0'})
        raw = urllib.request.urlopen(req, timeout=30).read()
        if not raw.startswith(('From ' + sha).encode()):
            raise ValueError('Non-patch or wrong revision response for ' + c)
        dest.write_bytes(raw)
        method = 'exact stable-maintainer mirror HTTP patch'
    return {'cve': c, 'stable_fix': sha, 'primary_url': 'https://git.kernel.org/stable/c/' + sha,
            'snapshot_url': url, 'method': method, 'retrieved_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'sha256': hashlib.sha256(dest.read_bytes()).hexdigest(), 'file': str(dest)}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    out = list(ex.map(get, ids))
(P / 'fix-source-manifest.json').write_text(json.dumps(out, indent=2) + '\n')
rev = '1dfea587406b7dd79973831d1677fb2418e5e9aa'
sources = [{'path': str(f.relative_to(P / 'source/linux')), 'revision': rev,
            'sha256': hashlib.sha256(f.read_bytes()).hexdigest(),
            'url': 'https://github.com/vpsfreecz/linux/blob/' + rev + '/' + str(f.relative_to(P / 'source/linux'))}
           for f in sorted((P / 'source/linux').rglob('*')) if f.is_file()]
(P / 'source-manifest.json').write_text(json.dumps({'linux_revision': rev, 'sources': sources}, indent=2) + '\n')
print('All', len(out), 'exact fix snapshots and', len(sources), 'current Linux source files available')
