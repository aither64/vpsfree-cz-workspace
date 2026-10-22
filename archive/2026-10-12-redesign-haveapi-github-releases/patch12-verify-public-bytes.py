import base64
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import urllib.request

records = pathlib.Path(sys.argv[1])
originals = records / 'patch12-tag-artifacts'
manifest = json.loads((originals / 'release-manifest.json').read_text())
helper = json.loads((records / 'patch12-destination-helper-receipt.json').read_text())
assert manifest['source'] == '355c2990a4bfd3940d3234cb2077ad0127f43551'
assert manifest['run_id'] == '39313082898' and manifest['version'] == '0.29.12'
proof = {'source': manifest['source'], 'version': manifest['version'], 'run_id': manifest['run_id']}

def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        assert response.status == 200, (url, response.status)
        return response.read()

def registry_json(url):
    return json.loads(fetch(url))

packages = []
for name in ('haveapi', 'haveapi-client', 'haveapi-go-client'):
    metadata_url = f'https://rubygems.org/api/v2/rubygems/{name}/versions/0.29.12.json'
    metadata = registry_json(metadata_url)
    filename = f'{name}-0.29.12.gem'
    wanted = manifest['files'][filename]
    assert metadata['sha'] == wanted
    download = f'https://rubygems.org/downloads/{filename}'
    actual = hashlib.sha256(fetch(download)).hexdigest()
    assert actual == wanted, name
    packages.append({'name': name, 'version': '0.29.12', 'url': metadata_url, 'download': download, 'sha256': actual})
    print('Published bytes match original:', filename, flush=True)

npm_url = 'https://registry.npmjs.org/haveapi-client/0.29.12'
npm = registry_json(npm_url)
assert (npm['name'], npm['version']) == ('haveapi-client', '0.29.12')
repository = npm['repository']['url']
assert repository.removeprefix('git+').removesuffix('.git') == 'https://github.com/vpsfreecz/haveapi', repository
npm_filename = 'haveapi-client-0.29.12.tgz'
npm_original = (originals / npm_filename).read_bytes()
wanted_integrity = 'sha512-' + base64.b64encode(hashlib.sha512(npm_original).digest()).decode()
assert wanted_integrity in npm['dist']['integrity'].split()
assert npm['dist']['tarball'] == 'https://registry.npmjs.org/haveapi-client/-/haveapi-client-0.29.12.tgz'
npm_hash = hashlib.sha256(fetch(npm['dist']['tarball'])).hexdigest()
assert npm_hash == manifest['files'][npm_filename]
latest = registry_json('https://registry.npmjs.org/haveapi-client/latest')['version']
assert latest == '0.29.12', latest
proof['packages'] = packages
proof['npm'] = {'url': npm_url, 'version': npm['version'], 'repository': repository, 'latest': latest, 'sha256': npm_hash, 'integrity': wanted_integrity}
print('Published npm bytes, repository URL and latest tag match', flush=True)

release = json.loads((records / 'patch12-public-github-release.json').read_text())
assert not release['draft'] and not release['prerelease'] and release['tag_name'] == 'v0.29.12'
assert release['published_at']
expected_files = dict(manifest['files'])
expected_files['release-manifest.json'] = hashlib.sha256((originals / 'release-manifest.json').read_bytes()).hexdigest()
assert set(a['name'] for a in release['assets']) == set(expected_files)
assert release['body'].strip() == (originals / 'release-notes.md').read_text().strip()
with tempfile.TemporaryDirectory(prefix='haveapi-0.29.12-public-assets-') as directory:
    subprocess.run(['gh', 'release', 'download', 'v0.29.12', '--repo', 'vpsfreecz/haveapi', '--dir', directory], check=True)
    for name, wanted in expected_files.items():
        assert hashlib.sha256((pathlib.Path(directory) / name).read_bytes()).hexdigest() == wanted, name
proof['github'] = {'id': release['id'], 'url': release['html_url'], 'published_at': release['published_at'], 'draft': False, 'asset_hashes': expected_files}
print('All public GitHub asset bytes match original files and manifest', flush=True)

packagist_url = 'https://repo.packagist.org/p2/haveapi/client.json'
packagist = registry_json(packagist_url)
entries = packagist['packages']['haveapi/client']
entry = next(v for v in entries if v['version'].lstrip('v') == '0.29.12')
assert entry['source']['reference'] == helper['php_commit']
assert entry['dist']['reference'] == helper['php_commit']
proof['php'] = {'commit': helper['php_commit'], 'snapshot_and_source_match': helper['php_snapshot_and_source_match'], 'packagist': packagist_url, 'version': entry['version'], 'indexed_reference': entry['source']['reference']}
proof['all_checks_passed'] = True
(records / 'patch12-publication-verification.json').write_text(json.dumps(proof, indent=2) + '\n')
print('Packagist indexed 0.29.12 at verified PHP commit', helper['php_commit'], flush=True)
print('All publication destinations verified', flush=True)
