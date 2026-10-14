#!/usr/bin/env python3
import os
import pathlib
import subprocess

WORKSPACE = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-05-network-ipv4-left-counter'
ROOT = WORKSPACE / 'worktrees' / SLUG / 'vpsadmin'
HEAD = 'be136b6c00f03b85b7a12cc57550b4a1394a94a7'
BRANCH = SLUG
PATHS = {
    'api/lib/vpsadmin/api/resources/network.rb',
    'api/lib/vpsadmin/api/resources/ip_address.rb',
    'api/spec/api/resources/network_read_spec.rb',
    'api/spec/api/resources/ip_address_spec.rb',
    'api/spec/api/resources/host_ip_address_spec.rb',
    'api/spec/api/resources/network_interface_spec.rb',
    'api/spec/api/resources/ip_address_assignment_spec.rb',
    'docs/ip-locking.md',
}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


assert os.environ.get('DEV_SESSION_SLUG') == SLUG, 'Session marker mismatch'
assert os.environ.get('DEV_SESSION_WORKSPACE') == str(WORKSPACE), 'Workspace marker mismatch'
assert git('rev-parse', 'HEAD').decode().strip() == HEAD, 'Source HEAD changed'
assert git('branch', '--show-current').decode().strip() == BRANCH, 'Source branch changed'
entries = git('status', '--porcelain=v1', '-z').decode().split('\0')
changed = set()
for entry in filter(None, entries):
    assert entry[:3] == ' M ', f'Unexpected staged/untracked/status entry: {entry}'
    changed.add(entry[3:])
assert changed == PATHS, f'Unexpected source scope: {sorted(changed)}'
assert not git('diff', '--name-only', HEAD, '--', 'api/db/schema.rb', 'api/db/migrate').strip(), 'Schema/migration changed'
assert not (ROOT / 'api/config/database.yml').exists(), 'Configured database refused'
assert 'DATABASE_URL' not in os.environ, 'Explicit database URL refused'
print(f'Guard passed: {BRANCH} at {HEAD}, exactly {len(PATHS)} owned working paths; migration/schema unchanged')
