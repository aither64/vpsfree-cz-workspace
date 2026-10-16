from pathlib import Path
import json
import subprocess

record = Path(__file__).resolve().parent
root = record.parents[2]
slug = record.parent.name
items = json.loads((record / 'inventory.json').read_text())
for item in items:
    repo = root / 'worktrees' / slug / item['project']
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=repo)
    assert git('rev-parse', 'HEAD').decode().strip() == item['before']
    assert not git('status', '--porcelain=v1')
    if item['project'] == 'vpsadminos':
        subprocess.run(['overcommit', '--sign'], cwd=repo, check=True)
    with (record / (item['project'] + '-declared-restore.log')).open('w') as log:
        result = subprocess.run(
            ['git', 'rebase', '--onto', item['restore_to'], item['before']],
            cwd=repo, stdout=log, stderr=subprocess.STDOUT,
        )
    (record / (item['project'] + '-declared-restore.status')).write_text(str(result.returncode) + '\n')
    print(item['project'], result.returncode, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    assert git('rev-parse', 'HEAD').decode().strip() == item['restore_to']
    assert not git('status', '--porcelain=v1')
    for path in item['paths']:
        assert (repo / path).read_bytes() == git('show', item['restore_to'] + ':' + path)
    print(item['restore_to'], flush=True)
(record / 'restoration.status').write_text('0\n')
